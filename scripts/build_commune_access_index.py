"""Build the commune access index CSV from standardized input rows."""

from __future__ import annotations

import argparse
from pathlib import Path

from haiti_nippes.commune_index import build_commune_access_index
from haiti_nippes.io import read_commune_access_inputs, write_commune_access_index


DEFAULT_INPUT = Path("data/metadata/commune_access_input_template.csv")
DEFAULT_OUTPUT = Path("outputs/tables/commune_access_index.csv")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Build the Haiti Nippes commune access index."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="Input CSV with commune-level access indicators.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output CSV for scored commune-level access index.",
    )
    return parser.parse_args()


def main() -> None:
    """Read inputs, build index rows, and write the output CSV."""
    args = parse_args()
    records = read_commune_access_inputs(args.input)
    rows = build_commune_access_index(records)
    write_commune_access_index(rows, args.output)
    print(f"Wrote {len(rows)} commune access rows to {args.output}")


if __name__ == "__main__":
    main()
