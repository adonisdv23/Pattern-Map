"""Provider-free, design-only EP v1.1 offline harness.

This package accepts synthetic records and already-rendered bytes only.  It has
no model, network, provider, dataset-download, or cloud-runtime path.
"""

from .canonical import content_sha256, ordered_membership_sha256
from .parser import ParseResult, parse_output
from .scoring import score_output
from .parity import solve_exact_parity
from .planning import paired_exact_pvalue, run_power_surface

__all__ = [
    "ParseResult",
    "content_sha256",
    "ordered_membership_sha256",
    "parse_output",
    "paired_exact_pvalue",
    "run_power_surface",
    "score_output",
    "solve_exact_parity",
]
