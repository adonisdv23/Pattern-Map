#!/usr/bin/env python3
"""Focused structural QA for the v16 applied-framework lane.

This script checks artifact structure and guardrails only. It is not an
effectiveness evaluation and does not execute a model, provider, study, or
external action.
"""

from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

ORDINARY_ELIGIBILITY_CONTRACT = (
    "Ordinary is valid only for a reversible transformation of user-supplied "
    "material that requires no material claim judgment, comparison, selection "
    "or withholding, permission resolution, memory reuse, new acquisition, or "
    "externally consequential influence."
)
ORDINARY_TERMINAL_CONTRACT = (
    "The four-field ordinary record is terminal; it is not an ANSWER, route, "
    "stop, learning, or influence receipt."
)
ORDINARY_AUTHORITY_CONTRACT = (
    "Stage 0 grants no external-action authority; externally consequential "
    "action remains with an explicitly authorized human."
)
BUDGET_COMPLEXITY_CONTRACT = (
    "A budget records capacity and constraint; it cannot independently justify "
    "advanced machinery."
)
ADVANCED_ROUTE_CONTRACT = (
    "Advanced is justified only when consequence is high, uncertainty is high, "
    "and substantial capacity has been separately approved; volume, reuse, or "
    "longevity may shape capabilities inside the chosen level but do not "
    "independently select it."
)
ORDINARY_CONTRACT_FILES = (
    "framework/agent-playbook/QUICKSTART.md",
    "framework/agent-playbook/FULL_OPERATING_GUIDE.md",
    "framework/agent-playbook/COPYABLE_AGENT_BRIEF.md",
    "framework/agent-playbook/PREFLIGHT_CHECKLIST.md",
    "framework/templates/ORDINARY_RECORD.md",
    "framework/IMPLEMENTATION_CHOICES.md",
)
BUDGET_CONTRACT_FILES = (
    "framework/agent-playbook/QUICKSTART.md",
    "framework/agent-playbook/FULL_OPERATING_GUIDE.md",
    "framework/agent-playbook/COPYABLE_AGENT_BRIEF.md",
    "framework/IMPLEMENTATION_CHOICES.md",
)
ADVANCED_CONTRACT_FILES = BUDGET_CONTRACT_FILES


