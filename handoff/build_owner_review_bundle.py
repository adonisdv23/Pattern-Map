#!/usr/bin/env python3
"""Build a deterministic, complete, exact-commit Pattern Map owner bundle.

The builder is an authoring tool.  It requires a named non-default branch,
refuses dirty or non-HEAD inputs, reads every payload byte from Git rather than
the working tree, creates one enclosing directory, runs the verifier that
travels with the bundle, and writes a ZIP plus an external SHA-256 sidecar.  It
does not publish, release, deploy, merge, or authenticate the owner of the bytes.
"""

from __future__ import annotations

import argparse
import datetime as _datetime
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
import unicodedata
import zipfile
from pathlib import Path, PurePosixPath
from typing import Sequence


PACKAGE_NAME = "pattern-map-v16-owner-review"
OWNER_INTENT_SHA256 = "3aea5eeb19302a0e6498f7bcfccb23535953dbb6807fb5a486e0279bfa72543b"
PACKAGE_STATUS = (
    "private owner-review candidate; not merged, deployed, published, released, "
    "or empirically validated"
)
DEFAULT_BRANCH_NAMES = {"main", "master", "trunk"}
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
CONTROL_SOURCE_PATHS = {
    "START_HERE.md": "handoff/START_HERE_OWNER_REVIEW.md",
    "VERIFY_PACKAGE.py": "handoff/verify_extracted_owner_bundle.py",
}
REQUIRED_REPOSITORY_PATHS = {
    *CONTROL_SOURCE_PATHS.values(),
    "docs/OWNER_INTENT_V16.md",
    "docs/OWNER_INTENT_V16.sha256",
    "handoff/OWNER_REVIEW_MANIFEST_V16.json",
    "handoff/verify_owner_review_package.py",
}
PRIVATE_KEY_MARKERS = (
    ("-----BEGIN " + "PRIVATE KEY-----").encode("ascii"),
    ("-----BEGIN " + "OPENSSH PRIVATE KEY-----").encode("ascii"),
    ("-----BEGIN " + "RSA PRIVATE KEY-----").encode("ascii"),
    ("-----BEGIN " + "EC PRIVATE KEY-----").encode("ascii"),
)
KNOWN_PRIVATE_KEY_MARKER_FIXTURES = {
    # This immutable test source intentionally contains literal hostile marker
    # fixtures. Any path or byte drift removes the exception.
    "qa/handoff/test_portable_bundle.py": (
        "7871504bf6d0fbb592a5193b0d8af7d5c0eccd4c3a0f50833cc817250bff2aa2"
    ),
}
FORBIDDEN_ACTIVE_SEGMENTS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    "dist",
    "build",
    "target",
    "coverage",
    "tmp",
    "temp",
}
FORBIDDEN_SECRET_NAMES = {
    ".env",
    ".netrc",
    ".pypirc",
    "id_rsa",
    "id_ed25519",
    "credentials.json",
    "cookies.sqlite",
    "cookies",
    "auth.db",
    "login.keychain-db",
}
FORBIDDEN_SECRET_SEGMENTS = {".aws", ".ssh", ".gnupg", ".azure", "keychains"}
WINDOWS_FORBIDDEN_CHARACTERS = set('<>:"|?*')
WINDOWS_RESERVED_BASENAMES = {
    "con",
    "prn",
    "aux",
    "nul",
    *(f"com{index}" for index in range(1, 10)),
    *(f"lpt{index}" for index in range(1, 10)),
}


