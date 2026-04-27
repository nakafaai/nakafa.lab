# Assay Plan: Lab Partner Requirements

Date checked: 2026-04-27
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
| Batch and identity tracking | keeps natural products and analogs auditable |
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

## Partner Questions

Ask a potential lab partner:

- Can you measure endogenous HbF or `HBG1/HBG2` response?
- Can you distinguish HbF induction from blocked erythroid maturation?
- Can you run mature red-cell hemolysis or membrane-damage screens?
- Can you measure ATP, glycolysis-linked metabolism, deformability, membrane
  stress, or a practical equivalent for red-cell support claims?
- Can you accept de-identified thalassemia research context without giving
  patient-specific treatment advice?
- Can you export raw and summarized data for open research documentation?
- What sample type, ethics approval, and biosafety review would be required?
- Which assays are realistic in Indonesia or through remote collaboration?

Indonesian candidate settings are mapped in
[Indonesia lab partner candidate map](2026-04-27-indonesia-lab-partner-candidate-map.md).

## Stop Conditions

Stop a candidate before escalation if:

- compound or extract identity is unclear;
- HbF signal appears only with toxicity;
- erythroid maturation is impaired;
- mature red-cell hemolysis increases;
- immune, allergy, liver, kidney, or interaction risk is not reviewable;
- no qualified clinician or lab partner can audit the result.

## Linked Evidence

- [Epigenetic HbF screen V0](2026-04-27-epigenetic-hbf-screen-v0.md)
- [First HbF and red-cell safety assay work order V0](2026-04-27-first-assay-work-order-v0.md)
- [Red-cell metabolism readout spec V0](2026-04-27-red-cell-metabolism-readout-spec-v0.md)
- [Assay-ready HbF screen](../findings/2026-04-26-assay-ready-hbf-screen.md)
- [Assay funnel for cure discovery](../findings/2026-04-26-assay-funnel-for-cure-discovery.md)
- [K562 to HUDEP2 validation guardrail](../findings/2026-04-27-k562-to-hudep2-validation-guardrail.md)
- [HUDEP2 primary validation boundary](../findings/2026-04-27-hudep2-primary-validation-boundary.md)
- [HbF responder signature V0](../prioritization/2026-04-27-hbf-responder-signature-v0.md)
- [Pyruvate kinase red-cell metabolism benchmark](../findings/2026-04-27-pyruvate-kinase-red-cell-metabolism-benchmark.md)
