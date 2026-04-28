# Finding: BPOM Advanced Therapy Product Search

Date checked: 2026-04-27
Evidence label: Indonesian public-registry access screen, not treatment advice

## Working Conclusion

First-pass BPOM Cek Produk searches did not find public registered-drug records
for the current high-cost or advanced thalassemia benchmarks: Reblozyl /
luspatercept, Aqvesme / mitapivat, Zynteglo / betibeglogene, or Casgevy /
exagamglogene.

The same search did find `HYDROXYUREA MEDAC`, which is useful as a sanity check:
the script can recover a known registered drug record when the queried term is
present in BPOM's public product data.

This is not proof that special access, hospital procurement, compassionate use,
clinical referral, or import routes are impossible. It is a public-registry
screen that must be followed by clinician, hospital pharmacy, BPOM, and BPJS
verification.

## Query Result Summary

| Query terms | BPOM public product result |
| --- | --- |
| `REBLOZYL`, `luspatercept` | no records found in product-name or ingredient search |
| `AQVESME`, `mitapivat` | no records found in product-name or ingredient search |
| `ZYNTEGLO`, `betibeglogene` | no records found in product-name or ingredient search |
| `CASGEVY`, `exagamglogene` | no records found in product-name or ingredient search |
| `hydroxyurea`, `hydroxycarbamide` | `HYDROXYUREA MEDAC` found by product-name search |

## Research Implication

The access lane now has a stronger working hypothesis:

- high-cost disease-modifying and gene/cell therapies should remain global
  benchmark lanes, not assumed Indonesia-ready options;
- hydroxyurea remains the more realistic local-access comparator, while still
  requiring hematologist supervision and subtype-specific interpretation;
- every advanced-therapy discussion for case-001 should include a pharmacy /
  regulatory question, not only a biology question.

## Follow-Up Questions

- Can a hematologist or hospital pharmacist confirm whether luspatercept or
  mitapivat is available through special access or hospital import pathways?
- Does BPJS cover any disease-modifying thalassemia therapy beyond transfusion,
  chelation, and monitoring?
- Which Indonesian centers can formally evaluate adult TDT patients for HSCT,
  gene therapy referral, or advanced-therapy eligibility?

## Sources

- [BPOM medicine-product search page](https://cekbpom.pom.go.id/produk-obat)
- [BPOM advanced therapy product-search snapshot](../../../data/regulatory/bpom/2026-04-27-thalassemia-advanced-therapy-product-search.json)
- [Indonesia regulatory and access gap](2026-04-26-indonesia-regulatory-access-gap.md)
- [Indonesia access deep dive](2026-04-27-indonesia-access-deep-dive.md)
