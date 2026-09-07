#!/usr/bin/env python3
"""Faithful short-version + full-essay export; no cover note or protocol prose."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ["manuscript/NINETY_SECOND_VERSION.md", "manuscript/PATTERN_RECOGNITION_V16.md"]


def blocks(text):
    current = []
    for line in text.splitlines() + [""]:
        if not line.strip() or line.startswith("#") or re.match(r"^\d+\. ", line):
            if current:
                yield " ".join(current)
                current = []
            if line.strip():
                yield line.strip()
        else:
            current.append(line.strip())


def plain(text):
    return re.sub(r"^#+\s*", "", text).replace("**", "").replace("*", "")


def inline(text):
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    return re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)


def compact(text):
    return re.sub(r"\s+", "", text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "output/pdf/pattern-map-v16-mentor-reading.pdf")
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Reading", fontName="Times-Roman", fontSize=11.5, leading=16, spaceAfter=9, textColor=colors.HexColor("#172a31")))
    styles.add(ParagraphStyle(name="TitleReading", fontName="Helvetica-Bold", fontSize=24, leading=29, spaceAfter=17, textColor=colors.HexColor("#143e49"), keepWithNext=True))
    styles.add(ParagraphStyle(name="SectionReading", fontName="Helvetica-Bold", fontSize=15, leading=19, spaceBefore=15, spaceAfter=9, textColor=colors.HexColor("#143e49"), keepWithNext=True))
    styles.add(ParagraphStyle(name="SubsectionReading", fontName="Helvetica-Bold", fontSize=12, leading=16, spaceBefore=11, spaceAfter=7, textColor=colors.HexColor("#143e49"), keepWithNext=True))
    story, expected, hashes = [], [], {}
    for index, name in enumerate(SOURCES):
        data = (ROOT / name).read_bytes()
        hashes[name] = hashlib.sha256(data).hexdigest()
        if index:
            story.append(PageBreak())
        for block in blocks(data.decode("utf-8")):
            expected.append(plain(block))
            level = len(block) - len(block.lstrip("#"))
            style = "TitleReading" if level == 1 else "SectionReading" if level == 2 else "SubsectionReading" if level else "Reading"
            body = re.sub(r"^#+\s*", "", block)
            story.append(Paragraph(inline(body), styles[style]))
        story.append(Spacer(1, 5))

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#b8c7cb"))
        canvas.line(54, 44, 558, 44)
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#4d646b"))
        canvas.drawString(54, 31, "Pattern Map v16 | Human reading draft | Short version + complete essay")
        canvas.drawRightString(558, 31, str(doc.page))
        canvas.restoreState()

    doc = SimpleDocTemplate(str(args.output), pagesize=letter, rightMargin=60, leftMargin=60, topMargin=50, bottomMargin=59, title="Pattern Recognition: The Discrimination Layer", author="", pageCompression=1)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    pdf = PdfReader(args.output)
    # Remove our known running footer before checking blocks split across pages.
    page_texts = []
    for number, page in enumerate(pdf.pages, 1):
        text = page.extract_text() or ""
        footer_text = f"Pattern Map v16 | Human reading draft | Short version + complete essay\n{number}\n"
        if not text.startswith(footer_text):
            raise ValueError("Unexpected extraction order; review the running footer")
        page_texts.append(text[len(footer_text):])
    extracted = compact("\n".join(page_texts))
    cursor = 0
    for block in expected:
        match = extracted.find(compact(block), cursor)
        if match < 0:
            raise ValueError("PDF is missing or reordering a canonical text block: " + block[:70])
        cursor = match + len(compact(block))
    record = {"status": "TEXT_VERIFIED_RENDER_REVIEW_REQUIRED", "sources_sha256": hashes, "pdf_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(), "pages": len(pdf.pages), "canonical_blocks_in_order": len(expected), "role": "short version plus full canonical essay; mentor cover note remains separate"}
    args.output.with_suffix(".sources.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
