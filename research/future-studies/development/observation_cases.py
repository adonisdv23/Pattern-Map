"""Construct and validate study-design fixtures. Never calls a model or network.

Oracle keys live outside the model payload. These cases are authored examples,
not observed behavior, empirical measurements or independently approved keys.
"""
from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from pathlib import Path

STATUS = "SYNTHETIC_DESIGN_ONLY_UNRUN_NO_RESULTS"
FIXED = {"access": "AVAILABLE", "permission": "AUTHORIZED", "currency": "CURRENT"}
OBSERVATIONS = {"OBSERVED": "The expected item appears in the captured output.", "NOT_OBSERVED": "The expected item does not appear in the captured output.", "UNKNOWN": "No observation of the expected item is available."}
PROCESSES = {"CHECK_COMPLETED": "The stated scope was completely checked.", "FAILED_CAPTURE": "Capture failed before the stated scope was completely checked.", "NOT_CHECKED": "The stated check was not attempted."}


def packet(case_id, domain, expected, scope, observation, process, world, decision):
    return {"id": case_id, "status": STATUS, "domain": domain, "visible_facts": {"expected_item": expected, "scope": scope, "observation": observation, "process": process, **FIXED}, "oracle_only": {"world_presence": world, "accepted_decision": decision, "claim_ceiling": "Only the explicitly described observation scope"}}


def development_cases():
    args = ("local-review", "decision receipt R7", "the complete supplied folder snapshot at 12:00 UTC")
    return [
        packet("B-DEV-1", *args, "NOT_OBSERVED", "CHECK_COMPLETED", False, "REPORT_ABSENT_IN_SCOPE"),
        packet("B-DEV-2", *args, "NOT_OBSERVED", "FAILED_CAPTURE", False, "RECHECK_OR_KEEP_UNKNOWN"),
        packet("B-DEV-3", *args, "NOT_OBSERVED", "FAILED_CAPTURE", True, "RECHECK_OR_KEEP_UNKNOWN"),
        packet("B-DEV-4", *args, "OBSERVED", "CHECK_COMPLETED", True, "REPORT_PRESENT_IN_SCOPE"),
        packet("B-DEV-5", *args, "OBSERVED", "FAILED_CAPTURE", True, "REPORT_PRESENT_IN_SCOPE"),
        packet("B-DEV-6", *args, "UNKNOWN", "NOT_CHECKED", None, "RECHECK_OR_KEEP_UNKNOWN"),
    ]


def pilot_candidates():
    # Candidate packets need independent key review before any execution.
    domains = [
        ("build-log", "successful completion marker for build 42", "the supplied complete log for build 42"),
        ("file-delivery", "delivery receipt for report Q9", "the supplied delivery journal for the declared one-hour window"),
        ("inventory", "item K3", "the supplied current snapshot of shelf A, with every slot covered"),
        ("event-journal", "event E8", "the supplied complete local journal for sequence numbers 1 through 50"),
    ]
    result = []
    for i, args in enumerate(domains):
        for j, (obs, process, world, decision) in enumerate([
            ("NOT_OBSERVED", "CHECK_COMPLETED", False, "REPORT_ABSENT_IN_SCOPE"),
            ("NOT_OBSERVED", "FAILED_CAPTURE", None, "RECHECK_OR_KEEP_UNKNOWN"),
            ("OBSERVED", "CHECK_COMPLETED", True, "REPORT_PRESENT_IN_SCOPE"),
        ]):
            result.append(packet(f"B-PILOT-{i + 1}-{j + 1}", *args, obs, process, world, decision))
    return result


def model_payload(case, arm, surface=0):
    """No ID, hidden-world key or correct decision enters the model payload."""
    facts = case["visible_facts"]
    if arm == "B1":
        keys = list(facts) if surface == 0 else list(reversed(facts))
        return {key: facts[key] for key in keys}
    if arm != "B0":
        raise ValueError("unknown arm")
    clauses = [f"The expected item is {facts['expected_item']}.", f"The observation scope is {facts['scope']}.", OBSERVATIONS[facts["observation"]], PROCESSES[facts["process"]], "The supplied material is available, its use for this simulated local check is authorized, and it is current."]
    return " ".join(clauses if surface == 0 else list(reversed(clauses)))


def validate(cases):
    ids, seen = set(), {}
    for case in cases:
        assert case["id"] not in ids, "duplicate case ID"
        ids.add(case["id"])
        assert case["status"] == STATUS
        facts, key = case["visible_facts"], case["oracle_only"]
        assert {k: facts[k] for k in FIXED} == FIXED, "initial wedge changes held-fixed axes"
        assert facts["observation"] in OBSERVATIONS and facts["process"] in PROCESSES
        signature = json.dumps(facts, sort_keys=True)
        if signature in seen:
            assert seen[signature] == key["accepted_decision"], "oracle answer depends on an unobservable world"
        seen[signature] = key["accepted_decision"]
        if facts["observation"] == "OBSERVED":
            assert key["world_presence"] is True
            assert key["accepted_decision"] == "REPORT_PRESENT_IN_SCOPE"
        elif facts["process"] == "CHECK_COMPLETED":
            assert facts["observation"] == "NOT_OBSERVED" and key["world_presence"] is False
            assert key["accepted_decision"] == "REPORT_ABSENT_IN_SCOPE"
        else:
            assert key["accepted_decision"] == "RECHECK_OR_KEEP_UNKNOWN"
        for arm in ("B0", "B1"):
            for surface in (0, 1):
                rendered = json.dumps(model_payload(case, arm, surface))
                assert "oracle_only" not in rendered and "world_presence" not in rendered
                assert key["accepted_decision"] not in rendered, "answer leaked to model payload"


def main():
    dev, pilot = development_cases(), pilot_candidates()
    validate(dev + pilot)
    assert len(pilot) == 12 and len({c["domain"] for c in pilot}) == 4
    assert model_payload(dev[1], "B0") == model_payload(dev[2], "B0")
    assert model_payload(dev[1], "B1") == model_payload(dev[2], "B1")
    bad = deepcopy(dev)
    bad[2]["oracle_only"]["accepted_decision"] = "REPORT_ABSENT_IN_SCOPE"
    try:
        validate(bad)
    except AssertionError:
        pass
    else:
        raise AssertionError("hidden-world negative control did not fail")
    discovery = json.loads((Path(__file__).parent / "DISCOVERY_CASES.json").read_text())
    assert len(discovery["cases"]) == 4
    for case in discovery["cases"]:
        assert case["acceptable_routes"] and case["falsifier"] and case["constraints"]
        assert len({source["id"] for source in case["supplied_facts"]}) == len(case["supplied_facts"])
    payload = {"status": STATUS, "development": dev, "pilot_candidates": pilot}
    print(json.dumps({"status": "DESIGN_FIXTURES_VALID", "observation_development_cases": len(dev), "discovery_development_cases": 4, "pilot_candidate_packets": len(pilot), "candidate_payload_sha256": hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest(), "model_calls": 0, "empirical_results": False}, indent=2))


if __name__ == "__main__":
    main()