class CheckFailure(Exception):
    """Raised for a focused QA failure."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def read_text(relative: str) -> str:
    path = ROOT / relative
    require(path.is_file(), f"missing required file: {relative}")
    return path.read_text(encoding="utf-8")


def load_json(relative: str) -> dict:
    try:
        value = json.loads(read_text(relative))
    except json.JSONDecodeError as exc:
        raise CheckFailure(f"invalid JSON in {relative}: {exc}") from exc
    require(isinstance(value, dict), f"{relative} must contain a JSON object")
    return value


def normalized_text(value: str) -> str:
    """Collapse formatting whitespace for cross-artifact prose contracts."""

    return " ".join(value.split())


def qa_ordinary_eligibility(case: dict[str, bool]) -> bool:
    """Evaluate the Stage 0 truth table for QA only, never as a runtime router."""

    expected = {
        "reversible",
        "supplied_material_only",
        "material_claim_judgment",
        "comparison",
        "selection_or_withholding",
        "permission_resolution",
        "memory_reuse",
        "new_acquisition",
        "externally_consequential_influence",
    }
    require(set(case) == expected and all(isinstance(value, bool) for value in case.values()),
            "Stage 0 QA case does not use the exact boolean contract")
    disqualifiers = (
        "material_claim_judgment",
        "comparison",
        "selection_or_withholding",
        "permission_resolution",
        "memory_reuse",
        "new_acquisition",
        "externally_consequential_influence",
    )
    return (
        case["reversible"]
        and case["supplied_material_only"]
        and not any(case[key] for key in disqualifiers)
    )


def validate_stage_zero_contract() -> None:
    """Lock the corrected ordinary-path boundary across every copied entry point."""

    eligibility = normalized_text(ORDINARY_ELIGIBILITY_CONTRACT)
    terminal = normalized_text(ORDINARY_TERMINAL_CONTRACT)
    authority = normalized_text(ORDINARY_AUTHORITY_CONTRACT)
    for relative in ORDINARY_CONTRACT_FILES:
        content = normalized_text(read_text(relative))
        require(eligibility in content,
                f"{relative} does not carry the complete ordinary eligibility contract")
        require(terminal in content,
                f"{relative} does not keep the four-field ordinary record terminal")
        require(authority in content,
                f"{relative} does not keep external action under explicit human authority")

    budget_contract = normalized_text(BUDGET_COMPLEXITY_CONTRACT)
    for relative in BUDGET_CONTRACT_FILES:
        require(budget_contract in normalized_text(read_text(relative)),
                f"{relative} lets budget independently imply advanced machinery")

    advanced_contract = normalized_text(ADVANCED_ROUTE_CONTRACT)
    for relative in ADVANCED_CONTRACT_FILES:
        require(advanced_contract in normalized_text(read_text(relative)),
                f"{relative} diverges from the three-condition Advanced rule")

    for relative in (
        "framework/agent-playbook/QUICKSTART.md",
        "framework/agent-playbook/FULL_OPERATING_GUIDE.md",
        "framework/agent-playbook/COPYABLE_AGENT_BRIEF.md",
    ):
        content = normalized_text(read_text(relative)).lower()
        require("information beyond the user-supplied material" not in content
                and "information beyond what the user supplied" not in content,
                f"{relative} retains the ambiguous beyond-supplied Stage 0 gate")

    full_guide = normalized_text(
        read_text("framework/agent-playbook/FULL_OPERATING_GUIDE.md")
    ).lower()
    require("summarization, or creative transformation of supplied material normally stays ordinary"
            not in full_guide,
            "full guide still defaults supplied-material summarization to ordinary")
    require("they do not qualify automatically" in full_guide,
            "full guide does not correct the supplied-material transformation ambiguity")

    ordinary_template = read_text("framework/templates/ORDINARY_RECORD.md")
    field_labels = re.findall(r"^- ([A-Za-z ]+):\s*$", ordinary_template, re.MULTILINE)
    require(field_labels == [
                "Supplied scope",
                "Material assumptions",
                "Unchecked boundaries",
                "Output",
            ],
            "ordinary template must expose exactly four ordered fields")

    copyable_brief = read_text("framework/agent-playbook/COPYABLE_AGENT_BRIEF.md")
    copied_prompt = copyable_brief.split("~~~text", 1)[1].split("~~~", 1)[0]
    copied_ordinary = copied_prompt.split("ORDINARY_RECORD:", 1)[1].split(
        "Then stop.", 1
    )[0]
    copied_fields = re.findall(
        r"^\s+- ([a-z_]+):\s*$", copied_ordinary, re.MULTILINE
    )
    require(copied_fields == [
                "supplied_scope",
                "assumptions",
                "unchecked_boundaries",
                "output",
            ],
            "copied ordinary record must expose exactly four ordered fields")

    ordinary_fixture = load_json("qa/applied/receipts/ordinary-supplied-material.json")
    fixture_text = normalized_text(json.dumps(ordinary_fixture, sort_keys=True)).lower()
    for phrase in (
        "without changing, reordering, selecting, or omitting any supplied content",
        "no claim was judged",
        "no comparison, selection or withholding, permission resolution, memory reuse, "
        "new acquisition, or external influence was performed",
    ):
        require(phrase in fixture_text,
                f"ordinary fixture does not demonstrate the corrected boundary: {phrase}")

    ordinary_control = {
        "reversible": True,
        "supplied_material_only": True,
        "material_claim_judgment": False,
        "comparison": False,
        "selection_or_withholding": False,
        "permission_resolution": False,
        "memory_reuse": False,
        "new_acquisition": False,
        "externally_consequential_influence": False,
    }
    require(qa_ordinary_eligibility(ordinary_control),
            "Stage 0 QA rejected the exact reversible supplied-material control")

    disqualifying_mutations = {
        "irreversible transformation": {"reversible": False},
        "material beyond supplied input": {"supplied_material_only": False},
        "material claim judgment": {"material_claim_judgment": True},
        "comparison within supplied input": {"comparison": True},
        "selection or withholding within supplied input": {
            "selection_or_withholding": True,
        },
        "permission resolution": {"permission_resolution": True},
        "prior-memory reuse": {"memory_reuse": True},
        "new acquisition": {"new_acquisition": True},
        "externally consequential influence": {
            "externally_consequential_influence": True,
        },
    }
    for label, mutation in disqualifying_mutations.items():
        case = ordinary_control | mutation
        require(not qa_ordinary_eligibility(case),
                f"Stage 0 QA admitted {label} to the ordinary path")

    supplied_summary = ordinary_control | {
        "material_claim_judgment": True,
        "selection_or_withholding": True,
    }
    require(not qa_ordinary_eligibility(supplied_summary),
            "Stage 0 QA admitted a selective supplied-material summary as ordinary")


def validate_spec() -> None:
    spec = load_json("framework/SIX_FAMILIES.json")
    schema = load_json("framework/SIX_FAMILIES.schema.json")

    required_top = {
        "schema_version",
        "framework_id",
        "status",
        "description",
        "public_map",
        "families",
        "invariants",
        "implementation_note",
    }
    require(required_top <= set(spec), "six-family JSON is missing top-level keys")
    require(spec["schema_version"] == "pattern-map.six-families.v16", "wrong schema version")
    require(spec["framework_id"] == "pattern-map-discrimination-layer-v16", "wrong framework ID")
    require(spec["public_map"] is True, "six-family map must be public_map true")
    require(isinstance(spec["families"], list) and len(spec["families"]) == 6,
            "six-family JSON must contain exactly six families")
    require(schema["title"].startswith("Pattern Map v16"), "local schema is not the v16 schema")

    expected = [
        ("F1", "peripheral-signal", "Peripheral signal"),
        ("F2", "source-weighing", "Source weighing"),
        ("F3", "velocity-motion", "Velocity / motion"),
        ("F4", "absence-memory", "Absence + memory"),
        ("F5", "structured-patterns", "Structured patterns"),
        ("F6", "learning-loop", "Learning loop"),
    ]
    family_schema = schema["properties"]["families"]
    identity_contract = family_schema["allOf"][0]
    require(identity_contract.get("items") is False,
            "schema must reject family entries beyond the ordered six")
    prefix_items = identity_contract.get("prefixItems")
    require(isinstance(prefix_items, list) and len(prefix_items) == 6,
            "schema must express six ordered family identities")
    schema_identity = [
        (
            entry["properties"]["id"]["const"],
            entry["properties"]["slug"]["const"],
            entry["properties"]["name"]["const"],
        )
        for entry in prefix_items
    ]
    require(schema_identity == expected,
            "schema does not lock the exact ordered F1-F6 ID/slug/name tuple")
    seen = []
    family_keys = {
        "id",
        "slug",
        "name",
        "reader_question",
        "purpose",
        "mechanism",
        "inputs",
        "observable_actions",
        "outputs",
        "dependencies",
        "failure_modes",
        "boundaries",
        "implementation_levels",
        "when_not_to_use",
    }
    for family, expected_pair in zip(spec["families"], expected):
        require(isinstance(family, dict), "each family must be an object")
        require(family_keys <= set(family), f"{expected_pair[0]} is missing family keys")
        observed_identity = (family["id"], family["slug"], family["name"])
        require(observed_identity == expected_pair,
                f"family mismatch: expected {expected_pair}, got {observed_identity}")
        require(family["implementation_levels"].keys()
                == {"lightweight", "moderate", "advanced"},
                f"{family['id']} must expose all implementation levels")
        for key in ("inputs", "observable_actions", "outputs", "failure_modes",
                    "boundaries", "when_not_to_use"):
            require(isinstance(family[key], list) and family[key],
                    f"{family['id']} field {key} must be a non-empty list")
        seen.append(family["name"])
    require(seen == [name for _, _, name in expected], "family order is not stable")
    require(len(spec["invariants"]) >= 8, "six-family invariants are incomplete")

    markdown = read_text("framework/SIX_FAMILIES.md")
    for family_name in seen:
        require(family_name in markdown, f"{family_name} missing from Markdown map")
    for phrase in (
        "Peripheral is a candidate status",
        "Recurrence is not independent corroboration",
        "Provenance is not correctness",
        "Technical access is not operational permission",
        "Outcome learning proposes bounded updates",
    ):
        require(phrase in markdown, f"missing invariant in Markdown map: {phrase}")


def validate_artifact_inventory() -> None:
    required = [
        "framework/SIX_FAMILIES.md",
        "framework/SIX_FAMILIES.json",
        "framework/SIX_FAMILIES.schema.json",
        "framework/GLOSSARY.md",
        "framework/RELATIONSHIP_MAP.md",
        "framework/MECHANISMS.md",
        "framework/IMPLEMENTATION_CHOICES.md",
        "framework/OPERATOR_PLAYBOOK.md",
        "framework/BOUNDARIES_AND_FAILURES.md",
        "framework/templates/DECISION_BRIEF.md",
        "framework/templates/ORDINARY_RECORD.md",
        "framework/templates/ACQUISITION_RECEIPT.md",
        "framework/templates/EVIDENCE_REGISTER.md",
        "framework/templates/COMPARISON_MATRIX.md",
        "framework/templates/DISCONFIRMATION_LOG.md",
        "framework/templates/INFLUENCE_RECEIPT.md",
        "framework/templates/OUTCOME_REVIEW.md",
        "framework/templates/MEMORY_RECORD.md",
        "framework/agent-playbook/QUICKSTART.md",
        "framework/agent-playbook/FULL_OPERATING_GUIDE.md",
        "framework/agent-playbook/COPYABLE_AGENT_BRIEF.md",
        "framework/agent-playbook/PREFLIGHT_CHECKLIST.md",
        "framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md",
        "framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md",
        "cases/signal-foundry/README.md",
        "cases/general-research/README.md",
        "cases/product-and-process/README.md",
    ]
    for relative in required:
        require((ROOT / relative).stat().st_size > 0, f"empty required artifact: {relative}")

    evidence_register = read_text("framework/templates/EVIDENCE_REGISTER.md")
    require("Source role / authority" not in evidence_register,
            "evidence register collapses source role and claim-scoped authority")
    require("| Source role | Relevant track-record evidence | Claim-scoped authority |" in evidence_register,
            "evidence register must keep source role, track record, and claim-scoped authority separate")
    require("never a universal score" in evidence_register,
            "evidence register does not scope track record or reject a universal score")

    decision_receipt = read_text("framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md")
    disposition_section = decision_receipt.split("## Disposition", 1)[1].split(
        "## Outcome learning", 1
    )[0]
    require("ESCALATED:" not in disposition_section,
            "decision receipt treats the ESCALATE route as a human disposition")
    require("`ESCALATE` belongs in the route field" in disposition_section,
            "decision receipt does not explain route-versus-disposition separation")

    operator_playbook = read_text("framework/OPERATOR_PLAYBOOK.md")
    require("| Later outcome conflicts with expectation | OUTCOME_REVIEW |" not in operator_playbook,
            "operator playbook treats OUTCOME_REVIEW as a route")
    require("outcome-learning review, not a route" in operator_playbook,
            "operator playbook does not distinguish learning review from route state")

    influence_receipt = read_text("framework/templates/INFLUENCE_RECEIPT.md")
    selected_material = influence_receipt.split("## Selected material", 1)[1].split(
        "## Withheld material", 1
    )[0]
    require("AUTHORIZED / UNKNOWN" not in selected_material,
            "influence receipt permits unknown-authority material to influence output")
    require("preserve `UNKNOWN`" in influence_receipt
            and "belongs in Withheld material" in influence_receipt,
            "influence receipt does not route unresolved permission to withheld material")

    glossary = read_text("framework/GLOSSARY.md")
    require("| Source track record |" in glossary,
            "glossary omits the owner-locked source track-record dimension")

    all_text = "\n".join(read_text(relative) for relative in required if relative.endswith(".md"))
    for phrase in (
        "peripheral is a candidate",
        "recurrence is not",
        "provenance is not correctness",
        "technical access is not permission",
        "bounded update",
        "NOT_AUTHORIZED",
        "STOPPED_BUDGET",
    ):
        require(phrase.lower() in all_text.lower(),
                f"cross-file boundary phrase missing: {phrase}")

    signal = read_text("cases/signal-foundry/README.md").lower()
    require("illustration_only" in signal, "Signal Foundry case lacks illustration status")
    require("not_validation" in signal, "Signal Foundry case lacks validation boundary")
    require("not performed" in signal, "Signal Foundry case does not state unperformed operations")
    require("no row grants permission" in signal, "Signal Foundry permission boundary is incomplete")
    require("illustrative cost and stop envelope" in signal,
            "Signal Foundry case lacks a fixture-scoped cost/stop envelope")
    require("zero provider calls" in signal and "resume only" in signal,
            "Signal Foundry cost, stop, or resume boundary is incomplete")

    implementation = read_text("framework/IMPLEMENTATION_CHOICES.md")
    require("team process" in implementation and "model adaptation" in implementation,
            "implementation choices do not expose the bounded v13 path continuity")
    require("No path is inherently deeper" in implementation,
            "implementation path continuity lacks its anti-hierarchy boundary")

    route_values = {
        "ACQUIRE",
        "COMPARE",
        "CLARIFY",
        "ANSWER",
        "ANSWER_PROVISIONALLY",
        "HOLD",
        "DEFER",
        "ESCALATE",
        "REFUSE",
    }
    stop_values = {
        "CONTINUE",
        "COMPLETE",
        "STOPPED_BUDGET",
        "STOPPED_DEADLINE",
        "STOPPED_OTHER",
    }
    learning_values = {
        "LEARNING_PLANNED",
        "LEARNING_PENDING_OUTCOME",
        "LEARNING_REVIEWED",
        "LEARNING_NOT_APPLICABLE",
    }
    vocabulary_files = (
        "framework/MECHANISMS.md",
        "framework/GLOSSARY.md",
        "framework/agent-playbook/QUICKSTART.md",
        "framework/agent-playbook/FULL_OPERATING_GUIDE.md",
        "framework/agent-playbook/COPYABLE_AGENT_BRIEF.md",
        "framework/agent-playbook/PREFLIGHT_CHECKLIST.md",
        "framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md",
    )
    for relative in vocabulary_files:
        content = read_text(relative)
        for value in route_values | stop_values | learning_values:
            require(value in content,
                    f"{relative} is missing canonical route/stop/learning value {value}")

    mechanisms = read_text("framework/MECHANISMS.md")
    require("UNAUTHORIZED" not in mechanisms,
            "Mechanisms uses UNAUTHORIZED instead of canonical NOT_AUTHORIZED")
    boundaries = read_text("framework/BOUNDARIES_AND_FAILURES.md")
    require("Record STOPPED or ESCALATED" not in boundaries,
            "boundaries file uses noncanonical bare STOPPED/ESCALATED states")
    require("closed as STOPPED" not in boundaries,
            "boundaries file uses noncanonical bare STOPPED status")
    require("`ESCALATE`" in boundaries and "`STOPPED_OTHER`" in boundaries,
            "boundaries file does not distinguish canonical route and stop values")

    relationship = read_text("framework/RELATIONSHIP_MAP.md")
    for value in route_values:
        require(value in relationship,
                f"relationship map is missing canonical route value {value}")
    relationship_words = " ".join(relationship.split())
    require("output descriptions, not additional routes" in relationship_words,
            "relationship map does not distinguish packet outputs from routes")

    signal_routes = read_text("cases/signal-foundry/README.md")
    for value in ("ANSWER", "ANSWER_PROVISIONALLY", "HOLD", "ESCALATE"):
        require(value in signal_routes,
                f"Signal Foundry procedure is missing canonical route value {value}")
    signal_route_words = " ".join(signal_routes.split())
    require("Packet names describe outputs" in signal_route_words,
            "Signal Foundry procedure does not distinguish packet outputs from routes")

    quickstart = read_text("framework/agent-playbook/QUICKSTART.md")
    require("compare the observed outcome" in quickstart,
            "Quickstart does not close the learning loop")
    require("OUTCOME_REVIEW.md" in quickstart,
            "Quickstart does not point to the outcome-review artifact")
    require("relevant track-record evidence" in quickstart,
            "Quickstart omits the owner-locked F2 track-record dimension")

    preflight = read_text("framework/agent-playbook/PREFLIGHT_CHECKLIST.md")
    require(preflight.count("Group status: PASS / FAIL / UNKNOWN / NOT_APPLICABLE") == 8,
            "preflight does not capture a status for every P-group")
    require("PASS groups / evidence" in preflight
            and "NOT_APPLICABLE groups / reason" in preflight,
            "preflight receipt does not preserve status evidence and N/A reasons")
    require("NOT_AUTHORIZED_OR_AMBIGUOUS" not in preflight,
            "preflight collapses absent permission and unknown permission")
    for state in ("`NOT_AUTHORIZED`", "`UNKNOWN`", "`REVOKED`"):
        require(state in preflight,
                f"preflight does not preserve typed permission stop state {state}")

    require("preserve UNKNOWN and escalate" in quickstart,
            "Quickstart collapses unknown permission into NOT_AUTHORIZED")
    copyable_brief = read_text("framework/agent-playbook/COPYABLE_AGENT_BRIEF.md")
    for state in ("AUTHORIZED", "UNKNOWN", "NOT_AUTHORIZED", "REVOKED"):
        require(state in copyable_brief,
                f"copyable brief omits typed permission state {state}")

    fence_parts = copyable_brief.split("~~~text", 1)
    require(len(fence_parts) == 2 and "~~~" in fence_parts[1],
            "copyable brief is missing its advertised fenced prompt")
    copied_prompt = fence_parts[1].split("~~~", 1)[0]
    require("0. STAGE 0" in copied_prompt,
            "Stage 0 is outside the copied prompt")
    require(copied_prompt.index("0. STAGE 0") < copied_prompt.index("1. FRAME"),
            "Stage 0 must occur before FRAME in the copied prompt")
    require("0A. SCOPE THE ROUTE" in copied_prompt,
            "copyable brief does not scope the smallest layered route")
    require(copied_prompt.index("0. STAGE 0")
            < copied_prompt.index("0A. SCOPE THE ROUTE")
            < copied_prompt.index("1. FRAME"),
            "route scoping must follow Stage 0 and precede FRAME")
    for level in ("LIGHTWEIGHT", "MODERATE", "ADVANCED"):
        require(level in copied_prompt,
                f"copyable route scoping omits {level}")
    require("A higher level is not better" in copied_prompt,
            "copyable route scoping implies that more machinery is better")
    for field in ("supplied_scope:", "assumptions:",
                  "unchecked_boundaries:", "output:"):
        require(field in copied_prompt,
                f"copied ordinary record is missing {field}")
    for phrase in ("Then stop", "Do not continue to FRAME",
                   "do not create evidence, route, stop"):
        require(phrase.lower() in copied_prompt.lower(),
                f"copied Stage 0 lacks terminal boundary: {phrase}")

    require("| Low consequence, reversible, supplied material only | ORDINARY_PATH | ANSWER |"
            not in preflight,
            "preflight still converts the ordinary terminal record into ANSWER")

    ordinary_template = read_text("framework/templates/ORDINARY_RECORD.md")
    for field in ("Supplied scope", "Material assumptions",
                  "Unchecked boundaries", "Output"):
        require(field in ordinary_template,
                f"ordinary template is missing {field}")
    for forbidden in ("Route:", "Stop status:", "Learning status:",
                      "Family record", "Evidence register"):
        require(forbidden not in ordinary_template,
                f"ordinary template contains layered field {forbidden}")

    for relative in (
        "framework/templates/DECISION_BRIEF.md",
        "framework/templates/ACQUISITION_RECEIPT.md",
        "framework/templates/EVIDENCE_REGISTER.md",
        "framework/templates/INFLUENCE_RECEIPT.md",
        "framework/templates/MEMORY_RECORD.md",
        "framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md",
    ):
        content = read_text(relative)
        for state in PERMISSION_STATES:
            require(state in content,
                    f"{relative} omits typed permission state {state}")

    general_case = read_text("cases/general-research/README.md")
    for family in ("F3 Velocity / motion", "F6 Learning loop"):
        row = next((line for line in general_case.splitlines()
                    if line.startswith(f"| {family} |")), "")
        require("| NOT_USED |" in row and row.rstrip().endswith("| NONE |"),
                f"general-research fixture does not keep {family} inactive without an artifact")
    require(general_case.count("| NOT_USED |") >= 2,
            "general-research fixture must leave at least two families inactive")
    require("Comparison disposition: `PERFORMED`" in general_case
            and "Disconfirmation disposition: `PERFORMED`" in general_case,
            "general-research fixture does not bind its answer to substantive checks")
    require("No self-asserted motion count" in general_case,
            "general-research fixture invents a motion artifact for an inactive family")

    full_guide = read_text("framework/agent-playbook/FULL_OPERATING_GUIDE.md")
    for phrase in (
        "at least two distinct instants",
        "separately frozen initial anchor",
        "only `CURRENT`, `AUTHORIZED` memory",
        "comparison uses `NOT_APPLICABLE`; disconfirmation uses `SKIPPED`",
        "`authorized`, `permission_granted`, or",
    ):
        require(phrase in full_guide,
                f"full guide is missing applied integrity contract: {phrase}")

    memory_template = read_text("framework/templates/MEMORY_RECORD.md")
    for phrase in (
        "canonical UTF-8 payload bytes",
        "separately frozen root anchor",
        "exactly one `CURRENT` record",
        "`SUPERSEDED` record intact",
    ):
        require(phrase in memory_template,
                f"memory template is missing append-only contract: {phrase}")

    decision_receipt = read_text("framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md")
    for phrase in (
        "Comparison disposition: PERFORMED / NOT_APPLICABLE",
        "Disconfirmation disposition: PERFORMED / SKIPPED",
        "Only a `CURRENT`, `AUTHORIZED` memory record",
    ):
        require(phrase in decision_receipt,
                f"decision receipt is missing applied integrity field: {phrase}")

    for relative in ("cases/general-research/README.md", "cases/product-and-process/README.md"):
        case = read_text(relative).lower()
        require("illustrative fixture" in case, f"{relative} is not marked as a fixture")
        require("not empirical" in case, f"{relative} lacks non-empirical boundary")
        require("human" in case and "permission" in case, f"{relative} lacks human/permission boundary")


PERMISSION_STATES = {"AUTHORIZED", "UNKNOWN", "NOT_AUTHORIZED", "REVOKED"}
PERMISSION_REASON_CODES = {
    "AUTHORIZED": "AUTHORIZED_FOR_PURPOSE",
    "UNKNOWN": "PERMISSION_NOT_ESTABLISHED",
    "NOT_AUTHORIZED": "PERMISSION_ABSENT",
    "REVOKED": "PERMISSION_REVOKED",
}
ROUTES = {
    "ACQUIRE", "COMPARE", "CLARIFY", "ANSWER", "ANSWER_PROVISIONALLY",
    "HOLD", "DEFER", "ESCALATE", "REFUSE",
}
STOP_STATUSES = {
    "CONTINUE", "COMPLETE", "STOPPED_BUDGET", "STOPPED_DEADLINE",
    "STOPPED_OTHER",
}
MEMORY_ANCHOR_REGISTRY = "qa/applied/memory_anchor_registry.json"
EXACT_POINTER_PATTERN = re.compile(r"^[a-z][a-z0-9+.-]*://[^#\s]+#[^#\s]+$")
TIME_BEARING_PATTERN = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$"
)
DIGEST_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")
LEGACY_AUTHORIZATION_KEYS = {"authorized", "permission_granted", "is_authorized"}


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def require_string(value: object, message: str) -> None:
    require(nonempty(value), message)


def require_substantive_string(value: object, message: str) -> None:
    require(nonempty(value)
            and len(str(value).split()) >= 3
            and str(value).strip().upper() not in {
                "NOT_APPLICABLE", "UNKNOWN", "NONE", "DONE", "PASS"},
            message)


def require_string_list(value: object, message: str, *, allow_empty: bool = False) -> None:
    require(isinstance(value, list), message)
    if not allow_empty:
        require(bool(value), message)
    require(all(nonempty(item) for item in value), message)


def canonical_payload_digest(payload: object) -> str:
    """Hash the canonical UTF-8 JSON bytes used by the fixture contract."""

    canonical = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def parse_utc_observed_at(value: object, filename: str, record_id: str) -> datetime:
    """Parse the contract's UTC-Z timestamp and reject impossible instants."""

    require(isinstance(value, str)
            and TIME_BEARING_PATTERN.fullmatch(value) is not None,
            f"{filename}: {record_id} lacks a UTC-Z observation timestamp")
    try:
        instant = datetime.fromisoformat(f"{value[:-1]}+00:00")
    except ValueError as exc:
        raise CheckFailure(
            f"{filename}: {record_id} has an impossible observation instant"
        ) from exc
    require(instant.tzinfo is not None and instant.utcoffset() == timedelta(0),
            f"{filename}: {record_id} observation timestamp is not UTC")
    return instant


