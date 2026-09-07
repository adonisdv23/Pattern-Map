from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import sys
import unittest
from pathlib import Path

from canonical import content_sha256, manifest_receipt, ordered_membership_sha256
from parity import solve_exact_parity, token_count, tokenizer_fingerprint
from parser import parse_output, raw_output_receipt
from planning import paired_bootstrap_interval, paired_exact_pvalue, run_power_surface, simulate_power_cell
from scoring import score_output


class CharacterTokenizer:
    """Deterministic tokenizer used only for exhaustive local fixtures."""

    def encode(self, text: str) -> list[int]:
        return [ord(char) for char in text]


class OvershootTokenizer:
    """Tiny BPE-like fixture where the first filler candidate is two tokens."""

    def encode(self, text: str) -> list[int]:
        tokens: list[int] = []
        index = 0
        while index < len(text):
            if text.startswith("· ", index):
                tokens.extend((9001, 9002))
                index += 2
            elif text[index] == " ":
                tokens.append(9003)
                index += 1
            else:
                tokens.append(ord(text[index]))
                index += 1
        return tokens


class TestCanonical(unittest.TestCase):
    def test_content_and_membership_hashes_are_independent(self) -> None:
        content = {"bundle_id": "B1", "reports": [{"text": "alpha"}]}
        receipt = manifest_receipt(content, ["B1", "B2"])
        self.assertNotEqual(receipt["content_sha256"], receipt["membership_sha256"])
        self.assertNotEqual(content_sha256(content), content_sha256({"bundle_id": "B1", "reports": [{"text": "beta"}]}))
        self.assertNotEqual(ordered_membership_sha256(["B1", "B2"]), ordered_membership_sha256(["B2", "B1"]))


class TestStrictParserAndScoring(unittest.TestCase):
    ids = ["R1", "R2", "R3"]
    reports = [
        {"report_id": "R1", "origin_id": "O1", "stance": "supports"},
        {"report_id": "R2", "origin_id": "O2", "stance": "supports"},
        {"report_id": "R3", "origin_id": "O3", "stance": "refutes"},
    ]
    gold = {
        "bundle_id": "B1",
        "gold_support_origin_certainty": "multiple",
        "gold_support_origin_count": 2,
        "support_origin_ids": ["O1", "O2"],
        "gold_claim_state": "supported",
    }

    def test_exhaustive_invalid_fixtures_are_not_repaired(self) -> None:
        valid = b'{"claim_state":"supported","confidence":0.5,"evidence_ids":["R1"],"origin_count_supporting":1}'
        fixtures = {
            "valid": (valid, True, "NONE"),
            "duplicate": (b'{"claim_state":"supported","confidence":0.5,"evidence_ids":[],"origin_count_supporting":1,"origin_count_supporting":2}', False, "DUPLICATE_KEY"),
            "fenced": (b"```json\n" + valid + b"\n```", False, "INVALID_JSON"),
            "unknown_key": (valid[:-1] + b',"extra":1}', False, "SCHEMA_ERROR"),
            "unknown_id": (b'{"claim_state":"supported","confidence":0.5,"evidence_ids":["RX"],"origin_count_supporting":1}', False, "UNKNOWN_EVIDENCE_ID"),
            "bad_count": (b'{"claim_state":"supported","confidence":0.5,"evidence_ids":[],"origin_count_supporting":true}', False, "SCHEMA_ERROR"),
            "empty": (b"", False, "EMPTY_OUTPUT"),
            "utf8": (b"\xff", False, "INVALID_UTF8"),
        }
        for name, (raw, expected_valid, expected_code) in fixtures.items():
            with self.subTest(name=name):
                result = parse_output(raw, self.ids)
                self.assertEqual(result.valid, expected_valid)
                self.assertEqual(result.error_code, expected_code)
                receipt = raw_output_receipt(raw, result)
                self.assertFalse(receipt["repair_applied"])
                self.assertFalse(receipt["retry_applied"])

    def test_fc_cons_and_vor_keep_distinct_denominators(self) -> None:
        raw = b'{"claim_state":"supported","confidence":0.5,"evidence_ids":["R1","R2"],"origin_count_supporting":2}'
        result = parse_output(raw, self.ids)
        score = score_output(result, self.gold, self.reports, {"B1"})
        self.assertEqual(score["fc_cons"], 0)
        self.assertEqual(score["fc_cons_invalid_only"], 0)
        self.assertEqual(score["vor"], 1)
        self.assertEqual(score["selected_support_origin_count"], 2)

        unknown = dict(self.gold, bundle_id="B2", gold_support_origin_certainty="unknown")
        unknown_score = score_output(result, unknown, self.reports, {"B1"})
        self.assertEqual(unknown_score["fc_cons"], 1)
        self.assertEqual(unknown_score["vor"], 0)


