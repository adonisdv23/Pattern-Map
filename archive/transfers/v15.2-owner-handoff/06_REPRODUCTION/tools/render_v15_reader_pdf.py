#!/usr/bin/env python3
"""Render the v15.1 visual/print companion from canonical local artifacts.

The PDF is intentionally a visual companion. The semantic local HTML reader
and the Markdown source remain canonical, and no empirical result is implied.
"""

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
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    Image as RLImage,
    KeepTogether,
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

SERIF = "Times-Roman"
SERIF_BOLD = "Times-Bold"
SERIF_ITALIC = "Times-Italic"
SANS = "Helvetica"
SANS_BOLD = "Helvetica-Bold"


def register_fonts() -> None:
    """Register and embed readable serif and sans families when available."""
    global SERIF, SERIF_BOLD, SERIF_ITALIC, SANS, SANS_BOLD
    font_specs = {
        "V15Serif": Path("/System/Library/Fonts/Supplemental/Georgia.ttf"),
        "V15Serif-Bold": Path("/System/Library/Fonts/Supplemental/Georgia Bold.ttf"),
        "V15Serif-Italic": Path("/System/Library/Fonts/Supplemental/Georgia Italic.ttf"),
        "V15Sans": Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
        "V15Sans-Bold": Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
    }
    if all(path.is_file() for path in font_specs.values()):
        for name, path in font_specs.items():
            pdfmetrics.registerFont(TTFont(name, str(path)))
        pdfmetrics.registerFontFamily(
            "V15Serif",
            normal="V15Serif",
            bold="V15Serif-Bold",
            italic="V15Serif-Italic",
            boldItalic="V15Serif-Bold",
        )
        pdfmetrics.registerFontFamily(
            "V15Sans",
            normal="V15Sans",
            bold="V15Sans-Bold",
            italic="V15Sans",
            boldItalic="V15Sans-Bold",
        )
        SERIF = "V15Serif"
        SERIF_BOLD = "V15Serif-Bold"
        SERIF_ITALIC = "V15Serif-Italic"
        SANS = "V15Sans"
        SANS_BOLD = "V15Sans-Bold"


class V15DocTemplate(BaseDocTemplate):
    """A4 template with visible status on every page and PDF outline entries."""

    def __init__(self, filename: str, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="v15-reader-frame",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(PageTemplate(id="v15-reader", frames=[frame], onPage=self._decorate))
        self._outline_counter = 0

    def _decorate(self, canvas, doc):
        canvas.saveState()
        canvas.setFillColor(PAPER)
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        canvas.setFillColor(TEAL)
        canvas.rect(0, 0, 4.5 * mm, A4[1], fill=1, stroke=0)
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.45)
        canvas.line(self.leftMargin, 14.5 * mm, A4[0] - self.rightMargin, 14.5 * mm)
        canvas.setFont(SANS_BOLD, 5.8)
        canvas.setFillColor(CORAL)
        canvas.drawString(
            self.leftMargin,
            9.5 * mm,
            "UNTAGGED VISUAL/PRINT COMPANION · HTML IS CANONICAL · NO EMPIRICAL RESULTS",
        )
        canvas.setFillColor(MUTED)
        canvas.setFont(SANS, 6.3)
        canvas.drawRightString(A4[0] - self.rightMargin, 9.5 * mm, f"V15.1 · {doc.page:02d}")
        canvas.setTitle("Pattern Recognition: The Discrimination Layer — v15.1")
        canvas.setAuthor("Local owner-review package")
        canvas.setSubject("Visual companion to a conceptual synthesis and unrun research program")
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name == "SectionTitle":
            self._outline_counter += 1
            key = f"v15-section-{self._outline_counter}"
            title = flowable.getPlainText()
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(title, key, level=0, closed=False)


class Rule(Flowable):
    def __init__(self, width: float, color=TEAL, height: float = 4):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.height, fill=1, stroke=0)


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(escape(str(text)), style)


def rich(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text, style)


def image(path: Path, max_width: float, max_height: float) -> RLImage:
    flowable = RLImage(str(path))
    scale = min(max_width / flowable.imageWidth, max_height / flowable.imageHeight)
    flowable.drawWidth = flowable.imageWidth * scale
    flowable.drawHeight = flowable.imageHeight * scale
    flowable.hAlign = "CENTER"
    return flowable