def validate_requirement_disposition(
    value: object,
    records: list[dict],
    filename: str,
    *,
    label: str,
    inactive_status: str,
) -> str:
    """Bind a performed check to records or preserve one bounded skip reason."""

    require(isinstance(value, dict) and set(value) == {"status", "reason"},
            f"{filename}: {label} disposition must contain status and reason only")
    status = value["status"]
    require(status in {"PERFORMED", inactive_status},
            f"{filename}: {label} disposition is not typed")
    reason = value["reason"]
    require_string(reason, f"{filename}: {label} disposition lacks a reason")
    require("\n" not in reason and len(reason) <= 240,
            f"{filename}: {label} disposition reason must be one bounded line")
    if status == "PERFORMED":
        require(reason == "SUBSTANTIVE_RECORDS_LINKED",
                f"{filename}: performed {label} must name linked substantive records")
        require(bool(records),
                f"{filename}: performed {label} needs a substantive record")
    else:
        require(not records,
                f"{filename}: inactive {label} cannot carry performed records")
        require(reason not in {"NOT_APPLICABLE", "SKIPPED", "SUBSTANTIVE_RECORDS_LINKED"},
                f"{filename}: inactive {label} needs one bounded task-specific reason")
    return status


def validate_outcome(receipt: dict, filename: str) -> None:
    outcome = receipt.get("outcome")
    require(isinstance(outcome, dict),
            f"{filename}: outcome must be an exact status-discriminated object")
    require(isinstance(outcome.get("applicable"), bool),
            f"{filename}: outcome applicable must be a real boolean")
    learning_statuses = {
        "LEARNING_PLANNED",
        "LEARNING_PENDING_OUTCOME",
        "LEARNING_REVIEWED",
        "LEARNING_NOT_APPLICABLE",
    }
    require(outcome.get("learning_status") in learning_statuses,
            f"{filename}: outcome needs a canonical learning status")
    status = outcome["learning_status"]
    if outcome["applicable"] is False:
        require(set(outcome) == {"applicable", "learning_status"},
                f"{filename}: non-applicable outcome cannot carry expectation, result, review, disposition, or update fields")
        require(status == "LEARNING_NOT_APPLICABLE",
                f"{filename}: non-applicable outcome must say LEARNING_NOT_APPLICABLE")
        return

    pre_review_keys = {
        "applicable", "learning_status", "expectation_recorded",
        "outcome_window_recorded", "update_applied",
    }
    if status == "LEARNING_PLANNED":
        require(set(outcome) == pre_review_keys,
                f"{filename}: LEARNING_PLANNED must use only the planning-state keys")
        require(outcome["expectation_recorded"] is False
                and outcome["outcome_window_recorded"] is False,
                f"{filename}: LEARNING_PLANNED precedes expectation and window lock")
        require(outcome["update_applied"] is False,
                f"{filename}: LEARNING_PLANNED cannot apply an update")
        return

    if status == "LEARNING_PENDING_OUTCOME":
        require(set(outcome) == pre_review_keys,
                f"{filename}: LEARNING_PENDING_OUTCOME cannot carry result, review, disposition, or extra fields")
        require(outcome["expectation_recorded"] is True
                and outcome["outcome_window_recorded"] is True,
                f"{filename}: LEARNING_PENDING_OUTCOME needs locked expectation and outcome window")
        require(outcome["update_applied"] is False,
                f"{filename}: LEARNING_PENDING_OUTCOME cannot apply an update")
        return

    reviewed_keys = pre_review_keys | {
        "review_recorded", "observed_outcome", "missing_outcome_reason",
        "human_disposition",
    }
    require(status == "LEARNING_REVIEWED",
            f"{filename}: applicable outcome has an incompatible learning status")
    require(set(outcome) == reviewed_keys,
            f"{filename}: LEARNING_REVIEWED must use the exact reviewed-state keys")
    require(outcome["expectation_recorded"] is True
            and outcome["outcome_window_recorded"] is True,
            f"{filename}: LEARNING_REVIEWED needs the locked pre-outcome record")
    require(outcome["review_recorded"] is True,
            f"{filename}: LEARNING_REVIEWED needs a recorded outcome review")
    observed = outcome["observed_outcome"]
    missing = outcome["missing_outcome_reason"]
    require(isinstance(observed, str) and isinstance(missing, str),
            f"{filename}: reviewed outcome and missing-outcome reason must be strings")
    require((nonempty(observed) and observed != "NOT_APPLICABLE")
            or (nonempty(missing) and missing != "NOT_APPLICABLE"),
            f"{filename}: LEARNING_REVIEWED needs an observed or explicitly missing outcome")
    require(outcome["human_disposition"] in {
                "ACCEPTED", "REJECTED", "DEFERRED", "OVERRIDDEN",
                "REQUEST_ENRICHMENT"},
            f"{filename}: LEARNING_REVIEWED needs a canonical human disposition")
    require(outcome["update_applied"] is False,
            f"{filename}: an outcome review may propose but cannot silently apply an update")


