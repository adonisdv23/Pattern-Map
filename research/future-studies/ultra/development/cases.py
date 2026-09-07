"""Pure authored decision specification: no network, model, runner or real action.

Property checks consume independently reviewed properties. They never infer
truth from an implementation's self-description or automatically grade prose.
"""
from copy import deepcopy
import hashlib
import json
import math
from itertools import combinations

from case_objects import STATUS, author_objects

VISIBLE_FIELDS = ("task", "candidates", "constraints", "limits", "cost_basis",
                  "utility_assumptions", "action_set", "action_contract",
                  "output_contract", "scope_boundary")
HARM_CLASSES = ("false_absence", "unsupported_presence", "unsupported_selection",
                "invalid_transfer", "missed_feasible_option", "needless_hold_or_recheck",
                "scope_or_permission_error", "effort_failure")


def initial_state(case):
    return {"acquired_ids": [], "rejected_ids": [], "spent_units": 0,
            "history": [], "terminal_state": None, "final_response": None}


def visible_payload(case, state):
    """Allowlisted deep copy excluding case identity, unopened details and all keys."""
    payload = {name: deepcopy(case[name]) for name in VISIBLE_FIELDS}
    acquired = set(state["acquired_ids"])
    payload["evidence"] = deepcopy(case["initial_evidence"]) + [
        deepcopy(item) for item in case["evidence_pool"] if item["id"] in acquired]
    payload["state"] = deepcopy(state)
    return payload


def render(case, state, surface="paragraph", reverse=False):
    """Same JSON-encoded field clauses, with only paragraph/list separators changed.

    These are lexical parity/order checks, not independent natural paraphrases.
    """
    items = list(visible_payload(case, state).items())
    if reverse:
        items.reverse()
    clauses = [json.dumps(name) + ": " + json.dumps(value, sort_keys=True)
               for name, value in items]
    if surface == "paragraph":
        return "\n\n".join(clauses)
    if surface == "list":
        return "\n".join("- " + clause for clause in clauses)
    raise ValueError("unknown surface")


def apply_action(case, state, action_id, candidate_ids=(), response=None):
    """Return a new state; inspect static evidence and account for every attempt.

    Free successful bookkeeping and terminal actions are not acquisition. Invalid
    or rejected attempts cost the declared failure unit; no step performs work
    outside these authored objects.
    """
    if state["terminal_state"] is not None:
        raise ValueError("episode already terminal")
    result = deepcopy(state)
    actions = {item["id"]: item for item in case["action_set"]}
    action = actions.get(action_id)
    entry = {"action_id": action_id, "candidate_ids": list(candidate_ids),
             "status": "APPLIED"}
    valid = {item["id"] for item in case["candidates"]}
    if action is None:
        entry["status"] = "REJECTED_UNKNOWN_ACTION"
    elif action["kind"] in ("REJECT", "REOPEN", "COMPARE"):
        expected = 2 if action["kind"] == "COMPARE" else 1
        if len(candidate_ids) != expected or len(set(candidate_ids)) != expected or not set(candidate_ids) <= valid:
            entry["status"] = "REJECTED_CANDIDATE_ARGUMENT"
        elif action["kind"] == "REOPEN" and not case["limits"]["pruning_reversible"]:
            entry["status"] = "REJECTED_IRREVERSIBLE"
    elif action["kind"] == "SELECT":
        if not set(candidate_ids) <= valid or set(candidate_ids) & set(result["rejected_ids"]):
            entry["status"] = "REJECTED_SELECTION"
        elif not candidate_ids and not (response or {}).get("implementation"):
            entry["status"] = "REJECTED_EMPTY_SELECTION"
    requested = (case["limits"]["invalid_attempt_units"] if entry["status"].startswith("REJECTED")
                 else action["cost_units"])
    remaining = case["limits"]["acquisition_units"] - result["spent_units"]
    charged = min(remaining, requested)
    result["spent_units"] += charged
    entry.update({"charged_units": charged, "requested_units": requested})
    if charged < requested:
        entry["pre_budget_status"] = entry["status"]
        entry["status"] = "REJECTED_BUDGET"
        result["terminal_state"] = "STOP"
    elif entry["status"] == "APPLIED":
        kind = action["kind"]
        if kind == "INSPECT":
            identifier = action["evidence_id"]
            if identifier in result["acquired_ids"]:
                entry["status"] = "DUPLICATE_INSPECTION"
            else:
                result["acquired_ids"].append(identifier)
        elif kind == "REJECT":
            result["rejected_ids"] = sorted(set(result["rejected_ids"]) | set(candidate_ids))
        elif kind == "REOPEN":
            result["rejected_ids"] = sorted(set(result["rejected_ids"]) - set(candidate_ids))
        elif kind in ("SELECT", "HOLD", "STOP"):
            result["terminal_state"] = kind
            result["final_response"] = deepcopy(response)
    result["history"].append(entry)
    if len(result["history"]) >= case["limits"]["maximum_attempts"] and result["terminal_state"] is None:
        result["terminal_state"] = "STOP"
        entry["attempt_limit_reached"] = True
    return result


