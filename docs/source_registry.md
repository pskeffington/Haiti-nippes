# Source registry

This registry tracks source leads for the Haiti Nippes GIS and public-health recovery project. Keep claims tied to a source record before moving them into briefs, maps, or analysis outputs.

## Priority sources

| Id | Theme | Source lead | Publisher | Geography | Notes |
|---|---|---|---|---|---|
| SRC-001 | Administrative boundaries | Haiti subnational administrative boundary / COD-AB datasets | HDX / humanitarian geodata partners | National, department, commune | Use for department, arrondissement, commune, and communal-section geometries where licensing permits. |
| SRC-002 | Seismic hazard | M 7.2 Nippes, Haiti event page | USGS | Epicentral area and southern peninsula | Anchor event geometry, shake intensity, ground-failure layers, and earthquake date metadata. |
| SRC-003 | Population | Department and commune population baselines | IHSI / Haiti statistical sources | Department and commune | Use official or best-available population estimates for denominators. |
| SRC-004 | Humanitarian situation | Haiti earthquake situation reports | OCHA / ReliefWeb | Southern peninsula, including Nippes | Use for timeline, affected population, infrastructure damage, and operational constraints. |
| SRC-005 | WASH | Haiti WASH, water access, sanitation, and cholera-related reporting | UNICEF / WHO / PAHO / WASH Cluster | Department or commune where available | Use for WASH risk indicators and service-restoration context. |
| SRC-006 | Food security | Haiti acute food insecurity and livelihoods reporting | WFP / IPC / FEWS NET | Department or livelihood zone | Use for food-security overlay and vulnerability scoring. |
| SRC-007 | Flood and road disruption | Flood-prone roads, bridge/culvert chokepoints, landslide corridors, road washouts, passability observations | HDX / OpenStreetMap / humanitarian logistics sources / field verification | Department, commune, road corridor, chokepoint | Use for wet-season access penalties, flood exposure maps, and road-disruption registers. |

## Intake fields

Use these fields when turning source leads into source records:

- `id`
- `title`
- `publisher`
- `publication_date`
- `access_date`
- `url`
- `geography`
- `scale`
- `license`
- `reliability_notes`
- `planned_use`

## Source-handling rules

- Prefer official Haitian government, UN/OCHA, HDX, USGS, WHO/PAHO, UNICEF, WFP, IPC, FEWS NET, and peer-reviewed sources.
- Record file versions and download dates for every GIS layer.
- Keep raw geodata out of Git unless files are small, public, and licensed for redistribution.
- Store large or uncertain raw files outside the repository and document their source path here.
- Do not mix field observations with public-source data unless the provenance is clear.
