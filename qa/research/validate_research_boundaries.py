#!/usr/bin/env python3
"""Validate research separation and no-results boundary in active documents."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def require(condition: bool, message: str) -> None:
    if not condition:
        print(f"FAIL  {message}", file=sys.stderr)
        raise SystemExit(1)


def read(relative: str) -> str:
    path = ROOT / relative
    require(path.is_file(), f"missing required file: {relative}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    status = json.loads(read("research/the-echo-problem/qa/EP_V0_1_STATUS.json"))
    expected_classes = [
        "null",
        "rule_only",
        "invalidity_driven",
        "threshold_only_vor",
        "harmful",
        "shortcut_driven",
        "surface_or_semantic_audit_failure",
        "unstable",
        "noise_fragile",
        "nontransfer",
        "stopped_or_quarantined",
    ]
    require(status.get("unfavorable_result_classes") == expected_classes,
            "EP status taxonomy differs from the canonical 11-class sequence")
    boundary = status.get("research_boundary", {})
    require(boundary.get("model_or_provider_calls") == 0,
            "EP status does not record zero model/provider calls")
    require(boundary.get("empirical_study_run") is False,
            "EP status does not record the empirical study as unrun")
    require(boundary.get("participant_study_run") is False,
            "EP status does not record the participant study as unrun")

    separation = read("docs/TWO_PROJECT_SEPARATION.md")
    for token in expected_classes:
        require(f"`{token}`" in separation,
                f"two-project separation omits canonical class {token}")
    require("Remove all Echo-specific examples" in separation,
            "v16-without-Echo removal test is missing")
    require("Remove all v16 claims beyond origin accounting" in separation,
            "Echo-without-v16 removal test is missing")

    agenda = read("research/THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md")
    protocol = read(
        "research/future-studies/DL_PLAYBOOK_MATCHED_BUDGET_PROTOCOL_V0_1.md"
    )
    memo = read(
        "research/future-studies/DL_NARROW_WEDGE_DECISION_MEMO_V0_1.md"
    )
    source_route = read("manuscript/SOURCES_AND_RESEARCH_ROUTE.md")
    claims_ledger = read("docs/CLAIMS_AND_SOURCE_LEDGER_V16.md")
    source_qa = read(
        "qa/research/CURRENT_ADJACENT_SOURCE_VERIFICATION_2026-08-30.md"
    )
    hardening_qa = read(
        "qa/research/RESEARCH_BOUNDARY_HARDENING_QA_2026-08-30.md"
    )
    for label in (
        "Research Track 01",
        "Research Track 02",
        "decision usefulness",
        "supported novelty",
        "evidence diversity",
        "missing-perspective detection",
        "human correction effort",
        "matched",
    ):
        require(label.lower() in agenda.lower(),
                f"research agenda omits required concept: {label}")
        require(label.lower().replace("research track 01", "") in protocol.lower()
                or label.startswith("Research Track"),
                f"future protocol omits required concept: {label}")

    for text, name in ((agenda, "agenda"), (protocol, "protocol")):
        normalized = " ".join(text.lower().split())
        for boundary_phrase in (
            "UNRUN",
            "NO RESULTS",
            "later exact owner instruction",
        ):
            require(boundary_phrase.lower() in normalized,
                    f"{name} omits boundary phrase: {boundary_phrase}")
        require("no model" in normalized or "no provider or model" in normalized,
                f"{name} omits the unselected-model boundary")
        for result_class in (
            "null",
            "harmful",
            "shortcut-driven",
            "fragile",
            "non-transfer",
            "stopped",
        ):
            require(result_class.lower() in text.lower(),
                    f"{name} omits required unfavorable class: {result_class}")

    require("model/provider/version and decoding configuration" in protocol,
            "future protocol does not match model/provider/version")
    require("playbook instructions counted" in protocol,
            "future protocol does not count treatment instruction overhead")
    require("No sample size appears" in protocol,
            "future protocol does not expose its unresolved sample-size gate")

    for text, name in ((agenda, "agenda"), (protocol, "protocol")):
        normalized = " ".join(text.lower().split())
        for phrase in (
            "generic-diligence",
            "mechanism-isolated",
            "fixed-total-resource",
            "equal-operating-overhead",
            "decision accuracy or accepted-error",
        ):
            require(phrase.lower() in normalized,
                    f"{name} omits hardening requirement: {phrase}")
    require("O1 is a required comparator" in protocol,
            "protocol still treats generic diligence as optional")
    require("Only after the required baseline and mechanism-isolation gates"
            in protocol,
            "protocol does not sequence mechanism isolation before omnibus D1")

    for phrase in (
        "Candidate A",
        "Candidate B",
        "Strongest case against",
        "Adjacent work and novelty uncertainty",
        "Construct-validity risks",
        "Credible comparators",
        "Candidate outcomes and guardrails",
        "Resource estimands",
        "Blinding and cue leakage",
        "Permission and participant gates",
        "Unfavorable outcomes and no-go conditions",
        "without selecting a study",
        "NO PROVIDER, MODEL, CORPUS, DATASET, PARTICIPANT",
    ):
        require(phrase.lower() in memo.lower(),
                f"narrow-wedge memo omits required section/boundary: {phrase}")
    for result_class in (
        "null",
        "harmful",
        "shortcut-driven",
        "fragile",
        "non-transfer",
        "stopped",
        "invalid",
        "indeterminate",
    ):
        require(result_class in memo.lower(),
                f"narrow-wedge memo omits unfavorable class: {result_class}")

    normalized_memo = " ".join(memo.lower().split())
    for phrase in (
        "same task, evidence-access boundary, and required output specification",
        "generation study",
        "fixed-answer interface/correction study",
        "generated-answer or decision accuracy is not an eligible outcome",
        "a2 is a **composite treatment**",
        "ablation is predeclared",
    ):
        require(phrase in normalized_memo,
                f"Candidate A design boundary is missing: {phrase}")
    for axis in (
        "**observation:**",
        "**process/capture:**",
        "**access:**",
        "**permission:**",
        "**currency:**",
    ):
        require(axis in memo,
                f"Candidate B omits orthogonal axis: {axis}")
    for phrase in (
        "hold access at `available`, permission at `authorized`, and currency at `current`",
        "frozen task/world key",
        "trace-derived run state",
        "must not be backfilled",
    ):
        require(phrase in normalized_memo,
                f"Candidate B construct boundary is missing: {phrase}")

    require("**2026-08-30**" in source_route,
            "source route omits the current verification date")
    require("checked again immediately before any later-authorized publication"
            in source_route,
            "source route omits the publication-time recheck gate")
    require("was last checked on 2026-08-18" not in source_route,
            "source route retains stale verification language")
    require(re.search(
        r"(?:last checked|last verified|verified) on (?!2026-08-30)"
        r"\d{4}-\d{2}-\d{2}",
        source_route,
        flags=re.IGNORECASE,
    ) is None,
            "source route contains an older undifferentiated verification date")
    require("targeted wayfinding route, not a systematic or exhaustive"
            in source_route,
            "source route inflates targeted wayfinding into an exhaustive review")
    revised_component_boundary = (
        "component areas have substantial established and active prior work"
    )
    for text, name in (
        (source_route, "source route"),
        (agenda, "research agenda"),
        (hardening_qa, "research hardening QA"),
    ):
        require(revised_component_boundary in text.lower(),
                f"{name} omits the revised adjacent-work boundary")
        require("component practices are established" not in text.lower(),
                f"{name} retains the overbroad established-practices sentence")
    normalized_source_route = " ".join(source_route.split())
    for phrase in (
        "not a novel mechanism",
        "exhaustive taxonomy",
        "technical layer",
        "demonstrated improvement",
    ):
        require(phrase in normalized_source_route,
                f"source route omits contribution ceiling: {phrase}")

    current_urls = (
        "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
        "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents",
        "https://aclanthology.org/2025.findings-emnlp.303/",
        "https://aclanthology.org/2026.lrec-1.53/",
        "https://aclanthology.org/2025.emnlp-main.1738/",
        "https://arxiv.org/abs/2608.13956",
        "https://aclanthology.org/2025.emnlp-main.22/",
        "https://aclanthology.org/2026.acl-long.1185/",
        "https://arxiv.org/abs/2507.05257",
        "https://arxiv.org/abs/2507.04480",
        "https://aclanthology.org/2025.findings-acl.1087/",
        "https://aclanthology.org/2026.acl-long.1586/",
        "https://iclr.cc/virtual/2026/poster/10010639",
        "https://arxiv.org/abs/2506.11763",
        "https://aclanthology.org/2025.findings-emnlp.720/",
    )
    for url in current_urls:
        require(url in source_route,
                f"current source route omits verified primary/official URL: {url}")
        require(url in source_qa,
                f"source QA omits verification record for URL: {url}")
    require("PARTIAL / RECHECK AT PUBLICATION" in source_qa,
            "source QA conceals partial resolver checks")
    require("No systematic-search completeness" in source_qa,
            "source QA omits its non-exhaustive evidence ceiling")

    for claim_id in ("C16-014", "C16-016", "C16-017"):
        require(claim_id in claims_ledger,
                f"claims ledger omits current research claim: {claim_id}")
    for phrase in (
        "authored human-governed design/governance synthesis",
        "novel mechanism",
        "model/provider/corpus",
    ):
        require(phrase.lower() in claims_ledger.lower(),
                f"claims ledger omits current claim boundary: {phrase}")

    active_claim_text = "\n".join(
        (source_route, claims_ledger, agenda, protocol, memo)
    )
    forbidden_assertions = (
        r"\bPattern Map (?:proves|validates|improves)\b",
        r"\bThe Discrimination Layer (?:proves|validates|improves)\b",
        r"\bthe (?:framework|playbook) is effective\b",
        r"\bhas been empirically validated\b",
        r"\bstudy results show that (?:Pattern Map|the Discrimination Layer)\b",
        r"\b(?:nobody has studied|no prior work exists|the field is empty|unoccupied field)\b",
        r"\b(?:Pattern Map|the Discrimination Layer) is a novel mechanism\b",
    )
    for pattern in forbidden_assertions:
        require(re.search(pattern, active_claim_text, flags=re.IGNORECASE) is None,
                f"active research copy contains inflated assertion: {pattern}")

    print("PASS  Echo/v16 separation and exact unfavorable taxonomy")
    print("PASS  broader agenda and matched-budget protocol containment")
    print("PASS  mechanism-isolation sequencing and narrow-wedge containment")
    print("PASS  current targeted source route and publication-time recheck gate")
    print("PASS  novelty/effectiveness/result-inflation guard")
    print("PASS  no-results and future-authorization boundaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
