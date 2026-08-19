#!/usr/bin/env python3
"""Verify that the EP v0.1 preserved-source copies match the accession."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ARCHIVE_ROOT = ROOT / "archive/transfers/v15.2-owner-handoff"
CURATED_ROOT = ROOT / "research/the-echo-problem/preserved/v15.2"
MANIFEST_PATH = ARCHIVE_ROOT / "PATTERN_MAP_V15_2_OWNER_HANDOFF-manifest.json"

TREE_MAPPINGS = (
    (
        "01_FINAL_OUTPUT/site-source/",
        "site-source/",
    ),
    (
        "01_FINAL_OUTPUT/standalone-site/",
        "site-standalone/",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/offline-implementation/origin_accounting/",
        "harness/origin_accounting/",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/origin_accounting/fixtures/",
        "fixtures/",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/origin_accounting/config/",
        "fixtures/config/",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/origin_accounting/schema/",
        "fixtures/schema/",
    ),
)

FILE_MAPPINGS = (
    (
        "01_FINAL_OUTPUT/canonical-manuscript/THOUGHT_PIECE_V15_2.md",
        "manuscript/THOUGHT_PIECE_V15_2.md",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md",
        "protocol/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V0.md",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md",
        "protocol/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md",
        "protocol/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/tests/test_origin_accounting.py",
        "harness/tests/test_origin_accounting.py",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/CLAIMS_AND_EVIDENCE_REGISTER.csv",
        "prior-art/CLAIMS_AND_EVIDENCE_REGISTER.csv",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/CLAIMS_AND_EVIDENCE_REGISTER.md",
        "prior-art/CLAIMS_AND_EVIDENCE_REGISTER.md",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/OVERCLAIM_AND_COUNTERARGUMENT_REGISTER.md",
        "prior-art/OVERCLAIM_AND_COUNTERARGUMENT_REGISTER.md",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md",
        "prior-art/PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/PRIOR_ART_DELTA_V1.md",
        "prior-art/PRIOR_ART_DELTA_V1.md",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/REFERENCES.md",
        "prior-art/REFERENCES.md",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/RESEARCH_PAPER_READINESS_PATH.md",
        "prior-art/RESEARCH_PAPER_READINESS_PATH.md",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/V15_CLAIM_SOURCE_ARTIFACT_MATRIX.md",
        "prior-art/V15_CLAIM_SOURCE_ARTIFACT_MATRIX.md",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/references.bib",
        "prior-art/references.bib",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/overnight/01_THEORY_AND_PRIOR_ART_LUNA_MAX.md",
        "prior-art/overnight/01_THEORY_AND_PRIOR_ART_LUNA_MAX.md",
    ),
    (
        "03_RESEARCH_PROGRAM_UNRUN/research/overnight/rounds/07_LOOP2_CURRENT_LITERATURE_EXPANSION.md",
        "prior-art/overnight/07_LOOP2_CURRENT_LITERATURE_EXPANSION.md",
    ),
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_mapping(manifest: dict) -> dict[str, str]:
    mapping: dict[str, str] = {}
    entries = {entry["archive_path"]: entry for entry in manifest["files"]}
    for source, target in FILE_MAPPINGS:
        if source not in entries:
            raise ValueError(f"mapping source is absent from accession manifest: {source}")
        if target in mapping:
            raise ValueError(f"duplicate curated target: {target}")
        mapping[target] = source
    for source_prefix, target_prefix in TREE_MAPPINGS:
        matched = [source for source in entries if source.startswith(source_prefix)]
        if not matched:
            raise ValueError(f"mapping prefix has no manifest files: {source_prefix}")
        for source in matched:
            target = target_prefix + source[len(source_prefix) :]
            if target in mapping:
                raise ValueError(f"duplicate curated target: {target}")
            mapping[target] = source
    return mapping


def observed_curated_files() -> list[str]:
    if not CURATED_ROOT.is_dir():
        raise ValueError(f"missing curated root: {CURATED_ROOT}")
    files: list[str] = []
    for candidate in CURATED_ROOT.rglob("*"):
        if candidate.is_symlink():
            raise ValueError(f"symlink in curated source tree: {candidate}")
        if candidate.is_file():
            files.append(candidate.relative_to(CURATED_ROOT).as_posix())
    return sorted(files)


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    mapping = build_mapping(manifest)
    expected_targets = sorted(mapping)
    observed_targets = observed_curated_files()
    if observed_targets != expected_targets:
        missing = sorted(set(expected_targets) - set(observed_targets))
        extra = sorted(set(observed_targets) - set(expected_targets))
        raise ValueError(f"curated path mismatch; missing={missing}, extra={extra}")

    total_bytes = 0
    for target, source in mapping.items():
        source_path = ARCHIVE_ROOT / source
        target_path = CURATED_ROOT / target
        if source_path.is_symlink() or target_path.is_symlink():
            raise ValueError(f"symlink in mapped source: {source}")
        source_bytes = source_path.read_bytes()
        target_bytes = target_path.read_bytes()
        if source_bytes != target_bytes:
            raise ValueError(f"byte mismatch: {target}")
        entry = next(item for item in manifest["files"] if item["archive_path"] == source)
        if len(target_bytes) != entry["bytes"]:
            raise ValueError(f"byte count mismatch: {target}")
        if sha256_file(target_path) != entry["sha256"]:
            raise ValueError(f"SHA-256 mismatch: {target}")
        total_bytes += len(target_bytes)

    result = {
        "status": "PASS",
        "curated_files": len(mapping),
        "curated_bytes": total_bytes,
        "source_commit": manifest["source"]["commit"],
        "mapped_roles": ["manuscript", "site", "protocol", "harness", "fixtures", "prior_art"],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
