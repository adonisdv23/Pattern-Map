#!/usr/bin/env python3
"""Build a deterministic, self-verifying Pattern Map → Signal Foundry bundle.

The builder reads every source payload from an explicit Git commit with
``git show``.  It never copies the working tree, so the provenance recorded in
the generated metadata is the provenance of the bytes that are shipped.  The
result is intentionally a small context bundle rather than a second checkout:
it contains the human thesis, the six-family framework, the operator/agent
playbook, the bounded Signal Foundry case, the local publication companions,
and the minimum research-separation records needed to keep The Echo Problem
separate and unrun.

Only Python's standard library is required.  The ZIP uses fixed timestamps,
fixed permissions, sorted members, and stored entries so repeated builds from
the same commit and date are byte-stable on the same Python/zlib toolchain.
"""

from __future__ import annotations

import argparse
import datetime as _datetime
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile
from typing import Mapping, Sequence
import zipfile


PACKAGE_NAME = "pattern-map-v16-signal-foundry-portable"
PACKAGE_PREFIX = "PATTERN_MAP_V16_SIGNAL_FOUNDRY_PORTABLE"
SOURCE_REPOSITORY = "https://github.com/adonisdv23/Pattern-Map"
SOURCE_BRANCH_HINT = "codex/pattern-map-v16-foundation"
DRAFT_PR = "https://github.com/adonisdv23/Pattern-Map/pull/1"
SIGNAL_FOUNDRY_AUDITED_CHECKPOINT = "f9bf3775ca3d5b52ea5083cea52306c025727e23"
PREVIOUS_BUNDLE_NAME = "PATTERN_MAP_V16_SIGNAL_FOUNDRY_PORTABLE_2026-08-23_e565502.zip"
PREVIOUS_BUNDLE_SHA256 = "b73c5c5ecfc12a7db255d1626688a256c2ef52bc69a5d892b8cfc1da670a3b29"

# Keep this list explicit.  A portable handoff should not silently grow to
# include a dependency tree, a generated site directory, or a private local
# artifact merely because one appears under a broad source directory.
SOURCE_PATHS: tuple[str, ...] = (
    "README.md",
    "AGENTS.md",
    "docs/OWNER_INTENT_V16.md",
    "docs/OWNER_INTENT_V16.sha256",
    "docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md",
    "docs/ARTIFACT_BOUNDARIES.md",
    "docs/SOURCE_AUTHORITY_AND_LINEAGE.md",
    "docs/V16_ACCEPTANCE_CRITERIA.md",
    "docs/DECISION_LOG.md",
    "docs/REVIEW_AND_DISPOSITION_PROTOCOL.md",
    "docs/CLAIMS_AND_SOURCE_LEDGER_V16.md",
    "docs/ADVISORY_REVIEW_DISPOSITIONS.md",
    "docs/TWO_PROJECT_SEPARATION.md",
    "manuscript/README.md",
    "manuscript/PATTERN_RECOGNITION_V16.md",
    "manuscript/NINETY_SECOND_VERSION.md",
    "manuscript/MENTOR_COVER_NOTE.md",
    "manuscript/PUBLIC_ABSTRACT.md",
    "manuscript/ORIGIN_NOTE.md",
    "manuscript/SOURCES_AND_RESEARCH_ROUTE.md",
    "framework/README.md",
    "framework/SIX_FAMILIES.md",
    "framework/SIX_FAMILIES.json",
    "framework/SIX_FAMILIES.schema.json",
    "framework/RELATIONSHIP_MAP.md",
    "framework/GLOSSARY.md",
    "framework/OPERATOR_PLAYBOOK.md",
    "framework/IMPLEMENTATION_CHOICES.md",
    "framework/MECHANISMS.md",
    "framework/BOUNDARIES_AND_FAILURES.md",
    "framework/mechanisms/README.md",
    "framework/templates/README.md",
    "framework/templates/ACQUISITION_RECEIPT.md",
    "framework/templates/COMPARISON_MATRIX.md",
    "framework/templates/DECISION_BRIEF.md",
    "framework/templates/DISCONFIRMATION_LOG.md",
    "framework/templates/EVIDENCE_REGISTER.md",
    "framework/templates/INFLUENCE_RECEIPT.md",
    "framework/templates/OUTCOME_REVIEW.md",
    "framework/agent-playbook/QUICKSTART.md",
    "framework/agent-playbook/FULL_OPERATING_GUIDE.md",
    "framework/agent-playbook/COPYABLE_AGENT_BRIEF.md",
    "framework/agent-playbook/PREFLIGHT_CHECKLIST.md",
    "framework/agent-playbook/DECISION_RECEIPT_TEMPLATE.md",
    "framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md",
    "cases/README.md",
    "cases/signal-foundry/README.md",
    "cases/general-research/README.md",
    "cases/product-and-process/README.md",
    "handoff/README.md",
    "handoff/OWNER_REVIEW_PACKET_V16.md",
    "handoff/PACKAGE_MAP_V16.md",
    "handoff/BRANCH_AND_PR_STATE.md",
    "handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md",
    "handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md",
    # Include the committed builder so a receiving task can inspect the exact
    # reproducibility mechanism used to make the packet.
    "handoff/signal-foundry/build_portable_bundle.py",
    "site/README.md",
    "site/exports/standalone/pattern-map-v16.html",
    "site/exports/pattern-map-v16-owner-review.pdf",
    "research/README.md",
    "research/THE_DISCRIMINATION_LAYER_RESEARCH_AGENDA.md",
    "research/future-studies/DL_PLAYBOOK_MATCHED_BUDGET_PROTOCOL_V0_1.md",
    "research/the-echo-problem/README.md",
    "research/the-echo-problem/STATUS_AND_BOUNDARIES.md",
    "research/the-echo-problem/RELATION_TO_V16.md",
    "research/the-echo-problem/VERSION_HISTORY.md",
    "research/the-echo-problem/FUTURE_EXECUTION_PLAN.md",
    "research/the-echo-problem/PRESERVED_V15_2_INDEX.md",
    "research/the-echo-problem/qa/EP_V0_1_STATUS.json",
    "research/the-echo-problem/v1_1/README.md",
    "research/the-echo-problem/v1_1/PROTOCOL_V1_1_DESIGN_CHECKPOINT.md",
    "research/the-echo-problem/v1_1/PRIOR_MEASUREMENT_MATRIX.md",
    "qa/README.md",
    "qa/FINAL_ACCEPTANCE_MATRIX_V16.md",
    "qa/FINAL_ACTION_AUDIT_V16.md",
    "qa/site/OWNER_VISUAL_EXPORT_CLOSEOUT_2026-08-23.md",
    "assets/IMAGE_USE_LEDGER.md",
    "assets/diagrams/historical-v13-pattern-recognition-diagram-v12.png",
)

