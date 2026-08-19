"""Planning-only paired-Bernoulli power scaffolding.

No pilot outcome or model output is consumed.  The functions are deliberately
small and deterministic so their grid/configuration can be reviewed before a
preregistration.  They are not evidence of power for any eventual model.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Sequence, Tuple

from .analysis import bootstrap_difference, one_sided_lower_bootstrap, paired_exact_pvalue
from .config import FrozenConfig


def _paired_probabilities(baseline: float, discordance: float, delta: float) -> Tuple[float, float, float, float]:
    """Return p00,p01,p10,p11 for (F1,F2), or raise for invalid cells."""

    improvement = -delta
    p10 = (discordance + improvement) / 2.0  # F1=1,F2=0
    p01 = (discordance - improvement) / 2.0  # F1=0,F2=1
    # baseline is P(F1=1), so the shared-success cell is baseline minus the
    # F1=1,F2=0 improvement cell p10.
    p11 = baseline - p10
    p00 = 1.0 - p10 - p01 - p11
    if min(p00, p01, p10, p11) < -1e-12:
        raise ValueError("invalid paired Bernoulli cell")
    return max(0.0, p00), max(0.0, p01), max(0.0, p10), max(0.0, p11)


def _draw_pair(rng: random.Random, probabilities: Tuple[float, float, float, float]) -> Tuple[int, int]:
    p00, p01, p10, p11 = probabilities
    draw = rng.random()
    if draw < p00:
        return 0, 0
    if draw < p00 + p01:
        return 0, 1
    if draw < p00 + p01 + p10:
        return 1, 0
    return 1, 1


def simulate_fc_cell(
    baseline: float,
    discordance: float,
    delta: float,
    n: int,
    repetitions: int,
    seed: int,
    invalid_rate: float = 0.0,
    invalid_coding: str = "conservative",
    bootstrap_repetitions: int = 1000,
) -> Dict[str, Any]:
    if n <= 0 or repetitions <= 0 or bootstrap_repetitions <= 0:
        raise ValueError("n, repetitions, and bootstrap_repetitions must be positive")
    if not 0.0 <= invalid_rate <= 1.0:
        raise ValueError("invalid_rate must be between zero and one")
    if invalid_coding not in {"conservative", "liberal"}:
        raise ValueError("invalid_coding must be conservative or liberal")
    probabilities = _paired_probabilities(baseline, discordance, delta)
    rng = random.Random(seed)
    passes = 0
    coverages = 0
    p_values: List[float] = []
    for _ in range(repetitions):
        left: List[int] = []
        right: List[int] = []
        for _ in range(n):
            f1, f2 = _draw_pair(rng, probabilities)
            # Invalid coding is applied independently to either assigned run.
            # Conservative FC coding makes an invalid run a risk event (1);
            # liberal coding makes it a non-event (0). Both are planning-only
            # sensitivities and do not alter the locked primary estimand.
            if rng.random() < invalid_rate:
                f1 = 1 if invalid_coding == "conservative" else 0
            if rng.random() < invalid_rate:
                f2 = 1 if invalid_coding == "conservative" else 0
            left.append(f1)
            right.append(f2)
        p_value = paired_exact_pvalue(left, right)
        delta_hat = sum(right) / float(n) - sum(left) / float(n)
        interval_low, interval_high = bootstrap_difference(
            left,
            right,
            repetitions=bootstrap_repetitions,
            seed=seed + 1000003 + len(p_values),
        )
        p_values.append(p_value)
        if delta_hat < 0 and p_value < 0.05 and interval_high < 0:
            passes += 1
        target_delta = (1.0 - invalid_rate) * delta
        if interval_low <= target_delta <= interval_high:
            coverages += 1
    return {
        "baseline_fc": baseline,
        "discordance": discordance,
        "delta_f2_minus_f1": delta,
        "n": n,
        "repetitions": repetitions,
        "invalid_rate": invalid_rate,
        "invalid_coding": invalid_coding,
        "primary_decision_rate": passes / float(repetitions),
        "power_or_type_i_error": passes / float(repetitions),
        "bootstrap_coverage": coverages / float(repetitions),
        "bootstrap_repetitions_per_simulated_sample": bootstrap_repetitions,
        "bootstrap_interval": "paired_percentile_95_development_scaffold",
        "coverage_target": "expected_delta_after_invalid_coding",
        "median_p_value": sorted(p_values)[len(p_values) // 2] if p_values else None,
        "simulation_seed": seed,
    }


def run_power_simulation(
    config: Optional[FrozenConfig] = None,
    repetitions: Optional[int] = None,
    n_values: Sequence[int] = (240, 280, 300, 320, 360),
    bootstrap_repetitions: Optional[int] = None,
    vor_n_values: Sequence[int] = (75,),
    vor_bootstrap_repetitions: Optional[int] = None,
    include_vor: bool = True,
) -> Dict[str, Any]:
    """Run planning-only FC and fixed-M VOR operating-characteristic grids."""

    config = config or FrozenConfig()
    repetitions = int(repetitions or config.power_repetitions)
    bootstrap_repetitions = int(bootstrap_repetitions or config.bootstrap_repetitions)
    vor_bootstrap_repetitions = int(vor_bootstrap_repetitions or bootstrap_repetitions)
    if repetitions <= 0 or bootstrap_repetitions <= 0 or vor_bootstrap_repetitions <= 0:
        raise ValueError("simulation repetition counts must be positive")
    cells: List[Dict[str, Any]] = []
    skipped_cells: List[Dict[str, Any]] = []
    seed_base = 2026081801
    cell_index = 0
    for baseline in (0.20, 0.30, 0.40):
        for discordance in (0.10, 0.20, 0.30):
            for delta in (0.00, -0.05, -0.08, -0.10):
                for n in n_values:
                    for invalid_rate in (0.0, 0.02, 0.05, 0.10):
                        for invalid_coding in ("conservative", "liberal"):
                            parameters = {
                                "baseline": baseline,
                                "discordance": discordance,
                                "delta": delta,
                                "n": int(n),
                                "invalid_rate": invalid_rate,
                                "invalid_coding": invalid_coding,
                            }
                            try:
                                result = simulate_fc_cell(
                                    baseline,
                                    discordance,
                                    delta,
                                    int(n),
                                    repetitions,
                                    seed_base + cell_index,
                                    invalid_rate,
                                    invalid_coding=invalid_coding,
                                    bootstrap_repetitions=bootstrap_repetitions,
                                )
                            except ValueError as exc:
                                skipped_cells.append({"parameters": parameters, "reason": str(exc)})
                            else:
                                cells.append(result)
                            cell_index += 1
    vor_cells: List[Dict[str, Any]] = []
    vor_skipped_cells: List[Dict[str, Any]] = []
    if include_vor:
        vor_seed_base = seed_base + 100000000
        vor_index = 0
        for baseline in (0.70, 0.80, 0.90):
            for discordance in (0.10, 0.20, 0.30):
                for delta in (0.00, -0.02, -0.05, -0.08):
                    for n in vor_n_values:
                        for invalid_rate in (0.0, 0.02, 0.05, 0.10):
                            parameters = {
                                "baseline": baseline,
                                "discordance": discordance,
                                "delta": delta,
                                "n_fixed_M": int(n),
                                "invalid_rate": invalid_rate,
                                "invalid_coding": "invalid_as_zero",
                            }
                            try:
                                result = simulate_vor_cell(
                                    baseline,
                                    discordance,
                                    delta,
                                    int(n),
                                    repetitions,
                                    vor_seed_base + vor_index,
                                    margin=config.safety_margin,
                                    invalid_rate=invalid_rate,
                                    bootstrap_repetitions=vor_bootstrap_repetitions,
                                )
                            except ValueError as exc:
                                vor_skipped_cells.append({"parameters": parameters, "reason": str(exc)})
                            else:
                                vor_cells.append(result)
                            vor_index += 1
    return {
        "simulation_version": "paired-bernoulli-fc-vor-0.2.0",
        "status": "planning_only_no_pilot_or_model_outputs",
        "grid": {
            "baseline_fc": [0.20, 0.30, 0.40],
            "discordance": [0.10, 0.20, 0.30],
            "delta_f2_minus_f1": [0.00, -0.05, -0.08, -0.10],
            "n": list(n_values),
            "invalid_rate": [0.0, 0.02, 0.05, 0.10],
            "invalid_coding": ["conservative", "liberal"],
        },
        "repetitions_per_cell": repetitions,
        "bootstrap_repetitions_per_simulated_sample": bootstrap_repetitions,
        "seed_base": seed_base,
        "cells": cells,
        "skipped_cells": skipped_cells,
        "vor_grid": {
            "baseline_vor": [0.70, 0.80, 0.90],
            "discordance": [0.10, 0.20, 0.30],
            "delta_vor": [0.00, -0.02, -0.05, -0.08],
            "n_fixed_M": list(vor_n_values),
            "expected_protocol_n_fixed_M": 75,
            "invalid_rate": [0.0, 0.02, 0.05, 0.10],
            "invalid_coding": "invalid_as_zero",
        },
        "vor_repetitions_per_cell": repetitions,
        "vor_bootstrap_repetitions_per_simulated_sample": vor_bootstrap_repetitions,
        "vor_cells": vor_cells,
        "vor_skipped_cells": vor_skipped_cells,
        "vor_interval_method": "one_sided_95_lower_paired_percentile_development_scaffold",
        "interpretation": "Planning operating characteristics only; no power, coverage, or safety claim until the frozen manifest and fixed safety-set interval method are published.",
    }


def simulate_vor_cell(
    baseline: float,
    discordance: float,
    delta: float,
    n: int,
    repetitions: int,
    seed: int,
    margin: float = -0.05,
    invalid_rate: float = 0.0,
    bootstrap_repetitions: int = 1000,
) -> Dict[str, Any]:
    """Fixed-M VOR non-inferiority operating characteristic scaffold."""

    if n <= 0 or repetitions <= 0 or bootstrap_repetitions <= 0:
        raise ValueError("n, repetitions, and bootstrap_repetitions must be positive")
    if not 0.0 <= invalid_rate <= 1.0:
        raise ValueError("invalid_rate must be between zero and one")
    probabilities = _paired_probabilities(baseline, discordance, delta)
    rng = random.Random(seed)
    passes = 0
    coverages = 0
    for _ in range(repetitions):
        left: List[int] = []
        right: List[int] = []
        for _ in range(n):
            pair = _draw_pair(rng, probabilities)
            # VOR invalid outputs are conservatively coded as zero by the
            # locked safety rule. This is a planning stress parameter.
            left.append(0 if rng.random() < invalid_rate else pair[0])
            right.append(0 if rng.random() < invalid_rate else pair[1])
        delta_hat = sum(right) / float(n) - sum(left) / float(n)
        lower = one_sided_lower_bootstrap(
            left,
            right,
            repetitions=bootstrap_repetitions,
            seed=seed + 1000003 + passes + coverages,
        )
        if lower > margin:
            passes += 1
        target_delta = (1.0 - invalid_rate) * delta
        if lower <= target_delta:
            coverages += 1
    return {
        "baseline_vor": baseline,
        "discordance": discordance,
        "delta_vor": delta,
        "n_fixed_M": n,
        "repetitions": repetitions,
        "margin": margin,
        "invalid_rate": invalid_rate,
        "invalid_coding": "invalid_as_zero",
        "gate_probability": passes / float(repetitions),
        "probability_passing_guardrail": passes / float(repetitions),
        "coverage_probability": coverages / float(repetitions),
        "bootstrap_repetitions_per_simulated_sample": bootstrap_repetitions,
        "interval_method": "one_sided_95_lower_paired_percentile_development_scaffold",
        "status": "planning_only",
    }
