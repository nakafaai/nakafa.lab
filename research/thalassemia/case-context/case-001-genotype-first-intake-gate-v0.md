# Case-001 Genotype-First Intake Gate V0

Date checked: 2026-04-27
Last updated: 2026-04-28
Status: de-identified intake gate, not treatment advice

## Purpose

This gate prevents Nakafa Lab from overfitting research ideas to an unknown
thalassemia subtype.

Before a candidate is described as relevant to case-001, the repo must label
the genotype and phenotype context as known, partially known, or unknown. This
is especially important in Indonesia because beta-thalassemia, HbE/beta-
thalassemia, alpha-thalassemia, HbF modifiers, transfusion history, and immune
complications can point to different research lanes.

## Minimum Record Bundle

| Record | Minimum fields | Why it matters |
| --- | --- | --- |
| Diagnosis note | `TDT`, `NTDT`, beta, alpha, HbE/beta, or mixed disease | determines which endpoint evidence is relevant |
| Hemoglobin analysis | HbA, HbA2, HbF, HbE if present, method, date, and transfusion proximity | HPLC/electrophoresis can identify beta-thalassemia patterns and interacting hemoglobin variants |
| Molecular result | `HBB` variants plus deletion/duplication method if available | confirms beta-globin defect and beta-zero/beta-plus context |
| Alpha-globin result | `HBA1/HBA2` deletion, duplication, or sequence result if available | alpha-thalassemia or alpha duplication can change globin imbalance |
| HbF modifier context | HPFH-like variants, XmnI-HBG2, `BCL11A`, `HBS1L-MYB` if available | changes interpretation of HbF-inducing candidates |
| Family fallback | parental HPLC or genetic results if patient testing is unclear after transfusion | helps interpret inherited variants without exposing identity |

## Intake Labels

Use exactly one current label:

| Label | Meaning | Allowed research use |
| --- | --- | --- |
| `untyped` | subtype, Hb fractions, and genotype are not recorded | no patient-fit claims |
| `phenotype_only` | diagnosis and Hb fractions are available, but genotype is missing | candidate relevance stays provisional |
| `hbb_confirmed` | `HBB` result is available, but `HBA` or modifiers are missing | beta-globin lane can be discussed with caveats |
| `hbb_hba_confirmed` | `HBB` and `HBA` context are available | globin-balance interpretation becomes stronger |
| `modifier_context_known` | HbF modifier or HPFH-like context is available | HbF responder interpretation can be upgraded |

Current case-001 label: `phenotype_only`.

Reason for label: a historical hemoglobin-analysis record from infancy reports
HbF 97.6%, HbA2 2.0%, hemoglobin types A, F, and A2, and an interpretation
consistent with beta-thalassemia homozygous or compound heterozygous disease.
No molecular `HBB`, `HBA1`, `HBA2`, or HbF-modifier result is committed yet.

## Routing Rules

- If HbE/beta-thalassemia is present, compare HbF candidates against HbE/beta
  evidence first, not generic beta-thalassemia evidence.
- If beta-zero/beta-zero disease is confirmed, use gene-addition, HbF
  reactivation, and HSCT as proof-of-biology benchmarks while keeping access
  barriers explicit.
- If alpha-thalassemia, alpha duplication, or mixed disease is present, update
  the globin-balance and red-cell-survival interpretation before ranking
  candidates.
- If HbF or HPFH-like modifiers are present, update the HbF responder signature
  before promoting or demoting hydroxyurea, sirolimus, or other HbF lanes.
- If recent transfusion makes hemoglobin fractions hard to interpret, ask the
  hematologist whether molecular testing or family testing is the cleaner route.

## Doctor-Facing Ask

Ask the hematologist for the exact wording from the medical record:

```text
clinical_class:
subtype:
HPLC_or_electrophoresis_date:
recent_transfusion_before_HPLC:
HbA:
HbA2:
HbF:
HbE:
HBB_result:
HBA_result:
HbF_modifier_or_HPFH_result:
interpretation_from_hematologist:
```

## Boundaries

This gate does not recommend any drug, supplement, transfusion schedule,
chelation change, or advanced therapy. It only defines the minimum data needed
before the repo can say whether a research lane resembles case-001.

## Sources

- [Beta-Thalassemia GeneReviews, revised 2026-02-12](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [Medical record extraction 2026-04-28](case-001-medical-record-extraction-2026-04-28.md)
- [Indonesia genotype-first rule](../findings/2026-04-27-indonesia-genotype-first-rule.md)
- [HbF responder signature V0](../prioritization/2026-04-27-hbf-responder-signature-v0.md)
- [Case-001 research routing matrix](case-001-research-routing-v0.md)
- [Hematologist question sheet](hematologist-question-sheet-case-001.md)
