# Assay Plan: Lab Partner Requirements

Date checked: 2026-04-27
Last evidence update: 2026-08-05
Status: partner-readiness note, not an unsupervised wet-lab protocol

## Purpose

Nakafa Lab needs a qualified lab partner before any candidate can move from
literature into experimental evidence. The partner does not need to accept every
research hypothesis. The minimum job is to test whether candidates affect HbF,
erythroid maturation, viability, and mature red-cell safety.

## Minimum Capabilities

| Capability | Why it matters |
| --- | --- |
| Endogenous HbF or `HBG1/HBG2` readout | avoids relying on weak K562-only evidence |
| Erythroid maturation model | checks whether HbF signal survives differentiation |
| HbF protein or F-cell readout | separates mRNA signal from functional hemoglobin signal |
| Cell viability and maturation markers | rejects toxic HbF artifacts |
| Mature red-cell hemolysis screen | blocks candidates that damage red cells |
| Red-cell metabolism or membrane-stress readout | tests pyruvate kinase, ATP, hemolysis, and red-cell-support claims |
| Alpha-globin burden and autophagy readout | tests whether HbF rescue is paired with free alpha-globin cleanup biology |
| Batch and identity tracking | keeps natural products and analogs auditable |
| Donor provenance and research-material chain of custody | keeps patient-derived HSPCs ethically governed, de-identified, and auditable |
| Basic statistics and raw data export | lets Nakafa Lab compare candidates transparently |

Preferred model order:

1. endogenous reporter or gamma-globin mRNA screen;
2. HUDEP2 or equivalent erythroid validation;
3. primary erythroid or beta-thalassemia/HbE validation when feasible;
4. mature red-cell safety screen.

## First Candidate Panel

Start small. Do not run a broad natural-product screen before the controls and
safety gates work.

| Class | Candidate or control | Reason |
| --- | --- | --- |
| Positive comparator | hydroxyurea | low-cost HbF benchmark |
| Legacy comparator | butyrate-class control | proof-of-biology HbF benchmark |
| High-caution comparator | decitabine or lab-approved epigenetic control | target boundary only |
| Repurposing comparator | sirolimus | small human beta-thalassemia signal |
| Red-cell metabolism benchmark | mitapivat or lab-approved pyruvate kinase activator reference, only if legally and practically available | separates red-cell-support biology from HbF claims |
| Natural-product-adjacent seed | `T-BDMC` only if sourced with identity proof | strongest current curcuminoid analog bridge |
| Natural-product support seed | ginger/6-shogaol-rich extract only if standardized | red-cell-support comparator, not HbF lead |
| Hazard control | known hemolytic condition chosen by the lab | calibrates rejection threshold |

The first executable version of this panel is tracked in
[First HbF and red-cell safety assay work order V0](2026-04-27-first-assay-work-order-v0.md).
The quote-ready version is tracked in
[First lab quote brief V0](2026-04-27-first-lab-quote-brief-v0.md).

## Partner Questions

Ask a potential lab partner:

- Can you measure endogenous HbF or `HBG1/HBG2` response?
- Can you distinguish HbF induction from blocked erythroid maturation?
- Can you run mature red-cell hemolysis or membrane-damage screens?
- Can you measure free or insoluble alpha-globin, `ULK1`, p62/`SQSTM1`, or an
  equivalent autophagy-flux context?
- Can you measure ATP, glycolysis-linked metabolism, deformability, membrane
  stress, or a practical equivalent for red-cell support claims?
- Can you accept de-identified thalassemia research context without giving
  patient-specific treatment advice?
- Can you export raw and summarized data for open research documentation?
- What sample type, ethics approval, and biosafety review would be required?
- Which assays are realistic in Indonesia or through remote collaboration?

Indonesian candidate settings are mapped in
[Indonesia lab partner candidate map](2026-04-27-indonesia-lab-partner-candidate-map.md).

## Apheresis-Waste Hemoglobinopathy Material-Recovery Benchmark

BioRxiv version 1, DOI `10.64898/2026.08.02.742313`, supports a
hemoglobinopathy material-recovery benchmark. The verified abstract does not
identify a beta-thalassemia donor or diagnosis-specific denominator, so it does
not yet support a beta-thalassemia material-source claim. Keep it outside the
current quote. It is not a therapy, cure, or sample-routing instruction.

A qualified partner should compare recovered material with its current source
and report:

- total patient, independent-donor, specimen, and diagnosis-specific counts,
  including repeated specimens per donor;
- beta-thalassemia donor count, genotype or phenotype, and de-identified
  provenance;
- compatible consent, ethics approval, biosafety review, and research-only
  chain of custody;
- input volume, recovered-cell yield, purity, viability, colony formation, and
  failed-run denominator;
- erythroid differentiation, maturation, enucleation, HbF, F-cells, total
  hemoglobin, globin-chain balance, free alpha-globin, and hemolysis;
- staff time, consumables, storage, quality control, and cost per qualified
  aliquot; and
- raw data plus the paired comparator definition.

Hold the route at
`preclinical_hemoglobinopathy_material_recovery_benchmark_only`. Do not add it
to a quote or experiment until beta-thalassemia provenance and the
independent-patient and specimen denominators are confirmed. Stop the route if
material quality or erythroid function is not reproducible across at least
three genetically distinct donors, recovered cells materially underperform the
comparator on globin or safety endpoints, or measured cost per qualified
aliquot is not lower.

## Stop Conditions

Stop a candidate before escalation if:

- compound or extract identity is unclear;
- HbF signal appears only with toxicity;
- erythroid maturation is impaired;
- mature red-cell hemolysis increases;
- immune, allergy, liver, kidney, or interaction risk is not reviewable;
- no qualified clinician or lab partner can audit the result.
- patient-derived material lacks compatible consent, ethics approval,
  de-identification, biosafety review, or chain of custody;
- beta-thalassemia donor material cannot reproduce acceptable cell quality and
  erythroid function against the partner's current source; or
- the measured cost per qualified aliquot is not lower than the current source.

## Linked Evidence

- [Epigenetic HbF screen V0](2026-04-27-epigenetic-hbf-screen-v0.md)
- [First HbF and red-cell safety assay work order V0](2026-04-27-first-assay-work-order-v0.md)
- [First lab quote brief V0](2026-04-27-first-lab-quote-brief-v0.md)
- [Dual HbF and alpha-globin autophagy assay spec V0](2026-04-27-dual-hbf-alpha-autophagy-assay-spec-v0.md)
- [Red-cell metabolism readout spec V0](2026-04-27-red-cell-metabolism-readout-spec-v0.md)
- [Assay-ready HbF screen](../findings/2026-04-26-assay-ready-hbf-screen.md)
- [Assay funnel for cure discovery](../findings/2026-04-26-assay-funnel-for-cure-discovery.md)
- [K562 to HUDEP2 validation guardrail](../findings/2026-04-27-k562-to-hudep2-validation-guardrail.md)
- [HUDEP2 primary validation boundary](../findings/2026-04-27-hudep2-primary-validation-boundary.md)
- [HbF responder signature V0](../prioritization/2026-04-27-hbf-responder-signature-v0.md)
- [Pyruvate kinase red-cell metabolism benchmark](../findings/2026-04-27-pyruvate-kinase-red-cell-metabolism-benchmark.md)
- [Apheresis-waste CD34-positive HSPC preprint](https://doi.org/10.64898/2026.08.02.742313)
- [Official bioRxiv API record](https://api.biorxiv.org/details/biorxiv/10.64898/2026.08.02.742313)
