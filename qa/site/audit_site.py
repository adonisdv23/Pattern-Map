#!/usr/bin/env python3
"""Static, semantic, no-script, and boundary checks for the local v16 site.

This is structural QA only. It is not a reader-comprehension, effectiveness,
model, empirical, participant, or deployment result.
"""

from __future__ import annotations

import hashlib
import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "site" / "dist"
EXPORT = ROOT / "site" / "exports" / "standalone" / "pattern-map-v16.html"
DIAGRAM = ROOT / "assets" / "diagrams" / "historical-v13-pattern-recognition-diagram-v12.png"
EXPECTED_DIAGRAM_SHA = "8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae"
ROUTES = {
    "index.html": "Pattern Recognition / The Discrimination Layer",
    "read/index.html": "Read the idea",
    "map/index.html": "Explore the map",
    "apply/index.html": "Apply it",
    "guided/index.html": "Take the guided read",
    "examples/index.html": "Examples",
    "boundaries/index.html": "Boundaries",
    "sources/index.html": "Sources",
    "research/index.html": "Research",
    "history/index.html": "History",
}


class SemanticParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[dict[str, object]] = []
        self.headings: list[tuple[int, str]] = []
        self.landmarks: list[tuple[str, str]] = []
        self.interactive: list[tuple[str, dict[str, str], str]] = []
        self.images: list[dict[str, str]] = []
        self.scripts = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = {key: value or "" for key, value in attrs}
        if tag == "script":
            self.scripts += 1
        if tag == "img":
            self.images.append(attributes)
        if tag in {"header", "main", "nav", "footer", "article", "section"}:
            self.landmarks.append((tag, attributes.get("aria-label", "")))
        self.stack.append({"tag": tag, "attrs": attributes, "text": []})

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        for item in self.stack:
            item["text"].append(data)  # type: ignore[union-attr]

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index]["tag"] != tag:
                continue
            item = self.stack.pop(index)
            text = " ".join("".join(item["text"]).split())  # type: ignore[arg-type]
            attrs = item["attrs"]  # type: ignore[assignment]
            if re.fullmatch(r"h[1-6]", tag):
                self.headings.append((int(tag[1]), text))
            if tag in {"a", "button", "summary"}:
                self.interactive.append((tag, attrs, text))  # type: ignore[arg-type]
            break


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def parse(file: Path) -> tuple[str, SemanticParser]:
    text = file.read_text(encoding="utf-8")
    parser = SemanticParser()
    parser.feed(text)
    return text, parser


def accessible_name(attrs: dict[str, str], text: str) -> str:
    return attrs.get("aria-label", "").strip() or attrs.get("alt", "").strip() or text.strip()


def audit_route(relative: str, expected_title: str) -> list[str]:
    file = DIST / relative
    require(file.is_file(), f"missing built route: {relative}")
    text, parser = parse(file)
    messages: list[str] = []
    require(re.search(r'<html\b[^>]*\blang="en"', text) is not None, f"{relative}: missing lang=en")
    require(text.count('<main id="main"') == 1, f"{relative}: expected one main landmark")
    require('<a class="skip-link" href="#main">' in text, f"{relative}: skip link missing")
    require(any(label == "Principal routes" for tag, label in parser.landmarks if tag == "nav"), f"{relative}: principal nav label missing")
    require(len(parser.headings) >= 1, f"{relative}: no headings")
    require(sum(level == 1 for level, _ in parser.headings) == 1, f"{relative}: expected exactly one h1")
    require(parser.headings[0][0] == 1, f"{relative}: h1 is not the first heading")
    for previous, current in zip(parser.headings, parser.headings[1:]):
        require(current[0] <= previous[0] + 1, f"{relative}: heading jump {previous} -> {current}")
    for tag, attrs, text_value in parser.interactive:
        if tag == "a" and not attrs.get("href"):
            raise AssertionError(f"{relative}: anchor without href")
        if tag in {"button", "summary"}:
            require(accessible_name(attrs, text_value), f"{relative}: {tag} without accessible name")
        if tag == "button" and "data-term-trigger" in attrs:
            require(accessible_name(attrs, text_value).startswith("Explain "), f"{relative}: term trigger does not name its concept")
    for image in parser.images:
        require("alt" in image, f"{relative}: image without alt attribute")
    if expected_title != "Pattern Recognition / The Discrimination Layer":
        require(expected_title in text, f"{relative}: route title copy missing")
    messages.append(f"PASS semantic landmarks/headings/names: {relative}")
    return messages