def validate_ordinary_record(record: dict, filename: str) -> None:
    allowed = {"supplied_scope", "assumptions", "unchecked_boundaries", "output"}
    require(set(record) == allowed,
            f"{filename}: ordinary record must contain only supplied scope, assumptions, unchecked boundaries, and output")
    scope = record["supplied_scope"]
    require(isinstance(scope, dict) and set(scope) == {"instruction", "input_refs"},
            f"{filename}: supplied scope must contain instruction and input_refs only")
    require_string(scope["instruction"], f"{filename}: supplied instruction is empty")
    require_string_list(scope["input_refs"], f"{filename}: supplied input refs are empty")
    require_string_list(record["assumptions"], f"{filename}: assumptions must be explicit")
    require_string_list(record["unchecked_boundaries"],
                        f"{filename}: unchecked boundaries must be explicit")
    output = record["output"]
    require(isinstance(output, dict) and set(output) == {"output_ref", "description"},
            f"{filename}: ordinary output must contain output_ref and description only")
    require_string(output["output_ref"], f"{filename}: output ref is empty")
    require_string(output["description"], f"{filename}: output description is empty")


def validate_permission(permission: object, filename: str) -> str:
    required = {
        "technical_access", "state", "scope", "reason_code", "reason",
        "resume_condition",
    }
    require(isinstance(permission, dict) and set(permission) == required,
            f"{filename}: permission record must use the exact typed permission keys")
    require(permission["technical_access"] in {"AVAILABLE", "UNAVAILABLE", "UNKNOWN"},
            f"{filename}: technical access must be typed")
    state = permission["state"]
    require(state in PERMISSION_STATES,
            f"{filename}: permission state must preserve AUTHORIZED/UNKNOWN/NOT_AUTHORIZED/REVOKED")
    require(permission["reason_code"] == PERMISSION_REASON_CODES[state],
            f"{filename}: permission reason code does not match {state}")
    for key in ("scope", "reason", "resume_condition"):
        require_string(permission[key], f"{filename}: permission {key} is empty")
    if state == "AUTHORIZED":
        require(permission["resume_condition"] == "NOT_APPLICABLE",
                f"{filename}: authorized permission must not invent a resume gate")
    else:
        require(permission["resume_condition"] != "NOT_APPLICABLE",
                f"{filename}: blocked permission needs a state-specific resume condition")
    return state


def validate_evidence_records(receipt: dict, filename: str) -> dict[str, dict]:
    records = receipt.get("evidence_records")
    require(isinstance(records, list), f"{filename}: evidence_records must be a list")
    index: dict[str, dict] = {}
    required = {
        "id", "exact_pointer", "claim_ids", "permission_state",
        "time_bearing", "observed_at", "alignment_key",
        "source_role", "track_record_evidence", "claim_scoped_authority",
        "support_state", "origin_state", "recurrence_state", "relevance",
        "provenance_ref",
    }
    for record in records:
        require(isinstance(record, dict) and set(record) == required,
                f"{filename}: evidence record must use the exact contract keys")
        record_id = record["id"]
        require_string(record_id, f"{filename}: evidence ID is empty")
        require(record_id not in index, f"{filename}: duplicate evidence ID {record_id}")
        require_string(record["exact_pointer"],
                       f"{filename}: {record_id} lacks an exact pointer")
        require(EXACT_POINTER_PATTERN.fullmatch(record["exact_pointer"]) is not None,
                f"{filename}: {record_id} exact pointer is not resolvable to a named span")
        require_string_list(record["claim_ids"],
                            f"{filename}: {record_id} lacks claim references")
        require(record["source_role"] in {
                    "PRIMARY", "SECONDARY", "SPECIALIST", "AGGREGATOR",
                    "OTHER", "UNKNOWN"},
                f"{filename}: {record_id} has an untyped source role")
        track_record = record["track_record_evidence"]
        require(track_record == "UNKNOWN"
                or (isinstance(track_record, str)
                    and EXACT_POINTER_PATTERN.fullmatch(track_record) is not None),
                f"{filename}: {record_id} track record must be UNKNOWN or a resolvable evidence pointer")
        require_substantive_string(
            record["claim_scoped_authority"],
            f"{filename}: {record_id} lacks a claim-scoped authority boundary",
        )
        require(record["support_state"] in {
                    "SUPPORTED", "CONTRADICTED", "QUALIFIED",
                    "INSUFFICIENT", "UNKNOWN"},
                f"{filename}: {record_id} has an untyped support state")
        require(record["origin_state"] in {
                    "INDEPENDENT", "RELATED", "COMMON_ORIGIN", "UNKNOWN"},
                f"{filename}: {record_id} has an untyped origin state")
        require(record["recurrence_state"] in {
                    "RECURRENT", "NOT_RECURRENT", "UNKNOWN"},
                f"{filename}: {record_id} has an untyped recurrence state")
        require(record["relevance"] in {"HIGH", "MEDIUM", "LOW", "UNKNOWN"},
                f"{filename}: {record_id} has an untyped relevance state")
        require(isinstance(record["provenance_ref"], str)
                and EXACT_POINTER_PATTERN.fullmatch(record["provenance_ref"]) is not None,
                f"{filename}: {record_id} lacks a resolvable provenance reference")
        require(record["permission_state"] in PERMISSION_STATES,
                f"{filename}: {record_id} has an untyped permission state")
        require(isinstance(record["time_bearing"], bool),
                f"{filename}: {record_id} time_bearing must be boolean")
        require(isinstance(record["observed_at"], str),
                f"{filename}: {record_id} observed_at must be a string")
        require(isinstance(record["alignment_key"], str),
                f"{filename}: {record_id} alignment_key must be a string")
        if record["time_bearing"]:
            parse_utc_observed_at(record["observed_at"], filename, record_id)
            require(nonempty(record["alignment_key"])
                    and record["alignment_key"] != "NOT_APPLICABLE",
                    f"{filename}: {record_id} lacks a substantive alignment key")
        else:
            require(record["observed_at"] == "NOT_APPLICABLE"
                    and record["alignment_key"] == "NOT_APPLICABLE",
                    f"{filename}: non-time-bearing {record_id} must use NOT_APPLICABLE time fields")
        index[record_id] = record
    return index


