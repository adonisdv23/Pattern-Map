#!/usr/bin/env python3
"""Regression coverage for the portable Signal Foundry context bundle.

The test intentionally builds from ``HEAD`` through the checked-in builder.
Before that builder is committed, local pre-commit runs skip with an explicit
message; once it is present at ``HEAD`` the complete extraction and verifier
path runs.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re
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
FORBIDDEN_TEXT_MARKERS = ABSOLUTE_TEXT_PREFIXES + WINDOWS_ABSOLUTE_PREFIXES + (
    "file" + "://",
    "-----BEGIN " + "PRIVATE KEY-----",
    "-----BEGIN " + "OPENSSH PRIVATE KEY-----",
    "-----BEGIN " + "RSA PRIVATE KEY-----",
    "-----BEGIN " + "EC PRIVATE KEY-----",
)
TEXT_SUFFIXES = {
    ".css", ".html", ".js", ".json", ".md", ".mjs", ".py", ".sh",
    ".txt", ".yaml", ".yml",
}


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
        roots = [path for path in self.extract.iterdir() if path.is_dir()]
        self.assertEqual(len(roots), 1)
        self.bundle_root = roots[0]

    def test_embedded_verifier_and_manifest_cover_extracted_files(self) -> None:
        verifier = subprocess.run(
            [sys.executable, str(self.bundle_root / "verify_bundle.py")],
            cwd=self.bundle_root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
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
            if path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            lowered = path.read_bytes().decode("utf-8", errors="ignore").lower()
            for marker in FORBIDDEN_TEXT_MARKERS:
                with self.subTest(path=relative, marker=marker):
                    self.assertNotIn(marker.lower(), lowered)

        self.assertNotIn("/" + "Users" + "/" + "gpt", BUILDER.read_text(encoding="utf-8"))
        archive_files = [path for path in self.bundle_root.rglob("*") if path.is_file()]
        self.assertEqual(self.summary["archive_file_count"], len(archive_files))
        self.assertEqual(
            self.summary["archive_total_bytes"],
            sum(path.stat().st_size for path in archive_files),
        )

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
