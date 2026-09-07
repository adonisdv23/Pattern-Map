"""Deterministic JSON and hashing helpers.

The scaffold uses a conservative, dependency-free canonical form for local
receipts.  It rejects non-finite numbers and preserves array order.  It is
intentionally labelled as a local surrogate: a later release must run an
independent RFC 8785 conformance suite before calling its manifest RFC 8785
canonicalized.
"""

from __future__ import annotations

import hashlib
import json
import math
from typing import Any, Mapping


def _reject_nonfinite(value: Any) -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("non-finite JSON number is not allowed")
    if isinstance(value, Mapping):
        for key, child in value.items():
            if not isinstance(key, str):
                raise TypeError("JSON object keys must be strings")
            _reject_nonfinite(child)
    elif isinstance(value, (list, tuple)):
        for child in value:
            _reject_nonfinite(child)


def canonical_json_bytes(value: Any) -> bytes:
    """Serialize JSON deterministically for local hashes.

    `sort_keys`, compact separators, UTF-8 output, and ``allow_nan=False``
    provide stable local bytes.  This does not replace an RFC 8785
    implementation for publication-grade release manifests.
    """

    _reject_nonfinite(value)
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_json(value: Any) -> str:
    return sha256_bytes(canonical_json_bytes(value))


def text_sha256(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def ordered_membership_sha256(values: Any) -> str:
    """Hash an ordered membership list with an explicit trailing delimiter."""

    if not isinstance(values, (list, tuple)) or any(not isinstance(value, str) for value in values):
        raise TypeError("membership values must be an ordered string sequence")
    if len(values) != len(set(values)):
        raise ValueError("membership values must be unique")
    return sha256_bytes(("\n".join(values) + "\n").encode("utf-8"))
