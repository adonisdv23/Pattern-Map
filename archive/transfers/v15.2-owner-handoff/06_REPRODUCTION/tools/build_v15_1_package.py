#!/usr/bin/env python3
"""Build and verify the structured Pattern Map v15.1 owner-review archives.

The main ZIP is organized by reader role instead of mirroring the worktree.
Every member is allowlisted, hashed in an embedded manifest, and written with a
fixed timestamp. Dependencies, build products, caches, credentials, QA rasters,
and nested transfer ZIPs are intentionally excluded.
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
OUTPUT = ROOT / "output"
MAIN_ZIP = OUTPUT / "PATTERN_MAP_V15_1_OWNER_REVIEW.zip"
MAIN_SIDECAR = OUTPUT / "PATTERN_MAP_V15_1_OWNER_REVIEW.zip.sha256"
EXTERNAL_MANIFEST = OUTPUT / "PATTERN_MAP_V15_1_OWNER_REVIEW-manifest.json"
PDF_ZIP = OUTPUT / "PATTERN_MAP_V15_1_PDF_REVIEW.zip"
PDF_SIDECAR = OUTPUT / "PATTERN_MAP_V15_1_PDF_REVIEW.zip.sha256"
ARCHIVE_ROOT = "Pattern-Map-v15.1"
ZIP_TIMESTAMP = (2026, 8, 19, 12, 0, 0)

FORBIDDEN_PARTS = {
    ".git",
    ".next",
    ".vinext",
    ".wrangler",
    "__pycache__",
    "dist",
    "node_modules",
    "tmp",
}
FORBIDDEN_SUFFIXES = {".env", ".key", ".p12", ".pem", ".pfx", ".pyc"}


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


def safe_source(relative: Path) -> bool:
    if relative.is_absolute() or ".." in relative.parts:
        return False
    if any(part in FORBIDDEN_PARTS for part in relative.parts):
        return False
    if relative.name == ".DS_Store" or relative.name.startswith(".env"):
        return False
    if relative.suffix.lower() in FORBIDDEN_SUFFIXES:
        return False
    return True


def add_file(
    payload: dict[PurePosixPath, Path], source: str | Path, destination: str
) -> None:
    relative = Path(source)
    absolute = ROOT / relative
    target = PurePosixPath(destination)
    if not safe_source(relative):
        raise SystemExit(f"unsafe source path: {relative}")
    if absolute.is_symlink() or not absolute.is_file():
        raise SystemExit(f"missing or non-regular source: {relative}")
    if target.is_absolute() or ".." in target.parts:
        raise SystemExit(f"unsafe archive destination: {target}")
    if target in payload:
        raise SystemExit(f"duplicate archive destination: {target}")
    payload[target] = relative


def add_tree(
    payload: dict[PurePosixPath, Path], source_root: str, destination_root: str
) -> None:
    base = ROOT / source_root
    if not base.is_dir():
        raise SystemExit(f"missing source tree: {source_root}")
    for absolute in sorted(base.rglob("*")):
        if not absolute.is_file():
            continue
        relative = absolute.relative_to(ROOT)
        if not safe_source(relative):
            continue
        nested = absolute.relative_to(base).as_posix()
        add_file(payload, relative, f"{destination_root}/{nested}")


def collect_payload() -> dict[PurePosixPath, Path]:
    payload: dict[PurePosixPath, Path] = {}

    # 00 — orientation.
    add_file(payload, "README.md", "00_START_HERE/README.md")
    add_file(
        payload,
        "handoff/OWNER_REVIEW_PACKET_V15_1.md",
        "00_START_HERE/OWNER_REVIEW_PACKET_V15_1.md",
    )
    add_file(
        payload,
        "handoff/PACKAGE_MAP_V15_1.md",
        "00_START_HERE/PACKAGE_MAP_V15_1.md",
    )
    add_file(
        payload,
        "SOURCE_VERSIONS_USED.json",
        "00_START_HERE/SOURCE_VERSIONS_USED.json",
    )

    # 01 — final output.
    site_root_files = [
        "site/.gitignore",
        "site/.openai/hosting.json",
        "site/README.md",
        "site/drizzle.config.ts",
        "site/eslint.config.mjs",
        "site/next-env.d.ts",
        "site/next.config.ts",
        "site/package-lock.json",
        "site/package.json",
        "site/postcss.config.mjs",
        "site/tsconfig.json",
        "site/vite.config.ts",
    ]
    for source in site_root_files:
        site_relative = Path(source).relative_to("site").as_posix()
        add_file(payload, source, f"01_FINAL_OUTPUT/site/{site_relative}")
    for tree in ("app", "db", "drizzle", "public", "tests", "worker"):
        add_tree(payload, f"site/{tree}", f"01_FINAL_OUTPUT/site/{tree}")
    add_file(
        payload,
        "source/THOUGHT_PIECE_V15.md",
        "01_FINAL_OUTPUT/canonical-manuscript/THOUGHT_PIECE_V15.md",
    )
    add_file(
        payload,
        "output/pdf/PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf",
        "01_FINAL_OUTPUT/visual-review/PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf",
    )

    # 02 — current framework and bounded cases.
    for name in (
        "FRAMEWORK_COMPONENT_MAP.json",
        "FRAMEWORK_COMPONENT_MAP.md",
        "GLOSSARY.md",
        "READER_OUTCOME_AND_READING_PATH_V15_1.md",
        "THESIS_AND_TERMINOLOGY_CONTRACT.md",
    ):
        add_file(payload, f"source/{name}", f"02_CANONICAL_FRAMEWORK/source/{name}")
    add_tree(payload, "case-studies", "02_CANONICAL_FRAMEWORK/case-studies")

    # 03 — unrun empirical program and offline machinery.
    add_tree(payload, "research", "03_RESEARCH_PROGRAM_UNRUN/research")
    add_tree(
        payload,
        "tools/origin_accounting",
        "03_RESEARCH_PROGRAM_UNRUN/offline-implementation/origin_accounting",
    )
    add_tree(payload, "tests", "03_RESEARCH_PROGRAM_UNRUN/tests")

    # 04 — reasoning, red teams, and validation. QA rasters are deliberately
    # omitted; their final dispositions are in Markdown and the current PDF was
    # independently inspected.
    reports_root = ROOT / "reports"
    for absolute in sorted(reports_root.glob("*")):
        if absolute.is_file() and absolute.suffix.lower() in {".md", ".json"}:
            add_file(
                payload,
                absolute.relative_to(ROOT),
                f"04_REASONING_AND_QA/current-and-sealed/{absolute.name}",
            )
    for name in (
        "OWNER_REVIEW_PACKET_V15.md",
        "COMPLETE_TRANSFER_GUIDE_V15.md",
        "V15_PACKAGE_MANIFEST.json",
        "V15_SHA256SUMS.txt",
        "PDF_REVIEW_INDEX_V15_1.md",
    ):
        add_file(payload, f"handoff/{name}", f"04_REASONING_AND_QA/handoff-records/{name}")

    # 05 — history and all image candidates, with selection/provenance ledger.
    add_tree(payload, "archive/v13", "05_HISTORY_AND_VISUALS/v13-anchor")
    add_tree(payload, "assets/imagegen", "05_HISTORY_AND_VISUALS/image-candidates")
    add_file(
        payload,
        "source/THOUGHT_PIECE_V14.md",
        "05_HISTORY_AND_VISUALS/prior-version-surfaces/THOUGHT_PIECE_V14.md",
    )
    add_file(
        payload,
        "exports/THOUGHT_PIECE_V14.pdf",
        "05_HISTORY_AND_VISUALS/prior-version-surfaces/THOUGHT_PIECE_V14.pdf",
    )
    add_file(
        payload,
        "exports/THOUGHT_PIECE_V15.pdf",
        "05_HISTORY_AND_VISUALS/prior-version-surfaces/THOUGHT_PIECE_V15.pdf",
    )

    # 06 — reproduction utilities, excluding the origin-accounting module that
    # already lives with the unrun research program.
    for absolute in sorted((ROOT / "tools").glob("*")):
        if absolute.is_file() and safe_source(absolute.relative_to(ROOT)):
            add_file(
                payload,
                absolute.relative_to(ROOT),
                f"06_REPRODUCTION/tools/{absolute.name}",
            )

    return payload


def assert_payload_matches_head(payload: dict[PurePosixPath, Path]) -> None:
    failures: list[str] = []
    for source in sorted(set(payload.values()), key=lambda item: item.as_posix()):
        text = source.as_posix()
        tracked = subprocess.run(
            ["git", "ls-files", "--error-unmatch", "--", text],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if tracked.returncode:
            failures.append(f"untracked payload: {text}")
            continue
        clean = subprocess.run(
            ["git", "diff", "--quiet", "HEAD", "--", text],
            cwd=ROOT,
            check=False,
        )
        if clean.returncode:
            failures.append(f"payload differs from HEAD: {text}")
    if failures:
        raise SystemExit(
            "package payload must be committed and match HEAD:\n"
            + "\n".join(f"- {failure}" for failure in failures)
        )


def manifest_bytes(payload: dict[PurePosixPath, Path]) -> bytes:
    files = []
    total = 0
    for target, source in sorted(payload.items(), key=lambda item: str(item[0])):
        absolute = ROOT / source
        size = absolute.stat().st_size
        total += size
        files.append(
            {
                "archive_path": str(target),
                "source_path": source.as_posix(),
                "bytes": size,
                "sha256": sha256_file(absolute),
            }
        )
    manifest = {
        "schema_version": "1.0",
        "package_id": "pattern-map-v15.1-owner-review",
        "release_date": "2026-08-19",
        "status": "LOCAL_OWNER_REVIEW_NO_EMPIRICAL_RESULTS_NOT_PUBLISHED",
        "source": {
            "branch": git_text("branch", "--show-current"),
            "commit": git_text("rev-parse", "HEAD"),
            "payload_matches_commit": True,
        },
        "canonical": {
            "start": "00_START_HERE/OWNER_REVIEW_PACKET_V15_1.md",
            "site": "01_FINAL_OUTPUT/site/",
            "manuscript": "01_FINAL_OUTPUT/canonical-manuscript/THOUGHT_PIECE_V15.md",
            "pdf": "01_FINAL_OUTPUT/visual-review/PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf",
        },
        "research_boundary": {
            "empirical_results_present": False,
            "model_or_provider_calls": 0,
            "external_dataset_acquisition": False,
            "confirmatory_conditions": ["F0", "F1", "F2"],
            "t1_status": "OPTIONAL_DESCRIPTIVE_OUTSIDE_CONFIRMATORY_DENOMINATORS",
        },
        "external_actions": {
            "published": False,
            "deployed": False,
            "pushed": False,
            "pull_request_opened": False,
            "study_run": False,
        },
        "selection_policy": {
            "mode": "explicit_role_based_allowlist",
            "excluded": [
                "dependencies and caches",
                "site build products",
                "raw QA rasters",
                "nested owner ZIPs",
                "credentials and environment files",
            ],
        },
        "payload_file_count": len(files),
        "payload_total_bytes": total,
        "files": files,
    }
    return (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode()


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = (0o100644 & 0xFFFF) << 16
    return info


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        Path(temporary_name).replace(path)
    except BaseException:
        Path(temporary_name).unlink(missing_ok=True)
        raise


def write_zip(path: Path, members: dict[str, bytes]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.unlink(missing_ok=True)
    try:
        with zipfile.ZipFile(
            temporary,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
            strict_timestamps=True,
        ) as archive:
            for name in sorted(members):
                archive.writestr(zip_info(name), members[name])
        temporary.replace(path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def verify_zip(path: Path, expected: dict[str, bytes]) -> dict[str, object]:
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if names != sorted(expected):
            raise SystemExit(f"unexpected members or ordering in {path.name}")
        if len(names) != len(set(names)):
            raise SystemExit(f"duplicate members in {path.name}")
        for info in infos:
            pure = PurePosixPath(info.filename)
            if pure.is_absolute() or ".." in pure.parts:
                raise SystemExit(f"unsafe ZIP member: {info.filename}")
            if info.date_time != ZIP_TIMESTAMP:
                raise SystemExit(f"non-deterministic timestamp: {info.filename}")
            if archive.read(info) != expected[info.filename]:
                raise SystemExit(f"content mismatch: {info.filename}")
        bad = archive.testzip()
        if bad is not None:
            raise SystemExit(f"CRC failure: {bad}")
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
        "members": len(expected),
    }


def sidecar(path: Path, destination: Path) -> None:
    line = f"{sha256_file(path)}  {path.relative_to(ROOT).as_posix()}\n".encode()
    atomic_write(destination, line)


def main() -> None:
    payload = collect_payload()
    assert_payload_matches_head(payload)
    manifest = manifest_bytes(payload)
    atomic_write(EXTERNAL_MANIFEST, manifest)

    main_members = {
        f"{ARCHIVE_ROOT}/{target}": (ROOT / source).read_bytes()
        for target, source in payload.items()
    }
    main_members[f"{ARCHIVE_ROOT}/00_START_HERE/PACKAGE_MANIFEST.json"] = manifest
    write_zip(MAIN_ZIP, main_members)
    sidecar(MAIN_ZIP, MAIN_SIDECAR)

    pdf_members = {
        "Pattern-Map-v15.1-PDF-Review/00_READ_ME_FIRST.md": (
            ROOT / "handoff/PDF_REVIEW_INDEX_V15_1.md"
        ).read_bytes(),
        "Pattern-Map-v15.1-PDF-Review/01_THOUGHT_PIECE_V14.pdf": (
            ROOT / "exports/THOUGHT_PIECE_V14.pdf"
        ).read_bytes(),
        "Pattern-Map-v15.1-PDF-Review/02_THOUGHT_PIECE_V15.pdf": (
            ROOT / "exports/THOUGHT_PIECE_V15.pdf"
        ).read_bytes(),
        "Pattern-Map-v15.1-PDF-Review/03_PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf": (
            ROOT / "output/pdf/PATTERN_MAP_V15_1_REVIEW_COMPANION.pdf"
        ).read_bytes(),
    }
    write_zip(PDF_ZIP, pdf_members)
    sidecar(PDF_ZIP, PDF_SIDECAR)

    result = {
        "status": "PASS",
        "source_commit": git_text("rev-parse", "HEAD"),
        "manifest_sha256": sha256_bytes(manifest),
        "main_archive": verify_zip(MAIN_ZIP, main_members),
        "pdf_archive": verify_zip(PDF_ZIP, pdf_members),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