def make_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "Eyebrow": ParagraphStyle(
            "Eyebrow", parent=base["Normal"], fontName=SANS_BOLD, fontSize=7,
            leading=9, tracking=1.1, textColor=TEAL, spaceAfter=4 * mm,
        ),
        "CoverTitle": ParagraphStyle(
            "CoverTitle", parent=base["Title"], fontName=SERIF, fontSize=39,
            leading=41, alignment=TA_LEFT, textColor=INK, spaceAfter=1.5 * mm,
        ),
        "CoverAccent": ParagraphStyle(
            "CoverAccent", parent=base["Title"], fontName=SERIF_ITALIC,
            fontSize=35, leading=39, alignment=TA_LEFT, textColor=TEAL,
            spaceAfter=7 * mm,
        ),
        "Subtitle": ParagraphStyle(
            "Subtitle", parent=base["Normal"], fontName=SERIF_ITALIC,
            fontSize=14, leading=20, textColor=MUTED, spaceAfter=6 * mm,
        ),
        "SectionKicker": ParagraphStyle(
            "SectionKicker", parent=base["Normal"], fontName=SANS_BOLD,
            fontSize=7, leading=9, tracking=1, textColor=TEAL, spaceAfter=2.5 * mm,
        ),
        "SectionTitle": ParagraphStyle(
            "SectionTitle", parent=base["Heading1"], fontName=SERIF,
            fontSize=26, leading=30, textColor=INK, spaceAfter=4 * mm,
            keepWithNext=True,
        ),
        "SectionLead": ParagraphStyle(
            "SectionLead", parent=base["Normal"], fontName=SERIF,
            fontSize=11.7, leading=16.5, textColor=MUTED, spaceAfter=5 * mm,
        ),
        "Thesis": ParagraphStyle(
            "Thesis", parent=base["Normal"], fontName=SERIF,
            fontSize=15.5, leading=21, textColor=INK, spaceAfter=2 * mm,
        ),
        "CardTitle": ParagraphStyle(
            "CardTitle", parent=base["Heading3"], fontName=SERIF_BOLD,
            fontSize=12.2, leading=15, textColor=INK, spaceAfter=1.5 * mm,
            keepWithNext=True,
        ),
        "CardLabel": ParagraphStyle(
            "CardLabel", parent=base["Normal"], fontName=SANS_BOLD,
            fontSize=6.2, leading=8, tracking=.65, textColor=TEAL,
            spaceAfter=1.5 * mm,
        ),
        "CardLabelInverse": ParagraphStyle(
            "CardLabelInverse", parent=base["Normal"], fontName=SANS_BOLD,
            fontSize=6.2, leading=8, tracking=.65,
            textColor=colors.HexColor("#C7E0DF"), spaceAfter=1.5 * mm,
        ),
        "Body": ParagraphStyle(
            "Body", parent=base["BodyText"], fontName=SERIF,
            fontSize=9.1, leading=13.3, textColor=INK, spaceAfter=2.5 * mm,
        ),
        "BodySmall": ParagraphStyle(
            "BodySmall", parent=base["BodyText"], fontName=SANS,
            fontSize=7.6, leading=10.8, textColor=MUTED, spaceAfter=1.7 * mm,
        ),
        "BodyTiny": ParagraphStyle(
            "BodyTiny", parent=base["BodyText"], fontName=SANS,
            fontSize=6.45, leading=8.5, textColor=MUTED, spaceAfter=1 * mm,
        ),
        "BodyInverse": ParagraphStyle(
            "BodyInverse", parent=base["BodyText"], fontName=SERIF,
            fontSize=10.5, leading=15, textColor=colors.white, spaceAfter=2 * mm,
        ),
        "BigNumber": ParagraphStyle(
            "BigNumber", parent=base["Normal"], fontName=SERIF_BOLD,
            fontSize=24, leading=26, textColor=INK, spaceAfter=1 * mm,
        ),
        "Quote": ParagraphStyle(
            "Quote", parent=base["Normal"], fontName=SERIF_ITALIC,
            fontSize=15, leading=21, textColor=TEAL, leftIndent=6 * mm,
            rightIndent=6 * mm, spaceBefore=2 * mm, spaceAfter=5 * mm,
        ),
        "CenterTiny": ParagraphStyle(
            "CenterTiny", parent=base["Normal"], fontName=SANS,
            fontSize=6.3, leading=8.5, alignment=TA_CENTER, textColor=MUTED,
        ),
    }


def card(content, width: float, border=LINE, background=PAPER_LIGHT, padding=4 * mm):
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


def grid(rows, widths, *, header=True, font_style=None, header_style=None):
    table = Table(rows, colWidths=widths, repeatRows=1 if header else 0)
    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), .35, LINE),
        ("BACKGROUND", (0, 0), (-1, 0), PAPER_DEEP if header else PAPER_LIGHT),
        ("BACKGROUND", (0, 1 if header else 0), (-1, -1), PAPER_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 2.1 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.1 * mm),
    ]))
    return table


def bullets(items: list[str], styles, color=TEAL):
    return [
        rich(
            f'<font name="{SANS_BOLD}" color="{color.hexval()}">•</font>&nbsp;&nbsp;{escape(item)}',
            styles["BodySmall"],
        )
        for item in items
    ]


def section(story, number: str, title: str, lead: str, styles):
    story.extend([
        p(number, styles["SectionKicker"]),
        p(title, styles["SectionTitle"]),
        p(lead, styles["SectionLead"]),
    ])


