"""Typed maternal-health planning objects for the Haiti Nippes project."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class MaternalServiceType(StrEnum):
    """Maternal, newborn, and SRH service categories tracked by the project."""

    ANTENATAL_CARE = "antenatal_care"
    SKILLED_BIRTH_ATTENDANCE = "skilled_birth_attendance"
    BASIC_EMERGENCY_OBSTETRIC_CARE = "basic_emergency_obstetric_care"
    COMPREHENSIVE_EMERGENCY_OBSTETRIC_CARE = "comprehensive_emergency_obstetric_care"
    POSTPARTUM_CARE = "postpartum_care"
    NEONATAL_STABILIZATION = "neonatal_stabilization"
    FAMILY_PLANNING = "family_planning"
    GBV_SURVIVOR_CARE = "gbv_survivor_care"


class ReferralConstraint(StrEnum):
    """Common barriers that can interrupt maternal referral pathways."""

    DISTANCE = "distance"
    ROAD_PASSABILITY = "road_passability"
    TRANSPORT_AVAILABILITY = "transport_availability"
    COST = "cost"
    SECURITY = "security"
    FACILITY_READINESS = "facility_readiness"
    STAFFING = "staffing"
    BLOOD_PRODUCT_ACCESS = "blood_product_access"
    WASH = "wash"
    COMMUNICATIONS = "communications"


class MaternalRiskGroup(StrEnum):
    """Subpopulations prioritized for maternal-health access analysis."""

    PREGNANT_WOMEN = "pregnant_women"
    POSTPARTUM_WOMEN = "postpartum_women"
    ADOLESCENT_PREGNANT_WOMEN = "adolescent_pregnant_women"
    NEWBORNS = "newborns"
    LACTATING_WOMEN = "lactating_women"
    DISPLACED_WOMEN_AND_GIRLS = "displaced_women_and_girls"
    GBV_SURVIVORS = "gbv_survivors"
    WOMEN_WITH_OBSTETRIC_COMPLICATIONS = "women_with_obstetric_complications"


@dataclass(frozen=True)
class MaternalHealthIndicator:
    """Source-tagged maternal-health indicator definition."""

    name: str
    geography: str
    value: float | None = None
    unit: str | None = None
    year: int | None = None
    source_id: str | None = None
    notes: str = ""


@dataclass(frozen=True)
class MaternalServiceCapacity:
    """Facility or commune-level maternal-service capacity record."""

    geography: str
    services: tuple[MaternalServiceType, ...]
    source_id: str | None = None
    constraints: tuple[ReferralConstraint, ...] = field(default_factory=tuple)
    notes: str = ""

    def offers(self, service_type: MaternalServiceType) -> bool:
        """Return whether the capacity record includes a service type."""
        return service_type in self.services


@dataclass(frozen=True)
class MaternalReferralProfile:
    """Commune-level profile of referral barriers for obstetric emergencies."""

    commune: str
    nearest_referral_facility: str | None = None
    estimated_travel_minutes: float | None = None
    constraints: tuple[ReferralConstraint, ...] = field(default_factory=tuple)
    source_id: str | None = None
    notes: str = ""

    def has_constraint(self, constraint: ReferralConstraint) -> bool:
        """Return whether a referral constraint is present."""
        return constraint in self.constraints


@dataclass(frozen=True)
class MaternalSourceLead:
    """Lightweight source lead used before full registry reconciliation."""

    source_id: str
    title: str
    publisher: str
    url: str
    planned_use: str
    geography: str = "Haiti / Nippes"
    confidence: str = "source lead"


def priority_maternal_source_leads() -> tuple[MaternalSourceLead, ...]:
    """Return current source leads for the maternal-health course layer."""
    return (
        MaternalSourceLead(
            source_id="MAT-001",
            title="Health in the Americas: Haiti country profile",
            publisher="Pan American Health Organization",
            url="https://hia.paho.org/en/country-profiles/haiti",
            planned_use="Maternal mortality, skilled birth attendance, health financing, and access context.",
        ),
        MaternalSourceLead(
            source_id="MAT-002",
            title="Haiti Situation Report #3 - April 2025",
            publisher="United Nations Population Fund",
            url="https://haiti.unfpa.org/en/publications/haiti-situation-report-3-april-2025",
            planned_use="Sexual and reproductive health needs among displaced women, pregnant women, newborns, and girls.",
        ),
        MaternalSourceLead(
            source_id="MAT-003",
            title="Haiti country health profile",
            publisher="World Health Organization",
            url="https://www.who.int/countries/hti/",
            planned_use="Cross-check national maternal, neonatal, and health-system indicators.",
        ),
        MaternalSourceLead(
            source_id="MAT-004",
            title="Haiti gender data profile",
            publisher="World Bank Gender Data Portal",
            url="https://genderdata.worldbank.org/en/economies/haiti",
            planned_use="Cross-check maternal mortality, fertility, adolescent fertility, and gender indicators.",
        ),
    )
