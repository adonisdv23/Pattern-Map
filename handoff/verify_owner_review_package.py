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
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "handoff" / "OWNER_REVIEW_MANIFEST_V16.json"
CONTENT_CHECKPOINT = "874a0a8e09f0bde11532cf873087865addb7d973"
OWNER_REVIEW_PDF_CHECKPOINT = "06c61680f709861ccd3ffd2df5029e04c63cb450"
PHASE_0_BASELINE = "37c7c852ff406431454346eacc694ac04c5f57a5"
LANE_HEADS = {
    "applied_integrity": "93265692e95d56e35f8de68afcc435519419684b",
    "public_presentation": "361243c95050723f1693907f7446be5d690b9e58",
    "research_boundary_2026": "54bd0a7a11f4c072c8ceaab1a2abf7bc81a380cb",
}
CONVERGENCE_CORRECTION_HEADS = {
    "public_release_url_semantics": "c4a0f4c62e71cb2475f286f67ae0254a13f130a3",
    "research_protocol_axis_alignment": "ecf37ee64adfeb1847a5b6342d7550f7f5da6695",
    "stage_zero_contract_convergence": "1ceceb6c8b7131217c3e7c710976d868c3139260",
    "research_claim_convergence": "280eb4bc4a2eb910535b61a480226de5b4aac33f",
    "public_site_apply_convergence": "5bcd08df150f385c2bb3471a4a641a7ce9cb356d",
}
OPPORTUNITY_EXPANSION_BASELINE = "529852497109dc152928de642038d07b109a52e2"
OPPORTUNITY_EXPANSION_LANE_HEADS = {
    "project_use_starter": "9ed522afcacaa45e9bfa5950f03f454a87e3dd92",
    "public_mentor_rehearsal": "f2311d095d0afc094356e222624cff3aa1e3b939",
    "research_opportunity_scan": "30d4af6564e07154f0f60e8fd2d8a59f3c815944",
}
OPPORTUNITY_LOOP_2_REVIEWED_HEAD = "2b2d1bad8e9b7c954f209f0c9c6e0cfbc9d4815b"


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
    "docs/PUBLIC_AND_TRANSFER_HARDENING_PLAN_V16.md",
    "docs/OPPORTUNITY_EXPANSION_LOOPS_V16.md",
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
    "framework/templates/README.md",
    "framework/templates/ACQUISITION_RECEIPT.md",
    "framework/templates/COMPARISON_MATRIX.md",
    "framework/templates/DECISION_BRIEF.md",
    "framework/templates/DISCONFIRMATION_LOG.md",
    "framework/templates/EVIDENCE_REGISTER.md",
    "framework/templates/INFLUENCE_RECEIPT.md",
    "framework/templates/MEMORY_RECORD.md",
    "framework/templates/ORDINARY_RECORD.md",
    "framework/templates/OUTCOME_REVIEW.md",
    "framework/agent-playbook/QUICKSTART.md",
    "framework/agent-playbook/PROJECT_USE_STARTER.md",
    "framework/agent-playbook/FULL_OPERATING_GUIDE.md",
    "framework/agent-playbook/COPYABLE_AGENT_BRIEF.md",
    "framework/agent-playbook/PREFLIGHT_CHECKLIST.md",
    "framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md",
    "framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md",
    "cases/signal-foundry/README.md",
    "cases/general-research/README.md",
    "cases/product-and-process/README.md",
    "publication/README.md",
    "publication/MENTOR_REVIEW_SEQUENCE_V16.md",
    "publication/X_COPY_VARIANTS_V16.md",
    "publication/RELEASE_DECISION_CHECKLIST_V16.md",
    "handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md",
    "handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md",
    "handoff/signal-foundry/build_portable_bundle.py",
    "site/README.md",
    "site/.gitignore",
    "site/package.json",
    "site/package-lock.json",
    "site/build.mjs",
    "site/check.mjs",
    "site/serve.mjs",
    "site/publication.config.json",
    "site/src/publication-config.mjs",
    "site/src/site.css",
    "site/src/site.js",
    "site/src/term-popover-geometry.js",
    "site/src/recommendation.js",
    "site/scripts/generate_review_pdf.py",
    "site/exports/standalone/pattern-map-v16.html",
    "site/exports/standalone/pattern-map-v16-public.html",
    "site/exports/pattern-map-v16-owner-review.pdf",
    "research/README.md",
    "research/THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md",
    "research/future-studies/DL_PLAYBOOK_MATCHED_BUDGET_PROTOCOL_V0_1.md",
    "research/future-studies/DL_NARROW_WEDGE_DECISION_MEMO_V0_1.md",
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
    "qa/editorial/advisory/FINAL_INTENT_READER_REDTEAM_2026-08-30_d40ca61.md",
    "qa/editorial/advisory/FINAL_INTENT_READER_RECHECK_2026-08-30_6a61f6d.md",
    "qa/editorial/advisory/FINAL_INTENT_READER_RECHECK_2026-08-30_58f2756.md",
    "qa/applied/README.md",
    "qa/applied/PUBLIC_TRANSFER_APPLIED_INTEGRITY_QA_2026-08-30.md",
    "qa/applied/PROJECT_USE_COLD_START_QA_2026-08-30_d05aca5.md",
    "qa/applied/STAGE_ZERO_ORDINARY_CONTRACT_CONVERGENCE_QA_2026-08-30_0beee9a.md",
    "qa/applied/memory_anchor_registry.json",
    "qa/applied/validate_framework.py",
    "qa/applied/advisory/PUBLIC_MENTOR_KIT_CROSS_LANE_CHALLENGE_2026-08-30_f2311d0.md",
    "qa/applied/advisory/OPPORTUNITY_LOOP2_REMOVAL_TRANSFER_2026-08-30_2b2d1ba.md",
    "qa/applied/receipts/blocked-permission.json",
    "qa/applied/receipts/layered-ready.json",
    "qa/applied/receipts/lightweight-low-stakes.json",
    "qa/applied/receipts/memory-append-only-correction.json",
    "qa/applied/receipts/ordinary-supplied-material.json",
    "qa/applied/receipts/revoked-permission.json",
    "qa/applied/receipts/stopped-budget.json",
    "qa/applied/receipts/unknown-permission.json",
    "qa/handoff/POST_ULTRACODE_FINALIZATION_QA_2026-08-28.md",
    "qa/handoff/PUBLIC_AND_TRANSFER_HARDENING_QA_2026-08-30.md",
    "qa/handoff/FINAL_RED_TEAM_CORRECTION_QA_2026-08-30.md",
    "qa/handoff/OPPORTUNITY_EXPANSION_TERMINAL_QA_2026-08-30.md",
    "qa/handoff/advisory/CLAUDE_PUBLIC_TRANSFER_TERMINAL_AUDIT_2026-08-30_fb7d808.md",
    "qa/handoff/advisory/CLAUDE_PUBLIC_TRANSFER_TERMINAL_RECHECK_2026-08-30_4a1acab.md",
    "qa/research/validate_research_boundaries.py",
    "qa/research/README.md",
    "qa/research/CURRENT_ADJACENT_SOURCE_VERIFICATION_2026-08-30.md",
    "qa/research/RESEARCH_CLAIM_CONVERGENCE_QA_2026-08-30_0beee9a.md",
    "qa/research/RESEARCH_BOUNDARY_HARDENING_QA_2026-08-30.md",
    "qa/research/OPPORTUNITY_SOURCE_SCAN_2026-08-30_d05aca5.md",
    "qa/research/ECHO_V1_1_DESIGN_CHECKPOINT_QA_2026-08-23.md",
    "qa/research/test_research_claim_convergence.py",
    "qa/research/advisory/FINAL_RESEARCH_PROVENANCE_REDTEAM_2026-08-30_d40ca61.md",
    "qa/research/advisory/FINAL_RESEARCH_PROVENANCE_RECHECK_2026-08-30_6a61f6d.md",
    "qa/research/advisory/PROJECT_USE_STARTER_CROSS_LANE_CHALLENGE_2026-08-30_9ed522a.md",
    "qa/research/advisory/OPPORTUNITY_LOOP2_CLAIMS_BOUNDARY_2026-08-30_2b2d1ba.md",
    "qa/site/SITE_QA_REPORT.md",
    "qa/site/SITE_POLISH_QA.md",
    "qa/site/audit_site.py",
    "qa/site/LIVE_BROWSER_BOUNDARY_CHECK_2026-08-19_79a2392.md",
    "qa/site/PRO_ROUND_1_CORRECTION_QA_2026-08-20_5eb860e.md",
    "qa/site/PRO_ROUND_2_CORRECTION_QA_2026-08-22_c889260.md",
    "qa/site/TERMINAL_FINALIZATION_QA_2026-08-27.md",
    "qa/site/PUBLIC_MODE_BROWSER_QA_2026-08-30.md",
    "qa/site/OWNER_REPORTED_DOOR_CARD_CORRECTION_2026-08-30.md",
    "qa/site/FINAL_CONVERGENCE_SITE_QA_2026-08-30_5bcd08d.md",
    "qa/site/public-mode-contract.spec.mjs",
    "qa/site/public-nav-spacing-contract.spec.mjs",
    "qa/site/door-card-preview-contract.spec.mjs",
    "qa/site/advisory/FINAL_APPLIED_SITE_REDTEAM_2026-08-30_d40ca61.md",
    "qa/site/advisory/FINAL_APPLIED_SITE_RECHECK_2026-08-30_6a61f6d.md",
    "qa/site/advisory/CLAUDE_TERMINAL_AUDIT_2026-08-27_e565502.md",
    "qa/site/advisory/CHATGPT_PRO_INDEPENDENT_REVIEW_2026-08-20_cc5547d.md",
    "qa/site/advisory/CHATGPT_PRO_INDEPENDENT_REVIEW_ROUND_2_2026-08-22_4d2505e.md",
    "qa/site/advisory/SITE_VISUAL_EXPERIENCE_POST_POLISH_2026-08-19_a319794.md",
    "qa/interaction/apply-state-contract.spec.mjs",
    "qa/interaction/apply-cross-artifact-contract.spec.mjs",
    "qa/interaction/map-layout-contract.spec.mjs",
    "qa/interaction/term-popover-geometry-contract.spec.mjs",
    "qa/handoff/test_portable_bundle.py",
    "qa/handoff/CLAUDE_FINAL_PORTABLE_AUDIT_DISPOSITION_2026-08-30_c23c665.md",
    "qa/content/reader-language-contract.spec.mjs",
    "qa/publication/OPPORTUNITY_EXPANSION_PUBLIC_MENTOR_REHEARSAL_QA_2026-08-30_d05aca5.md",
    "qa/publication/publication-kit-contract.spec.mjs",
    "qa/publication/advisory/PROJECT_USE_STARTER_PUBLIC_LANE_CHALLENGE_2026-08-30_9ed522a.md",
    "qa/publication/advisory/OPPORTUNITY_LOOP2_PUBLIC_MENTOR_2026-08-30_2b2d1ba.md",
    "qa/visual/README.md",
    "qa/visual/POLISH_PLAN.md",
    "qa/visual/VISUAL_NEEDS.md",
    "qa/visual/VISUAL_QA_REPORT.md",
    "qa/visual/opportunity-final/README.md",
    "qa/visual/opportunity-final/public-home-1280x720.jpg",
    "qa/visual/opportunity-final/public-home-390x844.jpg",
    "qa/visual/opportunity-final/public-map-1280x720.jpg",
    "qa/visual/opportunity-final/public-map-detail-1280x720.jpg",
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
    "qa/visual/public-mode/public-apply-stage0-1280x720.jpg",
    "qa/visual/public-mode/public-home-reveal-1280x720.jpg",
    "qa/visual/public-mode/public-home-reveal-390x844.jpg",
    "qa/visual/public-mode/public-read-1280x720.jpg",
    "qa/visual/public-mode/public-read-390x844.jpg",
    "qa/visual/final-redteam/public-home-1440x720.jpg",
    "qa/visual/final-redteam/public-home-reveal-1440x720.jpg",
    "qa/visual/final-redteam/public-map-f2-1440x720.jpg",
    "qa/visual/final-redteam/public-map-f2-390x844.jpg",
    "qa/visual/final-redteam/public-common-origin-1440x720.jpg",
    "qa/visual/final-redteam/public-common-origin-390x844.jpg",
    "qa/visual/final-redteam/public-apply-advanced-hold-1440x720.jpg",
    "qa/visual/final-redteam/public-apply-advanced-hold-390x844.jpg",
    "qa/visual/final-redteam/standalone-sources-1440x720.jpg",
    "qa/visual/final-redteam/standalone-history-1440x720.jpg",
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


