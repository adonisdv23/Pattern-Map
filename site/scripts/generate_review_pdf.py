#!/usr/bin/env python3
"""Create the local Pattern Map v16 owner-review PDF companion.

This document is deliberately source-bounded: the small amount of prose here
is a review map for the local site, not a new research claim or an external
evidence summary.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "site" / "exports" / "pattern-map-v16-owner-review.pdf"
INTERFACE = ROOT / "docs" / "CONTENT_INTERFACE_V16.json"


INK = colors.HexColor("#152022")
INK_MUTED = colors.HexColor("#405255")
PAPER = colors.HexColor("#f4efe5")
PAPER_DARK = colors.HexColor("#e9e0d2")
LINE = colors.HexColor("#c8c2b6")
TEAL = colors.HexColor("#257d7b")
CORAL = colors.HexColor("#cb6945")
PURPLE = colors.HexColor("#8064a5")
BLUE = colors.HexColor("#4a7791")
GOLD = colors.HexColor("#b48638")


def ascii_text(value: object) -> str:
    """Keep the PDF text safe for the built-in fonts and PDF skill rules."""

    text = str(value)
    replacements = {
        "\u2014": "-",
        "\u2013": "-",
        "\u2011": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2192": "->",
        "\u2026": "...",
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def markup(value: object) -> str:
    return escape(ascii_text(value)).replace("\n", "<br/>")


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="CoverKicker",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8.2,
        leading=10,
        textColor=CORAL,
        tracking=1.6,
        spaceAfter=10,
    )
)
styles.add(
    ParagraphStyle(
        name="CoverTitle",
        parent=styles["Title"],
        fontName="Times-Bold",
        fontSize=31,
        leading=33,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        name="CoverDeck",
        parent=styles["Normal"],
        fontName="Times-Roman",
        fontSize=17,
        leading=21,
        textColor=INK_MUTED,
        spaceAfter=18,
    )
)
styles.add(
    ParagraphStyle(
        name="Headline",
        parent=styles["Heading1"],
        fontName="Times-Bold",
        fontSize=25,
        leading=27,
        textColor=INK,
        spaceBefore=3,
        spaceAfter=9,
    )
)
styles.add(
    ParagraphStyle(
        name="CoverProblemHeadline",
        parent=styles["Headline"],
        fontSize=23,
        leading=25,
    )
)
styles.add(
    ParagraphStyle(
        name="SectionTitle",
        parent=styles["Heading2"],
        fontName="Times-Bold",
        fontSize=18,
        leading=21,
        textColor=INK,
        spaceBefore=2,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="CardTitle",
        parent=styles["Heading3"],
        fontName="Times-Bold",
        fontSize=13.5,
        leading=15.5,
        textColor=INK,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.4,
        leading=13.2,
        textColor=INK,
        spaceAfter=7,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyMuted",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.6,
        leading=11.7,
        textColor=INK_MUTED,
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        name="SmallCaps",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.4,
        leading=9,
        textColor=INK_MUTED,
        tracking=1.1,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="Small",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.5,
        leading=9.4,
        textColor=INK_MUTED,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="Quote",
        parent=styles["BodyText"],
        fontName="Times-Italic",
        fontSize=13.5,
        leading=17,
        textColor=INK,
        leftIndent=13,
        borderColor=TEAL,
        borderWidth=2,
        borderPadding=8,
        spaceBefore=4,
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        name="TableHead",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.5,
        leading=9,
        textColor=colors.white,
    )
)
styles.add(
    ParagraphStyle(
        name="TableCell",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.7,
        leading=10.3,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        name="TableCellBold",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.7,
        leading=10.3,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        name="DoorLabel",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9.2,
        leading=11,
        textColor=INK,
        spaceAfter=3,
    )
)


def p(text: object, style: str = "Body") -> Paragraph:
    return Paragraph(markup(text), styles[style])


def rich(text: str, style: str = "Body") -> Paragraph:
    return Paragraph(ascii_text(text), styles[style])


def kicker(text: object) -> Paragraph:
    return p(ascii_text(text).upper(), "CoverKicker")


def rule(color: colors.Color = LINE, width: float = 1) -> HRFlowable:
    return HRFlowable(width="100%", thickness=width, color=color, spaceBefore=4, spaceAfter=12)


def tag(text: object, color: colors.Color = TEAL) -> Table:
    item = Table([[p(ascii_text(text).upper(), "SmallCaps")]], colWidths=[None])
    item.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.Color(color.red, color.green, color.blue, alpha=0.12)),
                ("BOX", (0, 0), (-1, -1), 0.6, color),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return item


def card(title: object, body: object, color: colors.Color = TEAL, label: object | None = None) -> Table:
    flow = []
    if label:
        flow.append(p(ascii_text(label).upper(), "SmallCaps"))
    flow.extend([p(title, "CardTitle"), p(body, "BodyMuted")])
    table = Table([[flow]], colWidths=[None])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#faf7f0")),
                ("BOX", (0, 0), (-1, -1), 0.6, LINE),
                ("LINEABOVE", (0, 0), (-1, 0), 4, color),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return table


def bullet(text: object) -> Paragraph:
    return rich(f"<font color='{TEAL.hexval()}'>&bull;</font>&nbsp;&nbsp;{markup(text)}", "Body")


def footer(canvas, doc) -> None:
    canvas.saveState()
    width, height = letter
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.55)
    canvas.line(doc.leftMargin, 0.47 * inch, width - doc.rightMargin, 0.47 * inch)
    canvas.setFillColor(INK_MUTED)
    canvas.setFont("Helvetica-Bold", 7.2)
    canvas.drawString(doc.leftMargin, 0.28 * inch, "PATTERN MAP V16  /  LOCAL OWNER REVIEW")
    canvas.setFont("Helvetica", 7.2)
    canvas.drawRightString(width - doc.rightMargin, 0.28 * inch, f"LOCAL ONLY  /  {doc.page}")
    canvas.restoreState()


def build_pdf() -> None:
    interface = json.loads(INTERFACE.read_text(encoding="utf-8"))
    first = interface["first_screen"]
    families = interface["families"]
    doors = interface["doors"]
    owner_hash = interface.get("owner_intent_sha256", "not repeated here")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(OUTPUT),
        invariant=1,
        pagesize=letter,
        leftMargin=0.67 * inch,
        rightMargin=0.67 * inch,
        topMargin=0.62 * inch,
        bottomMargin=0.62 * inch,
        title="Pattern Map v16 - Owner Review Companion",
        author="Pattern Map v16 local owner-review build",
        subject="Local review companion for the canonical Pattern Map v16 site",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="owner-review", frames=[frame], onPage=footer)])

    story = []

    # Page 1 - cover.
    story.extend(
        [
            Spacer(1, 0.2 * inch),
            kicker("Owner-review companion  /  v16"),
            p("Pattern Map", "CoverTitle"),
            p("Pattern Recognition / The Discrimination Layer", "CoverDeck"),
            rule(TEAL, 2),
            Spacer(1, 0.12 * inch),
            kicker("The human problem"),
            p(first["headline"], "CoverProblemHeadline"),
            p(first["standfirst"], "CoverDeck"),
            Spacer(1, 0.08 * inch),
        ]
    )
    door_rows = []
    door_colors = [TEAL, CORAL, BLUE]
    for index, door in enumerate(doors):
        door_rows.append(
            [
                [
                    p(f"0{index + 1}", "SmallCaps"),
                    p(door["label"], "DoorLabel"),
                    p(door["promise"], "BodyMuted"),
                ]
            ]
        )
    doors_table = Table(door_rows, colWidths=[doc.width], rowHeights=None)
    doors_style = [
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#faf7f0")),
    ]
    for row, color in enumerate(door_colors):
        doors_style.append(("LINEABOVE", (0, row), (-1, row), 3, color))
    doors_table.setStyle(TableStyle(doors_style))
    story.extend(
        [
            doors_table,
            Spacer(1, 0.18 * inch),
            p("A compact companion to the local interactive site. The site keeps the human essay, current relationship view, proportionate application path, targeted sources, research boundaries, and historical lineage in separate but connected routes, with an optional continuous Guided read.", "BodyMuted"),
            p("Accessibility route: this PDF is an untagged visual review companion. Use the standalone HTML for semantic headings, landmarks, links, and assistive-technology navigation.", "Small"),
            tag("Local owner review - not a deployment, publication, or research result", CORAL),
            PageBreak(),
        ]
    )

    # Page 2 - idea and reading path.
    story.extend(
        [
            kicker("01  /  Read the idea"),
            p("Start with the upstream choices.", "Headline"),
            p("The public opening is a human problem and a usable idea. Technical detail follows as progressive disclosure; it does not replace the coffee-conversation entry point.", "Body"),
            rich(f"<b>{markup(first['headline'])}</b><br/>{markup(first['standfirst'])}", "Quote"),
            p("The reading route is cumulative: a short 60-90-second version gives the shape, then the complete canonical essay provides the 10-15-minute treatment. The mentor cover note remains a distinct optional handoff rather than the public opening.", "Body"),
            rule(),
            kicker("Three doors, one optional guided path"),
        ]
    )
    route_cards = [
        card("Read the idea", "What changes when the system improves the choices made before generation?", TEAL, "01"),
        card("Explore the map", "Which of six families helps a reader notice, compare, preserve, question, or learn more deliberately?", CORAL, "02"),
        card("Apply it", "How much workflow is proportionate to this decision, and where should it stop?", BLUE, "03"),
    ]
    route_table = Table([route_cards], colWidths=[doc.width / 3 - 5] * 3, hAlign="LEFT")
    route_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    story.extend(
        [
            route_table,
            Spacer(1, 0.14 * inch),
            rich("<b>Optional continuous mode:</b> Take the guided read for one generated 8-12-minute path through the problem, six questions, key relationships, smallest useful application, examples, and boundaries. It reuses canonical components rather than forking the manuscript.", "BodyMuted"),
            Spacer(1, 0.08 * inch),
            p("What the framing does not claim", "SectionTitle"),
            bullet("The six families are not presented as newly invented categories."),
            bullet("A peripheral signal is a candidate for inspection, not proof of truth."),
            bullet("Provenance, recurrence, or access do not by themselves establish correctness, independence, or permission."),
            bullet("Fixtures, protocols, validators, reviews, and planning simulations are not empirical results."),
            Spacer(1, 0.1 * inch),
            tag("Content contract checkpoint: " + owner_hash[:16] + "...", PURPLE),
            PageBreak(),
        ]
    )

    # Page 3 - map.
    story.extend(
        [
            kicker("02  /  Explore the map"),
            p("Six families, held in one view.", "Headline"),
            p("The current relationship view is code-native and retains the historical F1-F6 identifiers without turning them into steps. Focus controls add emphasis but never hide essential meaning. With JavaScript off, the family cards, questions, boundaries, and relationship summary remain in the document.", "Body"),
        ]
    )
    family_rows = [[p("ID", "TableHead"), p("FAMILY", "TableHead"), p("READER QUESTION", "TableHead")]]
    for family in families:
        family_rows.append(
            [
                p(family["id"], "TableCellBold"),
                p(family["name"], "TableCellBold"),
                p(family["reader_question"], "TableCell"),
            ]
        )
    family_table = Table(family_rows, colWidths=[0.42 * inch, 1.55 * inch, doc.width - 1.97 * inch], repeatRows=1)
    family_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), INK),
                ("BOX", (0, 0), (-1, -1), 0.6, LINE),
                ("INNERGRID", (0, 1), (-1, -1), 0.35, LINE),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#faf7f0")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#faf7f0"), colors.HexColor("#f0eadf")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.extend(
        [
            family_table,
            Spacer(1, 0.18 * inch),
            p("Relationship view", "SectionTitle"),
            p("The line-free map names four limited relationships rather than implying one pipeline: a baseline is required before calling something motion or missing; source weighing and structured comparison can reveal a common origin; permission and human authority constrain influence; and a learning update waits for an observed outcome and review.", "Body"),
            card("A map is a discrimination layer, not a truth machine.", "It makes upstream choices inspectable and revisable. It does not guarantee that a candidate is true, repetition is independent, a source is correct, or every task needs every record.", PURPLE, "Boundary"),
            PageBreak(),
        ]
    )

    # Page 4 - teaching patterns and project boundaries.
    story.extend(
        [
            kicker("03  /  Examples that teach the boundary"),
            p("Three patterns make the idea concrete.", "Headline"),
            p("Examples stay bounded: they demonstrate what to inspect and what to label, not what an unrun study would prove.", "Body"),
        ]
    )
    patterns = [
        card("Specialist / peripheral candidate", "A specialist or peripheral source may reveal an overlooked mechanism or exception. It earns inspection, comparison, and provenance work; it does not become true merely because the default path missed it.", TEAL, "01  /  peripheral signal"),
        card("Velocity or expected absence", "A change is meaningful only relative to a relevant baseline. The same logic applies to an expected absence: state what should be present, define the comparison window, and keep the interpretation provisional.", CORAL, "02  /  motion + memory"),
        card("Common-origin recurrence", "Repeated material can share a common origin. Recurrence is useful for tracing spread or influence, but independence is UNKNOWN unless separately established.", PURPLE, "03  /  recurrence"),
    ]
    pattern_table = Table([[patterns[0], patterns[1]], [patterns[2], card("Signal Foundry", "ILLUSTRATION ONLY / READ-ONLY / NOT VALIDATION. This bounded example shows how a workspace can expose signals without turning the interface into evidence.", GOLD, "Separate illustration")]], colWidths=[doc.width / 2 - 5] * 2)
    pattern_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    story.extend(
        [
            pattern_table,
            Spacer(1, 0.07 * inch),
            card("Echo is separate and late", "SEPARATE PROJECT - UNRUN - NO RESULTS. Echo is a subordinate research track and a late common-origin example. Removing or hiding it leaves Read the idea, Explore the map, and Apply it coherent.", BLUE, "Research boundary"),
            Spacer(1, 0.12 * inch),
            p("The site keeps the evidence boundary visible without making it the opening move: Signal Foundry is an illustration, Echo is a separate unrun project, and neither defines the current v16 map.", "Body"),
            PageBreak(),
        ]
    )

    # Page 5 - apply.
    story.extend(
        [
            kicker("04  /  Apply it"),
            p("First decide whether a workflow is needed at all.", "Headline"),
            p("Stage 0 asks whether the work is an already-permitted, reversible supplied-material transformation with no material claim judgment, comparison, selection or withholding, permission resolution, memory reuse, acquisition, human action gate, or consequential external influence. If any condition fails, use the smallest layered route. The local studio recommends a plan; it does not run work or record an observed stop, outcome, learning review, or human decision.", "Body"),
        ]
    )
    level_rows = [[p("LEVEL", "TableHead"), p("WHEN IT FITS", "TableHead"), p("OBSERVABLE OUTPUT", "TableHead")]]
    levels = [
        ("Ordinary", "Every Stage 0 condition holds for an already-permitted, reversible supplied-material transformation.", "Supplied scope, material assumptions, unchecked boundaries, and output - then stop."),
        ("Lightweight", "One ambiguity or alternate comparison is worth a bounded pass.", "One alternate route, one challenge, a stated limit, and provisional wording if needed."),
        ("Moderate", "Consequential or high-uncertainty work that does not meet every Advanced condition needs explicit comparison.", "Evidence register, comparison, uncertainty, permission, and named human review."),
        ("Advanced", "Consequential work, high uncertainty, and substantial separately approved capacity are all present.", "Queryable records and repeatable review controls, only when their added cost is justified."),
    ]
    for row in levels:
        level_rows.append([p(row[0], "TableCellBold"), p(row[1], "TableCell"), p(row[2], "TableCell")])
    level_table = Table(level_rows, colWidths=[0.9 * inch, 2.45 * inch, doc.width - 3.35 * inch], repeatRows=1)
    level_table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), INK), ("BOX", (0, 0), (-1, -1), 0.6, LINE), ("INNERGRID", (0, 1), (-1, -1), 0.35, LINE), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#faf7f0"), colors.HexColor("#f0eadf")]), ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7), ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story.extend([level_table, Spacer(1, 0.14 * inch), card("Planning is not an event record", "The studio recommends an action, gate, planned stopping condition, and optional learning path. Its observed state remains NOT_RUN / NOT_TRIGGERED / NOT_OBSERVED / NOT_AVAILABLE / NOT_RECORDED until separately authorized work actually occurs.", PURPLE, "Apply integrity"), Spacer(1, 0.14 * inch), p("Operator path after Stage 0", "SectionTitle")])
    operator_steps = [
        "Frame the claim and decision.",
        "Name the baseline or expected state.",
        "Acquire only what the route authorizes.",
        "Assign each source a role for this claim.",
        "Compare candidates and alternatives.",
        "Look for disconfirming information.",
        "Record provenance without treating it as correctness.",
        "State what remains unknown.",
        "Apply the stop condition.",
        "Make the human disposition explicit.",
        "Record a bounded learning update.",
        "Review the actual record for future use.",
    ]
    step_cells = []
    for index, step in enumerate(operator_steps, start=1):
        step_cells.append(rich(f"<font color='{TEAL.hexval()}'><b>{index:02d}</b></font>&nbsp;&nbsp;{markup(step)}", "BodyMuted"))
    step_table = Table([[step_cells[:6], step_cells[6:]]], colWidths=[doc.width / 2 - 5] * 2)
    step_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOX", (0, 0), (-1, -1), 0.6, LINE), ("LINEBEFORE", (1, 0), (1, 0), 0.4, LINE), ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 5), ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#faf7f0"))]))
    story.extend([step_table, Spacer(1, 0.14 * inch), tag("Agent companion: Quickstart first, deeper guide when the decision warrants it", BLUE), PageBreak()])

    # Page 6 - boundaries, history, and QA.
    story.extend(
        [
            kicker("05  /  Boundaries and review status"),
            p("A review surface with its limits attached.", "Headline"),
            p("The local package is designed to make the artifact inspectable. It is not a deployment, a public replacement, a study, or a provider-backed run.", "Body"),
            p("Historical lineage", "SectionTitle"),
            card("Historical v13 origin - not the current v16 topology.", "The recovered v13 diagram is preserved for lineage and displayed with a hash-anchored label. The current topology is the code-native relationship view on Explore the map. The historical asset is never redrawn as the current system.", TEAL, "History route"),
            Spacer(1, 0.14 * inch),
            p("Owner-review QA completed", "SectionTitle"),
        ]
    )
    qa_items = [
        "Static build and route/link checks pass for ten routes plus the standalone export.",
        "Frozen content-interface validator passes; exact first-screen copy, door order, F1-F6 order, route manifests, and claim boundaries are present.",
        "Live browser checks cover 390-pixel, exact 821-pixel, 1024-pixel, and desktop layouts; map focus, permission precedence, Apply observed-state separation, term explainers, and horizontal overflow.",
        "Semantic landmark, heading, accessible-name, no-script, reduced-motion, forced-colors, reflow-oriented, print-hook, standalone, and Echo-removal audits pass within their automated scope.",
        "The untagged PDF was reopened, text-checked, rendered with Poppler, and visually inspected for clipping, overlap, and unreadable glyphs; semantic and assistive-technology navigation belongs to the standalone HTML.",
    ]
    qa_rows = [[p("•", "Body"), p(item, "Body")] for item in qa_items]
    qa_table = Table(qa_rows, colWidths=[0.18 * inch, doc.width - 0.18 * inch])
    qa_table.setStyle(
        TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (0, -1), TEAL),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    story.append(qa_table)
    story.extend(
        [
            Spacer(1, 0.06 * inch),
            card("What this QA does not establish", "QA is implementation evidence, not reader comprehension, persuasion, behavioral effectiveness, model quality, or research evidence. Physical keyboard, supported screen-reader, real 200% browser/OS zoom, browser print-preview, and owner/mentor judgment remain open.", CORAL, "Explicit residual"),
            Spacer(1, 0.15 * inch),
            p("Local handoff", "SectionTitle"),
            rich("Build from the repository root with <font name='Courier'>cd site &amp;&amp; npm run build &amp;&amp; npm run check</font>. Preview with <font name='Courier'>npm run dev</font> and open <font name='Courier'>http://127.0.0.1:4173/</font>. The semantic standalone export is under <font name='Courier'>site/exports/standalone/pattern-map-v16.html</font>; the untagged visual companion is under <font name='Courier'>site/exports/pattern-map-v16-owner-review.pdf</font>.", "BodyMuted"),
            tag("No hosting API, deployment, publication, release, or production URL used", PURPLE),
        ]
    )

    doc.build(story)
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    build_pdf()
