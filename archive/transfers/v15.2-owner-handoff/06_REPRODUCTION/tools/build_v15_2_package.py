#!/usr/bin/env python3
"""Build deterministic Pattern Map v15.2 owner and PDF review archives."""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath

import build_v15_1_package as base


ROOT = base.ROOT
OUTPUT = ROOT / "output"
MAIN_ZIP = OUTPUT / "PATTERN_MAP_V15_2_OWNER_HANDOFF.zip"
MAIN_SIDECAR = OUTPUT / "PATTERN_MAP_V15_2_OWNER_HANDOFF.zip.sha256"
EXTERNAL_MANIFEST = OUTPUT / "PATTERN_MAP_V15_2_OWNER_HANDOFF-manifest.json"
PDF_ZIP = OUTPUT / "PATTERN_MAP_V15_2_PDF_REVIEW.zip"
PDF_SIDECAR = OUTPUT / "PATTERN_MAP_V15_2_PDF_REVIEW.zip.sha256"
ARCHIVE_ROOT = "Pattern-Map-v15.2"


def _drop(payload: dict[PurePosixPath, Path], destination: str) -> None:
    payload.pop(PurePosixPath(destination), None)


def collect_payload() -> dict[PurePosixPath, Path]:
    payload = base.collect_payload()

    # Replace the prior release's orientation and final surfaces while keeping
    # its records under explicit history paths.
    for destination in (
        "00_START_HERE/README.md",
        "00_START_HERE/OWNER_REVIEW_PACKET_V15_1.md",
        "00_START_HERE/PACKAGE_MAP_V15_1.md",
        "01_FINAL_OUTPUT/canonical-manuscript/THOUGHT_PIECE_V15.md",
        "01_FINAL_OUTPUT/visual-review/PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf",
        "02_CANONICAL_FRAMEWORK/source/READER_OUTCOME_AND_READING_PATH_V15_1.md",
    ):
        _drop(payload, destination)

    base.add_file(
        payload,
        "handoff/ARCHIVE_README_V15_2.md",
        "00_START_HERE/README.md",
    )
    base.add_file(
        payload,
        "README.md",
        "06_REPRODUCTION/REPOSITORY_README.md",
    )

    base.add_file(
        payload,
        "handoff/OWNER_REVIEW_PACKET_V15_2.md",
        "00_START_HERE/OWNER_REVIEW_PACKET_V15_2.md",
    )
    base.add_file(
        payload,
        "handoff/PACKAGE_MAP_V15_2.md",
        "00_START_HERE/PACKAGE_MAP_V15_2.md",
    )
    base.add_file(
        payload,
        "handoff/PDF_REVIEW_INDEX_V15_2.md",
        "00_START_HERE/PDF_REVIEW_INDEX_V15_2.md",
    )
    base.add_file(
        payload,
        "handoff/REASONING_AND_LOGIC_V15_2.md",
        "00_START_HERE/REASONING_AND_LOGIC_V15_2.md",
    )
    base.add_file(
        payload,
        "handoff/VERSION_HISTORY_V15_2.md",
        "00_START_HERE/VERSION_HISTORY_V15_2.md",
    )

    base.add_tree(
        payload,
        "output/v15_2/standalone",
        "01_FINAL_OUTPUT/standalone-site",
    )
    base.add_file(
        payload,
        "source/THOUGHT_PIECE_V15_2.md",
        "01_FINAL_OUTPUT/canonical-manuscript/THOUGHT_PIECE_V15_2.md",
    )
    base.add_file(
        payload,
        "output/pdf/PATTERN_MAP_V15_2_REVIEW_COMPANION.pdf",
        "01_FINAL_OUTPUT/pdf-review/PATTERN_MAP_V15_2_REVIEW_COMPANION.pdf",
    )
    base.add_file(
        payload,
        "source/READER_OUTCOME_AND_READING_PATH_V15_2.md",
        "02_CANONICAL_FRAMEWORK/source/READER_OUTCOME_AND_READING_PATH_V15_2.md",
    )

    # The base builder names the editable source simply `site/`; rename the
    # archive destination to make its role unmistakable.
    renamed: dict[PurePosixPath, Path] = {}
    for target, source in list(payload.items()):
        text = target.as_posix()
        if text.startswith("01_FINAL_OUTPUT/site/"):
            payload.pop(target)
            renamed[PurePosixPath(text.replace(
                "01_FINAL_OUTPUT/site/", "01_FINAL_OUTPUT/site-source/", 1
            ))] = source
    for target, source in renamed.items():
        if target in payload:
            raise SystemExit(f"duplicate renamed destination: {target}")
        payload[target] = source

    base.add_tree(
        payload,
        "reports/overnight/v15_2",
        "04_REASONING_AND_QA/overnight-v15.2",
    )
    reviews_root = ROOT / "reviews"
    if reviews_root.is_dir():
        for absolute in sorted(reviews_root.rglob("*")):
            if not absolute.is_file() or absolute.suffix.lower() not in {".md", ".json"}:
                continue
            relative = absolute.relative_to(ROOT)
            nested = absolute.relative_to(reviews_root).as_posix()
            base.add_file(
                payload,
                relative,
                f"04_REASONING_AND_QA/model-review-records/{nested}",
            )
    for name in (
        "OWNER_REVIEW_PACKET_V15_1.md",
        "PACKAGE_MAP_V15_1.md",
        "PDF_REVIEW_INDEX_V15_1.md",
    ):
        source = f"handoff/{name}"
        destination = f"04_REASONING_AND_QA/sealed-v15.1-handoff/{name}"
        base.add_file(payload, source, destination)

    if (ROOT / "experiments").is_dir():
        base.add_tree(
            payload,
            "experiments",
            "03_RESEARCH_PROGRAM_UNRUN/experiments",
        )
    if (ROOT / "source/candidates").is_dir():
        base.add_tree(
            payload,
            "source/candidates",
            "04_REASONING_AND_QA/editorial-candidates",
        )

    base.add_file(
        payload,
        "source/THOUGHT_PIECE_V15.md",
        "05_HISTORY_AND_VISUALS/prior-version-surfaces/THOUGHT_PIECE_V15_1.md",
    )
    base.add_file(
        payload,
        "source/READER_OUTCOME_AND_READING_PATH_V15_1.md",
        "05_HISTORY_AND_VISUALS/prior-version-surfaces/READER_OUTCOME_AND_READING_PATH_V15_1.md",
    )
    base.add_file(
        payload,
        "output/pdf/PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf",
        "05_HISTORY_AND_VISUALS/prior-review-pdfs/PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf",
    )
    base.add_tree(
        payload,
        "output/v15_2/history-html",
        "05_HISTORY_AND_VISUALS/prior-standalone-html",
    )

    return payload


