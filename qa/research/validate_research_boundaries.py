#!/usr/bin/env python3
"""Validate research separation and no-results boundary in active documents."""

from __future__ import annotations

import json
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

    print("PASS  Echo/v16 separation and exact unfavorable taxonomy")
    print("PASS  broader agenda and matched-budget protocol containment")
    print("PASS  no-results and future-authorization boundaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
