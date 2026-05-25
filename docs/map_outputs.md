# Map outputs

This file defines the standard map products for the Haiti Nippes GIS project. Each map should be reproducible from documented source layers and should include a data-quality note.

## Health access distance

**Output:** `outputs/maps/health_access_distance.png`

**Purpose:** Show which communes, settlements, or road-access zones are farthest from hospitals, clinics, dispensaries, and health posts.

**Required inputs:**

- Commune or settlement layer
- Health-facility point layer
- Facility type and operating-status fields

**Recommended views:**

- Distance to nearest hospital
- Distance to nearest clinic or lower-level facility
- Facilities by type and operating status

## Health access travel time

**Output:** `outputs/maps/health_access_travel_time.png`

**Purpose:** Estimate practical access burden by accounting for roads, surface type, road class, and seasonal passability.

**Required inputs:**

- Road network
- Road class and surface fields
- Road-condition or passability fields
- Health-facility points

**Recommended views:**

- Travel time to nearest hospital
- Travel time to nearest clinic or health post
- Areas exceeding 60, 90, and 120 minutes

## Road access condition

**Output:** `outputs/maps/road_access_condition.png`

**Purpose:** Identify roads, bridges, and chokepoints that may constrain emergency response, WASH repair, or medical evacuation.

**Required inputs:**

- Road network
- Road class
- Passability or condition field
- Bridge and chokepoint observations where available

**Recommended views:**

- Poor or unknown road segments
- Wet-season penalty segments
- Single-access or low-redundancy corridors

## WASH access

**Output:** `outputs/maps/wash_access.png`

**Purpose:** Show water and sanitation access gaps and prioritize places where WASH stress overlaps with poor health access.

**Required inputs:**

- Commune or settlement layer
- WASH indicators or water-point locations
- Functional/nonfunctional status where available

**Recommended views:**

- Water access score
- Sanitation access score
- Waterborne-disease risk flags
- Functional versus nonfunctional water points

## Compound access vulnerability

**Output:** `outputs/maps/compound_access_vulnerability.png`

**Purpose:** Combine health access, road access, WASH vulnerability, and population exposure into a transparent prioritization layer.

**Required inputs:**

- Commune boundaries
- Health access distance or travel-time outputs
- Road access score
- WASH vulnerability score
- Population exposure

**Recommended views:**

- Compound vulnerability index
- Component small multiples
- Data-gap overlay

## Data gap register

**Output:** `outputs/tables/data_gap_register.csv`

**Purpose:** Track missing or unreliable inputs that affect operational confidence.

**Minimum fields:**

- `geography_name`
- `missing_layer`
- `impact`
- `priority`
- `recommended_fix`
- `source_lead`

## Commune access index

**Output:** `outputs/tables/commune_access_index.csv`

**Purpose:** Produce a compact analytic table for prioritization, project briefs, and later dashboards.

**Minimum fields:**

- `commune`
- `nearest_hospital_km`
- `nearest_clinic_km`
- `travel_time_minutes`
- `road_access_score`
- `wash_vulnerability_score`
- `population_exposure`
- `compound_vulnerability_index`
- `data_gap_count`
- `quality`