def assess_reviewed_properties(case, rubric, properties, assertion, next_action,
                               evidence_ids, state):
    """Check externally adjudicated properties; NOT an automatic text grader.

    None means semantic review is absent. Novel implementation names do not
    enter the feasibility predicate. Its use of property labels proves no prose
    output actually has those properties.
    """
    available = {item["id"] for item in visible_payload(case, state)["evidence"]}
    if not set(evidence_ids) <= available:
        return {"status": "UNSUPPORTED_CITATION", "assertion_correct": None,
                "constraint_satisfied": None, "next_action_accepted": None}
    if properties is None:
        return {"status": "REQUIRES_SEMANTIC_REVIEW", "assertion_correct": None,
                "constraint_satisfied": None, "next_action_accepted": None}
    if not set(rubric["key_context_evidence_ids"]) <= available:
        return {"status": "REQUIRES_PARTIAL_EVIDENCE_REVIEW", "assertion_correct": None,
                "constraint_satisfied": None, "next_action_accepted": None}
    props = set(properties)
    feasible = (set(rubric["required_properties"]) <= props
                and not set(rubric["forbidden_properties"]) & props)
    return {"status": "REQUIRES_ACTION_REVIEW" if next_action is None else "AUTHORED_PROPERTY_CHECK_ONLY",
            "assertion_correct": assertion == rubric["assertion"],
            "constraint_satisfied": feasible,
            "next_action_accepted": None if next_action is None else next_action in rubric["accepted_next_actions"],
            "utility_graded": case["utility_assumptions"]["graded"]}


def optimal_authored_actions(case):
    """Only the explicit F5 loss/deadline table, never a general utility measure."""
    spec = case["utility_assumptions"]
    if not spec["graded"]:
        return None
    feasible = {name: value["loss_units"] for name, value in spec["actions"].items()
                if value["steps"] <= spec["deadline_steps"]}
    if not feasible:
        return set()
    best = min(feasible.values())
    return {name for name, loss in feasible.items() if loss == best}


def filter_independent(candidates, feasible, exploratory_first):
    """Complete common facts, fixed independent checks, no resource/pruning effect.

    Both return the complete accepted set. This finite illustration says nothing
    empirical about a model's internal reasoning.
    """
    if exploratory_first:
        retained = list(candidates)
        return tuple(item for item in retained if feasible[item])
    accepted = []
    for item in candidates:
        if feasible[item]:
            accepted.append(item)
    return tuple(accepted)


def feasible_combinations(component_properties, required):
    """Subset closure illustrates nonseparable feasibility, not a search policy."""
    identifiers = list(component_properties)
    return {frozenset(group) for size in range(1, len(identifiers) + 1)
            for group in combinations(identifiers, size)
            if set(required) <= set().union(*(component_properties[item] for item in group))}


