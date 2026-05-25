"""CSV input/output helpers for the Haiti Nippes GIS workflow."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from haiti_nippes.commune_index import CommuneAccessIndexRow, CommuneAccessInput


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


def write_commune_access_index(
    rows: Iterable[CommuneAccessIndexRow],
    path: str | Path,
) -> None:
    """Write commune-level access index rows to CSV."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rows_as_dicts = [row.to_dict() for row in rows]
    if not rows_as_dicts:
        output_path.write_text("", encoding="utf-8")
        return
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows_as_dicts[0].keys()))
        writer.writeheader()
        writer.writerows(rows_as_dicts)
