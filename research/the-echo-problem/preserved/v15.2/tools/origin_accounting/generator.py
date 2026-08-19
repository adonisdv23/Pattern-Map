"""Deterministic fictional corpus and F0/F1/F2 prompt construction.

The generator is deliberately slot-grammar based.  It does not call a model,
provider, network, or random external corpus.  Gold origin membership is a
construction-time bookkeeping relation only; it is never presented as
real-world epistemic independence.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import itertools
import random
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple

from .canonical import ordered_membership_sha256, sha256_json, text_sha256
from .config import FrozenConfig, SPLITS, STRUCTURES, assert_config_invariants


ID_RE = re.compile(r"^[A-Z]{2}-[A-Z2-7]{10}$")
TOKEN_RE = re.compile(r"[A-Za-z0-9_]+|[^\w\s]", re.UNICODE)
RELATION_CODE = {
    "dependent": "DPND",
    "independent_as_stipulated": "INDP",
    "unknown": "UNKN",
}

STYLES = ("lab_note", "release_note", "field_log", "review_note")
DOMAINS = ("technical", "environmental")
SUBJECTS = {
    "technical": ("Lumen cache", "Orchid relay", "Kite index", "Vesper queue"),
    "environmental": (
        "Northlake reed plot",
        "Vesper inlet",
        "Halcyon ridge",
        "Morrow wetland",
    ),
}
OBJECTS = {
    "technical": ("median sync latency", "batch completion time", "lookup delay", "queue dwell"),
    "environmental": ("salinity index", "night-flight count", "surface moisture", "reed density"),
}
BASELINES = {
    "technical": ("the baseline cache", "the prior relay", "the reference index", "the control queue"),
    "environmental": ("the reference plot", "the prior inlet reading", "the ridge baseline", "the control wetland"),
}
SURFACE_WORDS = (
    "amber", "birch", "cinder", "delta", "elm", "fallow", "granite", "harbor",
    "ivory", "juniper", "kelp", "lattice", "marble", "narrow", "ochre", "pebble",
    "quartz", "ripple", "sable", "thistle", "umber", "velvet", "willow", "xenon",
    "yarrow", "zephyr", "atlas", "bracken", "cedar", "dovetail", "estuary", "flint",
    "garnet", "hollow", "island", "jasper", "knoll", "lichen", "meadow", "nacre",
    "opal", "plume", "quill", "rosemary", "silt", "tundra", "upland", "violet",
    "walnut", "xylem", "yardarm", "zinc", "acorn", "barley", "clover", "drift",
    "ember", "fennel", "glade", "hazel", "inlet", "jute", "kestrel", "lantern",
    "moss", "nutmeg", "osprey", "pollen", "quarry", "reed", "spruce", "tamarind",
    "urchin", "valley", "wren", "xeric", "yew", "zest", "alder", "basalt",
    "cobalt", "dune", "equinox", "fern", "gully", "heather", "iris", "lagoon",
    "moraine", "nebula", "orbit", "prairie", "quartzite", "raven", "saffron", "topaz",
    "umber", "verge", "wheat", "xylophone", "yonder", "zinnia", "ash", "beacon",
    "coral", "dewdrop", "elmwood", "frost", "grove", "horizon", "ink", "jasmine",
    "kettle", "lowland", "minnow", "north", "olive", "pavilion", "quiet", "rivulet",
    "sienna", "tangle", "unfurl", "vernal", "west", "xenial", "yonder", "zonal",
)


class DeterministicTokenizer:
    """Small local token-count surrogate used only for parity scaffolding."""

    identifier = "deterministic-regex-surrogate-v1"

    @classmethod
    def count(cls, text: str) -> int:
        return len(TOKEN_RE.findall(text))


def _b32_digest(secret: str, message: str) -> str:
    digest = hmac.new(secret.encode("utf-8"), message.encode("utf-8"), hashlib.sha256).digest()
    return base64.b32encode(digest).decode("ascii").rstrip("=")[:10]


def opaque_id(prefix: str, config: FrozenConfig, object_type: str, namespace: str, index: int) -> str:
    """Make an opaque RFC-4648 Base32 identifier with no semantic bits."""

    return "%s-%s" % (prefix, _b32_digest(config.master_seed, "%s:%s:%d" % (object_type, namespace, index)))


def _date_for(index: int) -> str:
    year = 2040 + (index % 30)
    month = 1 + ((index * 7) % 12)
    day = 1 + ((index * 11) % 27)
    return "%04d-%02d-%02d" % (year, month, day)


def _claim_for(domain: str, index: int) -> Dict[str, Any]:
    subject = SUBJECTS[domain][index % len(SUBJECTS[domain])]
    obj = OBJECTS[domain][(index // 2) % len(OBJECTS[domain])]
    baseline = BASELINES[domain][(index // 3) % len(BASELINES[domain])]
    if domain == "technical":
        predicate = "reduced" if index % 3 else "increased"
        magnitude = 12 + (index * 7) % 42
        unit = "percent"
        claim = "%s %s %s by %d %s relative to %s during the %s test in %d." % (
            subject,
            predicate,
            obj,
            magnitude,
            unit,
            baseline,
            "Northlake" if index % 2 == 0 else "Morrow",
            2040 + (index % 30),
        )
    else:
        predicate = "recorded" if index % 4 else "did_not_record"
        magnitude = 3 + (index * 5) % 16
        unit = "index_points" if "index" in obj else "count"
        if predicate == "recorded":
            claim = "At %s during autumn %d, %s recorded %s at %d %s compared with %s." % (
                "Northlake" if index % 2 == 0 else "Halcyon",
                2040 + (index % 30),
                subject,
                obj,
                magnitude,
                unit,
                baseline,
            )
        else:
            claim = "At %s during autumn %d, %s did not record %s above %d %s compared with %s." % (
                "Northlake" if index % 2 == 0 else "Halcyon",
                2040 + (index % 30),
                subject,
                obj,
                magnitude,
                unit,
                baseline,
            )
    truth_state = ("refuted", "supported", "insufficient")[index % 3]
    return {
        "domain": domain,
        "subject": subject,
        "predicate": predicate,
        "object": obj,
        "magnitude": magnitude,
        "unit": unit,
        "baseline": baseline,
        "site": "Northlake" if index % 2 == 0 else "Morrow",
        "time_window": {"start_year": 2040 + (index % 30), "end_year": 2040 + (index % 30)},
        "truth_state": truth_state,
        "claim_text": claim,
        "lexical_seed": index * 7919 + 17,
    }


def _report_text(claim: Mapping[str, Any], style: str, transform: str, report_index: int) -> str:
    """Render a report without stating its latent relation or structure."""

    leads = {
        "lab_note": "A controlled lab note recorded the following measurement.",
        "release_note": "A dated release note described the following bounded result.",
        "field_log": "A field log recorded the following observation at the stated site.",
        "review_note": "A review note summarized the following result and its stated scope.",
    }
    method = {
        "lab_note": "The note names a comparator and a single observation window.",
        "release_note": "The report gives the version context and limits the result to this comparison.",
        "field_log": "The observer records the location, date, and the comparison condition.",
        "review_note": "The summary retains the measured comparison while noting that broader conclusions require more work.",
    }
    caveat = "The record remains bounded by this fictional observation window and does not claim a result beyond its stated scope."
    claim = str(claim["claim_text"])
    if transform == "dependent_paraphrase":
        claim = claim.replace(" recorded ", " reported ").replace(" reduced ", " showed a reduction in ")
    elif transform == "summary":
        claim = claim.replace(" during the ", " in the ").replace(" compared with ", " versus ")
    elif transform == "independent_contradiction":
        claim = "The comparison in this report points in the opposite direction from the target claim: " + claim
    text = "%s %s %s %s Observation window %s. Report sequence marker %02d." % (
        leads[style],
        claim,
        method[style],
        caveat,
        _date_for(report_index),
        report_index % 100,
    )
    # Deterministic lexical variation is crossed with structure and style so
    # exact/near-duplicate checks do not mistake shared grammar for leakage.
    marker_rng = random.Random(report_index * 104729 + 31)
    marker_words = marker_rng.sample(SURFACE_WORDS, 32)
    text += " Fictional calibration descriptors: %s." % " ".join(marker_words)
    # Keep the shortest generated records safely above the schema's 120-char minimum.
    while len(text) < 120:
        text += " The note remains limited to this fictional benchmark observation."
    return text


def _style_for(bundle_index: int, report_index: int) -> str:
    return STYLES[(bundle_index + report_index) % len(STYLES)]


def _relation_for(transform: str) -> str:
    if transform in ("dependent_copy", "dependent_paraphrase", "summary"):
        return "dependent"
    if transform == "independent_observation" or transform == "independent_contradiction":
        return "independent_as_stipulated"
    return "unknown"


def _structure_plan(structure: str) -> List[Tuple[str, str, str]]:
    """Return (stance, transformation, origin-label) report plans."""

    if structure == "one_origin_repetition":
        return [
            ("supports", "original", "support-0"),
            ("supports", "dependent_copy", "support-0"),
            ("supports", "dependent_paraphrase", "support-0"),
            ("supports", "summary", "support-0"),
        ]
    if structure == "multiple_origin_convergence":
        return [
            ("supports", "independent_observation", "support-0"),
            ("supports", "independent_observation", "support-1"),
            ("supports", "independent_observation", "support-2"),
            ("neutral", "original", "neutral-0"),
        ]
    if structure == "unknown_origin":
        return [
            ("supports", "original", "unknown-0"),
            ("supports", "original", "unknown-1"),
            ("supports", "summary", "unknown-0"),
            ("supports", "dependent_paraphrase", "unknown-1"),
        ]
    if structure == "conflict":
        return [
            ("supports", "original", "support-0"),
            ("supports", "dependent_paraphrase", "support-0"),
            ("refutes", "independent_contradiction", "refute-0"),
            ("refutes", "dependent_copy", "refute-0"),
        ]
    raise ValueError("unknown origin structure: %s" % structure)


def _origin_certainty(structure: str) -> Tuple[str, Optional[int]]:
    if structure == "one_origin_repetition":
        return "single", 1
    if structure == "multiple_origin_convergence":
        return "multiple", 3
    if structure == "unknown_origin":
        return "unknown", None
    if structure == "conflict":
        return "single", 1
    raise ValueError(structure)


@dataclass
class Corpus:
    propositions: List[Dict[str, Any]]
    reports: List[Dict[str, Any]]
    bundles_public: List[Dict[str, Any]]
    bundles_gold: List[Dict[str, Any]]
    provenance_graphs: List[Dict[str, Any]]
    split_index: List[Dict[str, Any]]

    def by_bundle(self) -> Dict[str, Dict[str, Any]]:
        reports = {record["report_id"]: record for record in self.reports}
        gold = {record["bundle_id"]: record for record in self.bundles_gold}
        output: Dict[str, Dict[str, Any]] = {}
        for public in self.bundles_public:
            output[public["bundle_id"]] = {
                "public": public,
                "gold": gold[public["bundle_id"]],
                "reports": [reports[rid] for rid in public["report_order"]],
            }
        return output

    def all_records(self) -> Iterable[Mapping[str, Any]]:
        for group in (
            self.propositions,
            self.reports,
            self.bundles_public,
            self.bundles_gold,
            self.provenance_graphs,
            self.split_index,
        ):
            for record in group:
                yield record


def _build_one_bundle(
    config: FrozenConfig,
    split: str,
    structure: str,
    bundle_index: int,
    proposition_index: int,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]], Dict[str, Any], Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    domain = DOMAINS[proposition_index % len(DOMAINS)]
    claim = _claim_for(domain, proposition_index)
    proposition_family_id = opaque_id("PF", config, "proposition_family", "%s:%s" % (split, structure), proposition_index)
    origin_family_id = opaque_id("OF", config, "origin_family", "%s:%s" % (split, structure), proposition_index)
    bundle_id = opaque_id("BD", config, "bundle", "%s:%s" % (split, structure), bundle_index)
    graph_id = opaque_id("PG", config, "provenance_graph", "%s:%s" % (split, structure), bundle_index)
    plans = _structure_plan(structure)
    origin_ids: Dict[str, str] = {}
    for label in sorted(set(plan[2] for plan in plans)):
        origin_ids[label] = opaque_id("OR", config, "origin", "%s:%s:%s" % (split, structure, label), bundle_index)

    reports: List[Dict[str, Any]] = []
    graph_nodes: List[Dict[str, Any]] = []
    graph_edges: List[Dict[str, Any]] = []
    previous_artifact_for_origin: Dict[str, str] = {}
    supporting_ids: List[str] = []
    refuting_ids: List[str] = []
    relation_by_report: Dict[str, str] = {}
    report_origin: Dict[str, str] = {}

    for report_index, (stance, transform, origin_label) in enumerate(plans):
        report_id = opaque_id("RP", config, "report", "%s:%s" % (split, structure), bundle_index * 10 + report_index)
        source_id = opaque_id("SC", config, "source", "%s:%s" % (split, structure), bundle_index * 10 + report_index)
        artifact_id = opaque_id("AR", config, "artifact", "%s:%s" % (split, structure), bundle_index * 10 + report_index)
        origin_id = origin_ids[origin_label]
        style = _style_for(bundle_index, report_index)
        report = {
            "report_id": report_id,
            "source_id": source_id,
            "artifact_id": artifact_id,
            "proposition_family_id": proposition_family_id,
            "origin_id": origin_id,
            "style": style,
            "stance": stance,
            "transformation_type": transform,
            "observed_at": _date_for(proposition_index * 100 + bundle_index * 10 + report_index),
            "text": _report_text(claim, style, transform, proposition_index * 100 + bundle_index * 10 + report_index),
        }
        report["text_sha256"] = text_sha256(report["text"])
        reports.append(report)
        # Unknown-origin bundles intentionally withhold every relation, even
        # when the latent construction used a summary/paraphrase transform.
        # The evaluator must not turn a hidden derivation into a visible cue.
        relation_by_report[report_id] = "unknown" if structure == "unknown_origin" else _relation_for(transform)
        report_origin[report_id] = origin_id
        if stance == "supports":
            supporting_ids.append(report_id)
        elif stance == "refutes":
            refuting_ids.append(report_id)
        graph_nodes.extend(
            [
                {"node_id": source_id, "node_type": "source"},
                {"node_id": artifact_id, "node_type": "artifact", "report_id": report_id},
            ]
        )
        if origin_id not in {node["node_id"] for node in graph_nodes}:
            graph_nodes.append({"node_id": origin_id, "node_type": "origin"})
        graph_edges.extend(
            [
                {"from": artifact_id, "to": source_id, "edge_type": "generated_from"},
                {"from": artifact_id, "to": origin_id, "edge_type": "generated_from"},
            ]
        )
        if transform in ("dependent_copy", "dependent_paraphrase", "summary"):
            parent = previous_artifact_for_origin.get(origin_label)
            if parent is None:
                raise ValueError("dependent report has no deterministic parent")
            graph_edges.append(
                {
                    "from": artifact_id,
                    "to": parent,
                    "edge_type": "derives_from",
                    "derivation": transform,
                }
            )
        previous_artifact_for_origin.setdefault(origin_label, artifact_id)

    order_rng = random.Random((bundle_index + 1) * 104729 + proposition_index)
    report_order = [record["report_id"] for record in reports]
    order_rng.shuffle(report_order)
    public = {
        "bundle_id": bundle_id,
        "proposition_family_id": proposition_family_id,
        "claim_text": claim["claim_text"],
        "report_ids": [record["report_id"] for record in reports],
        "report_order": report_order,
        "domain": domain,
        "observed_date_range": {
            "start": min(record["observed_at"] for record in reports),
            "end": max(record["observed_at"] for record in reports),
        },
    }
    public["bundle_text_sha256"] = sha256_json(
        {"claim_text": public["claim_text"], "report_order": [(rid, next(r["text"] for r in reports if r["report_id"] == rid)) for rid in report_order]}
    )
    certainty, support_count = _origin_certainty(structure)
    support_origin_ids = sorted({report_origin[rid] for rid in supporting_ids})
    refute_origin_ids = sorted({report_origin[rid] for rid in refuting_ids})
    gold = {
        "bundle_id": bundle_id,
        "split": split,
        "origin_structure": structure,
        "gold_claim_state": "contested" if structure == "conflict" else claim["truth_state"],
        "gold_support_origin_count": support_count,
        "gold_support_origin_certainty": certainty,
        "support_origin_ids": support_origin_ids,
        "refute_origin_ids": refute_origin_ids,
        "origin_family_id": origin_family_id,
        "supporting_report_ids": supporting_ids,
        "refuting_report_ids": refuting_ids,
        "relation_by_report_id": relation_by_report,
        "required_unknown_preservation": structure == "unknown_origin",
        "provenance_graph_id": graph_id,
        "stress_variant": "relation_noise" if split == "stress" else None,
        "noise_rate": 0.0,
        "noise_seed": None,
        "stress_cell_id": None,
    }
    if split == "stress":
        rate = config.noise_rates[(bundle_index // len(config.structures)) % len(config.noise_rates)]
        cell = (bundle_index % len(config.structures)) * len(config.noise_rates) + (bundle_index % len(config.noise_rates))
        gold["noise_rate"] = rate
        gold["noise_seed"] = opaque_id("NS", config, "noise", "%s:%s" % (split, structure), bundle_index)
        gold["stress_cell_id"] = "STRESS-%02d" % cell
    graph = {
        "provenance_graph_id": graph_id,
        "origin_family_id": origin_family_id,
        "nodes": graph_nodes,
        "edges": graph_edges,
        "latent_origin_count": len(origin_ids),
        "certified_relation_state": certainty,
    }
    proposition = {
        "proposition_family_id": proposition_family_id,
        "domain": claim["domain"],
        "subject": claim["subject"],
        "predicate": claim["predicate"],
        "object": claim["object"],
        "magnitude": claim["magnitude"],
        "unit": claim["unit"],
        "baseline": claim["baseline"],
        "site": claim["site"],
        "time_window": claim["time_window"],
        "truth_state": gold["gold_claim_state"],
        "lexical_seed": claim["lexical_seed"],
    }
    split_row = {
        "bundle_id": bundle_id,
        "proposition_family_id": proposition_family_id,
        "origin_family_id": origin_family_id,
        "split": split,
        "origin_structure": structure,
    }
    return proposition, reports, public, gold, graph, split_row


def generate_corpus(config: Optional[FrozenConfig] = None, small: bool = False) -> Corpus:
    """Generate deterministic split-blocked synthetic records.

    ``small=True`` emits one bundle per structure in each split for rapid
    smoke tests.  It is not the protocol's powered corpus and must never be
    described as a primary sample.
    """

    config = config or FrozenConfig()
    assert_config_invariants(config)
    propositions: List[Dict[str, Any]] = []
    reports: List[Dict[str, Any]] = []
    bundles_public: List[Dict[str, Any]] = []
    bundles_gold: List[Dict[str, Any]] = []
    graphs: List[Dict[str, Any]] = []
    split_index: List[Dict[str, Any]] = []
    bundle_index = 0
    proposition_index = 0
    for split in ("dev", "pilot", "primary", "stress"):
        for structure in STRUCTURES:
            count = 1 if small else int(config.split_counts[split][structure])
            for _ in range(count):
                proposition, bundle_reports, public, gold, graph, split_row = _build_one_bundle(
                    config, split, structure, bundle_index, proposition_index
                )
                propositions.append(proposition)
                reports.extend(bundle_reports)
                bundles_public.append(public)
                bundles_gold.append(gold)
                graphs.append(graph)
                split_index.append(split_row)
                bundle_index += 1
                proposition_index += 1
    corpus = Corpus(propositions, reports, bundles_public, bundles_gold, graphs, split_index)
    validate_corpus(corpus, config)
    return corpus


def build_primary_manifest(corpus: Corpus, config: Optional[FrozenConfig] = None) -> Dict[str, Any]:
    """Build the ordered, hash-locked primary A and safety M memberships."""

    config = config or FrozenConfig()
    assert_config_invariants(config)
    validate_corpus(corpus, config)
    gold_by_bundle = {record["bundle_id"]: record for record in corpus.bundles_gold}
    primary_ids = sorted(
        bundle_id for bundle_id, gold in gold_by_bundle.items() if gold.get("split") == "primary"
    )
    safety_ids = [
        bundle_id
        for bundle_id in primary_ids
        if gold_by_bundle[bundle_id].get("gold_support_origin_certainty") == "multiple"
    ]
    if len(primary_ids) != 300 or len(safety_ids) != 75:
        raise ValueError("primary manifest requires exactly 300 A rows and 75 M rows")
    manifest = {
        "manifest_version": "oa-primary-manifest-1.0.0",
        "protocol_version": config.protocol_version,
        "primary_bundle_ids": primary_ids,
        "primary_bundle_ids_sha256": ordered_membership_sha256(primary_ids),
        "primary_n": len(primary_ids),
        "safety_bundle_ids": safety_ids,
        "safety_bundle_ids_sha256": ordered_membership_sha256(safety_ids),
        "safety_n": len(safety_ids),
        "safety_definition": "primary bundles with gold_support_origin_certainty=multiple",
    }
    manifest["manifest_sha256"] = sha256_json(manifest)
    return manifest


def _neutral_pad(target_tokens: int, target_bytes: int, text: str, prefix: str = "") -> str:
    """Pad a prompt with inert ASCII tokens and spaces to both exact targets."""

    current_tokens = DeterministicTokenizer.count(prefix + text)
    if current_tokens > target_tokens:
        raise ValueError("prompt already exceeds target token count")
    padded = text + (" PAD" * (target_tokens - current_tokens))
    if len((prefix + padded).encode("utf-8")) > target_bytes:
        raise ValueError("prompt already exceeds target byte count")
    padded += " " * (target_bytes - len((prefix + padded).encode("utf-8")))
    if DeterministicTokenizer.count(prefix + padded) != target_tokens:
        raise AssertionError("deterministic padding failed token target")
    if len((prefix + padded).encode("utf-8")) != target_bytes:
        raise AssertionError("deterministic padding failed byte target")
    return padded


SHARED_SYSTEM = """You are a bounded evidence-counting evaluator.

