"""Run the first-pass Haiti Nippes GIS table pipeline."""

from __future__ import annotations

from haiti_nippes.pipeline import run_table_pipeline


def main() -> None:
    """Run the pipeline and print row counts."""
    result = run_table_pipeline()
    print("GIS table pipeline complete")
    print("===========================")
    for line in result.summary_lines():
        print(line)


if __name__ == "__main__":
    main()
