"""CSV IO helpers for the maternal-access index."""

from __future__ import annotations

import csv
from pathlib import Path

from haiti_nippes.maternal_access_index import (
    MaternalAccessIndexRow,
    MaternalAccessInput,
    build_maternal_access_index,
)
from haiti_nippes.maternal_health import ReferralConstraint


def _float_or_none(value: str | None) -> float | None:
    """Parse an optional numeric field."""
    if value is None:
        return None
    stripped = value.strip()
    if not stripped:
        return None
    return float(stripped)


def _split_tokens(value: str | None) -> tuple[str, ...]:
    """Split semicolon or pipe-delimited tokens."""
    if value is None:
        return ()
    normalized = value.replace("|", ";")
    return tuple(token.strip() for token in normalized.split(";") if token.strip())


def _parse_constraints(value: str | None) -> tuple[ReferralConstraint, ...]:
    """Parse constraint tokens into ReferralConstraint enum values.

    Unknown tokens are ignored so source-intake files can preserve notes without
    breaking the scoring pipeline. Use the validation report to audit omissions.
    """
    parsed: list[ReferralConstraint] = []
    for token in _split_tokens(value):
        normalized = token.strip().lower().replace("-", "_").replace(" ", "_")
        try:
            parsed.append(ReferralConstraint(normalized))
        except ValueError:
            continue
    return tuple(parsed)


def read_maternal_access_inputs(path: str | Path) -> tuple[MaternalAccessInput, ...]:
    """Read maternal-access input rows from CSV."""
    rows: list[MaternalAccessInput] = []
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows.append(
                MaternalAccessInput(
                    commune=row["commune"].strip(),
                    skilled_birth_attendance_gap_pct=_float_or_none(
                        row.get("skilled_birth_attendance_gap_pct")
                    ),
                    estimated_travel_minutes_to_referral=_float_or_none(
                        row.get("estimated_travel_minutes_to_referral")
                    ),
                    road_disruption_score=_float_or_none(row.get("road_disruption_score")),
                    facility_readiness_gap_score=_float_or_none(
                        row.get("facility_readiness_gap_score")
                    ),
                    wash_gap_score=_float_or_none(row.get("wash_gap_score")),
                    food_insecurity_score=_float_or_none(row.get("food_insecurity_score")),
                    displacement_pressure_score=_float_or_none(
                        row.get("displacement_pressure_score")
                    ),
                    constraints=_parse_constraints(row.get("constraints")),
                    source_ids=_split_tokens(row.get("source_ids")),
                )
            )
    return tuple(rows)


def write_maternal_access_index(
    rows: tuple[MaternalAccessIndexRow, ...], path: str | Path
) -> None:
    """Write maternal-access index rows to CSV."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "commune",
                "index_score",
                "priority",
                "missing_fields",
                "missing_field_count",
                "constraints",
                "source_ids",
                "notes",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "commune": row.commune,
                    "index_score": row.index_score,
                    "priority": row.priority.value,
                    "missing_fields": ";".join(row.missing_fields),
                    "missing_field_count": len(row.missing_fields),
                    "constraints": ";".join(constraint.value for constraint in row.constraints),
                    "source_ids": ";".join(row.source_ids),
                    "notes": row.notes,
                }
            )


def score_maternal_access_csv(input_path: str | Path, output_path: str | Path) -> tuple[MaternalAccessIndexRow, ...]:
    """Read, score, and write the maternal-access index CSV."""
    inputs = read_maternal_access_inputs(input_path)
    scored = build_maternal_access_index(inputs)
    write_maternal_access_index(scored, output_path)
    return scored
