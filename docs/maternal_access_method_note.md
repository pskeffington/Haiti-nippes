# Maternal access index method note

## Purpose

The maternal access index is an exploratory commune-level prioritization tool for the Haiti Nippes maternal-health project. It is designed to organize source-tagged evidence about referral barriers and emergency obstetric care readiness. It is not an official epidemiologic estimate, mortality model, prediction model, or causal inference model.

## Unit of analysis

The primary unit is the commune. Each row in the input table represents one Nippes commune and can later be linked to arrondissements, referral corridors, health facilities, road segments, WASH records, and population denominators.

## Input domains

| Domain | Field | Interpretation |
|---|---|---|
| Skilled birth attendance | `skilled_birth_attendance_gap_pct` | Estimated gap or vulnerability score related to skilled delivery coverage. |
| Referral travel time | `estimated_travel_minutes_to_referral` | Estimated travel time from commune or settlement proxy to referral facility. |
| Road disruption | `road_disruption_score` | Source-tagged road, flood, passability, or chokepoint risk score. |
| Facility readiness | `facility_readiness_gap_score` | Gap in maternal, newborn, BEmONC, CEmONC, staffing, supplies, or blood-product readiness. |
| WASH | `wash_gap_score` | Water, sanitation, hygiene, or facility WASH fragility relevant to safe delivery. |
| Food insecurity | `food_insecurity_score` | Food-security vulnerability used as a background maternal-risk stressor. |
| Displacement pressure | `displacement_pressure_score` | Population movement, IDP, returnee, deportee, or crisis-pressure signal affecting SRH needs. |
| Referral constraints | `constraints` | Categorical barriers such as road passability, transport availability, blood-product access, security, staffing, and communications. |
| Source IDs | `source_ids` | Evidence-control field linking each row to source-registry records. |

## Scoring logic

The implementation in `src/haiti_nippes/maternal_access_index.py` converts available input domains to bounded 0-100 risk scores, averages available values, and adds a bounded referral-constraint penalty. Missing values are preserved in the output as `missing_fields` rather than imputed. The score is then classified as low, moderate, high, or critical planning priority.

## Priority classes

| Class | Score range | Meaning |
|---|---:|---|
| Low | 0 to <35 | Lower relative access priority based on available evidence. |
| Moderate | 35 to <55 | Meaningful access concern requiring source completion or monitoring. |
| High | 55 to <75 | Strong planning concern across one or more access domains. |
| Critical | 75 to 100 | Highest planning priority for review, source completion, or intervention targeting. |

## Data-quality rules

- Missing values are not treated as zero risk.
- Missing values are listed in every output row.
- A score with many missing fields should be treated as low-confidence even when the numeric value is high or low.
- National indicators should not be copied into commune rows unless the row clearly labels them as national proxies.
- Synthetic values may be used only to validate software behavior and must be labeled as synthetic.

## Claim boundaries

The index can support statements such as source-completion priority, identification of documented or hypothesized maternal referral constraints, access-domain bottleneck review, and evidence-gap tracking.

The index cannot support claims that a commune has the highest maternal mortality rate, that the score predicts maternal deaths, that the score proves intervention effects, that placeholder values are observed field measurements, or that departmental claims are verified without source-registry support.

## Minimum readiness before public output

A public-facing table should include commune name, score, priority class, missing-field count, source IDs, notes on whether values are observed or derived, and a limitation statement that the table is a prioritization aid rather than an official estimate.

## Recommended next implementation

Create a reader for `data/maternal_access_inputs.csv` that parses constraints and source IDs, generates `MaternalAccessInput` objects, exports scored rows to `outputs/maternal_access_index.csv`, and writes a validation report that counts missing fields by commune.
