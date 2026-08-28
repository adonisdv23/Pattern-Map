#!/usr/bin/env python3
"""Focused structural QA for the v16 applied-framework lane.

This script checks artifact structure and guardrails only. It is not an
effectiveness evaluation and does not execute a model, provider, study, or
external action.
"""

from __future__ import annotations

import copy
import json
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
        "framework/templates/ACQUISITION_RECEIPT.md",
        "framework/templates/EVIDENCE_REGISTER.md",
        "framework/templates/COMPARISON_MATRIX.md",
        "framework/templates/DISCONFIRMATION_LOG.md",
        "framework/templates/INFLUENCE_RECEIPT.md",
        "framework/templates/OUTCOME_REVIEW.md",
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
    require("record `not_authorized`" in preflight.lower()
            and "record `unknown`" in preflight.lower(),
            "preflight does not preserve distinct permission stop states")

    require("preserve UNKNOWN and escalate" in quickstart,
            "Quickstart collapses unknown permission into NOT_AUTHORIZED")
    copyable_brief = read_text("framework/agent-playbook/COPYABLE_AGENT_BRIEF.md")
    require("preserve UNKNOWN when permission has not been established" in copyable_brief,
            "copyable brief collapses unknown permission into NOT_AUTHORIZED")

    for relative in ("cases/general-research/README.md", "cases/product-and-process/README.md"):
        case = read_text(relative).lower()
        require("illustrative fixture" in case, f"{relative} is not marked as a fixture")
        require("not empirical" in case, f"{relative} lacks non-empirical boundary")
        require("human" in case and "permission" in case, f"{relative} lacks human/permission boundary")


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
            require(
                (isinstance(observed, str) and bool(observed.strip()))
                or (isinstance(missing, str) and bool(missing.strip())),
                f"{filename}: LEARNING_REVIEWED needs an observed or explicitly missing outcome",
            )
            require(outcome.get("human_disposition") in {
                        "ACCEPTED", "REJECTED", "DEFERRED", "OVERRIDDEN",
                        "REQUEST_ENRICHMENT"},
                    f"{filename}: LEARNING_REVIEWED needs a canonical human disposition")
    else:
        require(outcome.get("learning_status") == "LEARNING_NOT_APPLICABLE",
                f"{filename}: non-applicable outcome must say LEARNING_NOT_APPLICABLE")