Return exactly one JSON object with these four keys and no others:
origin_count_supporting, claim_state, confidence, evidence_ids.

origin_count_supporting must be an integer from 0 through 6.
claim_state must be one of supported, refuted, insufficient, contested.
confidence must be a number from 0 through 1.
evidence_ids must be a unique JSON array of report IDs from the bundle.

Do not include Markdown, code fences, explanations, or additional keys.
Use only the claim and reports supplied in this task. Do not infer a provenance relation that is not supplied.

Metadata relation-code legend, when a relation code is present:
DPND means the report is dependent on another observed report or origin path.
INDP means a separate origin in this benchmark; this is a stipulated graph label, not a claim about the real world.
UNKN means the origin relation is unknown and must not be counted as independent.
NONE means no relation cue is supplied in that slot."""

F0_INSTRUCTION = """Assess the claim using the reports. Preserve uncertainty when the supplied evidence does not resolve the claim. Select the report IDs used for your assessment. Do not infer a provenance relation from wording, source ID, artifact ID, date, or report order."""
RULE_INSTRUCTION = """Count distinct origin pathways when the supplied information permits it. Do not treat repeated or derived reports as independent support. Preserve an unknown origin relation as unknown, and do not infer a relation that is not supplied. Select the report IDs used for your assessment."""


def _relation_code_for_report(gold: Mapping[str, Any], report_id: str, noisy: bool, config: FrozenConfig, bundle_index: int) -> str:
    relation = gold["relation_by_report_id"][report_id]
    code = RELATION_CODE[relation]
    # Unknown-origin is an explicit all-UNKN fixture. Relation-noise stress
    # must not turn withheld certification into a visible dependent or
    # independent cue.
    if gold.get("required_unknown_preservation") or gold.get("origin_structure") == "unknown_origin":
        return "UNKN"
    if not noisy or not gold.get("noise_rate"):
        return code
    # Deterministically perturb only the visible F2 cue; gold remains unchanged.
    seed = "%s:%s:%s" % (config.master_seed, gold["noise_seed"], report_id)
    chance = int.from_bytes(hashlib.sha256(seed.encode("utf-8")).digest()[:8], "big") / float(2 ** 64)
    if chance >= float(gold["noise_rate"]):
        return code
    alternatives = [candidate for candidate in ("DPND", "INDP", "UNKN") if candidate != code]
    selector = hashlib.sha256((seed + ":selector").encode("utf-8")).digest()[0] % len(alternatives)
    return alternatives[selector]


def _raw_prompt_text(
    bundle: Mapping[str, Any],
    condition: str,
    config: FrozenConfig,
    bundle_index: int,
) -> Tuple[str, Dict[str, str], str]:
    public = bundle["public"]
    gold = bundle["gold"]
    reports = bundle["reports"]
    relation_codes: Dict[str, str] = {}
    rows: List[str] = []
    for report in reports:
        if condition == "F2":
            code = _relation_code_for_report(gold, report["report_id"], True, config, bundle_index)
        else:
            code = "NONE"
        relation_codes[report["report_id"]] = code
        rows.append(
            "- report_id=%s; source_id=%s; artifact_id=%s; observed_at=%s; relation_code=%s\n  %s"
            % (
                report["report_id"],
                report["source_id"],
                report["artifact_id"],
                report["observed_at"],
                code,
                report["text"],
            )
        )
    instruction = F0_INSTRUCTION if condition == "F0" else RULE_INSTRUCTION
    user = "Claim:\n%s\n\nReports:\n%s\n\nMetadata slots:\n%s\n\n%s\n\nReturn the required JSON object now.\n" % (
        public["claim_text"],
        "\n".join(rows),
        "\n".join(
            "- report_id=%s; source_id=%s; artifact_id=%s; observed_at=%s; relation_code=%s"
            % (report["report_id"], report["source_id"], report["artifact_id"], report["observed_at"], relation_codes[report["report_id"]])
            for report in reports
        ),
        instruction,
    )
    return user, relation_codes, instruction


def build_prompt_instances(corpus: Corpus, config: Optional[FrozenConfig] = None) -> List[Dict[str, Any]]:
    """Build F0/F1/F2 prompt instances with exact length parity per bundle."""

    config = config or FrozenConfig()
    assert_config_invariants(config)
    prompts: List[Dict[str, Any]] = []
    for bundle_index, (bundle_id, bundle) in enumerate(sorted(corpus.by_bundle().items())):
        raw: Dict[str, str] = {}
        relation_codes: Dict[str, Dict[str, str]] = {}
        instructions: Dict[str, str] = {}
        for condition in ("F0", "F1", "F2"):
            raw[condition], relation_codes[condition], instructions[condition] = _raw_prompt_text(
                bundle, condition, config, bundle_index
            )
        raw_token_counts = {condition: DeterministicTokenizer.count(SHARED_SYSTEM + text) for condition, text in raw.items()}
        raw_byte_counts = {condition: len((SHARED_SYSTEM + text).encode("utf-8")) for condition, text in raw.items()}
        target_tokens = max(raw_token_counts.values()) + 8
        target_bytes = max(raw_byte_counts.values()) + 64
        padded = {
            condition: _neutral_pad(target_tokens, target_bytes, text, prefix=SHARED_SYSTEM)
            for condition, text in raw.items()
        }
        # Recalculate target against combined system+user bytes.  The first
        # pass above makes user text equal; this assertion protects drift.
        combined = {condition: SHARED_SYSTEM + text for condition, text in padded.items()}
        combined_bytes = {condition: len(text.encode("utf-8")) for condition, text in combined.items()}
        combined_tokens = {condition: DeterministicTokenizer.count(text) for condition, text in combined.items()}
        if len(set(combined_bytes.values())) != 1 or len(set(combined_tokens.values())) != 1:
            raise AssertionError("prompt parity construction failed")
        reports = bundle["reports"]
        report_hashes = {report["report_id"]: report["text_sha256"] for report in reports}
        report_order = [report["report_id"] for report in reports]
        report_hash_sequence = [
            {"report_id": report["report_id"], "text_sha256": report["text_sha256"]}
            for report in reports
        ]
        evidence_bytes_equal = all(
            text_sha256(report["text"]) == report["text_sha256"] for report in reports
        )
        for condition in ("F0", "F1", "F2"):
            prompt_instance_id = opaque_id("PI", config, "prompt_instance", bundle_id + ":" + condition, bundle_index)
            final_input_text = SHARED_SYSTEM + padded[condition]
            prompts.append(
                {
                    "prompt_instance_id": prompt_instance_id,
                    "bundle_id": bundle_id,
                    "condition": condition,
                    "prompt_version": "oa-prompts-0.1.0",
                    "system_text": SHARED_SYSTEM,
                    "user_text": padded[condition],
                    "instruction_text": instructions[condition],
                    "system_sha256": text_sha256(SHARED_SYSTEM),
                    "user_sha256": text_sha256(padded[condition]),
                    "instruction_sha256": text_sha256(instructions[condition]),
                    "final_input_text": final_input_text,
                    "final_input_sha256": text_sha256(final_input_text),
                    "input_token_count": combined_tokens[condition],
                    "input_byte_count": combined_bytes[condition],
                    "target_input_token_count": combined_tokens[condition],
                    "target_input_byte_count": combined_bytes[condition],
                    "tokenizer_id": DeterministicTokenizer.identifier,
                    "tokenizer_is_surrogate": True,
                    "token_parity_pass": combined_tokens[condition] == combined_tokens["F2"],
                    "byte_parity_pass": combined_bytes[condition] == combined_bytes["F2"],
                    "max_new_tokens": config.max_new_tokens,
                    "retrieval_calls": 0,
                    "tool_calls": 0,
                    "relation_codes": relation_codes[condition],
                    "report_id_order": report_order,
                    "report_text_sha256s": report_hashes,
                    "report_text_hash_sequence": report_hash_sequence,
                    # This is computed from the immutable report payload, not
                    # asserted as a caller-supplied receipt flag.
                    "evidence_bytes_equal": evidence_bytes_equal,
                    "intended_tokenizer_parity_status": "not_run_model_tokenizer",
                }
            )
    validate_prompt_parity(prompts, corpus=corpus)
    return prompts


def _validate_prompt_payload(prompt: Mapping[str, Any]) -> None:
    """Recompute payload hashes/counts before comparing condition receipts."""

    system_text = str(prompt["system_text"])
    user_text = str(prompt["user_text"])
    final_input_text = str(prompt["final_input_text"])
    instruction_text = str(prompt["instruction_text"])
    if prompt["system_sha256"] != text_sha256(system_text):
        raise ValueError("system prompt hash does not match payload")
    if prompt["user_sha256"] != text_sha256(user_text):
        raise ValueError("user prompt hash does not match payload")
    if prompt["instruction_sha256"] != text_sha256(instruction_text):
        raise ValueError("condition instruction hash does not match payload")
    if final_input_text != system_text + user_text:
        raise ValueError("final input is not system text followed by user text")
    if prompt["final_input_sha256"] != text_sha256(final_input_text):
        raise ValueError("final input hash does not match payload")
    expected_tokens = DeterministicTokenizer.count(final_input_text)
    expected_bytes = len(final_input_text.encode("utf-8"))
    if prompt["input_token_count"] != expected_tokens or prompt["target_input_token_count"] != expected_tokens:
        raise ValueError("prompt token receipt does not match payload")
    if prompt["input_byte_count"] != expected_bytes or prompt["target_input_byte_count"] != expected_bytes:
        raise ValueError("prompt byte receipt does not match payload")
    if prompt.get("intended_tokenizer_parity_status") != "not_run_model_tokenizer":
        raise ValueError("intended-tokenizer status must remain an open gate")
    order = list(prompt["report_id_order"])
    sequence = list(prompt["report_text_hash_sequence"])
    if len(order) != len(set(order)) or [row["report_id"] for row in sequence] != order:
        raise ValueError("report hash sequence/order receipt is inconsistent")
    if prompt["report_text_sha256s"] != {
        row["report_id"]: row["text_sha256"] for row in sequence
    }:
        raise ValueError("report hash map and ordered hash sequence differ")
    if set(prompt["relation_codes"]) != set(order) or any(
        code not in {"DPND", "INDP", "UNKN", "NONE"}
        for code in prompt["relation_codes"].values()
    ):
        raise ValueError("relation-code receipt does not cover the ordered evidence IDs")
    if not prompt["evidence_bytes_equal"]:
        raise ValueError("evidence byte equality receipt failed")


def validate_prompt_parity(
    prompts: Sequence[Mapping[str, Any]],
    corpus: Optional[Corpus] = None,
) -> None:
    """Validate prompt payload receipts and exact per-bundle condition parity.

    The local regex tokenizer proves only development parity. Intended-model
    tokenizer parity remains explicitly open until an owner-selected backend is
    available.
    """

    grouped: Dict[str, Dict[str, Mapping[str, Any]]] = {}
    for prompt in prompts:
        _validate_prompt_payload(prompt)
        bundle_group = grouped.setdefault(str(prompt["bundle_id"]), {})
        condition = str(prompt["condition"])
        if condition in bundle_group:
            raise ValueError("duplicate %s prompt for bundle %s" % (condition, prompt["bundle_id"]))
        bundle_group[condition] = prompt
    expected_by_bundle = corpus.by_bundle() if corpus is not None else {}
    for bundle_id, by_condition in grouped.items():
        if set(by_condition) != {"F0", "F1", "F2"}:
            raise ValueError("bundle %s does not have exactly F0/F1/F2 prompts" % bundle_id)
        f0, f1, f2 = by_condition["F0"], by_condition["F1"], by_condition["F2"]
        if f0["system_text"] != f1["system_text"] or f1["system_text"] != f2["system_text"]:
            raise ValueError("shared system prompt differs between conditions for %s" % bundle_id)
        if f0["system_sha256"] != f1["system_sha256"] or f1["system_sha256"] != f2["system_sha256"]:
            raise ValueError("shared system prompt hash differs between conditions for %s" % bundle_id)
        if f1["instruction_text"] != f2["instruction_text"] or f1["instruction_sha256"] != f2["instruction_sha256"]:
            raise ValueError("F1/F2 instruction differs for %s" % bundle_id)
        if f0["relation_codes"] and set(f0["relation_codes"].values()) != {"NONE"}:
            raise ValueError("F0 relation slots are not all NONE for %s" % bundle_id)
        if f1["relation_codes"] and set(f1["relation_codes"].values()) != {"NONE"}:
            raise ValueError("F1 relation slots are not all NONE for %s" % bundle_id)
        for field in ("input_token_count", "input_byte_count", "target_input_token_count", "target_input_byte_count"):
            if f1[field] != f2[field]:
                raise ValueError("F1/F2 %s mismatch for %s" % (field, bundle_id))
        if any(not condition["token_parity_pass"] for condition in (f0, f1, f2)):
            raise ValueError("condition token parity flag failed for %s" % bundle_id)
        if any(not condition["byte_parity_pass"] for condition in (f0, f1, f2)):
            raise ValueError("condition byte parity flag failed for %s" % bundle_id)
        for field in ("input_token_count", "input_byte_count"):
            if f0[field] != f1[field]:
                raise ValueError("F0 %s mismatch for %s" % (field, bundle_id))
        if f0["report_id_order"] != f1["report_id_order"] or f1["report_id_order"] != f2["report_id_order"]:
            raise ValueError("evidence report order differs between conditions for %s" % bundle_id)
        if f0["report_text_hash_sequence"] != f1["report_text_hash_sequence"] or f1["report_text_hash_sequence"] != f2["report_text_hash_sequence"]:
            raise ValueError("evidence text bytes differ between conditions for %s" % bundle_id)
        if corpus is not None:
            if bundle_id not in expected_by_bundle:
                raise ValueError("prompt references unknown corpus bundle %s" % bundle_id)
            expected_reports = expected_by_bundle[bundle_id]["reports"]
            expected_order = [report["report_id"] for report in expected_reports]
            expected_sequence = [
                {"report_id": report["report_id"], "text_sha256": text_sha256(report["text"])}
                for report in expected_reports
            ]
            for condition in (f0, f1, f2):
                if condition["report_id_order"] != expected_order or condition["report_text_hash_sequence"] != expected_sequence:
                    raise ValueError("prompt evidence does not match corpus bytes/order for %s" % bundle_id)


def validate_corpus(corpus: Corpus, config: Optional[FrozenConfig] = None) -> None:
    """Validate schemas' cross-record invariants, hashes, and graph links.

    The repository also ships Draft 2020-12 schemas. This dependency-free
    validator deliberately covers the relations that JSON Schema cannot express
    by itself, and is run at generation time before any receipt is written.
    """

    config = config or FrozenConfig()
    assert_config_invariants(config)

    def unique_records(records: Sequence[Mapping[str, Any]], key: str, label: str) -> Dict[str, Mapping[str, Any]]:
        output: Dict[str, Mapping[str, Any]] = {}
        for record in records:
            value = str(record[key])
            if value in output:
                raise ValueError("duplicate %s: %s" % (label, value))
            output[value] = record
        return output

    propositions = unique_records(corpus.propositions, "proposition_family_id", "proposition family")
    reports = unique_records(corpus.reports, "report_id", "report")
    public = unique_records(corpus.bundles_public, "bundle_id", "bundle")
    gold = unique_records(corpus.bundles_gold, "bundle_id", "gold bundle")
    graphs = unique_records(corpus.provenance_graphs, "provenance_graph_id", "provenance graph")
    split_rows = unique_records(corpus.split_index, "bundle_id", "split row")
    if not public or set(public) != set(gold) or set(public) != set(split_rows):
        raise ValueError("public, gold, and split bundle memberships differ")
    expected_graph_ids = {str(record["provenance_graph_id"]) for record in gold.values()}
    if set(graphs) != expected_graph_ids:
        raise ValueError("provenance graph membership is not exactly the gold graph membership")
    if set(propositions) != {str(record["proposition_family_id"]) for record in public.values()}:
        raise ValueError("proposition records are not exactly the public bundle families")

    # IDs may intentionally repeat for one origin across reports, but one
    # report/source/artifact must never be represented by two records.
    source_to_report: Dict[str, str] = {}
    artifact_to_report: Dict[str, str] = {}
    all_ids: Dict[str, str] = {}
    for record in corpus.all_records():
        for key, value in record.items():
            if key.endswith("_id") and isinstance(value, str) and "-" in value:
                if value in all_ids and all_ids[value] != key and key not in {"report_id", "origin_id"}:
                    raise ValueError("identifier collision: %s" % value)
                all_ids[value] = key
    for report_id, report in reports.items():
        for field, target in (("source_id", source_to_report), ("artifact_id", artifact_to_report)):
            value = str(report[field])
            if value in target and target[value] != report_id:
                raise ValueError("%s is assigned to multiple reports: %s" % (field, value))
            target[value] = report_id
        if text_sha256(str(report["text"])) != report["text_sha256"]:
            raise ValueError("report text hash mismatch: %s" % report_id)

    split_by_prop: Dict[str, str] = {}
    split_by_origin: Dict[str, str] = {}
    for row in split_rows.values():
        prop = str(row["proposition_family_id"])
        origin = str(row["origin_family_id"])
        split = str(row["split"])
        if prop in split_by_prop and split_by_prop[prop] != split:
            raise ValueError("proposition family crosses splits")
        if origin in split_by_origin and split_by_origin[origin] != split:
            raise ValueError("origin family crosses splits")
        split_by_prop[prop] = split
        split_by_origin[origin] = split
    if set(split_by_prop) != set(propositions):
        raise ValueError("split index does not cover all proposition families")

    reports_by_bundle: Dict[str, List[Mapping[str, Any]]] = defaultdict(list)
    for report_id, report in reports.items():
        matching = [bundle_id for bundle_id, item in public.items() if report_id in item["report_ids"]]
        if len(matching) != 1:
            raise ValueError("report must belong to exactly one public bundle: %s" % report_id)
        bundle_id = matching[0]
        if report["proposition_family_id"] != public[bundle_id]["proposition_family_id"]:
            raise ValueError("report proposition family disagrees with bundle: %s" % report_id)
        reports_by_bundle[bundle_id].append(report)

    for bundle_id, item in public.items():
        ids = list(item["report_order"])
        if len(ids) != len(set(ids)) or set(ids) != set(item["report_ids"]):
            raise ValueError("report order is not a permutation: %s" % bundle_id)
        bundle_reports = {report["report_id"]: report for report in reports_by_bundle[bundle_id]}
        if set(bundle_reports) != set(ids):
            raise ValueError("bundle report membership mismatch: %s" % bundle_id)
        expected_bundle_hash = sha256_json(
            {
                "claim_text": item["claim_text"],
                "report_order": [(rid, bundle_reports[rid]["text"]) for rid in ids],
            }
        )
        if expected_bundle_hash != item["bundle_text_sha256"]:
            raise ValueError("bundle text hash mismatch: %s" % bundle_id)
        observed = [bundle_reports[rid]["observed_at"] for rid in ids]
        if item["observed_date_range"] != {"start": min(observed), "end": max(observed)}:
            raise ValueError("bundle observed date range mismatch: %s" % bundle_id)
        split_row = split_rows[bundle_id]
        if split_row["proposition_family_id"] != item["proposition_family_id"]:
            raise ValueError("split row proposition family mismatch: %s" % bundle_id)
        proposition = propositions[item["proposition_family_id"]]
        if item["domain"] != proposition["domain"]:
            raise ValueError("public/proposition domain mismatch: %s" % bundle_id)

    for bundle_id, item in gold.items():
        public_item = public[bundle_id]
        graph = graphs.get(str(item["provenance_graph_id"]))
        if graph is None:
            raise ValueError("gold references unknown graph: %s" % bundle_id)
        split_row = split_rows[bundle_id]
        if split_row["split"] != item["split"] or split_row["origin_structure"] != item["origin_structure"]:
            raise ValueError("gold/split structure mismatch: %s" % bundle_id)
        if split_row["origin_family_id"] != item["origin_family_id"]:
            raise ValueError("gold/split origin family mismatch: %s" % bundle_id)
        report_ids = set(public_item["report_ids"])
        support_ids = set(item["supporting_report_ids"])
        refute_ids = set(item["refuting_report_ids"])
        relation_ids = set(item["relation_by_report_id"])
        if support_ids & refute_ids or (support_ids | refute_ids) - report_ids or relation_ids != report_ids:
            raise ValueError("gold report membership is inconsistent: %s" % bundle_id)
        bundle_reports = {report["report_id"]: report for report in reports_by_bundle[bundle_id]}
        expected_support = {rid for rid, report in bundle_reports.items() if report["stance"] == "supports"}
        expected_refute = {rid for rid, report in bundle_reports.items() if report["stance"] == "refutes"}
        if support_ids != expected_support or refute_ids != expected_refute:
            raise ValueError("gold stance lists disagree with report stances: %s" % bundle_id)
        expected_support_origins = {bundle_reports[rid]["origin_id"] for rid in support_ids}
        expected_refute_origins = {bundle_reports[rid]["origin_id"] for rid in refute_ids}
        if set(item["support_origin_ids"]) != expected_support_origins or set(item["refute_origin_ids"]) != expected_refute_origins:
            raise ValueError("gold origin sets disagree with report origins: %s" % bundle_id)
        for rid, report in bundle_reports.items():
            expected_relation = "unknown" if item["origin_structure"] == "unknown_origin" else _relation_for(report["transformation_type"])
            if item["relation_by_report_id"][rid] != expected_relation:
                raise ValueError("gold relation differs from transformation: %s" % rid)
        expected_claim = "contested" if item["origin_structure"] == "conflict" else propositions[public_item["proposition_family_id"]]["truth_state"]
        if item["gold_claim_state"] != expected_claim:
            raise ValueError("gold claim state mismatch: %s" % bundle_id)
        if item["required_unknown_preservation"] != (item["origin_structure"] == "unknown_origin"):
            raise ValueError("unknown preservation flag mismatch: %s" % bundle_id)
        count = item["gold_support_origin_count"]
        certainty = item["gold_support_origin_certainty"]
        if certainty == "unknown":
            if count is not None:
                raise ValueError("unknown support certainty must have null count")
        else:
            if count is None or count != len(expected_support_origins):
                raise ValueError("support origin count mismatch: %s" % bundle_id)
            expected_certainty = "none" if count == 0 else "single" if count == 1 else "multiple"
            if expected_certainty != certainty:
                raise ValueError("support count/certainty mismatch: %s" % bundle_id)

        node_ids = [node["node_id"] for node in graph["nodes"]]
        if len(node_ids) != len(set(node_ids)):
            raise ValueError("graph has duplicate node IDs: %s" % bundle_id)
        node_by_id = {node["node_id"]: node for node in graph["nodes"]}
        node_set = set(node_ids)
        for edge in graph["edges"]:
            if edge["from"] not in node_set or edge["to"] not in node_set:
                raise ValueError("graph contains dangling edge: %s" % bundle_id)
            if edge["from"] == edge["to"]:
                raise ValueError("graph contains a self-edge: %s" % bundle_id)
        artifact_nodes = [node for node in graph["nodes"] if node["node_type"] == "artifact"]
        source_nodes = {node["node_id"] for node in graph["nodes"] if node["node_type"] == "source"}
        origin_nodes = {node["node_id"] for node in graph["nodes"] if node["node_type"] == "origin"}
        if {node["node_id"] for node in artifact_nodes} != {report["artifact_id"] for report in bundle_reports.values()}:
            raise ValueError("graph artifact IDs do not match reports: %s" % bundle_id)
        if source_nodes != {report["source_id"] for report in bundle_reports.values()} or origin_nodes != {report["origin_id"] for report in bundle_reports.values()}:
            raise ValueError("graph source/origin nodes do not match reports: %s" % bundle_id)
        if graph["latent_origin_count"] != len(origin_nodes) or graph["origin_family_id"] != item["origin_family_id"]:
            raise ValueError("graph origin metadata mismatch: %s" % bundle_id)
        if graph["certified_relation_state"] != certainty:
            raise ValueError("graph certainty mismatch: %s" % bundle_id)
        graph_report_ids = {node.get("report_id") for node in artifact_nodes}
        if graph_report_ids != report_ids:
            raise ValueError("graph artifact report IDs do not match bundle: %s" % bundle_id)
        for report in bundle_reports.values():
            generated_targets = [
                edge["to"]
                for edge in graph["edges"]
                if edge["from"] == report["artifact_id"] and edge["edge_type"] == "generated_from"
            ]
            if len(generated_targets) != 2 or set(generated_targets) != {report["source_id"], report["origin_id"]}:
                raise ValueError("artifact source/origin parent invariant failed: %s" % report["report_id"])
            if node_by_id[report["source_id"]]["node_type"] != "source" or node_by_id[report["origin_id"]]["node_type"] != "origin":
                raise ValueError("artifact parent node types are inconsistent: %s" % report["report_id"])
            derivation_edges = [
                edge
                for edge in graph["edges"]
                if edge["from"] == report["artifact_id"] and edge["edge_type"] == "derives_from"
            ]
            if report["transformation_type"] in ("dependent_copy", "dependent_paraphrase", "summary"):
                if len(derivation_edges) != 1 or derivation_edges[0].get("derivation") != report["transformation_type"]:
                    raise ValueError("artifact derivation does not match report transformation: %s" % report["report_id"])
                if node_by_id[derivation_edges[0]["to"]]["node_type"] != "artifact":
                    raise ValueError("derivation parent is not an artifact: %s" % report["report_id"])
            elif derivation_edges:
                raise ValueError("non-dependent report has a derivation edge: %s" % report["report_id"])
        adjacency: Dict[str, List[str]] = defaultdict(list)
        for edge in graph["edges"]:
            if edge["edge_type"] == "derives_from":
                adjacency[edge["from"]].append(edge["to"])
        visiting: set = set()
        visited: set = set()

        def visit(node_id: str) -> None:
            if node_id in visiting:
                raise ValueError("derivation graph contains a cycle: %s" % bundle_id)
            if node_id in visited:
                return
            visiting.add(node_id)
            for parent_id in adjacency.get(node_id, []):
                visit(parent_id)
            visiting.remove(node_id)
            visited.add(node_id)

        for artifact in artifact_nodes:
            visit(artifact["node_id"])

    actual_counts = Counter((row["split"], row["origin_structure"]) for row in split_rows.values())
    full_counts = Counter(
        (split, structure)
        for split, values in config.split_counts.items()
        for structure, count in values.items()
        for _ in range(count)
    )
    small_counts = Counter((split, structure) for split in SPLITS for structure in STRUCTURES)
    if actual_counts != full_counts and actual_counts != small_counts:
        raise ValueError("corpus split/structure counts are neither protocol-sized nor small smoke-sized")
