# Assay Plan: First Lab Quote Brief V0

Date checked: 2026-04-27
Status: lab-outreach draft, not treatment advice and not contact permission

## Purpose

This brief converts the current computational panel optimizer into a
quote-ready request for a qualified lab partner. It should be sent only after
explicit founder approval and only without private patient records.

The ask is feasibility and pricing for a preclinical assay panel. It is not a
request for patient treatment, supplement approval, or off-label prescribing.

## One-Paragraph Lab Ask

Nakafa Lab is building an open, source-backed thalassemia research program. We
are seeking a qualified lab partner to quote a small preclinical pilot panel
that tests whether selected comparators or seed candidates affect fetal
hemoglobin, erythroid maturation, alpha-globin/autophagy biology, and mature
red-cell safety. We will not provide identifiable patient data, raw medical
records, or patient samples unless ethics approval, consent, biosafety review,
and clinician oversight are already in place.

## First Quote Panel

| Item | Role | Why included | Boundary |
| --- | --- | --- | --- |
| Hydroxyurea | positive HbF comparator | calibrates whether the assay detects a known HbF-positive signal | comparator only, not a new cure claim |
| Purified resveratrol | HbF seed tested against HPFH-like readouts | low-friction seed with prior beta-thalassemia erythroid-precursor signal | seed only until endogenous HbF and safety replication |
| Sirolimus | mTOR/autophagy comparator | connects HbF/gamma-globin signal with `ULK1` and alpha-globin cleanup questions | immune-active comparator, not patient-facing |
| Standardized 6-shogaol-rich ginger extract | red-cell support comparator | tests red-cell support or hemolysis-protection claims separately from HbF | support endpoint only |
| Melittin hazard control | hemolysis rejection threshold | calibrates mature red-cell damage and blocks unsafe bee-venom framing | hazard control only, not therapy |

Expansion items if the lab can support them:

- `T-BDMC`-like curcuminoid analog, only with exact compound identity and batch
  documentation;
- mitapivat or a lab-approved pyruvate kinase activator reference, only if
  legally and practically obtainable.

The later dual-readout prioritizer keeps this first quote panel unchanged. It
adds `AMPKB1` / `NRF2`, pyruvate kinase activation, and `T-BDMC`-like chemistry
as expansion-only lanes when the lab can support the identity, alpha-globin,
autophagy, maturation, viability, and hemolysis gates.

The `AMPKB1` / `NRF2` expansion gate keeps selective probes as assay-only and
keeps metformin as a low-priority warning comparator, not a lead, because the
retrieved NTDT human study did not show extra benefit over stable hydroxyurea.

The `AHSP` buffer gate adds `AHSP` as an optional expanded readout, not as a
required first-panel endpoint and not as a therapy lane. It is useful if the lab
can measure alpha-globin buffering beside HbF, alpha-globin burden, autophagy,
maturation, viability, and hemolysis.

## Required Feasibility Questions

Ask the lab to answer:

- Which erythroid model can you run: HUDEP2, CD34+ erythroid differentiation,
  beta-thalassemia/HbE cells, or another validated model?
- Can you measure `HBG1` / `HBG2` messenger RNA?
- Can you measure HbF protein or F-cell percentage?
- Can you measure erythroid maturation markers such as `CD71` and `CD235a`?
- Can you measure viability and apoptosis?
- Can you run mature red-cell hemolysis or membrane-damage assays?
- Can you measure alpha/non-alpha globin balance or free alpha-globin burden?
- For sirolimus, can you measure `ULK1`, p62 / `SQSTM1`, or another
  flux-aware autophagy readout?
- Can you measure `AHSP` mRNA or protein if it is kept as an optional expanded
  alpha-globin-buffer readout?
- Can you document compound or extract identity, vehicle, concentration range,
  replicates, raw data, and methods?
- What ethics, biosafety, material-transfer, or import constraints apply?

## Minimum Quote Output

Request a quote that separates:

- assay model setup;
- candidate procurement or material requirements;
- per-candidate cost;
- per-readout cost;
- replicate count;
- estimated timeline;
- raw-data export format;
- statistical summary format;
- limitations or assays the lab cannot run.

## Stop Conditions

Do not proceed if:

- the lab asks for identifiable patient data before a formal ethics path exists;
- compound identity or extract standardization cannot be documented;
- hemolysis safety cannot be tested;
- viability or erythroid maturation cannot be measured;
- the lab frames the panel as treatment validation instead of preclinical
  screening.

## Privacy And Security Boundary

Send only public research context and de-identified summaries. Do not send
names, exact birth dates, hospital numbers, contact details, raw clinical
records, screenshots, prescriptions, lab reports, or private family notes.

## Sources

- [First wet-lab panel optimizer result](../findings/2026-04-27-first-wet-lab-panel-optimizer-result.md)
- [Dual-readout panel prioritizer result](../findings/2026-04-27-dual-readout-panel-prioritizer-result.md)
- [AMPK/NRF2 expansion gate](../findings/2026-04-27-ampk-nrf2-expansion-gate.md)
- [AHSP alpha-globin buffer gate](../findings/2026-04-27-ahsp-alpha-globin-buffer-gate.md)
- [First HbF and red-cell safety assay work order V0](2026-04-27-first-assay-work-order-v0.md)
- [Lab partner requirements](2026-04-27-lab-partner-requirements.md)
- [Indonesia lab partner candidate map](2026-04-27-indonesia-lab-partner-candidate-map.md)
- [Experiment status boundary](../findings/2026-04-27-experiment-status-boundary.md)
- [Quran 16:43 expert-consultation guardrail](../../islamic/quran/016-an-nahl/043.md)
