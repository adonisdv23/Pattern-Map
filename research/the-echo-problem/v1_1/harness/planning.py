"""Deterministic planning-only paired FC power/MDE surface.

This module simulates binary paired outcomes from declared probabilities.  It
never consumes a model output, corpus, or pilot observation.  The exact
McNemar/binomial calculation is the same logic required by the preserved v1
protocol; bootstrap intervals are an optional deterministic planning sidecar.
"""

from __future__ import annotations

import math
import random
from typing import Any, Iterable, Sequence


def _lower_half_binomial_tail(k: int, n: int) -> float:
    """Return P[X <= k] for X~Binomial(n, 0.5), with k <= n/2.

    Starting from the largest term in the requested lower tail and walking
    downward avoids the cancellation and large-integer-to-float overflow of a
    complementary-CDF implementation. Extremely small tails may underflow to
    0.0, which remains a valid bounded p-value.
    """

    if k < 0:
        return 0.0
    if n < 0 or k > n // 2:
        raise ValueError("lower-tail helper requires 0 <= k <= n/2")
    log_term = (
        math.lgamma(n + 1)
        - math.lgamma(k + 1)
        - math.lgamma(n - k + 1)
        - n * math.log(2.0)
    )
    term = math.exp(log_term)
    terms = [term]
    for index in range(k, 0, -1):
        term *= index / (n - index + 1)
        terms.append(term)
    return min(1.0, max(0.0, math.fsum(terms)))


def paired_exact_pvalue(left: Sequence[int], right: Sequence[int]) -> float:
    """Two-sided exact McNemar/binomial p-value for paired binary vectors."""

    if len(left) != len(right):
        raise ValueError("paired vectors must have equal length")
    b = sum(int(a == 1 and z == 0) for a, z in zip(left, right))
    c = sum(int(a == 0 and z == 1) for a, z in zip(left, right))
    discordant = b + c
    if discordant == 0:
        return 1.0
    lower_tail = _lower_half_binomial_tail(min(b, c), discordant)
    return min(1.0, max(0.0, 2.0 * lower_tail))


def _cells(baseline: float, discordance: float, delta: float) -> tuple[float, float, float, float]:
    # p10 = P(F1=1,F2=0); p01 = P(F1=0,F2=1); delta = p01-p10.
    p10 = (discordance - delta) / 2.0
    p01 = (discordance + delta) / 2.0
    p11 = baseline - p10
    p00 = 1.0 - p10 - p01 - p11
    if min(p00, p01, p10, p11) < -1e-12:
        raise ValueError("declared paired cell is infeasible")
    return tuple(max(0.0, item) for item in (p00, p01, p10, p11))


def _draw(rng: random.Random, cells: tuple[float, float, float, float]) -> tuple[int, int]:
    draw = rng.random()
    p00, p01, p10, _ = cells
    if draw < p00:
        return 0, 0
    if draw < p00 + p01:
        return 0, 1
    if draw < p00 + p01 + p10:
        return 1, 0
    return 1, 1


def _percentile(values: list[float], fraction: float) -> float:
    values = sorted(values)
    if not values:
        raise ValueError("cannot take percentile of empty values")
    index = max(0, min(len(values) - 1, int(fraction * len(values))))
    return values[index]


def paired_bootstrap_interval(left: Sequence[int], right: Sequence[int], repetitions: int, seed: int) -> tuple[float, float]:
    if len(left) != len(right):
        raise ValueError("paired vectors must have equal length")
    if not left:
        raise ValueError("paired vectors must be non-empty")
    if repetitions <= 0:
        raise ValueError("bootstrap repetitions must be positive")
    differences = [int(z) - int(a) for a, z in zip(left, right)]
    rng = random.Random(seed)
    n = len(differences)
    samples = [sum(differences[rng.randrange(n)] for _ in range(n)) / n for _ in range(repetitions)]
    return _percentile(samples, 0.025), _percentile(samples, 0.975)


def simulate_power_cell(
    baseline: float,
    discordance: float,
    delta: float,
    n: int,
    repetitions: int,
    seed: int,
    *,
    bootstrap_repetitions: int = 0,
    invalid_f1: float = 0.0,
    invalid_f2: float = 0.0,
    invalid_coding: str = "conservative",
) -> dict[str, Any]:
    """Simulate one declared cell; output remains planning-only."""

    if n <= 0 or repetitions <= 0 or bootstrap_repetitions < 0:
        raise ValueError("n and repetitions must be positive")
    if not 0 <= invalid_f1 <= 1 or not 0 <= invalid_f2 <= 1:
        raise ValueError("invalid rates must be in [0,1]")
    if invalid_coding not in {"conservative", "liberal"}:
        raise ValueError("invalid_coding must be conservative or liberal")
    cells = _cells(baseline, discordance, delta)
    rng = random.Random(seed)
    decisions = 0
    coverages = 0
    for repetition in range(repetitions):
        left: list[int] = []
        right: list[int] = []
        for _ in range(n):
            f1, f2 = _draw(rng, cells)
            if rng.random() < invalid_f1:
                f1 = 1 if invalid_coding == "conservative" else 0
            if rng.random() < invalid_f2:
                f2 = 1 if invalid_coding == "conservative" else 0
            left.append(f1)
            right.append(f2)
        p_value = paired_exact_pvalue(left, right)
        observed_delta = sum(right) / n - sum(left) / n
        high = None
        if bootstrap_repetitions:
            _, high = paired_bootstrap_interval(left, right, bootstrap_repetitions, seed + 100003 + repetition)
        decisions += int(observed_delta < 0 and p_value < 0.05 and (high is None or high < 0))
        if high is not None:
            target = delta
            low, high_for_coverage = paired_bootstrap_interval(left, right, bootstrap_repetitions, seed + 200003 + repetition)
            coverages += int(low <= target <= high_for_coverage)
    return {
        "baseline_fc": baseline,
        "paired_discordance": discordance,
        "delta_f2_minus_f1": delta,
        "n": n,
        "repetitions": repetitions,
        "invalid_f1": invalid_f1,
        "invalid_f2": invalid_f2,
        "invalid_coding": invalid_coding,
        "decision_power_or_type_i_error": decisions / repetitions,
        "bootstrap_coverage": (coverages / repetitions) if bootstrap_repetitions else None,
        "decision_rule": "exact_two_sided_mcnemar_p_lt_0.05_and_delta_lt_0_plus_optional_bootstrap_upper_lt_0",
        "status": "planning_only_no_model_or_corpus_outputs",
        "seed": seed,
    }


