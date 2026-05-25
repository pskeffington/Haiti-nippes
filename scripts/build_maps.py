"""Build standard Haiti Nippes GIS map products."""

from __future__ import annotations

from haiti_nippes.map_builder import build_all_maps


def main() -> None:
    """Build all standard map products and print written paths."""
    written_paths = build_all_maps()
    print("Map build complete")
    print("==================")
    for path in written_paths:
        print(path)


if __name__ == "__main__":
    main()
