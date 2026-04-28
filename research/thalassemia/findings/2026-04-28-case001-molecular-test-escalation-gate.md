# Case-001 Molecular Test Escalation Gate

Date: 2026-04-28
Status: de-identified clinician-question gate, not treatment advice
Evidence label: GeneReviews + TIF 2025 + case-context synthesis

## Bottom Line

Case-001 remains `phenotype_only`. The next case-specific research blocker is a
clear molecular-record escalation sequence, not another candidate claim.

The minimum escalation is:

1. confirm whether the historical infancy hemoglobin analysis happened before
   any transfusion;
2. request or locate the `HBB` molecular result, including beta-zero or
   beta-plus interpretation;
3. request or locate `HBA1/HBA2` deletion, duplication, or copy-number context;
4. ask whether HPFH, delta-beta-thalassemia, `HBG1/HBG2` promoter, XmnI-HBG2,
   `BCL11A`, or `HBS1L-MYB` modifier context was reviewed;
5. use parent hemoglobin or genetic records only as a fallback when patient
   records are unavailable or hard to interpret.

## Why This Gate Exists

The historical record makes HbF biology highly relevant, but it does not prove
HPFH, beta-plus disease, alpha-thalassemia co-inheritance, or any specific HbF
modifier. GeneReviews states that beta-thalassemia diagnosis can be established
with hemoglobin findings and that `HBB` molecular testing can establish
diagnosis in younger infants with suggestive findings. It also describes `HBB`
sequence analysis first, followed by deletion/duplication analysis when needed.

Alpha-thalassemia GeneReviews adds that `HBA1/HBA2` testing often starts with
targeted common-deletion analysis, with sequence and deletion/duplication
methods used for broader detection. This matters because alpha-globin loss or
gain can change chain imbalance and the interpretation of Nakafa Lab's
HbF/alpha-globin/autophagy lane.

## Label Upgrade Rules

| Current evidence | Allowed label | Still blocked |
| --- | --- | --- |
| Historical Hb fractions only | `phenotype_only` | patient-specific candidate claims |
| `HBB` variants documented | `hbb_confirmed` | alpha-globin and modifier interpretation |
| `HBB` plus `HBA1/HBA2` context documented | `hbb_hba_confirmed` | HPFH/HBG-modifier interpretation unless reviewed |
| `HBB`, `HBA`, and HbF-modifier or HPFH/delta-beta context documented | `modifier_context_known` | treatment choice, dosing, and eligibility decisions still require clinicians |

## Doctor-Facing Ask

Use this wording:

> We are not asking to order a therapy from this result. We want to know which
> molecular records already exist and which ones are clinically appropriate to
> request so the diagnosis and HbF interpretation are not guessed from old Hb
> fractions alone.

Then ask:

1. Does the patient already have `HBB` sequencing or targeted mutation testing?
2. If `HBB` sequencing found only one or no pathogenic variant, was
   deletion/duplication analysis considered?
3. Has `HBA1/HBA2` deletion/copy-number testing been done, including common
   Southeast Asian deletions or alpha duplication if clinically relevant?
4. Was HPFH, delta-beta-thalassemia, `HBG1/HBG2` promoter, XmnI-HBG2,
   `BCL11A`, or `HBS1L-MYB` modifier context reviewed?
5. If testing access is limited, can parent HPLC or genetic records help
   clarify inheritance without replacing patient-level clinician review?

## Research Consequence

Until this gate is closed, Nakafa Lab can keep ranking assay candidates in
general, but case-001 patient relevance remains blocked. The strongest research
lane remains:

`HPFH-like HbF/F-cell rescue + alpha-globin/autophagy cleanup + preserved erythroid maturation + no mature red-cell hemolysis`.

This case can guide questions for that lane only after the molecular context is
known or explicitly unavailable.

## Islamic Research Boundary

Quran 16:43 supports asking qualified experts when knowledge is missing. Quran
55:7-9 supports careful measure. In this gate, those anchors require molecular
and clinician review before interpretation. They do not provide biomedical
proof or treatment permission.

## Sources

- [Case-001 molecular test escalation notebook](../notebooks/2026-04-28-case001-molecular-test-escalation-gate.ipynb)
- [Case-001 high-HbF genotype evidence gate](2026-04-28-case001-high-hbf-genotype-evidence-gate.md)
- [Case-001 genotype-first intake gate](../case-context/case-001-genotype-first-intake-gate-v0.md)
- [Case-001 minimum hematologist packet](../case-context/case-001-minimum-hematologist-packet.md)
- [Beta-Thalassemia GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [Alpha-Thalassemia GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1435/)
- [TIF 2025 genetic basis, pathophysiology, and diagnosis chapter](https://www.ncbi.nlm.nih.gov/books/NBK614253/)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