def run_power_surface(
    *,
    baselines: Iterable[float] = (0.20, 0.30, 0.40),
    discordances: Iterable[float] = (0.10, 0.20, 0.30),
    deltas: Iterable[float] = (0.0, -0.05, -0.08, -0.10),
    sample_sizes: Iterable[int] = (240, 280, 300, 320, 360, 400),
    invalidity_pairs: Iterable[tuple[float, float]] = ((0.0, 0.0),),
    invalid_coding: str = "conservative",
    repetitions: int = 10000,
    bootstrap_repetitions: int = 0,
    seed: int = 2026082301,
) -> dict[str, Any]:
    """Return a deterministic planning surface across discordance and N."""

    baselines = tuple(baselines)
    discordances = tuple(discordances)
    deltas = tuple(deltas)
    sample_sizes = tuple(sample_sizes)
    invalidity_pairs = tuple((float(f1), float(f2)) for f1, f2 in invalidity_pairs)
    if not invalidity_pairs:
        raise ValueError("at least one invalidity pair is required")
    cells: list[dict[str, Any]] = []
    index = 0
    for baseline in baselines:
        for discordance in discordances:
            for delta in deltas:
                for n in sample_sizes:
                    for invalid_f1, invalid_f2 in invalidity_pairs:
                        try:
                            cells.append(
                                simulate_power_cell(
                                    float(baseline),
                                    float(discordance),
                                    float(delta),
                                    int(n),
                                    repetitions,
                                    seed + index,
                                    bootstrap_repetitions=bootstrap_repetitions,
                                    invalid_f1=invalid_f1,
                                    invalid_f2=invalid_f2,
                                    invalid_coding=invalid_coding,
                                )
                            )
                        except ValueError as exc:
                            cells.append({
                                "baseline_fc": baseline,
                                "paired_discordance": discordance,
                                "delta_f2_minus_f1": delta,
                                "n": n,
                                "invalid_f1": invalid_f1,
                                "invalid_f2": invalid_f2,
                                "invalid_coding": invalid_coding,
                                "status": "skipped_infeasible_cell",
                                "reason": str(exc),
                            })
                        index += 1
    return {
        "version": "EP-v1.1-planning-surface-0.1",
        "status": "planning_only_no_model_or_corpus_outputs",
        "grid": {
            "baseline_fc": list(baselines),
            "paired_discordance": list(discordances),
            "delta_f2_minus_f1": list(deltas),
            "n": list(sample_sizes),
            "invalidity_pairs_f1_f2": [list(pair) for pair in invalidity_pairs],
            "invalid_coding": invalid_coding,
            "fixed_safety_set_size": 75,
        },
        "repetitions_per_cell": repetitions,
        "bootstrap_repetitions_per_sample": bootstrap_repetitions,
        "seed": seed,
        "cells": cells,
    }


if __name__ == "__main__":  # pragma: no cover
    import argparse
    import json

    def invalidity_pair(value: str) -> tuple[float, float]:
        try:
            left, right = value.split(",", 1)
            pair = (float(left), float(right))
        except (TypeError, ValueError) as exc:
            raise argparse.ArgumentTypeError("invalidity pair must be F1,F2") from exc
        if any(item < 0 or item > 1 for item in pair):
            raise argparse.ArgumentTypeError("invalidity rates must be in [0,1]")
        return pair

    parser = argparse.ArgumentParser(description="EP v1.1 planning-only MDE/power surface")
    parser.add_argument("--output", required=True)
    parser.add_argument("--repetitions", type=int, default=10000)
    parser.add_argument("--bootstrap-repetitions", type=int, default=0)
    parser.add_argument(
        "--invalidity-pair",
        action="append",
        type=invalidity_pair,
        help="repeatable F1,F2 rates; default 0,0 (for example 0.02,0.05)",
    )
    args = parser.parse_args()
    output = run_power_surface(
        repetitions=args.repetitions,
        bootstrap_repetitions=args.bootstrap_repetitions,
        invalidity_pairs=tuple(args.invalidity_pair) if args.invalidity_pair else ((0.0, 0.0),),
    )
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2, sort_keys=True)
        handle.write("\n")