GENERATED_PAYLOAD_NAMES: tuple[str, ...] = (
    "START_HERE.md",
    "COPYABLE_PROMPT.md",
    "BUNDLE_METADATA.json",
    "verify_bundle.py",
)
MANIFEST_NAME = "BUNDLE_MANIFEST.json"
CHECKSUMS_NAME = "SHA256SUMS.txt"
TEXT_SUFFIXES = frozenset(
    {".css", ".html", ".js", ".json", ".md", ".mjs", ".py", ".sh", ".txt", ".yaml", ".yml"}
)

# The strings are assembled instead of written as literal source-machine path
# prefixes.  This keeps the builder and generated verifier portable and makes
# it impossible to mistake this workstation's path for bundle provenance.
ABSOLUTE_TEXT_PREFIXES = tuple(
    "/" + part + "/" for part in ("Users", "Volumes", "home", "private", "var")
)
WINDOWS_ABSOLUTE_PREFIXES = (
    "C" + ":" + "\\",
    "D" + ":" + "\\",
    "C" + ":/",
    "D" + ":/",
)
FORBIDDEN_TEXT_MARKERS = ABSOLUTE_TEXT_PREFIXES + WINDOWS_ABSOLUTE_PREFIXES + (
    "file" + "://",
    "-----BEGIN " + "PRIVATE KEY-----",
    "-----BEGIN " + "OPENSSH PRIVATE KEY-----",
    "-----BEGIN " + "RSA PRIVATE KEY-----",
    "-----BEGIN " + "EC PRIVATE KEY-----",
)
FORBIDDEN_PATH_SEGMENTS = frozenset(
    {
        ".git",
        ".hg",
        ".svn",
        ".venv",
        "venv",
        "env",
        "node_modules",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        ".tox",
        "dist",
        "build",
        "target",
        "vendor",
        "deps",
        "dependencies",
        "cache",
        "caches",
        "tmp",
        "temp",
        "coverage",
    }
)


def _json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode(
        "utf-8"
    )


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _run_git(repo_root: Path, args: Sequence[str]) -> bytes:
    completed = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if completed.returncode != 0:
        rendered = " ".join(args[:3])
        raise RuntimeError(f"git command failed ({rendered}; exit {completed.returncode})")
    return completed.stdout