class TestParity(unittest.TestCase):
    def test_exhaustive_small_fixture_set_reaches_exact_parity(self) -> None:
        tokenizer = CharacterTokenizer()
        fixtures = [(f"F1-{i}", f"F2-{i} x") for i in range(25)]
        for f1, f2 in fixtures:
            solution = solve_exact_parity(
                f1,
                f2,
                tokenizer,
                candidates=(" ", "x"),
                max_segments=3,
                max_padding_tokens=8,
            )
            self.assertEqual(token_count(tokenizer, f1 + solution.f1_padding), solution.f1_tokens)
            self.assertEqual(token_count(tokenizer, f2 + solution.f2_padding), solution.f2_tokens)
            self.assertEqual(solution.f1_tokens, solution.f2_tokens)

    def test_content_or_order_mismatch_fails_closed(self) -> None:
        with self.assertRaises(ValueError):
            solve_exact_parity("a", "b", CharacterTokenizer(), report_hash_f1="a", report_hash_f2="b")
        with self.assertRaises(ValueError):
            solve_exact_parity("a", "a", CharacterTokenizer(), ordered_report_ids_f1=["R1"], ordered_report_ids_f2=["R2"])

    def test_overshoot_fixture_tries_another_exact_candidate(self) -> None:
        solution = solve_exact_parity(
            "base",
            "baseX",
            OvershootTokenizer(),
            candidates=("· ", " "),
            max_segments=3,
            max_padding_tokens=4,
        )
        self.assertEqual(solution.f1_tokens, solution.f2_tokens)
        self.assertEqual(solution.f1_padding, " ")

    @unittest.skipUnless(importlib.util.find_spec("tiktoken"), "optional tiktoken dependency is not installed")
    def test_real_bpe_claude_primary_fixture_300_pairs(self) -> None:
        import tiktoken

        tokenizer = tiktoken.get_encoding("cl100k_base")
        fixture = Path(__file__).resolve().parents[1] / "fixtures" / "CLAUDE_PRIMARY_RENDER_AUDIT_SEED1_N300.json"
        manifest = json.loads(fixture.read_text(encoding="utf-8"))
        self.assertEqual(manifest["schema"], "EP-v1.1-advisory-render-audit-0.1")
        self.assertEqual(manifest["status"], "offline_fixture_not_research_result")
        self.assertEqual(manifest["source"]["archive_sha256"], "b544b734324699a93abbb8cf0bcef3d61cc590ff7b603fc167a46b8f8539a253")
        self.assertEqual(manifest["source"]["generator_sha256"], "ac7917d314e897159baa7b98c5f0adc1276feba817463dc47499169ea50595fb")
        self.assertEqual(manifest["source"]["conditions_sha256"], "f7db90c7094cdb212b25d7fc124d20189f6466e08b543f4b0f989ff608fbb417")
        self.assertEqual(manifest["tokenizer"]["version"], "0.14.0")
        self.assertEqual(manifest["tokenizer"]["encoding"], "cl100k_base")
        self.assertEqual(tokenizer_fingerprint(tokenizer), "5af8a02a651e9db4366b5b14c2cc8f506d721ebdab0db3294337dd8ba15c4528")
        self.assertEqual(manifest["audit"]["seed"], 1)
        self.assertEqual(manifest["audit"]["n"], 300)
        self.assertEqual(manifest["audit"]["pair_count"], 300)
        self.assertEqual(manifest["audit"]["external_parent_audit_receipt_sha256"], "6d1fb03ec419511ce7aef652f85d3713030f958edb2e152bf08db2958f86fb68")
        expected_deltas = [-7, -6, -5, -4, -3, -1, 0, 1, 3, 4, 5, 6, 7, 8]
        self.assertEqual(manifest["audit"]["base_delta_f2_minus_f1"], expected_deltas)
        pairs = manifest["pairs"]
        self.assertEqual(len(pairs), 300)
        self.assertEqual([pair["bundle_id"] for pair in pairs], [f"b{index:04d}" for index in range(300)])
        receipt_fields = []
        observed_deltas = set()
        padded_counts = []
        for pair in pairs:
            f1 = str(pair["f1_text"])
            f2 = str(pair["f2_text"])
            self.assertEqual(hashlib.sha256(f1.encode("utf-8")).hexdigest(), pair["f1_render_sha256"])
            self.assertEqual(hashlib.sha256(f2.encode("utf-8")).hexdigest(), pair["f2_render_sha256"])
            self.assertEqual(token_count(tokenizer, f1), pair["f1_base_tokens"])
            self.assertEqual(token_count(tokenizer, f2), pair["f2_base_tokens"])
            observed_deltas.add(int(pair["base_delta_f2_minus_f1"]))
            self.assertEqual(pair["f2_base_tokens"] - pair["f1_base_tokens"], pair["base_delta_f2_minus_f1"])
            self.assertEqual(pair["f1_report_id_order"], pair["f2_report_id_order"])
            self.assertEqual(pair["f1_report_text_hash_sequence"], pair["f2_report_text_hash_sequence"])
            self.assertEqual(len(pair["f1_report_id_order"]), len(pair["f1_report_text_hash_sequence"]))
            self.assertEqual(
                hashlib.sha256(json.dumps(pair["f1_report_text_hash_sequence"], sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest(),
                pair["f1_report_text_hash_sequence_sha256"],
            )
            self.assertEqual(pair["f1_report_text_hash_sequence_sha256"], pair["f2_report_text_hash_sequence_sha256"])
            solution = solve_exact_parity(
                f1,
                f2,
                tokenizer,
                report_hash_f1=pair["f1_report_text_hash_sequence_sha256"],
                report_hash_f2=pair["f2_report_text_hash_sequence_sha256"],
                ordered_report_ids_f1=pair["f1_report_id_order"],
                ordered_report_ids_f2=pair["f2_report_id_order"],
            )
            self.assertEqual(solution.f1_tokens, solution.f2_tokens)
            padded_counts.append(solution.f1_tokens)
            receipt_fields.append({key: pair[key] for key in (
                "bundle_id", "f1_report_id_order", "f2_report_id_order",
                "f1_report_text_hash_sequence", "f2_report_text_hash_sequence",
                "f1_report_text_hash_sequence_sha256", "f2_report_text_hash_sequence_sha256",
                "f1_render_sha256", "f2_render_sha256",
                "f1_base_tokens", "f2_base_tokens", "base_delta_f2_minus_f1"
            )})
        receipt = hashlib.sha256(json.dumps(receipt_fields, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
        self.assertEqual(receipt, manifest["render_receipt_sha256"])
        self.assertEqual(sorted(observed_deltas), expected_deltas)
        self.assertEqual(min(padded_counts), 292)
        self.assertEqual(max(padded_counts), 486)
        self.assertEqual(tokenizer_fingerprint(tokenizer), "5af8a02a651e9db4366b5b14c2cc8f506d721ebdab0db3294337dd8ba15c4528")


class TestPlanning(unittest.TestCase):
    def test_exact_paired_logic(self) -> None:
        self.assertEqual(paired_exact_pvalue([0, 0, 0], [0, 0, 0]), 1.0)
        self.assertLess(paired_exact_pvalue([1] * 20, [0] * 20), 0.001)

    def test_exact_paired_logic_is_bounded_and_stable(self) -> None:
        p_100 = paired_exact_pvalue([1] * 100, [0] * 100)
        self.assertGreater(p_100, 0.0)
        self.assertLessEqual(p_100, 1.0)
        self.assertAlmostEqual(p_100, 2.0 ** (1 - 100), places=40)
        for n in (400, 2000):
            with self.subTest(n=n):
                p_value = paired_exact_pvalue([1] * n, [0] * n)
                self.assertGreaterEqual(p_value, 0.0)
                self.assertLessEqual(p_value, 1.0)
        self.assertEqual(paired_exact_pvalue([0] * 400, [0] * 400), 1.0)

    def test_bootstrap_rejects_unpaired_or_empty_inputs(self) -> None:
        with self.assertRaises(ValueError):
            paired_bootstrap_interval([0, 1], [0], 10, 1)
        with self.assertRaises(ValueError):
            paired_bootstrap_interval([], [], 10, 1)

    def test_planning_is_deterministic_and_explicitly_nonempirical(self) -> None:
        one = simulate_power_cell(0.30, 0.20, -0.08, 40, 50, 7)
        two = simulate_power_cell(0.30, 0.20, -0.08, 40, 50, 7)
        self.assertEqual(one, two)
        self.assertEqual(one["status"], "planning_only_no_model_or_corpus_outputs")
        surface = run_power_surface(
            baselines=(0.30,),
            discordances=(0.10, 0.20, 0.30),
            deltas=(-0.08,),
            sample_sizes=(300, 400),
            invalidity_pairs=((0.0, 0.0), (0.02, 0.05)),
            repetitions=20,
        )
        self.assertEqual(len(surface["cells"]), 12)
        self.assertEqual(surface["grid"]["invalidity_pairs_f1_f2"], [[0.0, 0.0], [0.02, 0.05]])
        self.assertEqual(
            {(cell["invalid_f1"], cell["invalid_f2"]) for cell in surface["cells"]},
            {(0.0, 0.0), (0.02, 0.05)},
        )
        self.assertEqual(surface["status"], "planning_only_no_model_or_corpus_outputs")


class TestNoProviderPath(unittest.TestCase):
    def test_harness_has_no_provider_or_network_imports(self) -> None:
        forbidden = {"requests", "urllib", "httpx", "openai", "anthropic", "boto3", "google"}
        root = Path(__file__).parent
        for path in root.glob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    names = {alias.name.split(".")[0] for alias in node.names}
                    self.assertTrue(names.isdisjoint(forbidden), path)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    self.assertNotIn(node.module.split(".")[0], forbidden, path)


if __name__ == "__main__":
    unittest.main()
