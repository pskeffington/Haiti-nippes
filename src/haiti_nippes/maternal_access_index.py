"""Maternal-access prioritization index for Nippes Department."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from statistics import mean

from haiti_nippes.maternal_health import ReferralConstraint


class MaternalAccessPriority(StrEnum):
    """Priority classes for commune-level maternal access planning."""

    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class MaternalAccessInput:
    """Commune-level input row for maternal-access scoring.

    Missing values are allowed during source intake. Production outputs should preserve
    the missingness fields and avoid presenting exploratory scores as official estimates.
    """

    commune: str
    skilled_birth_attendance_gap_pct: float | None = None
    estimated_travel_minutes_to_referral: float | None = None
    road_disruption_score: float | None = None
    facility_readiness_gap_score: float | None = None
    wash_gap_score: float | None = None
    food_insecurity_score: float | None = None
    displacement_pressure_score: float | None = None
    constraints: tuple[ReferralConstraint, ...] = ()
    source_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class MaternalAccessIndexRow:
    """Scored commune-level maternal-access prioritization row."""

    commune: str
    index_score: float
    priority: MaternalAccessPriority
    missing_fields: tuple[str, ...]
    constraints: tuple[ReferralConstraint, ...]
    source_ids: tuple[str, ...]
    notes: str


def clamp_score(value: float) -> float:
    """Clamp a numeric score to the 0-100 range."""
    return max(0.0, min(100.0, value))


def travel_time_score(minutes: float | None) -> float | None:
    """Convert referral travel time into a 0-100 risk score."""
    if minutes is None:
        return None
    if minutes <= 30:
        return 10.0
    if minutes <= 60:
        return 35.0
    if minutes <= 120:
        return 70.0
    return 100.0


def constraint_penalty(constraints: tuple[ReferralConstraint, ...]) -> float:
    """Return a bounded risk penalty for listed referral constraints."""
    high_weight_constraints = {
        ReferralConstraint.ROAD_PASSABILITY,
        ReferralConstraint.TRANSPORT_AVAILABILITY,
        ReferralConstraint.FACILITY_READINESS,
        ReferralConstraint.BLOOD_PRODUCT_ACCESS,
        ReferralConstraint.SECURITY,
    }
    base = 0.0
    for constraint in constraints:
        base += 8.0 if constraint in high_weight_constraints else 4.0
    return clamp_score(base)


def classify_priority(score: float) -> MaternalAccessPriority:
    """Classify a maternal-access score into a planning priority class."""
    if score >= 75:
        return MaternalAccessPriority.CRITICAL
    if score >= 55:
        return MaternalAccessPriority.HIGH
    if score >= 35:
        return MaternalAccessPriority.MODERATE
    return MaternalAccessPriority.LOW


def build_maternal_access_row(input_row: MaternalAccessInput) -> MaternalAccessIndexRow:
    """Build a maternal-access index row from a commune-level input record."""
    raw_scores = {
        "skilled_birth_attendance_gap_pct": input_row.skilled_birth_attendance_gap_pct,
        "estimated_travel_minutes_to_referral": travel_time_score(
            input_row.estimated_travel_minutes_to_referral
        ),
        "road_disruption_score": input_row.road_disruption_score,
        "facility_readiness_gap_score": input_row.facility_readiness_gap_score,
        "wash_gap_score": input_row.wash_gap_score,
        "food_insecurity_score": input_row.food_insecurity_score,
        "displacement_pressure_score": input_row.displacement_pressure_score,
    }
    missing_fields = tuple(name for name, value in raw_scores.items() if value is None)
    available_scores = [clamp_score(value) for value in raw_scores.values() if value is not None]
    base_score = mean(available_scores) if available_scores else 0.0
    final_score = clamp_score(base_score + constraint_penalty(input_row.constraints))
    return MaternalAccessIndexRow(
        commune=input_row.commune,
        index_score=round(final_score, 2),
        priority=classify_priority(final_score),
        missing_fields=missing_fields,
        constraints=input_row.constraints,
        source_ids=input_row.source_ids,
        notes="Exploratory prioritization score; not an official maternal mortality estimate.",
    )


def build_maternal_access_index(
    input_rows: tuple[MaternalAccessInput, ...],
) -> tuple[MaternalAccessIndexRow, ...]:
    """Build a stable commune-level maternal-access index table."""
    return tuple(build_maternal_access_row(row) for row in input_rows)