def _resolve_repo_root(explicit: str | None) -> Path:
    if explicit:
        candidate = Path(explicit).expanduser().resolve()
    else:
        candidate = Path(__file__).resolve().parents[2]
    top = _run_git(candidate, ["rev-parse", "--show-toplevel"]).decode("utf-8").strip()
    if not top:
        raise RuntimeError("could not resolve the Git repository root")
    return Path(top).resolve()


def _resolve_commit(repo_root: Path, requested: str) -> str:
    value = _run_git(
        repo_root,
        ["rev-parse", "--verify", "--end-of-options", f"{requested}^{{commit}}"],
    ).decode("ascii").strip()
    if len(value) != 40 or any(character not in "0123456789abcdef" for character in value):
        raise RuntimeError("Git did not return a full commit object name")
    return value


def _git_file_bytes(repo_root: Path, commit: str, relative: str) -> bytes:
    # Inspect the tree mode first so a committed symlink cannot be silently
    # copied as its link target or treated as a regular payload.
    listing = _run_git(repo_root, ["ls-tree", "-r", "--full-tree", commit, "--", relative])
    matching = [
        line for line in listing.decode("utf-8").splitlines() if line.endswith("\t" + relative)
    ]
    if len(matching) != 1:
        raise FileNotFoundError(f"selected Git payload is missing at {commit[:12]}: {relative}")
    object_metadata, listed_path = matching[0].split("\t", 1)
    mode, object_type, _object_id = object_metadata.split()
    if listed_path != relative:
        raise RuntimeError(f"Git tree path mismatch for selected payload: {relative}")
    if object_type != "blob" or mode.startswith("12"):
        raise RuntimeError(f"selected Git payload is not a regular file: {relative}")
    return _run_git(repo_root, ["show", f"{commit}:{relative}"])


def _path_is_safe(relative: str) -> bool:
    if not relative or "\x00" in relative or "\\" in relative:
        return False
    parsed = PurePosixPath(relative)
    if parsed.is_absolute() or any(part in {"", ".", ".."} for part in parsed.parts):
        return False
    if ":" in parsed.parts[0] or any(part.lower() in FORBIDDEN_PATH_SEGMENTS for part in parsed.parts):
        return False
    return parsed.as_posix() == relative


def _forbidden_marker(relative: str, data: bytes) -> str | None:
    # Decode only for path/secret markers.  The raw bytes remain byte-for-byte
    # unchanged in the bundle; ignoring undecodable binary bytes avoids
    # treating arbitrary compressed image data as prose.
    if PurePosixPath(relative).suffix.lower() not in TEXT_SUFFIXES:
        return None
    text = data.decode("utf-8", errors="ignore")
    lowered = text.lower()
    for marker in FORBIDDEN_TEXT_MARKERS:
        if marker.lower() in lowered:
            return marker
    return None


def _assert_payload_safe(relative: str, data: bytes) -> None:
    if not _path_is_safe(relative):
        raise RuntimeError(f"unsafe bundle path: {relative}")
    marker = _forbidden_marker(relative, data)
    if marker is not None:
        raise RuntimeError(f"source-machine or private-key marker in payload: {relative}")


def _write_bytes(root: Path, relative: str, data: bytes) -> None:
    _assert_payload_safe(relative, data)
    destination = root / Path(*PurePosixPath(relative).parts)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)


def _records(root: Path, *, include_manifest: bool = False) -> list[dict[str, object]]:
    paths: list[str] = []
    for path in root.rglob("*"):
        if path.is_symlink():
            raise RuntimeError(f"symlink in staging tree: {path.relative_to(root).as_posix()}")
        if path.is_file():
            relative = path.relative_to(root).as_posix()
            if not include_manifest and relative == MANIFEST_NAME:
                continue
            _assert_payload_safe(relative, path.read_bytes())
            paths.append(relative)
    records: list[dict[str, object]] = []
    for relative in sorted(paths):
        path = root / Path(*PurePosixPath(relative).parts)
        records.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": _sha256_file(path),
            }
        )
    return records


