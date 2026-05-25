"""CSV input/output helpers for the Haiti Nippes GIS workflow."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from haiti_nippes.access_model import DataQuality
from haiti_nippes.commune_index import CommuneAccessIndexRow, CommuneAccessInput
from haiti_nippes.flood_road_index import (
    ChokepointPriorityRow,
    FloodExposurePriorityRow,
    RoadDisruptionPriorityRow,
)
from haiti_nippes.flood_road_model import (
    DisruptionType,
    DrainageChokepoint,
    FloodExposureZone,
    PassabilityStatus,
    RoadDisruptionRecord,
)


COMMUNE_ACCESS_INPUT_FIELDS = [
    "commune",
    "nearest_hospital_km",
    "nearest_clinic_km",
    "travel_time_minutes",
    "road_penalty_multiplier",
    "wash_vulnerability_score",
    "population_exposure",
]


def _parse_float(value: str | None) -> float | None:
    """Parse an optional float from CSV text."""
    if value is None or value.strip() == "":
        return None
    return float(value)


def _parse_int(value: str | None) -> int | None:
    """Parse an optional integer from CSV text."""
    if value is None or value.strip() == "":
        return None
    return int(float(value))


def _parse_bool(value: str | None, default: bool = False) -> bool:
    """Parse a boolean from CSV text."""
    if value is None or value.strip() == "":
        return default
    return value.strip().casefold() in {"1", "true", "yes", "y"}


def _parse_quality(value: str | None) -> DataQuality:
    """Parse a data-quality value with a conservative fallback."""
    try:
        return DataQuality((value or "provisional").strip())
    except ValueError:
        return DataQuality.PROVISIONAL


def _write_rows(rows: Iterable[object], path: str | Path) -> None:
    """Write dataclass-like rows with ``to_dict`` methods to CSV."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rows_as_dicts = [row.to_dict() for row in rows]  # type: ignore[attr-defined]
    if not rows_as_dicts:
        output_path.write_text("", encoding="utf-8")
        return
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows_as_dicts[0].keys()))
        writer.writeheader()
        writer.writerows(rows_as_dicts)


def read_commune_access_inputs(path: str | Path) -> list[CommuneAccessInput]:
    """Read commune-level access inputs from a CSV file."""
    csv_path = Path(path)
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        records: list[CommuneAccessInput] = []
        for row in reader:
            commune = (row.get("commune") or "").strip()
            if not commune:
                continue
            records.append(
                CommuneAccessInput(
                    commune=commune,
                    nearest_hospital_km=_parse_float(row.get("nearest_hospital_km")),
                    nearest_clinic_km=_parse_float(row.get("nearest_clinic_km")),
                    travel_time_minutes=_parse_float(row.get("travel_time_minutes")),
                    road_penalty_multiplier=_parse_float(row.get("road_penalty_multiplier")),
                    wash_vulnerability_score=_parse_float(row.get("wash_vulnerability_score")),
                    population_exposure=_parse_int(row.get("population_exposure")),
                )
            )
        return records


def read_road_disruptions(path: str | Path) -> list[RoadDisruptionRecord]:
    """Read road-disruption records from CSV."""
    csv_path = Path(path)
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        records: list[RoadDisruptionRecord] = []
        for row in reader:
            disruption_id = (row.get("disruption_id") or "").strip()
            if not disruption_id:
                continue
            records.append(
                RoadDisruptionRecord(
                    disruption_id=disruption_id,
                    road_id=(row.get("road_id") or None),
                    location_name=(row.get("location_name") or "unknown").strip(),
                    disruption_type=DisruptionType((row.get("disruption_type") or "unknown").strip()),
                    passability=PassabilityStatus((row.get("passability") or "unknown").strip()),
                    flood_depth_m=_parse_float(row.get("flood_depth_m")),
                    detour_required=_parse_bool(row.get("detour_required")),
                    estimated_delay_minutes=_parse_float(row.get("estimated_delay_minutes")),
                    wet_season_only=_parse_bool(row.get("wet_season_only"), default=True),
                    source_id=(row.get("source_id") or None),
                    quality=_parse_quality(row.get("quality")),
                )
            )
        return records


def read_drainage_chokepoints(path: str | Path) -> list[DrainageChokepoint]:
    """Read drainage chokepoint records from CSV."""
    csv_path = Path(path)
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        records: list[DrainageChokepoint] = []
        for row in reader:
            chokepoint_id = (row.get("chokepoint_id") or "").strip()
            if not chokepoint_id:
                continue
            records.append(
                DrainageChokepoint(
                    chokepoint_id=chokepoint_id,
                    name=(row.get("name") or "unknown").strip(),
                    road_id=(row.get("road_id") or None),
                    chokepoint_type=(row.get("chokepoint_type") or "unknown").strip(),
                    condition=(row.get("condition") or None),
                    flood_susceptibility_score=_parse_float(row.get("flood_susceptibility_score")),
                    source_id=(row.get("source_id") or None),
                    quality=_parse_quality(row.get("quality")),
                )
            )
        return records


def read_flood_exposure_zones(path: str | Path) -> list[FloodExposureZone]:
    """Read flood-exposure zone records from CSV."""
    csv_path = Path(path)
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        records: list[FloodExposureZone] = []
        for row in reader:
            zone_id = (row.get("zone_id") or "").strip()
            if not zone_id:
                continue
            records.append(
                FloodExposureZone(
                    zone_id=zone_id,
                    name=(row.get("name") or "unknown").strip(),
                    geography_name=(row.get("geography_name") or "unknown").strip(),
                    flood_score=_parse_float(row.get("flood_score")),
                    return_period=(row.get("return_period") or None),
                    dominant_driver=(row.get("dominant_driver") or None),
                    source_id=(row.get("source_id") or None),
                    quality=_parse_quality(row.get("quality")),
                )
            )
        return records


def write_commune_access_index(
    rows: Iterable[CommuneAccessIndexRow],
    path: str | Path,
) -> None:
    """Write commune-level access index rows to CSV."""
    _write_rows(rows, path)


def write_road_disruption_register(
    rows: Iterable[RoadDisruptionPriorityRow],
    path: str | Path,
) -> None:
    """Write road-disruption priority rows to CSV."""
    _write_rows(rows, path)


def write_chokepoint_priority_register(
    rows: Iterable[ChokepointPriorityRow],
    path: str | Path,
) -> None:
    """Write drainage-chokepoint priority rows to CSV."""
    _write_rows(rows, path)


def write_flood_exposure_register(
    rows: Iterable[FloodExposurePriorityRow],
    path: str | Path,
) -> None:
    """Write flood-exposure priority rows to CSV."""
    _write_rows(rows, path)
