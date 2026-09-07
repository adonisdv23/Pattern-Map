#!/usr/bin/env python3
"""Adversarial tests for the bounded manifest and complete owner bundle."""

from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
import warnings
import zipfile
from pathlib import Path
from unittest import mock


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    if specification is None or specification.loader is None:
        raise RuntimeError(f"cannot load test module from {path}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


BUILDER = load_module(
    "pattern_map_owner_bundle_builder",
    REPOSITORY_ROOT / "handoff" / "build_owner_review_bundle.py",
)


def bounded_manifest_payload(module, records: list[dict[str, object]]) -> dict[str, object]:
    return {
        "schema_version": module.MANIFEST_SCHEMA_VERSION,
        "package": module.PACKAGE_NAME,
        "status": module.PACKAGE_STATUS,
        "generated_date": module.GENERATED_DATE,
        "historical_converged_checkpoint": module.CONTENT_CHECKPOINT,
        "owner_review_pdf_checkpoint": module.OWNER_REVIEW_PDF_CHECKPOINT,
        "phase_0_hardening_baseline": module.PHASE_0_BASELINE,
        "integrated_lane_heads": module.LANE_HEADS,
        "convergence_correction_heads": module.CONVERGENCE_CORRECTION_HEADS,
        "opportunity_expansion_baseline": module.OPPORTUNITY_EXPANSION_BASELINE,
        "opportunity_expansion_lane_heads": module.OPPORTUNITY_EXPANSION_LANE_HEADS,
        "opportunity_loop_2_reviewed_head": module.OPPORTUNITY_LOOP_2_REVIEWED_HEAD,
        "source_head": None,
        "source_head_resolution": module.SOURCE_HEAD_RESOLUTION,
        "evidence_note": module.EVIDENCE_NOTE,
        "archive_scope": module.ARCHIVE_SCOPE,
        "file_count": len(records),
        "total_bytes": sum(int(item["bytes"]) for item in records),
        "files": records,
    }


def run(command: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )


def git(repo: Path, *args: str) -> str:
    completed = run(["git", *args], cwd=repo)
    if completed.returncode != 0:
        raise RuntimeError(completed.stdout)
    return completed.stdout.strip()


def initialize_repository(root: Path) -> str:
    bounded = load_module(
        f"tiny_bounded_manifest_{os.urandom(4).hex()}",
        REPOSITORY_ROOT / "handoff" / "verify_owner_review_package.py",
    )
    copied_sources = {
        "docs/OWNER_INTENT_V16.md",
        "docs/OWNER_INTENT_V16.sha256",
        "handoff/START_HERE_OWNER_REVIEW.md",
        "handoff/verify_extracted_owner_bundle.py",
        "handoff/verify_owner_review_package.py",
    }
    for relative in bounded.REQUIRED_PATHS:
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if relative in copied_sources:
            shutil.copy2(REPOSITORY_ROOT / relative, destination)
        elif relative != "handoff/OWNER_REVIEW_MANIFEST_V16.json":
            destination.write_text(f"owner-bundle fixture: {relative}\n", encoding="utf-8")
    archived_cache = (
        root
        / "archive"
        / "historical-transfer"
        / "tools"
        / "__pycache__"
        / "historical.pyc"
    )
    archived_cache.parent.mkdir(parents=True, exist_ok=True)
    archived_cache.write_bytes(b"immutable archived cache fixture\n")
    (root / "README.md").write_text("# Tiny exact tree\n", encoding="utf-8")
    runner = root / "qa" / "run_owner_review_checks.sh"
    if runner.exists():
        runner.chmod(0o755)
    bounded.ROOT = root
    bounded.MANIFEST = root / "handoff" / "OWNER_REVIEW_MANIFEST_V16.json"
    records = bounded.current_records()
    bounded.MANIFEST.write_text(
        json.dumps(bounded_manifest_payload(bounded, records), indent=2) + "\n",
        encoding="utf-8",
    )
    git(root, "init", "-q")
    git(root, "config", "user.name", "Owner Bundle Test")
    git(root, "config", "user.email", "owner-bundle-test@example.invalid")
    git(root, "checkout", "-qb", "codex/owner-bundle-test")
    git(root, "add", ".")
    git(root, "commit", "-qm", "test fixture")
    (root / "SECOND.md").write_text("second exact commit\n", encoding="utf-8")
    git(root, "add", "SECOND.md")
    git(root, "commit", "-qm", "second fixture commit")
    return git(root, "rev-parse", "HEAD")


def extract(zip_path: Path, destination: Path) -> Path:
    with zipfile.ZipFile(zip_path) as archive:
        archive.extractall(destination)
        roots = {name.split("/", 1)[0] for name in archive.namelist() if name}
    if len(roots) != 1:
        raise AssertionError(f"expected one enclosing root, observed {roots}")
    return destination / next(iter(roots))


class BoundedManifestTests(unittest.TestCase):
    def load_bounded(self):
        return load_module(
            f"bounded_manifest_{id(self)}_{os.urandom(3).hex()}",
            REPOSITORY_ROOT / "handoff" / "verify_owner_review_package.py",
        )

    def make_tiny_manifest(self, root: Path):
        module = self.load_bounded()
        module.ROOT = root
        module.MANIFEST = root / "manifest.json"
        module.REQUIRED_PATHS = ["payload.txt"]
        (root / "payload.txt").write_text("bounded payload\n", encoding="utf-8")
        records = module.current_records()
        payload = bounded_manifest_payload(module, records)
        module.MANIFEST.write_text(json.dumps(payload) + "\n", encoding="utf-8")
        return module, payload

    def test_strict_control_fields_duplicate_nonfinite_and_symlink(self) -> None:
        with tempfile.TemporaryDirectory(prefix="owner-bounded-test-") as temporary:
            root = Path(temporary)
            module, payload = self.make_tiny_manifest(root)
            module.verify_manifest()

            mutations = {
                "false-status": {**payload, "status": "merged, deployed, published, validated"},
                "boolean-schema": {**payload, "schema_version": True},
                "extra-key": {**payload, "authorized": True},
                "missing-key": {key: value for key, value in payload.items() if key != "archive_scope"},
            }
            for name, mutation in mutations.items():
                with self.subTest(name=name):
                    module.MANIFEST.write_text(json.dumps(mutation) + "\n", encoding="utf-8")
                    with self.assertRaises(AssertionError):
                        module.verify_manifest()

            valid = json.dumps(payload)
            duplicate = valid.replace(
                '"schema_version": 2', '"schema_version": 2, "schema_version": 2', 1
            )
            module.MANIFEST.write_text(duplicate + "\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                module.verify_manifest()

            nonfinite = valid.replace('"file_count": 1', '"file_count": NaN', 1)
            module.MANIFEST.write_text(nonfinite + "\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                module.verify_manifest()

            module.MANIFEST.write_text(valid + "\n", encoding="utf-8")
            manifest_target = root / "external-manifest-target.json"
            manifest_target.write_text(valid + "\n", encoding="utf-8")
            module.MANIFEST.unlink()
            try:
                module.MANIFEST.symlink_to(manifest_target.name)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks are unavailable on this platform")
            with self.assertRaises(AssertionError):
                module.verify_manifest()
            module.MANIFEST.unlink()
            module.MANIFEST.write_text(valid + "\n", encoding="utf-8")
            target = root / "target.txt"
            target.write_text("outside manifest path\n", encoding="utf-8")
            (root / "payload.txt").unlink()
            try:
                (root / "payload.txt").symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks are unavailable on this platform")
            with self.assertRaises(AssertionError):
                module.verify_manifest()

    def test_author_writer_requires_clean_named_nondefault_git_checkout(self) -> None:
        with tempfile.TemporaryDirectory(prefix="owner-author-test-") as temporary:
            root = Path(temporary)
            git(root, "init", "-q")
            git(root, "config", "user.name", "Owner Bundle Test")
            git(root, "config", "user.email", "owner-bundle-test@example.invalid")
            git(root, "checkout", "-qb", "codex/owner-bundle-test")
            (root / "payload.txt").write_text("clean\n", encoding="utf-8")
            git(root, "add", "payload.txt")
            git(root, "commit", "-qm", "clean author fixture")
            module = self.load_bounded()
            module.ROOT = root
            module.assert_clean_git_authoring_context()
            git(root, "checkout", "-qb", "main")
            with self.assertRaises(AssertionError):
                module.assert_clean_git_authoring_context()
            git(root, "checkout", "-q", "codex/owner-bundle-test")
            git(root, "checkout", "-q", "--detach", "HEAD")
            with self.assertRaises(AssertionError):
                module.assert_clean_git_authoring_context()
            git(root, "checkout", "-q", "codex/owner-bundle-test")
            (root / "dirty.txt").write_text("dirty\n", encoding="utf-8")
            with self.assertRaises(AssertionError):
                module.assert_clean_git_authoring_context()


class CompleteOwnerBundleTests(unittest.TestCase):
    def build_pair(self, base: Path):
        repo = base / "repo"
        repo.mkdir()
        commit = initialize_repository(repo)
        first_output = base / "first"
        second_output = base / "second"
        first = BUILDER.build_bundle(
            repo_root=repo,
            requested_commit="HEAD",
            output_dir=first_output,
            generated_date="2026-08-30",
            require_upstream=False,
        )
        second = BUILDER.build_bundle(
            repo_root=repo,
            requested_commit=commit,
            output_dir=second_output,
            generated_date="2026-08-30",
            require_upstream=False,
        )
        return repo, commit, first, second

    def test_deterministic_bundle_and_hostile_extraction_mutations(self) -> None:
        with tempfile.TemporaryDirectory(prefix="owner-complete-test-") as temporary:
            base = Path(temporary)
            repo, commit, first, second = self.build_pair(base)
            first_zip, first_sidecar, first_summary = first
            second_zip, second_sidecar, second_summary = second
            self.assertEqual(first_zip.read_bytes(), second_zip.read_bytes())
            self.assertEqual(first_sidecar.read_text(), second_sidecar.read_text())
            self.assertEqual(first_summary["source_commit"], commit)
            self.assertEqual(second_summary["source_commit"], commit)
            self.assertIn(BUILDER.sha256_file(first_zip), first_sidecar.read_text())

            git(repo, "branch", "-m", "renamed-with-same-commit")
            third_zip, third_sidecar, third_summary = BUILDER.build_bundle(
                repo_root=repo,
                requested_commit="HEAD",
                output_dir=base / "third-renamed-branch",
                generated_date="2026-08-30",
                require_upstream=False,
            )
            self.assertEqual(first_zip.read_bytes(), third_zip.read_bytes())
            self.assertEqual(first_sidecar.read_text(), third_sidecar.read_text())
            self.assertNotEqual(first_summary["source_ref"], third_summary["source_ref"])

            active_branch = git(repo, "branch", "--show-current")
            git(repo, "checkout", "-qb", "main")
            with self.assertRaises(BUILDER.BuildError):
                BUILDER.build_bundle(
                    repo_root=repo,
                    requested_commit="HEAD",
                    output_dir=base / "default-branch-output",
                    generated_date="2026-08-30",
                    require_upstream=False,
                )
            git(repo, "checkout", "-q", active_branch)
            git(repo, "checkout", "-q", "--detach", "HEAD")
            with self.assertRaises(BUILDER.BuildError):
                BUILDER.build_bundle(
                    repo_root=repo,
                    requested_commit="HEAD",
                    output_dir=base / "detached-head-output",
                    generated_date="2026-08-30",
                    require_upstream=False,
                )
            git(repo, "checkout", "-q", active_branch)

            with zipfile.ZipFile(first_zip) as archive:
                names = archive.namelist()
                self.assertEqual(len(names), len(set(names)))
                roots = {name.split("/", 1)[0] for name in names if name}
                self.assertEqual(roots, {f"Pattern-Map-v16-{commit[:12]}"})
                self.assertIsNone(archive.testzip())

            valid_copy = base / "valid-copy"
            root = extract(first_zip, valid_copy)
            completed = run([sys.executable, "VERIFY_PACKAGE.py"], cwd=root)
            self.assertEqual(completed.returncode, 0, completed.stdout)
            self.assertIn("PASS complete extracted owner bundle", completed.stdout)
            metadata = json.loads((root / "PACKAGE_METADATA.json").read_text())
            self.assertNotIn("source_ref", metadata)

            mutation_cases = [
                "byte",
                "extra",
                "extra-dir",
                "missing",
                "symlink",
                "duplicate-json",
                "nonfinite",
                "metadata-status",
                "metadata-schema-boolean",
                "metadata-invalid-date",
                "metadata-extra-key",
                "metadata-missing-key",
                "metadata-manual-gate",
                "manifest-status",
                "manifest-schema-boolean",
                "manifest-extra-key",
                "manifest-missing-key",
                "control-byte",
            ]
            for mutation in mutation_cases:
                with self.subTest(mutation=mutation):
                    destination = base / f"mutated-{mutation}"
                    extracted = extract(first_zip, destination)
                    readme = extracted / "repository" / "README.md"
                    if mutation == "byte":
                        readme.write_bytes(readme.read_bytes() + b"x")
                    elif mutation == "extra":
                        (extracted / "repository" / "EXTRA.txt").write_text("extra\n")
                    elif mutation == "extra-dir":
                        (extracted / "repository" / "EMPTY_EXTRA").mkdir()
                    elif mutation == "missing":
                        readme.unlink()
                    elif mutation == "symlink":
                        readme.unlink()
                        try:
                            readme.symlink_to(extracted / "PACKAGE_METADATA.json")
                        except (OSError, NotImplementedError):
                            continue
                    elif mutation == "duplicate-json":
                        path = extracted / "FULL_PAYLOAD_MANIFEST.json"
                        raw = path.read_text()
                        path.write_text(
                            raw.replace(
                                '"schema_version": 1',
                                '"schema_version": 1, "schema_version": 1',
                                1,
                            )
                        )
                    elif mutation == "nonfinite":
                        path = extracted / "FULL_PAYLOAD_MANIFEST.json"
                        raw = path.read_text()
                        path.write_text(
                            re.sub(r'"file_count": \d+', '"file_count": NaN', raw, count=1)
                        )
                    elif mutation.startswith("metadata-"):
                        path = extracted / "PACKAGE_METADATA.json"
                        payload = json.loads(path.read_text())
                        if mutation == "metadata-status":
                            payload["status"] = "released and owner-approved"
                        elif mutation == "metadata-schema-boolean":
                            payload["schema_version"] = True
                        elif mutation == "metadata-invalid-date":
                            payload["generated_date"] = "2026-99-99"
                        elif mutation == "metadata-extra-key":
                            payload["authorized"] = True
                        elif mutation == "metadata-missing-key":
                            del payload["prohibited_actions"]
                        elif mutation == "metadata-manual-gate":
                            payload["manual_gates"] = []
                        path.write_text(json.dumps(payload) + "\n", encoding="utf-8")
                    elif mutation.startswith("manifest-"):
                        path = extracted / "FULL_PAYLOAD_MANIFEST.json"
                        payload = json.loads(path.read_text())
                        if mutation == "manifest-status":
                            payload["status"] = "released and owner-approved"
                        elif mutation == "manifest-schema-boolean":
                            payload["schema_version"] = True
                        elif mutation == "manifest-extra-key":
                            payload["authorized"] = True
                        elif mutation == "manifest-missing-key":
                            del payload["control_files"]
                        path.write_text(json.dumps(payload) + "\n", encoding="utf-8")
                    elif mutation == "control-byte":
                        start = extracted / "START_HERE.md"
                        start.write_bytes(start.read_bytes() + b"\nmutated control\n")
                    failed = run([sys.executable, "VERIFY_PACKAGE.py"], cwd=extracted)
                    self.assertNotEqual(failed.returncode, 0, failed.stdout)

            with self.assertRaises(BUILDER.BuildError):
                BUILDER.build_bundle(
                    repo_root=repo,
                    requested_commit="HEAD",
                    output_dir=first_zip.parent,
                    generated_date="2026-08-30",
                    require_upstream=False,
                )
            with self.assertRaises(BUILDER.BuildError):
                BUILDER.build_bundle(
                    repo_root=repo,
                    requested_commit="HEAD^",
                    output_dir=base / "old-head",
                    generated_date="2026-08-30",
                    require_upstream=False,
                )
            with self.assertRaises(BUILDER.BuildError):
                BUILDER.build_bundle(
                    repo_root=repo,
                    requested_commit="HEAD",
                    output_dir=base / "invalid-date",
                    generated_date="2026-99-99",
                    require_upstream=False,
                )
            with self.assertRaises(BUILDER.BuildError):
                BUILDER.build_bundle(
                    repo_root=repo,
                    requested_commit="HEAD",
                    output_dir=repo / "forbidden-output",
                    generated_date="2026-08-30",
                    require_upstream=False,
                )
            with self.assertRaises(BUILDER.BuildError):
                BUILDER.build_bundle(
                    repo_root=repo,
                    requested_commit="HEAD",
                    output_dir=base / "missing-upstream",
                    generated_date="2026-08-30",
                    require_upstream=True,
                )

            symlink = repo / "committed-link"
            try:
                symlink.symlink_to("README.md")
            except (OSError, NotImplementedError):
                pass
            else:
                git(repo, "add", "committed-link")
                git(repo, "commit", "-qm", "committed symlink fixture")
                with self.assertRaises(BUILDER.BuildError):
                    BUILDER.build_bundle(
                        repo_root=repo,
                        requested_commit="HEAD",
                        output_dir=base / "symlink-tree-output",
                        generated_date="2026-08-30",
                        require_upstream=False,
                    )
            (repo / "dirty.txt").write_text("dirty\n", encoding="utf-8")
            with self.assertRaises(BUILDER.BuildError):
                BUILDER.build_bundle(
                    repo_root=repo,
                    requested_commit="HEAD",
                    output_dir=base / "dirty-output",
                    generated_date="2026-08-30",
                    require_upstream=False,
                )

    def test_zip_safety_rejects_unsafe_duplicate_and_symlink_entries(self) -> None:
        with tempfile.TemporaryDirectory(prefix="owner-zip-safety-") as temporary:
            root = Path(temporary)
            cases: dict[str, list[zipfile.ZipInfo | str]] = {
                "unsafe": ["Bundle/../escape.txt"],
                "duplicate": ["Bundle/file.txt", "Bundle/file.txt"],
            }
            for name, entries in cases.items():
                with self.subTest(name=name):
                    path = root / f"{name}.zip"
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore", UserWarning)
                        with zipfile.ZipFile(path, "w") as archive:
                            for entry in entries:
                                archive.writestr(entry, b"x")
                    with self.assertRaises(BUILDER.BuildError):
                        BUILDER.assert_zip_safe(path, root_name="Bundle")

            symlink_zip = root / "symlink.zip"
            symlink = zipfile.ZipInfo("Bundle/link")
            symlink.create_system = 3
            symlink.external_attr = 0o120777 << 16
            with zipfile.ZipFile(symlink_zip, "w") as archive:
                archive.writestr(symlink, b"target")
            with self.assertRaises(BUILDER.BuildError):
                BUILDER.assert_zip_safe(symlink_zip, root_name="Bundle")

            fifo_zip = root / "fifo.zip"
            fifo = zipfile.ZipInfo("Bundle/fifo")
            fifo.create_system = 3
            fifo.external_attr = (stat.S_IFIFO | 0o644) << 16
            with zipfile.ZipFile(fifo_zip, "w") as archive:
                archive.writestr(fifo, b"not really a fifo")
            with self.assertRaises(BUILDER.BuildError):
                BUILDER.assert_zip_safe(fifo_zip, root_name="Bundle")

    def test_path_and_secret_guards(self) -> None:
        for relative in (
            "../escape",
            "site/dist/output.html",
            ".env",
            ".netrc",
            ".pypirc",
            "keys/private.pem",
            "nested/name:stream",
            "nested/CON.txt",
            "nested/trailing.",
            "nested/what?.md",
            "nested/control\x01.md",
        ):
            with self.subTest(relative=relative):
                with self.assertRaises(BUILDER.BuildError):
                    BUILDER.safe_repository_path(relative)
        BUILDER.safe_repository_path(
            "archive/transfers/v14-complete-2026-08-18/tools/__pycache__/historical.pyc"
        )
        with self.assertRaises(BUILDER.BuildError):
            BUILDER.assert_payload_bytes_safe(
                "payload.txt", b"-----BEGIN " + b"PRIVATE KEY-----\nsecret"
            )
        portable_fixture_path = "qa/handoff/test_portable_bundle.py"
        portable_fixture = (REPOSITORY_ROOT / portable_fixture_path).read_bytes()
        BUILDER.assert_payload_bytes_safe(portable_fixture_path, portable_fixture)
        with self.assertRaises(BUILDER.BuildError):
            BUILDER.assert_payload_bytes_safe(
                portable_fixture_path, portable_fixture + b"\nbyte drift"
            )
        with self.assertRaises(BUILDER.BuildError):
            BUILDER.assert_payload_bytes_safe(
                "qa/handoff/copied_fixture.py", portable_fixture
            )
        composed = "unicode/\u00c5.md"
        decomposed = "unicode/A\u030a.md"
        self.assertEqual(
            BUILDER.portable_path_key(composed), BUILDER.portable_path_key(decomposed)
        )
        fake_tree = (
            f"100644 blob {'0' * 40}\t{composed}\0"
            f"100644 blob {'1' * 40}\t{decomposed}\0"
        ).encode("utf-8")
        with mock.patch.object(BUILDER, "run_git", return_value=fake_tree):
            with self.assertRaises(BUILDER.BuildError):
                BUILDER.parse_tree(Path("/unused"), "0" * 40)

    def test_production_exact_head_tree_passes_path_and_payload_preflight(self) -> None:
        commit = git(REPOSITORY_ROOT, "rev-parse", "HEAD")
        tree = BUILDER.parse_tree(REPOSITORY_ROOT, commit)
        blobs = BUILDER.git_blobs(
            REPOSITORY_ROOT, [object_id for _path, _mode, object_id in tree]
        )
        for relative, _mode, object_id in tree:
            BUILDER.assert_payload_bytes_safe(
                relative, blobs[object_id]
            )

    def test_stale_bounded_manifest_and_changed_owner_intent_block_build(self) -> None:
        with tempfile.TemporaryDirectory(prefix="owner-stale-bounded-") as temporary:
            base = Path(temporary)
            stale_repo = base / "stale-repo"
            stale_repo.mkdir()
            initialize_repository(stale_repo)
            (stale_repo / "README.md").write_text(
                "changed after bounded seal\n", encoding="utf-8"
            )
            git(stale_repo, "add", "README.md")
            git(stale_repo, "commit", "-qm", "stale bounded fixture")
            with self.assertRaisesRegex(
                BUILDER.BuildError, "bounded owner-review manifest failed"
            ):
                BUILDER.build_bundle(
                    repo_root=stale_repo,
                    requested_commit="HEAD",
                    output_dir=base / "stale-output",
                    generated_date="2026-08-30",
                    require_upstream=False,
                )

            identity_repo = base / "identity-repo"
            identity_repo.mkdir()
            initialize_repository(identity_repo)
            (identity_repo / "docs" / "OWNER_INTENT_V16.md").write_text(
                "not the locked Pattern Map owner intent\n", encoding="utf-8"
            )
            git(identity_repo, "add", "docs/OWNER_INTENT_V16.md")
            git(identity_repo, "commit", "-qm", "wrong owner identity fixture")
            with self.assertRaisesRegex(
                BUILDER.BuildError, "locked Pattern Map v16 owner intent"
            ):
                BUILDER.build_bundle(
                    repo_root=identity_repo,
                    requested_commit="HEAD",
                    output_dir=base / "identity-output",
                    generated_date="2026-08-30",
                    require_upstream=False,
                )

            verifier_repo = base / "hostile-verifier-repo"
            verifier_repo.mkdir()
            initialize_repository(verifier_repo)
            hostile_verifier = (
                verifier_repo / "handoff" / "verify_extracted_owner_bundle.py"
            )
            hostile_verifier.write_text(
                "#!/usr/bin/env python3\nprint('PASS STUB — no bytes checked')\n",
                encoding="utf-8",
            )
            bounded = load_module(
                f"hostile_bounded_{os.urandom(4).hex()}",
                verifier_repo / "handoff" / "verify_owner_review_package.py",
            )
            bounded.ROOT = verifier_repo
            bounded.MANIFEST = (
                verifier_repo / "handoff" / "OWNER_REVIEW_MANIFEST_V16.json"
            )
            records = bounded.current_records()
            bounded.MANIFEST.write_text(
                json.dumps(bounded_manifest_payload(bounded, records), indent=2)
                + "\n",
                encoding="utf-8",
            )
            git(verifier_repo, "add", ".")
            git(verifier_repo, "commit", "-qm", "hostile extracted verifier fixture")
            with self.assertRaisesRegex(
                BUILDER.BuildError, "extracted verifier differs"
            ):
                BUILDER.build_bundle(
                    repo_root=verifier_repo,
                    requested_commit="HEAD",
                    output_dir=base / "hostile-verifier-output",
                    generated_date="2026-08-30",
                    require_upstream=False,
                )

    def test_output_races_preserve_unowned_targets_and_clean_owned_partial(self) -> None:
        with tempfile.TemporaryDirectory(prefix="owner-output-race-") as temporary:
            base = Path(temporary)
            repo = base / "repo"
            repo.mkdir()
            commit = initialize_repository(repo)
            zip_name = f"PATTERN_MAP_V16_OWNER_REVIEW_2026-08-30_{commit[:12]}.zip"

            for race_kind in ("both", "sidecar-only"):
                with self.subTest(race_kind=race_kind):
                    output = base / race_kind
                    output.mkdir()
                    final_zip = output / zip_name
                    final_sidecar = output / f"{zip_name}.sha256"
                    original_verify = BUILDER.verify_copied_extraction

                    def inject_race(zip_path: Path, *, root_name: str) -> str:
                        result = original_verify(zip_path, root_name=root_name)
                        if race_kind == "both":
                            final_zip.write_bytes(b"unowned zip sentinel")
                        final_sidecar.write_bytes(b"unowned sidecar sentinel")
                        return result

                    with mock.patch.object(
                        BUILDER,
                        "verify_copied_extraction",
                        side_effect=inject_race,
                    ):
                        with self.assertRaises(BUILDER.BuildError):
                            BUILDER.build_bundle(
                                repo_root=repo,
                                requested_commit="HEAD",
                                output_dir=output,
                                generated_date="2026-08-30",
                                require_upstream=False,
                            )
                    if race_kind == "both":
                        self.assertEqual(final_zip.read_bytes(), b"unowned zip sentinel")
                    else:
                        self.assertFalse(
                            final_zip.exists(), "owned partial ZIP survived sidecar race"
                        )
                    self.assertEqual(
                        final_sidecar.read_bytes(), b"unowned sidecar sentinel"
                    )
                    self.assertEqual(list(output.glob(".*.building-*")), [])
                    self.assertEqual(list(output.glob(".*.lock")), [])

            direct_source = base / "direct-source"
            direct_destination = base / "direct-destination"
            direct_source.write_bytes(b"owned source")
            direct_source_stat = direct_source.lstat()
            real_link = os.link

            def swap_source_before_link(source, destination, *, follow_symlinks=False):
                Path(source).unlink()
                Path(source).write_bytes(b"foreign replacement")
                return real_link(
                    source,
                    destination,
                    follow_symlinks=follow_symlinks,
                )

            with mock.patch.object(
                BUILDER.os, "link", side_effect=swap_source_before_link
            ):
                with self.assertRaisesRegex(
                    BUILDER.BuildError, "did not bind the expected inode"
                ):
                    BUILDER.publish_exclusive(
                        direct_source, direct_destination, direct_source_stat
                    )
            self.assertEqual(
                direct_destination.read_bytes(), b"foreign replacement"
            )

            replaced_output = base / "replaced-after-zip-publish"
            replaced_output.mkdir()
            replaced_zip = replaced_output / zip_name
            replaced_sidecar = replaced_output / f"{zip_name}.sha256"
            original_publish = BUILDER.publish_exclusive

            def replace_after_zip_publish(source, destination, source_stat):
                published = original_publish(source, destination, source_stat)
                if Path(destination).suffix == ".zip":
                    Path(destination).unlink()
                    Path(destination).write_bytes(b"foreign final zip")
                return published

            with mock.patch.object(
                BUILDER,
                "publish_exclusive",
                side_effect=replace_after_zip_publish,
            ):
                with self.assertRaisesRegex(
                    BUILDER.BuildError, "changed before read"
                ):
                    BUILDER.build_bundle(
                        repo_root=repo,
                        requested_commit="HEAD",
                        output_dir=replaced_output,
                        generated_date="2026-08-30",
                        require_upstream=False,
                    )
            self.assertEqual(replaced_zip.read_bytes(), b"foreign final zip")
            self.assertFalse(replaced_sidecar.exists())
            self.assertEqual(list(replaced_output.glob(".*.building-*")), [])
            self.assertEqual(list(replaced_output.glob(".*.lock")), [])

    def test_full_runner_fails_fast_without_git_and_points_to_package_mode(self) -> None:
        with tempfile.TemporaryDirectory(prefix="owner-no-git-runner-") as temporary:
            root = Path(temporary)
            (root / "qa").mkdir()
            (root / "handoff").mkdir()
            shutil.copy2(
                REPOSITORY_ROOT / "qa" / "run_owner_review_checks.sh",
                root / "qa" / "run_owner_review_checks.sh",
            )
            shutil.copy2(
                REPOSITORY_ROOT / "handoff" / "START_HERE_OWNER_REVIEW.md",
                root / "handoff" / "START_HERE_OWNER_REVIEW.md",
            )
            completed = run(["sh", "qa/run_owner_review_checks.sh"], cwd=root)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("requires a Git clone/worktree", completed.stdout)
            self.assertIn("--extracted-package", completed.stdout)
            self.assertIn("handoff/START_HERE_OWNER_REVIEW.md", completed.stdout)
            runner_text = (
                REPOSITORY_ROOT / "qa" / "run_owner_review_checks.sh"
            ).read_text(encoding="utf-8")
            self.assertIn(
                "git status --porcelain=v1 --untracked-files=all", runner_text
            )
            self.assertLess(
                runner_text.index("qa_initial_dirty_state="),
                runner_text.index("[1/12] Locked owner intent"),
            )
            self.assertLess(
                runner_text.index("[1/12] Locked owner intent"),
                runner_text.index("qa_dirty_state="),
            )
            start_text = (
                REPOSITORY_ROOT / "handoff" / "START_HERE_OWNER_REVIEW.md"
            ).read_text(encoding="utf-8")
            self.assertIn(
                "sh qa/run_owner_review_checks.sh --extracted-package", start_text
            )

            parent = root / "enclosing-repository"
            bundle = parent / "received-bundle"
            (bundle / "qa").mkdir(parents=True)
            (bundle / "handoff").mkdir()
            git(parent, "init", "-q")
            shutil.copy2(
                REPOSITORY_ROOT / "qa" / "run_owner_review_checks.sh",
                bundle / "qa" / "run_owner_review_checks.sh",
            )
            shutil.copy2(
                REPOSITORY_ROOT / "handoff" / "START_HERE_OWNER_REVIEW.md",
                bundle / "handoff" / "START_HERE_OWNER_REVIEW.md",
            )
            nested = run(["sh", "qa/run_owner_review_checks.sh"], cwd=bundle)
            self.assertNotEqual(nested.returncode, 0)
            self.assertIn("requires a Git clone/worktree", nested.stdout)
            self.assertIn("--extracted-package", nested.stdout)
            self.assertNotIn("[1/12]", nested.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