def assert_pdf_checkpoint_bound() -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", OWNER_REVIEW_PDF_CHECKPOINT):
        raise AssertionError(
            "owner-review PDF checkpoint is pending; commit regenerated PDF bytes, "
            "then bind that exact producer commit before writing or verifying the manifest"
        )


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
    assert_pdf_checkpoint_bound()
    records = current_records()
    payload = {
        "schema_version": 2,
        "package": "pattern-map-v16-owner-review",
        "status": "owner-review candidate; not merged, deployed, published, or empirically validated",
        "generated_date": "2026-08-30",
        "historical_converged_checkpoint": CONTENT_CHECKPOINT,
        "owner_review_pdf_checkpoint": OWNER_REVIEW_PDF_CHECKPOINT,
        "phase_0_hardening_baseline": PHASE_0_BASELINE,
        "integrated_lane_heads": LANE_HEADS,
        "convergence_correction_heads": CONVERGENCE_CORRECTION_HEADS,
        "opportunity_expansion_baseline": OPPORTUNITY_EXPANSION_BASELINE,
        "opportunity_expansion_lane_heads": OPPORTUNITY_EXPANSION_LANE_HEADS,
        "opportunity_loop_2_reviewed_head": OPPORTUNITY_LOOP_2_REVIEWED_HEAD,
        "source_head": None,
        "source_head_resolution": {
            "status": "resolve_at_use",
            "command": "git rev-parse --verify HEAD",
            "sealed_signal_bundle_field": "BUNDLE_METADATA.json.source_commit",
        },
        "evidence_note": "This manifest covers the locked human thesis and six-family content; the preserved Echo boundary; the shared-source review/public site and deterministic teaching reveal; fail-closed publication metadata and semantic headings; a genuine four-field ordinary route; typed permission, resolvable comparison/disconfirmation, real UTC motion instants, selected influence, and append-only current-memory fixtures; the targeted 2025–2026 adjacent-work boundary and two unrun study-mode candidates; the optional repository-local project-use starter; the unpublished mentor/X/release-decision rehearsal kit; the supplemental targeted opportunity source scan; two post-build opportunity/red-team loops; exact-commit Signal Foundry subset construction with classified out-of-packet links; and the regenerated six-page review PDF. Manual owner/mentor comprehension, physical keyboard, supported screen reader, real zoom, forced colors, native print, hardware touch, byline, canonical URL, social image, and publication-time link checks remain open. Agent and Claude reviews are advisory only. No study, deployment, publication, merge, research-provider selection/call, external dataset acquisition, outreach, or incremental spend is implied.",
        "archive_scope": "Key ledgers and verifiers are included here; immutable archive payload hashes remain authoritative in their own manifests.",
        "file_count": len(records),
        "total_bytes": sum(int(record["bytes"]) for record in records),
        "files": records,
    }
    MANIFEST.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"WROTE {MANIFEST.relative_to(ROOT)}: {len(records)} files / {payload['total_bytes']} bytes")