def manifest_bytes(payload: dict[PurePosixPath, Path]) -> bytes:
    files: list[dict[str, object]] = []
    total = 0
    for target, source in sorted(payload.items(), key=lambda item: str(item[0])):
        absolute = ROOT / source
        size = absolute.stat().st_size
        total += size
        files.append({
            "archive_path": str(target),
            "source_path": source.as_posix(),
            "bytes": size,
            "sha256": base.sha256_file(absolute),
        })

    manifest = {
        "schema_version": "1.0",
        "package_id": "pattern-map-v15.2-owner-handoff",
        "release_date": "2026-08-19",
        "status": "LOCAL_OWNER_REVIEW_NO_EMPIRICAL_RESULTS_NOT_PUBLISHED",
        "source": {
            "branch": base.git_text("branch", "--show-current"),
            "commit": base.git_text("rev-parse", "HEAD"),
            "baseline_v15_1_commit": "22f232701184812489843731b6fe27592118eb29",
            "payload_matches_commit": True,
        },
        "canonical": {
            "start": "00_START_HERE/OWNER_REVIEW_PACKET_V15_2.md",
            "standalone_site": "01_FINAL_OUTPUT/standalone-site/index.html",
            "site_source": "01_FINAL_OUTPUT/site-source/",
            "manuscript": "01_FINAL_OUTPUT/canonical-manuscript/THOUGHT_PIECE_V15_2.md",
            "pdf": "01_FINAL_OUTPUT/pdf-review/PATTERN_MAP_V15_2_REVIEW_COMPANION.pdf",
            "historical_standalone_html": "05_HISTORY_AND_VISUALS/prior-standalone-html/index.html",
            "protocol": "03_RESEARCH_PROGRAM_UNRUN/research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md",
            "protocol_v1_1_status": "DRAFT_AMENDMENT_NOT_CANONICAL",
        },
        "research_boundary": {
            "empirical_results_present": False,
            "empirical_study_model_or_provider_calls": 0,
            "design_image_generation": "OCCURRED_EXACT_MODEL_NAME_NOT_EXPOSED_NOT_EMPIRICAL_EVIDENCE",
            "model_assisted_editorial_review": "OCCURRED_RECORDS_INCLUDED_NOT_EMPIRICAL_EVIDENCE",
            "external_dataset_acquisition": False,
            "participants": 0,
            "confirmatory_conditions": ["F0", "F1", "F2"],
            "primary_planned_cases": 300,
            "fixed_planned_safety_subset": 75,
            "t1_status": "OPTIONAL_DESCRIPTIVE_RIGHTS_AND_ANNOTATION_GATED_OUTSIDE_CONFIRMATORY_DENOMINATORS",
            "unfavorable_results_preserved": [
                "null",
                "rule_only",
                "invalidity_driven",
                "threshold_only_vor",
                "harmful",
                "shortcut_driven",
                "surface_or_semantic_audit_failure",
                "unstable",
                "noise_fragile",
                "nontransfer",
                "stopped_or_quarantined",
            ],
        },
        "external_actions": {
            "published": False,
            "deployed": False,
            "pushed": False,
            "pull_request_opened": False,
            "study_run": False,
            "preregistered": False,
        },
        "visual_boundary": {
            "v13_anchor_preserved": True,
            "generated_hero_used": False,
            "current_system_map_raster_used": False,
            "e2_deeper_example_only": True,
            "complete_inventory": "05_HISTORY_AND_VISUALS/image-candidates/IMAGE_USE_TABLE_V15_2.md",
        },
        "validation_boundary": {
            "static_site_and_route_tests": "PASS",
            "offline_harness_tests": "PASS",
            "pdf_page_render_review": "PASS",
            "archive_integrity": "PASS_AT_PACKAGE_CREATION",
            "manual_browser_and_assistive_technology": "EXPLICIT_OWNER_RESIDUAL",
        },
        "selection_policy": {
            "mode": "explicit_role_based_allowlist",
            "excluded": [
                "dependencies and caches",
                "site build products",
                "temporary PDF render rasters",
                "nested owner ZIPs",
                "credentials and environment files",
            ],
        },
        "payload_file_count": len(files),
        "payload_total_bytes": total,
        "files": files,
    }
    return (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode()


def main() -> None:
    payload = collect_payload()
    base.assert_payload_matches_head(payload)
    manifest = manifest_bytes(payload)
    base.atomic_write(EXTERNAL_MANIFEST, manifest)

    main_members = {
        f"{ARCHIVE_ROOT}/{target}": (ROOT / source).read_bytes()
        for target, source in payload.items()
    }
    main_members[f"{ARCHIVE_ROOT}/00_START_HERE/PACKAGE_MANIFEST.json"] = manifest
    base.write_zip(MAIN_ZIP, main_members)
    base.sidecar(MAIN_ZIP, MAIN_SIDECAR)

    pdf_members = {
        "Pattern-Map-v15.2-PDF-Review/00_READ_ME_FIRST.md": (
            ROOT / "handoff/PDF_REVIEW_INDEX_V15_2.md"
        ).read_bytes(),
        "Pattern-Map-v15.2-PDF-Review/01_THOUGHT_PIECE_V14.pdf": (
            ROOT / "exports/THOUGHT_PIECE_V14.pdf"
        ).read_bytes(),
        "Pattern-Map-v15.2-PDF-Review/02_THOUGHT_PIECE_V15.pdf": (
            ROOT / "exports/THOUGHT_PIECE_V15.pdf"
        ).read_bytes(),
        "Pattern-Map-v15.2-PDF-Review/03_PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf": (
            ROOT / "output/pdf/PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf"
        ).read_bytes(),
        "Pattern-Map-v15.2-PDF-Review/04_PATTERN_MAP_V15_2_REVIEW_COMPANION.pdf": (
            ROOT / "output/pdf/PATTERN_MAP_V15_2_REVIEW_COMPANION.pdf"
        ).read_bytes(),
    }
    base.write_zip(PDF_ZIP, pdf_members)
    base.sidecar(PDF_ZIP, PDF_SIDECAR)

    result = {
        "status": "PASS",
        "source_commit": base.git_text("rev-parse", "HEAD"),
        "manifest_sha256": base.sha256_bytes(manifest),
        "main_archive": base.verify_zip(MAIN_ZIP, main_members),
        "pdf_archive": base.verify_zip(PDF_ZIP, pdf_members),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
