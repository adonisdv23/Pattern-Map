#!/usr/bin/env python3
"""Verify one extracted Pattern Map v16 owner-review bundle.

This standard-library verifier checks the complete packaged Git payload and
the generated control files.  It proves consistency with the manifest that
travelled in the same ZIP; the separately delivered ZIP SHA-256 sidecar is the
outer byte-identity check.  Neither mechanism is a digital signature.
"""

from __future__ import annotations

import datetime as _datetime
import hashlib
import json
import os
import re
import stat
import sys
import unicodedata
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "FULL_PAYLOAD_MANIFEST.json"
METADATA_PATH = ROOT / "PACKAGE_METADATA.json"

PACKAGE_NAME = "pattern-map-v16-owner-review"
OWNER_INTENT_SHA256 = "3aea5eeb19302a0e6498f7bcfccb23535953dbb6807fb5a486e0279bfa72543b"
PACKAGE_STATUS = (
    "private owner-review candidate; not merged, deployed, published, released, "
    "or empirically validated"
)
PAYLOAD_SCOPE = "complete regular-file payload from one exact committed Pattern Map Git tree"
VERIFICATION_SCOPE = (
    "complete path, byte-count, and SHA-256 consistency for the extracted payload "
    "plus generated controls, with canonical schema validation for recorded Git modes; "
    "authenticity still depends on the separately delivered ZIP SHA-256 sidecar"
)
MANUAL_GATES = [
    "owner/mentor comprehension, voice, naming, and taste",
    "physical keyboard and hardware touch",
    "supported screen reader",
    "real 200 percent zoom and forced colors",
    "native browser print preview",
    "publication identity, rights, metadata, links, destination, and authorization",
]
PROHIBITED_ACTIONS = [
    "merge",
    "deploy",
    "publish",
    "release",
    "run a study or provider/model call",
    "spend or acquire an external dataset",
    "preregister or contact people",
]
METADATA_KEYS = {
    "schema_version",
    "package",
    "status",
    "generated_date",
    "source_commit",
    "source_short_commit",
    "owner_intent_sha256",
    "root_directory",
    "payload_scope",
    "verification_scope",
    "bounded_manifest_path",
    "external_sidecar_required",
    "manual_gates",
    "prohibited_actions",
}
MANIFEST_KEYS = {
    "schema_version",
    "package",
    "status",
    "source_commit",
    "root_directory",
    "payload_root",
    "file_count",
    "total_bytes",
    "control_files",
    "files",
}
RECORD_KEYS = {"path", "mode", "bytes", "sha256"}
CONTROL_PATHS = {"START_HERE.md", "PACKAGE_METADATA.json", "VERIFY_PACKAGE.py"}
PRIVATE_KEY_MARKERS = (
    ("-----BEGIN " + "PRIVATE KEY-----").encode("ascii"),
    ("-----BEGIN " + "OPENSSH PRIVATE KEY-----").encode("ascii"),
    ("-----BEGIN " + "RSA PRIVATE KEY-----").encode("ascii"),
    ("-----BEGIN " + "EC PRIVATE KEY-----").encode("ascii"),
)
KNOWN_PRIVATE_KEY_MARKER_FIXTURES = {
    "repository/qa/handoff/test_portable_bundle.py": (
        "7871504bf6d0fbb592a5193b0d8af7d5c0eccd4c3a0f50833cc817250bff2aa2"
    ),
}
WINDOWS_FORBIDDEN_CHARACTERS = set('<>:"|?*')
WINDOWS_RESERVED_BASENAMES = {
    "con",
    "prn",
    "aux",
    "nul",
    *(f"com{index}" for index in range(1, 10)),
    *(f"lpt{index}" for index in range(1, 10)),
}


class VerificationError(RuntimeError):
    """A stable, recipient-readable package verification failure."""


