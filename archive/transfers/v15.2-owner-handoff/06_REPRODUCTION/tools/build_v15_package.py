#!/usr/bin/env python3
"""Build the deterministic, compact Discrimination Layer v15 owner package.

The package is an allowlisted release artifact. It intentionally excludes
dependencies, build outputs, caches, intermediate QA rasters, old final
surfaces, and unrelated review bundles. Run only after committing the payload
state that should be identified in the package manifest.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
import zipfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ID = "discrimination-layer-v15-owner-review"
ARCHIVE_ROOT = "Discrimination-Layer-v15"
RELEASE_DATE = "2026-08-18"
ZIP_TIMESTAMP = (2026, 8, 18, 12, 0, 0)

MANIFEST_PATH = Path("handoff/V15_PACKAGE_MANIFEST.json")
CHECKSUM_PATH = Path("handoff/V15_SHA256SUMS.txt")
ZIP_PATH = Path("exports/DISCRIMINATION_LAYER_V15_OWNER_PACKAGE.zip")
ZIP_SIDECAR_PATH = Path(
    "exports/DISCRIMINATION_LAYER_V15_OWNER_PACKAGE.zip.sha256"
)

EXACT_PAYLOAD_FILES = (
    Path("README.md"),
    Path("SOURCE_VERSIONS_USED.json"),
    Path("assets/imagegen/IMAGE_SELECTION_LEDGER.md"),
    Path("assets/imagegen/candidates/E2-echo-sheets-watermark.png"),
    Path("assets/imagegen/candidates/H1-evidence-aperture.png"),
    Path("exports/THOUGHT_PIECE_V15.pdf"),
    Path("handoff/OWNER_REVIEW_PACKET_V15.md"),
    Path("handoff/COMPLETE_TRANSFER_GUIDE_V15.md"),
    Path("research/CLAIMS_AND_EVIDENCE_REGISTER.csv"),
    Path("research/CLAIMS_AND_EVIDENCE_REGISTER.md"),
    Path("research/F0_F1_F2_IMPLEMENTATION_READINESS_V1.md"),
    Path("research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md"),
    Path("research/OVERCLAIM_AND_COUNTERARGUMENT_REGISTER.md"),
    Path("research/PAPER_PROSPECTUS_V1.md"),
    Path("research/PRIOR_ART_AND_ADJACENT_FIELDS_MAP.md"),
    Path("research/PRIOR_ART_DELTA_V1.md"),
    Path("research/REAL_SYNDICATION_TRANSFER_FEASIBILITY_V1.md"),
    Path("research/REFERENCES.md"),
    Path("research/V15_CLAIM_SOURCE_ARTIFACT_MATRIX.md"),
    Path("research/references.bib"),
    Path("source/THOUGHT_PIECE_V15.md"),
    Path("source/FRAMEWORK_COMPONENT_MAP.json"),
    Path("source/FRAMEWORK_COMPONENT_MAP.md"),
    Path("source/GLOSSARY.md"),
    Path("source/THESIS_AND_TERMINOLOGY_CONTRACT.md"),
    Path("tools/render_v15_reader_pdf.py"),
    Path("tools/build_v15_package.py"),
    Path("tools/verify_v15_package.py"),
    Path("tests/test_origin_accounting.py"),
)

TREE_PAYLOAD_ROOTS = (
    Path("archive/v13"),
    Path("case-studies"),
    Path("research/origin_accounting"),
    Path("site/app"),
    Path("site/db"),
    Path("site/drizzle"),
    Path("site/public"),
    Path("site/tests"),
    Path("site/worker"),
    Path("tools/origin_accounting"),
)

SITE_ROOT_FILES = (
    Path("site/.gitignore"),
    Path("site/.openai/hosting.json"),
    Path("site/README.md"),
    Path("site/drizzle.config.ts"),
    Path("site/eslint.config.mjs"),
    Path("site/next-env.d.ts"),
    Path("site/next.config.ts"),
    Path("site/package-lock.json"),
    Path("site/package.json"),
    Path("site/postcss.config.mjs"),
    Path("site/tsconfig.json"),
    Path("site/vite.config.ts"),
)

REPORT_EXACT_FILES = (
    Path("reports/V13_RECOVERY_AND_INTENT_MEMO.md"),
)

FORBIDDEN_PARTS = {
    "node_modules",
    "dist",
    ".next",
    ".wrangler",
    "__pycache__",
    ".venv",
    ".git",
}
FORBIDDEN_SUFFIXES = {".pyc", ".pem", ".key", ".p12", ".pfx"}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_text(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, text=True, stderr=subprocess.PIPE
    ).strip()


def is_safe_payload_path(relative: Path) -> bool:
    if relative.is_absolute() or ".." in relative.parts:
        return False
    if any(part in FORBIDDEN_PARTS for part in relative.parts):
        return False
    if relative.suffix.lower() in FORBIDDEN_SUFFIXES:
        return False
    if relative.name.startswith(".env") or relative.name == ".DS_Store":
        return False
    return True


def collect_payload() -> list[Path]:
    selected: set[Path] = set(EXACT_PAYLOAD_FILES)
    selected.update(SITE_ROOT_FILES)
    selected.update(REPORT_EXACT_FILES)
    selected.update(
        path.relative_to(ROOT)
        for path in (ROOT / "reports").glob("V15_*.md")
        if path.is_file()
    )

    for relative_root in TREE_PAYLOAD_ROOTS:
        absolute_root = ROOT / relative_root
        if not absolute_root.is_dir():
            raise SystemExit(f"missing payload tree: {relative_root.as_posix()}")
        for path in absolute_root.rglob("*"):
            if path.is_file():
                relative = path.relative_to(ROOT)
                if is_safe_payload_path(relative):
                    selected.add(relative)

    paths = sorted(selected, key=lambda item: item.as_posix())
    if not paths:
        raise SystemExit("payload selection is empty")

    for relative in paths:
        absolute = ROOT / relative
        if not is_safe_payload_path(relative):
            raise SystemExit(f"unsafe or excluded payload path: {relative.as_posix()}")
        if absolute.is_symlink():
            raise SystemExit(f"symlinks are not allowed in the package: {relative}")
        if not absolute.is_file():
            raise SystemExit(f"missing payload file: {relative.as_posix()}")

    return paths


def assert_payload_matches_head(paths: list[Path]) -> None:
    failures: list[str] = []
    for relative in paths:
        rel_text = relative.as_posix()
        tracked = subprocess.run(
            ["git", "ls-files", "--error-unmatch", "--", rel_text],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if tracked.returncode:
            failures.append(f"untracked payload: {rel_text}")
            continue
        clean = subprocess.run(
            ["git", "diff", "--quiet", "HEAD", "--", rel_text],
            cwd=ROOT,
            check=False,
        )
        if clean.returncode:
            failures.append(f"payload differs from HEAD: {rel_text}")
    if failures:
        details = "\n".join(f"- {failure}" for failure in failures)
        raise SystemExit(
            "package payload must be committed and match HEAD before sealing:\n"
            + details
        )


def category_for(relative: Path) -> str:
    path = relative.as_posix()
    if path.startswith("handoff/"):
        return "owner_handoff"
    if path.startswith("source/"):
        return "canonical_concept"
    if path.startswith("site/"):
        return "interactive_reader_source"
    if path.startswith("research/origin_accounting/"):
        return "offline_research_schema"
    if path.startswith("research/overnight/"):
        return "advisory_research_audit"
    if path.startswith("research/"):
        return "research_program"
    if path.startswith("reports/"):
        return "decision_qa_receipt"
    if path.startswith("tools/origin_accounting/"):
        return "offline_research_implementation"
    if path.startswith("tools/") or path.startswith("tests/"):
        return "reproduction_and_validation"
    if path.startswith("archive/v13/"):
        return "historical_v13"
    if path.startswith("assets/imagegen/"):
        return "visual_selection_record"
    if path.startswith("case-studies/"):
        return "bounded_case_study"
    if path.startswith("exports/"):
        return "visual_print_companion"
    return "release_orientation"


def role_for(relative: Path) -> str:
    path = relative.as_posix()
    special = {
        "README.md": "canonical_repository_orientation",
        "SOURCE_VERSIONS_USED.json": "source_registry_and_supersession_record",
        "source/THOUGHT_PIECE_V15.md": "canonical_manuscript",
        "source/FRAMEWORK_COMPONENT_MAP.json": "canonical_machine_readable_map",
        "site/app/page.tsx": "canonical_reader_composition",
        "research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md": "frozen_unrun_protocol",
        "research/PRIOR_ART_DELTA_V1.md": "verified_prior_art_delta",
        "reports/V15_DECISION_LEDGER.md": "canonical_disposition_record",
        "reports/V15_VISUAL_AND_ACCESSIBILITY_QA.md": "release_surface_qa",
        "handoff/OWNER_REVIEW_PACKET_V15.md": "compact_owner_decision_path",
        "handoff/COMPLETE_TRANSFER_GUIDE_V15.md": "complete_transfer_record",
        "exports/THOUGHT_PIECE_V15.pdf": "untagged_visual_print_companion",
    }
    return special.get(path, f"supporting_{category_for(relative)}")


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", dir=path.parent
    )
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary_name).replace(path)
    except BaseException:
        Path(temporary_name).unlink(missing_ok=True)
        raise


def manifest_bytes(paths: list[Path], branch: str, commit: str) -> bytes:
    entries = []
    total_bytes = 0
    for relative in paths:
        absolute = ROOT / relative
        size = absolute.stat().st_size
        total_bytes += size
        entries.append(
            {
                "path": relative.as_posix(),
                "category": category_for(relative),
                "role": role_for(relative),
                "bytes": size,
                "sha256": sha256_file(absolute),
            }
        )

    manifest = {
        "schema_version": "1.0",
        "package_id": PACKAGE_ID,
        "release_date": RELEASE_DATE,
        "status": "LOCAL_OWNER_REVIEW_NO_EMPIRICAL_RESULTS_NOT_PUBLISHED",
        "source": {
            "branch": branch,
            "commit": commit,
            "payload_matches_commit": True,
            "historical_v14_artifact_commit": (
                "261c516710f67998224a16c056bba0aefd5c26f4"
            ),
        },
        "archive": {
            "path": ZIP_PATH.as_posix(),
            "top_level_directory": ARCHIVE_ROOT,
            "deterministic_timestamp": "2026-08-18T12:00:00",
            "container_checksum": ZIP_SIDECAR_PATH.as_posix(),
            "container_checksum_location": "outside_archive_to_avoid_recursion",
        },
        "canonical_surfaces": {
            "owner_packet": "handoff/OWNER_REVIEW_PACKET_V15.md",
            "manuscript": "source/THOUGHT_PIECE_V15.md",
            "interactive_reader": "site/",
            "framework_map": "source/FRAMEWORK_COMPONENT_MAP.json",
            "protocol": "research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md",
            "decision_ledger": "reports/V15_DECISION_LEDGER.md",
            "pdf": "exports/THOUGHT_PIECE_V15.pdf",
            "accessible_surface": "semantic_HTML_and_Markdown",
        },
        "research_boundary": {
            "empirical_results_present": False,
            "model_or_provider_calls": 0,
            "external_dataset_acquisition": False,
            "t1_status": "DESCRIPTIVE_RIGHTS_GATED_OUTSIDE_CONFIRMATORY_DENOMINATORS",
            "confirmatory_conditions": ["F0", "F1", "F2"],
            "f3_exists": False,
        },
        "external_action_boundary": {
            "published": False,
            "deployed": False,
            "pushed": False,
            "pull_request_opened": False,
            "preregistered": False,
            "participants_contacted": False,
        },
        "selection_policy": {
            "mode": "explicit_canonical_allowlist",
            "excluded": [
                "dependencies and caches",
                "site build products",
                "intermediate QA rasters",
                "superseded v14 final surfaces",
                "unrelated external-review bundles",
                "credentials and environment files",
            ],
            "control_files_inside_archive": [
                MANIFEST_PATH.as_posix(),
                CHECKSUM_PATH.as_posix(),
            ],
        },
        "payload_file_count": len(entries),
        "payload_total_bytes": total_bytes,
        "files": entries,
    }
    return (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode(
        "utf-8"
    )


def checksum_bytes(paths: list[Path], manifest_data: bytes) -> bytes:
    lines = [
        f"{sha256_file(ROOT / relative)}  {relative.as_posix()}" for relative in paths
    ]
    lines.append(f"{sha256_bytes(manifest_data)}  {MANIFEST_PATH.as_posix()}")
    return ("\n".join(lines) + "\n").encode("utf-8")


def zip_info(member: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(member, date_time=ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = (0o100644 & 0xFFFF) << 16
    return info


def build_zip(paths: list[Path], manifest_data: bytes, checksum_data: bytes) -> None:
    ZIP_PATH_ABSOLUTE = ROOT / ZIP_PATH
    ZIP_PATH_ABSOLUTE.parent.mkdir(parents=True, exist_ok=True)
    temporary = ZIP_PATH_ABSOLUTE.with_suffix(".zip.tmp")
    temporary.unlink(missing_ok=True)

    members: dict[str, bytes] = {
        f"{ARCHIVE_ROOT}/{relative.as_posix()}": (ROOT / relative).read_bytes()
        for relative in paths
    }
    members[f"{ARCHIVE_ROOT}/{MANIFEST_PATH.as_posix()}"] = manifest_data
    members[f"{ARCHIVE_ROOT}/{CHECKSUM_PATH.as_posix()}"] = checksum_data

    try:
        with zipfile.ZipFile(
            temporary,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
            strict_timestamps=True,
        ) as archive:
            for member in sorted(members):
                archive.writestr(zip_info(member), members[member])
        temporary.replace(ZIP_PATH_ABSOLUTE)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def main() -> None:
    if not (ROOT / ".git").exists():
        # Git worktrees use a .git file rather than a directory.
        if not (ROOT / ".git").is_file():
            raise SystemExit(f"not a Git worktree: {ROOT}")

    paths = collect_payload()
    assert_payload_matches_head(paths)
    branch = git_text("branch", "--show-current")
    commit = git_text("rev-parse", "HEAD")

    manifest_data = manifest_bytes(paths, branch, commit)
    checksum_data = checksum_bytes(paths, manifest_data)

    atomic_write(ROOT / MANIFEST_PATH, manifest_data)
    atomic_write(ROOT / CHECKSUM_PATH, checksum_data)
    build_zip(paths, manifest_data, checksum_data)

    zip_hash = sha256_file(ROOT / ZIP_PATH)
    sidecar = f"{zip_hash}  {ZIP_PATH.as_posix()}\n".encode("utf-8")
    atomic_write(ROOT / ZIP_SIDECAR_PATH, sidecar)

    print(
        json.dumps(
            {
                "status": "PASS",
                "package_id": PACKAGE_ID,
                "source_commit": commit,
                "payload_files": len(paths),
                "manifest_sha256": sha256_bytes(manifest_data),
                "zip": ZIP_PATH.as_posix(),
                "zip_bytes": (ROOT / ZIP_PATH).stat().st_size,
                "zip_sha256": zip_hash,
                "zip_sidecar": ZIP_SIDECAR_PATH.as_posix(),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
