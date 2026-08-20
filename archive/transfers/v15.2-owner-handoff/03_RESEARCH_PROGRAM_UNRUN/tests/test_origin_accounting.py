"""Focused offline tests for the F0/F1/F2 readiness scaffold."""

from __future__ import annotations

import hashlib
import json
import copy
import tempfile
from pathlib import Path
import unittest
from typing import Dict

from tools.origin_accounting.analysis import paired_analysis, paired_exact_pvalue, score_output
from tools.origin_accounting.canonical import canonical_json_bytes
from tools.origin_accounting.cli import run_generate
from tools.origin_accounting.config import FrozenConfig, assert_config_invariants, frozen_config_sha256, frozen_config_path
from tools.origin_accounting.diagnostics import (
    field_only_diagnostic,
    metadata_only_counter,
    relation_noise_fixture,
    split_leakage_report,
)
from tools.origin_accounting.generator import (
    build_primary_manifest,
    build_prompt_instances,
    generate_corpus,
    validate_corpus,
    validate_prompt_parity,
)
from tools.origin_accounting.parser import (
    parse_output,
    parser_fixture_cases,
    raw_output_record,
    validate_raw_output_record,
    validate_run_record,
)
from tools.origin_accounting.power import _paired_probabilities, run_power_simulation, simulate_fc_cell


class OriginAccountingReadinessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = FrozenConfig()
        assert_config_invariants(self.config)

    def test_small_corpus_is_deterministic_and_split_blocked(self) -> None:
        first = generate_corpus(self.config, small=True)
        second = generate_corpus(self.config, small=True)
        self.assertEqual(first.propositions, second.propositions)
        self.assertEqual(first.reports, second.reports)
        self.assertEqual(first.bundles_gold, second.bundles_gold)
        leakage = split_leakage_report(first)
        self.assertEqual(leakage["status"], "precheck_pass")
        self.assertEqual(leakage["clearance_status"], "unresolved")
        self.assertFalse(leakage["authoritative"])
        self.assertEqual(len(first.bundles_public), 16)
        self.assertEqual(
            {gold["origin_structure"] for gold in first.bundles_gold},
            set(self.config.structures),
        )

    def test_graph_and_unknown_origin_invariants(self) -> None:
        corpus = generate_corpus(self.config, small=True)
        graphs = {graph["provenance_graph_id"]: graph for graph in corpus.provenance_graphs}
        for graph in graphs.values():
            node_ids = [node["node_id"] for node in graph["nodes"]]
            self.assertEqual(len(node_ids), len(set(node_ids)))
            node_set = set(node_ids)
            for edge in graph["edges"]:
                self.assertIn(edge["from"], node_set)
                self.assertIn(edge["to"], node_set)
        unknown = next(gold for gold in corpus.bundles_gold if gold["origin_structure"] == "unknown_origin")
        self.assertIsNone(unknown["gold_support_origin_count"])
        self.assertEqual(unknown["gold_support_origin_certainty"], "unknown")
        self.assertTrue(unknown["required_unknown_preservation"])
        unknown_codes = {
            prompt["condition"]: prompt["relation_codes"]
            for prompt in build_prompt_instances(corpus, self.config)
            if prompt["bundle_id"] == unknown["bundle_id"]
        }["F2"]
        self.assertEqual(set(unknown_codes.values()), {"UNKN"})

        multiple = next(gold for gold in corpus.bundles_gold if gold["origin_structure"] == "multiple_origin_convergence")
        multiple_codes = {
            prompt["condition"]: prompt["relation_codes"]
            for prompt in build_prompt_instances(corpus, self.config)
            if prompt["bundle_id"] == multiple["bundle_id"]
        }["F2"]
        self.assertEqual(
            sum(multiple_codes[rid] == "INDP" for rid in multiple["supporting_report_ids"]),
            multiple["gold_support_origin_count"],
        )
        # Refuting reports must not be laundered into supporting-origin recall.
        self.assertEqual(
            sum(multiple_codes[rid] == "INDP" for rid in multiple["refuting_report_ids"]),
            0,
        )
        conflict = next(gold for gold in corpus.bundles_gold if gold["origin_structure"] == "conflict")
        conflict_codes = {
            prompt["condition"]: prompt["relation_codes"]
            for prompt in build_prompt_instances(corpus, self.config)
            if prompt["bundle_id"] == conflict["bundle_id"]
        }["F2"]
        self.assertEqual(
            sum(conflict_codes[rid] == "INDP" for rid in conflict["supporting_report_ids"]),
            0,
        )
        self.assertEqual(
            sum(conflict_codes[rid] == "INDP" for rid in conflict["refuting_report_ids"]),
            1,
        )

    def test_full_unknown_origin_stress_preserves_all_visible_unknown_codes(self) -> None:
        corpus = generate_corpus(self.config, small=False)
        prompts = build_prompt_instances(corpus, self.config)
        gold_by_bundle = {record["bundle_id"]: record for record in corpus.bundles_gold}
        for prompt in prompts:
            gold = gold_by_bundle[prompt["bundle_id"]]
            if prompt["condition"] == "F2" and gold["origin_structure"] == "unknown_origin":
                self.assertEqual(set(prompt["relation_codes"].values()), {"UNKN"})

    def test_prompt_has_exact_per_bundle_token_and_byte_parity(self) -> None:
        corpus = generate_corpus(self.config, small=True)
        prompts = build_prompt_instances(corpus, self.config)
        by_bundle: Dict[str, Dict[str, dict]] = {}
        for prompt in prompts:
            by_bundle.setdefault(prompt["bundle_id"], {})[prompt["condition"]] = prompt
        self.assertEqual(len(by_bundle), 16)
        for conditions in by_bundle.values():
            self.assertEqual(
                len({conditions[c]["input_token_count"] for c in ("F0", "F1", "F2")}),
                1,
            )
            self.assertEqual(
                len({conditions[c]["input_byte_count"] for c in ("F0", "F1", "F2")}),
                1,
            )
            self.assertNotEqual(conditions["F1"]["user_sha256"], conditions["F2"]["user_sha256"])
            self.assertEqual(conditions["F1"]["report_text_sha256s"], conditions["F2"]["report_text_sha256s"])
            self.assertTrue(conditions["F1"]["tokenizer_is_surrogate"])

    def test_prompt_parity_recomputes_mutated_payload_and_instruction(self) -> None:
        corpus = generate_corpus(self.config, small=True)
        prompts = build_prompt_instances(corpus, self.config)
        for field in ("system_text", "user_text"):
            mutated = copy.deepcopy(prompts)
            next(prompt for prompt in mutated if prompt["condition"] == "F2")[field] += " MUTATION"
            with self.assertRaises(ValueError):
                validate_prompt_parity(mutated, corpus=corpus)
        mutated = copy.deepcopy(prompts)
        target = next(prompt for prompt in mutated if prompt["condition"] == "F2")
        target["instruction_text"] += " MUTATION"
        target["instruction_sha256"] = hashlib.sha256(target["instruction_text"].encode("utf-8")).hexdigest()
        with self.assertRaises(ValueError):
            validate_prompt_parity(mutated, corpus=corpus)

    def test_corpus_validator_rejects_hash_and_cross_record_tampering(self) -> None:
        corpus = generate_corpus(self.config, small=True)
        mutations = []
        tampered = copy.deepcopy(corpus)
        tampered.reports[0]["text"] += " TAMPER"
        mutations.append(tampered)
        tampered = copy.deepcopy(corpus)
        tampered.reports[0]["proposition_family_id"] = "PF-AAAAAAAAAA"
        mutations.append(tampered)
        tampered = copy.deepcopy(corpus)
        tampered.reports[0]["stance"] = "refutes"
        tampered.reports[0]["origin_id"] = "OR-AAAAAAAAAA"
        mutations.append(tampered)
        tampered = copy.deepcopy(corpus)
        report_id = tampered.bundles_public[0]["report_ids"][0]
        tampered.bundles_gold[0]["relation_by_report_id"][report_id] = "dependent"
        mutations.append(tampered)
        for tampered in mutations:
            with self.assertRaises(ValueError):
                validate_corpus(tampered, self.config)

    def test_parser_is_strict_and_preserves_raw_receipt(self) -> None:
        expected_ids = {"RP-BBBBBBBBBB", "RP-CCCCCCCCCC"}
        for name, raw, expected_status, expected_code in parser_fixture_cases():
            result = parse_output(raw, expected_ids)
            self.assertEqual(result.parse_status, expected_status, name)
            self.assertEqual(result.error_code, expected_code, name)
            if name == "valid":
                receipt = raw_output_record("RN-AAAAAAAAAA", raw, result)
                validate_raw_output_record(receipt)
                self.assertEqual(receipt["byte_length"], len(raw))
                self.assertEqual(
                    receipt["raw_output_sha256"], hashlib.sha256(raw).hexdigest()
                )
                self.assertEqual(result.parsed["origin_count_supporting"], 1)
                with self.assertRaises(ValueError):
                    raw_output_record("RN-AAAAAAAAAA", b"other", result)
        validate_run_record(
            {
                "run_id": "RN-AAAAAAAAAA",
                "prompt_instance_id": "PI-AAAAAAAAAA",
                "bundle_id": "BD-AAAAAAAAAA",
                "condition": "F2",
                "model_id": "UNSELECTED",
                "model_revision": None,
                "tokenizer_revision": None,
                "decoder": {"temperature": 0},
                "chat_template": "unselected",
                "runtime": {"python": "3.12"},
                "dependency_hashes": {},
                "hardware": {"class": "offline"},
                "seed": 7,
                "started_at_utc": "2040-01-01T00:00:00Z",
                "status": "completed",
                "input_tokens": 10,
                "input_byte_length": 20,
                "output_tokens": 5,
                "latency_ms": 1.0,
                "cpu_ms": 1.0,
                "gpu_ms": None,
                "peak_memory_mb": 1.0,
                "system_prompt_sha256": "0" * 64,
                "user_prompt_sha256": "1" * 64,
                "final_input_sha256": "2" * 64,
                "raw_output_sha256": "3" * 64,
                "error_code": "NONE",
            }
        )

    def test_all_assigned_false_corroboration_and_fixed_vor_set(self) -> None:
        corpus = generate_corpus(self.config, small=True)
        by_bundle = corpus.by_bundle()
        scores = {"F1": {}, "F2": {}}
        for bundle_id, bundle in by_bundle.items():
            reports = bundle["reports"]
            ids = [report["report_id"] for report in reports]
            valid_raw = json.dumps(
                {
                    "origin_count_supporting": 1,
                    "claim_state": bundle["gold"]["gold_claim_state"],
                    "confidence": 0.5,
                    "evidence_ids": ids[:2],
                },
                separators=(",", ":"),
            ).encode("utf-8")
            invalid = parse_output(b"not-json", ids)
            valid = parse_output(valid_raw, ids)
            scores["F1"][bundle_id] = score_output(valid, bundle["gold"], reports)
            scores["F2"][bundle_id] = score_output(invalid, bundle["gold"], reports)
        gold = {bundle_id: bundle["gold"] for bundle_id, bundle in by_bundle.items()}
        with self.assertRaises(ValueError):
            paired_analysis(scores, gold, self.config, bootstrap_repetitions=50)
        result = paired_analysis(
            scores,
            gold,
            self.config,
            bootstrap_repetitions=50,
            analysis_mode="descriptive_smoke",
        )
        self.assertEqual(result["analysis_mode"], "descriptive_smoke")
        self.assertEqual(result["primary_n"], 16)
        self.assertTrue(result["invalid_outputs_in_primary_denominator"])
        self.assertEqual(result["fixed_safety_set_M"]["n"], 4)
        self.assertTrue(result["fixed_safety_set_M"]["invalid_outputs_coded_as_zero"])
        self.assertIn("secondary_descriptive", result)
        self.assertIn(
            "absolute_origin_count_error",
            result["secondary_descriptive"]["metrics"],
        )
        self.assertIn(
            "valid_certified_conflict",
            result["secondary_descriptive"]["scope_summaries"],
        )

    def test_secondary_metrics_score_support_origins_without_penalizing_neutral_evidence(self) -> None:
        corpus = generate_corpus(self.config, small=True)
        bundle = next(
            item
            for item in corpus.by_bundle().values()
            if item["gold"]["origin_structure"] == "multiple_origin_convergence"
        )
        gold = bundle["gold"]
        reports = bundle["reports"]
        report_ids = [report["report_id"] for report in reports]
        supporting_ids = list(gold["supporting_report_ids"])
        neutral_id = next(
            report["report_id"] for report in reports if report["stance"] == "neutral"
        )

        # The emitted count is correct (three), but the selected evidence
        # contains only one supporting origin plus a neutral report. The
        # neutral report is legitimate assessment evidence and must not be
        # interpreted as support credit or a wrong-origin assignment.
        neutral_selection_raw = json.dumps(
            {
                "origin_count_supporting": 3,
                "claim_state": gold["gold_claim_state"],
                "confidence": 0.5,
                "evidence_ids": [supporting_ids[0], neutral_id],
            },
            separators=(",", ":"),
        ).encode("utf-8")
        scored = score_output(
            parse_output(neutral_selection_raw, report_ids),
            gold,
            reports,
        )
        self.assertEqual(scored["absolute_origin_count_error"], 0)
        self.assertEqual(scored["support_origin_set_precision"], 1.0)
        self.assertAlmostEqual(scored["support_origin_set_recall"], 1.0 / 3.0)
        self.assertEqual(scored["support_origin_set_exact_match"], 0)
        self.assertEqual(len(scored["selected_support_origin_ids"]), 1)
        self.assertNotIn("evidence_id_precision", scored)
        self.assertNotIn("support_origin_false_credit_count", scored)
        self.assertNotIn("support_origin_misassignment", scored)
        self.assertEqual(
            scored["secondary_metrics_scope"],
            "valid_certified_non_conflict",
        )

        invalid = score_output(parse_output(b"not-json", report_ids), gold, reports)
        self.assertFalse(invalid["secondary_metrics_defined"])
        self.assertIsNone(invalid["absolute_origin_count_error"])
        self.assertIsNone(invalid["support_origin_set_precision"])

    def test_secondary_origin_metrics_exclude_unknown_and_conflict_cases(self) -> None:
        corpus = generate_corpus(self.config, small=True)
        by_structure = {
            item["gold"]["origin_structure"]: item
            for item in corpus.by_bundle().values()
        }
        for structure in ("unknown_origin", "conflict"):
            bundle = by_structure[structure]
            gold = bundle["gold"]
            reports = bundle["reports"]
            report_ids = [report["report_id"] for report in reports]
            raw = json.dumps(
                {
                    "origin_count_supporting": 1,
                    "claim_state": gold["gold_claim_state"],
                    "confidence": 0.5,
                    "evidence_ids": report_ids[:1],
                },
                separators=(",", ":"),
            ).encode("utf-8")
            scored = score_output(parse_output(raw, report_ids), gold, reports)
            metric = (
                scored["absolute_origin_count_error"]
                if structure == "unknown_origin"
                else scored["support_origin_set_precision"]
            )
            self.assertIsNone(metric)
            if structure == "conflict":
                self.assertEqual(
                    scored["secondary_metrics_scope"],
                    "valid_certified_conflict",
                )
                self.assertIsNone(scored["support_origin_set_precision"])
                self.assertEqual(
                    scored["secondary_metrics_exclusion"],
                    "contested_claim_support_set_not_scored",
                )
            else:
                self.assertEqual(
                    scored["secondary_metrics_scope"],
                    "valid_unknown_or_uncertified",
                )
                self.assertEqual(
                    scored["secondary_metrics_exclusion"],
                    "unknown_or_uncertified_support_origins",
                )

    def test_empty_selected_support_origin_precision_is_undefined(self) -> None:
        reports = [
            {
                "report_id": "RP-AAAAAAAAAA",
                "origin_id": "OR-AAAAAAAAAA",
                "stance": "neutral",
            },
            {
                "report_id": "RP-BBBBBBBBBB",
                "origin_id": "OR-BBBBBBBBBB",
                "stance": "supports",
            },
        ]
        none_gold = {
            "gold_support_origin_certainty": "none",
            "gold_support_origin_count": 0,
            "support_origin_ids": [],
            "gold_claim_state": "supported",
            "supporting_report_ids": [],
        }
        empty_raw = b'{"origin_count_supporting":0,"claim_state":"supported","confidence":0.5,"evidence_ids":[]}'
        empty_scored = score_output(
            parse_output(empty_raw, {report["report_id"] for report in reports}),
            none_gold,
            reports,
        )
        self.assertIsNone(empty_scored["support_origin_set_precision"])
        self.assertIsNone(empty_scored["support_origin_set_recall"])
        self.assertEqual(empty_scored["support_origin_set_exact_match"], 1)

        one_gold = {
            "gold_support_origin_certainty": "single",
            "gold_support_origin_count": 1,
            "support_origin_ids": ["OR-BBBBBBBBBB"],
            "gold_claim_state": "supported",
            "supporting_report_ids": ["RP-BBBBBBBBBB"],
        }
        neutral_raw = b'{"origin_count_supporting":1,"claim_state":"supported","confidence":0.5,"evidence_ids":["RP-AAAAAAAAAA"]}'
        neutral_scored = score_output(
            parse_output(neutral_raw, {report["report_id"] for report in reports}),
            one_gold,
            reports,
        )
        self.assertIsNone(neutral_scored["support_origin_set_precision"])
        self.assertEqual(neutral_scored["support_origin_set_recall"], 0.0)
        self.assertEqual(neutral_scored["support_origin_set_exact_match"], 0)

    def test_confirmatory_analysis_requires_ordered_300_75_manifest(self) -> None:
        corpus = generate_corpus(self.config, small=False)
        manifest = build_primary_manifest(corpus, self.config)
        gold = {record["bundle_id"]: record for record in corpus.bundles_gold}
        scores = {
            condition: {
                bundle_id: {"fc_cons": 0, "valid": 1, "vor": 0}
                for bundle_id in manifest["primary_bundle_ids"]
            }
            for condition in ("F1", "F2")
        }
        result = paired_analysis(scores, gold, self.config, bootstrap_repetitions=5, manifest=manifest)
        self.assertEqual(result["analysis_mode"], "confirmatory")
        self.assertEqual(result["primary_n"], 300)
        self.assertEqual(result["fixed_safety_set_M"]["n"], 75)
        broken = copy.deepcopy(manifest)
        broken["primary_bundle_ids"] = broken["primary_bundle_ids"][:-1]
        with self.assertRaises(ValueError):
            paired_analysis(scores, gold, self.config, bootstrap_repetitions=5, manifest=broken)

    def test_shortcut_noise_and_power_scaffolds_are_descriptive(self) -> None:
        metadata = metadata_only_counter(["DPND", "INDP", "INDP", "INDP", "UNKN"])
        self.assertEqual(metadata["independent_as_stipulated_code_count"], 3)
        self.assertEqual(metadata["independent_code_present"], True)
        field = field_only_diagnostic(["DPND", "INDP", "UNKN"])
        self.assertFalse(field["model_run"])
        noise = relation_noise_fixture(self.config)
        self.assertTrue(noise["gold_untouched"])
        self.assertTrue(noise["unknown_preserved_in_base"])
        null = simulate_fc_cell(0.30, 0.20, 0.00, 20, 30, 7)
        self.assertEqual(null["repetitions"], 30)
        self.assertIn("power_or_type_i_error", null)
        self.assertIn("bootstrap_coverage", null)
        p00, p01, p10, p11 = _paired_probabilities(0.30, 0.20, -0.08)
        self.assertAlmostEqual(p10 + p11, 0.30)
        self.assertAlmostEqual((p01 + p11) - (p10 + p11), -0.08)
        power = run_power_simulation(
            self.config,
            repetitions=1,
            n_values=(10,),
            bootstrap_repetitions=5,
            vor_n_values=(10,),
            vor_bootstrap_repetitions=5,
        )
        self.assertTrue(power["cells"])
        self.assertTrue(power["vor_cells"])
        self.assertEqual(power["vor_grid"]["expected_protocol_n_fixed_M"], 75)
        self.assertIn("primary_decision_rate", power["cells"][0])
        self.assertIn("gate_probability", power["vor_cells"][0])
        self.assertIn("coverage_probability", power["vor_cells"][0])

    def test_cli_consumes_hashed_frozen_config_file(self) -> None:
        source = frozen_config_path()
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "frozen_config.json"
            payload = json.loads(source.read_text(encoding="utf-8"))
            payload["master_seed"] = "OA-test-config-consumption-seed"
            config_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
            receipt = run_generate(Path(temp_dir) / "out", small=True, config_path=config_path)
            self.assertEqual(receipt["config_file_sha256"], frozen_config_sha256(config_path))
            self.assertNotEqual(receipt["config_file_sha256"], frozen_config_sha256(source))

    def test_canonical_local_hash_rejects_nonfinite_numbers(self) -> None:
        with self.assertRaises(ValueError):
            canonical_json_bytes({"bad": float("nan")})
        self.assertEqual(canonical_json_bytes({"b": 1, "a": 2}), b'{"a":2,"b":1}')
        self.assertAlmostEqual(paired_exact_pvalue([1, 0, 0, 1], [0, 0, 1, 1]), 1.0)


if __name__ == "__main__":
    unittest.main()
