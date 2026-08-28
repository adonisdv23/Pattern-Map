#!/usr/bin/env python3
"""Write or verify the bounded Pattern Map v16 owner-review manifest.

The manifest intentionally covers canonical review entry points and the
integrity ledgers/verifiers for the much larger immutable archives. It does not
duplicate every archive payload hash; those remain authoritative in their own
checked manifests.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "handoff" / "OWNER_REVIEW_MANIFEST_V16.json"
CONTENT_CHECKPOINT = "874a0a8e09f0bde11532cf873087865addb7d973"


REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    ".gitignore",
    "docs/OWNER_INTENT_V16.md",
    "docs/OWNER_INTENT_V16.sha256",
    "docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md",
    "docs/ARTIFACT_BOUNDARIES.md",
    "docs/TWO_PROJECT_SEPARATION.md",
    "docs/SOURCE_AUTHORITY_AND_LINEAGE.md",
    "docs/MIGRATION_INVENTORY.md",
    "docs/V13_TO_V16_FIDELITY_MATRIX.md",
    "docs/V16_ACCEPTANCE_CRITERIA.md",
    "docs/V16_ROADMAP.md",
    "docs/CONTENT_INTERFACE_FREEZE_V16.md",
    "docs/CONTENT_INTERFACE_V16.json",
    "docs/CLAIMS_AND_SOURCE_LEDGER_V16.md",
    "docs/ADVISORY_REVIEW_DISPOSITIONS.md",
    "docs/DECISION_LOG.md",
    "docs/REVIEW_AND_DISPOSITION_PROTOCOL.md",
    "docs/VERSION_HISTORY.md",
    "docs/BINARY_ARTIFACT_POLICY.md",
    "manuscript/PATTERN_RECOGNITION_V16.md",
    "manuscript/NINETY_SECOND_VERSION.md",
    "manuscript/MENTOR_COVER_NOTE.md",
    "manuscript/PUBLIC_ABSTRACT.md",
    "manuscript/ORIGIN_NOTE.md",
    "manuscript/SOURCES_AND_RESEARCH_ROUTE.md",
    "framework/SIX_FAMILIES.md",
    "framework/SIX_FAMILIES.json",
    "framework/SIX_FAMILIES.schema.json",
    "framework/RELATIONSHIP_MAP.md",
    "framework/GLOSSARY.md",
    "framework/OPERATOR_PLAYBOOK.md",
    "framework/IMPLEMENTATION_CHOICES.md",
    "framework/MECHANISMS.md",
    "framework/BOUNDARIES_AND_FAILURES.md",
    "framework/agent-playbook/QUICKSTART.md",
    "framework/agent-playbook/FULL_OPERATING_GUIDE.md",
    "framework/agent-playbook/COPYABLE_AGENT_BRIEF.md",
    "framework/agent-playbook/PREFLIGHT_CHECKLIST.md",
    "framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md",
    "framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md",
    "cases/signal-foundry/README.md",
    "cases/general-research/README.md",
    "cases/product-and-process/README.md",
    "handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md",
    "handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md",
    "handoff/signal-foundry/build_portable_bundle.py",
    "site/README.md",
    "site/package.json",
    "site/package-lock.json",
    "site/build.mjs",
    "site/check.mjs",
    "site/src/site.css",
    "site/src/site.js",
    "site/src/term-popover-geometry.js",
    "site/src/recommendation.js",
    "site/scripts/generate_review_pdf.py",
    "site/exports/standalone/pattern-map-v16.html",
    "site/exports/pattern-map-v16-owner-review.pdf",
    "research/README.md",
    "research/THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md",
    "research/future-studies/DL_PLAYBOOK_MATCHED_BUDGET_PROTOCOL_V0_1.md",
    "research/the-echo-problem/README.md",
    "research/the-echo-problem/STATUS_AND_BOUNDARIES.md",
    "research/the-echo-problem/RELATION_TO_V16.md",
    "research/the-echo-problem/VERSION_HISTORY.md",
    "research/the-echo-problem/FUTURE_EXECUTION_PLAN.md",
    "research/the-echo-problem/PRESERVED_V15_2_INDEX.md",
    "research/the-echo-problem/qa/EP_V0_1_QA.md",
    "research/the-echo-problem/qa/EP_V0_1_STATUS.json",
    "research/the-echo-problem/qa/verify_preserved_sources.py",
    "research/the-echo-problem/v1_1/README.md",
    "research/the-echo-problem/v1_1/PROTOCOL_V1_1_DESIGN_CHECKPOINT.md",
    "research/the-echo-problem/v1_1/PRIOR_MEASUREMENT_MATRIX.md",
    "research/the-echo-problem/v1_1/fixtures/CLAUDE_PRIMARY_RENDER_AUDIT_SEED1_N300.json",
    "research/the-echo-problem/v1_1/harness/README.md",
    "research/the-echo-problem/v1_1/harness/__init__.py",
    "research/the-echo-problem/v1_1/harness/canonical.py",
    "research/the-echo-problem/v1_1/harness/generate_claude_primary_fixture.py",
    "research/the-echo-problem/v1_1/harness/parity.py",
    "research/the-echo-problem/v1_1/harness/parser.py",
    "research/the-echo-problem/v1_1/harness/planning.py",
    "research/the-echo-problem/v1_1/harness/scoring.py",
    "research/the-echo-problem/v1_1/harness/test_v1_1.py",
    "assets/IMAGE_USE_LEDGER.md",
    "assets/diagrams/historical-v13-pattern-recognition-diagram-v12.png",
    "archive/CHECKPOINT_INDEX.json",
    "archive/verify_checkpoint_index.py",
    "archive/transfers/v14-complete-2026-08-18/00_START_HERE/PACKAGE_MANIFEST.md",
    "archive/transfers/v14-complete-2026-08-18/00_START_HERE/SHA256SUMS.txt",
    "archive/transfers/v15.2-owner-handoff/ACCESSION_RECORD.md",
    "archive/transfers/v15.2-owner-handoff/PATTERN_MAP_V15_2_OWNER_HANDOFF-manifest.json",
    "archive/transfers/v15.2-owner-handoff/PATTERN_MAP_V15_2_OWNER_HANDOFF.zip.sha256",
    "archive/transfers/v15.2-owner-handoff/RECONSTRUCTION_GUIDE.md",
    "archive/transfers/v15.2-owner-handoff/verify_accession.py",
    "qa/FINAL_ACCEPTANCE_MATRIX_V16.md",
    "qa/FINAL_ACTION_AUDIT_V16.md",
    "qa/README.md",
    "qa/run_owner_review_checks.sh",
    "qa/editorial/MANUSCRIPT_QA_REPORT.md",
    "qa/editorial/validate_content_interface.py",
    "qa/applied/README.md",
    "qa/applied/validate_framework.py",
    "qa/applied/receipts/blocked-permission.json",
    "qa/applied/receipts/layered-ready.json",
    "qa/applied/receipts/lightweight-low-stakes.json",
    "qa/applied/receipts/ordinary-supplied-material.json",
    "qa/applied/receipts/stopped-budget.json",
    "qa/handoff/POST_ULTRACODE_FINALIZATION_QA_2026-08-28.md",
    "qa/research/validate_research_boundaries.py",
    "qa/research/ECHO_V1_1_DESIGN_CHECKPOINT_QA_2026-08-23.md",
    "qa/site/SITE_QA_REPORT.md",
    "qa/site/SITE_POLISH_QA.md",
    "qa/site/audit_site.py",
    "qa/site/LIVE_BROWSER_BOUNDARY_CHECK_2026-08-19_79a2392.md",
    "qa/site/PRO_ROUND_1_CORRECTION_QA_2026-08-20_5eb860e.md",
    "qa/site/PRO_ROUND_2_CORRECTION_QA_2026-08-22_c889260.md",
    "qa/site/TERMINAL_FINALIZATION_QA_2026-08-27.md",
    "qa/site/advisory/CLAUDE_TERMINAL_AUDIT_2026-08-27_e565502.md",
    "qa/site/advisory/CHATGPT_PRO_INDEPENDENT_REVIEW_2026-08-20_cc5547d.md",
    "qa/site/advisory/CHATGPT_PRO_INDEPENDENT_REVIEW_ROUND_2_2026-08-22_4d2505e.md",
    "qa/site/advisory/SITE_VISUAL_EXPERIENCE_POST_POLISH_2026-08-19_a319794.md",
    "qa/interaction/apply-state-contract.spec.mjs",
    "qa/interaction/map-layout-contract.spec.mjs",
    "qa/interaction/term-popover-geometry-contract.spec.mjs",
    "qa/handoff/test_portable_bundle.py",
    "qa/content/reader-language-contract.spec.mjs",
    "qa/visual/README.md",
    "qa/visual/POLISH_PLAN.md",
    "qa/visual/VISUAL_NEEDS.md",
    "qa/visual/VISUAL_QA_REPORT.md",
    "qa/visual/VISUAL_EXPERIENCE_REVISION_REPORT.md",
    "qa/site/SITE_HYGIENE_QA_2026-08-23_d4b7b9e.md",
    "qa/site/css-selector-use.spec.mjs",
    "qa/visual/verify_image_formats.py",
    "qa/visual/screenshots/home-desktop-1440x1000.jpg",
    "qa/visual/screenshots/home-tablet-1024x768.jpg",
    "qa/visual/screenshots/home-mobile-390x844.jpg",
    "qa/visual/screenshots/map-desktop-1440x1000.jpg",
    "qa/visual/screenshots/apply-tablet-1024x768.jpg",
    "qa/visual/screenshots/history-desktop-1440x1000.jpg",
    "qa/visual/screenshots/history-full.jpg",
    "qa/visual/screenshots-final-v16-polish/home-1440x900.jpg",
    "qa/visual/screenshots-final-v16-polish/home-1280x720.jpg",
    "qa/visual/screenshots-final-v16-polish/home-1024x768.jpg",
    "qa/visual/screenshots-final-v16-polish/home-768x1024.jpg",
    "qa/visual/screenshots-final-v16-polish/home-390x844.jpg",
    "qa/visual/screenshots-final-v16-polish/home-360x800.jpg",
    "qa/visual/screenshots-final-v16-polish/read-1440x900.jpg",
    "qa/visual/screenshots-final-v16-polish/read-390x844.jpg",
    "qa/visual/screenshots-final-v16-polish/map-1440x900.jpg",
    "qa/visual/screenshots-final-v16-polish/map-1280x720.jpg",
    "qa/visual/screenshots-final-v16-polish/map-1024x768.jpg",
    "qa/visual/screenshots-final-v16-polish/map-768x1024.jpg",
    "qa/visual/screenshots-final-v16-polish/map-390x844.jpg",
    "qa/visual/screenshots-final-v16-polish/map-360x800.jpg",
    "qa/visual/screenshots-final-v16-polish/apply-1440x900.jpg",
    "qa/visual/screenshots-final-v16-polish/apply-1280x720.jpg",
    "qa/visual/screenshots-final-v16-polish/apply-1024x768.jpg",
    "qa/visual/screenshots-final-v16-polish/apply-768x1024.jpg",
    "qa/visual/screenshots-final-v16-polish/apply-390x844.jpg",
    "qa/visual/screenshots-final-v16-polish/apply-360x800.jpg",
    "qa/visual/screenshots-final-v16-polish/examples-1440x900.jpg",
    "qa/visual/screenshots-final-v16-polish/examples-390x844.jpg",
    "qa/visual/screenshots-final-v16-polish/boundaries-1440x900.jpg",
    "qa/visual/screenshots-final-v16-polish/sources-1440x900.jpg",
    "qa/visual/screenshots-final-v16-polish/research-1440x900.jpg",
    "qa/visual/screenshots-final-v16-polish/history-1440x900.jpg",
    "qa/visual/screenshots-final-v16-polish/interaction-states/map-f1-focused-1280x720.jpg",
    "qa/visual/screenshots-final-v16-polish/interaction-states/apply-advanced-hold-1280x720.jpg",
    "qa/visual/screenshots-final-v16-polish/interaction-states/standalone-all-routes-1280x720.jpg",
    "qa/visual/pdf-renders/pattern-map-v16-owner-review-final-1.png",
    "qa/visual/pdf-renders/pattern-map-v16-owner-review-final-2.png",
    "qa/visual/pdf-renders/pattern-map-v16-owner-review-final-3.png",
    "qa/visual/pdf-renders/pattern-map-v16-owner-review-final-4.png",
    "qa/visual/pdf-renders/pattern-map-v16-owner-review-final-5.png",
    "qa/visual/pdf-renders/pattern-map-v16-owner-review-final-6.png",
    "qa/visual/pdf-renders-final-v16-polish/page-1.png",
    "qa/visual/pdf-renders-final-v16-polish/page-2.png",
    "qa/visual/pdf-renders-final-v16-polish/page-3.png",
    "qa/visual/pdf-renders-final-v16-polish/page-4.png",
    "qa/visual/pdf-renders-final-v16-polish/page-5.png",
    "qa/visual/pdf-renders-final-v16-polish/page-6.png",
    "qa/research/advisory/PRIOR_ART_AND_OVERCLAIM_BOUNDARY_2026-08-19_ea8a6e2.md",
    "qa/research/advisory/HOSTILE_NOVELTY_REVIEW_2026-08-19_6a29ed8.md",
    "qa/applied/advisory/BUILDER_OPERATOR_ACCEPTANCE_2026-08-19_6a29ed8.md",
    "qa/applied/advisory/APPLIED_RENDERED_POST_REVISION_VERIFICATION_2026-08-19_8aa5f94.md",
    "qa/applied/advisory/APPLIED_FINAL_REGRESSION_CHECK_2026-08-19_2a54b24.md",
    "qa/editorial/advisory/COLD_NONTECHNICAL_READER_2026-08-19_6a29ed8.md",
    "qa/editorial/advisory/COLD_READER_POST_REVISION_VERIFICATION_2026-08-19_2a54b24.md",
    "qa/site/advisory/SITE_COMPREHENSION_ACCESSIBILITY_2026-08-19_6a29ed8.md",
    "qa/site/advisory/SITE_POST_REVISION_VERIFICATION_2026-08-19_2a54b24.md",
    "qa/site/OWNER_VISUAL_EXPORT_CLOSEOUT_2026-08-23.md",
    "handoff/README.md",
    "handoff/OWNER_REVIEW_PACKET_V16.md",
    "handoff/PACKAGE_MAP_V16.md",
    "handoff/BRANCH_AND_PR_STATE.md",
    "handoff/verify_owner_review_package.py",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def current_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for relative in sorted(REQUIRED_PATHS):
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(f"required owner-review artifact missing: {relative}")
        records.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        )
    return records


def write_manifest() -> None:
    records = current_records()
    payload = {
        "schema_version": 1,
        "package": "pattern-map-v16-owner-review",
        "status": "owner-review candidate; not merged, deployed, published, or empirically validated",
        "generated_date": "2026-08-28",
        "content_site_source_and_pdf_checkpoint": CONTENT_CHECKPOINT,
        "evidence_note": "The manifest covers canonical content checkpoint 874a0a8 plus the post-Ultracode reusable-contract source checkpoint c86e537: the prior ChatGPT Pro and owner visual/export corrections; exhaustive 108-case Stage 0/permission/state behavior; a genuine ordinary supplied-material receipt; F2 role/track-record/claim-authority separation; fail-closed reviewed learning and selected influence; exact ordered F1-F6 schema identity; descriptive no-script term help; responsive line-free Map; flow-native common-origin teaching visual; measured desktop term-panel clearance and viewport clamping; structurally contained human-first standalone routes with contrast-safe demoted callout headings; a non-overlapping normal-flow Home Apply preview; print-safe evidence routes and tables; fresh-clone-safe Signal Foundry handoffs; all-payload portable marker scanning; deterministic exact-commit bundle construction; EP v1.1 design, strict offline harness, frozen 300-pair render fixture, and claim dispositions; the six-page review companion; and the evidence index that labels a319794 routed-site captures as historical and superseded for current Map/Apply semantics. Manual owner/keyboard/screen-reader/real-zoom/forced-colors/native-print/touch gates remain open. Claude and Luna reviews were advisory only. No study, deployment, publication, merge, research-provider selection/call, or incremental spend is implied.",
        "archive_scope": "Key ledgers and verifiers are included here; immutable archive payload hashes remain authoritative in their own manifests.",
        "file_count": len(records),
        "total_bytes": sum(int(record["bytes"]) for record in records),
        "files": records,
    }
    MANIFEST.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"WROTE {MANIFEST.relative_to(ROOT)}: {len(records)} files / {payload['total_bytes']} bytes")


def verify_manifest() -> None:
    if not MANIFEST.is_file():
        raise FileNotFoundError(f"manifest missing: {MANIFEST.relative_to(ROOT)}")
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected = current_records()
    if payload.get("schema_version") != 1:
        raise AssertionError("unsupported owner-review manifest schema")
    if payload.get("content_site_source_and_pdf_checkpoint") != CONTENT_CHECKPOINT:
        raise AssertionError("content checkpoint mismatch")
    if payload.get("files") != expected:
        raise AssertionError("owner-review manifest does not match current artifact bytes")
    if payload.get("file_count") != len(expected):
        raise AssertionError("owner-review manifest file count mismatch")
    total = sum(int(record["bytes"]) for record in expected)
    if payload.get("total_bytes") != total:
        raise AssertionError("owner-review manifest byte count mismatch")
    print(f"PASS owner-review manifest: {len(expected)} files / {total} bytes")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="rewrite the deterministic manifest from current files")
    args = parser.parse_args()
    if args.write:
        write_manifest()
    else:
        verify_manifest()


if __name__ == "__main__":
    main()