def validate_receipt(receipt: dict, filename: str) -> None:
    common_required = {
        "receipt_id",
        "operating_level",
        "evidence_selection",
        "consequence",
        "permission",
        "budget",
        "route",
        "stop_status",
        "stop_reason",
        "outcome",
    }
    require(common_required <= set(receipt), f"{filename} is missing common receipt keys")
    permission = receipt["permission"]
    budget = receipt["budget"]
    route = receipt["route"]
    stop_status = receipt["stop_status"]
    stop_reason = receipt["stop_reason"].lower()

    routes = {
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
    stop_statuses = {
        "CONTINUE",
        "COMPLETE",
        "STOPPED_BUDGET",
        "STOPPED_DEADLINE",
        "STOPPED_OTHER",
    }
    require(route in routes, f"{filename}: route is not canonical: {route}")
    require(stop_status in stop_statuses,
            f"{filename}: stop status is not canonical: {stop_status}")

    require(isinstance(permission.get("technical_access"), bool),
            f"{filename}: technical access must be boolean")
    require(isinstance(permission.get("authorized"), bool),
            f"{filename}: authorization must be boolean")
    require(isinstance(budget.get("remaining_minutes"), (int, float)),
            f"{filename}: remaining budget must be numeric")
    require(receipt["consequence"] in {"LOW", "MEDIUM", "HIGH"},
            f"{filename}: consequence is not canonical")
    validate_outcome(receipt, filename)

    operating_level = receipt["operating_level"]
    evidence_selection = receipt["evidence_selection"]
    if operating_level == "ORDINARY":
        layered_keys = {"baseline", "comparison", "disconfirmation", "influence"}
        require(evidence_selection == "NONE",
                f"{filename}: ordinary path cannot select or acquire evidence")
        require(receipt["consequence"] == "LOW",
                f"{filename}: ordinary fixture must be low consequence")
        require(permission.get("authorized") is True
                and permission.get("disclosure_allowed") is True,
                f"{filename}: ordinary supplied-material use must be authorized")
        require(receipt.get("supplied_material_only") is True,
                f"{filename}: ordinary path must be supplied-material only")
        require(receipt.get("external_action") is False,
                f"{filename}: ordinary path cannot authorize external action")
        require(route == "ANSWER" and stop_status == "COMPLETE",
                f"{filename}: ordinary path must end in ANSWER / COMPLETE")
        require(not (layered_keys & set(receipt)),
                f"{filename}: ordinary path must not fabricate layered evidence records")
        require(isinstance(receipt.get("assumptions"), list) and receipt["assumptions"],
                f"{filename}: ordinary path must name its assumptions")
        require(isinstance(receipt.get("unchecked_boundaries"), list)
                and receipt["unchecked_boundaries"],
                f"{filename}: ordinary path must name what was not checked")
        return

    require(operating_level in {"LIGHTWEIGHT", "MODERATE", "ADVANCED"},
            f"{filename}: operating level is not canonical")
    require(evidence_selection == "NEEDED",
            f"{filename}: layered route must record evidence selection as needed")
    layered_required = {"baseline", "comparison", "disconfirmation", "influence"}
    require(layered_required <= set(receipt), f"{filename} is missing layered receipt keys")
    baseline = receipt["baseline"]
    comparison = receipt["comparison"]
    disconfirmation = receipt["disconfirmation"]
    influence = receipt["influence"]
    require(isinstance(influence.get("recorded"), bool),
            f"{filename}: influence recorded must be boolean")
    selected_items = influence.get("selected_items")
    require(isinstance(selected_items, list),
            f"{filename}: selected influence items must be a list")
    if influence["recorded"]:
        require(bool(selected_items),
                f"{filename}: recorded influence needs at least one selected item")
    else:
        require(not selected_items,
                f"{filename}: unrecorded influence cannot contain selected items")

    if not permission["authorized"]:
        require(route in {"HOLD", "ESCALATE", "REFUSE"},
                f"{filename}: unauthorized work must hold, escalate, or refuse")
        require(stop_status != "CONTINUE",
                f"{filename}: unauthorized work cannot remain in CONTINUE state")
        require("permission" in stop_reason or "access" in stop_reason,
                f"{filename}: unauthorized stop reason must name permission/access")
        require(not influence["recorded"],
                f"{filename}: unauthorized item cannot be marked influential")

    if receipt["consequence"] == "HIGH" and route in {"ANSWER", "ANSWER_PROVISIONALLY"}:
        require(baseline.get("present") is True,
                f"{filename}: high-consequence answer needs a baseline")
        require(comparison.get("done") is True,
                f"{filename}: high-consequence answer needs comparison")
        require(disconfirmation.get("attempted") is True,
                f"{filename}: high-consequence answer needs disconfirmation")

    if route in {"ANSWER", "ANSWER_PROVISIONALLY"}:
        require(influence["recorded"] is True,
                f"{filename}: answer route needs an influence receipt")

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
        require(baseline.get("motion_repeated") is True,
                f"{filename}: motion claim needs repeated observations")
    if receipt.get("absence_claim") is True:
        require(baseline.get("absence_expected") is True,
                f"{filename}: absence claim needs an expected baseline")
    if receipt.get("independence_claim") is True:
        require(comparison.get("origin_state") == "INDEPENDENT",
                f"{filename}: independence claim needs an independent relation")

def validate_receipt_guard_mutations() -> None:
    """Prove reviewed-learning cannot be asserted by changing one status token."""

    base = json.loads(read_text("qa/applied/receipts/layered-ready.json"))
    invalid = copy.deepcopy(base)
    invalid["outcome"]["learning_status"] = "LEARNING_REVIEWED"
    try:
        validate_receipt(invalid, "synthetic-reviewed-without-review.json")
    except CheckFailure:
        pass
    else:
        raise CheckFailure(
            "validator accepted LEARNING_REVIEWED without an outcome review and disposition"
        )

    valid = copy.deepcopy(invalid)
    valid["outcome"].update(
        {
            "review_recorded": True,
            "observed_outcome": "SYNTHETIC_CONTRACT_OBSERVATION_ONLY",
            "human_disposition": "DEFERRED",
        }
    )
    validate_receipt(valid, "synthetic-reviewed-contract-control.json")

    invalid_influence = copy.deepcopy(base)
    invalid_influence["influence"]["selected_items"] = []
    try:
        validate_receipt(invalid_influence, "synthetic-empty-recorded-influence.json")
    except CheckFailure:
        pass
    else:
        raise CheckFailure(
            "validator accepted recorded influence without a selected item"
        )

    blocked = json.loads(read_text("qa/applied/receipts/blocked-permission.json"))
    invalid_blocked = copy.deepcopy(blocked)
    invalid_blocked["influence"]["selected_items"] = ["UNAUTHORIZED-ITEM"]
    try:
        validate_receipt(invalid_blocked, "synthetic-unrecorded-selected-item.json")
    except CheckFailure:
        pass
    else:
        raise CheckFailure(
            "validator accepted selected material while influence was unrecorded"
        )

    ordinary = json.loads(read_text("qa/applied/receipts/ordinary-supplied-material.json"))
    for key, value in (
        ("comparison", {"done": True}),
        ("evidence_selection", "NEEDED"),
    ):
        invalid_ordinary = copy.deepcopy(ordinary)
        invalid_ordinary[key] = value
        try:
            validate_receipt(invalid_ordinary, f"synthetic-ordinary-{key}.json")
        except CheckFailure:
            pass
        else:
            raise CheckFailure(
                f"validator accepted ordinary path with disallowed {key}"
            )


def validate_receipts() -> None:
    receipt_dir = ROOT / "qa/applied/receipts"
    files = sorted(receipt_dir.glob("*.json"))
    require(len(files) >= 5, "receipt fixture set is too small")
    require((receipt_dir / "ordinary-supplied-material.json").is_file(),
            "genuine Stage-0 ordinary receipt fixture is missing")
    require(not (receipt_dir / "ordinary-low-stakes.json").exists(),
            "layered low-stakes receipt is still mislabeled as ordinary")
    for path in files:
        try:
            receipt = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise CheckFailure(f"invalid receipt JSON in {path.name}: {exc}") from exc
        require(isinstance(receipt, dict), f"{path.name} must contain an object")
        validate_receipt(receipt, path.name)


def main() -> int:
    checks = [
        ("six-family JSON and schema contract", validate_spec),
        ("artifact inventory and boundary language", validate_artifact_inventory),
        ("receipt fixtures through preflight/stop logic", validate_receipts),
        ("reviewed-learning fail-closed guard mutations", validate_receipt_guard_mutations),
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
