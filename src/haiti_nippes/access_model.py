"""Access-model objects for health, road, and WASH GIS analysis."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class FacilityType(str, Enum):
    """Health-service facility categories."""

    HOSPITAL = "hospital"
    CLINIC = "clinic"
    DISPENSARY = "dispensary"
    HEALTH_POST = "health_post"
    PHARMACY = "pharmacy"
    UNKNOWN = "unknown"


class DataQuality(str, Enum):
    """Data-quality flags used across GIS layers."""

    VERIFIED = "verified"
    PROVISIONAL = "provisional"
    STALE = "stale"
    CONFLICTING = "conflicting"
    MISSING = "missing"


@dataclass(frozen=True)
class HealthFacility:
    """A mapped health-service point."""

    name: str
    facility_type: FacilityType
    commune: str | None
    latitude: float | None
    longitude: float | None
    operating_status: str | None = None
    capacity_notes: str | None = None
    source_id: str | None = None
    quality: DataQuality = DataQuality.PROVISIONAL

    @property
    def has_coordinates(self) -> bool:
        """Return whether the facility has usable point coordinates."""
        return self.latitude is not None and self.longitude is not None


@dataclass(frozen=True)
class RoadSegmentStatus:
    """Condition metadata for a road segment or chokepoint."""

    road_id: str
    road_class: str | None
    surface: str | None
    passability: str | None
    wet_season_penalty: float = 1.0
    bridge_or_chokepoint: bool = False
    source_id: str | None = None
    quality: DataQuality = DataQuality.PROVISIONAL

    def travel_penalty(self) -> float:
        """Return a conservative travel-time penalty multiplier."""
        base = max(self.wet_season_penalty, 1.0)
        if self.bridge_or_chokepoint:
            return base * 1.25
        return base


@dataclass(frozen=True)
class WashAccessRecord:
    """WASH access indicator for a place or administrative unit."""

    geography_id: str
    geography_name: str
    water_access_score: float | None
    sanitation_access_score: float | None
    cholera_or_waterborne_risk: float | None = None
    source_id: str | None = None
    quality: DataQuality = DataQuality.PROVISIONAL

    def composite_score(self) -> float | None:
        """Return a simple WASH vulnerability score where higher means worse access."""
        components = [
            self.water_access_score,
            self.sanitation_access_score,
            self.cholera_or_waterborne_risk,
        ]
        observed = [component for component in components if component is not None]
        if not observed:
            return None
        return sum(observed) / len(observed)


@dataclass(frozen=True)
class CommuneAccessProfile:
    """Commune-level access and vulnerability summary."""

    commune: str
    nearest_hospital_km: float | None
    nearest_clinic_km: float | None
    estimated_travel_time_minutes: float | None
    road_access_penalty: float | None
    wash_vulnerability_score: float | None
    population_exposure: int | None = None
    quality: DataQuality = DataQuality.PROVISIONAL

    def vulnerability_index(self) -> float | None:
        """Combine normalized access components into a transparent provisional index.

        Inputs are assumed to be pre-normalized to a 0-1 scale before production use.
        Higher values indicate greater vulnerability.
        """
        components = [
            self.nearest_hospital_km,
            self.nearest_clinic_km,
            self.estimated_travel_time_minutes,
            self.road_access_penalty,
            self.wash_vulnerability_score,
        ]
        observed = [component for component in components if component is not None]
        if not observed:
            return None
        return sum(observed) / len(observed)