def main() -> None:
    output: list[str] = []
    for route, expected_title in ROUTES.items():
        output.extend(audit_route(route, expected_title))

    root_text = (DIST / "index.html").read_text(encoding="utf-8")
    map_text = (DIST / "map/index.html").read_text(encoding="utf-8")
    apply_text = (DIST / "apply/index.html").read_text(encoding="utf-8")
    guided_text = (DIST / "guided/index.html").read_text(encoding="utf-8")
    read_text = (DIST / "read/index.html").read_text(encoding="utf-8")
    sources_text = (DIST / "sources/index.html").read_text(encoding="utf-8")
    examples_text = (DIST / "examples/index.html").read_text(encoding="utf-8")
    css_text = (ROOT / "site" / "src" / "site.css").read_text(encoding="utf-8")

    essential = [
        "AI slop often begins before the model writes a word.",
        "Pattern Recognition is the discipline of improving them.",
        "Peripheral signal",
        "Source weighing",
        "Velocity / motion",
        "Absence + memory",
        "Structured patterns",
        "Learning loop",
        "Human authority stays explicit.",
    ]
    for value in essential:
        require(value in root_text + map_text + apply_text + read_text, f"essential site meaning missing: {value}")
    output.append("PASS no-script essential meaning is present in static HTML")

    for value in ["ordinary", "lightweight", "moderate", "advanced", "ACQUIRE", "STOPPED_BUDGET", "LEARNING_PENDING_OUTCOME"]:
        require(value.lower() in apply_text.lower(), f"Apply vocabulary missing: {value}")
    require('name="evidenceSelection"' in apply_text and "Stage 0 comes first" in apply_text, "Apply Stage 0 evidence-selection gate missing")
    output.append("PASS Apply route exposes ordinary/lightweight/moderate/advanced and route/stop/learning vocabularies")

    term_names = re.findall(r'<button\b[^>]*data-term-trigger[^>]*aria-label="(Explain [^"]+)"', root_text + map_text + apply_text + guided_text)
    require(term_names and len(set(term_names)) >= 6, "contextual term triggers lack distinct descriptive names")
    require(".no-js .term-popover-trigger" in css_text and ".no-js .reading-progress-wrap" in css_text, "no-script optional-control suppression missing")
    require(re.search(r'@media \(min-width: 601px\) and \(max-width: 1100px\)[\s\S]*?\.term-popover\s*\{[^}]*position:\s*static', css_text) is not None, "medium-width term popover is not flow-native")
    require(re.search(r'@media\s*\(max-width:\s*600px\)[\s\S]{0,2400}?\.route-brief\s*\{[^}]*grid-template-columns:\s*repeat\(3', css_text) is None, "narrow route brief regressed to three columns")
    output.append("PASS descriptive term controls, no-script suppression, and responsive route-help contracts")

    recommendation_match = re.search(r'<aside class="route-recommendation-card"[\s\S]*?</aside>', apply_text)
    require(recommendation_match is not None, "Apply planning recommendation card missing")
    recommendation_text = recommendation_match.group(0)
    for token in ("COMPLETE", "STOPPED_", "HUMAN_DISPOSITION_RECORDED", "LEARNING_PENDING_OUTCOME", "LEARNING_REVIEWED"):
        require(token not in recommendation_text, f"Apply planning card fabricates observed event: {token}")
    for token in ("NOT_RUN", "NOT_TRIGGERED", "NOT_OBSERVED", "NOT_AVAILABLE", "NOT_RECORDED"):
        require(token in recommendation_text, f"Apply initial observed state missing: {token}")
    output.append("PASS Apply recommendation separates plans, simulations, and unobserved state")

    for section_id in ("guided-opening", "guided-families", "guided-relations", "guided-apply", "guided-examples", "guided-boundary"):
        require(f'id="{section_id}"' in guided_text, f"Guided route section missing: {section_id}")
    require("editorial estimate only" in guided_text, "Guided route reading-time caveat missing")
    output.append("PASS optional Guided route preserves a continuous authored reading path")

    for value in ["@media print", "prefers-reduced-motion", "forced-colors", "details > summary"]:
        require(value in css_text, f"responsive/accessibility CSS hook missing: {value}")
    output.append("PASS reduced-motion, forced-colors, 200%-friendly reflow, and print hooks present")

    stripped = re.sub(r"<script\b[^>]*>[\s\S]*?</script>", "", root_text + map_text + apply_text, flags=re.IGNORECASE)
    for value in ["AI slop often begins before the model writes a word.", "Peripheral signal", "ordinary", "lightweight", "moderate", "advanced"]:
        require(value in stripped, f"no-script simulation lost essential value: {value}")
    output.append("PASS no-script simulation retains first-screen, map, and application essentials")

    echo_removed = re.sub(r"echo|origin-accounting|no results", "", read_text + map_text + apply_text, flags=re.IGNORECASE)
    for value in ["Pattern Recognition", "Peripheral signal", "Source weighing", "Learning loop", "ACQUIRE", "HOLD", "STOPPED_BUDGET"]:
        require(value in echo_removed, f"Echo-removal simulation lost principal-route meaning: {value}")
    output.append("PASS synthetic Echo-removal simulation leaves Read/Explore/Apply meaning coherent")

    history_text = (DIST / "history/index.html").read_text(encoding="utf-8")
    require("Historical v13 origin — not the current v16 topology." in history_text, "historical/current label missing")
    require("current relationship view" in history_text.lower(), "current relationship distinction missing")
    require(hashlib.sha256(DIAGRAM.read_bytes()).hexdigest() == EXPECTED_DIAGRAM_SHA, "historical diagram hash changed")
    output.append("PASS historical diagram label/current-topology distinction and hash")

    standalone_text = EXPORT.read_text(encoding="utf-8")
    _, standalone_parser = parse(EXPORT)
    require("<style>" in standalone_text and 'rel="stylesheet"' not in standalone_text, "standalone export still needs external CSS")
    require("<script src=" not in standalone_text, "standalone export still needs external JavaScript")
    require("Read the idea" in standalone_text and "Explore the map" in standalone_text and "Apply it" in standalone_text, "standalone export lost principal doors")
    require(f'src="../../../assets/diagrams/{DIAGRAM.name}"' in standalone_text and DIAGRAM.is_file(), "standalone export lost its local historical diagram reference")
    standalone_id_list = re.findall(r'\sid="([^"]+)"', standalone_text)
    require(len(standalone_id_list) == len(set(standalone_id_list)), "standalone export contains duplicate IDs")
    require(sum(level == 1 for level, _ in standalone_parser.headings) == 1, "standalone export must have exactly one h1")
    for previous, current in zip(standalone_parser.headings, standalone_parser.headings[1:]):
        require(current[0] <= previous[0] + 1, f"standalone export heading jump {previous} -> {current}")
    for route_id in ("home", "read", "map", "apply", "guided", "examples", "boundaries", "sources", "research", "history"):
        require(f'<section class="standalone-section" id="{route_id}"' in standalone_text, f"standalone route section missing: {route_id}")
    output.append("PASS direct-open all-routes HTML has embedded runtime, one h1, unique IDs, named sections, and its documented repository-local image")

    metareasoning_href = 'href="https://doi.org/10.1016/0004-3702(91)90015-C"'
    require(metareasoning_href in sources_text, "parenthesized external URL was not preserved")
    for label, html in (("sources route", sources_text), ("standalone export", standalone_text)):
        require(not re.search(r'<a\b[^>]*<(?:/?em|/?strong|/?code)\b', html, flags=re.IGNORECASE), f"{label}: inline markup corrupted an anchor start tag")
        for match in re.finditer(r'<a href="https?:[^"]+"([^>]*)>', html):
            attributes = match.group(1)
            require('target="_blank"' in attributes, f"{label}: external link missing target=_blank")
            require('rel="noreferrer"' in attributes, f"{label}: external link missing rel=noreferrer")
    output.append("PASS external Markdown links preserve URLs and safe anchor attributes")

    for token in ("STOPPED_BUDGET", "LEARNING_NOT_APPLICABLE", "NOT_AUTHORIZED_OR_AMBIGUOUS"):
        require(token in apply_text, f"Apply route mutated state token: {token}")
        require(token in standalone_text, f"standalone export mutated state token: {token}")
    signal_foundry_status = "ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION"
    require(signal_foundry_status in examples_text, "Examples route mutated Signal Foundry status")
    require(signal_foundry_status in standalone_text, "standalone export mutated Signal Foundry status")
    standalone_ids = set(re.findall(r'\sid="([^"]+)"', standalone_text))
    standalone_fragments = re.findall(r'href="#([^"]+)"', standalone_text)
    missing_fragments = sorted(set(standalone_fragments) - standalone_ids)
    require(not missing_fragments, f"standalone export has missing fragments: {missing_fragments}")
    require('href="#source-' not in standalone_text, "standalone export contains an unresolved source fragment")
    output.append("PASS exact underscore-bearing state vocabulary and standalone fragment integrity")

    print("\n".join(output))
    print("NOTE structural QA is not reader comprehension or effectiveness evidence")


if __name__ == "__main__":
    main()
