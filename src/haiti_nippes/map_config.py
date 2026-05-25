"""Map configuration objects for Haiti Nippes GIS outputs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MapLayerSpec:
    """A geospatial layer used by a map product."""

    name: str
    path: Path
    geometry_type: str
    required: bool = True

    def exists(self) -> bool:
        """Return whether the layer file exists."""
        return self.path.exists()


@dataclass(frozen=True)
class MapProductSpec:
    """Specification for a reproducible map product."""

    name: str
    output_path: Path
    title: str
    layers: tuple[MapLayerSpec, ...]
    notes: str

    def missing_layers(self) -> tuple[MapLayerSpec, ...]:
        """Return missing required layers."""
        return tuple(layer for layer in self.layers if layer.required and not layer.exists())

    def ready(self) -> bool:
        """Return whether required layers are available."""
        return not self.missing_layers()


@dataclass(frozen=True)
class MapBuildConfig:
    """Filesystem paths for map building."""

    processed_dir: Path = Path("data/processed")
    map_output_dir: Path = Path("outputs/maps")


def map_products(config: MapBuildConfig | None = None) -> tuple[MapProductSpec, ...]:
    """Return standard map products for the project."""
    cfg = config or MapBuildConfig()
    communes = MapLayerSpec(
        name="Nippes communes",
        path=cfg.processed_dir / "nippes_communes.geojson",
        geometry_type="polygon",
    )
    roads = MapLayerSpec(
        name="Road network",
        path=cfg.processed_dir / "roads.geojson",
        geometry_type="line",
        required=False,
    )
    health = MapLayerSpec(
        name="Health facilities",
        path=cfg.processed_dir / "health_facilities.geojson",
        geometry_type="point",
        required=False,
    )
    road_disruptions = MapLayerSpec(
        name="Road disruptions",
        path=cfg.processed_dir / "road_disruptions.geojson",
        geometry_type="point",
        required=False,
    )
    chokepoints = MapLayerSpec(
        name="Drainage chokepoints",
        path=cfg.processed_dir / "drainage_chokepoints.geojson",
        geometry_type="point",
        required=False,
    )
    flood_zones = MapLayerSpec(
        name="Flood exposure zones",
        path=cfg.processed_dir / "flood_exposure_zones.geojson",
        geometry_type="polygon",
        required=False,
    )
    wash_sites = MapLayerSpec(
        name="WASH sites",
        path=cfg.processed_dir / "wash_sites.geojson",
        geometry_type="point",
        required=False,
    )
    return (
        MapProductSpec(
            name="health_access_distance",
            output_path=cfg.map_output_dir / "health_access_distance.png",
            title="Nippes health access distance",
            layers=(communes, roads, health),
            notes="Shows communes, road network, and health facility destinations when available.",
        ),
        MapProductSpec(
            name="road_access_condition",
            output_path=cfg.map_output_dir / "road_access_condition.png",
            title="Nippes road access condition",
            layers=(communes, roads, road_disruptions, chokepoints),
            notes="Shows road access constraints, disruption points, and drainage chokepoints.",
        ),
        MapProductSpec(
            name="flood_exposure_zones",
            output_path=cfg.map_output_dir / "flood_exposure_zones.png",
            title="Nippes flood exposure zones",
            layers=(communes, flood_zones, roads, chokepoints),
            notes="Shows flood-prone zones and access chokepoints when flood layers are available.",
        ),
        MapProductSpec(
            name="wash_access",
            output_path=cfg.map_output_dir / "wash_access.png",
            title="Nippes WASH access",
            layers=(communes, wash_sites, roads),
            notes="Shows WASH site coverage or WASH access data when available.",
        ),
        MapProductSpec(
            name="compound_access_vulnerability",
            output_path=cfg.map_output_dir / "compound_access_vulnerability.png",
            title="Nippes compound access vulnerability",
            layers=(communes, flood_zones, roads, health, wash_sites),
            notes="Combines health, road, flood, WASH, and commune context for planning-grade review.",
        ),
    )
