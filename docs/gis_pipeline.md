# GIS pipeline

This pipeline turns raw public GIS and indicator data into reproducible access maps for Nippes Department.

## Pipeline stages

### 1. Intake

Collect raw source files and record each source in `docs/source_registry.md` before analysis.

Expected inputs:

- Administrative boundaries
- Road network
- Health-facility points
- WASH indicators or water-point records
- Population exposure table or raster
- Earthquake and hazard layers

### 2. Standardization

Convert raw files into project schemas defined in `docs/gis_schema.md`.

Standardization tasks:

- Reproject geospatial layers to a common working CRS.
- Normalize commune and arrondissement names.
- Assign `source_id` and `quality` fields.
- Create stable IDs for facilities, roads, WASH records, and administrative units.
- Export cleaned files to `data/processed/`.

### 3. Validation

Validate required fields, geometry type, coordinate reference system, and missing data.

Validation outputs:

- `outputs/tables/data_gap_register.csv`
- Console or log summary of missing required fields
- Quality flags for each input layer

### 4. Access analysis

Generate distance and access indicators.

Core outputs:

- Distance to nearest hospital
- Distance to nearest clinic or health post
- Estimated travel time to nearest service point
- Road access score
- WASH vulnerability score
- Compound commune vulnerability index

### 5. Map production

Generate standard maps defined in `docs/map_outputs.md`.

Expected maps:

- Health access distance
- Health access travel time
- Road access condition
- WASH access
- Compound access vulnerability

### 6. Review and field verification

Flag uncertain records for verification. Treat maps as decision-support tools, not definitive ground truth, until sources are verified.

## Working assumptions

- All source claims require a source registry entry.
- Missing data should be visible in outputs instead of silently dropped.
- Commune-level products are the first stable target.
- Facility-level and road-network analyses should remain provisional until facility status and road passability are verified.

## Priority development order

1. Commune and department boundaries.
2. Health-facility point inventory.
3. Road network and passability attributes.
4. WASH indicators.
5. Population exposure joins.
6. Compound index and map exports.