class BuildError(RuntimeError):
    """A stable author-facing bundle construction error."""


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode(
        "utf-8"
    )


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def trusted_adjacent_regular_bytes(name: str) -> bytes:
    """Read one non-symlink control beside this builder from a stable inode."""

    path = Path(__file__).resolve().with_name(name)
    try:
        before = path.lstat()
    except OSError as error:
        raise BuildError(f"trusted adjacent control is unavailable: {name}") from error
    if not stat.S_ISREG(before.st_mode):
        raise BuildError(f"trusted adjacent control is not a regular file: {name}")
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as error:
        raise BuildError(f"cannot open trusted adjacent control safely: {name}") from error
    try:
        opened = os.fstat(descriptor)
        if (
            opened.st_dev != before.st_dev
            or opened.st_ino != before.st_ino
            or not stat.S_ISREG(opened.st_mode)
        ):
            raise BuildError(f"trusted adjacent control changed before read: {name}")
        with os.fdopen(descriptor, "rb") as handle:
            descriptor = -1
            data = handle.read()
        after = path.lstat()
        if after.st_dev != opened.st_dev or after.st_ino != opened.st_ino:
            raise BuildError(f"trusted adjacent control changed during read: {name}")
        return data
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_git(repo_root: Path, args: Sequence[str], *, text: bool = False) -> bytes | str:
    completed = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=text,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip() if text else completed.stderr.decode("utf-8", "replace").strip()
        raise BuildError(f"git {' '.join(args[:3])} failed: {detail or completed.returncode}")
    return completed.stdout


def resolve_repo_root(explicit: str | None) -> Path:
    candidate = Path(explicit).expanduser().resolve() if explicit else Path(__file__).resolve().parents[1]
    top = str(run_git(candidate, ["rev-parse", "--show-toplevel"], text=True)).strip()
    if not top:
        raise BuildError("could not resolve the Pattern Map Git root")
    return Path(top).resolve()


def resolve_exact_clean_head(
    repo_root: Path, requested_commit: str, *, require_upstream: bool
) -> tuple[str, str]:
    head = str(run_git(repo_root, ["rev-parse", "--verify", "HEAD^{commit}"], text=True)).strip()
    commit = str(
        run_git(repo_root, ["rev-parse", "--verify", f"{requested_commit}^{{commit}}"], text=True)
    ).strip()
    if commit != head:
        raise BuildError("owner bundle must package the exact current HEAD, not a different commit")
    dirty = str(run_git(repo_root, ["status", "--porcelain=v1", "--untracked-files=all"], text=True))
    if dirty.strip():
        raise BuildError("owner bundle requires a clean Git checkout; commit intended bytes first")
    branch_probe = subprocess.run(
        ["git", "symbolic-ref", "--quiet", "--short", "HEAD"],
        cwd=repo_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        check=False,
    )
    if branch_probe.returncode != 0 or not branch_probe.stdout.strip():
        raise BuildError(
            "owner bundle authoring requires a named non-default branch; "
            "detached HEAD is not allowed"
        )
    source_ref = branch_probe.stdout.strip()
    if source_ref.casefold() in DEFAULT_BRANCH_NAMES:
        raise BuildError(
            "owner bundle authoring requires a named non-default branch, not "
            f"{source_ref!r}"
        )
    if require_upstream:
        upstream = str(run_git(repo_root, ["rev-parse", "--verify", "@{upstream}^{commit}"], text=True)).strip()
        if upstream != commit:
            raise BuildError(
                "--require-upstream requested, but the current branch/upstream tips differ; "
                "push and read back the exact branch before sealing"
            )
    return commit, source_ref


def parse_tree(repo_root: Path, commit: str) -> list[tuple[str, str, str]]:
    raw = run_git(repo_root, ["ls-tree", "-rz", "--full-tree", commit])
    assert isinstance(raw, bytes)
    records: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    seen_casefold: dict[str, str] = {}
    for entry in raw.split(b"\0"):
        if not entry:
            continue
        try:
            metadata, encoded_path = entry.split(b"\t", 1)
            mode, object_type, object_id = metadata.decode("ascii").split()
            relative = encoded_path.decode("utf-8")
        except (ValueError, UnicodeError) as error:
            raise BuildError("could not parse an exact Git tree entry") from error
        if object_type != "blob" or mode not in {"100644", "100755"}:
            raise BuildError(f"owner bundle permits regular Git files only: {relative} ({mode} {object_type})")
        safe_repository_path(relative)
        if relative in seen:
            raise BuildError(f"duplicate Git payload path: {relative}")
        folded = portable_path_key(relative)
        if folded in seen_casefold:
            raise BuildError(
                "case-colliding Git payload paths are not portable: "
                f"{seen_casefold[folded]} and {relative}"
            )
        seen.add(relative)
        seen_casefold[folded] = relative
        records.append((relative, mode, object_id))
    records.sort(key=lambda item: item[0])
    if not records:
        raise BuildError("exact Git tree contains no regular-file payload")
    return records


