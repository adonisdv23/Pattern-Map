"""Strict, write-once parser for the four-field model output contract."""

from __future__ import annotations

import base64
import hashlib
import json
import math
import re
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from .config import FrozenConfig


REPORT_ID_RE = re.compile(r"^RP-[A-Z2-7]{10}$")
ALLOWED_KEYS = {
    "origin_count_supporting",
    "claim_state",
    "confidence",
    "evidence_ids",
}
CLAIM_STATES = {"supported", "refuted", "insufficient", "contested"}
ERROR_CODES = {
    "NONE",
    "TIMEOUT",
    "CANCELLED",
    "BACKEND_ERROR",
    "EMPTY_OUTPUT",
    "INVALID_UTF8",
    "INVALID_JSON",
    "DUPLICATE_KEY",
    "SCHEMA_ERROR",
    "SEMANTIC_ERROR",
    "UNKNOWN_EVIDENCE_ID",
}


class DuplicateKeyError(ValueError):
    pass


def _pairs_no_duplicates(pairs: List[Tuple[str, Any]]) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise DuplicateKeyError(key)
        output[key] = value
    return output


@dataclass(frozen=True)
class ParseResult:
    parse_status: str
    error_code: str
    parsed: Optional[Dict[str, Any]]
    raw_sha256: str
    byte_length: int

    @property
    def valid(self) -> bool:
        return self.parse_status == "valid" and self.parsed is not None


def _failure(status: str, code: str, raw: bytes) -> ParseResult:
    if code not in ERROR_CODES:
        raise ValueError("unknown parser error code: %s" % code)
    return ParseResult(status, code, None, hashlib.sha256(raw).hexdigest(), len(raw))


def parse_output(raw: bytes, bundle_report_ids: Iterable[str], config: Optional[FrozenConfig] = None) -> ParseResult:
    """Parse one immutable raw byte string; never repair or retry it."""

    config = config or FrozenConfig()
    digest = hashlib.sha256(raw).hexdigest()
    if not raw:
        return _failure("empty_output", "EMPTY_OUTPUT", raw)
    try:
        decoded = raw.decode("utf-8")
    except UnicodeDecodeError:
        return _failure("invalid_utf8", "INVALID_UTF8", raw)
    stripped = decoded.strip(" \t\r\n")
    if not stripped:
        return _failure("empty_output", "EMPTY_OUTPUT", raw)
    try:
        value = json.loads(
            stripped,
            object_pairs_hook=_pairs_no_duplicates,
            parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)),
        )
    except DuplicateKeyError:
        return _failure("invalid_json", "DUPLICATE_KEY", raw)
    except (TypeError, ValueError, json.JSONDecodeError):
        return _failure("invalid_json", "INVALID_JSON", raw)
    if not isinstance(value, dict):
        return _failure("schema_error", "SCHEMA_ERROR", raw)
    if set(value) != ALLOWED_KEYS:
        return _failure("schema_error", "SCHEMA_ERROR", raw)
    origin_count = value.get("origin_count_supporting")
    if isinstance(origin_count, bool) or not isinstance(origin_count, int) or not 0 <= origin_count <= config.max_evidence_ids:
        return _failure("schema_error", "SCHEMA_ERROR", raw)
    claim_state = value.get("claim_state")
    if not isinstance(claim_state, str) or claim_state not in CLAIM_STATES:
        return _failure("schema_error", "SCHEMA_ERROR", raw)
    confidence = value.get("confidence")
    if isinstance(confidence, bool) or not isinstance(confidence, (int, float)):
        return _failure("schema_error", "SCHEMA_ERROR", raw)
    if not math.isfinite(float(confidence)) or not 0 <= float(confidence) <= 1:
        return _failure("schema_error", "SCHEMA_ERROR", raw)
    evidence_ids = value.get("evidence_ids")
    if not isinstance(evidence_ids, list) or len(evidence_ids) > config.max_evidence_ids:
        return _failure("schema_error", "SCHEMA_ERROR", raw)
    if any(not isinstance(evidence_id, str) for evidence_id in evidence_ids):
        return _failure("schema_error", "SCHEMA_ERROR", raw)
    if len(evidence_ids) != len(set(evidence_ids)):
        return _failure("semantic_error", "SEMANTIC_ERROR", raw)
    report_ids = set(bundle_report_ids)
    for evidence_id in evidence_ids:
        if not isinstance(evidence_id, str) or not REPORT_ID_RE.match(evidence_id):
            return _failure("schema_error", "SCHEMA_ERROR", raw)
        if evidence_id not in report_ids:
            return _failure("semantic_error", "UNKNOWN_EVIDENCE_ID", raw)
    parsed = {
        "origin_count_supporting": origin_count,
        "claim_state": claim_state,
        "confidence": float(confidence),
        "evidence_ids": list(evidence_ids),
    }
    return ParseResult("valid", "NONE", parsed, digest, len(raw))


