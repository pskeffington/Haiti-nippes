# Haiti-nippes

Field-oriented repository for the Haiti Nippes project. The working purpose is to organize evidence, geospatial notes, public-health risk factors, and recovery planning for Nippes Department, Haiti, with particular attention to earthquake recovery, WASH resilience, health-access restoration, and rural service delivery.

**Maintainer:** Paul Skeffington, MS, MPH  
**Repository status:** active source-registration and field-profile scaffold.  
**Last documentation refresh:** 2026-05-26

## Current update — 2026-05-26

The repository remains in early source-registration and object-model setup. The immediate documentation priority is to build `docs/source_registry.md`, define administrative geography objects, and keep all demographic, WASH, food-security, seismic, and health-access claims tied to source-log entries before producing briefs, maps, or risk tables.

## Situation frame

Nippes is one of Haiti's ten departments, with Miragoane as its capital and an estimated 2015 population of about 342,325. The department includes coastal and rural communes across the Miragoane, Anse-a-Veau, and Baraderes arrondissements. Petit-Trou-de-Nippes was near the epicentral area of the 14 August 2021 magnitude 7.2 earthquake, which caused major loss of life, building damage, and continuing recovery needs across Haiti's southern peninsula.

## Project objectives

- Build a concise open-source profile of Nippes Department.
- Track earthquake recovery, WASH, food security, health access, and infrastructure fragility.
- Separate source notes, datasets, analytic notebooks, and publication-ready outputs.
- Keep the repository lightweight, reproducible, and easy to extend.

## Repository map

```text
Haiti-nippes/
├── README.md
├── data/                 # Raw and derived datasets, not committed unless small and public
├── docs/                 # Project briefs, source notes, and written outputs
├── notebooks/            # Exploratory analysis notebooks
├── src/                  # Reusable analysis modules
└── outputs/              # Tables, figures, and generated artifacts
```

## Initial work packages

### 1. Source registry

Create a source log for demographic, humanitarian, WASH, food-security, health-facility, seismic, and administrative-boundary references. Each source should record title, publisher, date, URL, access date, geography, and reliability notes.

### 2. Administrative geography

Define Nippes Department and its arrondissements/communes in a reusable geography file. Prioritize official Haitian statistical or humanitarian boundary sources when available.

### 3. Risk profile

Develop a short baseline profile covering seismic exposure, road access, health access, water and sanitation, food security, and post-2021 recovery constraints.

### 4. Data model

Use small, typed objects for core entities:

- `Department`
- `Arrondissement`
- `Commune`
- `SourceRecord`
- `RiskIndicator`
- `ProjectOutput`

### 5. Outputs

Target outputs include a two-page project brief, a source registry, a commune-level risk table, and a reproducible map/figure set.

## Source leads

- USGS earthquake event page for the 14 August 2021 M 7.2 Nippes earthquake.
- Haitian IHSI population estimates for department and commune population baselines.
- OCHA, ReliefWeb, UNICEF, WFP, PAHO/WHO, and IOM reporting for humanitarian and public-health indicators.
- HDX and Haiti administrative-boundary datasets for shapefiles and geocoding.

## Style rules

- Keep `README` capitalized.
- Use sentence case for section titles and project labels unless a proper noun or acronym requires capitalization.
- Keep source claims tied to citations or source-log entries.
- Avoid committing sensitive, private, or unverifiable data.

## Next action

Start with `docs/source_registry.md`, then add a minimal `src/haiti_nippes/` package for typed project objects.
