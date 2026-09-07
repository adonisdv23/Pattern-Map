"""Strict, no-repair parser for the four-field EP output contract."""

from __future__ import annotations

import base64
import hashlib
import json
import math
from dataclasses import dataclass
from typing import Any, Iterable, Mapping


ERROR_CODES = {
    "NONE",
    "EMPTY_OUTPUT",
    "INVALID_UTF8",
    "INVALID_JSON",
    "DUPLICATE_KEY",
    "SCHEMA_ERROR",
    "SEMANTIC_ERROR",
    "UNKNOWN_EVIDENCE_ID",
}


@dataclass(frozen=True)
class ParseResult:
    valid: bool
    parse_status: str
    error_code: str
    parsed: Mapping[str, Any] | None


class _DuplicateKey(ValueError):
    pass


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateKey(key)
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(value)


def _invalid(status: str, code: str) -> ParseResult:
    return ParseResult(False, status, code, None)


def parse_output(raw: bytes, known_evidence_ids: Iterable[str]) -> ParseResult:
    """Parse raw bytes without extraction, coercion, repair, or retry."""

    if not raw or not raw.strip():
        return _invalid("empty_output", "EMPTY_OUTPUT")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return _invalid("invalid_utf8", "INVALID_UTF8")
    try:
        value = json.loads(
            text,
            object_pairs_hook=_pairs,
            parse_constant=_reject_constant,
        )
    except _DuplicateKey:
        return _invalid("invalid_json", "DUPLICATE_KEY")
    except (TypeError, ValueError, json.JSONDecodeError):
        return _invalid("invalid_json", "INVALID_JSON")
    if not isinstance(value, dict):
        return _invalid("schema_error", "SCHEMA_ERROR")
    required = {
        "origin_count_supporting",
        "claim_state",
        "confidence",
        "evidence_ids",
    }
    if set(value) != required:
        return _invalid("schema_error", "SCHEMA_ERROR")
    count = value["origin_count_supporting"]
    confidence = value["confidence"]
    evidence_ids = value["evidence_ids"]
    if (
        isinstance(count, bool)
        or not isinstance(count, int)
        or count < 0
        or count > 6
    ):
        return _invalid("schema_error", "SCHEMA_ERROR")
    if value["claim_state"] not in {"supported", "refuted", "insufficient", "contested"}:
        return _invalid("schema_error", "SCHEMA_ERROR")
    if (
        isinstance(confidence, bool)
        or not isinstance(confidence, (int, float))
        or not math.isfinite(float(confidence))
        or not 0.0 <= float(confidence) <= 1.0
    ):
        return _invalid("schema_error", "SCHEMA_ERROR")
    if (
        not isinstance(evidence_ids, list)
        or len(evidence_ids) > 6
        or any(not isinstance(item, str) for item in evidence_ids)
        or len(evidence_ids) != len(set(evidence_ids))
    ):
        return _invalid("schema_error", "SCHEMA_ERROR")
    known = set(known_evidence_ids)
    if any(item not in known for item in evidence_ids):
        return _invalid("semantic_error", "UNKNOWN_EVIDENCE_ID")
    return ParseResult(True, "valid", "NONE", value)


def raw_output_receipt(raw: bytes, result: ParseResult) -> dict[str, Any]:
    """Create an immutable local receipt for raw output and parser status."""

    return {
        "raw_output_b64": base64.b64encode(raw).decode("ascii"),
        "byte_length": len(raw),
        "raw_output_sha256": hashlib.sha256(raw).hexdigest(),
        "parse_status": result.parse_status,
        "error_code": result.error_code,
        "repair_applied": False,
        "retry_applied": False,
        "status": "offline_design_receipt",
    }
