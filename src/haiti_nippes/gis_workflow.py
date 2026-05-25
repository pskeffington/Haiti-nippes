"""GIS workflow helpers for Haiti Nippes maps and spatial joins."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GisLayer:
    """Expected geospatial layer with local path and metadata."""

    name: str
    path: Path
    geometry_type: str
    source_id: str
    required: bool = True

    def exists(self) -> bool:
        """Return whether the layer path currently exists."""
        return self.path.exists()


@dataclass(frozen=True)
class GisWorkflowConfig:
    """Filesystem configuration for the GIS workflow."""

    data_dir: Path = Path("data")
    output_dir: Path = Path("outputs/maps")

    @property
    def raw_dir(self) -> Path:
        """Raw data directory."""
        return self.data_dir / "raw"

    @property
    def processed_dir(self) -> Path:
        """Processed data directory."""
        return self.data_dir / "processed"


def expected_layers(config: GisWorkflowConfig | None = None) -> tuple[GisLayer, ...]:
    """Return the first-pass GIS layers expected by the project."""
    cfg = config or GisWorkflowConfig()
    return (
        GisLayer(
            name="Nippes communes",
            path=cfg.processed_dir / "nippes_communes.geojson",
            geometry_type="polygon",
            source_id="SRC-001",
        ),
        GisLayer(
            name="Nippes department boundary",
            path=cfg.processed_dir / "nippes_department.geojson",
            geometry_type="polygon",
            source_id="SRC-001",
        ),
        GisLayer(
            name="2021 earthquake epicenter",
            path=cfg.processed_dir / "earthquake_2021_epicenter.geojson",
            geometry_type="point",
            source_id="SRC-002",
        ),
        GisLayer(
            name="Road network",
            path=cfg.processed_dir / "roads.geojson",
            geometry_type="line",
            source_id="SRC-001",
            required=False,
        ),
        GisLayer(
            name="Health facilities",
            path=cfg.processed_dir / "health_facilities.geojson",
            geometry_type="point",
            source_id="SRC-004",
            required=False,
        ),
    )


def validate_layer_manifest(layers: tuple[GisLayer, ...] | None = None) -> dict[str, list[str]]:
    """Validate expected GIS files and return missing required/optional layers."""
    target_layers = layers or expected_layers()
    missing_required = [layer.name for layer in target_layers if layer.required and not layer.exists()]
    missing_optional = [layer.name for layer in target_layers if not layer.required and not layer.exists()]
    present = [layer.name for layer in target_layers if layer.exists()]
    return {
        "present": present,
        "missing_required": missing_required,
        "missing_optional": missing_optional,
    }


def ensure_output_dirs(config: GisWorkflowConfig | None = None) -> None:
    """Create output directories needed by map-generation workflows."""
    cfg = config or GisWorkflowConfig()
    cfg.output_dir.mkdir(parents=True, exist_ok=True)
    cfg.processed_dir.mkdir(parents=True, exist_ok=True)


def main() -> None:
    """Print the current GIS layer readiness status."""
    ensure_output_dirs()
    status = validate_layer_manifest()
    print("GIS layer readiness")
    print("===================")
    for key, values in status.items():
        print(f"{key}:")
        if values:
            for value in values:
                print(f"  - {value}")
        else:
            print("  - none")


if __name__ == "__main__":
    main()