def strict_json_object(path: Path) -> dict[str, object]:
    def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
        result: dict[str, object] = {}
        for key, value in pairs:
            if key in result:
                raise VerificationError(f"{path.name}: duplicate object key {key!r}")
            result[key] = value
        return result

    def reject_nonfinite(value: str) -> object:
        raise VerificationError(f"{path.name}: non-finite JSON value {value!r}")

    try:
        relative = path.relative_to(ROOT).as_posix()
        text = regular_bytes(relative).decode("utf-8")
        payload = json.loads(
            text,
            object_pairs_hook=reject_duplicate_keys,
            parse_constant=reject_nonfinite,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        raise VerificationError(f"cannot parse {path.name}: {error}") from error
    if not isinstance(payload, dict):
        raise VerificationError(f"{path.name}: root must be a JSON object")
    return payload


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_relative(value: object) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        raise VerificationError(f"invalid manifest path: {value!r}")
    parsed = PurePosixPath(value)
    if parsed.is_absolute() or any(part in {"", ".", ".."} for part in parsed.parts):
        raise VerificationError(f"unsafe manifest path: {value!r}")
    if value != parsed.as_posix():
        raise VerificationError(f"non-portable manifest path: {value!r}")
    for part in parsed.parts:
        if any(ord(character) < 32 or ord(character) == 127 for character in part):
            raise VerificationError(f"control character in manifest path: {value!r}")
        if any(character in WINDOWS_FORBIDDEN_CHARACTERS for character in part):
            raise VerificationError(f"cross-platform-forbidden manifest path: {value!r}")
        if part.endswith((" ", ".")):
            raise VerificationError(f"trailing dot/space in manifest path: {value!r}")
        basename = part.split(".", 1)[0].casefold()
        if basename in WINDOWS_RESERVED_BASENAMES:
            raise VerificationError(f"reserved cross-platform manifest path: {value!r}")
    return value


def portable_path_key(relative: str) -> str:
    """Return the case- and Unicode-normalized collision key for one safe path."""

    safe_relative(relative)
    return unicodedata.normalize("NFC", relative).casefold()


def regular_bytes(relative: str) -> bytes:
    current = ROOT
    for part in PurePosixPath(relative).parts:
        current = current / part
        if current.is_symlink():
            raise VerificationError(f"symlink is not allowed: {relative}")
    try:
        mode = current.lstat().st_mode
    except FileNotFoundError as error:
        raise VerificationError(f"missing packaged file: {relative}") from error
    if not stat.S_ISREG(mode):
        raise VerificationError(f"non-regular packaged path: {relative}")
    try:
        return current.read_bytes()
    except OSError as error:
        raise VerificationError(f"cannot read packaged file {relative}: {error}") from error


def validate_record(record: object, *, label: str) -> dict[str, object]:
    if not isinstance(record, dict) or set(record) != RECORD_KEYS:
        raise VerificationError(f"{label}: record must contain path/mode/bytes/sha256 only")
    relative = safe_relative(record["path"])
    mode = record["mode"]
    byte_count = record["bytes"]
    digest = record["sha256"]
    if mode not in {"100644", "100755"}:
        raise VerificationError(f"{label}: unsupported Git mode for {relative}")
    if type(byte_count) is not int or byte_count < 0:
        raise VerificationError(f"{label}: invalid byte count for {relative}")
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise VerificationError(f"{label}: invalid SHA-256 for {relative}")
    return record


def verify_records(records: object, *, label: str) -> tuple[list[str], int]:
    if not isinstance(records, list):
        raise VerificationError(f"{label}: records must be a list")
    paths: list[str] = []
    casefold_paths: dict[str, str] = {}
    total = 0
    for index, raw_record in enumerate(records):
        record = validate_record(raw_record, label=f"{label}[{index}]")
        relative = str(record["path"])
        if relative in paths:
            raise VerificationError(f"{label}: duplicate path {relative}")
        folded = portable_path_key(relative)
        if folded in casefold_paths:
            raise VerificationError(
                f"{label}: case-colliding paths {casefold_paths[folded]} and {relative}"
            )
        data = regular_bytes(relative)
        if len(data) != record["bytes"]:
            raise VerificationError(f"byte-count mismatch: {relative}")
        if sha256_bytes(data) != record["sha256"]:
            raise VerificationError(f"SHA-256 mismatch: {relative}")
        if any(marker in data for marker in PRIVATE_KEY_MARKERS):
            expected_fixture_digest = KNOWN_PRIVATE_KEY_MARKER_FIXTURES.get(relative)
            if not expected_fixture_digest or sha256_bytes(data) != expected_fixture_digest:
                raise VerificationError(f"private-key marker in packaged file: {relative}")
        paths.append(relative)
        casefold_paths[folded] = relative
        total += len(data)
    if paths != sorted(paths):
        raise VerificationError(f"{label}: records are not sorted by path")
    return paths, total


def physical_inventory() -> tuple[set[str], set[str]]:
    files: set[str] = set()
    directories: set[str] = set()
    for directory, directory_names, file_names in os.walk(ROOT, followlinks=False):
        base = Path(directory)
        for name in list(directory_names):
            candidate = base / name
            relative = candidate.relative_to(ROOT).as_posix()
            if candidate.is_symlink():
                raise VerificationError(f"symlink directory is not allowed: {relative}")
            if not stat.S_ISDIR(candidate.lstat().st_mode):
                raise VerificationError(f"non-directory path is not allowed: {relative}")
            safe_relative(relative)
            directories.add(relative)
        for name in file_names:
            candidate = base / name
            relative = candidate.relative_to(ROOT).as_posix()
            if candidate.is_symlink():
                raise VerificationError(f"symlink file is not allowed: {relative}")
            if not stat.S_ISREG(candidate.lstat().st_mode):
                raise VerificationError(f"non-regular file is not allowed: {relative}")
            safe_relative(relative)
            files.add(relative)
    return files, directories


def parent_directories(paths: set[str]) -> set[str]:
    expected: set[str] = set()
    for relative in paths:
        parent = PurePosixPath(relative).parent
        while parent.as_posix() != ".":
            expected.add(parent.as_posix())
            parent = parent.parent
    return expected


def verify() -> None:
    if Path(__file__).is_symlink():
        raise VerificationError("VERIFY_PACKAGE.py itself may not be a symlink")
    metadata = strict_json_object(METADATA_PATH)
    manifest = strict_json_object(MANIFEST_PATH)

    if set(metadata) != METADATA_KEYS:
        raise VerificationError("PACKAGE_METADATA.json has missing or extra control keys")
    if type(metadata["schema_version"]) is not int or metadata["schema_version"] != 1:
        raise VerificationError("package metadata schema version must be exact integer 1")
    if metadata["package"] != PACKAGE_NAME:
        raise VerificationError("package metadata identity/schema mismatch")
    if metadata["status"] != PACKAGE_STATUS:
        raise VerificationError("package metadata status/authority boundary mismatch")
    generated_date = metadata["generated_date"]
    if not isinstance(generated_date, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", generated_date):
        raise VerificationError("package metadata date is not YYYY-MM-DD")
    try:
        parsed_date = _datetime.date.fromisoformat(generated_date)
    except ValueError as error:
        raise VerificationError("package metadata date is not a valid calendar date") from error
    if parsed_date.isoformat() != generated_date:
        raise VerificationError("package metadata date is not canonical YYYY-MM-DD")
    source_commit = metadata["source_commit"]
    if not isinstance(source_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        raise VerificationError("package metadata source commit is invalid")
    if metadata["source_short_commit"] != source_commit[:12]:
        raise VerificationError("package metadata short commit mismatch")
    if metadata["owner_intent_sha256"] != OWNER_INTENT_SHA256:
        raise VerificationError("package metadata owner-intent checkpoint mismatch")
    expected_root = f"Pattern-Map-v16-{source_commit[:12]}"
    if metadata["root_directory"] != expected_root or ROOT.name != expected_root:
        raise VerificationError("extracted root directory does not match the exact source commit")
    if metadata["payload_scope"] != PAYLOAD_SCOPE:
        raise VerificationError("package metadata payload-scope mismatch")
    if metadata["verification_scope"] != VERIFICATION_SCOPE:
        raise VerificationError("package metadata verification-scope mismatch")
    if metadata["bounded_manifest_path"] != "repository/handoff/OWNER_REVIEW_MANIFEST_V16.json":
        raise VerificationError("bounded-manifest pointer mismatch")
    if metadata["external_sidecar_required"] is not True:
        raise VerificationError("package metadata must require the external ZIP sidecar")
    if metadata["manual_gates"] != MANUAL_GATES:
        raise VerificationError("package metadata manual-gate boundary mismatch")
    if metadata["prohibited_actions"] != PROHIBITED_ACTIONS:
        raise VerificationError("package metadata prohibited-action boundary mismatch")

    if set(manifest) != MANIFEST_KEYS:
        raise VerificationError("FULL_PAYLOAD_MANIFEST.json has missing or extra control keys")
    if type(manifest["schema_version"]) is not int or manifest["schema_version"] != 1:
        raise VerificationError("full manifest schema version must be exact integer 1")
    if manifest["package"] != PACKAGE_NAME:
        raise VerificationError("full manifest identity/schema mismatch")
    if manifest["status"] != PACKAGE_STATUS:
        raise VerificationError("full manifest status/authority boundary mismatch")
    if manifest["source_commit"] != source_commit:
        raise VerificationError("full manifest source-commit mismatch")
    if manifest["root_directory"] != expected_root or manifest["payload_root"] != "repository":
        raise VerificationError("full manifest root/payload-scope mismatch")

    control_paths, _control_bytes = verify_records(
        manifest["control_files"], label="control_files"
    )
    if set(control_paths) != CONTROL_PATHS:
        raise VerificationError("full manifest control-file set mismatch")
    payload_paths, total = verify_records(manifest["files"], label="files")
    if any(not path.startswith("repository/") for path in payload_paths):
        raise VerificationError("full manifest payload path is outside repository/")
    if type(manifest["file_count"]) is not int or manifest["file_count"] != len(payload_paths):
        raise VerificationError("full manifest file-count mismatch")
    if type(manifest["total_bytes"]) is not int or manifest["total_bytes"] != total:
        raise VerificationError("full manifest total-byte mismatch")

    expected_files = set(control_paths) | set(payload_paths) | {"FULL_PAYLOAD_MANIFEST.json"}
    expected_casefold = {portable_path_key(path) for path in expected_files}
    if len(expected_casefold) != len(expected_files):
        raise VerificationError("manifest contains cross-scope case-colliding paths")
    observed_files, observed_directories = physical_inventory()
    if len({portable_path_key(path) for path in observed_files}) != len(observed_files):
        raise VerificationError("extracted package contains case-colliding physical paths")
    missing = sorted(expected_files - observed_files)
    extra = sorted(observed_files - expected_files)
    if missing or extra:
        raise VerificationError(f"extracted file-set mismatch; missing={missing}, extra={extra}")
    expected_directories = parent_directories(expected_files)
    missing_directories = sorted(expected_directories - observed_directories)
    extra_directories = sorted(observed_directories - expected_directories)
    if missing_directories or extra_directories:
        raise VerificationError(
            "extracted directory-set mismatch; "
            f"missing={missing_directories}, extra={extra_directories}"
        )

    print(
        "PASS complete extracted owner bundle: "
        f"{len(payload_paths)} Git files / {total} payload bytes / source {source_commit}"
    )
    print(
        "BOUNDARY: this proves consistency with the bundled manifest; verify the "
        "original ZIP against its separately delivered SHA-256 sidecar for outer byte identity."
    )


def main() -> int:
    try:
        verify()
    except (VerificationError, OSError, ValueError) as error:
        print(f"FAIL extracted owner bundle: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
