#!/usr/bin/env python3
"""Render the v15.2 owner-review companion from the established v15 template.

The v15.1 renderer remains frozen for historical reproduction. This adapter
updates the edition, corrected reading contract, and post-red-team method
language while retaining the tested visual system. The semantic HTML routes
and Markdown manuscript remain canonical.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import render_v15_reader_pdf as base


_ORIGINAL_P = base.p
_ORIGINAL_RICH = base.rich


def _ascii_dashes(value: str) -> str:
    """Meet the PDF output contract without changing source documents."""
    translation = str.maketrans({
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
    })
    return value.translate(translation)


def _edition_text(value: str) -> str:
    value = _ascii_dashes(value)
    value = value.replace("V15.1", "V15.2").replace("v15.1", "v15.2")
    replacements = {
        "About 5 min": "About 4 min",
        "15-20 min": "About 9 min",
        "30-45+ min": "Reference depth",
        "Essential argument and receipt": "Opening, argument, and receipt",
        "Map, components, objections": "Complete essay and owner stop",
        "Lab, sources, and technical records": "Explore, Lab, Sources, and technical records",
        "One frozen-model supplied-cue question; F0/F1/F2 only.":
            "One model to be selected; supplied-cue question; F0/F1/F2 only.",
        "The same frozen model would receive the same fictional evidence in three matched versions. No model has been selected and no study has been run.":
            "One not-yet-selected frozen model would receive the same fictional report text, order, output contract, rule, and resources in three matched versions. The relation field is the intended F1/F2 difference. No study has been run.",
        "F1/F2 must preserve exact report bytes and order, exact input-byte length, exact system and instruction bytes, and exact token count under the selected frozen tokenizer. The local regex tokenizer is only a development surrogate.":
            "F1/F2 must preserve report text, order, shape, rule, output contract, and resources. The relation field is the intended difference, so final prompt bytes and hashes may differ; input-byte lengths and selected-tokenizer counts must match. The local regex tokenizer is only a development surrogate.",
        "Risk = invalid output, or a valid count of at least two supporting origins when the manifest certifies none/single or withholds certification as unknown.":
            "FC_cons risk = invalid output, or a valid assertion of at least two supporting origins when the manifest certifies zero or one, or withholds certification as unknown. Report the valid overcount and invalid-output components separately.",
        "On the frozen multiple-origin subset, a valid output must count at least two supporting origins and cite evidence spanning at least two stipulated support roots.":
            "On the frozen M=75 multiple-origin subset, a valid output must count at least two supporting origins and cite evidence spanning at least two benchmark-stipulated support roots. Ordered membership and its hash come from the restricted pre-run manifest and may never be filtered by validity or post-run output.",
        "On fixed M, report F1/F2 VOR, delta, membership hash, and prespecified one-sided 95% lower bound; pass only above -0.05.":
            "On fixed M=75, report F1/F2 VOR, delta, membership hash, and a prespecified one-sided 95% lower bound; pass only above -0.05. Freeze the interval method and verify coverage before registration.",
        "Analysis lock: A=300, fixed M, 10,000-resample primary interval, declared safety interval, coverage simulations.":
            "Analysis lock: A=300, fixed M=75, 10,000-resample primary interval, declared safety interval, and coverage simulations.",
        "No model or tokenizer is selected; no pilot or primary output exists; no preregistration, participant, provider, deployment, or publication is authorized. Offline readiness does not cross that line.":
            "Open gates remain: model/checkpoint and tokenizer selection; provider/runtime and decoding receipt; corpus and split hashes; leakage and parity acceptance; safety-interval method and simulated coverage; ethics/privacy/licensing decisions; registration destination; budget and run authority. No pilot, primary study, preregistration, external-data acquisition, provider spend, deployment, or publication is authorized.",
        "Null, negative, harmful, or unstable":
            "Null, rule-only, invalidity-only, harmful, direct-code/field-only, surface/semantic-audit failure, unstable, noise-fragile, non-transfer, or stopped/quarantined",
        "Preserve and report it; do not change the endpoint, denominator, or run until favorable.":
            "Preserve and report it. Quarantine audit failures; narrow, reject, or retire the tested cue as specified; never change the endpoint, denominator, exclusions, or run until the result becomes favorable.",
        "source/THOUGHT_PIECE_V15.md · v15.2 content":
            "source/THOUGHT_PIECE_V15_2.md · canonical v15.2 content",
        "Semantic local HTML with Essay, Explore, and Lab tracks.":
            "Semantic local HTML with Essay, Explore, Lab, and Sources routes.",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value


def _v15_2_p(text: str, style):
    return _ORIGINAL_P(_edition_text(str(text)), style)


def _v15_2_rich(text: str, style):
    return _ORIGINAL_RICH(_edition_text(str(text)), style)


class V152DocTemplate(base.V15DocTemplate):
    """Retain the established page system with accurate v15.2 metadata."""

    def __init__(self, filename: str, **kwargs):
        kwargs["title"] = "Pattern Recognition: The Discrimination Layer - v15.2"
        kwargs["author"] = "Local owner-review package"
        kwargs["subject"] = "Visual companion to a conceptual synthesis and unrun research program"
        super().__init__(filename, **kwargs)

    def _decorate(self, canvas, doc):
        canvas.saveState()
        canvas.setFillColor(base.PAPER)
        canvas.rect(0, 0, base.A4[0], base.A4[1], fill=1, stroke=0)
        canvas.setFillColor(base.TEAL)
        canvas.rect(0, 0, 4.5 * base.mm, base.A4[1], fill=1, stroke=0)
        canvas.setStrokeColor(base.LINE)
        canvas.setLineWidth(0.45)
        canvas.line(self.leftMargin, 14.5 * base.mm, base.A4[0] - self.rightMargin, 14.5 * base.mm)
        canvas.setFont(base.SANS_BOLD, 5.8)
        canvas.setFillColor(base.CORAL)
        canvas.drawString(
            self.leftMargin,
            9.5 * base.mm,
            "UNTAGGED VISUAL/PRINT COMPANION - HTML IS CANONICAL - NO EMPIRICAL RESULTS",
        )
        canvas.setFillColor(base.MUTED)
        canvas.setFont(base.SANS, 6.3)
        canvas.drawRightString(base.A4[0] - self.rightMargin, 9.5 * base.mm, f"V15.2 - {doc.page:02d}")
        canvas.setTitle("Pattern Recognition: The Discrimination Layer - v15.2")
        canvas.setAuthor("Local owner-review package")
        canvas.setSubject("Visual companion to a conceptual synthesis and unrun research program")
        canvas.restoreState()


def build_pdf(framework_path: Path, output_path: Path) -> None:
    base.p = _v15_2_p
    base.rich = _v15_2_rich
    base.V15DocTemplate = V152DocTemplate
    base.build_pdf(framework_path, output_path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--framework",
        type=Path,
        default=Path("source/FRAMEWORK_COMPONENT_MAP.json"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output/pdf/PATTERN_MAP_V15_2_REVIEW_COMPANION.pdf"),
    )
    args = parser.parse_args()
    build_pdf(args.framework, args.output)


if __name__ == "__main__":
    main()
