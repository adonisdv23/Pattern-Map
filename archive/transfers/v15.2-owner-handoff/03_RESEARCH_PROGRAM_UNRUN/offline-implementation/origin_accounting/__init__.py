"""Offline scaffolding for the F0/F1/F2 origin-accounting protocol.

This package intentionally contains no model, network, provider, or cloud
runtime integration.  It provides deterministic synthetic records, prompt
construction, strict output parsing, fixed-denominator scoring, diagnostics,
and planning-only power simulations so the protocol can be audited before a
model is selected or a primary split is opened.
"""

from .config import FrozenConfig, load_frozen_config
from .generator import Corpus, build_primary_manifest, generate_corpus, build_prompt_instances, validate_corpus
from .parser import ParseResult, parse_output, raw_output_record, validate_raw_output_record, validate_run_record
from .analysis import paired_analysis, score_output

__all__ = [
    "Corpus",
    "FrozenConfig",
    "ParseResult",
    "build_prompt_instances",
    "build_primary_manifest",
    "generate_corpus",
    "load_frozen_config",
    "paired_analysis",
    "parse_output",
    "raw_output_record",
    "validate_raw_output_record",
    "validate_run_record",
    "score_output",
    "validate_corpus",
]
