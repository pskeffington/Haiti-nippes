# GIS schema

This schema defines the minimum fields for the Haiti Nippes GIS project. The goal is to keep every map reproducible, joinable, and auditable.

## Administrative units

Use this schema for commune and communal-section boundary files.

| Field | Type | Required | Description |
|---|---:|---:|---|
| `admin_id` | string | Yes | Stable administrative unit identifier. |
| `name` | string | Yes | Unit name. |
| `admin_level` | string | Yes | Department, arrondissement, commune, or communal section. |
| `parent_id` | string | No | Parent administrative unit identifier. |
| `department` | string | Yes | Department name. |
| `arrondissement` | string | No | Arrondissement name. |
| `commune` | string | No | Commune name. |
| `population` | integer | No | Best available population estimate. |
| `population_year` | integer | No | Year of population estimate. |
| `source_id` | string | Yes | Source registry identifier. |
| `quality` | string | Yes | Data-quality flag. |

## Health facilities

Use this schema for hospitals, clinics, dispensaries, health posts, pharmacies, and mobile-care locations.

| Field | Type | Required | Description |
|---|---:|---:|---|
| `facility_id` | string | Yes | Stable facility identifier. |
| `name` | string | Yes | Facility name. |
| `facility_type` | string | Yes | Hospital, clinic, dispensary, health post, pharmacy, or unknown. |
| `operator` | string | No | Government, NGO, private, mission, or unknown. |
| `operating_status` | string | No | Open, limited, closed, damaged, unknown. |
| `capacity_level` | string | No | High, medium, low, unknown. |
| `services` | string | No | Summary of known services. |
| `commune` | string | No | Commune name. |
| `latitude` | float | Yes | WGS84 latitude. |
| `longitude` | float | Yes | WGS84 longitude. |
| `source_id` | string | Yes | Source registry identifier. |
| `quality` | string | Yes | Data-quality flag. |

## Road segments

Use this schema for road-network access analysis.

| Field | Type | Required | Description |
|---|---:|---:|---|
| `road_id` | string | Yes | Stable road segment identifier. |
| `road_class` | string | No | Primary, secondary, tertiary, residential, track, path, unknown. |
| `surface` | string | No | Paved, gravel, dirt, mixed, unknown. |
| `condition` | string | No | Good, fair, poor, impassable, unknown. |
| `passability` | string | No | All vehicle, high-clearance, foot only, blocked, unknown. |
| `bridge_or_chokepoint` | boolean | Yes | Whether the segment contains or depends on a chokepoint. |
| `wet_season_penalty` | float | Yes | Travel-time multiplier under wet-season conditions. |
| `source_id` | string | Yes | Source registry identifier. |
| `quality` | string | Yes | Data-quality flag. |

## WASH records

Use this schema for water, sanitation, hygiene, and waterborne-disease risk indicators.

| Field | Type | Required | Description |
|---|---:|---:|---|
| `wash_id` | string | Yes | Stable WASH record identifier. |
| `geography_id` | string | Yes | Linked administrative or settlement identifier. |
| `geography_name` | string | Yes | Human-readable geography name. |
| `water_access_score` | float | No | Normalized 0-1 score where higher means worse access. |
| `sanitation_access_score` | float | No | Normalized 0-1 score where higher means worse access. |
| `cholera_or_waterborne_risk` | float | No | Normalized 0-1 risk score. |
| `functional_water_points` | integer | No | Count of known functional water points. |
| `nonfunctional_water_points` | integer | No | Count of known nonfunctional water points. |
| `source_id` | string | Yes | Source registry identifier. |
| `quality` | string | Yes | Data-quality flag. |

## Commune access index

Use this schema for the final commune-level output table.

| Field | Type | Required | Description |
|---|---:|---:|---|
| `commune` | string | Yes | Commune name. |
| `nearest_hospital_km` | float | No | Distance to nearest hospital. |
| `nearest_clinic_km` | float | No | Distance to nearest clinic or lower-level health facility. |
| `travel_time_minutes` | float | No | Estimated travel time to nearest service point. |
| `road_access_score` | float | No | Normalized 0-1 score where higher means worse road access. |
| `wash_vulnerability_score` | float | No | Normalized 0-1 score where higher means worse WASH vulnerability. |
| `population_exposure` | integer | No | Exposed population denominator. |
| `compound_vulnerability_index` | float | No | Transparent weighted index. |
| `data_gap_count` | integer | Yes | Count of missing required analytic inputs. |
| `quality` | string | Yes | Final quality flag. |
