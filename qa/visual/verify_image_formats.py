#!/usr/bin/env python3
"""Check that image extensions agree with their byte signatures.

The owner-review evidence under ``qa/visual`` is current, inspectable material,
so a misleading extension is a real QA defect. Historical and preserved
research trees are different: their bytes are immutable after accession. This
checker reports those mismatches without proposing a rename.

Usage::

    python3 qa/visual/verify_image_formats.py
    python3 qa/visual/verify_image_formats.py --report

The default command fails only when a non-immutable image has a mismatched
extension. ``--report`` also prints preserved mismatches for an explicit
provenance record.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
IMAGE_EXTENSIONS = {".gif", ".jpeg", ".jpg", ".png", ".webp"}
IMMUTABLE_PREFIXES = (
    "archive/",
    "research/the-echo-problem/preserved/",
)


def actual_format(prefix: bytes) -> str:
    """Return the canonical extension implied by a file signature."""

    if prefix.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if prefix.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if prefix.startswith((b"GIF87a", b"GIF89a")):
        return ".gif"
    if prefix.startswith(b"RIFF") and prefix[8:12] == b"WEBP":
        return ".webp"
    return "unknown"


def scan() -> tuple[list[tuple[str, str, str]], list[tuple[str, str, str]]]:
    current: list[tuple[str, str, str]] = []
    preserved: list[tuple[str, str, str]] = []

    for candidate in sorted(ROOT.rglob("*")):
        if not candidate.is_file() or candidate.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        relative = candidate.relative_to(ROOT).as_posix()
        claimed = candidate.suffix.lower()
        found = actual_format(candidate.read_bytes()[:16])
        if found == claimed:
            continue
        record = (relative, claimed, found)
        if relative.startswith(IMMUTABLE_PREFIXES):
            preserved.append(record)
        else:
            current.append(record)

    return current, preserved


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--report",
        action="store_true",
        help="also list mismatches in immutable archive/preserved trees",
    )
    args = parser.parse_args()

    current, preserved = scan()

    if args.report:
        if preserved:
            print(f"Preserved mismatches (immutable, not corrected): {len(preserved)}")
            for relative, claimed, found in preserved:
                print(f"  {relative}: named {claimed}, bytes are {found}")
        else:
            print("Preserved mismatches: 0")

    if current:
        print(f"FAIL current image-extension mismatches: {len(current)}")
        for relative, claimed, found in current:
            print(f"  {relative}: named {claimed}, bytes are {found}")
        print("Rename current evidence with git mv, then update active references.")
        return 1

    print(
        "PASS current image extensions match their byte signatures "
        f"({len(preserved)} immutable mismatch(es) retained by policy)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
