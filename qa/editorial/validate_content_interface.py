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
OWNER_INTENT_CHECKPOINT_PATH = ROOT / "docs/OWNER_INTENT_V16.sha256"
LOCKED_OWNER_INTENT_SHA256 = (
    "3aea5eeb19302a0e6498f7bcfccb23535953dbb6807fb5a486e0279bfa72543b"
)

EXPECTED_FIRST_SCREEN = {
    "headline": "AI slop often begins before the model writes a word.",
    "standfirst": (
        "A polished answer can still feel generic when the system follows the "
        "obvious search path, misses a specialist perspective, skips a useful "
        "comparison, overlooks an expected absence, or forgets what happened "
        "before. The answer inherits those upstream choices. Pattern Recognition "
        "is the discipline of improving them."
    ),
    "claim_status": "owner-approved-conceptual-framing-not-measured-prevalence",
    "must_precede": [
        "protocol",
        "disclaimer",
        "literature-defense",
        "provenance-graph",
        "research-status",
        "echo-example",
    ],
}

EXPECTED_FAMILIES = [
    {
        "id": "F1",
        "slug": "peripheral-signal",
        "name": "Peripheral signal",
        "reader_question": "What might the default path have overlooked?",
    },
    {
        "id": "F2",
        "slug": "source-weighing",
        "name": "Source weighing",
        "reader_question": "What role does each source play for this exact claim?",
    },
    {
        "id": "F3",
        "slug": "velocity-motion",
        "name": "Velocity / motion",
        "reader_question": "What is changing unusually relative to a relevant baseline?",
    },
    {
        "id": "F4",
        "slug": "absence-memory",
        "name": "Absence + memory",
        "reader_question": (
            "What should be present but is not, and what prior context changes "
            "the meaning of now?"
        ),
    },
    {
        "id": "F5",
        "slug": "structured-patterns",
        "name": "Structured patterns",
        "reader_question": "What becomes visible through explicit comparison?",
    },
    {
        "id": "F6",
        "slug": "learning-loop",
        "name": "Learning loop",
        "reader_question": (
            "What did we expect, what happened, and what bounded update is justified?"
        ),
    },
]

EXPECTED_FAMILY_BOUNDARIES = {
    "F1": "less-visible is a reason to inspect, not a reason to believe",
    "F2": "provenance is not correctness",
    "F3": "one observation is not velocity",
    "F4": "a gap is not proof of nonexistence",
    "F5": "recurrence is not corroboration",
    "F6": "learning proposes a bounded update; it does not silently apply one",
}

EXPECTED_INVARIANTS = [
    "Peripheral is a candidate status, not a truth status.",
    "Recurrence is not independent corroboration.",
    "Provenance is not correctness.",
    "Technical access is not operational permission.",
    "Motion and absence are baseline-dependent.",
    "Unknown relations stay unknown.",
    "Human disposition is a decision record, not a fact.",
    "Outcome learning proposes bounded updates and preserves history.",
]

