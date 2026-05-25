# Data

This directory documents expected GIS and indicator datasets for the Haiti Nippes project.

Large raw datasets should not be committed unless they are small, public, and licensed for redistribution. Store large files externally and document their source, version, and local path in `docs/source_registry.md`.

## Planned layers

| Layer | Geometry | Expected source | Status | Notes |
|---|---:|---|---|---|
| Nippes department boundary | Polygon | HDX / COD-AB | Planned | Department outline for project maps. |
| Nippes communes | Polygon | HDX / COD-AB | Planned | Commune-level joins and choropleths. |
| Roads | Line | HDX / OSM-derived humanitarian extract | Planned | Access and isolation analysis. |
| Health facilities | Point | HDX / MSPP / humanitarian source | Planned | Validate source date before use. |
| Earthquake epicenter | Point | USGS | Planned | 14 August 2021 M 7.2 event. |
| Shaking / intensity | Raster or polygon | USGS / ShakeMap | Planned | Use for exposure overlays. |
| WASH indicators | Table or point | UNICEF / WASH Cluster | Planned | Commune-level indicators where available. |
| Food-security indicators | Table or polygon | IPC / WFP / FEWS NET | Planned | Department or livelihood-zone overlays. |

## Directory convention

```text
data/
├── raw/          # Source files, preferably ignored if large
├── processed/    # Cleaned geospatial layers and joined tables
└── metadata/     # Data dictionaries, source manifests, and checksums
```

## Minimum metadata

Every dataset should have:

- Source title
- Publisher
- Download date
- Publication or version date
- URL or source path
- License or reuse note
- Coordinate reference system
- Geometry type
- Processing notes
