#!/usr/bin/env python3
"""Verify selected version anchors without duplicating immutable transfers.

This is an archive-integrity check. It does not run a model, provider, study,
participant workflow, deployment, publication, or external action.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INDEX = Path(__file__).with_name("CHECKPOINT_INDEX.json")
EXPECTED_VERSIONS = ["v13", "v14", "v15", "v15.1", "v15.2"]


def fail(message: str) -> None:
    print(f"FAIL  {message}", file=sys.stderr)
    raise SystemExit(1)


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def main() -> int:
    try:
        index = json.loads(INDEX.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read checkpoint index: {exc}")

    if index.get("schema_version") != "pattern-map.archive-checkpoint-index.v1":
        fail("unexpected checkpoint-index schema version")

    versions = index.get("versions")
    if not isinstance(versions, list):
        fail("versions must be a list")
    if [item.get("version") for item in versions] != EXPECTED_VERSIONS:
        fail("version order or membership changed")

    seen: set[str] = set()
    checked_files = 0
    checked_bytes = 0

    for version in versions:
        anchors = version.get("anchors")
        if not isinstance(anchors, list) or not anchors:
            fail(f"{version.get('version')} has no anchors")
        for anchor in anchors:
            relative = anchor.get("path")
            if not isinstance(relative, str) or not relative.startswith("archive/transfers/"):
                fail(f"unsafe or non-transfer anchor path: {relative!r}")
            if relative in seen:
                fail(f"duplicate anchor path: {relative}")
            seen.add(relative)

            path = ROOT / relative
            if not path.is_file():
                fail(f"missing anchor: {relative}")
            actual_bytes = path.stat().st_size
            if actual_bytes != anchor.get("bytes"):
                fail(
                    f"byte mismatch for {relative}: expected {anchor.get('bytes')}, "
                    f"got {actual_bytes}"
                )
            actual_hash = digest(path)
            if actual_hash != anchor.get("sha256"):
                fail(f"SHA-256 mismatch for {relative}")
            checked_files += 1
            checked_bytes += actual_bytes

    v152 = versions[-1]
    container = v152.get("external_container", {})
    if container.get("stored_in_git") is not False:
        fail("v15.2 exact ZIP must remain recorded as outside ordinary Git")
    if container.get("bytes") != 41436496:
        fail("v15.2 exact ZIP byte count changed")
    if container.get("sha256") != (
        "f8b71db0bda7f7564e5d3cec1f697bee38b3fcb17b56f47c79bf653f39b549b5"
    ):
        fail("v15.2 exact ZIP hash changed")

    print(
        f"PASS  checkpoint index: {len(versions)} versions, "
        f"{checked_files} selected anchors, {checked_bytes} bytes"
    )
    print("PASS  v15.2 exact ZIP remains hash-anchored outside ordinary Git")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