def _copyable_prompt(commit: str, branch: str) -> str:
    return f"""You are continuing a bounded, read-only Pattern Map v16 handoff in the Signal Foundry repository.

Context packet identity:
- Product name: Signal Foundry. Its own repository, schemas, records, permissions, and current owner instructions remain authoritative.
- Pattern Map source repository: {SOURCE_REPOSITORY}
- Pattern Map source branch: {branch}
- Pattern Map source commit: {commit}
- Draft review: {DRAFT_PR} (open/draft/unmerged; do not merge it)
- The audited Signal Foundry anchor is {SIGNAL_FOUNDRY_AUDITED_CHECKPOINT}; compare against it read-only and never reset the receiving checkout to it.

Before editing, read the nearest Signal Foundry AGENTS.md and inspect its own checkout, branch, remotes, worktrees, modified files, and untracked files. Preserve existing local work. Then read this packet's START_HERE.md and the two canonical handoff files under handoff/signal-foundry/.

Use the existing OPERATOR_DECISION plus RATIONALE pair as the first seam to inspect. Do not invent a Pattern Map classifier, a V14 deep link, “Sigma Foundry,” a second ledger, a universal score, or a new event type. CONTEXT_DISPOSITION is a conceptual completeness worksheet only; it is not valid against the current Signal Foundry decision-memory schema and must not be implemented from this packet.

This packet is context and review material, not mutation authority. Do not deploy, publish, merge, change production, call a provider or model, acquire an external dataset, spend, preregister, contact people, or run an empirical/participant study merely because this packet is present. If any referenced file, schema, route, or record is missing, STOP and request the exact missing file or current repository evidence; do not infer, recreate, or silently substitute it. If current Signal Foundry contracts conflict materially with this packet, report the exact conflict before changing anything.
"""


def _start_here(
    *,
    commit: str,
    branch: str,
    zip_name: str,
    source_records: Sequence[Mapping[str, object]],
    prompt: str,
) -> str:
    source_count = len(source_records)
    source_bytes = sum(int(record["bytes"]) for record in source_records)
    return f"""# Pattern Map v16 → Signal Foundry portable handoff

Status: **verified context bundle candidate; owner review only**

This directory is a self-contained, read-only context packet for a Codex task
working in the Signal Foundry repository on another computer. It is not a
checkout of either repository and it does not grant mutation authority.

## Read this first

1. Before extraction, place `{zip_name}` beside its
   `{zip_name}.sha256` sidecar and run
   `shasum -a 256 -c {zip_name}.sha256` (or `sha256sum -c` where available).
   Stop if the outer checksum fails.
2. Extract the ZIP into a new directory beside or outside the receiving Signal
   Foundry repository. Do not extract over that repository.
3. From this directory, run `python3 verify_bundle.py`. If Python is not
   available, run `shasum -a 256 -c SHA256SUMS.txt` and report the limitation.
4. Read the exact files in this order: `START_HERE.md`, `README.md`,
   `docs/OWNER_INTENT_V16.md`, `docs/THESIS_AND_AUDIENCE_CONTRACT_V16.md`,
   `docs/ARTIFACT_BOUNDARIES.md`,
   `handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md`,
   `handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md`,
   `manuscript/NINETY_SECOND_VERSION.md`, `framework/SIX_FAMILIES.md`,
   `framework/OPERATOR_PLAYBOOK.md`, `framework/agent-playbook/QUICKSTART.md`,
   `cases/signal-foundry/README.md`, and the Echo boundary records under
   `research/the-echo-problem/`.
5. Give the downstream task the copyable prompt below or the exact contents of
   `COPYABLE_PROMPT.md`.

## Exact Pattern Map provenance

```text
repository: {SOURCE_REPOSITORY}
branch:     {branch}
commit:     {commit}
review:     {DRAFT_PR}
state:      open / draft / unmerged; owner review and manual gates remain open
```

Payload files are read byte-for-byte from that Git commit. The generated
manifest records each selected file's path, byte count, and SHA-256. The
manifest deliberately excludes `BUNDLE_MANIFEST.json` itself because hashing a
manifest that contains its own hash is circular. `SHA256SUMS.txt` is included
in the manifest, but excludes itself and the manifest for the same reason. The
verifier checks this rule explicitly.

This bundle contains {source_count} committed source files ({source_bytes:,}
bytes), the repaired standalone HTML, the secondary six-page PDF companion,
and the historical v13 diagram required by the standalone's relative image
path. It is a selected handoff, not the complete repository, Git history,
dependency tree, v14 transfer, v15.2 archive, or Signal Foundry source.

## Downstream guardrails

- The product name is **Signal Foundry**. Signal Foundry's own repository is
  authoritative for current schemas, records, permissions, and implementation.
- Test the existing append-only `OPERATOR_DECISION` + `RATIONALE` seam first;
  do not create a duplicate universal receipt or event stream.
- `CONTEXT_DISPOSITION` is conceptual only and **not current-schema-valid**;
  the packet is not permission to implement it.
- No V14 deep link exists in this packet, and no Pattern Map classifier exists.
  Do not invent either one or substitute a hosted/public URL for the local
  artifacts.
- Missing files or materially changed contracts must be requested and
  reconciled, not inferred from summaries, screenshots, or this packet.
- This packet alone authorizes no app mutation, deployment, publication,
  merge, provider/model call, external dataset acquisition, spending,
  preregistration, outreach, or empirical/participant study.
- Pattern Map v16 is an operating philosophy and design proposal. Signal
  Foundry and the other case files are bounded illustrations, not validation.
  The Echo Problem remains a separate unrun research track with no results.

## Copyable downstream prompt

Copy only the fenced text below into the receiving Codex task after extracting
and verifying this directory:

```text
{prompt.rstrip()}
```

## Local review surfaces in this packet

- `site/exports/standalone/pattern-map-v16.html` is the direct-open semantic
  all-routes companion. Keep the extracted directory structure intact so the
  historical diagram resolves.
- `site/exports/pattern-map-v16-owner-review.pdf` is a secondary visual
  companion, not the accessibility or interactive source.
- The full local site can be rebuilt only from a full Pattern Map checkout;
  this packet intentionally does not contain dependencies or generated site
  output.

## Verification

```sh
python3 verify_bundle.py
shasum -a 256 -c SHA256SUMS.txt
```

The second command is an optional independent checksum check. Both commands
are provider-free and make no network calls.
"""


