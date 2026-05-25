"""Smoke-test the Haiti Nippes GIS package without requiring GIS data files."""

from __future__ import annotations

from haiti_nippes import (
    build_map_readiness_report,
    build_nippes_department,
    build_road_disruption_register,
    read_road_disruptions,
)


def main() -> None:
    """Run package-level smoke checks."""
    department = build_nippes_department()
    communes = department.communes()
    readiness_rows = build_map_readiness_report()
    road_records = read_road_disruptions("data/metadata/road_disruptions_starter.csv")
    road_rows = build_road_disruption_register(road_records)

    print("Smoke test complete")
    print("===================")
    print(f"department: {department.name}")
    print(f"communes: {len(communes)}")
    print(f"map readiness rows: {len(readiness_rows)}")
    print(f"starter road disruption rows: {len(road_rows)}")

    if len(communes) == 0:
        raise RuntimeError("No communes loaded from geography model.")
    if len(readiness_rows) == 0:
        raise RuntimeError("No map products loaded from map configuration.")
    if len(road_rows) == 0:
        raise RuntimeError("No starter road disruption rows were parsed.")


if __name__ == "__main__":
    main()