EXPECTED_SOURCE_MANIFESTS = {
    "read": [
        "manuscript/NINETY_SECOND_VERSION.md",
        "manuscript/PATTERN_RECOGNITION_V16.md",
        "manuscript/MENTOR_COVER_NOTE.md",
        "manuscript/PUBLIC_ABSTRACT.md",
    ],
    "map": [
        "framework/SIX_FAMILIES.json",
        "framework/SIX_FAMILIES.md",
        "framework/RELATIONSHIP_MAP.md",
        "framework/GLOSSARY.md",
    ],
    "apply": [
        "framework/OPERATOR_PLAYBOOK.md",
        "framework/IMPLEMENTATION_CHOICES.md",
        "framework/BOUNDARIES_AND_FAILURES.md",
        "framework/agent-playbook/QUICKSTART.md",
        "framework/agent-playbook/FULL_OPERATING_GUIDE.md",
        "framework/agent-playbook/COPYABLE_AGENT_BRIEF.md",
        "framework/agent-playbook/PREFLIGHT_CHECKLIST.md",
        "framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md",
        "framework/templates/README.md",
        "framework/templates/DECISION_BRIEF.md",
        "framework/templates/ACQUISITION_RECEIPT.md",
        "framework/templates/EVIDENCE_REGISTER.md",
        "framework/templates/COMPARISON_MATRIX.md",
        "framework/templates/DISCONFIRMATION_LOG.md",
        "framework/templates/INFLUENCE_RECEIPT.md",
        "framework/templates/OUTCOME_REVIEW.md",
    ],
    "examples": [
        "manuscript/PATTERN_RECOGNITION_V16.md",
        "framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md",
        "cases/README.md",
        "cases/signal-foundry/README.md",
        "cases/general-research/README.md",
        "cases/product-and-process/README.md",
    ],
    "boundaries": [
        "framework/BOUNDARIES_AND_FAILURES.md",
        "docs/ARTIFACT_BOUNDARIES.md",
    ],
    "sources": [
        "manuscript/SOURCES_AND_RESEARCH_ROUTE.md",
        "docs/CLAIMS_AND_SOURCE_LEDGER_V16.md",
    ],
    "research": [
        "research/README.md",
        "research/THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md",
        "research/future-studies/DL_PLAYBOOK_MATCHED_BUDGET_PROTOCOL_V0_1.md",
        "research/the-echo-problem/README.md",
        "research/the-echo-problem/STATUS_AND_BOUNDARIES.md",
    ],
    "history": [
        "manuscript/ORIGIN_NOTE.md",
        "docs/SOURCE_AUTHORITY_AND_LINEAGE.md",
        "archive/README.md",
        "archive/v13/README.md",
        (
            "archive/transfers/v14-complete-2026-08-18/05_HISTORICAL_V13/"
            "LIVE_SITE_REFERENCE_MANIFEST.json"
        ),
        (
            "archive/transfers/v14-complete-2026-08-18/05_HISTORICAL_V13/"
            "pattern-recognition-diagram-v12.png"
        ),
    ],
}

EXPECTED_CLAIMS = [
    "six-families-are-not-claimed-as-new",
    "peripheral-is-candidate-not-truth",
    "provenance-is-not-correctness",
    "recurrence-is-not-independent-corroboration",
    "access-is-not-permission",
    "fixtures-protocols-validators-and-reviews-are-not-results",
    "signal-foundry-is-illustration-not-validation",
    "research-tracks-are-unrun-with-no-results",
    "human-judgment-and-consequential-authority-remain-human",
]

EXPECTED_ACTION_KEYS = {
    "merge_main",
    "deploy",
    "publish",
    "github_release",
    "replace_public_site",
    "empirical_study",
    "model_study",
    "participant_study",
    "provider_call",
    "paid_provider",
    "dataset_acquisition",
    "participant_activity",
    "preregister",
    "outreach_or_contact",
    "spend",
}

