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
| MAT-001 | Maternal health indicators | Health in the Americas: Haiti country profile | PAHO | National, with relevance to Nippes | Use for maternal mortality, skilled birth attendance, health financing, and rural access context. |
| MAT-002 | Sexual and reproductive health in crisis | Haiti Situation Report #3 - April 2025 | UNFPA | National and crisis-affected populations | Use for displaced women and girls, pregnant and breastfeeding women, newborns, SRH continuity, and GBV service needs. |
| MAT-003 | National health indicators | Haiti country health profile and GHO indicators | WHO | National | Cross-check maternal, neonatal, workforce, and service-delivery indicators. |
| MAT-004 | Gender and maternal-health indicators | Haiti gender data profile | World Bank Gender Data Portal | National | Cross-check maternal mortality, fertility, adolescent fertility, and gender indicators. |
| MAT-005 | Health-system policy framework | Plan Directeur Sante 2021-2031 | MSPP / Government of Haiti | National and departmental implementation context | Use for health governance, service-delivery, human resources, UHC, and maternal-child-health policy framing. |
| MAT-006 | Departmental maternal access | Departmental facility, referral, and population inputs | MSPP, IHSI, HDX, PAHO/WHO, UNFPA | Department, commune, referral corridor | Use for Nippes-specific maternal referral analysis when verified source files are identified. |

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

- Prefer official Haitian government, UN/OCHA, HDX, USGS, WHO/PAHO, UNICEF, WFP, IPC, FEWS NET, UNFPA, World Bank, and peer-reviewed sources.
- Record file versions and download dates for every GIS layer.
- Keep raw geodata out of Git unless files are small, public, and licensed for redistribution.
- Store large or uncertain raw files outside the repository and document their source path here.
- Do not mix field observations with public-source data unless the provenance is clear.
- Keep all maternal-health statistics linked to source IDs before moving them into a submission draft.