def advancement_rule(comparisons, thresholds, *, instrument_valid):
    """Illustrative gate with caller-supplied values; never authorizes execution.

    Each contrast contains task-cluster rows and separate resource-cost deltas.
    This arithmetic is not an uncertainty estimator or a pilot result.
    """
    required = {"minimum_mean_gain", "maximum_cost_deltas"}
    if thresholds is None or not required <= set(thresholds):
        return "UNSET_VALUE_JUDGMENTS"
    if not instrument_valid or set(comparisons) != {"ordinary", "purpose_mechanism"}:
        return "REDESIGN_INSTRUMENT"
    delta = thresholds["minimum_mean_gain"]
    if isinstance(delta, bool) or not isinstance(delta, (int, float)) or not math.isfinite(delta) or delta <= 0:
        return "UNSET_VALUE_JUDGMENTS"
    if not thresholds["maximum_cost_deltas"] or any(
            isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value)
            for value in thresholds["maximum_cost_deltas"].values()):
        return "UNSET_VALUE_JUDGMENTS"
    for contrast in comparisons.values():
        rows = contrast["rows"]
        if not rows or any(row["ambiguous"] for row in rows):
            return "REDESIGN_INSTRUMENT"
        if any(isinstance(row["acceptance_delta"], bool)
               or not isinstance(row["acceptance_delta"], (int, float))
               or not math.isfinite(row["acceptance_delta"])
               or not -1 <= row["acceptance_delta"] <= 1 for row in rows):
            return "REDESIGN_INSTRUMENT"
        mean = sum(row["acceptance_delta"] for row in rows) / len(rows)
        if mean < thresholds["minimum_mean_gain"]:
            return "DO_NOT_ADVANCE"
        for group in ("domain", "regime"):
            for value in {row[group] for row in rows}:
                if sum(row["acceptance_delta"] for row in rows if row[group] == value) < 0:
                    return "DO_NOT_ADVANCE"
        for row in rows:
            if set(row["error_increases"]) != set(HARM_CLASSES):
                return "REDESIGN_INSTRUMENT"
            if any(type(value) is not int for value in row["error_increases"].values()):
                return "REDESIGN_INSTRUMENT"
            if type(row["treatment_scope_errors"]) is not int or row["treatment_scope_errors"] < 0:
                return "REDESIGN_INSTRUMENT"
            if row["treatment_scope_errors"] > 0:
                return "DO_NOT_ADVANCE"
        for error_class in HARM_CLASSES:
            if sum(row["error_increases"][error_class] for row in rows) > 0:
                return "DO_NOT_ADVANCE"
            for regime in {row["regime"] for row in rows}:
                if sum(row["error_increases"][error_class] for row in rows
                       if row["regime"] == regime) > 0:
                    return "DO_NOT_ADVANCE"
        if set(contrast["cost_deltas"]) != set(thresholds["maximum_cost_deltas"]):
            return "REDESIGN_INSTRUMENT"
        if any(not isinstance(value, (int, float)) or not math.isfinite(value)
               for value in contrast["cost_deltas"].values()):
            return "REDESIGN_INSTRUMENT"
        if any(value > thresholds["maximum_cost_deltas"][kind]
               for kind, value in contrast["cost_deltas"].items()):
            return "DO_NOT_ADVANCE"
    return "ELIGIBLE_FOR_DESIGN_REVIEW_ONLY"


def validate_objects(cases, keys):
    if set(cases) != set(keys):
        raise ValueError("case/key mismatch")
    for identifier, case in cases.items():
        if case["id"] != identifier or case["status"] != STATUS:
            raise ValueError("case identity/status mismatch")
        source_ids = [item["id"] for item in case["initial_evidence"] + case["evidence_pool"]]
        if len(source_ids) != len(set(source_ids)):
            raise ValueError("duplicate evidence ID")
        pool_ids = {item["id"] for item in case["evidence_pool"]}
        if any(not set(item["detail_evidence_ids"]) <= pool_ids for item in case["candidates"]):
            raise ValueError("dangling catalogue evidence")
        if not keys[identifier]["required_properties"] or not case["constraints"]:
            raise ValueError("missing acceptance constraints")
        authored = optimal_authored_actions(case)
        if authored is not None and authored != set(keys[identifier]["accepted_next_actions"]):
            raise ValueError("action key conflicts with supplied utility table")


def main():
    cases, keys = author_objects()
    validate_objects(cases, keys)
    def digest(value):
        return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()
    print(json.dumps({"status": STATUS, "families": len({item["family"] for item in cases.values()}),
                      "variants": len(cases), "case_sha256": digest(cases),
                      "key_sha256": digest(keys), "empirical_results": False,
                      "model_calls": 0, "semantic_validation": "REQUIRES_INDEPENDENT_REVIEW"}, indent=2))


if __name__ == "__main__":
    main()
