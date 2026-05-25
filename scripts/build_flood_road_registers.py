"""Build flood and road-disruption priority registers."""

from __future__ import annotations

import argparse
from pathlib import Path

from haiti_nippes.flood_road_index import (
    build_chokepoint_priority_register,
    build_flood_exposure_register,
    build_road_disruption_register,
)
from haiti_nippes.io import (
    read_drainage_chokepoints,
    read_flood_exposure_zones,
    read_road_disruptions,
    write_chokepoint_priority_register,
    write_flood_exposure_register,
    write_road_disruption_register,
)


DEFAULT_ROAD_INPUT = Path("data/metadata/road_disruptions_template.csv")
DEFAULT_CHOKEPOINT_INPUT = Path("data/metadata/drainage_chokepoints_template.csv")
DEFAULT_FLOOD_INPUT = Path("data/metadata/flood_exposure_zones_template.csv")
DEFAULT_ROAD_OUTPUT = Path("outputs/tables/road_disruption_register.csv")
DEFAULT_CHOKEPOINT_OUTPUT = Path("outputs/tables/chokepoint_priority_register.csv")
DEFAULT_FLOOD_OUTPUT = Path("outputs/tables/flood_exposure_register.csv")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Build Haiti Nippes flood and road-disruption registers."
    )
    parser.add_argument("--road-input", type=Path, default=DEFAULT_ROAD_INPUT)
    parser.add_argument("--chokepoint-input", type=Path, default=DEFAULT_CHOKEPOINT_INPUT)
    parser.add_argument("--flood-input", type=Path, default=DEFAULT_FLOOD_INPUT)
    parser.add_argument("--road-output", type=Path, default=DEFAULT_ROAD_OUTPUT)
    parser.add_argument("--chokepoint-output", type=Path, default=DEFAULT_CHOKEPOINT_OUTPUT)
    parser.add_argument("--flood-output", type=Path, default=DEFAULT_FLOOD_OUTPUT)
    return parser.parse_args()


def main() -> None:
    """Build all flood and road-disruption registers."""
    args = parse_args()

    road_records = read_road_disruptions(args.road_input)
    chokepoint_records = read_drainage_chokepoints(args.chokepoint_input)
    flood_records = read_flood_exposure_zones(args.flood_input)

    road_rows = build_road_disruption_register(road_records)
    chokepoint_rows = build_chokepoint_priority_register(chokepoint_records)
    flood_rows = build_flood_exposure_register(flood_records)

    write_road_disruption_register(road_rows, args.road_output)
    write_chokepoint_priority_register(chokepoint_rows, args.chokepoint_output)
    write_flood_exposure_register(flood_rows, args.flood_output)

    print(f"Wrote {len(road_rows)} road disruption rows to {args.road_output}")
    print(f"Wrote {len(chokepoint_rows)} chokepoint rows to {args.chokepoint_output}")
    print(f"Wrote {len(flood_rows)} flood exposure rows to {args.flood_output}")


if __name__ == "__main__":
    main()