def validate_baseline_records(receipt: dict, filename: str,
                              evidence: dict[str, dict]) -> list[dict]:
    records = receipt.get("baseline_records")
    require(isinstance(records, list), f"{filename}: baseline_records must be a list")
    seen: set[str] = set()
    required = {
        "id", "basis", "observation_boundary", "evidence_ids",
        "motion_assessed", "motion_observation_ids", "motion_alignment_key",
        "absence_expected",
    }
    for record in records:
        require(isinstance(record, dict) and set(record) == required,
                f"{filename}: baseline record must use the exact contract keys")
        record_id = record["id"]
        require_string(record_id, f"{filename}: baseline ID is empty")
        require(record_id not in seen, f"{filename}: duplicate baseline ID {record_id}")
        seen.add(record_id)
        require_substantive_string(record["basis"],
                                   f"{filename}: {record_id} lacks a substantive basis")
        require_substantive_string(
            record["observation_boundary"],
            f"{filename}: {record_id} lacks a substantive observation boundary",
        )
        require_string_list(record["evidence_ids"],
                            f"{filename}: {record_id} lacks evidence references")
        for evidence_id in record["evidence_ids"]:
            require(evidence_id in evidence,
                    f"{filename}: {record_id} references missing evidence {evidence_id}")
            require(evidence[evidence_id]["permission_state"] == "AUTHORIZED",
                    f"{filename}: {record_id} uses blocked evidence {evidence_id}")
        require(isinstance(record["motion_assessed"], bool),
                f"{filename}: {record_id} motion_assessed must be boolean")
        require_string_list(record["motion_observation_ids"],
                            f"{filename}: {record_id} motion observation refs are malformed",
                            allow_empty=True)
        require(isinstance(record["motion_alignment_key"], str),
                f"{filename}: {record_id} motion_alignment_key must be a string")
        motion_ids = record["motion_observation_ids"]
        if record["motion_assessed"]:
            require(len(motion_ids) >= 2 and len(set(motion_ids)) == len(motion_ids),
                    f"{filename}: {record_id} motion needs at least two distinct observation refs")
            require(set(motion_ids) <= set(record["evidence_ids"]),
                    f"{filename}: {record_id} motion refs must be part of its baseline evidence")
            require(nonempty(record["motion_alignment_key"])
                    and record["motion_alignment_key"] != "NOT_APPLICABLE",
                    f"{filename}: {record_id} motion needs a substantive alignment key")
            motion_instants: list[datetime] = []
            for evidence_id in motion_ids:
                require(evidence_id in evidence,
                        f"{filename}: {record_id} motion references missing evidence {evidence_id}")
                motion_record = evidence[evidence_id]
                require(motion_record["permission_state"] == "AUTHORIZED",
                        f"{filename}: {record_id} motion uses blocked evidence {evidence_id}")
                require(motion_record["time_bearing"] is True,
                        f"{filename}: {record_id} motion uses a non-time-bearing ref {evidence_id}")
                require(motion_record["alignment_key"] == record["motion_alignment_key"],
                        f"{filename}: {record_id} motion refs do not share the alignment key")
                motion_instants.append(
                    parse_utc_observed_at(
                        motion_record["observed_at"], filename, evidence_id,
                    )
                )
            require(len(set(motion_instants)) >= 2,
                    f"{filename}: {record_id} motion refs need at least two distinct UTC instants")
        else:
            require(not motion_ids and record["motion_alignment_key"] == "NOT_APPLICABLE",
                    f"{filename}: inactive motion must have no refs and NOT_APPLICABLE alignment")
        require(isinstance(record["absence_expected"], bool),
                f"{filename}: {record_id} absence_expected must be boolean")
    return records


def validate_comparison_records(receipt: dict, filename: str,
                                evidence: dict[str, dict]) -> list[dict]:
    records = receipt.get("comparison_records")
    require(isinstance(records, list), f"{filename}: comparison_records must be a list")
    seen: set[str] = set()
    required = {
        "id", "unit", "item_ids", "alignment_boundary", "result",
        "origin_state",
    }
    origin_states = {"INDEPENDENT", "RELATED", "COMMON_ORIGIN", "UNKNOWN", "NOT_APPLICABLE"}
    for record in records:
        require(isinstance(record, dict) and set(record) == required,
                f"{filename}: comparison record must use the exact contract keys")
        record_id = record["id"]
        require_string(record_id, f"{filename}: comparison ID is empty")
        require(record_id not in seen, f"{filename}: duplicate comparison ID {record_id}")
        seen.add(record_id)
        require_string(record["unit"], f"{filename}: {record_id} has empty unit")
        for key in ("alignment_boundary", "result"):
            require_substantive_string(
                record[key], f"{filename}: {record_id} has non-substantive {key}",
            )
        require_string_list(record["item_ids"],
                            f"{filename}: {record_id} needs comparison items")
        require(len(set(record["item_ids"])) >= 2,
                f"{filename}: {record_id} needs at least two distinct items")
        for item_id in record["item_ids"]:
            require(item_id in evidence,
                    f"{filename}: {record_id} references missing item {item_id}")
            require(evidence[item_id]["permission_state"] == "AUTHORIZED",
                    f"{filename}: {record_id} compares blocked item {item_id}")
        require(record["origin_state"] in origin_states,
                f"{filename}: {record_id} has a noncanonical origin state")
    return records


def validate_disconfirmation_records(receipt: dict, filename: str,
                                     evidence: dict[str, dict]) -> list[dict]:
    records = receipt.get("disconfirmation_records")
    require(isinstance(records, list),
            f"{filename}: disconfirmation_records must be a list")
    seen: set[str] = set()
    required = {
        "id", "route_or_query", "target", "result", "residual_uncertainty",
        "evidence_ids",
    }
    for record in records:
        require(isinstance(record, dict) and set(record) == required,
                f"{filename}: disconfirmation record must use the exact contract keys")
        record_id = record["id"]
        require_string(record_id, f"{filename}: disconfirmation ID is empty")
        require(record_id not in seen,
                f"{filename}: duplicate disconfirmation ID {record_id}")
        seen.add(record_id)
        for key in ("route_or_query", "target", "result", "residual_uncertainty"):
            require_substantive_string(
                record[key], f"{filename}: {record_id} has non-substantive {key}",
            )
        require_string_list(record["evidence_ids"],
                            f"{filename}: {record_id} lacks resolvable evidence references")
        for evidence_id in record["evidence_ids"]:
            require(evidence_id in evidence,
                    f"{filename}: {record_id} references missing evidence {evidence_id}")
            require(evidence[evidence_id]["permission_state"] == "AUTHORIZED",
                    f"{filename}: {record_id} uses blocked evidence {evidence_id}")
    return records


def validate_memory_records(receipt: dict, filename: str,
                            evidence: dict[str, dict]) -> dict[str, dict]:
    records = receipt.get("memory_records")
    require(isinstance(records, list), f"{filename}: memory_records must be a list")
    index: dict[str, dict] = {}
    required = {
        "id", "lineage_id", "version", "source_scope", "payload", "content_digest",
        "source_evidence_ids", "permission_state", "reuse_scope", "status",
        "supersedes", "corrects", "prior_content_digest", "correction_reason",
        "human_disposition", "lineage_mode", "branch_authorization_ref",
    }
    anchor_registry = load_json(MEMORY_ANCHOR_REGISTRY)
    require(set(anchor_registry) == {"schema_version", "anchors"}
            and anchor_registry["schema_version"] == "pattern-map.memory-anchors.v1"
            and isinstance(anchor_registry["anchors"], dict),
            f"{MEMORY_ANCHOR_REGISTRY}: malformed frozen anchor registry")
    anchors = anchor_registry["anchors"]
    for record in records:
        require(isinstance(record, dict) and set(record) == required,
                f"{filename}: memory record must use the exact contract keys")
        record_id = record["id"]
        require_string(record_id, f"{filename}: memory ID is empty")
        require(record_id not in index, f"{filename}: duplicate memory ID {record_id}")
        require_string(record["lineage_id"],
                       f"{filename}: {record_id} lacks a lineage ID")
        require(isinstance(record["version"], int) and record["version"] >= 1,
                f"{filename}: {record_id} has invalid version")
        require_substantive_string(record["source_scope"],
                                   f"{filename}: {record_id} lacks substantive source scope")
        require(isinstance(record["content_digest"], str)
                and DIGEST_PATTERN.fullmatch(record["content_digest"]) is not None,
                f"{filename}: {record_id} lacks a canonical content digest")
        require(isinstance(record["payload"], dict)
                and set(record["payload"]) == {"claim_id", "statement", "scope"},
                f"{filename}: {record_id} payload must contain claim_id, statement, and scope only")
        for key in ("claim_id", "statement", "scope"):
            if key == "claim_id":
                require_string(record["payload"][key],
                               f"{filename}: {record_id} payload {key} is empty")
            else:
                require_substantive_string(
                    record["payload"][key],
                    f"{filename}: {record_id} payload {key} is not substantive",
                )
        require(record["content_digest"] == canonical_payload_digest(record["payload"]),
                f"{filename}: {record_id} digest is not bound to canonical payload bytes")
        require_string_list(record["source_evidence_ids"],
                            f"{filename}: {record_id} lacks source evidence")
        for evidence_id in record["source_evidence_ids"]:
            require(evidence_id in evidence,
                    f"{filename}: {record_id} references missing source evidence {evidence_id}")
            require(evidence[evidence_id]["permission_state"] == "AUTHORIZED",
                    f"{filename}: {record_id} derives memory from blocked evidence {evidence_id}")
        require(record["permission_state"] in PERMISSION_STATES,
                f"{filename}: {record_id} has untyped permission")
        require_substantive_string(record["reuse_scope"],
                                   f"{filename}: {record_id} lacks a substantive reuse scope")
        require(record["status"] in {"CURRENT", "SUPERSEDED"},
                f"{filename}: {record_id} has invalid status")
        require(record["lineage_mode"] == "LINEAR",
                f"{filename}: {record_id} uses an unsupported or unauthorized branch mode")
        require(record["branch_authorization_ref"] == "NOT_APPLICABLE",
                f"{filename}: linear {record_id} must not invent branch authorization")
        index[record_id] = record

    children: dict[str, list[str]] = {record_id: [] for record_id in index}
    roots_by_lineage: dict[str, list[str]] = {}
    for record_id, record in index.items():
        link_values = (record["supersedes"], record["corrects"])
        if link_values == (None, None):
            require(record["prior_content_digest"] is None
                    and record["correction_reason"] is None
                    and record["human_disposition"] == "NOT_APPLICABLE",
                    f"{filename}: original {record_id} invents correction metadata")
            require(record["version"] == 1,
                    f"{filename}: lineage root {record_id} must be version 1")
            roots_by_lineage.setdefault(record["lineage_id"], []).append(record_id)
            continue
        require(all(nonempty(value) for value in link_values)
                and record["supersedes"] == record["corrects"],
                f"{filename}: {record_id} must link the same preserved correction target")
        target_id = record["supersedes"]
        require(target_id in index,
                f"{filename}: {record_id} references missing prior memory {target_id}")
        target = index[target_id]
        require(record["lineage_id"] == target["lineage_id"],
                f"{filename}: {record_id} crosses memory lineages")
        require(record["version"] == target["version"] + 1,
                f"{filename}: {record_id} does not advance exactly one version")
        require(record["prior_content_digest"] == target["content_digest"],
                f"{filename}: {record_id} prior digest does not match preserved {target_id}")
        require_string(record["correction_reason"],
                       f"{filename}: {record_id} lacks a correction reason")
        require(record["human_disposition"] == "ACCEPTED",
                f"{filename}: {record_id} cannot enter this current lineage without ACCEPTED disposition")
        children[target_id].append(record_id)

    for record_id, successor_ids in children.items():
        require(len(successor_ids) <= 1,
                f"{filename}: unauthorized memory fork after {record_id}; linear lineage allows one successor")

    records_by_lineage: dict[str, list[dict]] = {}
    for record in index.values():
        records_by_lineage.setdefault(record["lineage_id"], []).append(record)
    require(set(roots_by_lineage) == set(records_by_lineage),
            f"{filename}: every memory lineage needs one preserved root")
    for lineage_id, lineage_records in records_by_lineage.items():
        roots = roots_by_lineage.get(lineage_id, [])
        require(len(roots) == 1,
                f"{filename}: {lineage_id} must have exactly one lineage root")
        root_id = roots[0]
        require(lineage_id in anchors,
                f"{filename}: {lineage_id} lacks a separately frozen initial anchor")
        anchor = anchors[lineage_id]
        require(isinstance(anchor, dict)
                and set(anchor) == {"root_record_id", "root_content_digest"}
                and anchor["root_record_id"] == root_id
                and anchor["root_content_digest"] == index[root_id]["content_digest"],
                f"{filename}: {lineage_id} root does not match its frozen initial anchor")
        current = [record for record in lineage_records if record["status"] == "CURRENT"]
        require(len(current) == 1,
                f"{filename}: {lineage_id} must have exactly one CURRENT record")
        current_id = current[0]["id"]
        require(not children[current_id],
                f"{filename}: CURRENT record {current_id} cannot already have a successor")
        for record in lineage_records:
            if record["id"] == current_id:
                continue
            require(record["status"] == "SUPERSEDED" and len(children[record["id"]]) == 1,
                    f"{filename}: non-current memory {record['id']} must remain SUPERSEDED history with one successor")
    return index


