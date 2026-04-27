# Iron Overload Organ-Risk Gate

Date: 2026-04-27
Status: doctor-facing data gate, not treatment advice

## Bottom Line

For a transfusion-dependent thalassemia case with weekly transfusions, iron
overload is not a side issue. It is a near-term organ-risk gate that must be
measured before Nakafa Lab can rank any candidate as clinically relevant.

This is not a cure lane by itself. It is a safety and context gate for heart,
liver, endocrine, pancreas, kidney, chelation, and adherence risk.

## Why This Matters

The TIF 2025 iron-overload chapter states that repeated transfusions inevitably
load iron because humans lack a way to excrete excess iron. It also separates
two clinical problems:

- iron accumulation from transfusion and ineffective erythropoiesis;
- toxicity from reactive iron species when chelation coverage is inadequate.

That means the useful question is not "should the patient get more iron?" The
question is whether iron input, iron storage, organ distribution, chelation
coverage, and toxicity monitoring are known.

## Evidence Snapshot

| Source | Signal | Repo implication |
| --- | --- | --- |
| TIF 2025 iron-overload chapter | iron overload can damage heart, liver, endocrine organs, and other tissues; chelation aims to balance iron input and excretion while avoiding over-chelation | collect organ-risk packet before candidate ranking |
| TIF 2025 myocardial iron section | locally validated myocardial `T2*` MRI is recommended as part of yearly monitoring in multi-transfused patients at risk | ferritin alone is not enough for cardiac-risk interpretation |
| Cardiac iron meta-analysis | cardiac iron overload and cardiovascular complications remain common in beta-thalassemia major cohorts | cardiac gate stays high priority |
| Cardiac `T2*` monitoring study | severe cardiac siderosis improved over follow-up with chelation optimization; cardiac `T2*` did not correlate cleanly with ferritin, liver iron, or LVEF in that cohort | discordant markers should trigger specialist review |
| Ferritin/MRI studies | ferritin can correlate with liver iron but can mislead for cardiac, pancreatic, splenic, or total-body iron distribution | use ferritin trend as screening, not final organ map |
| Endocrine complication studies | endocrine complications appear in TDT and relate to iron burden; established endocrine damage can become hard to reverse | ask for proactive endocrine monitoring |

## Decision Labels

Use these labels in case notes and doctor conversations:

- `iron_packet_missing`: ferritin, LIC, cardiac `T2*`, chelation, and organ
  monitoring are not yet documented.
- `ferritin_trend_only`: ferritin is known, but liver/cardiac MRI is missing.
- `lic_known`: liver iron concentration is documented.
- `cardiac_t2star_known`: cardiac `T2*` is documented with date and method.
- `organ_screen_incomplete`: liver, cardiac, endocrine, kidney, or bone
  monitoring is missing.
- `chelation_review_needed`: chelator name, dose, adherence, tolerability, or
  monitoring is incomplete.
- `toxicity_review_needed`: kidney, liver, hearing, eye, GI, neutrophil, or
  drug-interaction concerns need clinician review.
- `specialist_managed`: a hematologist has reviewed iron burden and chelation
  using current records.

## Doctor Packet

Ask the hematologist to review the following as a single packet:

- ferritin values over time, not one isolated number;
- liver iron concentration by MRI, including date, method, and units;
- cardiac `T2*` MRI, including date, method, and whether the center is
  calibrated for this measurement;
- current chelator name, dose, schedule, adherence barriers, side effects, and
  monitoring plan;
- kidney and liver function monitoring relevant to chelation;
- heart monitoring: cardiac `T2*`, LVEF method, ECG/echo or MRI context;
- endocrine monitoring: growth/puberty history if relevant, diabetes,
  thyroid, parathyroid, gonadal axis, vitamin D, and bone health;
- infection and liver-virus context if ferritin suddenly rises;
- whether autoimmune disease or immune medicines change chelation, transplant,
  trial, or infection-risk decisions.

## Research Consequences

No candidate should be promoted as patient-relevant if it:

- increases iron absorption without a clear clinician-reviewed reason;
- interferes with chelation;
- worsens liver, kidney, cardiac, endocrine, or immune risk;
- only improves an antioxidant marker while ignoring HbF, transfusion burden,
  organ iron, or hemolysis;
- relies on Quran 57:25 as an iron-supplement claim.

This gate also protects the iron-axis research lane. Hepcidin, ferroportin,
`TMPRSS6`, erythroferrone, `NTBI`, and labile plasma iron remain mechanistic
research targets, not self-treatment instructions.

## Islamic Research Boundary

Quran 57:25 motivates reflection on iron's strength and benefit, while Quran
55:7-9 reinforces measurement and balance. For this project, the biomedical
meaning is disciplined measurement: iron can be essential and dangerous in the
same patient.

These verses do not justify iron supplementation for thalassemia.

## Sources

- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [Cardiac complications and iron overload meta-analysis, PMID 30729283](https://pubmed.ncbi.nlm.nih.gov/30729283/)
- [Cardiac T2* MRI monitoring, PMID 33919601](https://pubmed.ncbi.nlm.nih.gov/33919601/)
- [Low ferritin can mislead cardiac-risk interpretation, PMID 16798647](https://pubmed.ncbi.nlm.nih.gov/16798647/)
- [Organ-specific iron distribution by MRI T2*, PMID 22943064](https://pubmed.ncbi.nlm.nih.gov/22943064/)
- [Endocrine complications in TDT, PMID 38817060](https://pubmed.ncbi.nlm.nih.gov/38817060/)
- [TDT T2* MRI organ-overload study, PMID 40224685](https://pubmed.ncbi.nlm.nih.gov/40224685/)
- [Iron-overload organ-risk selected abstracts](../../../data/literature/pubmed/2026-04-27-iron-overload-organ-risk-selected-abstracts.xml)
- [TDT iron MRI and chelation search snapshot](../../../data/literature/pubmed/2026-04-27-tdt-iron-overload-mri-chelation-search.json)
- [Ferritin, liver, and cardiac T2* search snapshot](../../../data/literature/pubmed/2026-04-27-ferritin-cardiac-liver-t2star-correlation-search.json)
- [Endocrine iron-overload monitoring search snapshot](../../../data/literature/pubmed/2026-04-27-tdt-endocrine-iron-overload-monitoring-search.json)
- [Chelation and cardiac T2* survival search snapshot](../../../data/literature/pubmed/2026-04-27-chelation-cardiac-t2star-survival-search.json)
- [Quran 57:25 iron guardrail](../../islamic/quran/057-al-hadid/025.md)
- [Quran 55:7-9 mizan guardrail](../../islamic/quran/055-ar-rahman/007-009.md)