def raw_output_record(run_id: str, raw: bytes, result: ParseResult) -> Dict[str, Any]:
    """Create an immutable raw-output receipt without exposing decoded text."""

    digest = hashlib.sha256(raw).hexdigest()
    if result.raw_sha256 != digest or result.byte_length != len(raw):
        raise ValueError("ParseResult does not describe the supplied raw bytes")

    return {
        "run_id": run_id,
        "raw_output_b64": base64.b64encode(raw).decode("ascii"),
        "byte_length": len(raw),
        "raw_output_sha256": result.raw_sha256,
        "parse_status": result.parse_status,
        "error_code": result.error_code,
    }


def validate_raw_output_record(record: Mapping[str, Any]) -> None:
    """Fail closed on base64/length/hash consistency in a raw receipt."""

    required = {
        "run_id",
        "raw_output_b64",
        "byte_length",
        "raw_output_sha256",
        "parse_status",
        "error_code",
    }
    missing = required - set(record)
    if missing:
        raise ValueError("raw-output receipt is missing fields: %s" % sorted(missing))
    if not isinstance(record["raw_output_b64"], str):
        raise ValueError("raw_output_b64 must be a string")
    try:
        raw = base64.b64decode(record["raw_output_b64"].encode("ascii"), validate=True)
    except (ValueError, UnicodeEncodeError) as exc:
        raise ValueError("raw_output_b64 is not strict base64") from exc
    if base64.b64encode(raw).decode("ascii") != record["raw_output_b64"]:
        raise ValueError("raw_output_b64 is not canonical base64")
    if not isinstance(record["byte_length"], int) or isinstance(record["byte_length"], bool):
        raise ValueError("raw-output byte_length must be an integer")
    if record["byte_length"] != len(raw):
        raise ValueError("raw-output byte_length does not match decoded bytes")
    if record["raw_output_sha256"] != hashlib.sha256(raw).hexdigest():
        raise ValueError("raw-output hash does not match decoded bytes")
    if record["error_code"] not in ERROR_CODES:
        raise ValueError("raw-output error code is not in the parser codebook")
    if record["parse_status"] not in {
        "valid",
        "invalid_utf8",
        "invalid_json",
        "schema_error",
        "semantic_error",
        "runtime_error",
        "timeout",
        "empty_output",
        "cancelled",
    }:
        raise ValueError("raw-output parse status is not in the receipt codebook")
    if record["parse_status"] == "valid" and record["error_code"] != "NONE":
        raise ValueError("valid raw output must have error_code NONE")


RUN_STATUSES = {"completed", "runtime_error", "timeout", "cancelled"}
RUN_ERROR_CODES = ERROR_CODES | {"NONE"}


def validate_run_record(record: Mapping[str, Any]) -> None:
    """Validate the offline run-audit fields required by the protocol."""

    required = {
        "run_id",
        "prompt_instance_id",
        "bundle_id",
        "condition",
        "model_id",
        "model_revision",
        "tokenizer_revision",
        "decoder",
        "chat_template",
        "runtime",
        "dependency_hashes",
        "hardware",
        "seed",
        "started_at_utc",
        "status",
        "input_tokens",
        "input_byte_length",
        "output_tokens",
        "latency_ms",
        "cpu_ms",
        "gpu_ms",
        "peak_memory_mb",
        "system_prompt_sha256",
        "user_prompt_sha256",
        "final_input_sha256",
        "raw_output_sha256",
        "error_code",
    }
    missing = required - set(record)
    if missing:
        raise ValueError("run receipt is missing fields: %s" % sorted(missing))
    if record["condition"] not in {"F0", "F1", "F2"}:
        raise ValueError("run receipt condition is invalid")
    if record["status"] not in RUN_STATUSES:
        raise ValueError("run receipt status is invalid")
    if record["error_code"] not in RUN_ERROR_CODES:
        raise ValueError("run receipt error code is invalid")
    for field in ("input_tokens", "input_byte_length", "output_tokens"):
        if not isinstance(record[field], int) or isinstance(record[field], bool) or record[field] < 0:
            raise ValueError("run receipt %s must be a nonnegative integer" % field)
    for field in ("latency_ms", "cpu_ms", "gpu_ms", "peak_memory_mb"):
        value = record[field]
        if value is not None and (isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0):
            raise ValueError("run receipt %s must be nonnegative or null" % field)
    for field in ("system_prompt_sha256", "user_prompt_sha256", "final_input_sha256"):
        if not isinstance(record[field], str) or not re.match(r"^[a-f0-9]{64}$", record[field]):
            raise ValueError("run receipt %s must be a SHA-256 hex digest" % field)
    raw_digest = record["raw_output_sha256"]
    if raw_digest is not None and (not isinstance(raw_digest, str) or not re.match(r"^[a-f0-9]{64}$", raw_digest)):
        raise ValueError("run receipt raw_output_sha256 must be a digest or null")
    for field in ("decoder", "runtime", "dependency_hashes", "hardware"):
        if not isinstance(record[field], Mapping):
            raise ValueError("run receipt %s must be an object" % field)
    if record["status"] == "completed" and raw_digest is None:
        raise ValueError("completed run must link a raw-output digest")