def validate_layered_receipt(receipt: dict, filename: str) -> None:
    require(not (set(receipt) & LEGACY_AUTHORIZATION_KEYS),
            f"{filename}: receipt top level contains a contradictory legacy authorization field")
    common_required = {
        "receipt_id", "operating_level", "evidence_selection", "consequence",
        "permission", "budget", "evidence_records", "baseline_records",
        "comparison_records", "comparison_disposition",
        "disconfirmation_records", "disconfirmation_disposition", "memory_records",
        "memory_use", "influence", "route", "stop_status", "stop_reason",
        "outcome",
    }
    require(common_required <= set(receipt), f"{filename} is missing layered receipt keys")
    require(receipt["operating_level"] in {"LIGHTWEIGHT", "MODERATE", "ADVANCED"},
            f"{filename}: operating level is not canonical")
    require(receipt["evidence_selection"] == "NEEDED",
            f"{filename}: layered route must record evidence selection as needed")
    require(receipt["consequence"] in {"LOW", "MEDIUM", "HIGH"},
            f"{filename}: consequence is not canonical")
    permission_state = validate_permission(receipt["permission"], filename)
    if permission_state != "AUTHORIZED":
        for collection_name in (
            "evidence_records", "baseline_records", "comparison_records",
            "disconfirmation_records", "memory_records",
        ):
            require(receipt.get(collection_name) == [],
                    f"{filename}: global {permission_state} permission requires empty {collection_name}")
        require(receipt.get("memory_use") == {"status": "NOT_USED", "record_ids": []},
                f"{filename}: global {permission_state} permission requires memory NOT_USED")
        require(receipt.get("influence") == {
                    "recorded": False, "selected_items": [], "withheld_items": []},
                f"{filename}: global {permission_state} permission requires empty influence")
    budget = receipt["budget"]
    require(isinstance(budget, dict)
            and isinstance(budget.get("remaining_minutes"), (int, float))
            and isinstance(budget.get("limit_minutes"), (int, float)),
            f"{filename}: budget needs numeric remaining and limit minutes")
    route = receipt["route"]
    stop_status = receipt["stop_status"]
    require(route in ROUTES, f"{filename}: route is not canonical: {route}")
    require(stop_status in STOP_STATUSES,
            f"{filename}: stop status is not canonical: {stop_status}")
    require_string(receipt["stop_reason"], f"{filename}: stop reason is empty")
    stop_reason = receipt["stop_reason"].lower()
    validate_outcome(receipt, filename)

    evidence = validate_evidence_records(receipt, filename)
    baselines = validate_baseline_records(receipt, filename, evidence)
    comparisons = validate_comparison_records(receipt, filename, evidence)
    disconfirmations = validate_disconfirmation_records(receipt, filename, evidence)
    memories = validate_memory_records(receipt, filename, evidence)
    comparison_status = validate_requirement_disposition(
        receipt["comparison_disposition"],
        comparisons,
        filename,
        label="comparison",
        inactive_status="NOT_APPLICABLE",
    )
    disconfirmation_status = validate_requirement_disposition(
        receipt["disconfirmation_disposition"],
        disconfirmations,
        filename,
        label="disconfirmation",
        inactive_status="SKIPPED",
    )

    memory_use = receipt["memory_use"]
    require(isinstance(memory_use, dict)
            and set(memory_use) == {"status", "record_ids"},
            f"{filename}: memory_use must contain status and record_ids only")
    require(memory_use["status"] in {"USED", "NOT_USED"},
            f"{filename}: memory_use status is not canonical")
    require_string_list(memory_use["record_ids"],
                        f"{filename}: memory_use record IDs are malformed",
                        allow_empty=True)
    if memory_use["status"] == "USED":
        require(bool(memory_use["record_ids"]),
                f"{filename}: used memory needs a record reference")
    else:
        require(not memory_use["record_ids"],
                f"{filename}: unused memory cannot name record references")
    for memory_id in memory_use["record_ids"]:
        require(memory_id in memories,
                f"{filename}: memory use references missing record {memory_id}")
        require(memories[memory_id]["permission_state"] == "AUTHORIZED",
                f"{filename}: unresolved or blocked memory {memory_id} cannot be used")
        require(memories[memory_id]["status"] == "CURRENT",
                f"{filename}: only CURRENT memory may be used; {memory_id} is preserved history")

    influence = receipt["influence"]
    require(isinstance(influence, dict)
            and set(influence) == {"recorded", "selected_items", "withheld_items"},
            f"{filename}: influence must use the exact contract keys")
    require(isinstance(influence.get("recorded"), bool),
            f"{filename}: influence recorded must be boolean")
    require_string_list(influence.get("selected_items"),
                        f"{filename}: selected influence items must be a string list",
                        allow_empty=True)
    require_string_list(influence.get("withheld_items"),
                        f"{filename}: withheld influence items must be a string list",
                        allow_empty=True)
    selected_items = influence["selected_items"]
    withheld_items = influence["withheld_items"]
    require(not (set(selected_items) & set(withheld_items)),
            f"{filename}: an item cannot be selected and withheld")
    selectable = {**evidence, **memories}
    for item_id in selected_items + withheld_items:
        require(item_id in selectable,
                f"{filename}: influence references missing item {item_id}")
    for item_id in selected_items:
        require(selectable[item_id]["permission_state"] == "AUTHORIZED",
                f"{filename}: unresolved or blocked item {item_id} cannot influence output")
        if item_id in memories:
            require(memories[item_id]["status"] == "CURRENT",
                    f"{filename}: only CURRENT memory may influence output; {item_id} is history")
    if influence["recorded"]:
        require(bool(selected_items),
                f"{filename}: recorded influence needs at least one selected item")
    else:
        require(not selected_items,
                f"{filename}: unrecorded influence cannot contain selected items")

    if permission_state != "AUTHORIZED":
        allowed_routes = {
            "UNKNOWN": {"HOLD", "ESCALATE"},
            "NOT_AUTHORIZED": {"HOLD", "ESCALATE", "REFUSE"},
            "REVOKED": {"HOLD", "ESCALATE", "REFUSE"},
        }
        require(route in allowed_routes[permission_state],
                f"{filename}: {permission_state} work uses an impermissible route")
        require(stop_status != "CONTINUE",
                f"{filename}: blocked permission cannot remain in CONTINUE state")
        require(permission_state in receipt.get("uncertainty", []),
                f"{filename}: blocked permission state must remain visible")
        state_words = {
            "UNKNOWN": ("not been established", "unknown"),
            "NOT_AUTHORIZED": ("permission", "not authoriz"),
            "REVOKED": ("revoked",),
        }
        require(any(word in stop_reason for word in state_words[permission_state]),
                f"{filename}: stop reason does not preserve {permission_state} semantics")

    if receipt["consequence"] == "HIGH" and route in {"ANSWER", "ANSWER_PROVISIONALLY"}:
        require(bool(baselines),
                f"{filename}: high-consequence answer needs a substantive baseline record")

    if route in {"ANSWER", "ANSWER_PROVISIONALLY"}:
        require(influence["recorded"] is True,
                f"{filename}: answer route needs a resolvable influence receipt")
        require(comparison_status in {"PERFORMED", "NOT_APPLICABLE"}
                and disconfirmation_status in {"PERFORMED", "SKIPPED"},
                f"{filename}: answer route lacks typed comparison/disconfirmation disposition")

    if budget["remaining_minutes"] <= 0:
        require(stop_status in {"STOPPED_BUDGET", "STOPPED_DEADLINE", "STOPPED_OTHER"},
                f"{filename}: exhausted budget needs a stop status")
        require(route not in {"ACQUIRE", "COMPARE"},
                f"{filename}: exhausted budget cannot route to more work")
        require("budget" in stop_reason or "deadline" in stop_reason,
                f"{filename}: exhausted budget reason must be explicit")
    if stop_status == "STOPPED_BUDGET":
        require("budget" in stop_reason,
                f"{filename}: STOPPED_BUDGET reason must name budget")

    for claim_field in ("motion_claim", "absence_claim", "independence_claim"):
        if claim_field in receipt:
            require(isinstance(receipt[claim_field], bool),
                    f"{filename}: {claim_field} must be boolean")
    if receipt.get("motion_claim") is True:
        require(any(record["motion_assessed"] is True for record in baselines),
                f"{filename}: motion claim needs aligned time-bearing observation refs")
        for baseline in (record for record in baselines if record["motion_assessed"]):
            require(any(
                        set(baseline["motion_observation_ids"]) <= set(comparison["item_ids"])
                        and baseline["motion_alignment_key"] in comparison["alignment_boundary"]
                        for comparison in comparisons
                    ),
                    f"{filename}: motion refs need a substantive comparison using the alignment key")
    if receipt.get("absence_claim") is True:
        require(any(record["absence_expected"] is True for record in baselines),
                f"{filename}: absence claim needs an expected baseline")
    if receipt.get("independence_claim") is True:
        require(any(record["origin_state"] == "INDEPENDENT" for record in comparisons),
                f"{filename}: independence claim needs an independent comparison relation")


