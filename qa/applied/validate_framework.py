#!/usr/bin/env python3
"""Focused structural QA for the v16 applied-framework lane.

This script checks artifact structure and guardrails only. It is not an
effectiveness evaluation and does not execute a model, provider, study, or
external action.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


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


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def require_string(value: object, message: str) -> None:
    require(nonempty(value), message)


def require_string_list(value: object, message: str, *, allow_empty: bool = False) -> None:
    require(isinstance(value, list), message)
    if not allow_empty:
        require(bool(value), message)
    require(all(nonempty(item) for item in value), message)


def validate_outcome(receipt: dict, filename: str) -> None:
    outcome = receipt.get("outcome", {})
    learning_statuses = {
        "LEARNING_PLANNED",
        "LEARNING_PENDING_OUTCOME",
        "LEARNING_REVIEWED",
        "LEARNING_NOT_APPLICABLE",
    }
    require(outcome.get("learning_status") in learning_statuses,
            f"{filename}: outcome needs a canonical learning status")
    if outcome.get("applicable") is True:
        require(outcome.get("learning_status") in {
                    "LEARNING_PENDING_OUTCOME", "LEARNING_REVIEWED"},
                f"{filename}: applicable outcome needs pending or reviewed state")
        require(outcome.get("expectation_recorded") is True,
                f"{filename}: learning needs a pre-outcome expectation")
        require(outcome.get("update_applied") is False,
                f"{filename}: fixture must not silently apply a learning update")
        if outcome.get("learning_status") == "LEARNING_REVIEWED":
            require(outcome.get("review_recorded") is True,
                    f"{filename}: LEARNING_REVIEWED needs a recorded outcome review")
            observed = outcome.get("observed_outcome")
            missing = outcome.get("missing_outcome_reason")
            require(nonempty(observed) or nonempty(missing),
                    f"{filename}: LEARNING_REVIEWED needs an observed or explicitly missing outcome")
            require(outcome.get("human_disposition") in {
                        "ACCEPTED", "REJECTED", "DEFERRED", "OVERRIDDEN",
                        "REQUEST_ENRICHMENT"},
                    f"{filename}: LEARNING_REVIEWED needs a canonical human disposition")
    else:
        require(outcome.get("learning_status") == "LEARNING_NOT_APPLICABLE",
                f"{filename}: non-applicable outcome must say LEARNING_NOT_APPLICABLE")


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
    require(isinstance(permission, dict) and required <= set(permission),
            f"{filename}: permission record is incomplete")
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
    required = {"id", "exact_pointer", "claim_ids", "permission_state"}
    for record in records:
        require(isinstance(record, dict) and required <= set(record),
                f"{filename}: evidence record is incomplete")
        record_id = record["id"]
        require_string(record_id, f"{filename}: evidence ID is empty")
        require(record_id not in index, f"{filename}: duplicate evidence ID {record_id}")
        require_string(record["exact_pointer"],
                       f"{filename}: {record_id} lacks an exact pointer")
        require_string_list(record["claim_ids"],
                            f"{filename}: {record_id} lacks claim references")
        require(record["permission_state"] in PERMISSION_STATES,
                f"{filename}: {record_id} has an untyped permission state")
        index[record_id] = record
    return index


def validate_baseline_records(receipt: dict, filename: str,
                              evidence: dict[str, dict]) -> list[dict]:
    records = receipt.get("baseline_records")
    require(isinstance(records, list), f"{filename}: baseline_records must be a list")
    seen: set[str] = set()
    required = {
        "id", "basis", "observation_boundary", "evidence_ids",
        "motion_timepoints", "absence_expected",
    }
    for record in records:
        require(isinstance(record, dict) and required <= set(record),
                f"{filename}: baseline record is incomplete")
        record_id = record["id"]
        require_string(record_id, f"{filename}: baseline ID is empty")
        require(record_id not in seen, f"{filename}: duplicate baseline ID {record_id}")
        seen.add(record_id)
        require_string(record["basis"], f"{filename}: {record_id} lacks a basis")
        require_string(record["observation_boundary"],
                       f"{filename}: {record_id} lacks an observation boundary")
        require_string_list(record["evidence_ids"],
                            f"{filename}: {record_id} lacks evidence references")
        for evidence_id in record["evidence_ids"]:
            require(evidence_id in evidence,
                    f"{filename}: {record_id} references missing evidence {evidence_id}")
            require(evidence[evidence_id]["permission_state"] == "AUTHORIZED",
                    f"{filename}: {record_id} uses blocked evidence {evidence_id}")
        require(isinstance(record["motion_timepoints"], int)
                and record["motion_timepoints"] >= 0,
                f"{filename}: {record_id} has invalid motion_timepoints")
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
        require(isinstance(record, dict) and required <= set(record),
                f"{filename}: comparison record is incomplete")
        record_id = record["id"]
        require_string(record_id, f"{filename}: comparison ID is empty")
        require(record_id not in seen, f"{filename}: duplicate comparison ID {record_id}")
        seen.add(record_id)
        for key in ("unit", "alignment_boundary", "result"):
            require_string(record[key], f"{filename}: {record_id} has empty {key}")
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
        require(isinstance(record, dict) and required <= set(record),
                f"{filename}: disconfirmation record is incomplete")
        record_id = record["id"]
        require_string(record_id, f"{filename}: disconfirmation ID is empty")
        require(record_id not in seen,
                f"{filename}: duplicate disconfirmation ID {record_id}")
        seen.add(record_id)
        for key in ("route_or_query", "target", "result", "residual_uncertainty"):
            require_string(record[key], f"{filename}: {record_id} has empty {key}")
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
        "id", "version", "source_scope", "content_digest",
        "source_evidence_ids", "permission_state", "reuse_scope", "status",
        "supersedes", "corrects", "prior_content_digest", "correction_reason",
    }
    digest_pattern = re.compile(r"^sha256:[0-9a-f]{64}$")
    for record in records:
        require(isinstance(record, dict) and required <= set(record),
                f"{filename}: memory record is incomplete")
        record_id = record["id"]
        require_string(record_id, f"{filename}: memory ID is empty")
        require(record_id not in index, f"{filename}: duplicate memory ID {record_id}")
        require(isinstance(record["version"], int) and record["version"] >= 1,
                f"{filename}: {record_id} has invalid version")
        require_string(record["source_scope"],
                       f"{filename}: {record_id} lacks source scope")
        require(isinstance(record["content_digest"], str)
                and digest_pattern.fullmatch(record["content_digest"]) is not None,
                f"{filename}: {record_id} lacks a canonical content digest")
        require_string_list(record["source_evidence_ids"],
                            f"{filename}: {record_id} lacks source evidence")
        for evidence_id in record["source_evidence_ids"]:
            require(evidence_id in evidence,
                    f"{filename}: {record_id} references missing source evidence {evidence_id}")
            require(evidence[evidence_id]["permission_state"] == "AUTHORIZED",
                    f"{filename}: {record_id} derives memory from blocked evidence {evidence_id}")
        require(record["permission_state"] in PERMISSION_STATES,
                f"{filename}: {record_id} has untyped permission")
        require_string(record["reuse_scope"],
                       f"{filename}: {record_id} lacks a reuse scope")
        require(record["status"] in {"CURRENT", "SUPERSEDED"},
                f"{filename}: {record_id} has invalid status")
        index[record_id] = record

    for record_id, record in index.items():
        link_values = (record["supersedes"], record["corrects"])
        if link_values == (None, None):
            require(record["prior_content_digest"] is None
                    and record["correction_reason"] is None,
                    f"{filename}: original {record_id} invents correction metadata")
            continue
        require(all(nonempty(value) for value in link_values)
                and record["supersedes"] == record["corrects"],
                f"{filename}: {record_id} must link the same preserved correction target")
        target_id = record["supersedes"]
        require(target_id in index,
                f"{filename}: {record_id} references missing prior memory {target_id}")
        target = index[target_id]
        require(record["version"] > target["version"],
                f"{filename}: {record_id} does not advance the prior version")
        require(record["prior_content_digest"] == target["content_digest"],
                f"{filename}: {record_id} prior digest does not match preserved {target_id}")
        require_string(record["correction_reason"],
                       f"{filename}: {record_id} lacks a correction reason")
        require(record["status"] == "CURRENT" and target["status"] == "SUPERSEDED",
                f"{filename}: correction must append CURRENT and preserve SUPERSEDED records")
    return index


def validate_layered_receipt(receipt: dict, filename: str) -> None:
    common_required = {
        "receipt_id", "operating_level", "evidence_selection", "consequence",
        "permission", "budget", "evidence_records", "baseline_records",
        "comparison_records", "disconfirmation_records", "memory_records",
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

    influence = receipt["influence"]
    require(isinstance(influence, dict), f"{filename}: influence must be an object")
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
        require(not influence["recorded"] and not selected_items,
                f"{filename}: {permission_state} material cannot influence output")
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
        require(bool(comparisons),
                f"{filename}: high-consequence answer needs a substantive comparison record")
        require(bool(disconfirmations),
                f"{filename}: high-consequence answer needs a substantive disconfirmation record")

    if route in {"ANSWER", "ANSWER_PROVISIONALLY"}:
        require(influence["recorded"] is True,
                f"{filename}: answer route needs a resolvable influence receipt")

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

    if receipt.get("motion_claim") is True:
        require(any(record["motion_timepoints"] >= 2 for record in baselines),
                f"{filename}: motion claim needs a baseline with repeated observations")
    if receipt.get("absence_claim") is True:
        require(any(record["absence_expected"] is True for record in baselines),
                f"{filename}: absence claim needs an expected baseline")
    if receipt.get("independence_claim") is True:
        require(any(record["origin_state"] == "INDEPENDENT" for record in comparisons),
                f"{filename}: independence claim needs an independent comparison relation")


def expect_failure(value: dict, filename: str, message: str,
                   *, ordinary: bool = False) -> None:
    try:
        if ordinary:
            validate_ordinary_record(value, filename)
        else:
            validate_layered_receipt(value, filename)
    except CheckFailure:
        return
    raise CheckFailure(message)


def validate_receipt_guard_mutations() -> None:
    """Fail closed on status-only, dangling-reference, and overwrite mutations."""

    base = load_json("qa/applied/receipts/layered-ready.json")

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
            "human_disposition": "DEFERRED",
        }
    )
    validate_layered_receipt(valid, "synthetic-reviewed-contract-control.json")

    for mutation_name, mutate in (
        ("baseline-dangling", lambda value: value["baseline_records"][0]["evidence_ids"].append("E-MISSING")),
        ("comparison-empty-unit", lambda value: value["comparison_records"][0].update({"unit": ""})),
        ("comparison-dangling", lambda value: value["comparison_records"][0]["item_ids"].append("E-MISSING")),
        ("comparison-revoked", lambda value: value["evidence_records"][1].update({"permission_state": "REVOKED"})),
        ("disconfirmation-empty-query", lambda value: value["disconfirmation_records"][0].update({"route_or_query": ""})),
        ("disconfirmation-dangling", lambda value: value["disconfirmation_records"][0]["evidence_ids"].append("E-MISSING")),
        ("influence-dangling", lambda value: value["influence"]["selected_items"].append("E-MISSING")),
    ):
        invalid_reference = copy.deepcopy(base)
        mutate(invalid_reference)
        expect_failure(
            invalid_reference,
            f"synthetic-{mutation_name}.json",
            f"validator accepted malformed or unresolved {mutation_name} record",
        )

    invalid_influence_permission = copy.deepcopy(base)
    invalid_influence_permission["evidence_records"].append(
        {
            "id": "E-UNKNOWN",
            "exact_pointer": "synthetic://unresolved/item",
            "claim_ids": ["C-UNKNOWN"],
            "permission_state": "UNKNOWN",
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

    invalid_permission = copy.deepcopy(base)
    invalid_permission["permission"]["state"] = True
    expect_failure(
        invalid_permission,
        "synthetic-boolean-permission.json",
        "validator accepted a boolean authorization state",
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
            "exact_pointer": "synthetic://blocked/item",
            "claim_ids": ["C-BLOCKED"],
            "permission_state": "NOT_AUTHORIZED",
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

    ordinary = load_json("qa/applied/receipts/ordinary-supplied-material.json")
    for key, value in (
        ("evidence_records", []),
        ("route", "ANSWER"),
        ("stop_status", "COMPLETE"),
        ("outcome", {"learning_status": "LEARNING_NOT_APPLICABLE"}),
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
    memory_mutations = (
        ("missing-prior", lambda value: value["memory_records"].pop(0)),
        ("silent-overwrite", lambda value: value["memory_records"][0].update({
            "content_digest": "sha256:3333333333333333333333333333333333333333333333333333333333333333"
        })),
        ("missing-source", lambda value: value["memory_records"][1]["source_evidence_ids"].append("E-MISSING")),
        ("dangling-use", lambda value: value["memory_use"]["record_ids"].append("M-MISSING")),
        ("revoked-use", lambda value: value["memory_records"][1].update({"permission_state": "REVOKED"})),
    )
    for mutation_name, mutate in memory_mutations:
        invalid_memory = copy.deepcopy(memory)
        mutate(invalid_memory)
        expect_failure(
            invalid_memory,
            f"synthetic-memory-{mutation_name}.json",
            f"validator accepted invalid append-only memory mutation {mutation_name}",
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
