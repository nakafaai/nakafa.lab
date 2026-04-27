# Finding: BPOM Sirolimus Product Search

Date checked: 2026-04-27
Evidence label: Indonesian public-registry access screen, not treatment advice

## Working Conclusion

First-pass BPOM Cek Produk searches did not find public registered-drug records
for `SIROLIMUS`, `RAPAMUNE`, or `RAPAMYCIN` in either product-name or ingredient
fields.

This keeps sirolimus in the repo as a monitored research and clinical benchmark
lane, not as a locally confirmed access comparator. It does not prove that
hospital import, special access, transplant-program supply, or non-public
procurement routes are impossible.

## Why This Matters

Sirolimus already has a direct beta-thalassemia evidence lane: small human pilot
data, gamma-globin signals, and mechanistic links to `ULK1`, autophagy, and
alpha-globin burden. The access question is separate from that biology.

For Indonesia-facing prioritization:

- hydroxyurea is currently the clearer public local-access comparator because
  BPOM search found `HYDROXYUREA MEDAC`;
- sirolimus remains a hypothesis-strengthening comparator until a clinician or
  hospital pharmacist confirms legal availability and monitoring feasibility;
- the reported autoimmune context in case-001 makes immune-active drug ideas
  especially dependent on hematologist review.

## Query Result Summary

| Query term | Product-name search | Ingredient search |
| --- | --- | --- |
| `SIROLIMUS` | no records found | no records found |
| `RAPAMUNE` | no records found | no records found |
| `RAPAMYCIN` | no records found | no records found |

## Doctor Or Pharmacy Questions

Ask only as clinician-review questions:

- Is sirolimus legally available in this hospital or care network for any
  indication?
- If it is not visible in public BPOM product search, are there special access,
  import, transplant-program, or clinical-trial routes that matter?
- Would this patient's autoimmune diagnosis, infection history, kidney/liver
  status, lipid profile, mouth-ulcer risk, wound-healing risk, or current
  medicines rule out an immune-active repurposing discussion?
- If sirolimus is scientifically interesting but not locally feasible, should it
  stay only as an assay comparator against safer HbF/autophagy candidates?

## Boundary

Do not infer patient eligibility, dosing, safety, legality, affordability, or
reimbursement from this note. This is a public product-search screen and a
research-routing guardrail.

## Sources

- [BPOM Cek Produk obat page](https://cekbpom.pom.go.id/produk-obat)
- [BPOM sirolimus product-search snapshot](../../../data/regulatory/bpom/2026-04-27-sirolimus-product-search.json)
- [Sirolimus deep dive](2026-04-26-sirolimus-deep-dive.md)
- [AMPKB1/autophagy/HbF bridge](2026-04-27-ampkb1-autophagy-hbf-bridge.md)
- [Hydroxyurea local-access comparator](2026-04-27-hydroxyurea-local-access-comparator.md)
