# Runbook

This runbook describes the current reproducible workflow for the Haiti Nippes GIS project.

## Setup

Install the project in editable mode from the repository root:

```bash
python -m pip install -e .
```

Install optional GIS dependencies when working with geospatial files:

```bash
python -m pip install -e '.[gis]'
```

## Validate expected GIS layers

Run the GIS manifest check:

```bash
python src/haiti_nippes/gis_workflow.py
```

Expected early-stage result: commune, department, and earthquake layers will be missing until real processed GeoJSON files are added. Road, health, flood, and chokepoint layers are tracked as optional because they may arrive in stages.

## Run the combined GIS table pipeline

The combined table pipeline reads the commune-access template plus the starter flood and road records, then writes all current table outputs:

```bash
python scripts/run_gis_pipeline.py
```

Default outputs:

```text
outputs/tables/commune_access_index.csv
outputs/tables/road_disruption_register.csv
outputs/tables/chokepoint_priority_register.csv
outputs/tables/flood_exposure_register.csv
```

## Build static maps

Build the standard map products:

```bash
python scripts/build_maps.py
```

If required GeoJSON layers are missing, the map builder writes text placeholders explaining which layer files are needed. Once processed layers are added, it writes PNG maps to:

```text
outputs/maps/health_access_distance.png
outputs/maps/road_access_condition.png
outputs/maps/flood_exposure_zones.png
outputs/maps/wash_access.png
outputs/maps/compound_access_vulnerability.png
```

## Build commune access index only

Fill or replace:

```text
data/metadata/commune_access_input_template.csv
```

Then run:

```bash
build-commune-access-index
```

Default output:

```text
outputs/tables/commune_access_index.csv
```

## Build flood and road-disruption registers only

Fill or replace these templates or use the starter files:

```text
data/metadata/road_disruptions_template.csv
data/metadata/drainage_chokepoints_template.csv
data/metadata/flood_exposure_zones_template.csv
data/metadata/road_disruptions_starter.csv
data/metadata/drainage_chokepoints_starter.csv
data/metadata/flood_exposure_zones_starter.csv
```

Then run:

```bash
build-flood-road-registers
```

Default outputs:

```text
outputs/tables/road_disruption_register.csv
outputs/tables/chokepoint_priority_register.csv
outputs/tables/flood_exposure_register.csv
```

## Data priorities

The next useful data pass should add:

1. Commune and department boundaries.
2. Health facility points with operating status.
3. Road network with class, surface, and passability fields.
4. Flood-prone corridors, bridges, culverts, and drainage chokepoints.
5. WASH access indicators or water-point records.

## Quality discipline

Every row should preserve:

- `source_id`
- `quality`
- date or source notes where available
- uncertainty flags when public datasets disagree

Do not treat generated scores as operational ground truth until source records and field verification support them.
