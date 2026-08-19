"""Offline split, balance, noise, and shortcut diagnostics."""

from __future__ import annotations

import hashlib
import math
import re
from collections import Counter, defaultdict
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from .canonical import sha256_json
from .config import FrozenConfig, STRUCTURES
from .generator import Corpus, DeterministicTokenizer, RELATION_CODE, STYLES


WORD_RE = re.compile(r"[A-Za-z0-9]+")


def normalized_text(text: str) -> str:
    return " ".join(text.lower().split())


def ngrams(text: str, width: int = 5) -> set:
    text = normalized_text(text)
    if len(text) < width:
        return {text}
    return {text[index : index + width] for index in range(len(text) - width + 1)}


def jaccard(left: set, right: set) -> float:
    union = left | right
    return len(left & right) / float(len(union) or 1)


def split_leakage_report(corpus: Corpus) -> Dict[str, Any]:
    """Check family blocking and exact/near duplicate report text."""

    family_splits: Dict[str, set] = defaultdict(set)
    origin_splits: Dict[str, set] = defaultdict(set)
    for row in corpus.split_index:
        family_splits[row["proposition_family_id"]].add(row["split"])
        origin_splits[row["origin_family_id"]].add(row["split"])
    cross_family = sorted(key for key, values in family_splits.items() if len(values) > 1)
    cross_origin = sorted(key for key, values in origin_splits.items() if len(values) > 1)
    records = corpus.reports
    exact_cross_split: List[Tuple[str, str]] = []
    near_cross_split: List[Tuple[str, str, float]] = []
    split_by_prop = {row["proposition_family_id"]: row["split"] for row in corpus.split_index}
    normalized = {report["report_id"]: normalized_text(report["text"]) for report in records}
    char_grams = {report["report_id"]: ngrams(report["text"]) for report in records}
    word_sets = {report["report_id"]: set(WORD_RE.findall(normalized[report["report_id"]])) for report in records}
    for left_index, left in enumerate(records):
        left_split = split_by_prop.get(left["proposition_family_id"])
        for right in records[left_index + 1 :]:
            right_split = split_by_prop.get(right["proposition_family_id"])
            if left_split == right_split:
                continue
            if normalized[left["report_id"]] == normalized[right["report_id"]]:
                exact_cross_split.append((left["report_id"], right["report_id"]))
            # Token-set blocking keeps the offline precheck tractable for the
            # protocol-sized synthetic inventory. The final lock still needs
            # the independently implemented exhaustive character/token probe.
            word_overlap = jaccard(word_sets[left["report_id"]], word_sets[right["report_id"]])
            if word_overlap < 0.55:
                continue
            overlap = jaccard(char_grams[left["report_id"]], char_grams[right["report_id"]])
            if overlap >= 0.80:
                near_cross_split.append((left["report_id"], right["report_id"], overlap))
    return {
        # This blocked token-set/character-gram scan is deliberately only a
        # cheap precheck. It is never an authorizing leakage clearance.
        "status": "precheck_pass" if not cross_family and not cross_origin and not exact_cross_split and not near_cross_split else "precheck_fail",
        "clearance_status": "unresolved",
        "authoritative": False,
        "probe": "blocked_token_set_character_ngram_precheck",
        "cross_split_proposition_families": cross_family,
        "cross_split_origin_families": cross_origin,
        "cross_split_exact_text_pairs": exact_cross_split,
        "cross_split_near_text_pairs_at_or_above_0.80": near_cross_split,
        "thresholds": {"exact": 0, "near_jaccard": 0.80},
    }


def balance_report(corpus: Corpus) -> Dict[str, Any]:
    """Summarize structure/domain/style/position counts without inferential claims."""

    gold_by_bundle = {record["bundle_id"]: record for record in corpus.bundles_gold}
    reports_by_id = {record["report_id"]: record for record in corpus.reports}
    counts = Counter()
    for public in corpus.bundles_public:
        gold = gold_by_bundle[public["bundle_id"]]
        for position, report_id in enumerate(public["report_order"]):
            report = reports_by_id[report_id]
            counts[(gold["split"], gold["origin_structure"], report["style"], position)] += 1
    return {
        "rows": [
            {
                "split": split,
                "origin_structure": structure,
                "style": style,
                "position": position,
                "count": counts[(split, structure, style, position)],
            }
            for split in ("dev", "pilot", "primary", "stress")
            for structure in STRUCTURES
            for style in STYLES
            for position in range(6)
            if counts[(split, structure, style, position)]
        ],
        "condition_invariant_order": True,
        "interpretation": "descriptive control inventory; no balance result is an efficacy result",
    }


