# Roadmap

## Immediate goal

Prepare the Haiti Nippes maternal-health project to pass STEM CV Curator review and abstract-readiness scanning while preserving conservative source boundaries.

## Current phase

Validation-gated abstract and object-model refinement.

## Completed surfaces

- `README.md` identifies the repository as a Haiti Nippes public-health, recovery, WASH, and rural service-delivery workspace.
- `PROJECT_STATUS.md` exposes the current status line, public summary, STEM CV Curator classification, and evidence boundary.
- `docs/structured_abstract.md` provides the human-readable structured abstract.
- `docs/abstract_eval_packet.json` provides machine-readable abstract signals for scanner review.
- `docs/abstract_ml_readiness.md` lists expected pass criteria and failure modes.
- `src/haiti_nippes/maternal_health.py` defines maternal-health service, risk, referral, indicator, capacity, and source-lead objects.
- `src/haiti_nippes/maternal_access_index.py` defines the exploratory commune-level maternal-access prioritization model.

## Next validation steps

1. Reconcile PAHO, UNFPA, WHO, World Bank, MSPP, IHSI, and HDX source leads into full source records.
2. Replace placeholder values in `data/maternal_access_inputs.csv` only when source-tagged values are available.
3. Add a method note describing how maternal-access scores are calculated and what they cannot claim.
4. Generate a sample maternal-access table using clearly marked synthetic or placeholder-safe inputs for software validation only.
5. Run the STEM CV Curator after the status surface is live so the project is captured as a public-health validation-gated object.

## Claim gates

- No unsupported department-level maternal mortality value.
- No causal inference claim.
- No prediction claim.
- No field-verification claim.
- No final policy recommendation without source reconciliation.

## Intended deliverables

- Module one topic selection draft.
- Structured abstract.
- Source registry.
- Maternal-health framework.
- Maternal-access index method note.
- Commune-level maternal-access prioritization table.
- Final policy brief or manuscript-style project section.
