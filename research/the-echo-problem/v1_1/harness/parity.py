"""Exact, deterministic F1/F2 parity search for a selected tokenizer.

The solver is deliberately tokenizer-agnostic: the caller supplies an object
with ``encode(text)`` or a callable returning token IDs.  The optional
`tiktoken` helper is imported only when explicitly requested.  Search is over
neutral development padding candidates and records the actual resulting token
counts; it never assumes that a string has a fixed token length under BPE.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import hashlib
import json
from typing import Any, Callable, Iterable, Sequence

try:  # supports both package imports and unittest discovery from this folder
    from .canonical import sha256_bytes
except ImportError:  # pragma: no cover - discovery mode
    from canonical import sha256_bytes


# These strings are development-only candidates for a reserved, semantically
# inert padding slot.  They are not a license to append arbitrary prose to a
# live prompt; the selected-template receipt must define and audit the slot.
DEFAULT_PADDING_CANDIDATES = (" ", " x", " foo", ". ", " 1")


def _encode(tokenizer: Any, text: str) -> Sequence[int]:
    encoded = tokenizer.encode(text) if hasattr(tokenizer, "encode") else tokenizer(text)
    return list(encoded)


def token_count(tokenizer: Any, text: str) -> int:
    return len(_encode(tokenizer, text))


@dataclass(frozen=True)
class ParitySolution:
    f1_padding: str
    f2_padding: str
    f1_tokens: int
    f2_tokens: int
    total_padding_segments: int
    total_padding_bytes: int
    status: str


def _padding_options(
    base: str,
    tokenizer: Any,
    candidates: Sequence[str],
    max_segments: int,
    max_padding_tokens: int,
) -> list[tuple[int, int, str]]:
    """Enumerate context-sensitive candidate strings deterministically."""

    seen = {""}
    queue: deque[tuple[str, int]] = deque([("", 0)])
    options: list[tuple[int, int, str]] = []
    base_count = token_count(tokenizer, base)
    while queue:
        padding, segments = queue.popleft()
        count = token_count(tokenizer, base + padding)
        if count <= base_count + max_padding_tokens:
            options.append((count, segments, padding))
        if segments >= max_segments:
            continue
        for candidate in candidates:
            new_padding = padding + candidate
            if new_padding in seen:
                continue
            seen.add(new_padding)
            queue.append((new_padding, segments + 1))
    return sorted(options, key=lambda item: (item[0], item[1], len(item[2]), item[2]))


def _find_target_padding(
    base: str,
    target: int,
    tokenizer: Any,
    candidates: Sequence[str],
    max_segments: int,
    max_padding_tokens: int,
) -> tuple[int, int, str] | None:
    """Find one bounded padding string for one exact target count.

    Breadth-first search stops at the first target, avoiding the Cartesian
    explosion of enumerating every string on both sides of a pair.
    """

    base_count = token_count(tokenizer, base)
    if target < base_count or target > base_count + max_padding_tokens:
        return None
    # Most BPE encodings have a reserved candidate whose repeated application
    # adds one token at a time. Check those direct sequences first; this makes
    # large real prompts cheap while still measuring the actual context.
    for candidate in candidates:
        for segments in range(1, max_segments + 1):
            padding = candidate * segments
            if token_count(tokenizer, base + padding) == target:
                return (target, segments, padding)
    queue: deque[tuple[str, int]] = deque([("", 0)])
    seen = {""}
    matches: list[tuple[int, int, str]] = []
    while queue:
        padding, segments = queue.popleft()
        count = token_count(tokenizer, base + padding)
        if count == target:
            # Breadth-first order makes this the minimum segment solution;
            # candidate ordering is frozen for deterministic tie-breaking.
            return (count, segments, padding)
        if segments >= min(max_segments, 6):
            continue
        for candidate in candidates:
            new_padding = padding + candidate
            if new_padding in seen:
                continue
            seen.add(new_padding)
            queue.append((new_padding, segments + 1))
    return None


def solve_exact_parity(
    f1_text: str,
    f2_text: str,
    tokenizer: Any,
    *,
    candidates: Sequence[str] = DEFAULT_PADDING_CANDIDATES,
    max_segments: int = 16,
    max_padding_tokens: int = 16,
    report_hash_f1: str | None = None,
    report_hash_f2: str | None = None,
    ordered_report_ids_f1: Sequence[str] | None = None,
    ordered_report_ids_f2: Sequence[str] | None = None,
) -> ParitySolution:
    """Find exact equal token counts or fail closed.

    Report hashes and ordered IDs are optional inputs for local callers, but if
    provided they must match.  The solver never repairs a report mismatch.
    """

    if report_hash_f1 is not None and report_hash_f2 is not None and report_hash_f1 != report_hash_f2:
        raise ValueError("F1/F2 report content hashes differ; parity is not admissible")
    if ordered_report_ids_f1 is not None and ordered_report_ids_f2 is not None:
        if list(ordered_report_ids_f1) != list(ordered_report_ids_f2):
            raise ValueError("F1/F2 report order or membership differs; parity is not admissible")
    base_f1 = token_count(tokenizer, f1_text)
    base_f2 = token_count(tokenizer, f2_text)
    # First try to pad only the shorter side to the longer side's current
    # count. This is the common case and is much cheaper than enumerating both
    # Cartesian option sets. If context-sensitive BPE behavior blocks that
    # target, search shared higher targets in ascending order.
    targets = list(range(max(base_f1, base_f2), max(base_f1, base_f2) + max_padding_tokens + 1))
    for target in targets:
        f1_padding = _find_target_padding(
            f1_text, target, tokenizer, candidates, max_segments, max_padding_tokens
        )
        f2_padding = _find_target_padding(
            f2_text, target, tokenizer, candidates, max_segments, max_padding_tokens
        )
        if f1_padding is None or f2_padding is None:
            continue
        _, f1_segments, f1_pad = f1_padding
        _, f2_segments, f2_pad = f2_padding
        count = target
        segments = f1_segments + f2_segments
        byte_count = len(f1_pad) + len(f2_pad)
        break
    else:
        raise ValueError("no exact F1/F2 token parity solution within bounded padding search")
    return ParitySolution(
        f1_padding=f1_pad,
        f2_padding=f2_pad,
        f1_tokens=count,
        f2_tokens=count,
        total_padding_segments=segments,
        total_padding_bytes=byte_count,
        status="selected_tokenizer_exact_parity_candidate",
    )


def tiktoken_tokenizer(encoding_name: str = "cl100k_base") -> Any:
    """Load tiktoken only when the caller explicitly asks for it."""

    try:
        import tiktoken  # type: ignore
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise RuntimeError("tiktoken is not installed in this environment") from exc
    return tiktoken.get_encoding(encoding_name)


def tokenizer_fingerprint(tokenizer: Any) -> str:
    """Hash the observable encoding tables for a reproducible local receipt."""

    if not all(hasattr(tokenizer, attr) for attr in ("_mergeable_ranks", "_special_tokens", "_pat_str")):
        raise TypeError("tokenizer does not expose a stable local encoding fingerprint")
    payload = {
        "mergeable_ranks": sorted((key.hex(), value) for key, value in tokenizer._mergeable_ranks.items()),
        "special_tokens": sorted(tokenizer._special_tokens.items()),
        "pat_str": tokenizer._pat_str,
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
