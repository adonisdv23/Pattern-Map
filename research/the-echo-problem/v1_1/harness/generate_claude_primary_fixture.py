#!/usr/bin/env python3
"""Materialize a byte-preserved, provider-free render audit fixture.

This build-only utility reads the advisory Claude package from an explicitly
provided local checkout.  It copies rendered prompt bytes and provenance
hashes, not package code, into a deterministic fixture.  The fixture is then
audited without importing the advisory package.  No model, provider, network,
corpus, or participant path exists in this script.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import sys
from pathlib import Path
from typing import Any


ARCHIVE_SHA256 = "b544b734324699a93abbb8cf0bcef3d61cc590ff7b603fc167a46b8f8539a253"
EXTERNAL_AUDIT_RECEIPT_SHA256 = "6d1fb03ec419511ce7aef652f85d3713030f958edb2e152bf08db2958f86fb68"
ENCODING_FINGERPRINT = "5af8a02a651e9db4366b5b14c2cc8f506d721ebdab0db3294337dd8ba15c4528"


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def source_hash(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def tokenizer_fingerprint(tokenizer: Any) -> str:
    payload = {
        "mergeable_ranks": sorted((key.hex(), value) for key, value in tokenizer._mergeable_ranks.items()),
        "special_tokens": sorted(tokenizer._special_tokens.items()),
        "pat_str": tokenizer._pat_str,
    }
    return sha256_bytes(canonical_bytes(payload))


def report_metadata(bundle: Any) -> tuple[list[str], list[str], str]:
    ids = [str(report.report_id) for report in bundle.reports]
    hashes = [sha256_bytes(str(report.text).encode("utf-8")) for report in bundle.reports]
    return ids, hashes, sha256_bytes(canonical_bytes(hashes))


def build_fixture(package_root: Path, archive_path: Path, output: Path) -> None:
    generator_path = package_root / "oa" / "generate.py"
    conditions_path = package_root / "oa" / "conditions.py"
    if not generator_path.is_file() or not conditions_path.is_file():
        raise FileNotFoundError("package root must contain oa/generate.py and oa/conditions.py")
    if not archive_path.is_file():
        raise FileNotFoundError(archive_path)

    sys.path.insert(0, str(package_root))
    try:
        generate = importlib.import_module("oa.generate")
        conditions = importlib.import_module("oa.conditions")
        import tiktoken

        tokenizer = tiktoken.get_encoding("cl100k_base")
        bundles = generate.generate_set(300, seed=1)
        pairs: list[dict[str, Any]] = []
        for bundle in bundles:
            f1 = conditions.render(bundle, "F1")
            f2 = conditions.render(bundle, "F2")
            ids, hashes, report_hash = report_metadata(bundle)
            pairs.append(
                {
                    "bundle_id": str(bundle.bundle_id),
                    "structure": str(bundle.structure),
                    "f1_report_id_order": ids,
                    "f2_report_id_order": list(ids),
                    "f1_report_text_hash_sequence": hashes,
                    "f2_report_text_hash_sequence": list(hashes),
                    "f1_report_text_hash_sequence_sha256": report_hash,
                    "f2_report_text_hash_sequence_sha256": report_hash,
                    "f1_render_sha256": sha256_bytes(f1.encode("utf-8")),
                    "f2_render_sha256": sha256_bytes(f2.encode("utf-8")),
                    "f1_base_tokens": len(tokenizer.encode(f1)),
                    "f2_base_tokens": len(tokenizer.encode(f2)),
                    "base_delta_f2_minus_f1": len(tokenizer.encode(f2)) - len(tokenizer.encode(f1)),
                    "f1_text": f1,
                    "f2_text": f2,
                }
            )
    finally:
        sys.path.remove(str(package_root))

    receipt_fields = [
        {
            key: pair[key]
            for key in (
                "bundle_id",
                "f1_report_id_order",
                "f2_report_id_order",
                "f1_report_text_hash_sequence",
                "f2_report_text_hash_sequence",
                "f1_report_text_hash_sequence_sha256",
                "f2_report_text_hash_sequence_sha256",
                "f1_render_sha256",
                "f2_render_sha256",
                "f1_base_tokens",
                "f2_base_tokens",
                "base_delta_f2_minus_f1",
            )
        }
        for pair in pairs
    ]
    deltas = sorted({int(pair["base_delta_f2_minus_f1"]) for pair in pairs})
    manifest = {
        "schema": "EP-v1.1-advisory-render-audit-0.1",
        "status": "offline_fixture_not_research_result",
        "source": {
            "archive_name": "PATTERN_MAP_CLAUDE_SESSION_2026-08-19.zip",
            "archive_sha256": sha256_bytes(archive_path.read_bytes()),
            "package_relative_root": "PATTERN_MAP_CLAUDE_SESSION_2026-08-19/03_CODE/origin-accounting",
            "generator_relative_path": "03_CODE/origin-accounting/oa/generate.py",
            "generator_sha256": source_hash(generator_path),
            "conditions_relative_path": "03_CODE/origin-accounting/oa/conditions.py",
            "conditions_sha256": source_hash(conditions_path),
            "generator_function": "oa.generate.generate_set(n=300, seed=1)",
            "renderer_function": "oa.conditions.render(bundle, condition)",
        },
        "tokenizer": {
            "implementation": "tiktoken",
            "version": tiktoken.__version__,
            "encoding": "cl100k_base",
            "mergeable_ranks": len(tokenizer._mergeable_ranks),
            "encoding_table_fingerprint": tokenizer_fingerprint(tokenizer),
        },
        "audit": {
            "seed": 1,
            "n": 300,
            "conditions": ["F1", "F2"],
            "pair_count": len(pairs),
            "exact_parity_expected": True,
            "base_delta_f2_minus_f1": deltas,
            "padded_count_min": min(max(pair["f1_base_tokens"], pair["f2_base_tokens"]) for pair in pairs),
            "padded_count_max": max(max(pair["f1_base_tokens"], pair["f2_base_tokens"]) for pair in pairs),
            "external_parent_audit_receipt_sha256": EXTERNAL_AUDIT_RECEIPT_SHA256,
        },
        "render_receipt_sha256": sha256_bytes(canonical_bytes(receipt_fields)),
        "pairs": pairs,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package-root", type=Path, required=True)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.archive.name != "PATTERN_MAP_CLAUDE_SESSION_2026-08-19.zip":
        raise ValueError("unexpected advisory archive name")
    if sha256_bytes(args.archive.read_bytes()) != ARCHIVE_SHA256:
        raise ValueError("advisory archive SHA-256 does not match the recorded source")
    build_fixture(args.package_root, args.archive, args.output)


if __name__ == "__main__":
    main()
