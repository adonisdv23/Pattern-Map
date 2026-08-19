"""Frozen, offline-safe configuration for the origin-accounting scaffold."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Tuple


STRUCTURES: Tuple[str, ...] = (
    "one_origin_repetition",
    "multiple_origin_convergence",
    "unknown_origin",
    "conflict",
)
SPLITS: Tuple[str, ...] = ("dev", "pilot", "primary", "stress")
NOISE_RATES: Tuple[float, ...] = (0.05, 0.10, 0.20)


@dataclass(frozen=True)
class FrozenConfig:
    """Configuration values that must be frozen before any primary run.

    The model and intended tokenizer are deliberately unselected.  The
    scaffold can only validate parity with the deterministic local surrogate
    tokenizer named below; it must never be mistaken for a model lock.
    """

    study_id: str = "OA-TPC-001"
    protocol_version: str = "1.0"
    specification_version: str = "loop3-operationalization-0.3"
    schema_version: str = "1.0.0"
    generator_version: str = "oa-slot-grammar-0.1.0"
    parser_version: str = "parser-0.1.0"
    master_seed: str = "OA-v1-offline-scaffold-seed"
    model_id: str = "UNSELECTED"
    model_revision: Optional[str] = None
    tokenizer_revision: Optional[str] = None
    tokenizer_surrogate_id: str = "deterministic-regex-surrogate-v1"
    tokenizer_surrogate_status: str = "LIMITATION_ONLY_NOT_A_MODEL_TOKENIZER"
    primary_n: int = 300
    development_n: int = 80
    pilot_n: int = 40
    stress_n: int = 60
    reports_per_bundle_min: int = 4
    reports_per_bundle_max: int = 6
    max_evidence_ids: int = 6
    max_new_tokens: int = 128
    max_input_tokens: int = 1920
    max_total_tokens: int = 2048
    alpha: float = 0.05
    safety_margin: float = -0.05
    practical_delta: float = -0.08
    bootstrap_repetitions: int = 10000
    power_repetitions: int = 10000
    split_counts: Mapping[str, Mapping[str, int]] = field(
        default_factory=lambda: {
            "dev": {
                "one_origin_repetition": 20,
                "multiple_origin_convergence": 20,
                "unknown_origin": 20,
                "conflict": 20,
            },
            "pilot": {
                "one_origin_repetition": 10,
                "multiple_origin_convergence": 10,
                "unknown_origin": 10,
                "conflict": 10,
            },
            "primary": {
                "one_origin_repetition": 75,
                "multiple_origin_convergence": 75,
                "unknown_origin": 75,
                "conflict": 75,
            },
            "stress": {
                "one_origin_repetition": 15,
                "multiple_origin_convergence": 15,
                "unknown_origin": 15,
                "conflict": 15,
            },
        }
    )
    structures: Tuple[str, ...] = STRUCTURES
    noise_rates: Tuple[float, ...] = NOISE_RATES

    def to_dict(self) -> Dict[str, Any]:
        """Return JSON-safe config data with immutable tuples materialized."""

        data = dict(self.__dict__)
        data["split_counts"] = {
            split: dict(counts) for split, counts in self.split_counts.items()
        }
        data["structures"] = list(self.structures)
        data["noise_rates"] = list(self.noise_rates)
        data["conditions"] = ["F0", "F1", "F2"]
        data["primary_contrast"] = "F2_minus_F1_all_assigned_FC_cons"
        data["safety_endpoint"] = "stipulated_support_origin_recall_fixed_M"
        data["canonicalization"] = "deterministic-json-v1; RFC8785-conformance-required-before-release"
        data["data_status"] = "synthetic_only"
        data["owner_release_authorization"] = False
        data["network_or_provider_calls"] = False
        data["protocol_identity"] = "origin-accounting-protocol-v1.0"
        data["specification_status"] = "historical_operationalization_input_not_a_protocol_identity"
        return data

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "FrozenConfig":
        """Load a config while ignoring derived receipt fields."""

        allowed = set(cls.__dataclass_fields__.keys())
        kwargs: Dict[str, Any] = {key: value[key] for key in allowed if key in value}
        if "split_counts" in kwargs:
            kwargs["split_counts"] = {
                str(split): {str(k): int(v) for k, v in counts.items()}
                for split, counts in kwargs["split_counts"].items()
            }
        if "structures" in kwargs:
            kwargs["structures"] = tuple(kwargs["structures"])
        if "noise_rates" in kwargs:
            kwargs["noise_rates"] = tuple(float(rate) for rate in kwargs["noise_rates"])
        return cls(**kwargs)


def frozen_config_path(path: Optional[Path] = None) -> Path:
    """Return the committed configuration path used by offline entry points."""

    if path is None:
        path = Path(__file__).resolve().parents[2] / "research" / "origin_accounting" / "config" / "frozen_config.json"
    return path


def frozen_config_sha256(path: Optional[Path] = None) -> str:
    """Hash the exact committed configuration bytes for a receipt."""

    config_path = frozen_config_path(path)
    if not config_path.is_file():
        raise FileNotFoundError("frozen configuration is missing: %s" % config_path)
    return hashlib.sha256(config_path.read_bytes()).hexdigest()


def load_frozen_config(path: Optional[Path] = None) -> FrozenConfig:
    """Load the committed frozen config and fail closed if it is missing."""

    path = frozen_config_path(path)
    if not path.is_file():
        raise FileNotFoundError("frozen configuration is missing: %s" % path)
    with path.open("r", encoding="utf-8") as handle:
        return FrozenConfig.from_mapping(json.load(handle))


def assert_config_invariants(config: FrozenConfig) -> None:
    """Fail closed when the frozen implementation config drifts."""

    if tuple(config.structures) != STRUCTURES:
        raise ValueError("structures must remain the four protocol structures")
    if config.protocol_version != "1.0":
        raise ValueError("the frozen scaffold must identify canonical protocol v1.0")
    if tuple(config.noise_rates) != NOISE_RATES:
        raise ValueError("noise_rates must remain the locked nonzero stress rates")
    expected_primary = sum(config.split_counts["primary"].values())
    if expected_primary != config.primary_n:
        raise ValueError("primary split counts do not equal primary_n")
    if config.primary_n != 300:
        raise ValueError("the locked primary set must contain exactly 300 bundles")
    if config.split_counts["primary"].get("multiple_origin_convergence") != 75:
        raise ValueError("the locked safety set must contain exactly 75 primary bundles")
    expected_dev = sum(config.split_counts["dev"].values())
    if expected_dev != config.development_n:
        raise ValueError("development split counts do not equal development_n")
    expected_pilot = sum(config.split_counts["pilot"].values())
    if expected_pilot != config.pilot_n:
        raise ValueError("pilot split counts do not equal pilot_n")
    expected_stress = sum(config.split_counts["stress"].values())
    if expected_stress != config.stress_n:
        raise ValueError("stress split counts do not equal stress_n")
    if config.model_id != "UNSELECTED":
        raise ValueError("the offline scaffold must not select a model")
    if config.tokenizer_revision is not None:
        raise ValueError("the offline scaffold must not claim a model tokenizer revision")
