"""Deterministic authored checks; no sampled behavior, study or benchmark."""
from copy import deepcopy
from itertools import permutations, product
import json
import unittest

from case_objects import author_objects
from cases import (
    HARM_CLASSES, advancement_rule, apply_action, assess_reviewed_properties,
    feasible_combinations, filter_independent, initial_state,
    optimal_authored_actions, render, validate_objects, visible_payload,
)


class DevelopmentObjects(unittest.TestCase):
    def setUp(self):
        self.cases, self.keys = author_objects()

    def inspect_key_context(self, identifier):
        case, rubric = self.cases[identifier], self.keys[identifier]
        state = initial_state(case)
        for source in rubric["key_context_evidence_ids"]:
            if source.startswith("d"):
                state = apply_action(case, state, "INSPECT:" + source)
        return state

    def assess(self, identifier, state=None, **overrides):
        case, rubric = self.cases[identifier], self.keys[identifier]
        state = state if state is not None else self.inspect_key_context(identifier)
        args = {"properties": rubric["required_properties"], "assertion": rubric["assertion"],
                "next_action": rubric["accepted_next_actions"][0], "evidence_ids": ["e1"]}
        args.update(overrides)
        return assess_reviewed_properties(case, rubric, state=state, **args)

    def test_eight_distinct_authored_families_with_paired_variants(self):
        validate_objects(self.cases, self.keys)
        self.assertEqual(len(self.cases), 16)
        self.assertEqual(len({case["family"] for case in self.cases.values()}), 8)
        self.assertEqual(len({case["task"] for case in self.cases.values()}), 8)
        for case in self.cases.values():
            self.assertTrue(case["candidates"] and case["action_set"] and case["constraints"])

    def test_projection_serialization_lexical_parity_and_key_isolation(self):
        for identifier, case in self.cases.items():
            state = initial_state(case)
            payload = visible_payload(case, state)
            self.assertEqual(json.loads(json.dumps(payload)), payload)
            self.assertNotIn("id", payload)
            self.assertNotIn("family", payload)
            self.assertNotIn("evidence_pool", payload)
            self.keys[identifier]["secret_answer_canary"] = "HIDDEN_ANSWER_SENTINEL"
            self.assertNotIn("HIDDEN_ANSWER_SENTINEL", json.dumps(visible_payload(case, state)))
            self.assertNotIn("hidden_worlds", json.dumps(payload))
            initial_texts = {item["text"] for item in payload["evidence"]}
            self.assertFalse(initial_texts & {item["text"] for item in case["evidence_pool"]})
            for reverse in (False, True):
                paragraphs = render(case, state, "paragraph", reverse).split("\n\n")
                listed = [line[2:] for line in render(case, state, "list", reverse).splitlines()]
                self.assertEqual(paragraphs, listed)
                self.assertEqual(sorted(paragraphs),
                                 sorted(render(case, state, "paragraph").split("\n\n")))
            payload["candidates"][0]["summary"] = "changed copy"
            self.assertNotEqual(payload["candidates"], case["candidates"])

    def test_hidden_worlds_never_change_same_trace_assertion_or_action_key(self):
        for identifier in ("F4-other-event", "F5-cheap-check", "F5-costly-check"):
            case, rubric = self.cases[identifier], self.keys[identifier]
            self.assertEqual(rubric["hidden_worlds"], [False, True])
            state = initial_state(case)
            for action in (None, "INSPECT:d1"):
                if action:
                    state = apply_action(case, state, action)
                original = visible_payload(case, state)
                outcomes = []
                for world in (False, True):
                    revised_key = deepcopy(rubric)
                    revised_key["hidden_worlds"] = [world]
                    outcomes.append(assess_reviewed_properties(
                        case, revised_key, rubric["required_properties"],
                        "UNKNOWN_IN_SCOPE", rubric["accepted_next_actions"][0], ["e1"], state))
                    self.assertEqual(original, visible_payload(case, state))
                self.assertEqual(outcomes[0], outcomes[1])
                self.assertTrue(outcomes[0]["assertion_correct"])

    def test_later_capture_failure_does_not_erase_positive_presence(self):
        positive = self.assess("F4-matching-event", assertion="PRESENT_IN_SCOPE")
        self.assertTrue(positive["assertion_correct"])
        self.assertFalse(self.assess("F4-matching-event", assertion="UNKNOWN_IN_SCOPE")["assertion_correct"])
        self.assertFalse(self.assess("F4-other-event", assertion="PRESENT_IN_SCOPE")["assertion_correct"])

    def test_assertion_correctness_separate_from_supplied_action_value(self):
        wrong_next = self.assess("F5-cheap-check", next_action="defer_with_unknown")
        self.assertTrue(wrong_next["assertion_correct"])
        self.assertFalse(wrong_next["next_action_accepted"])
        self.assertTrue(self.assess("F5-costly-check", next_action="defer_with_unknown")["next_action_accepted"])
        self.assertEqual(optimal_authored_actions(self.cases["F5-cheap-check"]), {"request_complete_check"})
        delayed = deepcopy(self.cases["F5-cheap-check"])
        delayed["utility_assumptions"]["actions"]["request_complete_check"]["steps"] = 3
        self.assertEqual(optimal_authored_actions(delayed), {"defer_with_unknown"})
        self.assertIsNone(optimal_authored_actions(self.cases["F4-matching-event"]))

    def test_partial_context_and_unforeseen_implementation_are_not_automatic_failures(self):
        identifier = "F8-fixed-checkpoint"
        case = self.cases[identifier]
        self.assertEqual(self.assess(identifier, initial_state(case))["status"], "REQUIRES_PARTIAL_EVIDENCE_REVIEW")
        self.assertEqual(self.assess(identifier, properties=None)["status"], "REQUIRES_SEMANTIC_REVIEW")
        state = self.inspect_key_context(identifier)
        result = apply_action(case, state, "SELECT", response={"implementation": "An unforeseen digest-bound build recipe"})
        self.assertEqual(result["terminal_state"], "SELECT")
        self.assertTrue(self.assess(identifier, result)["constraint_satisfied"])
        unknown_action = self.assess(identifier, next_action=None)
        self.assertIsNone(unknown_action["next_action_accepted"])
        self.assertEqual(unknown_action["status"], "REQUIRES_ACTION_REVIEW")

    def test_citation_requires_actual_evidence_release(self):
        case = self.cases["F3-reversible"]
        state = initial_state(case)
        self.assertEqual(self.assess("F3-reversible", state, evidence_ids=["d1"])["status"], "UNSUPPORTED_CITATION")
        after = apply_action(case, state, "INSPECT:d1")
        self.assertTrue(self.assess("F3-reversible", after, evidence_ids=["e1", "d1"])["constraint_satisfied"])
        self.assertEqual(state["acquired_ids"], [])

    def test_duplicate_failed_rejected_and_overbudget_attempts_are_retained(self):
        case = self.cases["F1-verbatim"]
        state = initial_state(case)
        state = apply_action(case, state, "INSPECT:d1")
        state = apply_action(case, state, "INSPECT:d1")
        state = apply_action(case, state, "UNKNOWN_ACTION")
        state = apply_action(case, state, "INSPECT:d1")
        self.assertEqual([row["charged_units"] for row in state["history"]], [1, 1, 1, 0])
        self.assertEqual([row["status"] for row in state["history"]],
                         ["APPLIED", "DUPLICATE_INSPECTION", "REJECTED_UNKNOWN_ACTION", "REJECTED_BUDGET"])
        self.assertEqual(state["spent_units"], 3)
        self.assertEqual(state["terminal_state"], "STOP")
        self.assertEqual(state["acquired_ids"], ["d1"])
        with self.assertRaises(ValueError):
            apply_action(case, state, "STOP")

    def test_rejection_reopening_preserve_sources_and_expose_irreversibility(self):
        endings = {}
        for variant in ("reversible", "irreversible"):
            case = self.cases["F3-" + variant]
            state = apply_action(case, initial_state(case), "REJECT", ["c1"])
            state = apply_action(case, state, "INSPECT:d1")
            evidence_before = visible_payload(case, state)["evidence"]
            state = apply_action(case, state, "REOPEN", ["c1"])
            self.assertEqual(evidence_before, visible_payload(case, state)["evidence"])
            state = apply_action(case, state, "SELECT", ["c1"], response={"implementation": "c1 with Z2 settings"})
            endings[variant] = state
        self.assertEqual(endings["reversible"]["terminal_state"], "SELECT")
        self.assertIn("REJECTED_IRREVERSIBLE", [item["status"] for item in endings["irreversible"]["history"]])
        self.assertEqual(endings["irreversible"]["terminal_state"], "STOP")
        self.assertEqual(endings["irreversible"]["history"][-1]["status"], "REJECTED_BUDGET")

    def test_terminal_states_and_comparison_are_observable(self):
        case = self.cases["F1-verbatim"]
        for terminal in ("SELECT", "HOLD", "STOP"):
            state = apply_action(case, initial_state(case), "COMPARE", ["c1", "c2"])
            state = apply_action(case, state, terminal, ["c1"] if terminal == "SELECT" else (),
                                 response={"reason": "Authored terminal example"})
            self.assertEqual(state["terminal_state"], terminal)
            self.assertEqual(len(state["history"]), 2)
            self.assertEqual(state["spent_units"], 0)

    def test_timing_equivalence_over_all_four_candidate_truth_tables_and_orders(self):
        for bits in product((False, True), repeat=4):
            feasibility = dict(zip("abcd", bits))
            for order in permutations("abcd"):
                self.assertEqual(filter_independent(order, feasibility, False),
                                 filter_independent(order, feasibility, True))

    def test_complementarity_is_an_assumption_violation_not_a_timing_result(self):
        required = {"order_A", "bytes_A"}
        compatible = {"manifest": {"order_A"}, "blobs": {"bytes_A"}}
        independent_survivors = {item: props for item, props in compatible.items() if required <= props}
        self.assertEqual(independent_survivors, {})
        self.assertEqual(feasible_combinations(compatible, required), {frozenset({"manifest", "blobs"})})
        incompatible = {"manifest": {"order_A"}, "blobs": {"bytes_B"}}
        self.assertEqual(feasible_combinations(incompatible, required), set())

    def test_discriminating_acquisition_changes_visible_evidence_not_access(self):
        for family, variants in (("F6", ("idempotent", "non-idempotent")),
                                 ("F8", ("fixed-checkpoint", "drifting-input"))):
            first, second = [self.cases[family + "-" + item] for item in variants]
            first_initial, second_initial = initial_state(first), initial_state(second)
            self.assertEqual(visible_payload(first, first_initial), visible_payload(second, second_initial))
            detail = "d1" if family == "F6" else "d3"
            first_after = apply_action(first, first_initial, "INSPECT:" + detail)
            second_after = apply_action(second, second_initial, "INSPECT:" + detail)
            self.assertNotEqual(visible_payload(first, first_after)["evidence"],
                                visible_payload(second, second_after)["evidence"])
            self.assertEqual(first["action_set"], second["action_set"])

    def test_bad_keys_and_dangling_evidence_fail_mechanical_checks(self):
        bad = deepcopy(self.keys)
        bad["F5-cheap-check"]["accepted_next_actions"] = ["defer_with_unknown"]
        with self.assertRaisesRegex(ValueError, "utility"):
            validate_objects(self.cases, bad)
        bad_cases = deepcopy(self.cases)
        bad_cases["F1-verbatim"]["candidates"][0]["detail_evidence_ids"] = ["missing"]
        with self.assertRaisesRegex(ValueError, "dangling"):
            validate_objects(bad_cases, self.keys)


