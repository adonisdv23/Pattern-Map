#!/usr/bin/env python3
"""Verify that every current visual-evidence file is the format its name claims.

Why this exists
---------------
The independent round-one review found that files under `qa/visual/` were named
`.png` while their bytes were JPEG. That is a small defect with a large meaning
for this project: a publication arguing that provenance and inspection matter
cannot ship review evidence whose label disagrees with its content. The current
evidence was renamed to match its bytes, and this check keeps it that way.

Archive exception
-----------------
`archive/` and `research/**/preserved/` are immutable after accession. Some
accessioned files carry the same mismatch. Renaming them would break the byte
and history preservation rule, so they are reported as a known preserved
condition rather than corrected. That is the documented trade-off, not an
oversight.

Usage
-----
    python3 qa/visual/verify_image_formats.py            # fail on mismatch
    python3 qa/visual/verify_image_formats.py --report   # list preserved cases
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SIGNATURES = {
    "png": (b"\x89PNG\r\n\x1a\n",),
    "jpg": (b"\xff\xd8\xff",),
    "jpeg": (b"\xff\xd8\xff",),
    "gif": (b"GIF87a", b"GIF89a"),
    "webp": (b"RIFF",),
}

# Paths whose bytes and names are frozen by the archive and preservation rules.
IMMUTABLE_PREFIXES = ("archive/", "research/the-echo-problem/preserved/")

CHECKED_SUFFIXES = tuple(f".{name}" for name in SIGNATURES)


def actual_format(data: bytes) -> str:
    for name, prefixes in SIGNATURES.items():
        if name == "jpeg":
            continue
        if any(data.startswith(prefix) for prefix in prefixes):
            return name
    return "unknown"


def scan() -> tuple[list[tuple[str, str, str]], list[tuple[str, str, str]]]:
    current: list[tuple[str, str, str]] = []
    preserved: list[tuple[str, str, str]] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in CHECKED_SUFFIXES:
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative.startswith(".git/"):
            continue
        claimed = path.suffix.lower().lstrip(".")
        claimed = "jpg" if claimed == "jpeg" else claimed
        found = actual_format(path.read_bytes()[:16])
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
    parser.add_argument("--report", action="store_true", help="list preserved archive mismatches too")
    args = parser.parse_args()

    current, preserved = scan()

    if args.report and preserved:
        print(f"Preserved archive mismatches (immutable, not corrected): {len(preserved)}")
        for relative, claimed, found in preserved:
            print(f"  {relative}: named .{claimed}, bytes are {found}")

    if current:
        print(f"FAIL: {len(current)} current evidence file(s) claim a format their bytes do not match")
        for relative, claimed, found in current:
            print(f"  {relative}: named .{claimed}, bytes are {found}")
        print("Rename the file to match its bytes with `git mv`, then update every reference to it.")
        return 1

    print(
        f"PASS current visual evidence formats match their names "
        f"({len(preserved)} immutable archive mismatch(es) preserved by policy)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