def two_cards(left, right, width: float, gap: float = 5 * mm):
    col = (width - gap) / 2
    table = Table([[left(col), right(col)]], colWidths=[col, col])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), gap),
        ("RIGHTPADDING", (1, 0), (1, 0), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return table


def component_card(component: dict, styles, width: float):
    color = FAMILY_COLORS[component["family_id"]]
    failures = "; ".join(component["known_failure_modes"][:2])
    content = [
        rich(
            f'<font color="{color.hexval()}"><b>{escape(component["id"])} · {escape(component["family_id"])}</b></font>',
            styles["CardLabel"],
        ),
        p(component["name"], styles["CardTitle"]),
        p(component["what_it_is"], styles["BodySmall"]),
        rich(f'<b>Failure watch:</b> {escape(failures)}', styles["BodyTiny"]),
        rich(
            f'<b>Evidence status:</b> {escape(component["evidence_basis"]["maturity"].replace("_", " ").title())}',
            styles["BodyTiny"],
        ),
    ]
    return card(content, width, border=color, padding=3.2 * mm)


def build_pdf(framework_path: Path, output_path: Path) -> None:
    register_fonts()
    styles = make_styles()
    framework = json.loads(framework_path.read_text(encoding="utf-8"))
    repo_root = framework_path.resolve().parent.parent
    v13_image = repo_root / "site/public/images/v13-six-families-origin-map.png"
    example_image = repo_root / "site/public/images/nine-mentions-one-origin.jpg"
    for required in (v13_image, example_image):
        if not required.is_file():
            raise FileNotFoundError(f"Required visual asset missing: {required}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc = V15DocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=19 * mm,
        rightMargin=15 * mm,
        topMargin=17 * mm,
        bottomMargin=20 * mm,
        title="Pattern Recognition: The Discrimination Layer — v15.1",
        author="Local owner-review package",
        subject="Visual companion to a conceptual synthesis and unrun research program",
    )
    width = doc.width
    story: list[Flowable] = []

    # 01 — Cover
    story.extend([
        Spacer(1, 13 * mm),
        p("PERSONAL SYSTEMS MEMO · V15.1 · LOCAL OWNER REVIEW", styles["Eyebrow"]),
        p("Pattern Recognition /", styles["CoverTitle"]),
        p("The Discrimination Layer", styles["CoverAccent"]),
        p(
            "Why repeated reports can still amount to one origin—and what an AI system should preserve before it generates.",
            styles["Subtitle"],
        ),
        Rule(width, TEAL, 4),
        Spacer(1, 8 * mm),
        card([
            p("WORKING PROPOSITION · CONCEPTUAL SYNTHESIS", styles["CardLabel"]),
            rich('<font color="#1B6265"><b>Make the judgment before generation visible.</b></font>', styles["Thesis"]),
            p(
                "An AI answer inherits earlier choices about what was found, treated as separate evidence, allowed to influence the answer, or left out. Those choices should be visible and correctable. Whether that visibility improves outcomes enough to justify its cost is the empirical question—not a conclusion.",
                styles["Thesis"],
            ),
        ], width, border=TEAL, padding=6 * mm),
        Spacer(1, 7 * mm),
        card([
            p("TERM BOUNDARY", styles["CardLabel"]),
            p(
                "Discrimination means technical differentiation among information and possible actions—not social classification and not a model discriminator.",
                styles["Body"],
            ),
        ], width, border=CORAL),
        Spacer(1, 6 * mm),
        rich('<font color="#9C4233"><b>NO STUDY RUN · NO EMPIRICAL RESULTS · NOT PUBLISHED</b></font>', styles["BodySmall"]),
        p("The semantic local HTML reader is the canonical accessible surface. This PDF is an untagged visual/print companion.", styles["BodySmall"]),
        PageBreak(),
    ])

    # 02 — Reading contract
    section(
        story,
        "00 · READING CONTRACT",
        "Two tracks, one visible truth boundary",
        "Read the essay for the argument; use the Lab to inspect the unrun protocol. The two surfaces meet at the same receipt and never blur concept with result.",
        styles,
    )
    story.append(two_cards(
        lambda col: card([
            p("ESSAY + EXPLORE", styles["CardLabel"]),
            p("The conceptual track", styles["CardTitle"]),
            *bullets([
                "A concrete counting error and an exact fictional receipt.",
                "Six mechanism families and eleven inspectable responsibilities.",
                "Verified precedents, objections, retirement tests, and limits.",
            ], styles),
        ], col, border=TEAL),
        lambda col: card([
            p("LAB", styles["CardLabel"]),
            p("The empirical track", styles["CardTitle"]),
            *bullets([
                "One frozen-model supplied-cue question; F0/F1/F2 only.",
                "Fixed synthetic denominators, endpoints, stop gates, and null handling.",
                "Optional natural-syndication T1 stays descriptive and separate.",
            ], styles, BLUE),
        ], col, border=BLUE),
        width,
    ))
    story.extend([
        Spacer(1, 7 * mm),
        card([
            p("MAXIMUM CURRENT CLAIM", styles["CardLabel"]),
            p(
                "V15.1 improves the conceptual synthesis and execution readiness. It does not establish provenance discovery, real-world independence, factual correctness, human benefit, field transfer, or a validated mechanism.",
                styles["Thesis"],
            ),
        ], width, border=INK, padding=5 * mm),
        Spacer(1, 6 * mm),
        p("Suggested owner path", styles["CardTitle"]),
        grid([
            [p("TIME", styles["CardLabel"]), p("INSPECT", styles["CardLabel"]), p("DECIDE", styles["CardLabel"])],
            [p("60–90 sec", styles["BodySmall"]), p("Opening and counting error", styles["BodySmall"]), p("Can you restate the core idea in plain language?", styles["BodySmall"])],
            [p("About 5 min", styles["BodySmall"]), p("Essential argument and receipt", styles["BodySmall"]), p("Does the thesis survive the example?", styles["BodySmall"])],
            [p("15–20 min", styles["BodySmall"]), p("Map, components, objections", styles["BodySmall"]), p("Is the synthesis useful enough to keep?", styles["BodySmall"])],
            [p("30–45+ min", styles["BodySmall"]), p("Lab, sources, and technical records", styles["BodySmall"]), p("Is the research program worth its remaining gates?", styles["BodySmall"])],
        ], [25 * mm, 66 * mm, width - 91 * mm]),
        PageBreak(),
    ])

    # 03 — Opening
    section(
        story,
        "01 · THE COUNTING ERROR",
        "Nine reports can still amount to one origin.",
        "Different headlines, layouts, and wording do not create new roots. The reports may remain useful observations, but recurrence cannot silently become corroboration.",
        styles,
    )
    story.extend([
        card([
            p("THE FLAT SUMMARY SAYS", styles["CardLabelInverse"]),
            rich('<font color="#FFFFFF"><b>“Nine sources agree that the new tool is broadly validated.”</b></font>', styles["BodyInverse"]),
        ], width, border=INK, background=INK, padding=5 * mm),
        Spacer(1, 5 * mm),
    ])
    stat_col = width / 4
    stats = Table([[
        [p("OBSERVATIONS", styles["CardLabel"]), p("09", styles["BigNumber"]), p("preserved", styles["BodyTiny"])],
        [p("KNOWN CLUSTER", styles["CardLabel"]), p("01", styles["BigNumber"]), p("Origin A", styles["BodyTiny"])],
        [p("SUPPORT ORIGINS", styles["CardLabel"]), p("00", styles["BigNumber"]), p("for this broad claim", styles["BodyTiny"])],
        [p("DISPOSITION", styles["CardLabel"]), p("HOLD", styles["CardTitle"]), p("verify another relation", styles["BodyTiny"])],
    ]], colWidths=[stat_col] * 4)
    stats.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), .4, LINE),
        ("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 3 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
    ]))
    story.extend([
        stats,
        Spacer(1, 6 * mm),
        p("What changed in the bad summary", styles["CardTitle"]),
        *bullets([
            "Nine report observations became nine apparent origin paths.",
            "Apparent plurality became support for a broader claim.",
            "The unknown relationship between origin, stance, and claim disappeared.",
            "A fluent answer concealed the earlier accounting decision.",
        ], styles, CORAL),
        Spacer(1, 4 * mm),
        rich('<b>The correction is not “count less.”</b> It is: count the right unit under a stated rule, preserve the reports, and keep unresolved lineage unresolved.', styles["Quote"]),
        card([
            p("NEXT PERMITTED STEP", styles["CardLabel"]),
            p("Inspect the launch announcement; seek a separately authored benchmark or failure report; record its origin relation; then assess the exact claim it supports or refutes.", styles["Body"]),
        ], width, border=TEAL),
        PageBreak(),
    ])

    # 04 — Exact receipt
    section(
        story,
        "02 · FICTIONAL RECEIPT · ORIGIN-EX-01",
        "Preserve observations without inventing support.",
        "This is a static illustration, not a dataset, provenance audit, or runtime. Rows are unordered and all nine report records remain visible.",
        styles,
    )
    receipt_rows = [[
        p("RECORD", styles["CardLabel"]),
        p("KIND", styles["CardLabel"]),
        p("DECLARED RELATION", styles["CardLabel"]),
        p("ACCOUNTING", styles["CardLabel"]),
    ]]
    for index in range(1, 10):
        receipt_rows.append([
            p(f"O{index:02d}", styles["BodyTiny"]),
            p("Report observation", styles["BodyTiny"]),
            rich('Origin A · <font color="#5C467D"><b>DEPENDENT</b></font>', styles["BodyTiny"]),
            p("Preserve; not separately rooted support under this rule.", styles["BodyTiny"]),
        ])
    story.extend([
        grid(receipt_rows, [17 * mm, 37 * mm, 46 * mm, width - 100 * mm]),
        Spacer(1, 5 * mm),
        two_cards(
            lambda col: card([
                p("RELATION STATES", styles["CardLabel"]),
                rich('<b>DPND</b> · traceable to another observed path<br/><b>INDP</b> · separate origin by benchmark stipulation only<br/><b>UNKN</b> · unresolved; never guess<br/><b>NONE</b> · no relation value supplied', styles["BodySmall"]),
            ], col, border=VIOLET),
            lambda col: card([
                p("CLAIM STATE", styles["CardLabel"]),
                p("INSUFFICIENT", styles["CardTitle"]),
                p("Origin A exists, but its stance toward “broadly validated” has not been established. B1 and C1 are contrast roots with support unassessed.", styles["BodySmall"]),
            ], col, border=CORAL),
            width,
        ),
        Spacer(1, 5 * mm),
        card([
            p("HUMAN DISPOSITION", styles["CardLabel"]),
            p("HOLD · VERIFY ANOTHER ORIGIN RELATION", styles["CardTitle"]),
            p("No automatic admission, rejection, truth verdict, or provenance discovery.", styles["BodySmall"]),
        ], width, border=INK, padding=4 * mm),
        PageBreak(),
    ])

    # 05 — Distinctions
    section(
        story,
        "03 · DISTINCTION CONTRACT",
        "Keep unlike judgments unlike.",
        "The point is error visibility, not one schema per concept. When distinctions collapse, the system loses the ability to explain where a bad route began.",
        styles,
    )
    distinctions = [
        ("Source identity", "Artifact identity", "One source can publish many artifacts; one artifact can move."),
        ("Provenance", "Correctness", "A false claim can have perfect lineage."),
        ("Recurrence", "Corroboration", "Copies can recur without a new root."),
        ("Origin relation", "Claim support", "A separate root can be irrelevant; a copy can contain a useful span."),
        ("Source authority", "Universal trust", "Authority is claim-, role-, domain-, and time-scoped."),
        ("Claim support", "Citation presence", "A citation can be irrelevant, contradictory, or too broad."),
        ("Relevance", "General importance", "Relevance belongs to the current decision."),
        ("Technical access", "Authorization", "Reachability is not permission to use or retain."),
        ("Enrichment value", "Action priority", "More learning can help without being the next permitted step."),
        ("Action priority", "Truth", "A sandbox step is a decision, not a factual verdict."),
        ("Owner disposition", "External fact", "Accept, defer, and override are accountable choices."),
        ("Outcome", "Retroactive truth", "A later result updates policy; it does not rewrite history."),
    ]
    drows = [[p("KEEP SEPARATE", styles["CardLabel"]), p("DO NOT SUBSTITUTE", styles["CardLabel"]), p("WHY", styles["CardLabel"])]]
    drows.extend([[p(a, styles["BodyTiny"]), p(b, styles["BodyTiny"]), p(c, styles["BodyTiny"])] for a, b, c in distinctions])
    story.extend([
        grid(drows, [39 * mm, 43 * mm, width - 82 * mm]),
        Spacer(1, 5 * mm),
        card([
            p("D04 · ORIGIN RELATION", styles["CardLabel"]),
            p("Shared known origin · unresolved · separately rooted by stipulation", styles["CardTitle"]),
            p("The historical `independence` label remains a compatibility alias. V15.1 does not equate this field with real-world causal, editorial, methodological, or epistemic independence.", styles["BodySmall"]),
        ], width, border=VIOLET),
        PageBreak(),
    ])

    # 06 — History
    section(
        story,
        "04 · HISTORICAL ORIGIN",
        "Preserve v13; do not mistake it for current topology.",
        "The recovered diagram is historical evidence of the concept’s origin. V15.1 keeps it unchanged and renders the current architecture in live text and structured records.",
        styles,
    )
    story.extend([
        image(v13_image, width, 144 * mm),
        Spacer(1, 4 * mm),
        grid([
            [p("ARTIFACT", styles["CardLabel"]), p("STATUS", styles["CardLabel"]), p("BOUNDARY", styles["CardLabel"])],
            [p("v13 diagram PNG", styles["BodyTiny"]), p("Exact hash verified", styles["BodyTiny"]), p("1024×1536; SHA-256 8a8204…3ae; immutable historical anchor", styles["BodyTiny"])],
            [p("Rendered DOM snapshot", styles["BodyTiny"]), p("Reference capture", styles["BodyTiny"]), p("Useful rendered state; not the original standalone source", styles["BodyTiny"])],
            [p("Standalone v13 HTML", styles["BodyTiny"]), p("Unavailable", styles["BodyTiny"]), p("Expected byte identity remains unverified", styles["BodyTiny"])],
        ], [43 * mm, 37 * mm, width - 80 * mm]),
        PageBreak(),
    ])

    # 07 — Six families
    section(
        story,
        "05 · CURRENT ARCHITECTURE",
        "Six mechanism families; two loops; one preserved history.",
        "The map is a reviewable decomposition, not a maturity model, a required service topology, or a proven minimum.",
        styles,
    )
    family_cells = []
    for family in framework["mechanism_families"]:
        color = FAMILY_COLORS[family["id"]]
        family_cells.append(lambda col, f=family, c=color: card([
            rich(f'<font color="{c.hexval()}"><b>{escape(f["id"])}</b></font>', styles["CardLabel"]),
            p(f["name"], styles["CardTitle"]),
            p(f["purpose"], styles["BodyTiny"]),
            p("Components · " + ", ".join(f["component_ids"]), styles["BodyTiny"]),
        ], col, border=c, padding=3.3 * mm))
    for row_start in range(0, 6, 2):
        story.extend([two_cards(family_cells[row_start], family_cells[row_start + 1], width), Spacer(1, 4 * mm)])
    story.extend([
        Spacer(1, 2 * mm),
        grid([
            [p("FAST EVIDENCE LOOP", styles["CardLabel"]), p("SLOW LEARNING LOOP", styles["CardLabel"])],
            [p("Brief → acquire → identify → relate → assess → route → package → owner disposition", styles["BodySmall"]), p("Used packet → defined outcome → comparison → proposed update → human approval → new version", styles["BodySmall"])],
            [p("Returns to acquisition when a consequential gap warrants bounded search.", styles["BodyTiny"]), p("Never silently rewrites observations, prior decisions, or policy history.", styles["BodyTiny"])],
        ], [width / 2, width / 2]),
        PageBreak(),
    ])

    # 08–10 — Components
    component_groups = [
        ("06 · COMPONENT RECORDS · C01–C04", "From intent to origin-aware relationships", framework["components"][:4]),
        ("07 · COMPONENT RECORDS · C05–C08", "From exact claims to a bounded context packet", framework["components"][4:8]),
        ("08 · COMPONENT RECORDS · C09–C11", "From human correction to revisable learning", framework["components"][8:11]),
    ]
    for kicker, title, group in component_groups:
        section(
            story,
            kicker,
            title,
            "Every card names a responsibility, a failure watch, and its evidence maturity. The complete canonical specification remains in the HTML and machine-readable map.",
            styles,
        )
        for start in range(0, len(group), 2):
            pair = group[start:start + 2]
            if len(pair) == 2:
                story.extend([
                    two_cards(
                        lambda col, comp=pair[0]: component_card(comp, styles, col),
                        lambda col, comp=pair[1]: component_card(comp, styles, col),
                        width,
                    ),
                    Spacer(1, 4 * mm),
                ])
            else:
                story.extend([component_card(pair[0], styles, width), Spacer(1, 4 * mm)])
        if kicker.startswith("08"):
            story.extend([
                Spacer(1, 2 * mm),
                card([
                    p("MINIMUM IMPLEMENTATION CLAIM", styles["CardLabel"]),
                    p("Task and permission framing; identity and provenance; claim and relationship representation; separate assessment dimensions; bounded routing; human correction; versioned outcome feedback whenever learning is claimed.", styles["Body"]),
                ], width, border=INK),
            ])
        story.append(PageBreak())

    # 11 — Worked application
    section(
        story,
        "09 · WORKED APPLICATION",
        "What changes after the receipt?",
        "The illustration is not another telling of the nine-report example. It shows how a corrected accounting record changes the next permitted action without deciding truth.",
        styles,
    )
    story.extend([
        image(example_image, width, 86 * mm),
        Spacer(1, 4 * mm),
        grid([
            [p("BEFORE", styles["CardLabel"]), p("CORRECTION", styles["CardLabel"]), p("AFTER", styles["CardLabel"])],
            [p("Nine appearances were summarized as nine supporting sources.", styles["BodySmall"]), p("All nine are linked to Origin A; support for the broad claim remains unassessed.", styles["BodySmall"]), p("The route changes from premature acceptance to HOLD plus one bounded verification step.", styles["BodySmall"])],
            [p("Unknowns disappeared in prose.", styles["BodySmall"]), p("UNKN remains a first-class relation state.", styles["BodySmall"]), p("The packet states what is missing and when to stop.", styles["BodySmall"])],
        ], [width / 3] * 3),
        Spacer(1, 5 * mm),
        card([
            p("DECISION IMPLICATION", styles["CardLabel"]),
            p("A sandbox pilot can be authorized without endorsing “broadly validated.” Permission, evidence status, and action priority remain different records.", styles["Thesis"]),
        ], width, border=CORAL),
        p("E2 is a labeled AI-generated illustration. It is not a dataset, finding, independent validation, or required interpretive evidence.", styles["BodyTiny"]),
        PageBreak(),
    ])

    # 12 — Prior art
    section(
        story,
        "10 · VERIFIED PRIOR ART",
        "The closest precedents remove the broad novelty claim.",
        "V15.1 keeps the contribution narrow by distinguishing established mechanisms, direct comparators, adjacent methods, and the remaining supplied-cue experiment.",
        styles,
    )
    prior_rows = [[p("PRECEDENT", styles["CardLabel"]), p("WHAT IT ESTABLISHES", styles["CardLabel"]), p("WHAT IT BLOCKS", styles["CardLabel"])]]
    prior = [
        ("Dong et al. · VLDB 2009", "Copying-aware truth discovery and source dependence.", "No novelty claim for dependence-aware aggregation."),
        ("Zhang, Ives & Roth · ACL 2020", "Natural-language claim-provenance graphs with inferred source/statement relations.", "Closest direct precedent; supplied oracle cues must be distinguished from provenance inference."),
        ("Senn · BMC MRM 2009", "Shared studies or analyses can be double-counted.", "No novelty claim for choosing an effective evidence unit."),
        ("Cochrane Handbook · current", "Multiple reports must be collated around the underlying study.", "No novelty claim for preserving reports while avoiding study double count."),
        ("Greenberg · BMJ 2009", "Citation practices can amplify an unsupported claim into apparent authority.", "Citation count is not independent corroboration."),
        ("NEWS-COPY · arXiv 2022", "Same-original duplicates under abridgement and OCR noise.", "No novelty claim for noisy duplicate grouping."),
        ("Newswire · NeurIPS 2024", "Historical reproduction clusters separate appearances from reproduced articles.", "Outlet recurrence cannot be equated with perspectives or truth."),
        ("MMR / SetR / NEST / RARE / Schelpe", "Diversity-aware, set-wise, redundancy-sensitive retrieval, and byte-exact deduplication precedents.", "No novelty claim for redundancy penalties, joint set selection, or exact duplicate removal."),
        ("Strittmatter et al. · 2024", "Human judgments of evidential dependence in fictitious scenarios.", "Human sensitivity and effective-independence questions have direct precedent."),
    ]
    prior_rows.extend([[p(a, styles["BodyTiny"]), p(b, styles["BodyTiny"]), p(c, styles["BodyTiny"])] for a, b, c in prior])
    story.extend([
        grid(prior_rows, [43 * mm, 62 * mm, width - 105 * mm]),
        Spacer(1, 4 * mm),
        card([
            p("NOVELTY DISCIPLINE", styles["CardLabel"]),
            p("The project does not introduce copying detection, deduplication, claim graphs, diversity retrieval, conflict handling, or evidence-unit accounting.", styles["Body"]),
        ], width, border=CORAL),
        PageBreak(),
    ])

    # 13 — Current RAG adjacency and residual claim
    section(
        story,
        "11 · CLOSEST CURRENT COMPARATORS",
        "What remains after RAG and provenance work are credited?",
        "Several current manuscripts are useful comparisons, but publication status, task mismatch, and origin-ground-truth limits stay visible.",
        styles,
    )
    current = [
        ("RAMDocs", "Conflicting-evidence robustness", "Adjacent; not origin accounting"),
        ("Li, Padman & Krishnan", "Cross-institution source-set answer variation", "Unreviewed manuscript; source answers are not derivation"),
        ("EvidentialRAG", "Conflict and uncertainty fusion", "Unreviewed manuscript; not oracle-origin cue isolation"),
        ("Naphade", "Distinct vs paraphrased opposing evidence", "Unreviewed; distinct documents are not verified origins"),
        ("Ross et al.", "Exact duplicate, paraphrase, and diverse retrieval sets", "Unreviewed; different estimand and no real-world origin proof"),
    ]
    crows = [[p("WORK", styles["CardLabel"]), p("DIRECT VALUE", styles["CardLabel"]), p("BOUNDARY", styles["CardLabel"])]]
    crows.extend([[p(a, styles["BodySmall"]), p(b, styles["BodySmall"]), p(c, styles["BodySmall"])] for a, b, c in current])
    story.extend([
        grid(crows, [39 * mm, 56 * mm, width - 95 * mm]),
        Spacer(1, 7 * mm),
        card([
            p("RESIDUAL CONCEPTUAL CONTRIBUTION", styles["CardLabel"]),
            p("A boundary-preserving synthesis that makes identity, origin relation, claim support, permission, cost, routing, and human disposition jointly inspectable before generation.", styles["Thesis"]),
        ], width, border=TEAL, padding=5 * mm),
        Spacer(1, 5 * mm),
        card([
            p("RESIDUAL EMPIRICAL QUESTION", styles["CardLabel"]),
            p("Does a supplied typed origin cue change origin counting beyond an explicit rule when evidence, prompt budget, model, and output contract are held fixed?", styles["Thesis"]),
            p("This is not provenance discovery, a new RAG architecture, or broad mechanism novelty.", styles["BodySmall"]),
        ], width, border=BLUE, padding=5 * mm),
        PageBreak(),
    ])

    # 14 — Objections and retirement
    section(
        story,
        "12 · ADVERSARIAL READING",
        "The strongest objections are design requirements.",
        "A defensible framework states how it can fail, when simpler methods should win, and when the name or decomposition should be retired.",
        styles,
    )
    objections = [
        ("Old work under a new label", "Credit mature provenance, evidence-synthesis, retrieval, HCI, and learning literatures; keep only synthesis and narrow tests."),
        ("A gatekeeper in quality-control clothing", "Expose exclusions, unknowns, permissions, appeal, and source coverage; let correction change the packet."),
        ("Provenance as rigor theater", "Require each receipt field to change a consequential route or remove it."),
        ("More costly than the error", "Compare against strong simple retrieval-plus-citation baselines under matched cost."),
        ("Decorative human review", "Expose exact spans, relations, omissions, and reasons; measure whether people can correct them."),
        ("Feedback optimizes the wrong proxy", "Predefine target, horizon, exposure, confounders, and approval; never silently update."),
        ("The name does harm", "Test reader comprehension and prefer Context Judgment Layer if the technical definition fails."),
    ]
    orows = []
    for index in range(0, len(objections), 2):
        row = []
        for title, answer in objections[index:index + 2]:
            row.append([p(title, styles["CardTitle"]), p(answer, styles["BodySmall"])])
        if len(row) == 1:
            row.append([])
        orows.append(row)
    otable = Table(orows, colWidths=[width / 2] * 2)
    otable.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), .4, LINE),
        ("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 4 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
    ]))
    story.extend([
        otable,
        Spacer(1, 5 * mm),
        card([
            p("RETIRE FOR A TASK WHEN…", styles["CardLabel"]),
            p("A simpler baseline performs equivalently at lower cost; the distinctions are not usable; origin grouping suppresses valid convergence; review and permissions become ceremonial; feedback amplifies contaminated proxies; or the name continues to misstate the thesis.", styles["Body"]),
        ], width, border=CORAL),
        PageBreak(),
    ])

    # 15 — Conditions
    section(
        story,
        "13 · LAB · ONE QUESTION · NO RESULTS",
        "Do supplied origin labels add anything beyond a plain counting rule?",
        "The same frozen model would receive the same fictional evidence in three matched versions. No model has been selected and no study has been run.",
        styles,
    )
    condition_rows = [[p("VERSION", styles["CardLabel"]), p("WHAT CHANGES", styles["CardLabel"]), p("ORIGIN CLUE", styles["CardLabel"]), p("ROLE", styles["CardLabel"])], [
        p("F0", styles["CardTitle"]), p("Ordinary evidence assessment", styles["BodySmall"]), p("Not shown", styles["BodySmall"]), p("Secondary baseline", styles["BodySmall"]),
    ], [
        p("F1", styles["CardTitle"]), p("Same evidence plus an explicit origin-counting rule", styles["BodySmall"]), p("Not shown", styles["BodySmall"]), p("Rule-only comparator", styles["BodySmall"]),
    ], [
        p("F2", styles["CardTitle"]), p("Same rule and evidence plus supplied relationship labels", styles["BodySmall"]), p("Shared / separate in test / unknown", styles["BodySmall"]), p("Supplied-cue condition", styles["BodySmall"]),
    ]]
    story.extend([
        grid(condition_rows, [21 * mm, 67 * mm, 48 * mm, width - 136 * mm]),
        Spacer(1, 6 * mm),
        card([
            p("MAIN COMPARISON", styles["CardLabel"]),
            rich('<b>Compare F2 with F1</b> across 300 planned primary test cases. This isolates the supplied labels from the rule itself.', styles["Thesis"]),
            p("F0 is descriptive. The optional real-world check called T1 is separate. Invalid answers still count instead of disappearing from the analysis.", styles["BodySmall"]),
        ], width, border=BLUE, padding=5 * mm),
        Spacer(1, 5 * mm),
        card([
            p("PARITY LOCK", styles["CardLabel"]),
            p("F1/F2 must preserve exact report bytes and order, exact input-byte length, exact system and instruction bytes, and exact token count under the selected frozen tokenizer. The local regex tokenizer is only a development surrogate.", styles["Body"]),
        ], width, border=VIOLET),
        PageBreak(),
    ])

    # 16 — Corpus and endpoints
    section(
        story,
        "14 · CORPUS + ENDPOINTS",
        "Fixed denominators make failure visible.",
        "The generator is deterministic, fictional, and offline. The plan contains 300 primary test cases (N=300). That is a sample size, not a result or confidence score.",
        styles,
    )
    corpus_rows = [[p("SPLIT", styles["CardLabel"]), p("TOTAL", styles["CardLabel"]), p("ONE ORIGIN", styles["CardLabel"]), p("MULTIPLE", styles["CardLabel"]), p("UNKNOWN", styles["CardLabel"]), p("CONFLICT", styles["CardLabel"])]]
    for split, total in [("dev", 80), ("pilot", 40), ("primary", 300), ("stress", 60)]:
        quarter = total // 4
        corpus_rows.append([p(split, styles["BodySmall"]), p(str(total), styles["BodySmall"]), p(str(quarter), styles["BodySmall"]), p(str(quarter), styles["BodySmall"]), p(str(quarter), styles["BodySmall"]), p(str(quarter), styles["BodySmall"])])
    story.extend([
        grid(corpus_rows, [31 * mm, 22 * mm, 29 * mm, 29 * mm, 29 * mm, width - 140 * mm]),
        Spacer(1, 6 * mm),
        two_cards(
            lambda col: card([
                p("MAIN MEASURE · FC_cons", styles["CardLabel"]),
                p("False corroboration", styles["CardTitle"]),
                p("Risk = invalid output, or a valid count of at least two supporting origins when the manifest certifies none/single or withholds certification as unknown.", styles["BodySmall"]),
                rich('<b>Denominator:</b> all 300 assigned primary test cases.', styles["BodyTiny"]),
            ], col, border=CORAL),
            lambda col: card([
                p("SAFETY CHECK · VOR", styles["CardLabel"]),
                p("Valid-origin recall", styles["CardTitle"]),
                p("On the frozen multiple-origin subset, a valid output must count at least two supporting origins and cite evidence spanning at least two stipulated support roots.", styles["BodySmall"]),
                rich('<b>Margin:</b> paired lower bound must exceed −0.05.', styles["BodyTiny"]),
            ], col, border=SAGE),
            width,
        ),
        Spacer(1, 5 * mm),
        card([
            p("UNKNOWN-ORIGIN TRUTH BOUNDARY", styles["CardLabel"]),
            p("Every prompt-visible value is UNKN. A valid assertion of two or more paths is conservatively risk-coded because the relation is uncertified—not because the latent world is known to contain zero or one origin.", styles["Body"]),
        ], width, border=VIOLET),
        PageBreak(),
    ])

    # 17 — Analysis and gates
    section(
        story,
        "15 · ANALYSIS + STOP GATES",
        "A favorable number is insufficient without a valid route to it.",
        "The confirmatory decision has one superiority test and one safety gate. Everything else is descriptive or diagnostic.",
        styles,
    )
    story.extend([
        grid([
            [p("PRIMARY DECISION", styles["CardLabel"]), p("SAFETY DECISION", styles["CardLabel"])],
            [p("Beneficial F2−F1 paired risk difference; exact two-sided McNemar/binomial p<.05; 95% paired bootstrap interval upper bound below 0; N=300.", styles["BodySmall"]), p("On fixed M, report F1/F2 VOR, delta, membership hash, and prespecified one-sided 95% lower bound; pass only above −0.05.", styles["BodySmall"])],
            [p("Report whether the −0.08 planning benchmark was reached; it is not another hidden test.", styles["BodyTiny"]), p("Interval method and coverage must be frozen and simulated at actual |M| before preregistration.", styles["BodyTiny"])],
        ], [width / 2, width / 2]),
        Spacer(1, 5 * mm),
        p("Fail closed before any empirical run", styles["CardTitle"]),
        *bullets([
            "Corpus integrity: exact hashes, split-family isolation, graph invariants, and all-UNKN prompt invariant.",
            "Prompt parity: exact bytes, order, instruction fields, and intended-tokenizer equality.",
            "Leakage: blocked surface classifier with frozen ceiling and interval; semantic audit with adjudication.",
            "Execution receipt: exact model/checkpoint/tokenizer/runtime/hardware/decoding plus immutable raw bytes and hashes.",
            "Analysis lock: A=300, fixed M, 10,000-resample primary interval, declared safety interval, coverage simulations.",
        ], styles, CORAL),
        Spacer(1, 4 * mm),
        card([
            p("CURRENT STOP LINE", styles["CardLabel"]),
            p("No model or tokenizer is selected; no pilot or primary output exists; no preregistration, participant, provider, deployment, or publication is authorized. Offline readiness does not cross that line.", styles["Body"]),
        ], width, border=INK),
        PageBreak(),
    ])

    # 18 — T1 and negative results
    section(
        story,
        "16 · TRANSFER + NEGATIVE RESULTS",
        "The optional real-world check stays separate; an unfavorable result stays in the record.",
        "Natural syndication can stress parts of the accounting problem, but available public data do not supply the ground truth required by the confirmatory estimand.",
        styles,
    )
    story.extend([
        grid([
            [p("SOURCE", styles["CardLabel"]), p("BOUNDED USE", styles["CardLabel"]), p("BLOCKING LIMIT", styles["CardLabel"])],
            [p("NEWS-COPY", styles["BodySmall"]), p("Same-original / dependent fixtures", styles["BodySmall"]), p("Nonduplicates are not verified independent origins; rights unresolved", styles["BodySmall"])],
            [p("Newswire", styles["BodySmall"]), p("Reproduction clusters and recurrence context", styles["BodySmall"]), p("Cluster rows lack claim stance, evidence spans, support/refute origins, and multiple-origin truth", styles["BodySmall"])],
        ], [34 * mm, 51 * mm, width - 85 * mm]),
        Spacer(1, 5 * mm),
        card([
            p("T1 BOUNDARY", styles["CardLabel"]),
            p("Separate rights and annotation manifest · descriptive only · outside A, M, primary/safety denominators, confidence intervals, tests, and effect estimates · never F3", styles["Body"]),
        ], width, border=BLUE),
        Spacer(1, 6 * mm),
        p("Locked interpretations", styles["CardTitle"]),
        grid([
            [p("OBSERVED PATTERN", styles["CardLabel"]), p("REQUIRED INTERPRETATION", styles["CardLabel"])],
            [p("F1 and F2 beat F0; F2 ties F1", styles["BodySmall"]), p("Credit the explicit rule, not typed metadata.", styles["BodySmall"])],
            [p("F2 reduces FC but harms VOR", styles["BodySmall"]), p("Reject the cue as unsafe; it suppresses valid stipulated convergence.", styles["BodySmall"])],
            [p("Effect survives only superficial metadata", styles["BodySmall"]), p("Report a shortcut, formatting, or direct-code result.", styles["BodySmall"])],
            [p("Null, negative, harmful, or unstable", styles["BodySmall"]), p("Preserve and report it; do not change the endpoint, denominator, or run until favorable.", styles["BodySmall"])],
        ], [61 * mm, width - 61 * mm]),
        PageBreak(),
    ])

    # 19 — Limitations
    section(
        story,
        "17 · LIMITATIONS",
        "Sixteen constraints that cannot be smoothed away",
        "The package is complete only if the absences are as legible as the proposal.",
        styles,
    )
    limitations = [
        "No empirical evaluation",
        "No broad novelty finding",
        "No proven minimum decomposition",
        "No validated constructs",
        "No provenance discovery",
        "No real-world independence claim",
        "No truth result",
        "Open-world evidence remains incomplete",
        "Costs are unknown",
        "Human control is unproven",
        "Memory can amplify error",
        "Transfer remains unresolved and rights-gated",
        "Historical standalone v13 HTML is unavailable",
        "Product cases are circular if treated as evidence",
        "The name may fail reader comprehension",
        "No publication or deployment authorization",
    ]
    lrows = []
    for row_start in range(0, 16, 4):
        row = []
        for index, item in enumerate(limitations[row_start:row_start + 4], start=row_start + 1):
            row.append([
                p(f"{index:02d}", styles["BigNumber"]),
                p(item, styles["BodySmall"]),
            ])
        lrows.append(row)
    ltable = Table(lrows, colWidths=[width / 4] * 4)
    ltable.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), .4, LINE),
        ("BACKGROUND", (0, 0), (-1, -1), PAPER_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 4 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4 * mm),
    ]))
    story.extend([
        ltable,
        Spacer(1, 8 * mm),
        card([
            p("A COMPLETE CONCEPTUAL SITE CAN PRECEDE RESULTS", styles["CardLabel"]),
            p("The empirical paper and any result surface cannot. Until a separately authorized run passes every gate, the Lab remains a protocol and all result language remains absent.", styles["Thesis"]),
        ], width, border=CORAL, padding=5 * mm),
        PageBreak(),
    ])

    # 20 — Close
    section(
        story,
        "18 · OWNER DECISION",
        "Keep the question visible enough to answer honestly.",
        "An AI system will make context judgments whether or not it names them. The proposal is to expose those judgments early enough to contest—then retire the machinery wherever it does not earn its cost.",
        styles,
    )
    story.extend([
        rich("The important move is not to count less. It is to count the right unit under a stated rule and preserve what remains unknown.", styles["Quote"]),
        Rule(width, TEAL, 4),
        Spacer(1, 6 * mm),
        p("Owner questions", styles["CardTitle"]),
        *bullets([
            "Does the nine-report receipt make the thesis concrete without overclaiming?",
            "Is “Discrimination Layer” worth retaining, or should the public name become “Context Judgment Layer”?",
            "Are the six-family / eleven-component map and its compatibility IDs ready to freeze for owner review?",
            "Should the narrow F2−F1 program remain the first paper, contingent on a later exact model/tokenizer/run authorization?",
            "Should T1 remain deferred until rights and field-level annotation feasibility are independently cleared?",
        ], styles, TEAL),
        Spacer(1, 5 * mm),
        two_cards(
            lambda col: card([
                p("CANONICAL READING SURFACE", styles["CardLabel"]),
                p("site/", styles["CardTitle"]),
                p("Semantic local HTML with Essay, Explore, and Lab tracks.", styles["BodySmall"]),
                p("source/THOUGHT_PIECE_V15.md · v15.1 content", styles["BodyTiny"]),
            ], col, border=TEAL),
            lambda col: card([
                p("EXECUTION SPECIFICATION", styles["CardLabel"]),
                p("research/", styles["CardTitle"]),
                p("Prospectus, protocol, readiness memo, schemas, offline tools, and review receipts.", styles["BodySmall"]),
                p("No external run is authorized by these files.", styles["BodyTiny"]),
            ], col, border=BLUE),
            width,
        ),
        Spacer(1, 7 * mm),
        card([
            p("FINAL STATUS", styles["CardLabel"]),
            rich('<font color="#9C4233"><b>LOCAL OWNER REVIEW · CONCEPTUAL SYNTHESIS · UNRUN RESEARCH PROGRAM · NOT PUBLISHED</b></font>', styles["Body"]),
        ], width, border=INK),
    ])

    doc.build(story)


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
        default=Path("output/pdf/PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf"),
    )
    args = parser.parse_args()
    build_pdf(args.framework, args.output)


if __name__ == "__main__":
    main()