class AdvancementExamples(unittest.TestCase):
    """Hypothetical arithmetic rows, not simulated performance or chosen study values."""
    def setUp(self):
        self.thresholds = {"minimum_mean_gain": 0.1,
                           "maximum_cost_deltas": {"toy_units": 0, "review_minutes": 1}}
        rows = [{"acceptance_delta": 0.25, "domain": "d" + str(index % 3),
                 "regime": "r" + str(index % 4), "ambiguous": False,
                 "treatment_scope_errors": 0,
                 "error_increases": {name: 0 for name in HARM_CLASSES}}
                for index in range(12)]
        self.comparisons = {name: {"rows": deepcopy(rows),
                                  "cost_deltas": {"toy_units": 0, "review_minutes": 0}}
                            for name in ("ordinary", "purpose_mechanism")}

    def run_gate(self, comparisons=None, thresholds=None, valid=True):
        return advancement_rule(comparisons or self.comparisons,
                                self.thresholds if thresholds is None else thresholds,
                                instrument_valid=valid)

    def test_adversarial_outcome_table(self):
        scenarios = {}
        scenarios["all_guards_pass"] = (deepcopy(self.comparisons), "ELIGIBLE_FOR_DESIGN_REVIEW_ONLY")
        for name in ("two_wins_ten_losses", "only_ordinary_improves", "losing_domain",
                     "harm_despite_acceptance_gain", "new_scope_error_even_if_baseline_also_errs",
                     "explained_excess_cost", "ambiguous_key"):
            value = deepcopy(self.comparisons)
            rows = value["purpose_mechanism"]["rows"]
            expected = "DO_NOT_ADVANCE"
            if name == "two_wins_ten_losses":
                for index, row in enumerate(rows):
                    row["acceptance_delta"] = 0.25 if index < 2 else -0.5
            elif name == "only_ordinary_improves":
                for row in rows:
                    row["acceptance_delta"] = 0
            elif name == "losing_domain":
                for row in rows:
                    row["acceptance_delta"] = -0.1 if row["domain"] == "d0" else 0.5
            elif name == "harm_despite_acceptance_gain":
                rows[0]["error_increases"]["unsupported_presence"] = 1
            elif name == "new_scope_error_even_if_baseline_also_errs":
                rows[0]["treatment_scope_errors"] = 1
            elif name == "explained_excess_cost":
                value["purpose_mechanism"]["cost_deltas"]["toy_units"] = 1
            elif name == "ambiguous_key":
                rows[0]["ambiguous"] = True
                expected = "REDESIGN_INSTRUMENT"
            scenarios[name] = (value, expected)
        for name, (value, expected) in scenarios.items():
            with self.subTest(name=name):
                self.assertEqual(self.run_gate(value), expected)

    def test_unset_or_nonfinite_values_and_missing_accounts_do_not_advance(self):
        self.assertEqual(advancement_rule(self.comparisons, None, instrument_valid=True), "UNSET_VALUE_JUDGMENTS")
        for delta in (0, float("nan"), float("inf"), True):
            thresholds = deepcopy(self.thresholds)
            thresholds["minimum_mean_gain"] = delta
            self.assertEqual(self.run_gate(thresholds=thresholds), "UNSET_VALUE_JUDGMENTS")
        missing = deepcopy(self.comparisons)
        del missing["ordinary"]["rows"][0]["error_increases"]["false_absence"]
        self.assertEqual(self.run_gate(missing), "REDESIGN_INSTRUMENT")
        invalid_harm = deepcopy(self.comparisons)
        invalid_harm["ordinary"]["rows"][0]["error_increases"]["false_absence"] = float("nan")
        self.assertEqual(self.run_gate(invalid_harm), "REDESIGN_INSTRUMENT")
        self.assertEqual(self.run_gate(valid=False), "REDESIGN_INSTRUMENT")


if __name__ == "__main__":
    unittest.main()
