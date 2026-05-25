"""Build the Haiti Nippes map-readiness report."""

from __future__ import annotations

from haiti_nippes.map_readiness import build_map_readiness_report, write_map_readiness_report


def main() -> None:
    """Write the standard map-readiness report."""
    rows = build_map_readiness_report()
    output_path = "outputs/tables/map_readiness_report.csv"
    write_map_readiness_report(rows, output_path)
    print(f"Wrote {len(rows)} map readiness rows to {output_path}")


if __name__ == "__main__":
    main()
