# GIS mapping plan

This plan defines the first analytic mapping track for the Haiti Nippes project. The GIS work should prioritize practical access and service-restoration questions rather than general cartography.

## Core mapping questions

1. Which communes and settlements are farthest from hospitals, clinics, and health posts?
2. Which areas have weak road access or likely travel-time barriers during rainy-season or disaster-response conditions?
3. Which communities face overlapping health-access, WASH-access, and food-security stress?
4. Where should mobile clinics, WASH repair teams, or supply drops be prioritized if roads degrade?
5. Which locations need field verification because public datasets disagree or are stale?

## Priority GIS layers

| Theme | Layer | Geometry | Use |
|---|---|---:|---|
| Administrative geography | Department, arrondissement, commune, communal section | Polygon | Boundary joins and summary maps. |
| Population exposure | Population grids or commune totals | Raster or table | Denominators for risk and service coverage. |
| Health access | Hospitals, clinics, dispensaries, health posts, pharmacies | Point | Distance and travel-time analysis. |
| Roads | Primary, secondary, tertiary, tracks, bridges | Line | Network access and isolation analysis. |
| Road condition | Passability, surface, bridge condition, landslide/flood exposure | Line or point | Travel-time penalty and response feasibility. |
| WASH access | Water points, piped systems, latrines, sanitation coverage, cholera reporting where available | Point, polygon, or table | WASH vulnerability and repair prioritization. |
| Hazards | Earthquake epicenter, ShakeMap, landslide susceptibility, flood-prone corridors | Point, raster, polygon | Exposure overlays. |
| Food security | IPC/WFP/FEWS NET classifications | Polygon or table | Compounded vulnerability scoring. |

## Analysis products

### Health-service distance map

Map straight-line and road-network distance to the nearest verified hospital, clinic, dispensary, or health post. Produce separate maps for all health facilities and higher-capacity facilities only.

### Travel-time access map

Estimate travel time to the nearest health facility using road classes and road-condition penalties. Where condition data is missing, classify estimates as provisional.

### Road access condition map

Rank roads and communes by likely response constraints: missing bridges, poor surface, flood exposure, landslide exposure, or lack of redundancy.

### WASH access map

Map water-point and sanitation-service coverage where data exist. Where point data are unavailable, summarize WASH indicators by commune and flag missing data.

### Compound access vulnerability map

Combine health access, road access, WASH access, and population exposure into a simple transparent index. Keep component scores visible so the index does not hide data uncertainty.

## Minimum outputs

- `outputs/maps/health_access_distance.png`
- `outputs/maps/health_access_travel_time.png`
- `outputs/maps/road_access_condition.png`
- `outputs/maps/wash_access.png`
- `outputs/tables/commune_access_index.csv`
- `outputs/tables/data_gap_register.csv`

## Data-quality flags

Use these flags in every processed dataset:

| Flag | Meaning |
|---|---|
| `verified` | Source appears authoritative and internally consistent. |
| `provisional` | Public source is plausible but needs verification. |
| `stale` | Source date is likely too old for operational decisions. |
| `conflicting` | Multiple sources disagree. |
| `missing` | Needed field or geometry is not available. |

## Field-verification priorities

- Facility name, type, operating status, and service capacity.
- Road passability by vehicle type and season.
- Bridge condition and chokepoints.
- Functional water points and WASH repair needs.
- Settlements that appear isolated by both distance and road condition.
