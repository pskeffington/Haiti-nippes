"""Run the first-pass Haiti Nippes GIS pipeline."""

from __future__ import annotations

import argparse

from haiti_nippes.pipeline import run_table_pipeline


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run the Haiti Nippes GIS pipeline.")
    parser.add_argument(
        "--maps",
        action="store_true",
        help="Also build static maps or placeholder map reports.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the pipeline and print row counts plus optional map outputs."""
    args = parse_args()
    result = run_table_pipeline(build_maps=args.maps)
    print("GIS pipeline complete")
    print("=====================")
    for line in result.summary_lines():
        print(line)


if __name__ == "__main__":
    main()