def parser_fixture_cases() -> List[Tuple[str, bytes, str, str]]:
    """Return strict parser fixtures used by offline tests.

    IDs are syntactically valid but not tied to any generated corpus.  The
    caller supplies membership when checking unknown-ID behavior.
    """

    good = b'{"origin_count_supporting":1,"claim_state":"supported","confidence":0.5,"evidence_ids":[]}'
    return [
        ("valid", good, "valid", "NONE"),
        ("fenced", b"```json\n" + good + b"\n```", "invalid_json", "INVALID_JSON"),
        ("leading_prose", b"Here is the result: " + good, "invalid_json", "INVALID_JSON"),
        ("trailing_prose", good + b" trailing", "invalid_json", "INVALID_JSON"),
        ("duplicate_key", b'{"origin_count_supporting":1,"origin_count_supporting":2,"claim_state":"supported","confidence":0.5,"evidence_ids":[]}', "invalid_json", "DUPLICATE_KEY"),
        ("unknown_key", b'{"origin_count_supporting":1,"claim_state":"supported","confidence":0.5,"evidence_ids":[],"extra":1}', "schema_error", "SCHEMA_ERROR"),
        ("wrong_type", b'{"origin_count_supporting":"1","claim_state":"supported","confidence":0.5,"evidence_ids":[]}', "schema_error", "SCHEMA_ERROR"),
        ("nan", b'{"origin_count_supporting":1,"claim_state":"supported","confidence":NaN,"evidence_ids":[]}', "invalid_json", "INVALID_JSON"),
        ("infinity", b'{"origin_count_supporting":1,"claim_state":"supported","confidence":Infinity,"evidence_ids":[]}', "invalid_json", "INVALID_JSON"),
        ("too_many_ids", b'{"origin_count_supporting":1,"claim_state":"supported","confidence":0.5,"evidence_ids":["RP-AAAAAAAAAA","RP-BBBBBBBBBB","RP-CCCCCCCCCC","RP-DDDDDDDDDD","RP-EEEEEEEEEE","RP-FFFFFFFFFF","RP-GGGGGGGGGG"]}', "schema_error", "SCHEMA_ERROR"),
        ("duplicate_ids", b'{"origin_count_supporting":1,"claim_state":"supported","confidence":0.5,"evidence_ids":["RP-AAAAAAAAAA","RP-AAAAAAAAAA"]}', "semantic_error", "SEMANTIC_ERROR"),
        ("unknown_id", b'{"origin_count_supporting":1,"claim_state":"supported","confidence":0.5,"evidence_ids":["RP-AAAAAAAAAA"]}', "semantic_error", "UNKNOWN_EVIDENCE_ID"),
        ("negative_count", b'{"origin_count_supporting":-1,"claim_state":"supported","confidence":0.5,"evidence_ids":[]}', "schema_error", "SCHEMA_ERROR"),
        ("confidence_string", b'{"origin_count_supporting":1,"claim_state":"supported","confidence":"0.5","evidence_ids":[]}', "schema_error", "SCHEMA_ERROR"),
        ("multiple_objects", good + b"\n" + good, "invalid_json", "INVALID_JSON"),
        ("empty", b"", "empty_output", "EMPTY_OUTPUT"),
        ("whitespace", b" \n\t", "empty_output", "EMPTY_OUTPUT"),
        ("malformed_utf8", b"\xff\xfe", "invalid_utf8", "INVALID_UTF8"),
    ]
