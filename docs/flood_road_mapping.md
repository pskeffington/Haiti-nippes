# Flood and road-disruption mapping

This track identifies places where flooding, drainage failure, landslides, bridges, culverts, or road washouts can break access to health care, WASH repair, markets, and emergency response.

## Core questions

- Which roads become degraded, high-clearance-only, foot-only, or blocked during flood or wet-season conditions?
- Which bridges, culverts, fords, and drainage points are likely chokepoints?
- Which communes lose practical access to hospitals or clinics when flooded road segments are penalized?
- Which WASH repair areas are hard to reach after rainfall, flooding, or landslides?
- Which locations require field verification before operational routing decisions are made?

## Required layers

| Layer | Geometry | File target | Purpose |
|---|---:|---|---|
| Road network | Line | `data/processed/roads.geojson` | Base network for access and routing. |
| Road disruptions | Point | `data/processed/road_disruptions.geojson` | Observed or modeled blocked/degraded locations. |
| Drainage chokepoints | Point | `data/processed/drainage_chokepoints.geojson` | Bridges, culverts, fords, washout-prone crossings. |
| Flood exposure zones | Polygon | `data/processed/flood_exposure_zones.geojson` | Flood-prone corridors or areas. |
| Health facilities | Point | `data/processed/health_facilities.geojson` | Access destinations. |
| WASH sites | Point or table | `data/processed/wash_sites.geojson` | Repair/service destinations. |

## Road disruption fields

| Field | Type | Description |
|---|---:|---|
| `disruption_id` | string | Stable identifier. |
| `road_id` | string | Linked road segment ID if known. |
| `location_name` | string | Local place, bridge, crossing, or corridor name. |
| `disruption_type` | string | Flooding, landslide, bridge failure, culvert failure, washout, debris, or unknown. |
| `passability` | string | Open, degraded, high-clearance only, foot only, blocked, or unknown. |
| `flood_depth_m` | float | Estimated water depth if known. |
| `detour_required` | boolean | Whether practical routing needs a detour. |
| `estimated_delay_minutes` | float | Added travel time if known. |
| `wet_season_only` | boolean | Whether the disruption is seasonal. |
| `source_id` | string | Source registry ID. |
| `quality` | string | Verified, provisional, stale, conflicting, or missing. |

## Drainage chokepoint fields

| Field | Type | Description |
|---|---:|---|
| `chokepoint_id` | string | Stable identifier. |
| `name` | string | Bridge, culvert, ford, or crossing name. |
| `road_id` | string | Linked road segment ID if known. |
| `chokepoint_type` | string | Bridge, culvert, ford, drainage, river crossing, or unknown. |
| `condition` | string | Good, fair, poor, failed, unknown. |
| `flood_susceptibility_score` | float | 0-1 score where higher means more flood-prone. |
| `source_id` | string | Source registry ID. |
| `quality` | string | Data-quality flag. |

## Flood exposure fields

| Field | Type | Description |
|---|---:|---|
| `zone_id` | string | Stable identifier. |
| `name` | string | Zone or corridor name. |
| `geography_name` | string | Commune, settlement, or corridor. |
| `flood_score` | float | 0-1 score where higher means greater exposure. |
| `return_period` | string | Flood return period or scenario if available. |
| `dominant_driver` | string | Riverine, coastal, drainage, rainfall, storm surge, unknown. |
| `source_id` | string | Source registry ID. |
| `quality` | string | Data-quality flag. |

## Map products

- `outputs/maps/flood_exposure_zones.png`
- `outputs/maps/road_disruptions.png`
- `outputs/maps/drainage_chokepoints.png`
- `outputs/maps/wet_season_health_access.png`
- `outputs/tables/road_disruption_register.csv`
- `outputs/tables/chokepoint_priority_register.csv`

## Field verification checklist

- Confirm whether the road is passable by sedan, high-clearance vehicle, motorcycle, foot, or not at all.
- Confirm whether a bridge, culvert, ford, or drainage crossing is structurally intact.
- Record whether flooding is seasonal, rainfall-triggered, storm-surge related, or persistent.
- Estimate detour feasibility and delay.
- Note whether WASH repair teams or ambulances can reach the location.
- Capture date, observer, source, and confidence for every observation.
