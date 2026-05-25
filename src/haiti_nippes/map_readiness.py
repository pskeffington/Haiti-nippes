"""Map readiness reporting for Haiti Nippes GIS layers."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path

from haiti_nippes.map_config import MapProductSpec, map_products


@dataclass(frozen=True)
class MapReadinessRow:
    """Readiness status for one map product."""

    map_name: str
    output_path: str
    ready: bool
    missing_required_layers: str
    missing_optional_layers: str
    notes: str

    def to_dict(self) -> dict[str, object]:
        """Return a serializable row dictionary."""
        return asdict(self)


def build_map_readiness_row(product: MapProductSpec) -> MapReadinessRow:
    """Build one map-readiness row."""
    missing_required = [layer.name for layer in product.layers if layer.required and not layer.exists()]
    missing_optional = [layer.name for layer in product.layers if not layer.required and not layer.exists()]
    return MapReadinessRow(
        map_name=product.name,
        output_path=str(product.output_path),
        ready=not missing_required,
        missing_required_layers="; ".join(missing_required),
        missing_optional_layers="; ".join(missing_optional),
        notes=product.notes,
    )


def build_map_readiness_report(
    products: tuple[MapProductSpec, ...] | None = None,
) -> list[MapReadinessRow]:
    """Build readiness rows for all standard map products."""
    target_products = products or map_products()
    return [build_map_readiness_row(product) for product in target_products]


def write_map_readiness_report(
    rows: list[MapReadinessRow],
    path: str | Path = "outputs/tables/map_readiness_report.csv",
) -> None:
    """Write map-readiness rows to CSV."""
    import csv

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rows_as_dicts = [row.to_dict() for row in rows]
    if not rows_as_dicts:
        output_path.write_text("", encoding="utf-8")
        return
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows_as_dicts[0].keys()))
        writer.writeheader()
        writer.writerows(rows_as_dicts)
