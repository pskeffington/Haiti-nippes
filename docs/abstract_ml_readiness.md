# Abstract ML-readiness checklist

## Purpose

This checklist makes the Haiti Nippes maternal-health abstract readable to both human reviewers and automated scanners that evaluate whether an abstract contains a clear background, objective, population, setting, methods, evidence boundary, expected output, policy relevance, and limitation statement.

## Pass criteria

| Criterion | Required signal | Status |
|---|---|---|
| Background | Names the global-health problem and why it matters. | Included. |
| Setting | Specifies Haiti and Nippes Department without implying unsupported department-level indicators. | Included. |
| Population | Identifies pregnant and postpartum women, newborns, adolescents, displaced women and girls, and women with obstetric complications. | Included. |
| Objective | States what the project will prioritize, map, or analyze. | Included. |
| Methods | Describes source registry, commune-level inputs, referral constraints, and exploratory access index. | Included. |
| Data boundaries | Separates national statistics from Nippes-specific analytic inputs. | Included. |
| Expected outputs | Names source registry, commune-level table, referral-priority score, and policy recommendations. | Included. |
| Policy relevance | Connects outputs to skilled birth attendance, emergency obstetric referral, facility readiness, WASH, and UHC. | Included. |
| Limitation | States that derived scores are prioritization tools, not official maternal-mortality estimates. | Included. |
| Keywords | Uses classifier-friendly terms: maternal mortality, emergency obstetric care, rural access, Haiti, Nippes, skilled birth attendance, WASH, referral. | Included. |

## Abstract failure modes to avoid

- Do not claim department-level maternal mortality unless a Nippes-specific source is added.
- Do not state that the index predicts deaths.
- Do not describe placeholder CSV values as measured data.
- Do not conflate national Haiti indicators with commune-level Nippes estimates.
- Do not imply field verification or operational access.
- Do not overstate causality from source-registry inputs.

## Preferred abstract structure

```text
Background -> Objective -> Methods -> Expected outputs -> Policy relevance -> Limitations
```

## Classifier-friendly labels

- Study type: applied public-health policy analysis
- Geography: Haiti; Nippes Department; commune-level analytic framework
- Population: pregnant women, postpartum women, newborns, adolescent pregnant women, displaced women and girls
- Constraint domains: travel time, road disruption, facility readiness, WASH access, displacement pressure, food insecurity, blood-product access
- Target: maternal-health access prioritization and emergency obstetric referral readiness
- Output: source-tagged maternal-access index and policy brief