def verify_manifest() -> None:
    assert_pdf_checkpoint_bound()
    if not MANIFEST.is_file():
        raise FileNotFoundError(f"manifest missing: {MANIFEST.relative_to(ROOT)}")
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected = current_records()
    if payload.get("schema_version") != 2:
        raise AssertionError("unsupported owner-review manifest schema")
    if payload.get("historical_converged_checkpoint") != CONTENT_CHECKPOINT:
        raise AssertionError("historical converged checkpoint mismatch")
    if payload.get("owner_review_pdf_checkpoint") != OWNER_REVIEW_PDF_CHECKPOINT:
        raise AssertionError("owner-review PDF checkpoint mismatch")
    if payload.get("phase_0_hardening_baseline") != PHASE_0_BASELINE:
        raise AssertionError("Phase 0 hardening checkpoint mismatch")
    if payload.get("integrated_lane_heads") != LANE_HEADS:
        raise AssertionError("integrated lane-head provenance mismatch")
    if payload.get("convergence_correction_heads") != CONVERGENCE_CORRECTION_HEADS:
        raise AssertionError("convergence-correction provenance mismatch")
    if payload.get("opportunity_expansion_baseline") != OPPORTUNITY_EXPANSION_BASELINE:
        raise AssertionError("opportunity-expansion baseline mismatch")
    if payload.get("opportunity_expansion_lane_heads") != OPPORTUNITY_EXPANSION_LANE_HEADS:
        raise AssertionError("opportunity-expansion lane provenance mismatch")
    if payload.get("opportunity_loop_2_reviewed_head") != OPPORTUNITY_LOOP_2_REVIEWED_HEAD:
        raise AssertionError("opportunity Loop 2 reviewed-head mismatch")
    if payload.get("source_head") is not None:
        raise AssertionError("owner-review manifest must not hard-code its self-referential source head")
    resolution = payload.get("source_head_resolution")
    expected_resolution = {
        "status": "resolve_at_use",
        "command": "git rev-parse --verify HEAD",
        "sealed_signal_bundle_field": "BUNDLE_METADATA.json.source_commit",
    }
    if resolution != expected_resolution:
        raise AssertionError("source-head resolution contract mismatch")
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
    try:
        if args.write:
            write_manifest()
        else:
            verify_manifest()
    except (AssertionError, FileNotFoundError, json.JSONDecodeError, OSError) as exc:
        raise SystemExit(f"FAIL owner-review manifest: {exc}") from None


if __name__ == "__main__":
    main()