EXPECTED_REQUIRED_EXAMPLES = [
    "peripheral-or-specialist-candidate",
    "velocity-or-expected-absence-with-baseline",
    "common-origin-recurrence-with-unknown-independence",
]
EXPECTED_IMPLEMENTATION_LEVELS = ["ordinary", "lightweight", "moderate", "advanced"]
EXPECTED_REQUIRED_OUTPUTS = [
    "local-interactive-site",
    "standalone-html",
    "pdf-review-companion",
    "responsive-keyboard-screen-reader-print-qa",
]
EXPECTED_ESSENTIAL_WITHOUT_JS = [
    "human-problem",
    "broad-definition",
    "six-family-names-and-questions",
    "human-judgment-boundary",
    "implementation-levels",
]
EXPECTED_POPOVER_TERMS = [
    "Evidence spine",
    "Typed relationship",
    "Influence receipt",
    "Cost-bounded route",
    "Versioned memory",
    "Common origin",
    "Human disposition",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def words(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").split())


def main() -> None:
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    family_source = json.loads(FAMILIES_PATH.read_text(encoding="utf-8"))

    checkpoint_parts = OWNER_INTENT_CHECKPOINT_PATH.read_text(encoding="utf-8").split()
    require(len(checkpoint_parts) == 2, "owner-intent checkpoint must contain hash and filename")
    require(checkpoint_parts[1] == "OWNER_INTENT_V16.md",
            "owner-intent checkpoint names the wrong file")
    observed_owner_hash = hashlib.sha256(OWNER_INTENT_PATH.read_bytes()).hexdigest()
    for label, digest in (
        ("validator lock", LOCKED_OWNER_INTENT_SHA256),
        ("checked-in checkpoint", checkpoint_parts[0]),
        ("content interface", contract["owner_intent_sha256"]),
        ("current owner-intent file", observed_owner_hash),
    ):
        require(digest == LOCKED_OWNER_INTENT_SHA256,
                f"{label} differs from the locked owner-intent digest")

    require(contract["first_screen"] == EXPECTED_FIRST_SCREEN,
            "first-screen content or status changed")
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

    surfaces = {
        surface["id"]: surface
        for surface in contract["doors"] + contract["secondary_routes"]
    }
    require(set(surfaces) == set(EXPECTED_SOURCE_MANIFESTS),
            "content-interface source surface set changed")
    for surface_id, expected_sources in EXPECTED_SOURCE_MANIFESTS.items():
        require(surfaces[surface_id]["sources"] == expected_sources,
                f"source manifest changed for {surface_id}")

    family_projection = [
        {key: family[key] for key in ("id", "slug", "name", "reader_question")}
        for family in family_source["families"]
    ]
    require(family_projection == EXPECTED_FAMILIES,
            "canonical six-family source differs from the locked tuple")
    require(contract["families"] == EXPECTED_FAMILIES,
            "content-interface families differ from the locked tuple")
    for family in family_source["families"]:
        required_boundary = EXPECTED_FAMILY_BOUNDARIES[family["id"]]
        require(required_boundary in family["boundaries"],
                f"canonical boundary changed for {family['id']}")
    require(family_source["invariants"] == EXPECTED_INVARIANTS,
            "six-family invariants changed")

    source_paths = {
        relative
        for sources in EXPECTED_SOURCE_MANIFESTS.values()
        for relative in sources
    }
    source_paths.update(
        {
            contract["progressive_disclosure"]["popover_source"],
            contract["history"]["current_topology_source"],
            contract["visual_policy"]["image_ledger_path"],
        }
    )
    if contract["visual_policy"]["bitmap_requires_documented_need"]:
        source_paths.add(contract["visual_policy"]["visual_needs_path"])
    for relative in sorted(source_paths):
        require((ROOT / relative).is_file(), f"missing frozen source path: {relative}")

    visual_needs = (ROOT / contract["visual_policy"]["visual_needs_path"]).read_text(
        encoding="utf-8"
    )
    image_ledger = (ROOT / contract["visual_policy"]["image_ledger_path"]).read_text(
        encoding="utf-8"
    )
    generated_root = ROOT / "assets/generated-candidates"
    generated_candidates = [
        path for path in generated_root.rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    ]
    require("NO GENERATED BITMAP NEED JUSTIFIED" in visual_needs,
            "current visual-needs status no longer records the pre-site decision")
    for candidate in generated_candidates:
        relative = candidate.relative_to(ROOT).as_posix()
        require(relative in image_ledger or candidate.name in image_ledger,
                f"generated candidate lacks image-ledger entry: {relative}")

    headline = contract["first_screen"]["headline"]
    standfirst = contract["first_screen"]["standfirst"]
    require("before the model writes a word" in headline,
            "first screen no longer leads with the pre-generation problem")
    for phrase in ("generic", "upstream choices", "Pattern Recognition"):
        require(phrase in standfirst, f"standfirst lost required phrase: {phrase}")
    for prohibited in ("protocol", "provenance", "Echo Problem", "no results"):
        require(prohibited.lower() not in (headline + " " + standfirst).lower(),
                f"first screen leads with prohibited detail: {prohibited}")

    require(contract["required_examples"] == EXPECTED_REQUIRED_EXAMPLES,
            "required teaching-pattern set changed")
    require(contract["implementation_levels"] == EXPECTED_IMPLEMENTATION_LEVELS,
            "implementation-level set or order changed")
    require(contract["required_outputs"] == EXPECTED_REQUIRED_OUTPUTS,
            "site output obligations changed")
    require(contract["claims"] == EXPECTED_CLAIMS,
            "claim-boundary set or order changed")

    disclosure = contract["progressive_disclosure"]
    require(disclosure["essential_without_javascript"] == EXPECTED_ESSENTIAL_WITHOUT_JS,
            "no-script essential-content set changed")
    require(disclosure["popover_terms"] == EXPECTED_POPOVER_TERMS,
            "popover term set or order changed")
    require(disclosure["closed_controls_may_hide_required_qualifications"] is False,
            "closed controls may not hide required qualifications")
    glossary = (ROOT / disclosure["popover_source"]).read_text(encoding="utf-8")
    for term in EXPECTED_POPOVER_TERMS:
        require(term in glossary, f"glossary no longer contains popover term: {term}")

    require(contract["echo"] == {
        "principal_door": False,
        "placement": "secondary-research-route-and-late-common-origin-example",
        "required_label": "Separate project — unrun — no results",
        "removal_must_preserve_all_principal_routes": True,
    }, "Echo placement or status boundary changed")
    require(
        contract["history"]["v13_label"]
        == "Historical v13 origin — not the current v16 topology.",
        "historical v13 label changed",
    )
    history_sources = set(EXPECTED_SOURCE_MANIFESTS["history"])
    nonhistory_sources = source_paths - history_sources
    require(not any("05_HISTORICAL_V13" in path or path == "archive/v13/README.md"
                    for path in nonhistory_sources),
            "historical v13 source escaped the History route")

    action_map = contract["external_actions_authorized"]
    require(set(action_map) == EXPECTED_ACTION_KEYS,
            "external-action boundary key set changed")
    for action in sorted(EXPECTED_ACTION_KEYS):
        require(action_map[action] is False,
                f"external action unexpectedly authorized: {action}")

    echo_readme = (ROOT / "research/the-echo-problem/README.md").read_text(
        encoding="utf-8"
    ).lower()
    for phrase in ("separate", "unrun", "no results", "not published"):
        require(phrase in echo_readme, f"Echo README lost boundary phrase: {phrase}")
    signal_foundry = (ROOT / "cases/signal-foundry/README.md").read_text(
        encoding="utf-8"
    )
    require("ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION" in signal_foundry,
            "Signal Foundry case lost its illustration/non-validation status")

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
    for heading in (
        "#### Worked example 1: a specialist signal",
        "#### Worked example 2: motion and expected absence",
        "## A narrower example: nine reports, one announcement",
    ):
        require(heading in essay, f"essay lost required teaching pattern: {heading}")
    echo_position = essay.find("## A narrower example: nine reports, one announcement")
    require(echo_position > positions[-1],
            "common-origin example appears before the complete six-family map")

    implementation = (ROOT / "framework/IMPLEMENTATION_CHOICES.md").read_text(
        encoding="utf-8"
    ).lower()
    for level in EXPECTED_IMPLEMENTATION_LEVELS:
        require(level in implementation,
                f"implementation source lost required level: {level}")

    print("PASS  immutable owner-intent checkpoint and content-interface JSON")
    print("PASS  exact three-door, secondary-route, and source manifests")
    print("PASS  locked six-family identity, questions, boundaries, and invariants")
    print("PASS  human-problem first screen, examples, and late Echo placement")
    print("PASS  claim, no-script, visual, output, and external-action obligations")
    print(f"PASS  manuscript lengths: essay={words(essay_path)} raw words; short={words(short_path)} raw words")
    print("NOTE  rendered site, accessibility, print, removal, and reader gates remain open")


if __name__ == "__main__":
    main()
