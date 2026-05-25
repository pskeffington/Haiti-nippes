"""Static map builders for Haiti Nippes GIS products."""

from __future__ import annotations

from pathlib import Path

from haiti_nippes.map_config import MapProductSpec, map_products


def _write_placeholder_map(product: MapProductSpec) -> None:
    """Write a text placeholder when required geospatial layers are unavailable."""
    product.output_path.parent.mkdir(parents=True, exist_ok=True)
    missing = product.missing_layers()
    lines = [
        product.title,
        "=" * len(product.title),
        "",
        "Map not rendered because required layer files are missing.",
        "",
        "Missing required layers:",
    ]
    if missing:
        lines.extend(f"- {layer.name}: {layer.path}" for layer in missing)
    else:
        lines.append("- none")
    lines.extend(
        [
            "",
            "Expected optional layers:",
            *[f"- {layer.name}: {layer.path}" for layer in product.layers if not layer.required],
            "",
            f"Notes: {product.notes}",
        ]
    )
    placeholder_path = product.output_path.with_suffix(".txt")
    placeholder_path.write_text("\n".join(lines), encoding="utf-8")


def _render_geopandas_map(product: MapProductSpec) -> None:
    """Render a simple layered static map with GeoPandas and Matplotlib."""
    import geopandas as gpd
    import matplotlib.pyplot as plt

    product.output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 10))

    rendered_any_layer = False
    for layer in product.layers:
        if not layer.exists():
            continue
        frame = gpd.read_file(layer.path)
        if frame.empty:
            continue
        if frame.crs is not None:
            frame = frame.to_crs(epsg=4326)
        if layer.geometry_type == "polygon":
            frame.boundary.plot(ax=ax, linewidth=0.8)
            frame.plot(ax=ax, alpha=0.12)
        elif layer.geometry_type == "line":
            frame.plot(ax=ax, linewidth=0.8)
        elif layer.geometry_type == "point":
            frame.plot(ax=ax, markersize=25)
        else:
            frame.plot(ax=ax)
        rendered_any_layer = True

    if not rendered_any_layer:
        plt.close(fig)
        _write_placeholder_map(product)
        return

    ax.set_title(product.title)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.text(
        0.01,
        0.01,
        product.notes,
        transform=ax.transAxes,
        fontsize=8,
        va="bottom",
        ha="left",
    )
    fig.tight_layout()
    fig.savefig(product.output_path, dpi=200)
    plt.close(fig)


def build_map_product(product: MapProductSpec) -> Path:
    """Build one map product and return the path that was written."""
    if not product.ready():
        _write_placeholder_map(product)
        return product.output_path.with_suffix(".txt")
    try:
        _render_geopandas_map(product)
        return product.output_path
    except ImportError:
        _write_placeholder_map(product)
        return product.output_path.with_suffix(".txt")


def build_all_maps() -> list[Path]:
    """Build every standard map product."""
    return [build_map_product(product) for product in map_products()]
