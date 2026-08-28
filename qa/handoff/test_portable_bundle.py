#!/usr/bin/env python3
"""Regression coverage for the portable Signal Foundry context bundle.

The test intentionally builds from ``HEAD`` through the checked-in builder.
Before that builder is committed, local pre-commit runs skip with an explicit
message; once it is present at ``HEAD`` the complete extraction and verifier
path runs.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[2]
BUILDER = ROOT / "handoff" / "signal-foundry" / "build_portable_bundle.py"
DATE = "2099-01-02"
FORBIDDEN_PATH_SEGMENTS = {
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
ABSOLUTE_TEXT_PREFIXES = tuple("/" + part + "/" for part in ("Users", "Volumes", "home", "private", "var"))
WINDOWS_ABSOLUTE_PREFIXES = (
    "C" + ":" + "\\",
    "D" + ":" + "\\",
    "C" + ":/",
    "D" + ":/",
)
FORBIDDEN_PATH_MARKERS = ABSOLUTE_TEXT_PREFIXES + WINDOWS_ABSOLUTE_PREFIXES + (
    "file" + "://",
)
FORBIDDEN_PRIVATE_KEY_MARKERS = (
    "-----BEGIN " + "PRIVATE KEY-----",
    "-----BEGIN " + "OPENSSH PRIVATE KEY-----",
    "-----BEGIN " + "RSA PRIVATE KEY-----",
    "-----BEGIN " + "EC PRIVATE KEY-----",
)
PRINTABLE_ASCII_RUN = re.compile(rb"[\x20-\x7e]{5,}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_head() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "--verify", "HEAD"], cwd=ROOT, text=True
    ).strip()


def safe_bundle_path(value: str) -> bool:
    if not value or "\x00" in value or "\\" in value:
        return False
    parsed = PurePosixPath(value)
    return (
        not parsed.is_absolute()
        and all(part not in {"", ".", ".."} for part in parsed.parts)
        and ":" not in parsed.parts[0]
        and not any(part.lower() in FORBIDDEN_PATH_SEGMENTS for part in parsed.parts)
        and parsed.as_posix() == value
    )


def forbidden_marker(data: bytes) -> str | None:
    lowered_data = data.lower()
    for marker in FORBIDDEN_PRIVATE_KEY_MARKERS:
        if marker.lower().encode("ascii") in lowered_data:
            return marker
    for run in PRINTABLE_ASCII_RUN.findall(data):
        lowered_run = run.lower()
        for marker in FORBIDDEN_PATH_MARKERS:
            if marker.lower().encode("ascii") in lowered_run:
                return marker
    return None


def run_builder(output_dir: Path) -> tuple[subprocess.CompletedProcess[str], dict[str, object]]:
    result = subprocess.run(
        [
            sys.executable,
            str(BUILDER),
            "--repo-root",
            str(ROOT),
            "--commit",
            "HEAD",
            "--output-dir",
            str(output_dir),
            "--date",
            DATE,
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        return result, {}
    return result, json.loads(result.stdout)


def load_builder_module():
    spec = importlib.util.spec_from_file_location("pattern_map_portable_builder", BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load portable builder module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PortableBundleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not BUILDER.is_file():
            raise unittest.SkipTest("portable builder is not present in the working tree")
        present = subprocess.run(
            ["git", "cat-file", "-e", "HEAD:handoff/signal-foundry/build_portable_bundle.py"],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if present.returncode != 0:
            raise unittest.SkipTest(
                "portable builder is not committed at HEAD; rerun after the builder commit"
            )

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory(prefix="pattern-map-portable-test-")
        self.addCleanup(self.temp_dir.cleanup)
        self.workspace = Path(self.temp_dir.name)
        self.output = self.workspace / "output"
        self.output.mkdir()
        result, summary = run_builder(self.output)
        self.assertEqual(
            result.returncode,
            0,
            msg=(result.stdout + "\n" + result.stderr).strip(),
        )
        self.summary = summary
        self.zip_path = self.output / str(summary["zip_name"])
        self.sidecar_path = self.output / str(summary["sidecar_name"])
        self.assertTrue(self.zip_path.is_file())
        self.assertTrue(self.sidecar_path.is_file())
        self.extract = self.workspace / "extract"
        self.extract.mkdir()
        with zipfile.ZipFile(self.zip_path) as archive:
            bad = archive.testzip()
            self.assertIsNone(bad, msg=f"corrupt ZIP member: {bad}")
            archive.extractall(self.extract)
        self.resolve_bundle_root()

    def resolve_bundle_root(self) -> None:
        roots = [path for path in self.extract.iterdir() if path.is_dir()]
        self.assertEqual(len(roots), 1)
        self.bundle_root = roots[0]

    def restore_extracted_bundle(self) -> None:
        shutil.rmtree(self.extract)
        self.extract.mkdir()
        with zipfile.ZipFile(self.zip_path) as archive:
            archive.extractall(self.extract)
        self.resolve_bundle_root()

    def run_embedded_verifier(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(self.bundle_root / "verify_bundle.py")],
            cwd=self.bundle_root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def reseal_payload(self, relative: str, suffix: bytes) -> None:
        """Modify one payload and consistently reseal all non-circular controls."""

        target = self.bundle_root / Path(*PurePosixPath(relative).parts)
        target.write_bytes(target.read_bytes() + suffix)

        manifest_path = self.bundle_root / "BUNDLE_MANIFEST.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        records = {str(record["path"]): record for record in manifest["files"]}
        self.assertIn(relative, records)
        records[relative]["bytes"] = target.stat().st_size
        records[relative]["sha256"] = sha256(target)

        checksums_path = self.bundle_root / "SHA256SUMS.txt"
        checksums: dict[str, str] = {}
        for line in checksums_path.read_text(encoding="utf-8").splitlines():
            digest, path_value = line.split("  ", 1)
            checksums[path_value] = digest
        self.assertIn(relative, checksums)
        checksums[relative] = sha256(target)
        checksums_path.write_text(
            "".join(f"{checksums[path]}  {path}\n" for path in sorted(checksums)),
            encoding="utf-8",
        )
        records["SHA256SUMS.txt"]["bytes"] = checksums_path.stat().st_size
        records["SHA256SUMS.txt"]["sha256"] = sha256(checksums_path)
        manifest["total_bytes"] = sum(int(record["bytes"]) for record in manifest["files"])
        manifest_path.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def test_embedded_verifier_and_manifest_cover_extracted_files(self) -> None:
        verifier = self.run_embedded_verifier()
        self.assertEqual(verifier.returncode, 0, msg=verifier.stdout + verifier.stderr)
        self.assertRegex(verifier.stdout, r"PASS portable bundle: [0-9]+ files / [0-9]+ bytes")

        manifest = json.loads((self.bundle_root / "BUNDLE_MANIFEST.json").read_text(encoding="utf-8"))
        metadata = json.loads((self.bundle_root / "BUNDLE_METADATA.json").read_text(encoding="utf-8"))
        records = manifest["files"]
        self.assertEqual([record["path"] for record in records], sorted(record["path"] for record in records))
        self.assertNotIn("BUNDLE_MANIFEST.json", [record["path"] for record in records])
        self.assertEqual(manifest["manifest_self_exclusion"], "BUNDLE_MANIFEST.json is excluded from its own files list because self-hashing is circular.")
        self.assertEqual(metadata["source_commit"], git_head())
        self.assertEqual(manifest["source_commit"], git_head())
        self.assertEqual(metadata["source_branch"], "codex/pattern-map-v16-foundation")
        self.assertEqual(manifest["source_branch"], "codex/pattern-map-v16-foundation")
        self.assertEqual(manifest["file_count"], len(records))
        self.assertEqual(manifest["total_bytes"], sum(record["bytes"] for record in records))

        for record in records:
            relative = str(record["path"])
            self.assertTrue(safe_bundle_path(relative), relative)
            path = self.bundle_root / Path(*PurePosixPath(relative).parts)
            self.assertTrue(path.is_file(), relative)
            self.assertFalse(path.is_symlink(), relative)
            self.assertEqual(path.stat().st_size, record["bytes"], relative)
            self.assertEqual(sha256(path), record["sha256"], relative)

    def test_start_here_states_downstream_contract_and_reading_path(self) -> None:
        start = (self.bundle_root / "START_HERE.md").read_text(encoding="utf-8")
        normalized_start = " ".join(start.split()).lower()
        required_facts = (
            "Signal Foundry",
            "Signal Foundry's own repository is authoritative",
            "OPERATOR_DECISION",
            "RATIONALE",
            "CONTEXT_DISPOSITION",
            "not current-schema-valid",
            "No V14 deep link exists",
            "no Pattern Map classifier exists",
            "no app mutation",
            "missing files or materially changed contracts must be requested and reconciled",
            "do not infer",
            "some selected markdown intentionally retains links",
            "subset boundary",
            "site/exports/standalone/pattern-map-v16.html",
            "site/exports/pattern-map-v16-owner-review.pdf",
            "research/the-echo-problem/",
        )
        for fact in required_facts:
            with self.subTest(fact=fact):
                self.assertIn(" ".join(fact.split()).lower(), normalized_start)
        self.assertIn("```text\nYou are continuing", start)
        self.assertIn("read-only", start.lower())
        self.assertIn(self.zip_path.name + ".sha256", start)
        self.assertIn("Stop if the outer checksum fails", start)

        copyable = (self.bundle_root / "COPYABLE_PROMPT.md").read_text(encoding="utf-8")
        normalized_copyable = " ".join(copyable.split()).lower()
        self.assertIn("some bundled markdown intentionally links", normalized_copyable)
        self.assertIn("request the exact missing file", normalized_copyable)
        self.assertIn("do not infer, recreate, or silently substitute", normalized_copyable)
        self.assertIn("optional local evidence, not required packet inputs", normalized_copyable)
        self.assertIn("only if each file is present", normalized_copyable)
        self.assertIn("record absent/unverified and continue", normalized_copyable)
        self.assertIn("required tracked packet file", normalized_copyable)
        self.assertIn("record unverified and continue", normalized_copyable)

        self.assertIn("optional local evidence, not required packet inputs", normalized_start)
        self.assertIn("record `absent/unverified` and continue", normalized_start)

    def test_optional_local_inputs_are_guarded_and_nonblocking(self) -> None:
        canonical = (
            self.bundle_root
            / "handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md"
        ).read_text(encoding="utf-8")
        brief = (
            self.bundle_root
            / "handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md"
        ).read_text(encoding="utf-8")
        normalized = " ".join((canonical + "\n" + brief).split()).lower()
        self.assertIn("optional local evidence", normalized)
        self.assertIn("not a required packet input", normalized)
        self.assertIn("optional local audit unavailable; continue without it", normalized)
        self.assertIn("do not fetch", normalized)

        guarded_blocks = []
        for document in (canonical, brief):
            for block in re.findall(r"```sh\n(.*?)\n```", document, flags=re.DOTALL):
                if "git show --stat 4a6ed78" in block:
                    guarded_blocks.append(block)
                    self.assertIn(
                        "git rev-parse --verify --quiet '4a6ed78^{commit}'",
                        block,
                    )
                    active_lines = [
                        line.strip()
                        for line in block.splitlines()
                        if line.strip() and not line.lstrip().startswith("#")
                    ]
                    self.assertFalse(
                        any(
                            re.match(r"git\s+(fetch|reset|push|merge)\b", line)
                            for line in active_lines
                        )
                    )
        self.assertEqual(len(guarded_blocks), 2)

        guard = guarded_blocks[0]
        receiving = self.workspace / "fresh-signal-foundry"
        receiving.mkdir()
        subprocess.run(["git", "init", "-b", "main"], cwd=receiving, check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "config", "user.name", "Portable QA"], cwd=receiving,
                       check=True)
        subprocess.run(["git", "config", "user.email", "qa@example.invalid"],
                       cwd=receiving, check=True)
        (receiving / "README.md").write_text("fixture\n", encoding="utf-8")
        subprocess.run(["git", "add", "README.md"], cwd=receiving, check=True)
        subprocess.run(["git", "commit", "-m", "fixture"], cwd=receiving, check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        absent = subprocess.run(
            ["/bin/sh", "-c", guard], cwd=receiving, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        )
        self.assertEqual(absent.returncode, 0, absent.stdout + absent.stderr)
        self.assertIn("UNVERIFIED", absent.stdout)
        self.assertIn("continue without it", absent.stdout)

        commit_only_guard = guard.replace("4a6ed78", "HEAD")
        commit_only = subprocess.run(
            ["/bin/sh", "-c", commit_only_guard], cwd=receiving, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        )
        self.assertEqual(commit_only.returncode, 0, commit_only.stdout + commit_only.stderr)
        self.assertIn("optional local audit branch unavailable", commit_only.stdout)

        subprocess.run(
            ["git", "branch", "codex/pattern-map-signal-foundry-transfer-audit", "HEAD"],
            cwd=receiving, check=True,
        )
        with_branch = subprocess.run(
            ["/bin/sh", "-c", commit_only_guard], cwd=receiving, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
        )
        self.assertEqual(with_branch.returncode, 0, with_branch.stdout + with_branch.stderr)
        self.assertNotIn("optional local audit branch unavailable", with_branch.stdout)

    def test_handoff_distinguishes_content_checkpoint_from_resolved_head(self) -> None:
        canonical = (
            self.bundle_root
            / "handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md"
        ).read_text(encoding="utf-8")
        summary = " ".join(canonical.splitlines()[:20]).lower()
        self.assertIn("content checkpoint", summary)
        self.assertIn("resolve the current", summary)
        self.assertIn("bundle_metadata.json.source_commit", summary)

        brief = (
            self.bundle_root
            / "handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md"
        ).read_text(encoding="utf-8")
        objects = []
        for source in re.findall(r"```json\n(.*?)\n```", brief, flags=re.DOTALL):
            try:
                objects.append(json.loads(source))
            except json.JSONDecodeError:
                continue
        checklist = next(value for value in objects if "pattern_map" in value)
        pattern_map = checklist["pattern_map"]
        self.assertEqual(
            pattern_map["content_checkpoint"],
            "874a0a8e09f0bde11532cf873087865addb7d973",
        )
        self.assertIsNone(pattern_map["head"])
        self.assertEqual(pattern_map["head_resolution"]["status"], "resolve_at_use")
        self.assertEqual(
            pattern_map["head_resolution"]["sealed_packet_field"],
            "BUNDLE_METADATA.json.source_commit",
        )

    def test_zip_sidecar_safety_and_forbidden_payloads(self) -> None:
        sidecar = self.sidecar_path.read_text(encoding="utf-8")
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)\n", sidecar)
        self.assertIsNotNone(match)
        assert match is not None
        self.assertEqual(match.group(2), self.zip_path.name)
        self.assertEqual(match.group(1), sha256(self.zip_path))
        self.assertNotIn("/", match.group(2))
        self.assertNotIn("\\", match.group(2))

        with zipfile.ZipFile(self.zip_path) as archive:
            names = archive.namelist()
            self.assertEqual(len(names), len(set(names)))
            for name in names:
                self.assertNotIn("\\", name)
                self.assertTrue(name.endswith("/") or safe_bundle_path(name.split("/", 1)[1]), name)
                self.assertFalse(name.startswith("/"), name)
                self.assertNotIn("../", name)
                self.assertNotIn("/..", name)
                self.assertIsNotNone(archive.getinfo(name))

        for path in self.bundle_root.rglob("*"):
            if path.is_dir():
                continue
            relative = path.relative_to(self.bundle_root).as_posix()
            self.assertTrue(safe_bundle_path(relative), relative)
            self.assertFalse(path.is_symlink(), relative)
            self.assertIsNone(forbidden_marker(path.read_bytes()), relative)

        self.assertNotIn("/" + "Users" + "/" + "gpt", BUILDER.read_text(encoding="utf-8"))
        archive_files = [path for path in self.bundle_root.rglob("*") if path.is_file()]
        self.assertEqual(self.summary["archive_file_count"], len(archive_files))
        self.assertEqual(
            self.summary["archive_total_bytes"],
            sum(path.stat().st_size for path in archive_files),
        )

    def test_resealed_binary_markers_fail_closed(self) -> None:
        targets = (
            "assets/diagrams/historical-v13-pattern-recognition-diagram-v12.png",
            "site/exports/pattern-map-v16-owner-review.pdf",
        )
        markers = (
            b"\x00/Users/example-machine/private-path\x00",
            b"\x00-----BEGIN PRIVATE KEY-----\x00",
        )
        for index, (relative, marker) in enumerate(
            (pair for target in targets for pair in ((target, markers[0]), (target, markers[1])))
        ):
            with self.subTest(relative=relative, marker=marker):
                if index:
                    self.restore_extracted_bundle()
                self.reseal_payload(relative, marker)
                verifier = self.run_embedded_verifier()
                self.assertNotEqual(verifier.returncode, 0, verifier.stdout + verifier.stderr)
                self.assertIn(
                    "source-machine or private-key marker",
                    (verifier.stdout + verifier.stderr).lower(),
                )

    def test_resealed_benign_binary_payloads_pass(self) -> None:
        targets = (
            "assets/diagrams/historical-v13-pattern-recognition-diagram-v12.png",
            "site/exports/pattern-map-v16-owner-review.pdf",
        )
        for index, relative in enumerate(targets):
            with self.subTest(relative=relative):
                if index:
                    self.restore_extracted_bundle()
                self.reseal_payload(relative, b"\x00BENIGN_BINARY_CONTROL_2026\x00")
                verifier = self.run_embedded_verifier()
                self.assertEqual(verifier.returncode, 0, verifier.stdout + verifier.stderr)

    def test_builder_marker_helper_covers_unknown_binary_suffixes(self) -> None:
        builder = load_builder_module()
        samples = (
            (b"\x89BIN\x00/Users/example-machine/private\x00", True),
            (b"\x89BIN\x00-----BEGIN OPENSSH PRIVATE KEY-----\x00", True),
            (b"\x89BIN\x00BENIGN_BINARY_CONTROL_2026\x00", False),
        )
        for data, forbidden in samples:
            with self.subTest(data=data):
                marker = builder._forbidden_marker("payload.unknown", data)
                self.assertEqual(marker is not None, forbidden)
                self.assertEqual(marker is not None, forbidden_marker(data) is not None)

    def test_same_commit_and_date_produce_identical_zip(self) -> None:
        second_output = self.workspace / "second-output"
        second_output.mkdir()
        result, summary = run_builder(second_output)
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
        second_zip = second_output / str(summary["zip_name"])
        self.assertEqual(self.zip_path.read_bytes(), second_zip.read_bytes())
        self.assertEqual(sha256(self.zip_path), sha256(second_zip))

    def test_builder_refuses_overwrite(self) -> None:
        result, _ = run_builder(self.output)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("refusing to overwrite", (result.stdout + result.stderr).lower())


if __name__ == "__main__":
    unittest.main()
