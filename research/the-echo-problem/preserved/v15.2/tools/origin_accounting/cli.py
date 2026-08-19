"""Command-line entry points for the offline origin-accounting scaffold."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Sequence

from .analysis import paired_analysis, score_output
from .canonical import canonical_json_bytes, sha256_bytes, sha256_json
from .config import FrozenConfig, frozen_config_sha256, frozen_config_path, load_frozen_config
from .diagnostics import control_receipt
from .generator import Corpus, build_primary_manifest, build_prompt_instances, generate_corpus, validate_corpus
from .parser import parse_output, parser_fixture_cases, raw_output_record
from .power import run_power_simulation


def _write_json(path: Path, value: Any) -> Dict[str, Any]:
    payload = canonical_json_bytes(value) + b"\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    return {"path": str(path), "sha256": sha256_bytes(payload), "bytes": len(payload)}


def _write_jsonl(path: Path, records: Iterable[Mapping[str, Any]]) -> Dict[str, Any]:
    payload = b"".join(canonical_json_bytes(record) + b"\n" for record in records)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    return {"path": str(path), "sha256": sha256_bytes(payload), "bytes": len(payload), "rows": payload.count(b"\n")}


def _corpus_files(out: Path, corpus: Corpus, prompts: Sequence[Mapping[str, Any]]) -> list:
    files = []
    files.append(_write_jsonl(out / "data" / "propositions.jsonl", corpus.propositions))
    files.append(_write_jsonl(out / "data" / "reports.jsonl", corpus.reports))
    files.append(_write_jsonl(out / "data" / "bundles_public.jsonl", corpus.bundles_public))
    files.append(_write_jsonl(out / "data" / "bundles_gold.jsonl", corpus.bundles_gold))
    files.append(_write_jsonl(out / "data" / "provenance_graphs.jsonl", corpus.provenance_graphs))
    files.append(_write_jsonl(out / "data" / "split_index.jsonl", corpus.split_index))
    files.append(_write_jsonl(out / "prompts" / "prompt_instances.jsonl", prompts))
    return files


def _build_smoke_scores(corpus: Corpus) -> Dict[str, Dict[str, Dict[str, Any]]]:
    """Create deterministic local parser/evaluator smoke scores, not results."""

    by_bundle = corpus.by_bundle()
    scores: Dict[str, Dict[str, Dict[str, Any]]] = {"F0": {}, "F1": {}, "F2": {}}
    for bundle_id, bundle in by_bundle.items():
        reports = bundle["reports"]
        evidence = [report["report_id"] for report in reports[:2]]
        raw = json.dumps(
            {
                "origin_count_supporting": 1,
                "claim_state": bundle["gold"]["gold_claim_state"],
                "confidence": 0.5,
                "evidence_ids": evidence,
            },
            separators=(",", ":"),
        ).encode("utf-8")
        result = parse_output(raw, [report["report_id"] for report in reports])
        scored = score_output(result, bundle["gold"], reports)
        for condition in scores:
            scores[condition][bundle_id] = scored
    return scores


def _load_cli_config(config_path: Path = None) -> tuple:
    path = frozen_config_path(config_path)
    config = load_frozen_config(path)
    return config, path, frozen_config_sha256(path)


def run_smoke(out: Path, small: bool = True, config_path: Path = None) -> Dict[str, Any]:
    config, committed_config_path, config_file_digest = _load_cli_config(config_path)
    corpus = generate_corpus(config, small=small)
    prompts = build_prompt_instances(corpus, config)
    validate_corpus(corpus, config)
    files = _corpus_files(out, corpus, prompts)
    receipt = control_receipt(corpus, prompts)
    receipt["config"] = config.to_dict()
    receipt["config_sha256"] = sha256_json(config.to_dict())
    receipt["config_file_sha256"] = config_file_digest
    receipt["config_path"] = str(committed_config_path)
    receipt["files"] = files
    receipt["status"] = "offline_smoke_only"
    receipt["primary_opened"] = False
    receipt["model_calls"] = 0
    receipt["provider_calls"] = 0
    receipt["network_calls"] = 0
    receipt["analysis"] = "not run as efficacy analysis; smoke records only"
    _write_json(out / "receipt.json", receipt)
    return receipt


def run_generate(out: Path, small: bool = False, config_path: Path = None) -> Dict[str, Any]:
    config, committed_config_path, config_file_digest = _load_cli_config(config_path)
    corpus = generate_corpus(config, small=small)
    prompts = build_prompt_instances(corpus, config)
    primary_manifest = None if small else build_primary_manifest(corpus, config)
    files = _corpus_files(out, corpus, prompts)
    if primary_manifest is not None:
        files.append(_write_json(out / "release" / "primary_manifest.json", primary_manifest))
    manifest = {
        "study_id": config.study_id,
        "protocol_version": config.protocol_version,
        "specification_version": config.specification_version,
        "protocol_identity": "origin-accounting-protocol-v1.0",
        "historical_specification_input": config.specification_version,
        "config_path": str(committed_config_path),
        "config_file_sha256": config_file_digest,
        "config_sha256": sha256_json(config.to_dict()),
        "status": "design_only_generated_synthetic_records",
        "primary_n": config.primary_n,
        "generated_bundle_count": len(corpus.bundles_public),
        "model": {"id": config.model_id, "revision": config.model_revision, "tokenizer_revision": config.tokenizer_revision},
        "tokenizer": {"id": config.tokenizer_surrogate_id, "status": config.tokenizer_surrogate_status},
        "conditions": ["F0", "F1", "F2"],
        "primary_contrast": "F2_minus_F1_all_assigned_FC_cons",
        "safety_endpoint": "stipulated_support_origin_recall_fixed_M",
        "data_status": "synthetic_only",
        "canonicalization": "deterministic-json-v1; RFC8785-conformance-required-before-release",
        "owner_release_authorization": False,
        "no_model_or_provider_calls": True,
        "primary_manifest": primary_manifest,
        "manifest_status": "confirmatory_manifest_emitted" if primary_manifest is not None else "descriptive_smoke_only_no_primary_manifest",
        "files": files,
    }
    _write_json(out / "release" / "manifest.json", manifest)
    return manifest


def run_parser_fixtures() -> Dict[str, Any]:
    # Keep A intentionally outside the membership set so the unknown-ID
    # fixture exercises semantic rejection rather than accidental validity.
    expected_ids = {"RP-BBBBBBBBBB", "RP-CCCCCCCCCC", "RP-DDDDDDDDDD", "RP-EEEEEEEEEE", "RP-FFFFFFFFFF"}
    results = []
    for name, raw, expected_status, expected_code in parser_fixture_cases():
        result = parse_output(raw, expected_ids)
        results.append(
            {
                "name": name,
                "expected_status": expected_status,
                "actual_status": result.parse_status,
                "expected_code": expected_code,
                "actual_code": result.error_code,
                "pass": result.parse_status == expected_status and result.error_code == expected_code,
                "raw_output_sha256": result.raw_sha256,
            }
        )
    return {"fixture_count": len(results), "pass": all(item["pass"] for item in results), "results": results}


def main(argv: Sequence[str] = ()) -> int:
    parser = argparse.ArgumentParser(description="Offline F0/F1/F2 origin-accounting scaffolding")
    subparsers = parser.add_subparsers(dest="command")
    smoke = subparsers.add_parser("smoke", help="generate a four-structure offline smoke corpus")
    smoke.add_argument("--out", type=Path, required=True)
    smoke.add_argument("--full", action="store_true", help="emit protocol-sized records; still no model calls")
    smoke.add_argument("--config", type=Path, default=None, help="path to the committed frozen config JSON")
    generate = subparsers.add_parser("generate", help="generate deterministic synthetic records")
    generate.add_argument("--out", type=Path, required=True)
    generate.add_argument("--small", action="store_true")
    generate.add_argument("--config", type=Path, default=None, help="path to the committed frozen config JSON")
    fixtures = subparsers.add_parser("parser-fixtures", help="run strict parser fixtures")
    power = subparsers.add_parser("power", help="run planning-only paired Bernoulli simulation")
    power.add_argument("--out", type=Path, required=True)
    power.add_argument("--repetitions", type=int, default=None)
    power.add_argument("--bootstrap-repetitions", type=int, default=None)
    power.add_argument("--vor-bootstrap-repetitions", type=int, default=None)
    power.add_argument("--vor-n", type=int, action="append", default=None, help="fixed-M size for a reduced planning smoke")
    power.add_argument("--skip-vor", action="store_true")
    power.add_argument("--config", type=Path, default=None, help="path to the committed frozen config JSON")
    args = parser.parse_args(list(argv))
    if args.command == "smoke":
        result = run_smoke(args.out, small=not args.full, config_path=args.config)
    elif args.command == "generate":
        result = run_generate(args.out, small=args.small, config_path=args.config)
    elif args.command == "parser-fixtures":
        result = run_parser_fixtures()
    elif args.command == "power":
        config, committed_config_path, config_file_digest = _load_cli_config(args.config)
        result = run_power_simulation(
            config=config,
            repetitions=args.repetitions,
            bootstrap_repetitions=args.bootstrap_repetitions,
            vor_bootstrap_repetitions=args.vor_bootstrap_repetitions,
            vor_n_values=tuple(args.vor_n) if args.vor_n else (75,),
            include_vor=not args.skip_vor,
        )
        result["config_path"] = str(committed_config_path)
        result["config_file_sha256"] = config_file_digest
        result["config_sha256"] = sha256_json(config.to_dict())
        _write_json(args.out / "analysis" / "power_simulation.json", result)
    else:
        parser.print_help()
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if result.get("pass", True) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