def safe_portable_path(relative: str) -> None:
    """Reject path shapes that are unsafe or non-portable in any package scope."""

    if not relative or "\\" in relative:
        raise BuildError(f"unsafe/non-portable Git path: {relative!r}")
    parsed = PurePosixPath(relative)
    if parsed.is_absolute() or any(part in {"", ".", ".."} for part in parsed.parts):
        raise BuildError(f"unsafe Git path: {relative!r}")
    if relative != parsed.as_posix():
        raise BuildError(f"non-portable Git path: {relative!r}")
    for part in parsed.parts:
        if any(ord(character) < 32 or ord(character) == 127 for character in part):
            raise BuildError(f"control character in Git path: {relative!r}")
        if any(character in WINDOWS_FORBIDDEN_CHARACTERS for character in part):
            raise BuildError(f"cross-platform-forbidden character in Git path: {relative!r}")
        if part.endswith((" ", ".")):
            raise BuildError(f"trailing dot/space in Git path: {relative!r}")
        basename = part.split(".", 1)[0].casefold()
        if basename in WINDOWS_RESERVED_BASENAMES:
            raise BuildError(f"reserved cross-platform Git path: {relative!r}")


def safe_repository_path(relative: str) -> None:
    """Apply portable-path rules plus active-repository hygiene policy."""

    safe_portable_path(relative)
    parsed = PurePosixPath(relative)
    lower_parts = tuple(part.lower() for part in parsed.parts)
    in_archive = lower_parts[0] == "archive"
    if not in_archive and any(part in FORBIDDEN_ACTIVE_SEGMENTS for part in lower_parts):
        raise BuildError(f"active dependency/cache/generated-build path is forbidden: {relative}")
    if any(part in FORBIDDEN_SECRET_SEGMENTS for part in lower_parts):
        raise BuildError(f"credential/keychain directory is forbidden: {relative}")
    name = lower_parts[-1]
    if name in FORBIDDEN_SECRET_NAMES or name.startswith(".env."):
        raise BuildError(f"secret-bearing path name is forbidden: {relative}")
    if name.endswith((".pem", ".key", ".p12", ".pfx")):
        raise BuildError(f"private-key/certificate-container path is forbidden: {relative}")


def portable_path_key(relative: str) -> str:
    """Return the case- and Unicode-normalized collision key for one safe path."""

    safe_portable_path(relative)
    return unicodedata.normalize("NFC", relative).casefold()


def git_blob(repo_root: Path, object_id: str) -> bytes:
    return git_blobs(repo_root, [object_id])[object_id]


