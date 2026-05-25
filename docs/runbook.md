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

## Build commune access index

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

## Build flood and road-disruption registers

Fill or replace these templates:

```text
data/metadata/road_disruptions_template.csv
data/metadata/drainage_chokepoints_template.csv
data/metadata/flood_exposure_zones_template.csv
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
