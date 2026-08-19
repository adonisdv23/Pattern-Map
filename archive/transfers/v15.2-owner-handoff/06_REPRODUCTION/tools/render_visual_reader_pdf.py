#!/usr/bin/env python3
"""Render the v14 visual reader companion from canonical framework data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Flowable,
    Frame,
    KeepTogether,
    Image as RLImage,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

PAPER = colors.HexColor("#F3EFE5")
PAPER_LIGHT = colors.HexColor("#FBF9F3")
PAPER_DEEP = colors.HexColor("#E7E0D3")
INK = colors.HexColor("#1F1D19")
MUTED = colors.HexColor("#625D55")
LINE = colors.HexColor("#C8C0B2")
TEAL = colors.HexColor("#1B6265")
SAGE = colors.HexColor("#536B40")
VIOLET = colors.HexColor("#5C467D")
CORAL = colors.HexColor("#9C4233")
OCHRE = colors.HexColor("#76500F")
BLUE = colors.HexColor("#35628C")

FAMILY_COLORS = {
    "F1": TEAL,
    "F2": SAGE,
    "F3": VIOLET,
    "F4": CORAL,
    "F5": OCHRE,
    "F6": BLUE,
}

SANS_FONT = "Helvetica"


def register_reader_fonts() -> None:
    """Embed a readable sans face instead of depending on PDF viewer substitution."""
    global SANS_FONT
    candidates = [
        Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path(
            "/Users/gpt/.cache/codex-runtimes/codex-primary-runtime/"
            "dependencies/native/poppler/poppler/fonts/DejaVuSans.ttf"
        ),
    ]
    for font_path in candidates:
        if font_path.is_file():
            pdfmetrics.registerFont(TTFont("ReaderSans", str(font_path)))
            SANS_FONT = "ReaderSans"
            return


class ReaderDocTemplate(BaseDocTemplate):
    """Document template with outline entries for named section paragraphs."""

    def __init__(self, filename: str, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="reader-frame",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(PageTemplate(id="reader", frames=[frame], onPage=self._decorate_page))
        self._outline_counter = 0

    def _decorate_page(self, canvas, doc):
        canvas.saveState()
        canvas.setFillColor(PAPER)
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        canvas.setFillColor(TEAL)
        canvas.rect(0, 0, 5 * mm, A4[1], fill=1, stroke=0)
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(self.leftMargin, 14 * mm, A4[0] - self.rightMargin, 14 * mm)
        canvas.setFillColor(MUTED)
        canvas.setFont(SANS_FONT, 6.7)
        canvas.drawString(self.leftMargin, 9.5 * mm, "PATTERN RECOGNITION · THE DISCRIMINATION LAYER · V14")
        page_label = f"{doc.page:02d}"
        canvas.drawRightString(A4[0] - self.rightMargin, 9.5 * mm, page_label)
        canvas.setTitle("Pattern Recognition: The Discrimination Layer — v14")
        canvas.setAuthor("Owner-review draft")
        canvas.setSubject("A visual systems framework for inspectable context judgment before AI generation")
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name in {"SectionTitle", "FamilyTitle"}:
            self._outline_counter += 1
            key = f"outline-{self._outline_counter}"
            title = flowable.getPlainText()
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title, key, level=0 if flowable.style.name == "SectionTitle" else 1, closed=False)


class StatusRule(Flowable):
    def __init__(self, width: float, color=TEAL, height: float = 4):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.height, fill=1, stroke=0)


def paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(escape(str(text)), style)


def rich(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text, style)


def fitted_image(path: Path, max_width: float, max_height: float, h_align: str = "CENTER") -> RLImage:
    """Return an aspect-preserving image flowable constrained to the given box."""
    image = RLImage(str(path))
    scale = min(max_width / image.imageWidth, max_height / image.imageHeight)
    image.drawWidth = image.imageWidth * scale
    image.drawHeight = image.imageHeight * scale
    image.hAlign = h_align
    return image


def bullets(items: list[str], style: ParagraphStyle, bullet_color=TEAL) -> list[Flowable]:
    output: list[Flowable] = []
    for item in items:
        output.append(
            Paragraph(
                f'<font name="{SANS_FONT}" color="{bullet_color.hexval()}">&bull;</font>&nbsp;&nbsp;{escape(item)}',
                style,
            )
        )
    return output


def make_styles():
    base = getSampleStyleSheet()
    styles: dict[str, ParagraphStyle] = {}
    styles["Eyebrow"] = ParagraphStyle(
        "Eyebrow", parent=base["Normal"], fontName="Courier", fontSize=7.3, leading=10,
        textColor=MUTED, spaceAfter=5 * mm, uppercase=True, tracking=1.3,
    )
    styles["CoverTitle"] = ParagraphStyle(
        "CoverTitle", parent=base["Title"], fontName="Times-Roman", fontSize=42, leading=40,
        textColor=INK, alignment=TA_LEFT, spaceAfter=4 * mm,
    )
    styles["CoverAccent"] = ParagraphStyle(
        "CoverAccent", parent=styles["CoverTitle"], fontName="Times-Italic", textColor=TEAL,
        fontSize=39, leading=39, spaceAfter=9 * mm,
    )
    styles["Subtitle"] = ParagraphStyle(
        "Subtitle", parent=base["Normal"], fontName="Times-Italic", fontSize=14.5, leading=20,
        textColor=MUTED, spaceAfter=10 * mm,
    )
    styles["Thesis"] = ParagraphStyle(
        "Thesis", parent=base["Normal"], fontName="Times-Roman", fontSize=16.2, leading=21,
        textColor=INK,
    )
    styles["SectionKicker"] = ParagraphStyle(
        "SectionKicker", parent=base["Normal"], fontName="Courier-Bold", fontSize=7, leading=9,
        textColor=TEAL, spaceAfter=2.5 * mm, tracking=1.1,
    )
    styles["SectionTitle"] = ParagraphStyle(
        "SectionTitle", parent=base["Heading1"], fontName="Times-Roman", fontSize=28, leading=31,
        textColor=INK, spaceAfter=5 * mm, keepWithNext=True,
    )
    styles["SectionLead"] = ParagraphStyle(
        "SectionLead", parent=base["Normal"], fontName="Times-Roman", fontSize=12.2, leading=17,
        textColor=MUTED, spaceAfter=6 * mm,
    )
    styles["Body"] = ParagraphStyle(
        "Body", parent=base["BodyText"], fontName=SANS_FONT, fontSize=8.8, leading=13,
        textColor=INK, spaceAfter=3 * mm,
    )
    styles["BodySmall"] = ParagraphStyle(
        "BodySmall", parent=styles["Body"], fontSize=7.7, leading=11, textColor=MUTED,
        spaceAfter=2 * mm,
    )
    styles["BodyTiny"] = ParagraphStyle(
        "BodyTiny", parent=styles["Body"], fontSize=6.6, leading=9.2, textColor=MUTED,
        spaceAfter=1.5 * mm,
    )
    styles["BodySmallInverse"] = ParagraphStyle(
        "BodySmallInverse", parent=styles["BodySmall"], textColor=colors.white,
    )
    styles["CardTitle"] = ParagraphStyle(
        "CardTitle", parent=base["Heading3"], fontName="Times-Roman", fontSize=13, leading=15,
        textColor=INK, spaceAfter=2 * mm, keepWithNext=True,
    )
    styles["NodeTitle"] = ParagraphStyle(
        "NodeTitle", parent=styles["CardTitle"], fontSize=10.5, leading=12, spaceAfter=0,
    )
    styles["CardLabel"] = ParagraphStyle(
        "CardLabel", parent=base["Normal"], fontName="Courier-Bold", fontSize=6.4, leading=8,
        textColor=TEAL, spaceAfter=2 * mm, tracking=.7,
    )
    styles["CardLabelInverse"] = ParagraphStyle(
        "CardLabelInverse", parent=styles["CardLabel"], textColor=colors.HexColor("#BCD7D6"),
    )
    styles["FamilyTitle"] = ParagraphStyle(
        "FamilyTitle", parent=base["Heading2"], fontName="Times-Roman", fontSize=24, leading=27,
        textColor=TEAL, spaceAfter=3 * mm, keepWithNext=True,
    )
    styles["ComponentTitle"] = ParagraphStyle(
        "ComponentTitle", parent=base["Heading3"], fontName="Times-Roman", fontSize=18, leading=21,
        textColor=INK, spaceAfter=3 * mm, keepWithNext=True,
    )
    styles["ComponentId"] = ParagraphStyle(
        "ComponentId", parent=base["Normal"], fontName="Courier-Bold", fontSize=7.2, leading=9,
        textColor=TEAL, spaceAfter=1.5 * mm, tracking=1,
    )
    styles["FieldLabel"] = ParagraphStyle(
        "FieldLabel", parent=base["Normal"], fontName="Courier-Bold", fontSize=6.2, leading=8,
        textColor=TEAL, spaceAfter=1.3 * mm, tracking=.5,
    )
    styles["FieldBody"] = ParagraphStyle(
        "FieldBody", parent=base["BodyText"], fontName=SANS_FONT, fontSize=7.5, leading=10.5,
        textColor=INK,
    )
    styles["Quote"] = ParagraphStyle(
        "Quote", parent=base["Normal"], fontName="Times-Italic", fontSize=16, leading=21,
        textColor=TEAL, leftIndent=8 * mm, borderColor=TEAL, borderWidth=0,
        spaceBefore=3 * mm, spaceAfter=6 * mm,
    )
    styles["CenterSmall"] = ParagraphStyle(
        "CenterSmall", parent=styles["BodySmall"], alignment=TA_CENTER, textColor=MUTED,
    )
    return styles


def card(content: list[Flowable], width: float, border=LINE, background=PAPER_LIGHT, padding=5 * mm):
    table = Table([[content]], colWidths=[width])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("BOX", (0, 0), (-1, -1), .6, border),
        ("LEFTPADDING", (0, 0), (-1, -1), padding),
        ("RIGHTPADDING", (0, 0), (-1, -1), padding),
        ("TOPPADDING", (0, 0), (-1, -1), padding),
        ("BOTTOMPADDING", (0, 0), (-1, -1), padding),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return table


def field_box(label: str, value: str, styles, color=TEAL):
    label_style = ParagraphStyle("FieldLabelLocal", parent=styles["FieldLabel"], textColor=color)
    return [paragraph(label.upper(), label_style), paragraph(value, styles["FieldBody"])]


def loop_lane(label: str, title: str, timing: str, nodes: list[tuple[str, str]], return_text: str, styles, width: float, color):
    inner_width = width - 10 * mm
    arrow_width = 5 * mm
    node_width = (inner_width - 3 * arrow_width) / 4
    node_label = ParagraphStyle("LoopNodeLabel", parent=styles["BodyTiny"], textColor=color, fontName="Courier-Bold")
    lane_label = ParagraphStyle("LoopLaneLabel", parent=styles["CardLabel"], textColor=colors.white, backColor=color, leftIndent=2 * mm, rightIndent=2 * mm)

    heading = Table([[
        [paragraph(label, lane_label), paragraph(title, styles["CardTitle"])],
        paragraph(timing.upper(), styles["BodyTiny"]),
    ]], colWidths=[inner_width * .72, inner_width * .28])
    heading.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
    ]))

    node_cells: list[object] = []
    for index, (verb, name) in enumerate(nodes):
        node_cells.append(card([paragraph(verb.upper(), node_label), paragraph(name, styles["NodeTitle"])], node_width, border=color, padding=2.2 * mm))
        if index < len(nodes) - 1:
            node_cells.append(rich(f'<font name="Courier-Bold" size="6.3" color="{color.hexval()}">TO</font>', styles["CenterSmall"]))
    track = Table([node_cells], colWidths=[node_width, arrow_width, node_width, arrow_width, node_width, arrow_width, node_width])
    track.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return_box = card([rich(f'<font name="Courier-Bold" size="6.3" color="{color.hexval()}">RETURN</font>&nbsp;&nbsp;{return_text}', styles["BodySmall"])], inner_width, border=color, padding=2.6 * mm)
    return card([heading, track, Spacer(1, 3 * mm), return_box], width, border=color, padding=5 * mm)


def component_story(component: dict, styles, width: float, color):
    story: list[Flowable] = [CondPageBreak(90 * mm)]
    id_style = ParagraphStyle("ComponentIdLocal", parent=styles["ComponentId"], textColor=color)
    story.append(KeepTogether([
        paragraph(component["id"], id_style),
        paragraph(component["name"], styles["ComponentTitle"]),
        StatusRule(width, color, 3),
        Spacer(1, 3 * mm),
        card(field_box("What it is", component["what_it_is"], styles, color), width, border=color),
        Spacer(1, 3 * mm),
    ]))

    pairs = [
        ("Why it exists", component["why_needed"]),
        ("Consumes", "; ".join(component["consumes"])),
        ("Produces", "; ".join(component["produces"])),
        ("How it interacts", " ".join(component["interactions"])),
        ("What can go wrong", " ".join(component["known_failure_modes"])),
        ("Illustrative example · not a result", component["bounded_implementation_example"]),
        ("Evidence boundary", f'{component["evidence_basis"]["maturity"].replace("_", " ").title()}. Adjacent fields: {", ".join(component["evidence_basis"]["prior_art_families"])}.'),
        ("What remains speculative", " ".join(component["speculative_elements"])),
        ("Human decisions", "; ".join(component["human_decisions"])),
        ("Cost boundaries", "; ".join(component["cost_boundaries"])),
        ("Provenance boundaries", " ".join(component["provenance_boundaries"])),
        ("Open questions", " ".join(component["open_questions"])),
    ]

    for row_index in range(0, len(pairs), 2):
        row = pairs[row_index:row_index + 2]
        cells = [field_box(label, value, styles, color) for label, value in row]
        if len(cells) == 1:
            cells.append([])
        table = Table([cells], colWidths=[(width - 2 * mm) / 2] * 2, hAlign="LEFT")
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT),
            ("GRID", (0, 0), (-1, -1), .45, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
            ("TOPPADDING", (0, 0), (-1, -1), 3.5 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5 * mm),
        ]))
        story.append(table)
    story.append(Spacer(1, 6 * mm))
    return story


def build_pdf(framework_path: Path, output_path: Path):
    register_reader_fonts()
    framework = json.loads(framework_path.read_text(encoding="utf-8"))
    repo_root = framework_path.resolve().parent.parent
    v13_image_path = repo_root / "site/public/images/v13-six-families-origin-map.png"
    example_image_path = repo_root / "site/public/images/nine-mentions-one-origin.jpg"
    for required_image in (v13_image_path, example_image_path):
        if not required_image.is_file():
            raise FileNotFoundError(f"Required PDF image is missing: {required_image}")
    styles = make_styles()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    doc = ReaderDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=16 * mm,
        topMargin=18 * mm,
        bottomMargin=20 * mm,
        title="Pattern Recognition: The Discrimination Layer — v14",
        author="Owner-review draft",
        subject="Visual systems framework for context judgment before AI generation",
    )
    width = doc.width
    story: list[Flowable] = []

    # Cover
    story.extend([
        Spacer(1, 10 * mm),
        paragraph("PERSONAL SYSTEMS MEMO · V14 · PROVISIONAL", styles["Eyebrow"]),
        paragraph("Pattern Recognition /", styles["CoverTitle"]),
        paragraph("The Discrimination Layer", styles["CoverAccent"]),
        paragraph("A visual systems framework for deciding what information deserves acquisition, comparison, enrichment, and influence before AI generates.", styles["Subtitle"]),
        rich('<b>Here, discrimination means technical differentiation among information and possible actions—not social classification.</b>', styles["BodySmall"]),
        StatusRule(width, TEAL, 4),
        Spacer(1, 7 * mm),
    ])
    thesis_card = card([
        paragraph("WORKING PROPOSITION · CONCEPTUAL SYNTHESIS", styles["CardLabel"]),
        rich('<font color="#1B6265"><b>Make the judgment before generation visible.</b></font>', styles["Thesis"]),
        paragraph("Some evidence-sensitive AI workflows may benefit from an explicit, inspectable responsibility for deciding what context can influence generation. Whether that responsibility improves outcomes enough to justify its cost is an empirical question.", styles["Thesis"]),
    ], width, border=TEAL, padding=6 * mm)
    story.extend([thesis_card, Spacer(1, 7 * mm)])
    route_width = (width - 5 * mm) / 2
    route_table = Table([[
        card([paragraph("START HERE · ABOUT 5 MINUTES", styles["CardLabel"]), paragraph("Understand the idea", styles["CardTitle"]), paragraph("Problem, thesis, map, one example, and what remains unproven.", styles["BodySmall"])], route_width, border=TEAL),
        card([paragraph("COMPLETE PATH · ABOUT 25 MINUTES", styles["CardLabel"]), paragraph("Inspect the system", styles["CardTitle"]), paragraph("Eleven responsibilities, relationships, failures, cases, and research horizon.", styles["BodySmall"])], route_width),
    ]], colWidths=[route_width, route_width], hAlign="LEFT")
    route_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 5 * mm), ("RIGHTPADDING", (1, 0), (1, 0), 0)]))
    story.extend([
        route_table,
        Spacer(1, 8 * mm),
        rich('<font name="Courier" size="7" color="#9C4233">STATUS</font>&nbsp;&nbsp; Conceptual synthesis and research agenda. Not empirical validation, peer review, deployment guidance, or a claim of scientific novelty.', styles["BodySmall"]),
        Spacer(1, 3 * mm),
        rich('<font name="Courier" size="7" color="#1B6265">SOURCE BOUNDARY</font>&nbsp;&nbsp; Reconciled with the owner-designated live v13 site. The original v13 diagram is preserved byte-for-byte and hash-verified; the archived rendered-DOM snapshot is a reference capture, while the original standalone HTML remains unavailable.', styles["BodySmall"]),
        Spacer(1, 3 * mm),
        rich('<font name="Courier" size="7" color="#35628C">ACCESSIBILITY</font>&nbsp;&nbsp; This is a visual/print companion. The semantic HTML reader is the accessible canonical reading surface.', styles["BodySmall"]),
        PageBreak(),
    ])

    # Five-minute overview
    story.extend([
        paragraph("01 · FIVE-MINUTE OVERVIEW", styles["SectionKicker"]),
        paragraph("The visible answer is often where hidden decisions surface.", styles["SectionTitle"]),
        paragraph("A model can write a polished answer from a poor evidence environment. The failure appears at the end, but the consequential choices often happened before generation.", styles["SectionLead"]),
        card([
            paragraph("CONCRETE PREVIEW", styles["CardLabelInverse"]),
            rich('<font color="#FFFFFF"><b>Nine positive articles can still trace to one launch announcement.</b></font>', styles["Thesis"]),
            rich('<font color="#DED8CD">Repeated mentions remain separate observations, but they do not establish distinct-origin support under this packet’s relation rule.</font>', styles["BodySmallInverse"]),
        ], width, border=INK, background=INK, padding=5 * mm),
        Spacer(1, 5 * mm),
    ])

    receipt_counts = Table([[
        [paragraph("OBSERVATIONS", styles["CardLabel"]), paragraph("09", styles["CardTitle"]), paragraph("under review", styles["BodyTiny"])],
        [paragraph("KNOWN CLUSTER", styles["CardLabel"]), paragraph("01", styles["CardTitle"]), paragraph("for those records", styles["BodyTiny"])],
        [paragraph("SUPPORT ORIGINS", styles["CardLabel"]), paragraph("00", styles["CardTitle"]), paragraph("under stated relation rule", styles["BodyTiny"])],
        [paragraph("SEPARATE ROOTS", styles["CardLabel"]), paragraph("02", styles["CardTitle"]), paragraph("contrast only", styles["BodyTiny"])],
    ]], colWidths=[width / 4] * 4)
    receipt_counts.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), .45, LINE),
        ("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 3 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
    ]))
    receipt_rows = [[
        paragraph("RECORD", styles["CardLabel"]),
        paragraph("RECORD KIND", styles["CardLabel"]),
        paragraph("ORIGIN RELATION", styles["CardLabel"]),
        paragraph("WHAT THIS COUNTS AS", styles["CardLabel"]),
    ]]
    for index in range(1, 10):
        receipt_rows.append([
            paragraph(f"O{index:02d}", styles["BodyTiny"]),
            paragraph("Report observation", styles["BodyTiny"]),
            rich('Origin A · <font color="#5C467D"><b>DEPENDENT</b></font>', styles["BodyTiny"]),
            paragraph("Repeats the launch announcement; not separately rooted support under this relation rule.", styles["BodyTiny"]),
        ])
    receipt_ledger = Table(receipt_rows, colWidths=[18 * mm, 37 * mm, 43 * mm, width - 98 * mm], repeatRows=1)
    receipt_ledger.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), .35, LINE),
        ("BACKGROUND", (0, 0), (-1, 0), PAPER_DEEP),
        ("BACKGROUND", (0, 1), (-1, -1), PAPER_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
    ]))
    relation_key = Table([[
        [paragraph("ORIGIN RELATION KEY", styles["CardLabel"]),
         rich('<b>DEPENDENT</b> · traceable to an existing artifact; preserve the observation, but do not count it as separately rooted support.<br/><br/><b>INDEPENDENT-AS-STIPULATED</b> · a separate root declared by this illustration or benchmark, not provenance discovery.<br/><br/><b>UNKNOWN</b> · unresolved; preserve it and do not guess either way.', styles["BodyTiny"])],
        [paragraph("SEPARATE ROOTS FOR CONTRAST", styles["CardLabel"]),
         rich('<b>B1</b> · separate root · illustrative<br/><b>C1</b> · separate root · illustrative<br/><br/>Claim support is not assessed. These roots are not counted as support for this packet’s claim.', styles["BodyTiny"])],
    ]], colWidths=[width * .62, width * .38])
    relation_key.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), .4, LINE),
        ("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 4 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4 * mm),
    ]))
    story.extend([
        paragraph("ORIGIN-ACCOUNTING RECEIPT · ORIGIN-EX-01 · VERSION 0.2", styles["SectionKicker"]),
        paragraph("Nine observations can still represent one origin.", styles["SectionTitle"]),
        paragraph("Fictional bundle; no live data. This static receipt records relationships and a human disposition. It does not discover provenance, establish truth, or depict a required workflow.", styles["SectionLead"]),
        card([
            paragraph("CLAIM UNDER REVIEW", styles["CardLabel"]),
            paragraph('“The tool is broadly validated.”', styles["CardTitle"]),
            rich('<font color="#9C4233"><b>INSUFFICIENT</b></font> · nine mentions do not establish nine distinct origins.', styles["BodySmall"]),
        ], width, border=INK, padding=4 * mm),
        Spacer(1, 4 * mm),
        receipt_counts,
        Spacer(1, 4 * mm),
        card([rich('<b>UNKNOWN stays unknown.</b> Do not move an unresolved origin relation into the dependent or separate-root total.', styles["BodySmall"])], width, border=VIOLET, padding=3.5 * mm),
        Spacer(1, 4 * mm),
        paragraph("Observation ledger · nine unordered records", styles["CardTitle"]),
        paragraph("Rows preserve observations; their order is not a workflow or confidence ranking.", styles["BodySmall"]),
        receipt_ledger,
        Spacer(1, 4 * mm),
        relation_key,
        Spacer(1, 4 * mm),
        card([
            paragraph("HUMAN DISPOSITION", styles["CardLabel"]),
            paragraph("HOLD · VERIFY ANOTHER ORIGIN RELATION", styles["CardTitle"]),
            paragraph("Inspect the originating announcement, then look for a separately authored benchmark and document its origin relation before changing the claim state. No automatic admission, rejection, or truth verdict.", styles["BodySmall"]),
        ], width, border=CORAL, padding=4 * mm),
        paragraph("Illustrative only · not a reported dataset · not a provenance audit · not a system runtime. No image is required to interpret this receipt.", styles["BodyTiny"]),
        Spacer(1, 6 * mm),
    ])
    questions = [
        "What was available at all?", "Which repetitions shared one origin?", "What supported each claim?",
        "Was another search worth its cost?", "What entered the final context?", "Who could correct the decision?",
    ]
    q_cells = []
    for index in range(0, len(questions), 2):
        q_cells.append([paragraph("?  " + questions[index], styles["Body"]), paragraph("?  " + questions[index + 1], styles["Body"])])
    q_table = Table(q_cells, colWidths=[width / 2] * 2)
    q_table.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .4, LINE), ("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm), ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm), ("TOPPADDING", (0, 0), (-1, -1), 3 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm)]))
    story.extend([q_table, Spacer(1, 6 * mm)])
    definitions = Table([[
        [paragraph("WHAT THE LAYER SEPARATES", styles["CardLabel"]), paragraph("Authority, support, independence, relevance, authorization, and action priority remain different judgments.", styles["BodySmall"])],
        [paragraph("LAYER", styles["CardLabel"]), paragraph("A systems responsibility, not necessarily one service, model, prompt, or box.", styles["BodySmall"])],
    ]], colWidths=[width / 2] * 2)
    definitions.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT), ("BOX", (0, 0), (-1, -1), .5, INK), ("INNERGRID", (0, 0), (-1, -1), .4, LINE), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 5 * mm), ("RIGHTPADDING", (0, 0), (-1, -1), 5 * mm), ("TOPPADDING", (0, 0), (-1, -1), 4 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm)]))
    v13_thumb = fitted_image(v13_image_path, 54 * mm, 82 * mm)
    v13_text = [
        paragraph("HISTORICAL REFERENCE · V13 · NOT THE V14 SYSTEM MAP", styles["CardLabel"]),
        paragraph("Six Families Map", styles["CardTitle"]),
        paragraph("The original diagram is preserved and hash-verified. It placed Peripheral Signal Mining at the center of source weighing, velocity, absence + memory, structured patterns, a learning loop, and implementation.", styles["BodyTiny"]),
        paragraph("Historical seven-step strip", styles["CardLabel"]),
        paragraph("1 Collect widely. 2 Score and weight sources. 3 Detect gaps with memory and longitudinal context. 4 Compare patterns and source sets. 5 Measure velocity. 6 Produce a ranked shortlist. 7 Continuously update weights and baselines.", styles["BodyTiny"]),
        paragraph("V14 replaces that center-and-sequence emphasis with inspectable responsibilities, typed relations, terminal states, human correction, and separately versioned outcome updates.", styles["BodyTiny"]),
    ]
    v13_table = Table([[v13_text, v13_thumb]], colWidths=[width - 60 * mm, 60 * mm])
    v13_table.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), .5, INK),
        ("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 4 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4 * mm),
    ]))
    story.extend([
        definitions,
        Spacer(1, 7 * mm),
        paragraph("FROM V13 TO V14", styles["SectionKicker"]),
        paragraph("The center of gravity moved, but the pulse remains.", styles["CardTitle"]),
        paragraph("V13 asked how to find the specialist comment, anomalous change, repeated unanswered question, or memory that generic workflows miss. V14 asks the harder follow-on: what gives any item the right to influence the answer?", styles["Body"]),
        paragraph("Underweighted is a starting condition, not a conclusion.", styles["Quote"]),
        Spacer(1, 4 * mm),
        v13_table,
        PageBreak(),
        paragraph("01 · DISTINCTION CONTRACT", styles["SectionKicker"]),
        paragraph("Keep the judgments apart.", styles["SectionTitle"]),
        paragraph("A useful discrimination layer cannot collapse every evidential and operational question into one confidence score. These paired terms define the framework's anti-collapse rule.", styles["SectionLead"]),
    ])
    distinctions = [
        ("Attention priority", "Truth"), ("Domain source authority", "Universal trust"),
        ("Claim support", "Source popularity"), ("Recurrence", "Independence"),
        ("Independence", "Different wording, URLs, or unknown origin"), ("Relevance", "General importance"),
        ("Operational authorization", "Source authority or technical access"), ("Enrichment value", "Action priority or acceptance"),
        ("Action priority", "A factual conclusion or truth probability"), ("Provenance", "Correctness"),
        ("Owner disposition", "External truth"), ("Signal candidate", "A verified event or conclusion"),
    ]
    d_rows = [[rich(f"<b>{escape(a)}</b><br/><font color='#9C4233' size='6'>IS NOT</font><br/>{escape(b)}", styles["BodySmall"]) for a, b in distinctions[i:i+2]] for i in range(0, len(distinctions), 2)]
    d_table = Table(d_rows, colWidths=[width / 2] * 2)
    d_table.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .4, LINE), ("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm), ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm), ("TOPPADDING", (0, 0), (-1, -1), 3 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm)]))
    story.extend([d_table, PageBreak()])

    # Map
    story.extend([
        paragraph("02 · SYSTEM MAP", styles["SectionKicker"]),
        paragraph("The judgment before generation", styles["SectionTitle"]),
        paragraph("Six families and eleven responsibilities. The flow is iterative: a gap can trigger another acquisition, a reviewer can revise the frame, and an outcome can propose—but not silently apply—a policy update.", styles["SectionLead"]),
    ])
    family_by_id = {family["id"]: family for family in framework["mechanism_families"]}
    card_width = (width - 16 * mm) / 3
    arrow_width = 8 * mm
    map_rows = []
    for row_start in (0, 3):
        row = []
        for offset in range(3):
            family = framework["mechanism_families"][row_start + offset]
            color = FAMILY_COLORS[family["id"]]
            component_ids = " · ".join(family["component_ids"])
            family_content = [
                rich(f'<font name="Times-Italic" size="14" color="{color.hexval()}">{int(family["id"][1:]):02d}</font>', styles["Body"]),
                paragraph(family["name"], styles["CardTitle"]),
                paragraph(family["purpose"], styles["BodyTiny"]),
                rich(f'<font name="Courier" size="6" color="{color.hexval()}">{component_ids}</font>', styles["BodyTiny"]),
            ]
            row.append(card(family_content, card_width, border=color, padding=4 * mm))
            if offset < 2:
                row.append("")
        map_rows.append(row)
    map_table = Table(map_rows, colWidths=[card_width, arrow_width, card_width, arrow_width, card_width], rowHeights=[55 * mm, 55 * mm], hAlign="LEFT")
    map_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 2 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm)]))
    story.extend([
        map_table,
        Spacer(1, 5 * mm),
        card([rich('<font name="Courier-Bold" size="6.3" color="#35628C">RETURN</font>&nbsp;&nbsp; Human correction and later outcomes can revise the route without rewriting the evidence.', styles["BodySmall"])], width, border=BLUE),
        Spacer(1, 6 * mm),
        paragraph("TEXT EQUIVALENT", styles["SectionKicker"]),
    ])
    map_steps = [
        "A bounded question and permission envelope governs acquisition.",
        "Captured material receives source, artifact, version, and derivation records.",
        "Relationship and claim views expose origin, support, contradiction, and gaps.",
        "Separate assessments inform a cost-bounded next action.",
        "A human can correct the route; evidence and decisions remain separately versioned.",
        "A defined later outcome may motivate an approved policy update.",
    ]
    story.extend(bullets(map_steps, styles["Body"]))
    story.append(PageBreak())

    # Components, family by family
    components_by_family: dict[str, list[dict]] = {family["id"]: [] for family in framework["mechanism_families"]}
    for component in framework["components"]:
        components_by_family[component["family_id"]].append(component)

    for family in framework["mechanism_families"]:
        color = FAMILY_COLORS[family["id"]]
        family_style = ParagraphStyle("FamilyTitleLocal", parent=styles["FamilyTitle"], textColor=color)
        story.extend([
            paragraph(f'{int(family["id"][1:]):02d} · MECHANISM FAMILY', styles["SectionKicker"]),
            paragraph(family["name"], family_style),
            paragraph(family["purpose"], styles["SectionLead"]),
        ])
        for component in components_by_family[family["id"]]:
            story.extend(component_story(component, styles, width, color))
        story.append(PageBreak())

    # Connections and example
    story.extend([
        paragraph("04 · CONNECTIONS", styles["SectionKicker"]),
        paragraph("One fast loop. One slower loop.", styles["SectionTitle"]),
        paragraph("The framework preserves observations, interpretations, decisions, and outcomes as different record types. Revision changes a view or policy; it does not erase the evidence path that existed at decision time.", styles["SectionLead"]),
    ])
    story.extend([
        loop_lane(
            "LOOP A", "Evidence enrichment", "within one decision",
            [("Observe", "Evidence graphs"), ("Separate", "Assessments"), ("Choose", "Router"), ("Permit", "Acquisition")],
            "<b>New captured evidence returns to the graphs.</b> A stop rule, cost, or permission boundary can end the loop.",
            styles, width, VIOLET,
        ),
        Spacer(1, 4 * mm),
        loop_lane(
            "LOOP B", "Outcome revision", "across decisions",
            [("Preserve", "Decision"), ("Observe", "Outcome"), ("Propose", "Update"), ("Review", "Human disposition")],
            "<b>Only an approved new policy changes future routing.</b> Original evidence, decision, and policy version remain intact.",
            styles, width, BLUE,
        ),
        Spacer(1, 5 * mm),
        paragraph("TEXT EQUIVALENT", styles["SectionKicker"]),
        paragraph("Within a decision, a typed gap can send a cost- and permission-bounded route back to acquisition; new evidence then returns to the relationship and claim views. Across decisions, a predefined outcome can motivate a proposed policy update, but human disposition controls whether a new version affects future routing.", styles["BodySmall"]),
        PageBreak(),
    ])
    state_rows = [
        ["OBSERVATION", "A captured issue report contains a rollback account.", "Preserve; append correction or supersession."],
        ["INTERPRETATION", "The report may indicate a failure mode.", "Revise with reason; never recast as observed fact."],
        ["DECISION", "Run one synthetic-data rollback check.", "Version with brief, route, owner, and cost."],
        ["OUTCOME", "The predefined sandbox check passed or failed.", "Record horizon and confounders; propose policy change separately."],
    ]
    state_table = Table([[paragraph("RECORD", styles["CardLabel"]), paragraph("EXAMPLE", styles["CardLabel"]), paragraph("REVISION RULE", styles["CardLabel"])]] + [[paragraph(cell, styles["BodySmall"]) for cell in row] for row in state_rows], colWidths=[30 * mm, 71 * mm, width - 101 * mm], repeatRows=1)
    state_table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), INK), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white), ("GRID", (0, 0), (-1, -1), .45, LINE), ("BACKGROUND", (0, 1), (-1, -1), PAPER_LIGHT), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm), ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm), ("TOPPADDING", (0, 0), (-1, -1), 3 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5 * mm)]))
    story.extend([
        state_table,
        Spacer(1, 8 * mm),
        paragraph("THREE IMPLEMENTATION PATHS", styles["SectionKicker"]),
        paragraph("Different placements, not maturity levels.", styles["CardTitle"]),
        paragraph("The responsibility can live in team practice, workflow coordination, model behavior, or a combination. None is inherently deeper or more defensible.", styles["BodySmall"]),
    ])
    path_width = (width - 6 * mm) / 3
    path_table = Table([[
        card([paragraph("PRACTICE", styles["CardLabel"]), paragraph("Make the judgment explicit in existing work.", styles["NodeTitle"]), paragraph("Define the decision, separate evidential judgments, record material exclusions, and state why research stopped.", styles["BodyTiny"])], path_width, border=TEAL, padding=3.5 * mm),
        card([paragraph("SYSTEM", styles["CardLabel"]), paragraph("Coordinate evidence, policy, review, and memory.", styles["NodeTitle"]), paragraph("Assemble an inspectable context packet while preserving provenance, permissions, and correction.", styles["BodyTiny"])], path_width, border=TEAL, padding=3.5 * mm),
        card([paragraph("MODEL", styles["CardLabel"]), paragraph("Encourage information seeking and abstention.", styles["NodeTitle"]), paragraph("Training or agent policies may help, but cannot replace external identity, receipts, permissions, or human authority.", styles["BodyTiny"])], path_width, border=TEAL, padding=3.5 * mm),
    ]], colWidths=[path_width, path_width, path_width])
    path_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm),
        ("RIGHTPADDING", (2, 0), (2, 0), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.extend([path_table, PageBreak()])

    story.extend([
        paragraph("05 · WORKED EXAMPLE", styles["SectionKicker"]),
        paragraph("Nine positive articles. One launch announcement.", styles["SectionTitle"]),
        paragraph("Illustrative example—not a reported case or result. A technical team is deciding whether to run a sandbox pilot of a data-migration tool. A flat summary sees popularity. The framework sees a chain of different questions.", styles["SectionLead"]),
        fitted_image(example_image_path, width, 105 * mm),
        Spacer(1, 2 * mm),
        paragraph("MANY MENTIONS CAN PRESERVE ONE ORIGIN", styles["CardLabel"]),
        paragraph("In this illustration, nine observations share one known origin; two artifacts have separate roots. Repetition is neither erased nor treated as proof, and common origin does not make a report false. Illustration only; colors encode no status; not a dataset, provenance audit, or result.", styles["BodyTiny"]),
        Spacer(1, 5 * mm),
    ])
    contrast_width = width / 2
    contrast_table = Table([[
        [paragraph("A FLAT SUMMARY SAYS", styles["CardLabelInverse"]), rich('<font color="#FFFFFF"><b>“Nine positive articles make the tool look broadly validated. A pilot appears low-risk.”</b></font>', styles["Thesis"])],
        [paragraph("THE LAYER ASKS", styles["CardLabelInverse"]), rich('<font color="#FFFFFF"><b>How many distinct origins are documented under the packet’s relation rule? Which exact claims are supported? What would change a sandbox-only decision?</b></font>', styles["Thesis"])],
    ]], colWidths=[contrast_width, contrast_width])
    contrast_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), INK),
        ("BACKGROUND", (1, 0), (1, 0), TEAL),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 5 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5 * mm),
    ]))
    story.extend([contrast_table, Spacer(1, 5 * mm)])
    example_steps = [
        ("1", "Bound the decision", "Sandbox only. No production data. Ninety minutes of research."),
        ("2", "Trace the material", "Nine positive articles paraphrase the same vendor announcement."),
        ("3", "Split the claims", "Nine mentions remain nine observations, but they establish only one known origin under the packet’s relation rule."),
        ("4", "Keep judgments separate", "Official documentation can be authoritative and still remain vendor-linked under the stated relation rule."),
        ("5", "Choose one bounded step", "Inspect the benchmark method and reproduce one rollback path locally."),
        ("6", "Preserve the outcome", "A later sandbox result may change a pilot rule, not external truth."),
    ]
    e_rows = []
    for index in range(0, 6, 3):
        row = []
        for number, title, body in example_steps[index:index+3]:
            row.append(card([rich(f'<font name="Courier-Bold" size="6.5" color="#9C4233">STEP {number}</font>', styles["Body"]), paragraph(title, styles["CardTitle"]), paragraph(body, styles["BodySmall"])], width / 3, border=CORAL, padding=4 * mm))
        e_rows.append(row)
    e_table = Table(e_rows, colWidths=[width / 3] * 3)
    e_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm), ("TOPPADDING", (0, 0), (-1, -1), 2 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    story.extend([
        e_table,
        Spacer(1, 6 * mm),
        card([paragraph("WHAT THE PACKET SAYS", styles["CardLabel"]), paragraph("The tool documents rollback. Its comparative speed claim remains vendor-supported only. Two failure reports are relevant but not prevalence evidence. Nine positive articles share one known origin. A bounded synthetic-data check is warranted before a sandbox-only pilot decision.", styles["Thesis"])], width, border=CORAL),
        PageBreak(),
    ])

    # Counterarguments
    story.extend([
        paragraph("06 · CHALLENGES & LIMITS", styles["SectionKicker"]),
        paragraph("A serious framework names how it could lose.", styles["SectionTitle"]),
    ])
    counters = [
        ("01", "Old work, new label", "The mechanisms reviewed here already have mature precedents. The plausible contribution is a boundary-preserving synthesis and evaluation agenda—not a new mechanism family."),
        ("02", "A new gatekeeper", "Any selection policy can reinforce institutional bias or erase peripheral evidence. Exclusions, unknowns, reasons, appeal, and source diversity must stay inspectable."),
        ("03", "Rigor theater", "Detailed provenance can trace a false claim perfectly. Lineage never upgrades correctness, independence, or permission by itself."),
        ("04", "More cost than value", "The architecture must beat strong simple baselines under matched time, tokens, retrieval, and review effort."),
        ("05", "Decorative human review", "A person placed after an opaque route may only rubber-stamp it. Review must expose the evidence path and permit consequential correction."),
        ("06", "Learning the wrong lesson", "Outcome feedback can encode preference, contaminated proxies, or hindsight. Updates need predefined outcomes, attribution limits, versioning, and approval."),
    ]
    c_rows = []
    for index in range(0, len(counters), 2):
        row = []
        for number, title, body in counters[index:index+2]:
            row.append(card([rich(f'<font name="Courier-Bold" size="6.5" color="#9C4233">CHALLENGE {number}</font>', styles["Body"]), paragraph(title, styles["CardTitle"]), paragraph(body, styles["BodySmall"])], width / 2, border=LINE, padding=4 * mm))
        c_rows.append(row)
    c_table = Table(c_rows, colWidths=[width / 2] * 2)
    c_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm), ("TOPPADDING", (0, 0), (-1, -1), 2 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    story.extend([c_table, Spacer(1, 6 * mm)])
    falsifiers = [
        "A strong retrieval-plus-citation baseline performs equivalently at lower cost.",
        "Reviewers cannot reliably distinguish authority, support, independence, relevance, and action priority.",
        "Origin-aware grouping hides legitimate convergence as often as it prevents false corroboration.",
        "The interface increases overload, review time, or overreliance enough to erase any benefit.",
        "Outcome updates encode local preference or contaminated proxies rather than better policy.",
    ]
    story.extend([card([paragraph("WHAT WOULD MATERIALLY WEAKEN OR RETIRE IT FOR A NAMED TASK CLASS?", styles["CardLabelInverse"])] + bullets(falsifiers, styles["BodySmallInverse"], CORAL), width, border=INK, background=INK, padding=5 * mm)])
    story.append(PageBreak())

    limitations = [
        ("No empirical evaluation.", "No experiment, participant study, field outcome, or comparative performance result."),
        ("No claim of mechanism novelty.", "The components have extensive prior art, and the integration may overlap a framework not yet found."),
        ("No proven minimum.", "Eleven components are an analytical decomposition, not a required implementation count."),
        ("No validated constructs.", "Reviewers may not reliably distinguish the proposed assessment dimensions."),
        ("Open-world evidence remains hard.", "Sources change, origins are obscured, evidence is inaccessible, and support stays contested."),
        ("Costs and utilities are uncertain.", "A clean stopping rule can still stop early or encode the wrong consequence model."),
        ("Human control is not guaranteed.", "Interfaces and organizational incentives can turn review into ceremony."),
        ("Memory can amplify error.", "Retention, retrieval, and summarization can preserve stale, biased, or manipulated content."),
        ("The name may fail.", "Discrimination layer may remain ambiguous or harmful despite a technical definition."),
        ("Historical HTML source is bounded.", "The original v13 diagram is preserved and hash-verified. A rendered-DOM snapshot is archived as reference; the original standalone HTML remains unavailable."),
        ("Product cases are illustrative.", "Alpha Solver and Signal Foundry are related cases, not independent validation."),
        ("No publication or owner approval.", "This is a local review draft."),
    ]
    story.extend([
        paragraph("CURRENT LIMITATIONS", styles["SectionKicker"]),
        paragraph("Twelve boundaries the presentation cannot smooth away.", styles["SectionTitle"]),
    ])
    limitation_rows = []
    for index in range(0, len(limitations), 2):
        row = []
        for offset, (title, body) in enumerate(limitations[index:index + 2], start=index + 1):
            row.append([
                rich(f'<font name="Courier-Bold" size="6.3" color="#9C4233">{offset:02d}</font>', styles["BodyTiny"]),
                paragraph(title, styles["CardTitle"]),
                paragraph(body, styles["BodyTiny"]),
            ])
        limitation_rows.append(row)
    limitation_table = Table(limitation_rows, colWidths=[width / 2] * 2)
    limitation_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), .45, LINE),
        ("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 3 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
    ]))
    story.extend([limitation_table, PageBreak()])

    # Cases and enterprise
    story.extend([
        paragraph("07 · BOUNDED CASES", styles["SectionKicker"]),
        paragraph("Translation, not validation", styles["SectionTitle"]),
        paragraph("Two product settings make the responsibilities concrete. Neither product is evidence that the full framework improves outcomes or generalizes.", styles["SectionLead"]),
    ])
    case_width = (width - 5 * mm) / 2
    case_table = Table([[
        card([
            paragraph("ALPHA SOLVER", styles["CardLabel"]),
            paragraph("A reasoning posture, not proof.", styles["CardTitle"]),
            card([rich('<b>Boundary:</b> repository structure and product intent do not show improved reasoning quality, safety, or outcomes.', styles["BodySmall"])], case_width - 10 * mm, border=VIOLET, background=PAPER_DEEP, padding=3 * mm),
            Spacer(1, 3 * mm),
            paragraph("The inspected Alpha Solver documents are intended to illustrate how a decision brief, explicit assumptions, alternatives, tool permissions, and reviewable reasoning can constrain a solution path.", styles["BodySmall"]),
        ], case_width, border=VIOLET),
        card([
            paragraph("SIGNAL FOUNDRY", styles["CardLabel"]),
            paragraph("Evidence responsibilities, not a universal model.", styles["CardTitle"]),
            card([rich('<b>Boundary:</b> those safeguards are product-specific design choices, not empirical support for eleven general responsibilities.', styles["BodySmall"])], case_width - 10 * mm, border=VIOLET, background=PAPER_DEEP, padding=3 * mm),
            Spacer(1, 3 * mm),
            paragraph("The inspected Signal Foundry boundary documents specify examples of immutable raw acquisition, exclusion boundaries, source-aware evidence, staged import, and separation between transcript and visual evidence.", styles["BodySmall"]),
        ], case_width, border=VIOLET),
    ]], colWidths=[case_width, case_width])
    case_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 5 * mm), ("RIGHTPADDING", (1, 0), (1, 0), 0)]))
    story.extend([
        case_table,
        Spacer(1, 7 * mm),
        card([paragraph("ENTERPRISE TRANSLATION", styles["CardLabel"]), paragraph("Identity, policy, receipts, review, versioning.", styles["CardTitle"]), paragraph("The framework can map to role-based authorization, lineage systems, policy engines, approval queues, evaluation records, and risk-management controls. That mapping does not establish compliance, safety, or return on investment in any deployment.", styles["BodySmall"])], width, border=VIOLET),
        PageBreak(),
    ])

    # Research horizon
    story.extend([
        paragraph("08 · RESEARCH HORIZON", styles["SectionKicker"]),
        paragraph("The next artifact depends on the claim we choose to test.", styles["SectionTitle"]),
        paragraph("The current work is a practitioner thought piece with an academic readiness path. It should not be styled as a paper until a contribution type, prior-art protocol, methods, data, participants, outcomes, and falsifiers are fixed in advance.", styles["SectionLead"]),
        card([
            paragraph("NARROWEST CREDIBLE FIRST PAPER · PROPOSED DESIGN, NOT A RESULT", styles["CardLabel"]),
            paragraph("Oracle Origin-Relation Metadata in One Frozen Model", styles["CardTitle"]),
            paragraph("80 development + 40 feasibility-only pilot + 300 primary + 60 locked stress bundles. Compare citation-only, rule-only, and the byte-identical rule plus stipulated relation metadata, with exact F1/F2 token parity.", styles["BodySmall"]),
            paragraph("Primary: all-assigned conservative-risk-coded F2−F1 false corroboration. Safety: fixed-set recall of stipulated supporting origins, with a candidate one-sided five-point non-inferiority margin. This estimates an observable condition effect—not internal reasoning, provenance discovery, human benefit, or the full layer.", styles["BodySmall"]),
        ], width, border=BLUE, padding=5 * mm),
        Spacer(1, 5 * mm),
    ])
    research_paths = [
        ("01", "Conceptual systems framework", "Can experts distinguish the typed responsibilities, and does an existing architecture already cover them?", "Protocol-led synthesis, construct sorting, discriminant validity, inter-rater agreement, and adversarial boundary cases."),
        ("02", "Design-science artifact", "Can a bounded artifact make the evidence-to-action path traceable and correctable?", "Requirements traceability, technical invariants, usability work, a strong simple baseline, and mechanism ablations."),
        ("03", "HCI / sensemaking system", "Which representation supports correction and calibrated reliance without overwhelming people?", "Representative-user studies, comprehension and correction measures, accessibility evaluation, and qualitative strategy analysis."),
        ("04", "AI context / evidence architecture", "Does origin-aware context policy improve supported generation under matched budgets?", "Strong RAG and reranker baselines, known-derivation corpora, matched tokens and spend, repeated runs, ablations, and blinded adjudication."),
        ("05", "Decision-support evaluation", "When does the framework improve decisions enough to justify its overhead?", "Preregistered comparative studies, validated outcomes, matched resources, blinded scoring, delayed outcomes where possible, and harm analysis."),
        ("06", "Practitioner thought piece", "Can the framework sharpen practice without borrowing academic authority it has not earned?", "Transparent synthesis, disciplined status labels, concrete examples, counterarguments, and an explicit route to future evidence."),
    ]
    for number, title, question, burden in research_paths:
        story.append(KeepTogether([card([
            rich(f'<font name="Courier" size="7" color="#35628C">{number}</font>', styles["BodyTiny"]),
            paragraph(title, styles["CardTitle"]),
            rich(f'<b>Question.</b> {escape(question)}', styles["BodySmall"]),
            rich(f'<b>Evidence burden.</b> {escape(burden)}', styles["BodySmall"]),
        ], width, border=LINE, padding=4 * mm), Spacer(1, 3 * mm)]))
    story.extend([
        Spacer(1, 3 * mm),
        card([paragraph("RECOMMENDED SEQUENCE", styles["CardLabel"]), paragraph("1 · construct boundary  →  2 · provenance-rich benchmark  →  3 · strong simple baselines  →  4 · people and outcomes", styles["BodySmall"])], width, border=BLUE),
        PageBreak(),
    ])

    # Sources and glossary
    story.extend([
        paragraph("09 · SELECTED SOURCES", styles["SectionKicker"]),
        paragraph("Prior art narrows the claim.", styles["SectionTitle"]),
        paragraph("The mechanisms reviewed here have mature precedents in adjacent fields. These selected primary and official sources support only the bounded points named below; they do not validate the synthesis.", styles["SectionLead"]),
    ])
    refs = [
        ("Lewis et al. (2020), Retrieval-Augmented Generation", "https://papers.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html", "Retrieving external material before generation."),
        ("Liu et al. (2024), Lost in the Middle", "https://aclanthology.org/2024.tacl-1.9/", "Long context does not guarantee uniform use of relevant information."),
        ("Tan et al. (2025), HydraRAG", "https://aclanthology.org/2025.emnlp-main.730/", "Integrated cross-source reasoning and corroboration make broad architecture novelty untenable."),
        ("Ge et al. (2025), CONFACT", "https://www.ijcai.org/proceedings/2025/1073", "Conflict and credibility information in RAG; credibility is not origin relation."),
        ("Nematov et al. (2025), Source Attribution in RAG", "https://doi.org/10.48550/arXiv.2507.04480", "Preprint on source influence, redundancy, complementarity, and synergy; not an origin-family graph."),
        ("Xia (2026), Matched Evidence Utilization", "https://doi.org/10.48550/arXiv.2606.06758", "Preprint precedent for observable matched-condition diagnostics rather than internal-mechanism claims."),
        ("W3C PROV-O", "https://www.w3.org/TR/prov-o/", "Entities, activities, agents, and derivation."),
        ("Cochrane Handbook, chapter 4", "https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04", "Collating multiple reports of one underlying study."),
        ("Thorne et al. (2018), FEVER", "https://aclanthology.org/N18-1074/", "Claim and evidence-state precedent."),
        ("Wadden et al. (2020), SciFact", "https://aclanthology.org/2020.emnlp-main.609/", "Scientific claim verification and rationales."),
        ("Min et al. (2023), FActScore", "https://aclanthology.org/2023.emnlp-main.741/", "Atomic factual precision as evaluation precedent."),
        ("Pirolli & Card (1999), Information Foraging", "https://doi.org/10.1037/0033-295X.106.4.643", "Resource-bounded search behavior."),
        ("Howard (1966), Information Value Theory", "https://doi.org/10.1109/TSSC.1966.300074", "Whether more information is worth its cost."),
        ("Metzger (2007), Credibility assessment", "https://doi.org/10.1002/asi.20672", "Contextual, multidimensional credibility assessment."),
        ("Horvitz (1999), Mixed-Initiative Interfaces", "https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/", "Uncertainty, timing, cost, and human control."),
        ("Amershi et al. (2019), Human-AI Interaction", "https://doi.org/10.1145/3290605.3300233", "Correction, control, and expectation management."),
        ("NIST AI RMF 1.0", "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10", "Enterprise governance context; not product validation."),
        ("Anthropic (2025), Context engineering", "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents", "Industry implementation context; not independent empirical support."),
    ]
    ref_rows = []
    for label, url, use in refs:
        safe_url = escape(url, {'"': '&quot;'})
        ref_rows.append([rich(f'<link href="{safe_url}" color="#1B6265"><u>{escape(label)}</u></link><br/><font size="6.7" color="#625D55">{escape(use)}</font>', styles["BodySmall"])])
    ref_table = Table(ref_rows, colWidths=[width])
    ref_table.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -2), .35, LINE), ("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT), ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm), ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm), ("TOPPADDING", (0, 0), (-1, -1), 3 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm)]))
    story.extend([ref_table, Spacer(1, 7 * mm)])

    story.extend([
        paragraph("10 · COMPACT GLOSSARY", styles["SectionKicker"]),
        paragraph("Interpretation guardrails", styles["SectionTitle"]),
    ])
    glossary = [
        ("Discrimination layer", "A proposed systems responsibility for deciding what context may influence generation; not a claim about one service, model, or novel mechanism."),
        ("Attention priority", "How urgently an item deserves inspection because of possible relevance or consequence; not truth probability."),
        ("Domain source authority", "Task- and claim-scoped standing to speak about a domain; not universal trust."),
        ("Claim support", "The relationship between exact evidence and a bounded proposition; not source popularity or citation presence."),
        ("Origin relation", "Whether observations share a known origin, are separately rooted as stipulated, or remain unresolved; it is not real-world epistemic independence."),
        ("Recurrence", "Repeated observation of a pattern; it does not establish distinct-origin support."),
        ("Relevance", "Usefulness to the current brief; not general importance, correctness, or permission."),
        ("Operational authorization", "Permission to acquire, process, disclose, retain, or act; not source competence or evidential support."),
        ("Enrichment value", "The expected benefit of another permitted operation considered with cost and risk; not action priority or acceptance."),
        ("Action priority", "The ordered permitted next step after consequence, uncertainty, cost, and authorization are considered; not a factual verdict."),
        ("Assessment attributes", "Uncertainty and possible consequence qualify judgments and routes; neither is an interchangeable master score."),
        ("Provenance", "A trace of identity, derivation, actors, and time; not proof that content is correct."),
        ("Signal candidate", "A derived pattern worth inspection; not a verified event or conclusion."),
        ("Owner disposition", "An accountable person’s recorded action or judgment; not external truth."),
    ]
    g_rows = []
    for index in range(0, len(glossary), 2):
        row = []
        for term, definition in glossary[index:index+2]:
            row.append([paragraph(term.upper(), styles["CardLabel"]), paragraph(definition, styles["BodySmall"])])
        if len(row) == 1:
            row.append([])
        g_rows.append(row)
    g_table = Table(g_rows, colWidths=[width / 2] * 2)
    g_table.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .4, LINE), ("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm), ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm), ("TOPPADDING", (0, 0), (-1, -1), 4 * mm), ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm)]))
    story.extend([
        g_table,
        Spacer(1, 10 * mm),
        StatusRule(width, TEAL, 4),
        Spacer(1, 8 * mm),
        paragraph("OWNER REVIEW PROMPT", styles["SectionKicker"]),
        paragraph("Does the framework make the hidden judgment easier to inspect—or merely more elaborate?", styles["SectionTitle"]),
        paragraph("The strongest current claim is deliberately modest: this is a coherent, historically grounded synthesis worth examining. It is not complete, empirically validated, or novel as a scientific mechanism. Current status: local owner review; not published.", styles["SectionLead"]),
    ])

    doc.build(story)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--framework", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build_pdf(args.framework, args.output)


if __name__ == "__main__":
    main()