def expect_failure(value: dict, filename: str, message: str,
                   *, ordinary: bool = False,
                   error_contains: str | None = None) -> None:
    try:
        if ordinary:
            validate_ordinary_record(value, filename)
        else:
            validate_layered_receipt(value, filename)
    except CheckFailure as exc:
        if error_contains is not None:
            require(error_contains in str(exc),
                    f"{message}; unexpected failure instead: {exc}")
        return
    raise CheckFailure(message)


def validate_receipt_guard_mutations() -> None:
    """Fail closed on status-only, dangling-reference, and overwrite mutations."""

    base = load_json("qa/applied/receipts/layered-ready.json")

    planned = copy.deepcopy(base)
    planned["outcome"] = {
        "applicable": True,
        "learning_status": "LEARNING_PLANNED",
        "expectation_recorded": False,
        "outcome_window_recorded": False,
        "update_applied": False,
    }
    validate_layered_receipt(planned, "synthetic-planned-contract-control.json")

    invalid = copy.deepcopy(base)
    invalid["outcome"]["learning_status"] = "LEARNING_REVIEWED"
    expect_failure(
        invalid,
        "synthetic-reviewed-without-review.json",
        "validator accepted LEARNING_REVIEWED without an outcome review and disposition",
    )
    valid = copy.deepcopy(invalid)
    valid["outcome"].update(
        {
            "review_recorded": True,
            "observed_outcome": "SYNTHETIC_CONTRACT_OBSERVATION_ONLY",
            "missing_outcome_reason": "NOT_APPLICABLE",
            "human_disposition": "DEFERRED",
        }
    )
    validate_layered_receipt(valid, "synthetic-reviewed-contract-control.json")

    for mutation_name, outcome in (
        (
            "pending-with-result",
            base["outcome"] | {
                "review_recorded": True,
                "observed_outcome": "CLAIMED_SUCCESS",
                "missing_outcome_reason": "NOT_APPLICABLE",
                "human_disposition": "ACCEPTED",
            },
        ),
        (
            "not-applicable-with-result",
            {
                "applicable": False,
                "learning_status": "LEARNING_NOT_APPLICABLE",
                "review_recorded": True,
                "observed_outcome": "CLAIMED_SUCCESS",
                "missing_outcome_reason": "NOT_APPLICABLE",
                "human_disposition": "ACCEPTED",
                "update_applied": True,
            },
        ),
        (
            "missing-applicable",
            {"learning_status": "LEARNING_NOT_APPLICABLE"},
        ),
        (
            "mistyped-applicable",
            {"applicable": "false", "learning_status": "LEARNING_NOT_APPLICABLE"},
        ),
        (
            "planned-after-lock",
            {
                "applicable": True,
                "learning_status": "LEARNING_PLANNED",
                "expectation_recorded": True,
                "outcome_window_recorded": True,
                "update_applied": False,
            },
        ),
    ):
        invalid_outcome = copy.deepcopy(base)
        invalid_outcome["outcome"] = outcome
        expect_failure(
            invalid_outcome,
            f"synthetic-{mutation_name}.json",
            f"validator accepted invalid learning transition {mutation_name}",
        )

    for mutation_name, mutate in (
        (
            "evidence-unresolvable-pointer",
            lambda value: value["evidence_records"][0].update(
                {"exact_pointer": "fixture://synthetic/layered-ready/source-a"}
            ),
        ),
        ("baseline-placeholder", lambda value: value["baseline_records"][0].update({"basis": "done"})),
        ("baseline-dangling", lambda value: value["baseline_records"][0]["evidence_ids"].append("E-MISSING")),
        ("comparison-empty-unit", lambda value: value["comparison_records"][0].update({"unit": ""})),
        ("comparison-placeholder-result", lambda value: value["comparison_records"][0].update({"result": "done"})),
        ("comparison-dangling", lambda value: value["comparison_records"][0]["item_ids"].append("E-MISSING")),
        ("comparison-revoked", lambda value: value["evidence_records"][1].update({"permission_state": "REVOKED"})),
        (
            "disconfirmation-empty-query",
            lambda value: value["disconfirmation_records"][0].update(
                {"route_or_query": ""}
            ),
        ),
        (
            "disconfirmation-placeholder-result",
            lambda value: value["disconfirmation_records"][0].update(
                {"result": "none"}
            ),
        ),
        (
            "disconfirmation-dangling",
            lambda value: value["disconfirmation_records"][0][
                "evidence_ids"
            ].append("E-MISSING"),
        ),
        ("influence-dangling", lambda value: value["influence"]["selected_items"].append("E-MISSING")),
    ):
        invalid_reference = copy.deepcopy(base)
        mutate(invalid_reference)
        expect_failure(
            invalid_reference,
            f"synthetic-{mutation_name}.json",
            f"validator accepted malformed or unresolved {mutation_name} record",
        )

    for field in (
        "source_role", "track_record_evidence", "claim_scoped_authority",
        "support_state", "origin_state", "recurrence_state", "relevance",
        "provenance_ref", "permission_state",
    ):
        missing_dimension = copy.deepcopy(base)
        del missing_dimension["evidence_records"][0][field]
        expect_failure(
            missing_dimension,
            f"synthetic-evidence-missing-{field}.json",
            f"validator accepted evidence with collapsed or missing F2 field {field}",
        )

    invalid_influence_permission = copy.deepcopy(base)
    invalid_influence_permission["evidence_records"].append(
        {
            "id": "E-UNKNOWN",
            "exact_pointer": "fixture://synthetic/unresolved/item#claim",
            "claim_ids": ["C-UNKNOWN"],
            "source_role": "UNKNOWN",
            "track_record_evidence": "UNKNOWN",
            "claim_scoped_authority": "May establish only the supplied unresolved fixture wording for C-UNKNOWN.",
            "support_state": "UNKNOWN",
            "origin_state": "UNKNOWN",
            "recurrence_state": "UNKNOWN",
            "relevance": "UNKNOWN",
            "provenance_ref": "fixture://synthetic/unresolved/item#provenance",
            "permission_state": "UNKNOWN",
            "time_bearing": False,
            "observed_at": "NOT_APPLICABLE",
            "alignment_key": "NOT_APPLICABLE",
        }
    )
    invalid_influence_permission["influence"]["selected_items"].append("E-UNKNOWN")
    expect_failure(
        invalid_influence_permission,
        "synthetic-influence-unknown.json",
        "validator accepted unresolved permission as selected influence",
    )

    invalid_high = copy.deepcopy(base)
    invalid_high["baseline_records"] = []
    expect_failure(
        invalid_high,
        "synthetic-high-without-baseline.json",
        "validator accepted a high-consequence answer without a substantive baseline",
    )

    for mutation_name, mutate in (
        ("motion-self-count", lambda value: value["baseline_records"][0].update({"motion_timepoints": 2})),
        ("motion-one-ref", lambda value: value["baseline_records"][0].update({"motion_observation_ids": ["E-001"]})),
        (
            "motion-duplicate-ref",
            lambda value: value["baseline_records"][0].update(
                {"motion_observation_ids": ["E-001", "E-001"]}
            ),
        ),
        (
            "motion-ref-outside-baseline",
            lambda value: value["baseline_records"][0].update(
                {"evidence_ids": ["E-001", "E-004"]}
            ),
        ),
        (
            "motion-without-aligned-comparison",
            lambda value: value["comparison_records"].pop(1),
        ),
        ("motion-misaligned", lambda value: value["evidence_records"][2].update({"alignment_key": "OTHER-ALIGNMENT"})),
        (
            "motion-not-time-bearing",
            lambda value: value["evidence_records"][2].update(
                {
                    "time_bearing": False,
                    "observed_at": "NOT_APPLICABLE",
                    "alignment_key": "NOT_APPLICABLE",
                }
            ),
        ),
        (
            "motion-impossible-instant",
            lambda value: value["evidence_records"][2].update(
                {"observed_at": "2026-99-99T99:99:99Z"}
            ),
        ),
        (
            "motion-duplicate-instant",
            lambda value: value["evidence_records"][2].update(
                {"observed_at": value["evidence_records"][0]["observed_at"]}
            ),
        ),
        ("motion-revoked", lambda value: value["evidence_records"][2].update({"permission_state": "REVOKED"})),
        ("motion-string-boolean", lambda value: value["baseline_records"][0].update({"motion_assessed": "true"})),
        ("motion-boolean-timestamp", lambda value: value["evidence_records"][2].update({"observed_at": True})),
    ):
        invalid_motion = copy.deepcopy(base)
        mutate(invalid_motion)
        expect_failure(
            invalid_motion,
            f"synthetic-{mutation_name}.json",
            f"validator accepted unsupported motion mutation {mutation_name}",
        )

    for mutation_name, mutate in (
        ("comparison-performed-without-record", lambda value: value.update({"comparison_records": []})),
        (
            "comparison-inactive-with-record",
            lambda value: value["comparison_disposition"].update(
                {
                    "status": "NOT_APPLICABLE",
                    "reason": "No aligned unit is relevant.",
                }
            ),
        ),
        (
            "comparison-unbounded-reason",
            lambda value: value.update(
                {
                    "comparison_records": [],
                    "comparison_disposition": {
                        "status": "NOT_APPLICABLE",
                        "reason": "line one\nline two",
                    },
                }
            ),
        ),
        ("disconfirmation-performed-without-record", lambda value: value.update({"disconfirmation_records": []})),
        (
            "disconfirmation-skipped-with-record",
            lambda value: value["disconfirmation_disposition"].update(
                {
                    "status": "SKIPPED",
                    "reason": "The supplied transformation adds no factual claim.",
                }
            ),
        ),
    ):
        invalid_disposition = copy.deepcopy(base)
        mutate(invalid_disposition)
        expect_failure(
            invalid_disposition,
            f"synthetic-{mutation_name}.json",
            f"validator accepted inconsistent answer-route {mutation_name}",
        )

    proportional_answer = load_json("qa/applied/receipts/lightweight-low-stakes.json")
    proportional_answer["comparison_records"] = []
    proportional_answer["comparison_disposition"] = {
        "status": "NOT_APPLICABLE",
        "reason": "Only a supplied-scope qualification is needed; no distinct comparison unit applies.",
    }
    proportional_answer["disconfirmation_records"] = []
    proportional_answer["disconfirmation_disposition"] = {
        "status": "SKIPPED",
        "reason": "The low-consequence answer is confined to supplied wording and adds no outside factual claim.",
    }
    validate_layered_receipt(
        proportional_answer,
        "synthetic-proportional-answer-control.json",
    )

    invalid_permission = copy.deepcopy(base)
    invalid_permission["permission"]["state"] = True
    expect_failure(
        invalid_permission,
        "synthetic-boolean-permission.json",
        "validator accepted a boolean authorization state",
    )
    for legacy_key, legacy_value in (
        ("authorized", True),
        ("permission_granted", False),
        ("is_authorized", "yes"),
    ):
        invalid_legacy_permission = copy.deepcopy(base)
        invalid_legacy_permission["permission"][legacy_key] = legacy_value
        expect_failure(
            invalid_legacy_permission,
            f"synthetic-legacy-permission-{legacy_key}.json",
            f"validator accepted contradictory legacy permission key {legacy_key}",
        )
        invalid_top_level_permission = copy.deepcopy(base)
        invalid_top_level_permission[legacy_key] = legacy_value
        expect_failure(
            invalid_top_level_permission,
            f"synthetic-top-level-legacy-permission-{legacy_key}.json",
            f"validator accepted top-level contradictory permission key {legacy_key}",
            error_contains="receipt top level contains a contradictory legacy authorization field",
        )
    unknown = load_json("qa/applied/receipts/unknown-permission.json")
    invalid_unknown = copy.deepcopy(unknown)
    invalid_unknown["permission"]["resume_condition"] = "NOT_APPLICABLE"
    expect_failure(
        invalid_unknown,
        "synthetic-unknown-without-resume.json",
        "validator accepted UNKNOWN permission without a resume condition",
    )
    invalid_reason = copy.deepcopy(unknown)
    invalid_reason["permission"]["reason_code"] = "PERMISSION_ABSENT"
    expect_failure(
        invalid_reason,
        "synthetic-unknown-as-absent.json",
        "validator collapsed UNKNOWN permission into NOT_AUTHORIZED semantics",
    )

    blocked = load_json("qa/applied/receipts/blocked-permission.json")
    invalid_blocked = copy.deepcopy(blocked)
    invalid_blocked["evidence_records"] = [
        {
            "id": "E-BLOCKED",
            "exact_pointer": "fixture://synthetic/blocked/item#claim",
            "claim_ids": ["C-BLOCKED"],
            "source_role": "UNKNOWN",
            "track_record_evidence": "UNKNOWN",
            "claim_scoped_authority": "May establish only the wording of the blocked synthetic item.",
            "support_state": "UNKNOWN",
            "origin_state": "UNKNOWN",
            "recurrence_state": "UNKNOWN",
            "relevance": "UNKNOWN",
            "provenance_ref": "fixture://synthetic/blocked/item#provenance",
            "permission_state": "NOT_AUTHORIZED",
            "time_bearing": False,
            "observed_at": "NOT_APPLICABLE",
            "alignment_key": "NOT_APPLICABLE",
        }
    ]
    invalid_blocked["influence"] = {
        "recorded": True,
        "selected_items": ["E-BLOCKED"],
        "withheld_items": [],
    }
    expect_failure(
        invalid_blocked,
        "synthetic-blocked-influence.json",
        "validator accepted blocked material as selected influence",
    )

    blocked_fixtures = {
        "UNKNOWN": load_json("qa/applied/receipts/unknown-permission.json"),
        "NOT_AUTHORIZED": blocked,
        "REVOKED": load_json("qa/applied/receipts/revoked-permission.json"),
    }
    for state, blocked_fixture in blocked_fixtures.items():
        for field, contaminated in (
            ("evidence_records", [{}]),
            ("baseline_records", [{}]),
            ("comparison_records", [{}]),
            ("disconfirmation_records", [{}]),
            ("memory_records", [{}]),
            ("memory_use", {"status": "USED", "record_ids": ["M-UNRESOLVED"]}),
            ("influence", {"recorded": False, "selected_items": [], "withheld_items": ["E-UNRESOLVED"]}),
        ):
            invalid_global_permission = copy.deepcopy(blocked_fixture)
            invalid_global_permission[field] = contaminated
            expect_failure(
                invalid_global_permission,
                f"synthetic-{state.lower()}-{field}.json",
                f"validator accepted {field} under global {state} permission",
                error_contains=(
                    f"requires empty {field}" if field.endswith("_records")
                    else ("requires memory NOT_USED" if field == "memory_use"
                          else "requires empty influence")
                ),
            )

    ordinary = load_json("qa/applied/receipts/ordinary-supplied-material.json")
    for key, value in (
        ("evidence_records", []),
        ("route", "ANSWER"),
        ("stop_status", "COMPLETE"),
        ("outcome", {"learning_status": "LEARNING_NOT_APPLICABLE"}),
        ("influence", {"recorded": False, "selected_items": [], "withheld_items": []}),
        ("families", []),
    ):
        invalid_ordinary = copy.deepcopy(ordinary)
        invalid_ordinary[key] = value
        expect_failure(
            invalid_ordinary,
            f"synthetic-ordinary-{key}.json",
            f"validator accepted ordinary record with disallowed {key}",
            ordinary=True,
        )

    memory = load_json("qa/applied/receipts/memory-append-only-correction.json")

    def coordinated_root_rewrite(value: dict) -> None:
        rewritten_payload = copy.deepcopy(value["memory_records"][0]["payload"])
        rewritten_payload["statement"] = "A coordinated rewrite replaces the frozen original wording."
        rewritten_digest = canonical_payload_digest(rewritten_payload)
        value["memory_records"][0]["payload"] = rewritten_payload
        value["memory_records"][0]["content_digest"] = rewritten_digest
        value["memory_records"][1]["prior_content_digest"] = rewritten_digest

    def placeholder_memory_payload(value: dict) -> None:
        value["memory_records"][1]["payload"]["statement"] = "done"
        value["memory_records"][1]["content_digest"] = canonical_payload_digest(
            value["memory_records"][1]["payload"]
        )

    def unauthorized_fork(value: dict) -> None:
        value["memory_records"][0]["status"] = "SUPERSEDED"
        value["memory_records"][1]["status"] = "SUPERSEDED"
        fork = copy.deepcopy(value["memory_records"][1])
        fork["id"] = "M-003"
        fork["payload"]["statement"] = "A second linear successor creates an unauthorized fork."
        fork["content_digest"] = canonical_payload_digest(fork["payload"])
        fork["status"] = "CURRENT"
        value["memory_records"].append(fork)
        value["memory_use"]["record_ids"] = ["M-003"]
        value["influence"]["selected_items"] = ["M-003"]
        value["influence"]["withheld_items"] = ["M-001", "M-002"]

    memory_mutations = (
        ("missing-prior", lambda value: value["memory_records"].pop(0)),
        ("silent-overwrite", lambda value: value["memory_records"][0].update({
            "content_digest": "sha256:3333333333333333333333333333333333333333333333333333333333333333"
        })),
        ("payload-without-digest", lambda value: value["memory_records"][1]["payload"].update({
            "statement": "Changed content without a new canonical digest."
        })),
        ("placeholder-payload", placeholder_memory_payload),
        ("coordinated-root-rewrite", coordinated_root_rewrite),
        ("unauthorized-fork", unauthorized_fork),
        ("missing-source", lambda value: value["memory_records"][1]["source_evidence_ids"].append("E-MISSING")),
        ("dangling-use", lambda value: value["memory_use"]["record_ids"].append("M-MISSING")),
        ("revoked-use", lambda value: value["memory_records"][1].update({"permission_state": "REVOKED"})),
        ("rejected-correction", lambda value: value["memory_records"][1].update({"human_disposition": "REJECTED"})),
        ("superseded-use", lambda value: value["memory_use"].update({"record_ids": ["M-001"]})),
        ("superseded-selection", lambda value: value["influence"].update({
            "selected_items": ["M-001"], "withheld_items": ["M-002"]
        })),
        ("multiple-current", lambda value: value["memory_records"][0].update({"status": "CURRENT"})),
    )
    for mutation_name, mutate in memory_mutations:
        invalid_memory = copy.deepcopy(memory)
        mutate(invalid_memory)
        expect_failure(
            invalid_memory,
            f"synthetic-memory-{mutation_name}.json",
            f"validator accepted invalid append-only memory mutation {mutation_name}",
            error_contains=(
                "unauthorized memory fork" if mutation_name == "unauthorized-fork"
                else None
            ),
        )