def surface_only_nearest_centroid(corpus: Corpus) -> Dict[str, Any]:
    """A transparent lexical probe for structure leakage.

    This is not a trained classifier and is not a replacement for the
    preregistered blocked TF-IDF probe.  It is useful as a deterministic smoke
    diagnostic before external ML dependencies are introduced.
    """

    gold_by_bundle = {record["bundle_id"]: record for record in corpus.bundles_gold}
    reports_by_id = {record["report_id"]: record for record in corpus.reports}
    per_structure: Dict[str, Counter] = {structure: Counter() for structure in STRUCTURES}
    bundle_tokens: Dict[str, Counter] = {}
    for public in corpus.bundles_public:
        tokens = Counter()
        for report_id in public["report_order"]:
            tokens.update(WORD_RE.findall(reports_by_id[report_id]["text"].lower()))
        bundle_tokens[public["bundle_id"]] = tokens
        per_structure[gold_by_bundle[public["bundle_id"]]["origin_structure"]].update(tokens)
    predictions: List[Tuple[str, str, str]] = []
    for bundle_id, tokens in bundle_tokens.items():
        scores = {
            structure: sum(min(count, per_structure[structure][token]) for token, count in tokens.items())
            for structure in STRUCTURES
        }
        predicted = max(STRUCTURES, key=lambda structure: (scores[structure], structure))
        actual = gold_by_bundle[bundle_id]["origin_structure"]
        predictions.append((bundle_id, actual, predicted))
    accuracy = sum(actual == predicted for _, actual, predicted in predictions) / float(len(predictions) or 1)
    return {
        "probe": "surface_only_nearest_centroid_smoke",
        "accuracy": accuracy,
        "n": len(predictions),
        "predictions": predictions,
        "status": "descriptive_smoke_only",
        "required_full_probe": "blocked character/token TF-IDF classifier with Wilson CI before primary lock",
    }


def metadata_only_counter(relation_codes: Sequence[str]) -> Dict[str, Any]:
    """Apply the public relation-code rule without report prose."""

    independent_count = sum(code == "INDP" for code in relation_codes)
    dependent = sum(code == "DPND" for code in relation_codes)
    unknown = sum(code == "UNKN" for code in relation_codes)
    return {
        "independent_as_stipulated_code_count": independent_count,
        "independent_code_present": independent_count > 0,
        "dependent_code_count": dependent,
        "unknown_code_count": unknown,
        "rule": "INDP is countable distinct-origin cue; DPND does not add a path; UNKN remains unresolved",
        "interpretation": "direct-code diagnostic only; not semantic evidence integration",
    }


def field_only_diagnostic(relation_codes: Sequence[str]) -> Dict[str, Any]:
    """Describe the no-report-text control without making a model call."""

    direct = metadata_only_counter(relation_codes)
    return {
        "condition": "field_only_no_report_text",
        "report_text_replaced": True,
        "model_run": False,
        "direct_metadata_counter": direct,
        "interpretation": "If a future model effect survives this control, classify it as direct-code/formatting behavior, not evidence-text integration.",
    }


def relation_noise_fixture(config: Optional[FrozenConfig] = None) -> Dict[str, Any]:
    """Return a deterministic relation-noise/unknown fixture for unit tests."""

    config = config or FrozenConfig()
    base = ["DPND", "INDP", "UNKN", "DPND", "INDP"]
    noisy = list(base)
    # Stable, local perturbation at the locked 20% fixture rate: one of five.
    digest = hashlib.sha256((config.master_seed + ":relation-noise-fixture").encode("utf-8")).digest()
    position = digest[0] % len(noisy)
    alternatives = [code for code in ("DPND", "INDP", "UNKN") if code != noisy[position]]
    noisy[position] = alternatives[digest[1] % len(alternatives)]
    return {
        "base_codes": base,
        "noisy_codes": noisy,
        "noise_rate": 0.20,
        "unknown_preserved_in_base": "UNKN" in base,
        "gold_untouched": True,
    }


def control_receipt(corpus: Corpus, prompts: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    """Bundle parity and diagnostic receipts for a local smoke run."""

    split_report = split_leakage_report(corpus)
    parity_bundles = len({prompt["bundle_id"] for prompt in prompts})
    return {
        "split_leakage": split_report,
        "prompt_bundle_count": parity_bundles,
        "prompt_count": len(prompts),
        "surface_only": surface_only_nearest_centroid(corpus),
        "balance": balance_report(corpus),
        "relation_noise_fixture": relation_noise_fixture(),
        "no_model_or_provider_called": True,
    }
