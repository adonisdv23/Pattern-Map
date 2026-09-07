#!/usr/bin/env python3
"""Verify the extracted v15.2 accession and, when supplied, its source ZIP."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path, PurePosixPath


ARCHIVE_ROOT = Path(__file__).resolve().parent
MANIFEST_NAME = "PATTERN_MAP_V15_2_OWNER_HANDOFF-manifest.json"
SIDECAR_NAME = "PATTERN_MAP_V15_2_OWNER_HANDOFF.zip.sha256"
ZIP_MEMBER_ROOT = "Pattern-Map-v15.2"
PAYLOAD_DIRECTORIES = (
    "00_START_HERE",
    "01_FINAL_OUTPUT",
    "02_CANONICAL_FRAMEWORK",
    "03_RESEARCH_PROGRAM_UNRUN",
    "04_REASONING_AND_QA",
    "05_HISTORY_AND_VISUALS",
    "06_REPRODUCTION",
)
EXPECTED_ZIP_BYTES = 41_436_496
EXPECTED_ZIP_SHA256 = (
    "f8b71db0bda7f7564e5d3cec1f697bee38b3fcb17b56f47c79bf653f39b549b5"
)
EXPECTED_MANIFEST_BYTES = 69_680
EXPECTED_MANIFEST_SHA256 = (
    "05aedafc2f5cb3f589cfdc69d1eff5c854c3bef97071324f9845d63a7a1028eb"
)
EXPECTED_PAYLOAD_FILES = 239
EXPECTED_PAYLOAD_BYTES = 48_717_432
EXPECTED_ZIP_SIDECAR_PATH = "output/PATTERN_MAP_V15_2_OWNER_HANDOFF.zip"
HASH_LINE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message: str) -> None:
    raise ValueError(message)


def safe_relative_path(value: str) -> Path:
    pure = PurePosixPath(value)
    if pure.is_absolute() or not pure.parts or ".." in pure.parts:
        fail(f"unsafe manifest path: {value}")
    return Path(*pure.parts)


def load_manifest(root: Path) -> tuple[dict, list[dict], bytes]:
    manifest_path = root / MANIFEST_NAME
    if manifest_path.is_symlink() or not manifest_path.is_file():
        fail(f"missing manifest: {manifest_path}")
    manifest_bytes = manifest_path.read_bytes()
    if len(manifest_bytes) != EXPECTED_MANIFEST_BYTES:
        fail(f"manifest byte count mismatch: {len(manifest_bytes)}")
    if sha256_bytes(manifest_bytes) != EXPECTED_MANIFEST_SHA256:
        fail("manifest SHA-256 mismatch")
    try:
        manifest = json.loads(manifest_bytes)
    except json.JSONDecodeError as error:
        fail(f"manifest is not valid JSON: {error}")

    if manifest.get("schema_version") != "1.0":
        fail("unexpected manifest schema_version")
    if manifest.get("package_id") != "pattern-map-v15.2-owner-handoff":
        fail("unexpected manifest package_id")
    if manifest.get("status") != "LOCAL_OWNER_REVIEW_NO_EMPIRICAL_RESULTS_NOT_PUBLISHED":
        fail("unexpected manifest status")

    entries = manifest.get("files")
    if not isinstance(entries, list) or len(entries) != EXPECTED_PAYLOAD_FILES:
        fail("manifest payload file count mismatch")
    paths: list[str] = []
    for entry in entries:
        if not isinstance(entry, dict):
            fail("manifest entry is not an object")
        path_text = entry.get("archive_path")
        if not isinstance(path_text, str):
            fail("manifest entry has no archive_path")
        relative = safe_relative_path(path_text)
        if relative.parts[0] not in PAYLOAD_DIRECTORIES:
            fail(f"manifest path is outside the payload directories: {path_text}")
        if not isinstance(entry.get("bytes"), int):
            fail(f"manifest entry has no integer byte count: {path_text}")
        digest = entry.get("sha256")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            fail(f"manifest entry has no valid SHA-256: {path_text}")
        paths.append(path_text)
    if paths != sorted(paths):
        fail("manifest entries are not sorted by archive_path")
    if len(paths) != len(set(paths)):
        fail("manifest contains duplicate archive_path values")
    if manifest.get("payload_file_count") != len(entries):
        fail("payload_file_count does not match manifest entries")
    if manifest.get("payload_total_bytes") != EXPECTED_PAYLOAD_BYTES:
        fail("manifest payload_total_bytes does not match accession anchor")
    return manifest, entries, manifest_bytes


def observed_payload_paths(root: Path) -> list[str]:
    paths: list[str] = []
    for directory in PAYLOAD_DIRECTORIES:
        base = root / directory
        if not base.is_dir() or base.is_symlink():
            fail(f"missing or invalid payload directory: {directory}")
        for candidate in base.rglob("*"):
            if candidate.is_symlink():
                fail(f"symlink found in payload: {candidate}")
            if candidate.is_file():
                paths.append(candidate.relative_to(root).as_posix())
    return sorted(paths)


def verify_payload(root: Path, entries: list[dict]) -> dict[str, int]:
    expected_paths = [entry["archive_path"] for entry in entries]
    actual_paths = observed_payload_paths(root)
    if actual_paths != expected_paths:
        missing = sorted(set(expected_paths) - set(actual_paths))
        extra = sorted(set(actual_paths) - set(expected_paths))
        fail(f"payload path mismatch; missing={missing}, extra={extra}")

    total_bytes = 0
    for entry in entries:
        relative = safe_relative_path(entry["archive_path"])
        path = root / relative
        observed_bytes = path.stat().st_size
        observed_sha256 = sha256_file(path)
        if observed_bytes != entry["bytes"]:
            fail(f"payload byte count mismatch: {entry['archive_path']}")
        if observed_sha256 != entry["sha256"]:
            fail(f"payload SHA-256 mismatch: {entry['archive_path']}")
        total_bytes += observed_bytes
    if total_bytes != EXPECTED_PAYLOAD_BYTES:
        fail(f"payload total byte mismatch: {total_bytes}")
    return {"files": len(entries), "bytes": total_bytes}


def parse_sidecar(path: Path) -> tuple[str, str, bytes]:
    if path.is_symlink() or not path.is_file():
        fail(f"missing sidecar: {path}")
    sidecar_bytes = path.read_bytes()
    try:
        lines = sidecar_bytes.decode("utf-8").splitlines()
    except UnicodeDecodeError as error:
        fail(f"sidecar is not UTF-8: {error}")
    if len(lines) != 1:
        fail("ZIP sidecar must contain exactly one line")
    match = HASH_LINE.fullmatch(lines[0])
    if match is None:
        fail("invalid ZIP sidecar format")
    digest, recorded_path = match.groups()
    if digest != EXPECTED_ZIP_SHA256:
        fail("ZIP sidecar hash does not match the accession anchor")
    if recorded_path != EXPECTED_ZIP_SIDECAR_PATH:
        fail("ZIP sidecar recorded path does not match the original")
    return digest, recorded_path, sidecar_bytes


def verify_source_zip(
    root: Path,
    entries: list[dict],
    manifest_bytes: bytes,
    source_zip: Path,
    source_sidecar: Path | None,
    source_manifest: Path | None,
) -> dict[str, object]:
    if source_zip.is_symlink() or not source_zip.is_file():
        fail(f"missing source ZIP: {source_zip}")
    observed_bytes = source_zip.stat().st_size
    observed_sha256 = sha256_file(source_zip)
    if observed_bytes != EXPECTED_ZIP_BYTES:
        fail(f"source ZIP byte count mismatch: {observed_bytes}")
    if observed_sha256 != EXPECTED_ZIP_SHA256:
        fail("source ZIP SHA-256 mismatch")

    archive_sidecar = root / SIDECAR_NAME
    _, _, archive_sidecar_bytes = parse_sidecar(archive_sidecar)
    sidecar_path = source_sidecar or Path(f"{source_zip}.sha256")
    if not sidecar_path.is_file():
        fail(f"missing source sidecar: {sidecar_path}")
    _, _, source_sidecar_bytes = parse_sidecar(sidecar_path)
    if source_sidecar_bytes != archive_sidecar_bytes:
        fail("accessioned sidecar differs from the original sidecar")

    manifest_path = source_manifest or (
        source_zip.parent / "PATTERN_MAP_V15_2_OWNER_HANDOFF-manifest.json"
    )
    if not manifest_path.is_file():
        fail(f"missing source manifest: {manifest_path}")
    source_manifest_bytes = manifest_path.read_bytes()
    if source_manifest_bytes != manifest_bytes:
        fail("accessioned manifest differs from the original manifest")
    if sha256_bytes(source_manifest_bytes) != EXPECTED_MANIFEST_SHA256:
        fail("source manifest SHA-256 mismatch")

    expected_members = {
        f"{ZIP_MEMBER_ROOT}/{entry['archive_path']}" for entry in entries
    }
    expected_members.add(f"{ZIP_MEMBER_ROOT}/00_START_HERE/PACKAGE_MANIFEST.json")
    with zipfile.ZipFile(source_zip, "r") as archive:
        infos = archive.infolist()
        observed_members = [info.filename for info in infos]
        if len(observed_members) != len(set(observed_members)):
            fail("source ZIP contains duplicate members")
        if set(observed_members) != expected_members:
            missing = sorted(expected_members - set(observed_members))
            extra = sorted(set(observed_members) - expected_members)
            fail(f"source ZIP member mismatch; missing={missing}, extra={extra}")
        if any(info.is_dir() for info in infos):
            fail("source ZIP contains an unexpected directory member")
        for entry in entries:
            member = f"{ZIP_MEMBER_ROOT}/{entry['archive_path']}"
            content = archive.read(member)
            if len(content) != entry["bytes"]:
                fail(f"source ZIP payload byte count mismatch: {member}")
            if sha256_bytes(content) != entry["sha256"]:
                fail(f"source ZIP payload SHA-256 mismatch: {member}")
        embedded = archive.read(f"{ZIP_MEMBER_ROOT}/00_START_HERE/PACKAGE_MANIFEST.json")
        if embedded != manifest_bytes:
            fail("embedded package manifest differs from the external manifest")
        bad_member = archive.testzip()
        if bad_member is not None:
            fail(f"source ZIP CRC failure: {bad_member}")

    return {
        "bytes": observed_bytes,
        "sha256": observed_sha256,
        "zip_members": len(observed_members),
        "sidecar_bytes_match": True,
        "manifest_bytes_match": True,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=ARCHIVE_ROOT,
        help="accession root; defaults to the directory containing this script",
    )
    parser.add_argument(
        "--source-zip",
        type=Path,
        default=None,
        help="verified external source ZIP; required for the complete container check",
    )
    parser.add_argument("--source-sidecar", type=Path, default=None)
    parser.add_argument("--source-manifest", type=Path, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root.resolve()
    manifest, entries, manifest_bytes = load_manifest(root)
    payload = verify_payload(root, entries)
    _, _, sidecar_bytes = parse_sidecar(root / SIDECAR_NAME)

    result: dict[str, object] = {
        "status": "PASS",
        "accession_root": str(root),
        "package_id": manifest["package_id"],
        "source_commit": manifest["source"]["commit"],
        "payload_files": payload["files"],
        "payload_bytes": payload["bytes"],
        "manifest_bytes": len(manifest_bytes),
        "manifest_sha256": sha256_bytes(manifest_bytes),
        "sidecar_bytes": len(sidecar_bytes),
        "source_zip_verified": False,
    }
    if args.source_zip is not None:
        result["source_zip"] = verify_source_zip(
            root,
            entries,
            manifest_bytes,
            args.source_zip.resolve(),
            args.source_sidecar.resolve() if args.source_sidecar else None,
            args.source_manifest.resolve() if args.source_manifest else None,
        )
        result["source_zip_verified"] = True
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
