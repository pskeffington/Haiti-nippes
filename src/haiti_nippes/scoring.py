"""Transparent scoring utilities for Haiti Nippes GIS access analysis."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class ScoreWeights:
    """Weights for the compound access vulnerability index."""

    hospital_distance: float = 0.25
    clinic_distance: float = 0.20
    travel_time: float = 0.25
    road_access: float = 0.15
    wash_vulnerability: float = 0.15

    def normalized(self) -> "ScoreWeights":
        """Return weights normalized to sum to one."""
        total = (
            self.hospital_distance
            + self.clinic_distance
            + self.travel_time
            + self.road_access
            + self.wash_vulnerability
        )
        if total <= 0:
            raise ValueError("Score weights must sum to a positive value.")
        return ScoreWeights(
            hospital_distance=self.hospital_distance / total,
            clinic_distance=self.clinic_distance / total,
            travel_time=self.travel_time / total,
            road_access=self.road_access / total,
            wash_vulnerability=self.wash_vulnerability / total,
        )


def clamp_score(value: float) -> float:
    """Clamp a score to the inclusive 0-1 interval."""
    return max(0.0, min(1.0, value))


def min_max_score(value: float | None, minimum: float, maximum: float) -> float | None:
    """Normalize a value to 0-1 where higher means worse vulnerability."""
    if value is None:
        return None
    if maximum <= minimum:
        raise ValueError("Maximum must be greater than minimum.")
    return clamp_score((value - minimum) / (maximum - minimum))


def distance_score(distance_km: float | None, severe_threshold_km: float = 25.0) -> float | None:
    """Score distance where 0 is adjacent and 1 meets or exceeds a severe threshold."""
    if distance_km is None:
        return None
    if severe_threshold_km <= 0:
        raise ValueError("Severe threshold must be positive.")
    return clamp_score(distance_km / severe_threshold_km)


def travel_time_score(minutes: float | None, severe_threshold_minutes: float = 120.0) -> float | None:
    """Score travel time where 1 indicates severe travel-time burden."""
    if minutes is None:
        return None
    if severe_threshold_minutes <= 0:
        raise ValueError("Severe threshold must be positive.")
    return clamp_score(minutes / severe_threshold_minutes)


def road_penalty_score(multiplier: float | None, severe_multiplier: float = 3.0) -> float | None:
    """Score road penalty multipliers into 0-1 vulnerability space."""
    if multiplier is None:
        return None
    if severe_multiplier <= 1.0:
        raise ValueError("Severe multiplier must be greater than 1.")
    return clamp_score((multiplier - 1.0) / (severe_multiplier - 1.0))


def weighted_index(scores: Mapping[str, float | None], weights: ScoreWeights | None = None) -> float | None:
    """Compute a weighted index while ignoring missing components.

    Scores must already be normalized to 0-1 where higher means worse access.
    Missing components are omitted and remaining weights are renormalized.
    """
    selected_weights = (weights or ScoreWeights()).normalized()
    weight_map = {
        "hospital_distance": selected_weights.hospital_distance,
        "clinic_distance": selected_weights.clinic_distance,
        "travel_time": selected_weights.travel_time,
        "road_access": selected_weights.road_access,
        "wash_vulnerability": selected_weights.wash_vulnerability,
    }
    observed = {
        key: clamp_score(value)
        for key, value in scores.items()
        if key in weight_map and value is not None
    }
    if not observed:
        return None
    observed_weight_total = sum(weight_map[key] for key in observed)
    if observed_weight_total <= 0:
        return None
    return sum(observed[key] * weight_map[key] for key in observed) / observed_weight_total


def quality_from_missing(required_values: Mapping[str, object | None]) -> str:
    """Assign a simple quality label based on missing analytic inputs."""
    missing_count = sum(value is None for value in required_values.values())
    if missing_count == 0:
        return "verified"
    if missing_count <= 2:
        return "provisional"
    return "missing"
