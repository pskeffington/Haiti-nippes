"""Console entry points for the Haiti Nippes GIS project."""

from __future__ import annotations

import argparse
from pathlib import Path

from haiti_nippes.commune_index import build_commune_access_index
from haiti_nippes.flood_road_index import (
    build_chokepoint_priority_register,
    build_flood_exposure_register,
    build_road_disruption_register,
)
from haiti_nippes.io import (
    read_commune_access_inputs,
    read_drainage_chokepoints,
    read_flood_exposure_zones,
    read_road_disruptions,
    write_chokepoint_priority_register,
    write_commune_access_index,
    write_flood_exposure_register,
    write_road_disruption_register,
)
from haiti_nippes.map_builder import build_all_maps
from haiti_nippes.map_readiness import build_map_readiness_report, write_map_readiness_report
from haiti_nippes.pipeline import run_table_pipeline


DEFAULT_COMMUNE_INPUT = Path("data/metadata/commune_access_input_template.csv")
DEFAULT_COMMUNE_OUTPUT = Path("outputs/tables/commune_access_index.csv")
DEFAULT_ROAD_INPUT = Path("data/metadata/road_disruptions_template.csv")
DEFAULT_CHOKEPOINT_INPUT = Path("data/metadata/drainage_chokepoints_template.csv")
DEFAULT_FLOOD_INPUT = Path("data/metadata/flood_exposure_zones_template.csv")
DEFAULT_ROAD_OUTPUT = Path("outputs/tables/road_disruption_register.csv")
DEFAULT_CHOKEPOINT_OUTPUT = Path("outputs/tables/chokepoint_priority_register.csv")
DEFAULT_FLOOD_OUTPUT = Path("outputs/tables/flood_exposure_register.csv")
DEFAULT_READINESS_OUTPUT = Path("outputs/tables/map_readiness_report.csv")


def build_commune_access_index_cli() -> None:
    """Build the commune access index CSV from standardized input rows."""
    parser = argparse.ArgumentParser(
        description="Build the Haiti Nippes commune access index."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_COMMUNE_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_COMMUNE_OUTPUT)
    args = parser.parse_args()

    records = read_commune_access_inputs(args.input)
    rows = build_commune_access_index(records)
    write_commune_access_index(rows, args.output)
    print(f"Wrote {len(rows)} commune access rows to {args.output}")


def build_flood_road_registers_cli() -> None:
    """Build flood and road-disruption priority registers."""
    parser = argparse.ArgumentParser(
        description="Build Haiti Nippes flood and road-disruption registers."
    )
    parser.add_argument("--road-input", type=Path, default=DEFAULT_ROAD_INPUT)
    parser.add_argument("--chokepoint-input", type=Path, default=DEFAULT_CHOKEPOINT_INPUT)
    parser.add_argument("--flood-input", type=Path, default=DEFAULT_FLOOD_INPUT)
    parser.add_argument("--road-output", type=Path, default=DEFAULT_ROAD_OUTPUT)
    parser.add_argument("--chokepoint-output", type=Path, default=DEFAULT_CHOKEPOINT_OUTPUT)
    parser.add_argument("--flood-output", type=Path, default=DEFAULT_FLOOD_OUTPUT)
    args = parser.parse_args()

    road_rows = build_road_disruption_register(read_road_disruptions(args.road_input))
    chokepoint_rows = build_chokepoint_priority_register(
        read_drainage_chokepoints(args.chokepoint_input)
    )
    flood_rows = build_flood_exposure_register(read_flood_exposure_zones(args.flood_input))

    write_road_disruption_register(road_rows, args.road_output)
    write_chokepoint_priority_register(chokepoint_rows, args.chokepoint_output)
    write_flood_exposure_register(flood_rows, args.flood_output)

    print(f"Wrote {len(road_rows)} road disruption rows to {args.road_output}")
    print(f"Wrote {len(chokepoint_rows)} chokepoint rows to {args.chokepoint_output}")
    print(f"Wrote {len(flood_rows)} flood exposure rows to {args.flood_output}")


def run_gis_pipeline_cli() -> None:
    """Run the first-pass Haiti Nippes GIS pipeline."""
    parser = argparse.ArgumentParser(description="Run the Haiti Nippes GIS pipeline.")
    parser.add_argument(
        "--maps",
        action="store_true",
        help="Also build static maps or placeholder map reports.",
    )
    args = parser.parse_args()

    result = run_table_pipeline(build_maps=args.maps)
    print("GIS pipeline complete")
    print("=====================")
    for line in result.summary_lines():
        print(line)


def build_maps_cli() -> None:
    """Build standard Haiti Nippes GIS map products."""
    written_paths = build_all_maps()
    print("Map build complete")
    print("==================")
    for path in written_paths:
        print(path)


def build_map_readiness_cli() -> None:
    """Build the Haiti Nippes map-readiness report."""
    rows = build_map_readiness_report()
    write_map_readiness_report(rows, DEFAULT_READINESS_OUTPUT)
    print(f"Wrote {len(rows)} map readiness rows to {DEFAULT_READINESS_OUTPUT}")
