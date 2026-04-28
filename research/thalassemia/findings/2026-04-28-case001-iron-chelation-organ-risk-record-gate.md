# Case-001 Iron Chelation Organ-Risk Record Gate

Date: 2026-04-28
Status: de-identified record gate, not treatment advice
Evidence label: guideline + PubMed snapshot synthesis

## Bottom Line

Case-001 remains `iron_packet_missing`.

Weekly transfusion plus reported daily chelation makes the iron and chelation
packet a high-priority blocker. Nakafa Lab cannot judge patient relevance for
HbF rescue, iron-axis, metabolic, immune, transplant, gene-therapy, or trial
lanes until iron input, iron storage, organ distribution, chelation coverage,
and chelator toxicity monitoring are documented or explicitly unavailable.

This gate does not ask for a medicine change. It asks for records that a
hematologist can interpret.

## What Is Known

- The family reports weekly transfusion.
- The family reports daily medicine consistent with chelation or related care,
  but the drug name, dose, schedule, adherence, side effects, and monitoring are
  not yet recorded.
- Current ferritin trend, liver iron concentration, cardiac `T2*`, endocrine
  screen, kidney/liver monitoring, and chelator-toxicity packet are not yet
  documented in the repo.

## Why This Is A Gate

The TIF 2025 iron-overload chapter states that repeated transfusion inevitably
loads iron because humans lack an active excess-iron excretion mechanism.
Chelation therefore has two roles: balancing iron input and output, and
reducing reactive iron toxicity. The same guideline also warns that ferritin is
best interpreted as a trend and can be confounded by inflammation, infection,
hepatitis, tissue injury, chelator type, and discordance with liver iron.

For this case, that means:

- ferritin alone cannot close cardiac or organ risk;
- liver iron concentration cannot reliably exclude myocardial iron;
- cardiac `T2*` is a separate safety gate;
- chelator identity and adherence matter because missed coverage can change
  `NTBI` or labile-iron risk;
- chelator toxicity monitoring matters before any candidate is ranked;
- endocrine, bone, liver, kidney, infection, spleen, and immune context must be
  treated as part of the same organ-risk packet.

## Record Requests For The Hematologist

Ask for these as records, not as instructions:

1. Serial ferritin values with dates and context around infection,
   inflammation, hepatitis, immune flare, or tissue injury.
2. Liver iron concentration by MRI, including date, method, field strength if
   available, analysis method, and units.
3. Cardiac `T2*` MRI, including date, method, center calibration, and LVEF or
   echo/MRI context.
4. Chelator name, dose, schedule, missed-dose/adherence barriers, side effects,
   and current monitoring plan.
5. Kidney, liver, blood-count, hearing, eye, GI, and drug-interaction
   monitoring as relevant to the exact chelator.
6. Endocrine and bone monitoring: glucose or diabetes status, thyroid,
   parathyroid, gonadal axis, vitamin D, growth/puberty history if relevant,
   and bone health.
7. Transfusion iron-input records: dates, unit count, volume, product type,
   body weight, hematocrit or pure red-cell volume, and interval.
8. Liver-virus, infection, inflammation, autoimmune, and spleen context that
   could confound ferritin or chelation decisions.

## Decision Labels

Keep using the existing iron-risk labels:

- `iron_packet_missing`: the packet is not yet complete enough for
  interpretation.
- `ferritin_trend_only`: ferritin is available, but LIC and cardiac `T2*` are
  missing.
- `lic_known`: liver iron concentration is documented with date and method.
- `cardiac_t2star_known`: cardiac `T2*` is documented with date and method.
- `organ_screen_incomplete`: heart, liver, endocrine, kidney, bone, infection,
  or spleen context is incomplete.
- `chelation_review_needed`: chelator identity, dose, schedule, adherence,
  tolerability, or monitoring is incomplete.
- `toxicity_review_needed`: possible chelator toxicity or monitoring gaps need
  clinician review.
- `specialist_managed`: a hematologist has reviewed the packet with current
  records.

Case-001 currently stays in `iron_packet_missing`, with `chelation_review_needed`,
`toxicity_review_needed`, and `organ_screen_incomplete` as active sublabels.

## Research Consequences

Do not promote any patient-specific candidate while this gate is open if it:

- might increase iron absorption;
- might interfere with chelation;
- depends on liver, kidney, immune, or cardiac safety context;
- claims organ-risk benefit from antioxidant markers alone;
- ignores transfusion iron input or MRI organ distribution;
- treats Quran 57:25 as an iron-supplement claim.

This gate also affects the no-lab research loop. Computational ranking can
continue, but every candidate must be marked `patient_relevance_blocked` until
the iron/chelation packet is known or a clinician says the missing records are
not required for that decision.

## Notebook Result

The reproducible notebook ranks the missing records by immediate-risk,
interpretation, referral, and safety pressure. It places cardiac `T2*`, liver
iron concentration, chelator identity/plan, ferritin trend context, and
chelator-toxicity monitoring as the top case-001 requests.

- [Case-001 iron chelation organ-risk record gate notebook](../notebooks/2026-04-28-case001-iron-chelation-organ-risk-record-gate.ipynb)

## Islamic Research Boundary

Quran 57:25 is an iron guardrail, not an iron-supplement instruction. Quran
55:7-9 supports disciplined measurement and balance. The repo should use these
anchors to avoid exaggeration and to require expert review when harm and
benefit can coexist in the same biological system.

## Sources

- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [Iron overload organ-risk gate](2026-04-27-iron-overload-organ-risk-gate.md)
- [TDT iron MRI and chelation monitoring snapshot](../../../data/literature/pubmed/2026-04-28-case001-tdt-iron-mri-chelation-monitoring.json)
- [TDT endocrine iron monitoring snapshot](../../../data/literature/pubmed/2026-04-28-case001-tdt-endocrine-iron-monitoring.json)
- [Ferritin and MRI discordance snapshot](../../../data/literature/pubmed/2026-04-28-case001-ferritin-mri-discordance.json)
- [Chelation safety monitoring snapshot](../../../data/literature/pubmed/2026-04-28-case001-chelation-safety-monitoring.json)
- [Deferiprone neutrophil-risk snapshot](../../../data/literature/pubmed/2026-04-28-case001-deferiprone-neutrophil-risk.json)
- [Deferasirox renal/hepatic-risk snapshot](../../../data/literature/pubmed/2026-04-28-case001-deferasirox-renal-hepatic-risk.json)
- [Quran 57:25 iron guardrail](../../islamic/quran/057-al-hadid/025.md)
- [Quran 55:7-9 mizan guardrail](../../islamic/quran/055-ar-rahman/007-009.md)
