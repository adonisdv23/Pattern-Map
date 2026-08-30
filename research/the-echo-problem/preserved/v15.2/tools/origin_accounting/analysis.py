"""Fixed-denominator F0/F1/F2 scoring and paired analyses."""

from __future__ import annotations

import math
import random
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from .canonical import ordered_membership_sha256, sha256_json
from .config import FrozenConfig, assert_config_invariants
from .parser import ParseResult


def _support_origin_count(parsed: Optional[Mapping[str, Any]], gold: Mapping[str, Any], reports_by_id: Mapping[str, Mapping[str, Any]]) -> int:
    if not parsed:
        return 0
    origins = set()
    for report_id in parsed.get("evidence_ids", []):
        report = reports_by_id.get(report_id)
        if report and report.get("stance") == "supports":
            origins.add(report["origin_id"])
    return len(origins)


def _selected_evidence_ids(parsed: Optional[Mapping[str, Any]]) -> List[str]:
    """Return model-selected evidence IDs, or an empty list for invalid output."""

    return list(parsed.get("evidence_ids", [])) if parsed else []


def _secondary_metrics(
    parsed: Optional[Mapping[str, Any]],
    gold: Mapping[str, Any],
    reports_by_id: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    """Calculate support-origin diagnostics without changing FC/VOR scoring.

    The output contract defines ``evidence_ids`` as reports used for the
    assessment, not reports credited as supporting the claim.  Therefore these
    diagnostics deliberately inspect only selected reports whose benchmark
    stance is ``supports``.  Neutral and refuting selections are preserved and
    are not treated as support-selection errors. Gold support-origin sets are
    usable only for certified, non-contested ``none``, ``single``, and
    ``multiple`` rows; unknown-origin and contested rows remain undefined for
    support-origin-set scoring rather than treating latent construction truth
    or mixed-stance evidence as a support-only assessment.
    """

    if parsed is None:
        return {
            "absolute_origin_count_error": None,
            "support_origin_set_precision": None,
            "support_origin_set_recall": None,
            "support_origin_set_exact_match": None,
            "secondary_metrics_defined": False,
            "secondary_metrics_scope": "invalid_output",
            "secondary_metrics_exclusion": "invalid_output",
        }

    evidence_ids = _selected_evidence_ids(parsed)

    gold_certainty = gold.get("gold_support_origin_certainty")
    gold_count = gold.get("gold_support_origin_count")
    certified_support = (
        gold_certainty in {"none", "single", "multiple"}
        and gold_count is not None
    )
    selected_support_origins = {
        reports_by_id[report_id]["origin_id"]
        for report_id in evidence_ids
        if report_id in reports_by_id
        and reports_by_id[report_id].get("stance") == "supports"
    }
    gold_support_origins = set(gold.get("support_origin_ids", []))

    conflict = gold.get("gold_claim_state") == "contested"
    if certified_support and not conflict:
        origin_overlap = selected_support_origins & gold_support_origins
        origin_precision = (
            len(origin_overlap) / float(len(selected_support_origins))
            if selected_support_origins
            else None
        )
        origin_recall = (
            len(origin_overlap) / float(len(gold_support_origins))
            if gold_support_origins
            else None
        )
        origin_exact = int(selected_support_origins == gold_support_origins)
        count_error = abs(int(parsed["origin_count_supporting"]) - int(gold_count))
    else:
        origin_precision = None
        origin_recall = None
        origin_exact = None
        count_error = None

    if not certified_support:
        scope = "valid_unknown_or_uncertified"
        exclusion = "unknown_or_uncertified_support_origins"
    elif conflict:
        # A contested claim may legitimately select refuting evidence. Keep
        # the row visible as its own scope but do not score a support-origin
        # set against that mixed-stance assessment.
        count_error = abs(int(parsed["origin_count_supporting"]) - int(gold_count))
        scope = "valid_certified_conflict"
        exclusion = "contested_claim_support_set_not_scored"
    else:
        scope = "valid_certified_non_conflict"
        exclusion = None

    return {
        "absolute_origin_count_error": count_error,
        "support_origin_set_precision": origin_precision,
        "support_origin_set_recall": origin_recall,
        "support_origin_set_exact_match": origin_exact,
        "secondary_metrics_defined": True,
        "secondary_metrics_scope": scope,
        "secondary_metrics_exclusion": exclusion,
    }


def score_output(
    result: ParseResult,
    gold: Mapping[str, Any],
    reports: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    """Score one output while keeping invalid results explicit."""

    report_by_id = {str(report["report_id"]): report for report in reports}
    valid = result.valid
    parsed = result.parsed if valid else None
    hat_n = int(parsed["origin_count_supporting"]) if parsed else None
    certainty = gold["gold_support_origin_certainty"]
    fc_obs = bool(valid and hat_n is not None and hat_n >= 2 and certainty in {"none", "single", "unknown"})
    fc_cons = bool((not valid) or fc_obs)
    fc_lib = bool(fc_obs)
    selected_support_origin_count = _support_origin_count(parsed, gold, report_by_id)
    in_fixed_safety_set = certainty == "multiple"
    vor = bool(
        in_fixed_safety_set
        and valid
        and hat_n is not None
        and hat_n >= 2
        and selected_support_origin_count >= 2
    )
    secondary = _secondary_metrics(parsed, gold, report_by_id)
    return {
        "valid": valid,
        "parse_status": result.parse_status,
        "error_code": result.error_code,
        "origin_count_supporting": hat_n,
        "fc_obs": int(fc_obs),
        "fc_cons": int(fc_cons),
        "fc_lib": int(fc_lib),
        "selected_support_origin_count": selected_support_origin_count,
        "vor": int(vor),
        "claim_state_correct": int(bool(valid and parsed.get("claim_state") == gold.get("gold_claim_state"))),
        "evidence_ids": list(parsed.get("evidence_ids", [])) if parsed else [],
        "selected_support_origin_ids": sorted(
            {
                report_by_id[report_id]["origin_id"]
                for report_id in (parsed.get("evidence_ids", []) if parsed else [])
                if report_id in report_by_id and report_by_id[report_id].get("stance") == "supports"
            }
        ),
        "secondary": secondary,
        **secondary,
    }


def _exact_binomial_cdf(k: int, n: int, p: float = 0.5) -> float:
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    return sum(math.comb(n, x) * (p ** x) * ((1 - p) ** (n - x)) for x in range(k + 1))


def paired_exact_pvalue(left: Sequence[int], right: Sequence[int]) -> float:
    """Two-sided exact paired McNemar/binomial p-value."""

    if len(left) != len(right):
        raise ValueError("paired vectors must have equal length")
    b = sum(int(a == 1 and z == 0) for a, z in zip(left, right))
    c = sum(int(a == 0 and z == 1) for a, z in zip(left, right))
    discordant = b + c
    if discordant == 0:
        return 1.0
    lower = _exact_binomial_cdf(min(b, c), discordant)
    upper = 1.0 - _exact_binomial_cdf(max(b, c) - 1, discordant)
    return min(1.0, 2.0 * min(lower, upper))


def bootstrap_difference(
    left: Sequence[int],
    right: Sequence[int],
    repetitions: int = 10000,
    seed: int = 20260818,
) -> Tuple[float, float]:
    """Deterministic paired percentile interval for mean(right-left)."""

    if len(left) != len(right) or not left:
        raise ValueError("paired bootstrap requires non-empty equal vectors")
    differences = [int(z) - int(a) for a, z in zip(left, right)]
    rng = random.Random(seed)
    n = len(differences)
    samples: List[float] = []
    for _ in range(int(repetitions)):
        total = 0
        for _ in range(n):
            total += differences[rng.randrange(n)]
        samples.append(total / float(n))
    samples.sort()
    low_index = max(0, min(len(samples) - 1, int(0.025 * len(samples))))
    high_index = max(0, min(len(samples) - 1, int(0.975 * len(samples)) - 1))
    return samples[low_index], samples[high_index]


def one_sided_lower_bootstrap(
    left: Sequence[int],
    right: Sequence[int],
    repetitions: int = 10000,
    seed: int = 20260819,
) -> float:
    if len(left) != len(right) or not left:
        raise ValueError("paired bootstrap requires non-empty equal vectors")
    differences = [int(z) - int(a) for a, z in zip(left, right)]
    rng = random.Random(seed)
    n = len(differences)
    samples: List[float] = []
    for _ in range(int(repetitions)):
        total = sum(differences[rng.randrange(n)] for _ in range(n))
        samples.append(total / float(n))
    samples.sort()
    # One-sided 95% lower bound: 5th percentile, not the 2.5th percentile
    # used by the two-sided 95% bootstrap interval.
    index = max(0, min(len(samples) - 1, int(0.05 * len(samples))))
    return samples[index]


SECONDARY_METRIC_KEYS = (
    "absolute_origin_count_error",
    "support_origin_set_precision",
    "support_origin_set_recall",
    "support_origin_set_exact_match",
)


def _descriptive_metric_summary(
    scores: Mapping[str, Mapping[str, Any]],
    bundle_ids: Sequence[str],
    metric: str,
) -> Dict[str, Any]:
    """Summarize a secondary metric without changing its defined denominator."""

    values = [
        float(scores[bundle_id][metric])
        for bundle_id in bundle_ids
        if scores[bundle_id].get(metric) is not None
    ]
    return {
        "n_defined": len(values),
        "mean": sum(values) / float(len(values)) if values else None,
    }


def _paired_descriptive_metric_summary(
    f1: Mapping[str, Mapping[str, Any]],
    f2: Mapping[str, Mapping[str, Any]],
    bundle_ids: Sequence[str],
    metric: str,
) -> Dict[str, Any]:
    """Summarize paired F2-minus-F1 differences for defined secondary rows."""

    differences = [
        float(f2[bundle_id][metric]) - float(f1[bundle_id][metric])
        for bundle_id in bundle_ids
        if f1[bundle_id].get(metric) is not None and f2[bundle_id].get(metric) is not None
    ]
    return {
        "n_paired_defined": len(differences),
        "mean_F2_minus_F1": sum(differences) / float(len(differences)) if differences else None,
    }


def _secondary_descriptive_analysis(
    f1: Mapping[str, Mapping[str, Any]],
    f2: Mapping[str, Mapping[str, Any]],
    bundle_ids: Sequence[str],
) -> Dict[str, Any]:
    """Return descriptive metric summaries as a non-confirmatory sidecar."""

    all_metrics = {
        metric: {
            "F1": _descriptive_metric_summary(f1, bundle_ids, metric),
            "F2": _descriptive_metric_summary(f2, bundle_ids, metric),
            "paired": _paired_descriptive_metric_summary(f1, f2, bundle_ids, metric),
        }
        for metric in SECONDARY_METRIC_KEYS
    }
    scope_summaries: Dict[str, Any] = {}
    for scope in (
        "valid_certified_non_conflict",
        "valid_certified_conflict",
        "valid_unknown_or_uncertified",
        "invalid_output",
    ):
        f1_scope_ids = [
            bundle_id
            for bundle_id in bundle_ids
            if f1[bundle_id].get("secondary_metrics_scope") == scope
        ]
        f2_scope_ids = [
            bundle_id
            for bundle_id in bundle_ids
            if f2[bundle_id].get("secondary_metrics_scope") == scope
        ]
        paired_scope_ids = [
            bundle_id
            for bundle_id in bundle_ids
            if f1[bundle_id].get("secondary_metrics_scope") == scope
            and f2[bundle_id].get("secondary_metrics_scope") == scope
        ]
        scope_summaries[scope] = {
            "F1_n": len(f1_scope_ids),
            "F2_n": len(f2_scope_ids),
            "metrics": {
                metric: {
                    "F1": _descriptive_metric_summary(f1, f1_scope_ids, metric),
                    "F2": _descriptive_metric_summary(f2, f2_scope_ids, metric),
                    "paired": _paired_descriptive_metric_summary(
                        f1,
                        f2,
                        paired_scope_ids,
                        metric,
                    ),
                }
                for metric in SECONDARY_METRIC_KEYS
            },
        }

    return {
        "policy": (
            "All metrics are descriptive only; invalid outputs and unknown-origin "
            "rows remain undefined for these metrics rather than being imputed. "
            "Support-origin metrics are computed only from selected reports "
            "whose benchmark stance is supports."
        ),
        "metrics": all_metrics,
        "scope_summaries": scope_summaries,
    }


def _fixed_set_hash(bundle_ids: Sequence[str]) -> str:
    """Compatibility wrapper for the ordered manifest membership hash."""

    return ordered_membership_sha256(list(bundle_ids))


def _manifest_without_digest(manifest: Mapping[str, Any]) -> Dict[str, Any]:
    return {key: value for key, value in manifest.items() if key != "manifest_sha256"}


def _validate_confirmatory_manifest(
    manifest: Mapping[str, Any],
    gold_by_bundle: Mapping[str, Mapping[str, Any]],
    config: FrozenConfig,
) -> Tuple[List[str], List[str]]:
    """Validate the frozen ordered A/M membership before any denominator work."""

    required = {
        "manifest_version",
        "protocol_version",
        "primary_bundle_ids",
        "primary_bundle_ids_sha256",
        "primary_n",
        "safety_bundle_ids",
        "safety_bundle_ids_sha256",
        "safety_n",
        "safety_definition",
        "manifest_sha256",
    }
    missing = required - set(manifest)
    if missing:
        raise ValueError("confirmatory manifest is missing fields: %s" % sorted(missing))
    if manifest["protocol_version"] != config.protocol_version or manifest["protocol_version"] != "1.0":
        raise ValueError("confirmatory manifest protocol identity is not v1.0")
    if manifest["manifest_sha256"] != sha256_json(_manifest_without_digest(manifest)):
        raise ValueError("confirmatory manifest digest does not match its payload")
    primary_ids = list(manifest["primary_bundle_ids"])
    safety_ids = list(manifest["safety_bundle_ids"])
    if any(not isinstance(value, str) for value in primary_ids + safety_ids):
        raise ValueError("confirmatory manifest memberships must be string IDs")
    if primary_ids != sorted(primary_ids) or safety_ids != sorted(safety_ids):
        raise ValueError("confirmatory manifest memberships must use deterministic sorted order")
    if len(primary_ids) != 300 or manifest["primary_n"] != 300:
        raise ValueError("confirmatory primary A must contain exactly 300 bundles")
    if len(safety_ids) != 75 or manifest["safety_n"] != 75:
        raise ValueError("confirmatory safety M must contain exactly 75 bundles")
    if manifest["primary_bundle_ids_sha256"] != ordered_membership_sha256(primary_ids):
        raise ValueError("primary A membership hash does not match ordered IDs")
    if manifest["safety_bundle_ids_sha256"] != ordered_membership_sha256(safety_ids):
        raise ValueError("safety M membership hash does not match ordered IDs")
    if len(primary_ids) != len(set(primary_ids)) or len(safety_ids) != len(set(safety_ids)):
        raise ValueError("confirmatory manifest memberships must be unique")
    if not set(safety_ids).issubset(primary_ids):
        raise ValueError("safety M must be a subset of primary A")
    if set(primary_ids) - set(gold_by_bundle):
        raise ValueError("primary manifest references missing gold bundles")
    if any(gold_by_bundle[bundle_id].get("split") != "primary" for bundle_id in primary_ids):
        raise ValueError("primary manifest contains a non-primary gold row")
    expected_safety = [
        bundle_id
        for bundle_id in primary_ids
        if gold_by_bundle[bundle_id].get("gold_support_origin_certainty") == "multiple"
    ]
    if expected_safety != safety_ids:
        raise ValueError("safety M does not equal the locked multiple-certainty subset of A")
    if manifest["safety_definition"] != "primary bundles with gold_support_origin_certainty=multiple":
        raise ValueError("safety M definition is not the locked benchmark definition")
    if config.primary_n != 300 or config.split_counts["primary"].get("multiple_origin_convergence") != 75:
        raise ValueError("config does not preserve locked 300/75 denominators")
    return primary_ids, safety_ids


def paired_analysis(
    scores_by_condition: Mapping[str, Mapping[str, Mapping[str, Any]]],
    gold_by_bundle: Mapping[str, Mapping[str, Any]],
    config: Optional[FrozenConfig] = None,
    bootstrap_repetitions: Optional[int] = None,
    manifest: Optional[Mapping[str, Any]] = None,
    analysis_mode: str = "confirmatory",
) -> Dict[str, Any]:
    """Calculate FC/VOR results with an explicit confirmatory denominator.

    Confirmatory analysis is fail-closed on the ordered 300-row primary
    manifest and its fixed 75-row safety subset.  A separately named
    ``descriptive_smoke`` mode exists for tiny offline fixtures and is never a
    primary result.
    """

    config = config or FrozenConfig()
    assert_config_invariants(config)
    if analysis_mode not in {"confirmatory", "descriptive_smoke"}:
        raise ValueError("analysis_mode must be confirmatory or descriptive_smoke")
    if analysis_mode == "confirmatory" and manifest is None:
        raise ValueError("confirmatory analysis requires an explicit primary manifest")
    if set(scores_by_condition) < {"F1", "F2"}:
        raise ValueError("F1 and F2 scores are required")
    if analysis_mode == "confirmatory":
        bundle_ids, fixed_ids = _validate_confirmatory_manifest(manifest, gold_by_bundle, config)
    else:
        bundle_ids = sorted(gold_by_bundle)
        fixed_ids = [
            bundle_id
            for bundle_id in bundle_ids
            if gold_by_bundle[bundle_id]["gold_support_origin_certainty"] == "multiple"
        ]
        if not fixed_ids:
            raise ValueError("fixed safety set M is empty in descriptive smoke mode")
    f1 = scores_by_condition["F1"]
    f2 = scores_by_condition["F2"]
    if set(f1) != set(bundle_ids) or set(f2) != set(bundle_ids):
        raise ValueError("analysis vectors must cover exactly the selected A membership")
    f1_fc = [int(f1[bundle_id]["fc_cons"]) for bundle_id in bundle_ids]
    f2_fc = [int(f2[bundle_id]["fc_cons"]) for bundle_id in bundle_ids]
    repetitions = int(bootstrap_repetitions or config.bootstrap_repetitions)
    fc_low, fc_high = bootstrap_difference(f1_fc, f2_fc, repetitions=repetitions)
    f1_vor = [int(f1[bundle_id]["vor"]) for bundle_id in fixed_ids]
    f2_vor = [int(f2[bundle_id]["vor"]) for bundle_id in fixed_ids]
    vor_low = one_sided_lower_bootstrap(f1_vor, f2_vor, repetitions=repetitions)
    fc_delta = sum(f2_fc) / float(len(f2_fc)) - sum(f1_fc) / float(len(f1_fc))
    vor_delta = sum(f2_vor) / float(len(f2_vor)) - sum(f1_vor) / float(len(f1_vor))
    return {
        "analysis_version": "fixed-denominator-0.1.0",
        "analysis_mode": analysis_mode,
        "primary_unit": "bundle",
        "primary_bundle_ids": bundle_ids,
        "primary_n": len(bundle_ids),
        "primary_manifest_sha256": manifest.get("manifest_sha256") if manifest is not None else None,
        "primary_membership_sha256": _fixed_set_hash(bundle_ids),
        "invalid_outputs_in_primary_denominator": True,
        "fc_cons": {
            "F1_rate": sum(f1_fc) / float(len(f1_fc)),
            "F2_rate": sum(f2_fc) / float(len(f2_fc)),
            "delta_F2_minus_F1": fc_delta,
            "paired_exact_p": paired_exact_pvalue(f1_fc, f2_fc),
            "bootstrap_95_percentile_ci": [fc_low, fc_high],
            "F1_invalid_rate": 1.0 - sum(int(f1[bundle_id]["valid"]) for bundle_id in bundle_ids) / float(len(bundle_ids)),
            "F2_invalid_rate": 1.0 - sum(int(f2[bundle_id]["valid"]) for bundle_id in bundle_ids) / float(len(bundle_ids)),
        },
        "fixed_safety_set_M": {
            "bundle_ids": fixed_ids,
            "n": len(fixed_ids),
            "membership_sha256": _fixed_set_hash(fixed_ids),
            "manifest_membership_sha256": manifest.get("safety_bundle_ids_sha256") if manifest is not None else None,
            "F1_rate": sum(f1_vor) / float(len(f1_vor)),
            "F2_rate": sum(f2_vor) / float(len(f2_vor)),
            "delta_F2_minus_F1": vor_delta,
            "one_sided_95_lower_bootstrap": vor_low,
            "margin": config.safety_margin,
            "noninferiority_guardrail_pass": vor_low > config.safety_margin,
            "invalid_outputs_coded_as_zero": True,
        },
        "secondary_descriptive": _secondary_descriptive_analysis(f1, f2, bundle_ids),
        "confirmatory_decision": {
            "fc_superiority_pass": bool(fc_delta < 0 and paired_exact_pvalue(f1_fc, f2_fc) < config.alpha and fc_high < 0),
            "vor_safety_gate_pass": bool(vor_low > config.safety_margin),
            "bounded_positive_result": bool(fc_delta < 0 and paired_exact_pvalue(f1_fc, f2_fc) < config.alpha and fc_high < 0 and vor_low > config.safety_margin),
        },
        "secondary_policy": "F0 comparisons, claim state, stress, structure, style, and seed slices are descriptive only",
    }