def git_blobs(repo_root: Path, object_ids: Sequence[str]) -> dict[str, bytes]:
    """Read exact Git blobs in one binary-safe cat-file batch."""

    unique_ids = list(dict.fromkeys(object_ids))
    completed = subprocess.run(
        ["git", "cat-file", "--batch"],
        cwd=repo_root,
        input=("\n".join(unique_ids) + "\n").encode("ascii"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.decode("utf-8", "replace").strip()
        raise BuildError(f"git cat-file --batch failed: {detail or completed.returncode}")
    output = completed.stdout
    cursor = 0
    blobs: dict[str, bytes] = {}
    for requested in unique_ids:
        header_end = output.find(b"\n", cursor)
        if header_end < 0:
            raise BuildError("truncated git cat-file batch header")
        try:
            returned, object_type, raw_size = output[cursor:header_end].decode("ascii").split()
            size = int(raw_size)
        except (UnicodeError, ValueError) as error:
            raise BuildError("invalid git cat-file batch header") from error
        if returned != requested or object_type != "blob" or size < 0:
            raise BuildError(f"unexpected git cat-file batch object for {requested}")
        data_start = header_end + 1
        data_end = data_start + size
        if data_end >= len(output) or output[data_end:data_end + 1] != b"\n":
            raise BuildError(f"truncated git cat-file batch payload for {requested}")
        blobs[requested] = output[data_start:data_end]
        cursor = data_end + 1
    if cursor != len(output):
        raise BuildError("unexpected trailing bytes from git cat-file batch")
    return blobs


def assert_payload_bytes_safe(relative: str, data: bytes) -> None:
    if not any(marker in data for marker in PRIVATE_KEY_MARKERS):
        return
    expected_fixture_digest = KNOWN_PRIVATE_KEY_MARKER_FIXTURES.get(relative)
    if expected_fixture_digest and sha256_bytes(data) == expected_fixture_digest:
        return
    raise BuildError(f"private-key marker found in Git payload: {relative}")


def write_regular(path: Path, data: bytes, mode: str = "100644") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() or path.is_symlink():
        raise BuildError(f"refusing to overwrite staged path: {path}")
    path.write_bytes(data)
    path.chmod(0o755 if mode == "100755" else 0o644)


def record(path: str, mode: str, data: bytes) -> dict[str, object]:
    return {"path": path, "mode": mode, "bytes": len(data), "sha256": sha256_bytes(data)}


def metadata_payload(
    *, commit: str, generated_date: str, root_directory: str
) -> dict[str, object]:
    return {
        "schema_version": 1,
        "package": PACKAGE_NAME,
        "status": PACKAGE_STATUS,
        "generated_date": generated_date,
        "source_commit": commit,
        "source_short_commit": commit[:12],
        "owner_intent_sha256": OWNER_INTENT_SHA256,
        "root_directory": root_directory,
        "payload_scope": PAYLOAD_SCOPE,
        "verification_scope": VERIFICATION_SCOPE,
        "bounded_manifest_path": "repository/handoff/OWNER_REVIEW_MANIFEST_V16.json",
        "external_sidecar_required": True,
        "manual_gates": MANUAL_GATES,
        "prohibited_actions": PROHIBITED_ACTIONS,
    }


def zip_info(
    name: str, *, directory: bool = False, executable: bool = False
) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.create_system = 3
    info.create_version = 20
    info.extract_version = 20
    info.flag_bits = 0
    info.compress_type = zipfile.ZIP_STORED
    file_mode = 0o100755 if executable else 0o100644
    info.external_attr = ((0o40755 if directory else file_mode) << 16) | (
        0x10 if directory else 0
    )
    return info


def staged_files(stage_root: Path) -> list[Path]:
    files: list[Path] = []
    for candidate in stage_root.rglob("*"):
        if candidate.is_symlink():
            raise BuildError(f"staged owner bundle contains a symlink: {candidate}")
        if candidate.is_file():
            files.append(candidate)
        elif not candidate.is_dir():
            raise BuildError(f"staged owner bundle contains a non-regular path: {candidate}")
    return sorted(files, key=lambda path: path.relative_to(stage_root).as_posix())


def write_zip(stage_root: Path, temporary_zip: Path, root_name: str) -> None:
    files = staged_files(stage_root)
    directories: set[str] = {root_name + "/"}
    for path in files:
        relative = path.relative_to(stage_root).as_posix()
        parent = PurePosixPath(root_name) / PurePosixPath(relative).parent
        while parent.as_posix() not in {".", root_name}:
            directories.add(parent.as_posix().rstrip("/") + "/")
            parent = parent.parent
    directories.add(root_name + "/repository/")
    with zipfile.ZipFile(
        temporary_zip, mode="x", compression=zipfile.ZIP_STORED, allowZip64=True
    ) as archive:
        for directory in sorted(directories):
            archive.writestr(zip_info(directory, directory=True), b"")
        for path in files:
            relative = path.relative_to(stage_root).as_posix()
            executable = bool(path.stat().st_mode & stat.S_IXUSR)
            archive.writestr(
                zip_info(f"{root_name}/{relative}", executable=executable),
                path.read_bytes(),
            )


def assert_zip_safe(zip_path: Path, *, root_name: str) -> None:
    with zipfile.ZipFile(zip_path) as archive:
        names: set[str] = set()
        portable_names: dict[str, str] = {}
        for item in archive.infolist():
            name = item.filename
            if name in names:
                raise BuildError(f"generated ZIP contains duplicate path: {name}")
            names.add(name)
            if "\\" in name or not name.startswith(root_name + "/"):
                raise BuildError(f"generated ZIP path escapes enclosing directory: {name}")
            parsed = PurePosixPath(name)
            if parsed.is_absolute() or ".." in parsed.parts or ":" in parsed.parts[0]:
                raise BuildError(f"generated ZIP contains unsafe path: {name}")
            member_path = name.rstrip("/")
            folded = portable_path_key(member_path)
            if folded in portable_names:
                raise BuildError(
                    "generated ZIP contains case/Unicode-colliding paths: "
                    f"{portable_names[folded]} and {name}"
                )
            portable_names[folded] = name
            unix_mode = (item.external_attr >> 16) & 0o170000
            expected_type = stat.S_IFDIR if item.is_dir() else stat.S_IFREG
            if unix_mode != expected_type:
                raise BuildError(f"generated ZIP contains a non-regular/non-directory path: {name}")
        bad_member = archive.testzip()
        if bad_member:
            raise BuildError(f"generated ZIP CRC failure: {bad_member}")


def verify_copied_extraction(zip_path: Path, *, root_name: str) -> str:
    with tempfile.TemporaryDirectory(prefix="pattern-map-owner-copy-") as temporary:
        destination = Path(temporary)
        with zipfile.ZipFile(zip_path) as archive:
            archive.extractall(destination)
        extracted_root = destination / root_name
        completed = subprocess.run(
            [sys.executable, str(extracted_root / "VERIFY_PACKAGE.py")],
            cwd=extracted_root,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
        if completed.returncode != 0:
            raise BuildError("copied-location extracted verifier failed: " + completed.stdout.strip())
        return completed.stdout.strip()


def parse_date(value: str) -> str:
    try:
        parsed = _datetime.date.fromisoformat(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("date must be YYYY-MM-DD") from error
    if parsed.isoformat() != value:
        raise argparse.ArgumentTypeError("date must be canonical YYYY-MM-DD")
    return value


def ensure_output_outside_repo(output_dir: Path, repo_root: Path) -> None:
    try:
        output_dir.resolve().relative_to(repo_root.resolve())
    except ValueError:
        return
    raise BuildError("owner bundle output directory must be outside the source repository")


def create_exclusive_marker(path: Path, content: str) -> os.stat_result:
    """Create one invocation-owned marker without following or replacing a path."""

    try:
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError as error:
        raise BuildError(f"owner-bundle output reservation already exists: {path.name}") from error
    created_stat = os.fstat(descriptor)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(content)
    except Exception:
        unlink_if_same(path, created_stat)
        raise
    return created_stat


def unlink_if_same(path: Path, expected: os.stat_result | None) -> None:
    """Remove only the exact inode positively created by this invocation."""

    if expected is None:
        return
    try:
        observed = path.lstat()
    except FileNotFoundError:
        return
    if same_inode(observed, expected):
        path.unlink()


def same_inode(first: os.stat_result, second: os.stat_result) -> bool:
    return first.st_dev == second.st_dev and first.st_ino == second.st_ino


def assert_same_regular_file(path: Path, expected: os.stat_result) -> None:
    try:
        observed = path.lstat()
    except FileNotFoundError as error:
        raise BuildError(f"invocation-owned temporary disappeared: {path.name}") from error
    if not same_inode(observed, expected) or not stat.S_ISREG(observed.st_mode):
        raise BuildError(f"invocation-owned temporary changed during build: {path.name}")


def open_same_regular_file(path: Path, expected: os.stat_result) -> int:
    """Open the expected regular inode without following a replacement symlink."""

    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as error:
        raise BuildError(f"invocation-owned file cannot be opened safely: {path.name}") from error
    observed = os.fstat(descriptor)
    if not same_inode(observed, expected) or not stat.S_ISREG(observed.st_mode):
        os.close(descriptor)
        raise BuildError(f"invocation-owned file changed before read: {path.name}")
    return descriptor


def sha256_same_regular_file(path: Path, expected: os.stat_result) -> str:
    descriptor = open_same_regular_file(path, expected)
    digest = hashlib.sha256()
    with os.fdopen(descriptor, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    assert_same_regular_file(path, expected)
    return digest.hexdigest()


def bytes_same_regular_file(path: Path, expected: os.stat_result) -> bytes:
    descriptor = open_same_regular_file(path, expected)
    with os.fdopen(descriptor, "rb") as handle:
        data = handle.read()
    assert_same_regular_file(path, expected)
    return data


def publish_exclusive(
    source: Path, destination: Path, source_stat: os.stat_result
) -> os.stat_result:
    """Atomically publish one built file without overwriting an existing target."""

    assert_same_regular_file(source, source_stat)
    try:
        os.link(source, destination, follow_symlinks=False)
    except FileExistsError as error:
        raise BuildError(
            f"refusing output race/overwrite; target appeared during build: {destination.name}"
        ) from error
    except OSError as error:
        raise BuildError(f"could not publish owner artifact {destination.name}: {error}") from error
    published = destination.lstat()
    if not same_inode(published, source_stat) or not stat.S_ISREG(published.st_mode):
        raise BuildError(
            f"published owner artifact did not bind the expected inode: {destination.name}"
        )
    return published


def build_bundle(
    *,
    repo_root: Path,
    requested_commit: str,
    output_dir: Path,
    generated_date: str,
    require_upstream: bool,
) -> tuple[Path, Path, dict[str, object]]:
    try:
        parsed_generated_date = _datetime.date.fromisoformat(generated_date)
    except (TypeError, ValueError) as error:
        raise BuildError("owner bundle date must be a valid YYYY-MM-DD calendar date") from error
    if parsed_generated_date.isoformat() != generated_date:
        raise BuildError("owner bundle date must be canonical YYYY-MM-DD")
    commit, source_ref = resolve_exact_clean_head(
        repo_root, requested_commit, require_upstream=require_upstream
    )
    tree = parse_tree(repo_root, commit)
    output_dir = output_dir.expanduser().resolve()
    ensure_output_outside_repo(output_dir, repo_root)
    output_dir.mkdir(parents=True, exist_ok=True)
    root_name = f"Pattern-Map-v16-{commit[:12]}"
    zip_name = f"PATTERN_MAP_V16_OWNER_REVIEW_{generated_date}_{commit[:12]}.zip"
    zip_path = output_dir / zip_name
    sidecar_path = output_dir / f"{zip_name}.sha256"
    lock_path = output_dir / f".{zip_name}.lock"
    lock_stat = create_exclusive_marker(
        lock_path,
        f"Pattern Map owner-bundle build PID {os.getpid()} for {commit}\n",
    )
    published_zip_stat: os.stat_result | None = None
    published_sidecar_stat: os.stat_result | None = None
    try:
        if zip_path.exists() or sidecar_path.exists():
            raise BuildError(f"refusing to overwrite existing owner artifact: {zip_name}")

        with tempfile.TemporaryDirectory(prefix="pattern-map-owner-stage-") as temporary:
            stage_root = Path(temporary) / root_name
            stage_root.mkdir()
            payload_records: list[dict[str, object]] = []
            payload_total = 0
            selected_control_bytes: dict[str, bytes] = {}
            tree_paths = {relative for relative, _mode, _object_id in tree}
            missing_controls = sorted(REQUIRED_REPOSITORY_PATHS - tree_paths)
            if missing_controls:
                raise BuildError(f"exact commit lacks owner-bundle control sources: {missing_controls}")

            exact_blobs = git_blobs(repo_root, [object_id for _path, _mode, object_id in tree])
            for relative, mode, object_id in tree:
                data = exact_blobs[object_id]
                assert_payload_bytes_safe(relative, data)
                package_relative = f"repository/{relative}"
                write_regular(stage_root / package_relative, data, mode)
                payload_records.append(record(package_relative, mode, data))
                payload_total += len(data)
                for control_name, source_path in CONTROL_SOURCE_PATHS.items():
                    if relative == source_path:
                        selected_control_bytes[control_name] = data

            for control_name, data in sorted(selected_control_bytes.items()):
                write_regular(stage_root / control_name, data, "100644")

            trusted_extracted_verifier = trusted_adjacent_regular_bytes(
                "verify_extracted_owner_bundle.py"
            )
            if selected_control_bytes.get("VERIFY_PACKAGE.py") != trusted_extracted_verifier:
                raise BuildError(
                    "staged extracted verifier differs from the trusted "
                    "builder-adjacent verifier"
                )

            staged_repository = stage_root / "repository"
            owner_intent = (
                staged_repository / "docs" / "OWNER_INTENT_V16.md"
            ).read_bytes()
            if sha256_bytes(owner_intent) != OWNER_INTENT_SHA256:
                raise BuildError("exact commit does not contain the locked Pattern Map v16 owner intent")
            owner_checksum = (
                staged_repository / "docs" / "OWNER_INTENT_V16.sha256"
            ).read_text(encoding="utf-8").split()
            if owner_checksum != [OWNER_INTENT_SHA256, "OWNER_INTENT_V16.md"]:
                raise BuildError("owner-intent checksum control does not match the locked checkpoint")

            staged_bounded_verifier = (
                staged_repository / "handoff" / "verify_owner_review_package.py"
            ).read_bytes()
            trusted_bounded_verifier = trusted_adjacent_regular_bytes(
                "verify_owner_review_package.py"
            )
            if staged_bounded_verifier != trusted_bounded_verifier:
                raise BuildError(
                    "staged bounded verifier differs from the trusted builder-adjacent verifier"
                )
            bounded_run = subprocess.run(
                [sys.executable, "handoff/verify_owner_review_package.py"],
                cwd=staged_repository,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                check=False,
            )
            if bounded_run.returncode != 0:
                raise BuildError(
                    "committed bounded owner-review manifest failed inside the staged payload: "
                    + bounded_run.stdout.strip()
                )

            metadata = metadata_payload(
                commit=commit,
                generated_date=generated_date,
                root_directory=root_name,
            )
            metadata_data = json_bytes(metadata)
            write_regular(stage_root / "PACKAGE_METADATA.json", metadata_data)

            control_records: list[dict[str, object]] = []
            for control_name in sorted({*selected_control_bytes, "PACKAGE_METADATA.json"}):
                control_data = (stage_root / control_name).read_bytes()
                control_records.append(record(control_name, "100644", control_data))
            manifest = {
                "schema_version": 1,
                "package": PACKAGE_NAME,
                "status": PACKAGE_STATUS,
                "source_commit": commit,
                "root_directory": root_name,
                "payload_root": "repository",
                "file_count": len(payload_records),
                "total_bytes": payload_total,
                "control_files": control_records,
                "files": payload_records,
            }
            write_regular(stage_root / "FULL_PAYLOAD_MANIFEST.json", json_bytes(manifest))

            verifier_run = subprocess.run(
                [sys.executable, str(stage_root / "VERIFY_PACKAGE.py")],
                cwd=stage_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                check=False,
            )
            if verifier_run.returncode != 0:
                raise BuildError("staged extracted verifier failed: " + verifier_run.stdout.strip())

            temporary_zip = output_dir / f".{zip_name}.building-{os.getpid()}"
            temporary_sidecar = output_dir / f".{zip_name}.sha256.building-{os.getpid()}"
            if temporary_zip.exists() or temporary_sidecar.exists():
                raise BuildError(f"temporary output already exists for {zip_name}")
            temporary_zip_stat: os.stat_result | None = None
            temporary_sidecar_stat: os.stat_result | None = None
            try:
                write_zip(stage_root, temporary_zip, root_name)
                temporary_zip_stat = temporary_zip.lstat()
                assert_zip_safe(temporary_zip, root_name=root_name)
                copied_verification = verify_copied_extraction(temporary_zip, root_name=root_name)
                zip_digest = sha256_file(temporary_zip)
                temporary_sidecar_stat = create_exclusive_marker(
                    temporary_sidecar,
                    f"{zip_digest}  {zip_path.name}\n",
                )
                published_zip_stat = publish_exclusive(
                    temporary_zip, zip_path, temporary_zip_stat
                )
                published_sidecar_stat = publish_exclusive(
                    temporary_sidecar, sidecar_path, temporary_sidecar_stat
                )
                if sha256_same_regular_file(zip_path, published_zip_stat) != zip_digest:
                    raise BuildError("published owner ZIP digest changed during build")
                expected_sidecar = f"{zip_digest}  {zip_path.name}\n".encode("utf-8")
                if bytes_same_regular_file(sidecar_path, published_sidecar_stat) != expected_sidecar:
                    raise BuildError("published owner ZIP sidecar changed during build")
            except Exception:
                unlink_if_same(zip_path, published_zip_stat)
                unlink_if_same(sidecar_path, published_sidecar_stat)
                raise
            finally:
                unlink_if_same(temporary_zip, temporary_zip_stat)
                unlink_if_same(temporary_sidecar, temporary_sidecar_stat)
    finally:
        unlink_if_same(lock_path, lock_stat)

    if published_zip_stat is None or published_sidecar_stat is None:
        raise BuildError("owner artifact publication did not complete")
    assert_same_regular_file(zip_path, published_zip_stat)
    assert_same_regular_file(sidecar_path, published_sidecar_stat)
    summary: dict[str, object] = {
        "zip_name": zip_path.name,
        "sidecar_name": sidecar_path.name,
        "source_commit": commit,
        "source_ref": source_ref,
        "root_directory": root_name,
        "payload_file_count": len(tree),
        "payload_total_bytes": sum(int(item["bytes"]) for item in payload_records),
        "zip_bytes": published_zip_stat.st_size,
        "zip_sha256": zip_digest,
        "copied_location_verification": copied_verification.splitlines()[0],
    }
    return zip_path, sidecar_path, summary


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", help="Pattern Map Git root (default: this checkout)")
    parser.add_argument("--commit", default="HEAD", help="exact commit to package; must equal HEAD")
    parser.add_argument("--output-dir", required=True, help="existing/new directory outside the repository")
    parser.add_argument("--date", required=True, type=parse_date, help="package date in YYYY-MM-DD")
    parser.add_argument(
        "--require-upstream",
        action="store_true",
        help="also require the current branch's upstream tip to equal the exact source commit",
    )
    args = parser.parse_args(argv)
    try:
        repo_root = resolve_repo_root(args.repo_root)
        zip_path, sidecar_path, summary = build_bundle(
            repo_root=repo_root,
            requested_commit=args.commit,
            output_dir=Path(args.output_dir),
            generated_date=args.date,
            require_upstream=args.require_upstream,
        )
    except (BuildError, OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"FAIL owner bundle: {error}", file=sys.stderr)
        return 1
    print(json.dumps(summary, indent=2, sort_keys=True))
    print(f"WROTE {zip_path}")
    print(f"WROTE {sidecar_path}")
    print("BOUNDARY: package construction is not merge, deployment, publication, release, or acceptance.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
