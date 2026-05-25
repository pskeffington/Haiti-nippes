"""Build flood and road-disruption priority registers."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Iterable

from haiti_nippes.flood_road_model import DrainageChokepoint, FloodExposureZone, RoadDisruptionRecord


@dataclass(frozen=True)
class RoadDisruptionPriorityRow:
    """Scored road-disruption register row."""

    disruption_id: str
    road_id: str | None
    location_name: str
    disruption_type: str
    passability: str
    severity_score: float
    detour_required: bool
    estimated_delay_minutes: float | None
    wet_season_only: bool
    source_id: str | None
    quality: str

    def to_dict(self) -> dict[str, object | None]:
        """Return a serializable row dictionary."""
        return asdict(self)


@dataclass(frozen=True)
class ChokepointPriorityRow:
    """Scored drainage chokepoint register row."""

    chokepoint_id: str
    name: str
    road_id: str | None
    chokepoint_type: str
    condition: str | None
    flood_susceptibility_score: float | None
    priority_score: float | None
    source_id: str | None
    quality: str

    def to_dict(self) -> dict[str, object | None]:
        """Return a serializable row dictionary."""
        return asdict(self)


@dataclass(frozen=True)
class FloodExposurePriorityRow:
    """Scored flood-exposure register row."""

    zone_id: str
    name: str
    geography_name: str
    flood_score: float | None
    return_period: str | None
    dominant_driver: str | None
    priority_score: float | None
    source_id: str | None
    quality: str

    def to_dict(self) -> dict[str, object | None]:
        """Return a serializable row dictionary."""
        return asdict(self)


def build_road_disruption_register(
    records: Iterable[RoadDisruptionRecord],
) -> list[RoadDisruptionPriorityRow]:
    """Build scored road-disruption rows."""
    return [
        RoadDisruptionPriorityRow(
            disruption_id=record.disruption_id,
            road_id=record.road_id,
            location_name=record.location_name,
            disruption_type=record.disruption_type.value,
            passability=record.passability.value,
            severity_score=record.severity_score(),
            detour_required=record.detour_required,
            estimated_delay_minutes=record.estimated_delay_minutes,
            wet_season_only=record.wet_season_only,
            source_id=record.source_id,
            quality=record.quality.value,
        )
        for record in records
    ]


def build_chokepoint_priority_register(
    records: Iterable[DrainageChokepoint],
) -> list[ChokepointPriorityRow]:
    """Build scored drainage-chokepoint rows."""
    return [
        ChokepointPriorityRow(
            chokepoint_id=record.chokepoint_id,
            name=record.name,
            road_id=record.road_id,
            chokepoint_type=record.chokepoint_type,
            condition=record.condition,
            flood_susceptibility_score=record.flood_susceptibility_score,
            priority_score=record.priority_score(),
            source_id=record.source_id,
            quality=record.quality.value,
        )
        for record in records
    ]


def build_flood_exposure_register(
    records: Iterable[FloodExposureZone],
) -> list[FloodExposurePriorityRow]:
    """Build scored flood-exposure rows."""
    return [
        FloodExposurePriorityRow(
            zone_id=record.zone_id,
            name=record.name,
            geography_name=record.geography_name,
            flood_score=record.flood_score,
            return_period=record.return_period,
            dominant_driver=record.dominant_driver,
            priority_score=record.normalized_score(),
            source_id=record.source_id,
            quality=record.quality.value,
        )
        for record in records
    ]