def validate_receipts() -> None:
    receipt_dir = ROOT / "qa/applied/receipts"
    required_files = {
        "ordinary-supplied-material.json",
        "lightweight-low-stakes.json",
        "layered-ready.json",
        "stopped-budget.json",
        "blocked-permission.json",
        "unknown-permission.json",
        "revoked-permission.json",
        "memory-append-only-correction.json",
    }
    files = sorted(receipt_dir.glob("*.json"))
    require(required_files <= {path.name for path in files},
            "receipt fixture set is missing a required contract case")
    require(not (receipt_dir / "ordinary-low-stakes.json").exists(),
            "layered low-stakes receipt is still mislabeled as ordinary")
    observed_permission_states: set[str] = set()
    for path in files:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise CheckFailure(f"invalid receipt JSON in {path.name}: {exc}") from exc
        require(isinstance(value, dict), f"{path.name} must contain an object")
        if path.name == "ordinary-supplied-material.json":
            validate_ordinary_record(value, path.name)
        else:
            validate_layered_receipt(value, path.name)
            observed_permission_states.add(value["permission"]["state"])
        if path.name == "memory-append-only-correction.json":
            require(value.get("fixture_status") == "SYNTHETIC_CONTRACT_ONLY_NOT_A_RESULT",
                    "F4 memory fixture is not explicitly synthetic/no-result")
    require(observed_permission_states == PERMISSION_STATES,
            "fixtures do not exercise all four typed permission states")


def main() -> int:
    checks = [
        ("six-family JSON and schema contract", validate_spec),
        ("artifact inventory and boundary language", validate_artifact_inventory),
        ("Stage 0 ordinary eligibility and terminal contract", validate_stage_zero_contract),
        ("ordinary and layered receipt contracts", validate_receipts),
        ("permission/reference/memory fail-closed mutations", validate_receipt_guard_mutations),
    ]
    try:
        for label, check in checks:
            check()
            print(f"PASS  {label}")
    except CheckFailure as exc:
        print(f"FAIL  {exc}", file=sys.stderr)
        return 1
    print("PASS  focused applied QA complete (structural/procedural only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
