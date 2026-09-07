#!/usr/bin/env python3
"""Verify the v15 manifest, checksum ledger, and deterministic ZIP archive."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path, PurePosixPath


DEFAULT_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_RELATIVE = Path("handoff/V15_PACKAGE_MANIFEST.json")
CHECKSUM_RELATIVE = Path("handoff/V15_SHA256SUMS.txt")
DEFAULT_ZIP_RELATIVE = Path("exports/DISCRIMINATION_LAYER_V15_OWNER_PACKAGE.zip")
ARCHIVE_ROOT = "Discrimination-Layer-v15"
ZIP_TIMESTAMP = (2026, 8, 18, 12, 0, 0)
HASH_LINE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_checksum_ledger(path: Path) -> dict[str, str]:
    records: dict[str, str] = {}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = HASH_LINE.fullmatch(line)
        if not match:
            raise ValueError(f"invalid checksum line {number}: {line!r}")
        digest, relative = match.groups()
        if relative in records:
            raise ValueError(f"duplicate checksum path: {relative}")
        records[relative] = digest
    return records


def safe_relative_path(value: str) -> Path:
    pure = PurePosixPath(value)
    if pure.is_absolute() or not pure.parts or ".." in pure.parts:
        raise ValueError(f"unsafe manifest path: {value}")
    return Path(*pure.parts)


def verify_filesystem(root: Path) -> tuple[dict, list[dict], dict[str, str]]:
    manifest_path = root / MANIFEST_RELATIVE
    checksum_path = root / CHECKSUM_RELATIVE
    manifest_data = manifest_path.read_bytes()
    manifest = json.loads(manifest_data)

    if manifest.get("schema_version") != "1.0":
        raise ValueError("unexpected manifest schema_version")
    if manifest.get("package_id") != "discrimination-layer-v15-owner-review":
        raise ValueError("unexpected package_id")
    if manifest.get("status") != "LOCAL_OWNER_REVIEW_NO_EMPIRICAL_RESULTS_NOT_PUBLISHED":
        raise ValueError("unexpected release status")

    entries = manifest.get("files")
    if not isinstance(entries, list) or not entries:
        raise ValueError("manifest files must be a non-empty list")
    if manifest.get("payload_file_count") != len(entries):
        raise ValueError("payload_file_count does not match file entries")

    paths = [entry.get("path") for entry in entries]
    if paths != sorted(paths):
        raise ValueError("manifest file entries are not sorted")
    if len(paths) != len(set(paths)):
        raise ValueError("manifest has duplicate paths")

    computed_total = 0
    expected_checksums: dict[str, str] = {}
    for entry in entries:
        relative_text = entry.get("path")
        if not isinstance(relative_text, str):
            raise ValueError("manifest entry has no string path")
        relative = safe_relative_path(relative_text)
        absolute = root / relative
        if absolute.is_symlink() or not absolute.is_file():
            raise ValueError(f"missing or non-regular payload: {relative_text}")
        size = absolute.stat().st_size
        digest = sha256_file(absolute)
        if size != entry.get("bytes"):
            raise ValueError(f"size mismatch: {relative_text}")
        if digest != entry.get("sha256"):
            raise ValueError(f"hash mismatch: {relative_text}")
        computed_total += size
        expected_checksums[relative_text] = digest

    if computed_total != manifest.get("payload_total_bytes"):
        raise ValueError("payload_total_bytes mismatch")

    expected_checksums[MANIFEST_RELATIVE.as_posix()] = sha256_bytes(manifest_data)
    observed_checksums = parse_checksum_ledger(checksum_path)
    if observed_checksums != expected_checksums:
        missing = sorted(set(expected_checksums) - set(observed_checksums))
        extra = sorted(set(observed_checksums) - set(expected_checksums))
        wrong = sorted(
            path
            for path in set(expected_checksums) & set(observed_checksums)
            if expected_checksums[path] != observed_checksums[path]
        )
        raise ValueError(
            f"checksum ledger mismatch; missing={missing}, extra={extra}, wrong={wrong}"
        )

    return manifest, entries, expected_checksums


def verify_sidecar(zip_path: Path, sidecar_path: Path) -> str:
    lines = sidecar_path.read_text(encoding="utf-8").splitlines()
    if len(lines) != 1:
        raise ValueError("ZIP checksum sidecar must contain exactly one line")
    match = HASH_LINE.fullmatch(lines[0])
    if not match:
        raise ValueError("invalid ZIP checksum sidecar")
    expected_hash, recorded_path = match.groups()
    if recorded_path != DEFAULT_ZIP_RELATIVE.as_posix():
        raise ValueError(f"unexpected ZIP path in sidecar: {recorded_path}")
    observed_hash = sha256_file(zip_path)
    if observed_hash != expected_hash:
        raise ValueError("ZIP container hash does not match sidecar")
    return observed_hash


def verify_zip(
    root: Path,
    zip_path: Path,
    sidecar_path: Path,
    entries: list[dict],
) -> tuple[str, int]:
    zip_hash = verify_sidecar(zip_path, sidecar_path)
    expected_relative = [entry["path"] for entry in entries] + [
        MANIFEST_RELATIVE.as_posix(),
        CHECKSUM_RELATIVE.as_posix(),
    ]
    expected_members = sorted(f"{ARCHIVE_ROOT}/{path}" for path in expected_relative)

    with zipfile.ZipFile(zip_path, "r") as archive:
        infos = archive.infolist()
        observed_members = [info.filename for info in infos]
        if observed_members != expected_members:
            missing = sorted(set(expected_members) - set(observed_members))
            extra = sorted(set(observed_members) - set(expected_members))
            raise ValueError(
                f"ZIP member mismatch; missing={missing}, extra={extra}, "
                "or member ordering is non-deterministic"
            )
        if len(observed_members) != len(set(observed_members)):
            raise ValueError("ZIP contains duplicate members")

        for info in infos:
            pure = PurePosixPath(info.filename)
            if pure.is_absolute() or ".." in pure.parts:
                raise ValueError(f"unsafe ZIP member: {info.filename}")
            if info.is_dir():
                raise ValueError(f"unexpected directory member: {info.filename}")
            if info.date_time != ZIP_TIMESTAMP:
                raise ValueError(f"non-deterministic timestamp: {info.filename}")
            mode = (info.external_attr >> 16) & 0o777
            if mode != 0o644:
                raise ValueError(f"unexpected ZIP mode {oct(mode)}: {info.filename}")
            if info.compress_type != zipfile.ZIP_DEFLATED:
                raise ValueError(f"unexpected compression: {info.filename}")

            relative_text = str(pure.relative_to(ARCHIVE_ROOT))
            filesystem_bytes = (root / safe_relative_path(relative_text)).read_bytes()
            archive_bytes = archive.read(info)
            if archive_bytes != filesystem_bytes:
                raise ValueError(f"ZIP content differs from filesystem: {relative_text}")

        bad_member = archive.testzip()
        if bad_member is not None:
            raise ValueError(f"ZIP CRC failure: {bad_member}")

    return zip_hash, len(expected_members)


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help="repository or extracted package root",
    )
    parser.add_argument(
        "--zip",
        dest="zip_path",
        type=Path,
        default=None,
        help="optional ZIP archive to verify",
    )
    parser.add_argument(
        "--zip-sidecar",
        type=Path,
        default=None,
        help="ZIP SHA-256 sidecar; defaults to <zip>.sha256",
    )
    return parser.parse_args()


def main() -> None:
    args = arguments()
    root = args.root.resolve()
    manifest, entries, expected_checksums = verify_filesystem(root)

    result = {
        "status": "PASS",
        "package_id": manifest["package_id"],
        "source_commit": manifest["source"]["commit"],
        "payload_files": len(entries),
        "checksums_verified": len(expected_checksums),
        "payload_total_bytes": manifest["payload_total_bytes"],
        "zip_verified": False,
    }

    if args.zip_path is not None:
        zip_path = args.zip_path.resolve()
        sidecar_path = (
            args.zip_sidecar.resolve()
            if args.zip_sidecar is not None
            else Path(f"{zip_path}.sha256")
        )
        zip_hash, member_count = verify_zip(
            root, zip_path, sidecar_path, entries
        )
        result.update(
            {
                "zip_verified": True,
                "zip_members": member_count,
                "zip_sha256": zip_hash,
                "zip_bytes": zip_path.stat().st_size,
            }
        )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
