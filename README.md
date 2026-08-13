# Haiti Nippes Public Health Research

Public, civic-facing research scaffold for reproducible secondary-data study of earthquake recovery, WASH resilience, health access, food security, infrastructure fragility, and rural service delivery in Nippes Department, Haiti.

**Maintainer:** Paul Skeffington, MS, MPH  
**Repository status:** source-registration and regional public-health research scaffold.  
**Last documentation review:** 2026-08-12

## Public-interest research boundary

This repository is maintained for public-health scholarship, humanitarian open-data methods, geospatial context, reproducible documentation, and regional systems analysis.

It does not provide field tasking, emergency authority, site-specific operational instructions, household-level vulnerability findings, clinical determinations, partner directives, or policy mandates. Public outputs should use source-verified, non-sensitive, appropriately aggregated information and should preserve uncertainty and data limitations.

## Research focus

The project examines Nippes Department through a reproducible regional profile covering:

- post-earthquake recovery context;
- WASH access and resilience;
- health-service access;
- food-security context;
- road and infrastructure constraints;
- administrative geography;
- public humanitarian and health indicators;
- source provenance and uncertainty.

## Core research question

How can public humanitarian, demographic, geospatial, WASH, health-access, and recovery data be organized into a reproducible regional profile of Nippes while avoiding unsupported causal, household-level, or operational claims?

## Current status

The repository remains in early source-registration and object-model development. Before briefs, maps, or comparative risk tables are treated as research evidence, source provenance, geography, update dates, and verification status should be recorded explicitly.

## Research objects

- `Department`
- `Arrondissement`
- `Commune`
- `SourceRecord`
- `RiskIndicator`
- `ProjectOutput`

These objects should support transparent data provenance and reproducible analysis rather than operational planning.

## Repository map

```text
Haiti-nippes/
├── README.md
├── data/                 # Raw and derived datasets; raw data excluded unless small and clearly redistributable
├── docs/                 # Source registry, protocols, written outputs
├── notebooks/            # Exploratory analysis
├── src/                  # Reusable analysis modules
└── outputs/              # Tables, figures, and generated artifacts
```

## Source classes

Priority source classes include official Haitian statistical sources where available, USGS earthquake records, PAHO/WHO, UNICEF, OCHA, ReliefWeb, WFP, IOM, HDX, and other public humanitarian or health-system sources with documented access and verification dates.

No source should be treated as current solely because it appears in the repository. Source date, geography, publisher, access route, and verification status should be logged before manuscript-weight use.

## Documentation standards

- Keep source claims tied to `docs/source_registry.md` or an equivalent machine-readable manifest.
- Preserve distinctions between observed data, published estimates, contextual narrative, and research interpretation.
- Avoid household-level coordinates or sensitive community vulnerability data.
- Record administrative-boundary versions and crosswalk decisions.
- Preserve uncertainty arising from displacement, incomplete reporting, changing access, and outdated denominators.
- Do not infer present conditions from post-2021 reports without date-specific verification.

## Next actions

1. Build or refresh `docs/source_registry.md` with publisher, date, URL, access date, geography, variable class, and verification status.
2. Define reusable administrative-geography files for department, arrondissement, and commune levels.
3. Build a descriptive regional indicator table with explicit source and year fields.
4. Add a methods note distinguishing descriptive secondary-data research from causal or operational assessment.
5. Create reproducible map and figure templates using non-sensitive public data.
6. Connect validated outputs to the broader public-health portfolio evidence ledger.

## Supported contribution

A reproducible, source-bounded regional public-health profile of Nippes using public humanitarian and health data.

## Unsupported contribution

No field deployment guidance, emergency response authority, household-level risk determination, clinical recommendation, or current-condition claim without source-date verification is made.
