"""Build commune-level access index rows from standardized inputs."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Iterable

from haiti_nippes.scoring import (
    ScoreWeights,
    distance_score,
    quality_from_missing,
    road_penalty_score,
    travel_time_score,
    weighted_index,
)


@dataclass(frozen=True)
class CommuneAccessInput:
    """Raw commune-level access indicators before scoring."""

    commune: str
    nearest_hospital_km: float | None = None
    nearest_clinic_km: float | None = None
    travel_time_minutes: float | None = None
    road_penalty_multiplier: float | None = None
    wash_vulnerability_score: float | None = None
    population_exposure: int | None = None


@dataclass(frozen=True)
class CommuneAccessIndexRow:
    """Scored commune-level access-index row."""

    commune: str
    nearest_hospital_km: float | None
    nearest_clinic_km: float | None
    travel_time_minutes: float | None
    road_access_score: float | None
    wash_vulnerability_score: float | None
    population_exposure: int | None
    compound_vulnerability_index: float | None
    data_gap_count: int
    quality: str

    def to_dict(self) -> dict[str, object | None]:
        """Return a serializable row dictionary."""
        return asdict(self)


def build_commune_access_row(
    record: CommuneAccessInput,
    weights: ScoreWeights | None = None,
) -> CommuneAccessIndexRow:
    """Build one commune-level access-index row."""
    hospital_score = distance_score(record.nearest_hospital_km)
    clinic_score = distance_score(record.nearest_clinic_km, severe_threshold_km=15.0)
    time_score = travel_time_score(record.travel_time_minutes)
    road_score = road_penalty_score(record.road_penalty_multiplier)
    wash_score = record.wash_vulnerability_score

    score_inputs = {
        "hospital_distance": hospital_score,
        "clinic_distance": clinic_score,
        "travel_time": time_score,
        "road_access": road_score,
        "wash_vulnerability": wash_score,
    }
    required_values = {
        "nearest_hospital_km": record.nearest_hospital_km,
        "nearest_clinic_km": record.nearest_clinic_km,
        "travel_time_minutes": record.travel_time_minutes,
        "road_penalty_multiplier": record.road_penalty_multiplier,
        "wash_vulnerability_score": record.wash_vulnerability_score,
    }
    data_gap_count = sum(value is None for value in required_values.values())
    return CommuneAccessIndexRow(
        commune=record.commune,
        nearest_hospital_km=record.nearest_hospital_km,
        nearest_clinic_km=record.nearest_clinic_km,
        travel_time_minutes=record.travel_time_minutes,
        road_access_score=road_score,
        wash_vulnerability_score=wash_score,
        population_exposure=record.population_exposure,
        compound_vulnerability_index=weighted_index(score_inputs, weights),
        data_gap_count=data_gap_count,
        quality=quality_from_missing(required_values),
    )


def build_commune_access_index(
    records: Iterable[CommuneAccessInput],
    weights: ScoreWeights | None = None,
) -> list[CommuneAccessIndexRow]:
    """Build a list of commune-level access-index rows."""
    return [build_commune_access_row(record, weights) for record in records]
