"""Deterministic content and ordered-membership receipts.

The content digest covers the complete canonical JSON value.  The membership
digest covers the ordered ID sequence separately, so content edits and order
or membership edits cannot be hidden behind an index-only hash.
"""

from __future__ import annotations

import hashlib
import json
import math
from typing import Any, Iterable, Mapping


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


def content_sha256(value: Any) -> str:
    """Hash complete serialized content, not just assigned IDs."""

    return sha256_bytes(canonical_json_bytes(value))


def ordered_membership_sha256(values: Iterable[str]) -> str:
    """Hash ordered unique membership with an explicit trailing delimiter."""

    ordered = list(values)
    if any(not isinstance(value, str) for value in ordered):
        raise TypeError("membership values must be strings")
    if len(ordered) != len(set(ordered)):
        raise ValueError("membership values must be unique")
    return sha256_bytes(("\n".join(ordered) + "\n").encode("utf-8"))


def manifest_receipt(content: Any, membership: Iterable[str]) -> dict[str, Any]:
    ordered = list(membership)
    return {
        "content_sha256": content_sha256(content),
        "membership_sha256": ordered_membership_sha256(ordered),
        "membership_count": len(ordered),
        "membership_ordered": ordered,
        "status": "offline_design_receipt",
    }
