# Maternal health framework for Nippes Department

## Purpose

This framework converts the Haiti Nippes repository from a general recovery and access scaffold into a maternal-health project workspace. It supports the course project, future briefs, commune-level tables, and access-analysis outputs focused on rural maternal survival.

## Core problem statement

Maternal mortality in rural Haiti is shaped by a chain of system constraints: delayed recognition of complications, limited antenatal continuity, weak skilled birth attendance coverage, poor road and transport access, limited emergency obstetric capacity, blood-product shortages, WASH fragility, user-fee exposure, and disaster or insecurity shocks that interrupt routine care. In Nippes, those constraints should be analyzed at the commune and referral-corridor level rather than only at the national level.

## Evidence anchor

PAHO's 2024 Health in the Americas country profile reports that Haiti's maternal mortality ratio was estimated at 350.4 deaths per 100,000 live births in 2020 and that 65.1 percent of births were attended by skilled birth personnel in 2018. PAHO also emphasizes the priority of preventable maternal deaths, emergency obstetric care, blood-product availability, and maternal and child health within universal health coverage.

UNFPA's April 2025 Haiti situation report describes deteriorating humanitarian conditions, more than 1 million internally displaced people, urgent SRH and protection needs for women and girls, continuity needs for deported pregnant women, and UNFPA-supported delivery and mobile-clinic activity during April-May 2025.

## Project question

How can Haiti's Nippes Department improve rural maternal survival by strengthening skilled birth attendance, emergency obstetric referral, facility readiness, WASH resilience, and commune-level access planning?

## Working thesis

Maternal survival in Nippes depends on a health-system access chain rather than a single facility metric. A credible policy response should combine community-based prenatal linkage, skilled birth attendance, emergency obstetric transport, blood-product access, facility-readiness monitoring, WASH resilience, and source-tagged commune-level risk analysis.

## Conceptual model

```text
Pregnancy risk
    -> household recognition and decision to seek care
    -> community health worker / antenatal contact
    -> transport and road passability
    -> first-contact facility readiness
    -> referral capacity
    -> emergency obstetric and neonatal care
    -> postpartum follow-up
    -> survival and recovery
```

## Minimum analytic units

| Unit | Role in analysis |
|---|---|
| Department | Frames the Nippes case and links to national policy. |
| Arrondissement | Groups communes for regional referral analysis. |
| Commune | Main scoring unit for maternal access and referral constraints. |
| Facility | Service-readiness and emergency obstetric care node. |
| Road or corridor | Travel-time, passability, flood, and referral-delay layer. |
| Source record | Evidence-control layer for every claim and indicator. |

## Priority indicators

| Domain | Indicator | Source status |
|---|---|---|
| Maternal mortality | Maternal mortality ratio per 100,000 live births | National indicator available from PAHO / World Bank; department-level source needed. |
| Skilled attendance | Percent of births attended by skilled health personnel | National indicator available from PAHO; department-level source needed. |
| Antenatal care | ANC contact coverage and continuity | Source lead needed. |
| Emergency care | Availability of BEmONC and CEmONC services | Facility-level source needed. |
| Referral access | Travel time to referral facility | Derived from road/facility data; requires source-tagged assumptions. |
| Blood-product access | Blood availability or referral linkage | Source lead needed. |
| WASH resilience | Water/sanitation reliability at facility or commune level | Use WASH source registry and facility-readiness sources. |
| Displacement and SRH | Pregnant women, postpartum women, GBV survivors, and displaced women/girls with SRH needs | UNFPA source lead available. |

## Policy levers

1. Strengthen prenatal identification and referral linkage through community health workers.
2. Improve skilled birth attendance coverage by connecting rural communes to reliable delivery points.
3. Map referral corridors and prioritize wet-season road, bridge, and transport constraints.
4. Identify BEmONC and CEmONC service gaps by commune and referral facility.
5. Add blood-product access as a critical emergency-obstetric-care constraint.
6. Integrate WASH resilience into maternal facility readiness.
7. Track displaced women, pregnant adolescents, newborns, and GBV survivors as priority groups.
8. Align recommendations with MSPP's Plan Directeur Sante 2021-2031 and universal health coverage framing.

## Deliverable path

```text
source_registry.md
    -> module_one_topic_selection.md
    -> maternal_health_framework.md
    -> maternal_access_inputs.csv
    -> maternal_access_index.py
    -> commune-level maternal access table
    -> final project brief / manuscript section
```

## Validation rules

- Do not publish department-level maternal indicators unless their geographic level is verified.
- Do not treat travel times as observed field data unless they come from a verified travel-time source or field-verified route log.
- Mark derived risk scores as analytic prioritization, not official burden estimates.
- Keep national statistics separate from Nippes-specific claims.
- Source every quantitative claim before moving it into final prose.
