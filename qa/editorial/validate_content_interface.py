#!/usr/bin/env python3
"""Validate the frozen v16 content interface; no model or external action."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONTRACT_PATH = ROOT / "docs/CONTENT_INTERFACE_V16.json"
FAMILIES_PATH = ROOT / "framework/SIX_FAMILIES.json"
OWNER_INTENT_PATH = ROOT / "docs/OWNER_INTENT_V16.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def words(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").split())


def main() -> None:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    family_source = json.loads(FAMILIES_PATH.read_text(encoding="utf-8"))

    observed_owner_hash = hashlib.sha256(OWNER_INTENT_PATH.read_bytes()).hexdigest()
    require(
        contract["owner_intent_sha256"] == observed_owner_hash,
        "content interface owner-intent hash does not match locked source",
    )

    require(
        [door["id"] for door in contract["doors"]] == ["read", "map", "apply"],
        "principal door order must be read, map, apply",
    )
    require(
        [door["label"] for door in contract["doors"]]
        == ["Read the idea", "Explore the map", "Apply it"],
        "principal door labels changed",
    )
    require(
        [route["id"] for route in contract["secondary_routes"]]
        == ["examples", "boundaries", "sources", "research", "history"],
        "secondary route set or order changed",
    )

    expected_families = [
        {
            key: family[key]
            for key in ("id", "slug", "name", "reader_question")
        }
        for family in family_source["families"]
    ]
    require(contract["families"] == expected_families,
            "content-interface families differ from stable six-family source")
    require(len(contract["families"]) == 6, "content interface must expose six families")

    source_paths: set[str] = set()
    for surface in contract["doors"] + contract["secondary_routes"]:
        source_paths.update(surface["sources"])
    source_paths.update(
        {
            contract["progressive_disclosure"]["popover_source"],
            contract["history"]["current_topology_source"],
            contract["visual_policy"]["image_ledger_path"],
        }
    )
    for relative in sorted(source_paths):
        require((ROOT / relative).exists(), f"missing frozen source path: {relative}")

    headline = contract["first_screen"]["headline"]
    standfirst = contract["first_screen"]["standfirst"]
    require("before the model writes a word" in headline,
            "first screen no longer leads with the pre-generation problem")
    for phrase in ("generic", "upstream choices", "Pattern Recognition"):
        require(phrase in standfirst, f"standfirst lost required phrase: {phrase}")
    for prohibited in ("protocol", "provenance", "Echo Problem", "no results"):
        require(prohibited.lower() not in (headline + " " + standfirst).lower(),
                f"first screen leads with prohibited detail: {prohibited}")

    require(contract["echo"]["principal_door"] is False,
            "Echo may not become a principal door")
    require(contract["echo"]["removal_must_preserve_all_principal_routes"] is True,
            "Echo removal test is not required")
    require(
        contract["history"]["v13_label"]
        == "Historical v13 origin — not the current v16 topology.",
        "historical v13 label changed",
    )
    require(
        contract["progressive_disclosure"]["closed_controls_may_hide_required_qualifications"]
        is False,
        "closed controls may not hide required qualifications",
    )

    for action, authorized in contract["external_actions_authorized"].items():
        require(authorized is False, f"external action unexpectedly authorized: {action}")

    essay_path = ROOT / "manuscript/PATTERN_RECOGNITION_V16.md"
    short_path = ROOT / "manuscript/NINETY_SECOND_VERSION.md"
    require(2800 <= words(essay_path) <= 3600,
            "canonical essay raw word count left the approximate 10–15-minute band")
    require(240 <= words(short_path) <= 340,
            "short version raw word count left the cumulative 60–90-second band")

    essay = essay_path.read_text(encoding="utf-8")
    essay_family_headings = [
        "### 1. Peripheral signal",
        "### 2. Source weighing",
        "### 3. Velocity and motion",
        "### 4. Absence and memory",
        "### 5. Structured patterns",
        "### 6. The learning loop",
    ]
    positions = [essay.find(heading) for heading in essay_family_headings]
    require(all(position >= 0 for position in positions),
            "essay no longer contains every numbered family heading")
    require(positions == sorted(positions), "essay family order changed")
    echo_position = essay.find("## A narrower example: nine reports, one announcement")
    require(echo_position > positions[-1],
            "common-origin example appears before the complete six-family map")

    print("PASS  locked owner intent and content-interface JSON")
    print("PASS  three principal doors and five secondary routes")
    print("PASS  six-family identity/order/questions align with canonical JSON")
    print("PASS  human-problem first screen and late Echo placement")
    print(f"PASS  manuscript lengths: essay={words(essay_path)} raw words; short={words(short_path)} raw words")
    print("PASS  no external action authorized by the content interface")


if __name__ == "__main__":
    main()
