"""Flood and road-disruption objects for the Haiti Nippes GIS project."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from haiti_nippes.access_model import DataQuality


class DisruptionType(str, Enum):
    """Road and access disruption categories."""

    FLOODING = "flooding"
    LANDSLIDE = "landslide"
    BRIDGE_FAILURE = "bridge_failure"
    CULVERT_FAILURE = "culvert_failure"
    WASHOUT = "washout"
    DEBRIS = "debris"
    UNKNOWN = "unknown"


class PassabilityStatus(str, Enum):
    """Operational passability categories."""

    OPEN = "open"
    DEGRADED = "degraded"
    HIGH_CLEARANCE_ONLY = "high_clearance_only"
    FOOT_ONLY = "foot_only"
    BLOCKED = "blocked"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class FloodExposureZone:
    """Flood exposure zone for commune, settlement, or corridor analysis."""

    zone_id: str
    name: str
    geography_name: str
    flood_score: float | None
    return_period: str | None = None
    dominant_driver: str | None = None
    source_id: str | None = None
    quality: DataQuality = DataQuality.PROVISIONAL

    def normalized_score(self) -> float | None:
        """Return flood exposure clipped to 0-1."""
        if self.flood_score is None:
            return None
        return max(0.0, min(1.0, self.flood_score))


@dataclass(frozen=True)
class RoadDisruptionRecord:
    """Observed or modeled disruption affecting a road segment or chokepoint."""

    disruption_id: str
    road_id: str | None
    location_name: str
    disruption_type: DisruptionType
    passability: PassabilityStatus
    flood_depth_m: float | None = None
    detour_required: bool = False
    estimated_delay_minutes: float | None = None
    wet_season_only: bool = True
    source_id: str | None = None
    quality: DataQuality = DataQuality.PROVISIONAL

    def severity_score(self) -> float:
        """Return a simple 0-1 severity score for access modeling."""
        passability_scores = {
            PassabilityStatus.OPEN: 0.0,
            PassabilityStatus.DEGRADED: 0.35,
            PassabilityStatus.HIGH_CLEARANCE_ONLY: 0.55,
            PassabilityStatus.FOOT_ONLY: 0.8,
            PassabilityStatus.BLOCKED: 1.0,
            PassabilityStatus.UNKNOWN: 0.5,
        }
        score = passability_scores[self.passability]
        if self.detour_required:
            score += 0.15
        if self.flood_depth_m is not None and self.flood_depth_m >= 0.3:
            score += 0.2
        return max(0.0, min(1.0, score))


@dataclass(frozen=True)
class DrainageChokepoint:
    """Bridge, culvert, ford, or drainage point that can break access."""

    chokepoint_id: str
    name: str
    road_id: str | None
    chokepoint_type: str
    condition: str | None
    flood_susceptibility_score: float | None
    source_id: str | None = None
    quality: DataQuality = DataQuality.PROVISIONAL

    def priority_score(self) -> float | None:
        """Return a maintenance or field-verification priority score."""
        if self.flood_susceptibility_score is None:
            return None
        base = max(0.0, min(1.0, self.flood_susceptibility_score))
        if self.condition in {"poor", "failed", "unknown"}:
            return max(base, 0.75)
        return base
