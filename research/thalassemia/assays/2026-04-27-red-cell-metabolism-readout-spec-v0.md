# Assay Spec: Red-Cell Metabolism Readouts V0

Date checked: 2026-04-27
Status: qualified-lab readout specification, not a patient treatment plan

## Purpose

This spec turns the pyruvate kinase / mitapivat benchmark into measurable
research outputs.

The key rule is simple: a red-cell-support candidate should not be promoted
because it sounds antioxidant. It needs evidence that red cells or erythroid
precursors survive better without worsening HbF, globin balance, iron burden,
immune risk, or mature red-cell hemolysis.

## Minimum Readout Set

| Readout | Preferred method | Why it matters |
| --- | --- | --- |
| ATP or glycolysis-linked energy state | lab-validated ATP assay, metabolomics, or pyruvate kinase pathway readout | pyruvate kinase activation is an energy-metabolism benchmark |
| hemolysis | LDH, bilirubin, plasma-free hemoglobin, haptoglobin, or lab hemolysis assay | separates red-cell support from red-cell damage |
| erythroid maturation | `CD71`, `CD235a`, Band3, CD49d, enucleation, or lab-equivalent markers | blocks false support signals caused by differentiation failure |
| alpha-globin membrane precipitation | membrane-bound globin assay, mass spectrometry, or lab-equivalent method | beta-thalassemia damage includes excess alpha-globin toxicity |
| oxidative or membrane stress | ROS, lipid peroxidation, deformability, or membrane-damage assay | turns antioxidant language into measurable red-cell endpoints |
| iron-axis markers | ferritin, hepcidin, erythroferrone, transfusion burden, or model-appropriate iron readout | improved erythropoiesis can change iron handling |
| HbF and globin balance | `HBG1/HBG2`, HbF protein, F-cells, alpha/non-alpha balance | confirms metabolism support does not bypass the core globin problem |

## Candidate Classes

| Candidate class | Example | Interpretation |
| --- | --- | --- |
| clinical benchmark | mitapivat or lab-approved pyruvate kinase activator reference | validates the readout family, subject to legal access and lab control |
| red-cell support seed | standardized 6-shogaol-rich ginger extract | support hypothesis only unless HbF or transfusion-burden evidence appears |
| adjunct comparator | EGCG-rich green-tea extract with safety review | adjunct biology only; liver and interaction gates remain active |
| hazard boundary | melittin or lab-chosen hemolysis control | calibrates rejection, not efficacy |

## Pass, Hold, Reject

Pass to deeper testing only if:

- hemolysis or membrane damage improves or does not worsen;
- erythroid maturation is preserved;
- energy or metabolism readout improves in a plausible direction;
- HbF, globin balance, or iron-axis readouts are not worsened;
- material identity and batch are auditable.

Hold if:

- the only signal is generic antioxidant activity;
- ATP or metabolism readouts are missing;
- HbF and globin-balance readouts are not measured;
- product identity or standardization is incomplete.

Reject if:

- mature red-cell hemolysis increases;
- erythroid maturation collapses;
- metabolism signal appears only at toxic concentrations;
- the candidate is a mixture without identity or batch control.

## Lab Output Table

```text
candidate:
identity_or_batch:
model:
concentration_range:
vehicle:
ATP_or_energy_state:
hemolysis:
erythroid_maturation:
alpha_globin_membrane_signal:
oxidative_or_membrane_stress:
iron_axis_signal:
HBG1_HBG2_or_HbF:
alpha_non_alpha_balance:
viability:
assay_interference:
metabolism_support_label:
decision:
reason:
raw_data_location:
```

## Sources

- [Pyruvate kinase red-cell metabolism benchmark](../findings/2026-04-27-pyruvate-kinase-red-cell-metabolism-benchmark.md)
- [First HbF and red-cell safety assay work order V0](2026-04-27-first-assay-work-order-v0.md)
- [HPFH-like assay readout spec V0](2026-04-27-hpfh-like-assay-readout-spec-v0.md)
- [Ginger shogaol red-cell support map](../findings/2026-04-27-ginger-shogaol-red-cell-support-map.md)
- [EGCG TDT clinical adjunct boundary](../findings/2026-04-27-egcg-tdt-clinical-adjunct-boundary.md)
- [Melittin bee-venom hazard deep dive](../findings/2026-04-27-melittin-bee-venom-hazard-deep-dive.md)
