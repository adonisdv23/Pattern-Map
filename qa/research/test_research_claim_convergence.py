#!/usr/bin/env python3
"""Focused regression tests for the 2026 research-claim convergence."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def normalized(text: str) -> str:
    return " ".join(text.lower().split())


class ResearchClaimConvergenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.route = read("manuscript/SOURCES_AND_RESEARCH_ROUTE.md")
        cls.ledger = read("docs/CLAIMS_AND_SOURCE_LEDGER_V16.md")
        cls.agenda = read("research/THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md")
        cls.memo = read(
            "research/future-studies/DL_NARROW_WEDGE_DECISION_MEMO_V0_1.md"
        )
        cls.source_qa = read(
            "qa/research/CURRENT_ADJACENT_SOURCE_VERIFICATION_2026-08-30.md"
        )

    def test_before_generation_is_logical_and_iterative(self) -> None:
        for name, text in (
            ("route", self.route),
            ("ledger", self.ledger),
            ("agenda", self.agenda),
            ("memo", self.memo),
        ):
            value = normalized(text)
            self.assertIn("logical responsibility boundary", value, name)
            self.assertIn("iterative", value, name)
            self.assertRegex(value, r"first (?:model call|token)", name)

    def test_contribution_ceiling_is_complete(self) -> None:
        ceiling = (
            "authored, proportional, human-governed design/governance "
            "synthesis and testable agenda"
        )
        for name, text in (
            ("route", self.route),
            ("ledger", self.ledger),
            ("agenda", self.agenda),
            ("memo", self.memo),
        ):
            value = normalized(text)
            self.assertIn(ceiling, value, name)
            for excluded in (
                "novel mechanism",
                "exhaustive taxonomy",
                "validated method",
                "effectiveness result",
                "universal architecture",
            ):
                self.assertIn(excluded, value, f"{name}: {excluded}")

    def test_candidate_a_is_interface_not_trace_mechanism(self) -> None:
        value = normalized(self.memo)
        for phrase in (
            "candidate a — provisional appropriate-reliance interface",
            "candidate a is **fixed-answer only**",
            "existing applied receipt is a stimulus, not a proposed new trace or receipt mechanism",
            "generated-answer or decision accuracy is not an eligible outcome",
            "appropriate acceptance",
            "false acceptance",
            "unnecessary correction",
            "reviewer burden",
        ):
            self.assertIn(phrase, value)
        self.assertNotIn("candidate a — claim-scoped influence receipt", value)
        self.assertNotIn("generation-study primary candidates", value)

    def test_candidate_b_remains_provisional_and_unselected(self) -> None:
        value = normalized(self.memo)
        self.assertIn("candidate b — provisional", value)
        self.assertIn("no sequencing recommendation between a and b", value)
        self.assertIn("candidate b is not a settled missingness taxonomy", value)
        self.assertNotIn("specify candidate b first", value)
        for axis in (
            "**observation:**",
            "**process/capture:**",
            "**access:**",
            "**permission:**",
            "**currency:**",
        ):
            self.assertIn(axis, self.memo)

    def test_no_paper_or_execution_selection(self) -> None:
        value = normalized(self.memo)
        self.assertIn("unselected and unauthorized", value)
        for item in (
            "candidate a or candidate b as a first paper",
            "provider, model, version, configuration",
            "corpus, dataset, task packet",
            "sample size, precision or power target",
            "model call, pilot",
        ):
            self.assertIn(item, value)
        self.assertIsNone(
            re.search(
                r"\bwe (?:select|selected|choose|chose) candidate [ab]\b",
                value,
            )
        )

    def test_named_neighbors_have_primary_or_official_routes(self) -> None:
        urls = (
            "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
            "https://iclr.cc/virtual/2026/poster/10008343",
            "https://arxiv.org/abs/2601.06189",
            "https://www.nist.gov/programs-projects/building-evaluation-probes-agentic-ai",
            "https://arxiv.org/abs/2608.18398",
            "https://aclanthology.org/2026.acl-demo.29/",
            "https://aclanthology.org/2025.naacl-demo.35/",
            "https://aclanthology.org/2026.eacl-long.361/",
            "https://aclanthology.org/2026.lrec-1.808/",
            "https://arxiv.org/abs/2602.18940",
            "https://aclanthology.org/2026.acl-long.1023/",
            "https://aclanthology.org/2026.acl-long.384/",
        )
        for url in urls:
            self.assertIn(url, self.route, url)
            self.assertIn(url, self.source_qa, url)

    def test_preprint_and_official_project_statuses_are_not_inflated(self) -> None:
        value = normalized(self.source_qa)
        for phrase in (
            "2026 arxiv preprint",
            "august 2026 arxiv preprint",
            "ongoing official nist project",
            "not a standard",
            "partial / recheck at publication",
            "targeted, not systematic or exhaustive",
        ):
            self.assertIn(phrase, value)


if __name__ == "__main__":
    unittest.main()