def _verifier_source() -> str:
    """Return the standalone verifier source embedded in every bundle."""

    # Keep this program self-contained: a receiving computer needs no package,
    # repository, network access, or builder source to verify an extraction.
    return r'''#!/usr/bin/env python3
"""Verify one extracted Pattern Map portable bundle using the stdlib only."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys


MANIFEST_NAME = "BUNDLE_MANIFEST.json"
CHECKSUMS_NAME = "SHA256SUMS.txt"
TEXT_SUFFIXES = frozenset({
    ".css", ".html", ".js", ".json", ".md", ".mjs", ".py", ".sh",
    ".txt", ".yaml", ".yml",
})
FORBIDDEN_PATH_SEGMENTS = frozenset({
    ".git", ".hg", ".svn", ".venv", "venv", "env", "node_modules",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".tox",
    "dist", "build", "target", "vendor", "deps", "dependencies", "cache",
    "caches", "tmp", "temp", "coverage",
})
ABSOLUTE_TEXT_PREFIXES = tuple("/" + part + "/" for part in (
    "Users", "Volumes", "home", "private", "var"
))
WINDOWS_ABSOLUTE_PREFIXES = (
    "C" + ":" + "\\", "D" + ":" + "\\", "C" + ":/", "D" + ":/"
)
FORBIDDEN_TEXT_MARKERS = ABSOLUTE_TEXT_PREFIXES + WINDOWS_ABSOLUTE_PREFIXES + (
    "file" + "://",
    "-----BEGIN " + "PRIVATE KEY-----",
    "-----BEGIN " + "OPENSSH PRIVATE KEY-----",
    "-----BEGIN " + "RSA PRIVATE KEY-----",
    "-----BEGIN " + "EC PRIVATE KEY-----",
)
SHA_LINE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$")


def fail(message: str) -> "NoReturn":
    raise SystemExit("FAIL portable bundle: " + message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_relative(value: object) -> str:
    if not isinstance(value, str) or not value or "\x00" in value or "\\" in value:
        fail("manifest contains a non-portable path")
    parsed = PurePosixPath(value)
    if parsed.is_absolute() or any(part in {"", ".", ".."} for part in parsed.parts):
        fail("manifest contains an unsafe path: " + value)
    if ":" in parsed.parts[0] or any(part.lower() in FORBIDDEN_PATH_SEGMENTS for part in parsed.parts):
        fail("manifest contains a forbidden path: " + value)
    if parsed.as_posix() != value:
        fail("manifest path is not normalized: " + value)
    return value


def text_marker(relative: str, data: bytes) -> str | None:
    if PurePosixPath(relative).suffix.lower() not in TEXT_SUFFIXES:
        return None
    text = data.decode("utf-8", errors="ignore").lower()
    for marker in FORBIDDEN_TEXT_MARKERS:
        if marker.lower() in text:
            return marker
    return None


def all_files(root: Path) -> set[str]:
    found: set[str] = set()
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            fail("symlink found: " + relative)
        if path.is_file():
            found.add(safe_relative(relative))
    return found


def main() -> int:
    root = Path(__file__).resolve().parent
    manifest_path = root / MANIFEST_NAME
    metadata_path = root / "BUNDLE_METADATA.json"
    checksums_path = root / CHECKSUMS_NAME
    if not manifest_path.is_file() or not metadata_path.is_file() or not checksums_path.is_file():
        fail("BUNDLE_MANIFEST.json, BUNDLE_METADATA.json, and SHA256SUMS.txt are required")

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        fail("invalid control JSON: " + type(error).__name__)
    if manifest.get("schema_version") != 1:
        fail("unsupported manifest schema")
    if metadata.get("schema_version") != 1:
        fail("unsupported metadata schema")
    if manifest.get("manifest_self_exclusion") != (
        "BUNDLE_MANIFEST.json is excluded from its own files list because self-hashing is circular."
    ):
        fail("manifest self-exclusion contract is missing")
    records = manifest.get("files")
    if not isinstance(records, list):
        fail("manifest files must be a list")
    normalized: list[dict[str, object]] = []
    for record in records:
        if not isinstance(record, dict):
            fail("manifest record is not an object")
        path = safe_relative(record.get("path"))
        size = record.get("bytes")
        digest = record.get("sha256")
        if not isinstance(size, int) or size < 0 or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            fail("invalid manifest record for " + path)
        normalized.append({"path": path, "bytes": size, "sha256": digest})
    if normalized != sorted(normalized, key=lambda item: str(item["path"])):
        fail("manifest records are not sorted")
    paths = [str(record["path"]) for record in normalized]
    if len(paths) != len(set(paths)):
        fail("manifest contains duplicate paths")
    if MANIFEST_NAME in paths:
        fail("manifest self-exclusion is violated")
    if CHECKSUMS_NAME not in paths:
        fail("SHA256SUMS.txt is not covered by the manifest")
    expected_files = set(paths) | {MANIFEST_NAME}
    actual_files = all_files(root)
    if actual_files != expected_files:
        missing = sorted(expected_files - actual_files)
        extra = sorted(actual_files - expected_files)
        fail("file set mismatch; missing=" + repr(missing) + " extra=" + repr(extra))

    for record in normalized:
        path = root / Path(*PurePosixPath(str(record["path"])).parts)
        data = path.read_bytes()
        marker = text_marker(str(record["path"]), data)
        if marker is not None:
            fail("source-machine or private-key marker in " + str(record["path"]))
        if path.stat().st_size != int(record["bytes"]):
            fail("byte count mismatch: " + str(record["path"]))
        if sha256(path) != str(record["sha256"]):
            fail("SHA-256 mismatch: " + str(record["path"]))

    checksum_lines = checksums_path.read_text(encoding="utf-8").splitlines()
    if any(not line or line.endswith(" ") for line in checksum_lines):
        fail("malformed SHA256SUMS.txt line")
    checksums: dict[str, str] = {}
    for line in checksum_lines:
        match = SHA_LINE.fullmatch(line)
        if match is None:
            fail("malformed SHA256SUMS.txt entry")
        digest, path_value = match.groups()
        path_value = safe_relative(path_value)
        if path_value in checksums:
            fail("duplicate checksum path: " + path_value)
        checksums[path_value] = digest
    checksum_expected = set(paths) - {CHECKSUMS_NAME}
    if set(checksums) != checksum_expected:
        fail("SHA256SUMS.txt set differs from manifest (manifest and checksum file are excluded)")
    for path_value, digest in checksums.items():
        if sha256(root / Path(*PurePosixPath(path_value).parts)) != digest:
            fail("checksum mismatch: " + path_value)

    if metadata.get("source_commit") != manifest.get("source_commit"):
        fail("metadata and manifest source commits differ")
    if not isinstance(metadata.get("source_commit"), str) or not re.fullmatch(r"[0-9a-f]{40}", metadata["source_commit"]):
        fail("metadata does not record a full source commit")
    if manifest.get("file_count") != len(normalized):
        fail("manifest file_count mismatch")
    if manifest.get("total_bytes") != sum(int(record["bytes"]) for record in normalized):
        fail("manifest total_bytes mismatch")
    print(f"PASS portable bundle: {len(normalized)} files / {sum(int(record['bytes']) for record in normalized)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''


def _manifest_payload(records: Sequence[Mapping[str, object]], commit: str, branch: str) -> dict[str, object]:
    total_bytes = sum(int(record["bytes"]) for record in records)
    return {
        "schema_version": 1,
        "package": PACKAGE_NAME,
        "source_repository": SOURCE_REPOSITORY,
        "source_branch": branch,
        "source_commit": commit,
        "manifest_self_exclusion": (
            "BUNDLE_MANIFEST.json is excluded from its own files list because self-hashing is circular."
        ),
        "checksum_self_exclusion": (
            "SHA256SUMS.txt excludes itself and BUNDLE_MANIFEST.json; all other manifest files are checked."
        ),
        "file_count": len(records),
        "total_bytes": total_bytes,
        "files": list(records),
    }


def _metadata_payload(
    *, commit: str, branch: str, date: str, source_records: Sequence[Mapping[str, object]]
) -> dict[str, object]:
    return {
        "schema_version": 1,
        "package": PACKAGE_NAME,
        "status": "owner-review context bundle; not a patch, deployment, publication, merge, or research result",
        "generated_date": date,
        "source_repository": SOURCE_REPOSITORY,
        "source_branch": branch,
        "source_commit": commit,
        "source_commit_short": commit[:7],
        "draft_review": DRAFT_PR,
        "signal_foundry_audited_checkpoint": SIGNAL_FOUNDRY_AUDITED_CHECKPOINT,
        "previous_bundle": {
            "filename": PREVIOUS_BUNDLE_NAME,
            "sha256": PREVIOUS_BUNDLE_SHA256,
            "status": "retained; superseded by this final-head bundle; never delete as part of this build",
        },
        "provenance": (
            "Selected payloads were read byte-for-byte from the named Git commit. "
            "Generated control files describe and verify that selected snapshot; "
            "the bundle does not include a source-machine path."
        ),
        "scope": (
            "Selected human thesis, framework, operator and agent playbook, bounded cases, "
            "handoff records, research-separation boundaries, standalone HTML, PDF companion, "
            "and historical v13 image. No dependencies, caches, generated site directory, "
            "complete archive, or Signal Foundry source."
        ),
        "selected_source_paths": [str(record["path"]) for record in source_records],
        "boundary": {
            "signal_foundry_name": "Signal Foundry",
            "signal_foundry_repository_is_authoritative": True,
            "first_seam": "OPERATOR_DECISION + RATIONALE",
            "context_disposition": "conceptual only; not valid against current Signal Foundry schema",
            "pattern_map_classifier": "does not exist",
            "v14_deep_link": "does not exist",
            "packet_mutation_authority": False,
            "echo_problem": "separate unrun research track; no results",
        },
    }


def _checksum_text(root: Path, records: Sequence[Mapping[str, object]]) -> bytes:
    # The checksum file is deliberately excluded from its own checksum set,
    # as is the manifest.  Its hash is nevertheless covered by the manifest.
    lines = []
    for record in records:
        relative = str(record["path"])
        if relative in {CHECKSUMS_NAME, MANIFEST_NAME}:
            continue
        path = root / Path(*PurePosixPath(relative).parts)
        lines.append(f"{_sha256_file(path)}  {relative}")
    return ("\n".join(lines) + "\n").encode("utf-8")


def _zip_info(name: str, *, directory: bool = False) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.create_system = 3
    info.create_version = 20
    info.extract_version = 20
    info.flag_bits = 0
    info.compress_type = zipfile.ZIP_STORED
    info.external_attr = ((0o40755 if directory else 0o100644) << 16) | (0x10 if directory else 0)
    return info


def _write_zip(stage: Path, destination: Path, root_name: str) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise FileExistsError(f"refusing to overwrite existing ZIP: {destination.name}")
    with zipfile.ZipFile(destination, mode="x", compression=zipfile.ZIP_STORED, allowZip64=True) as archive:
        archive.writestr(_zip_info(root_name + "/", directory=True), b"")
        files = sorted(path for path in stage.rglob("*") if path.is_file())
        for path in files:
            relative = path.relative_to(stage).as_posix()
            _assert_payload_safe(relative, path.read_bytes())
            archive.writestr(_zip_info(root_name + "/" + relative), path.read_bytes())


def _parse_date(value: str) -> str:
    try:
        _datetime.date.fromisoformat(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("date must be YYYY-MM-DD") from error
    return value


def build_bundle(
    *, repo_root: Path, requested_commit: str, output_dir: Path, date: str
) -> tuple[Path, Path, dict[str, object]]:
    commit = _resolve_commit(repo_root, requested_commit)
    # This packet is the portable handoff for the canonical pushed branch even
    # when it is built from an isolated finalization worktree.
    branch = SOURCE_BRANCH_HINT
    output_dir = output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    short = commit[:7]
    zip_name = f"{PACKAGE_PREFIX}_{date}_{short}.zip"
    zip_path = output_dir / zip_name
    sidecar_path = output_dir / (zip_name + ".sha256")
    if zip_path.exists() or sidecar_path.exists():
        raise FileExistsError(f"refusing to overwrite existing final artifact: {zip_name}")

    with tempfile.TemporaryDirectory(prefix="pattern-map-portable-") as temporary:
        stage = Path(temporary)
        source_records: list[dict[str, object]] = []
        seen: set[str] = set()
        for relative in SOURCE_PATHS:
            if relative in seen:
                raise RuntimeError(f"duplicate selected source path: {relative}")
            seen.add(relative)
            data = _git_file_bytes(repo_root, commit, relative)
            _write_bytes(stage, relative, data)
            source_records.append(
                {
                    "path": relative,
                    "bytes": len(data),
                    "sha256": _sha256_bytes(data),
                }
            )

        prompt = _copyable_prompt(commit, branch)
        _write_bytes(stage, "START_HERE.md", _start_here(
            commit=commit,
            branch=branch,
            zip_name=zip_name,
            source_records=source_records,
            prompt=prompt,
        ).encode("utf-8"))
        _write_bytes(stage, "COPYABLE_PROMPT.md", prompt.encode("utf-8"))
        _write_bytes(stage, "verify_bundle.py", _verifier_source().encode("utf-8"))
        metadata = _metadata_payload(
            commit=commit,
            branch=branch,
            date=date,
            source_records=source_records,
        )
        _write_bytes(stage, "BUNDLE_METADATA.json", _json_bytes(metadata))

        # Write checksums before the manifest.  The manifest covers the
        # checksum file; the checksum file excludes itself and the manifest,
        # which avoids a circular hash dependency.
        pre_manifest_records = _records(stage)
        _write_bytes(stage, CHECKSUMS_NAME, _checksum_text(stage, pre_manifest_records))
        manifest_records = _records(stage)
        manifest = _manifest_payload(manifest_records, commit, branch)
        _write_bytes(stage, MANIFEST_NAME, _json_bytes(manifest))

        # Exercise exactly the verifier that travels with the ZIP before any
        # outer artifact is written.
        verification = subprocess.run(
            [sys.executable, str(stage / "verify_bundle.py")],
            cwd=stage,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
        if verification.returncode != 0:
            raise RuntimeError("generated verifier failed before ZIP creation: " + verification.stdout.strip())

        _write_zip(stage, zip_path, zip_path.stem)
        zip_digest = _sha256_file(zip_path)
        archive_records = _records(stage, include_manifest=True)
        try:
            with sidecar_path.open("x", encoding="utf-8") as handle:
                handle.write(f"{zip_digest}  {zip_path.name}\n")
        except FileExistsError as error:
            raise FileExistsError(
                f"refusing to overwrite existing ZIP sidecar: {sidecar_path.name}"
            ) from error
        summary: dict[str, object] = {
            "zip_name": zip_path.name,
            "sidecar_name": sidecar_path.name,
            "source_commit": commit,
            "source_branch": branch,
            "file_count": len(manifest_records),
            "total_bytes": int(manifest["total_bytes"]),
            "archive_file_count": len(archive_records),
            "archive_total_bytes": sum(
                int(record["bytes"]) for record in archive_records
            ),
            "zip_bytes": zip_path.stat().st_size,
            "zip_sha256": zip_digest,
        }
        return zip_path, sidecar_path, summary


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        help="Pattern Map repository root (defaults to the repository containing this script)",
    )
    parser.add_argument(
        "--commit",
        default="HEAD",
        help="Git commit whose bytes are packaged (default: HEAD)",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Directory for the new ZIP and adjacent .zip.sha256 sidecar",
    )
    parser.add_argument(
        "--date",
        default=_datetime.date.today().isoformat(),
        type=_parse_date,
        help="Filename date in YYYY-MM-DD form (default: today)",
    )
    args = parser.parse_args(argv)
    try:
        repo_root = _resolve_repo_root(args.repo_root)
        zip_path, sidecar_path, summary = build_bundle(
            repo_root=repo_root,
            requested_commit=args.commit,
            output_dir=Path(args.output_dir),
            date=args.date,
        )
    except (FileExistsError, FileNotFoundError, OSError, RuntimeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    # Print names and integrity values, not machine-specific output paths.
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
