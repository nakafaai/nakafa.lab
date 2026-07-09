# Finding: BPOM Advanced Therapy Access Refresh

Date checked: 2026-07-09
Status: public-registry access refresh, not treatment advice

## Direct Answer

The July 9 BPOM refresh did not find public registered-drug records for the
advanced thalassemia benchmark terms in product-name or ingredient search:

- `REBLOZYL` / `luspatercept`
- `AQVESME` / `mitapivat`
- `ZYNTEGLO` / `betibeglogene`
- `CASGEVY` / `exagamglogene`

The same snapshot again found `HYDROXYUREA MEDAC` when searching
`hydroxyurea` by product name. That remains a sanity check that the search can
recover a public drug record. It is not a thalassemia indication claim and not
a patient-specific treatment recommendation.

## What Changed

Nothing in the public BPOM screen changed the access state since the April 27
baseline. The access label stays:

`indonesia_advanced_therapy_public_registry_not_found`

For Case-001, the clinical state is unchanged:

`branch_review_handoff_packet_incomplete`

## Interpretation

This refresh strengthens the current blocker map:

1. Casgevy, Zynteglo, Reblozyl, and Aqvesme remain benchmark and owner-question
   lanes in this repo, not assumed Indonesia-ready options.
2. Public BPOM absence does not prove that special access, hospital import,
   compassionate use, pending registration, private payment, or referral
   coordination is impossible.
3. The next useful human action is still owner verification: hematologist,
   hospital pharmacy, BPOM-facing regulatory owner, payer or BPJS owner, and
   referral-center owner.
4. The repo still cannot route Case-001 toward HSCT, autologous gene-cell
   therapy, disease-modifying drugs, trial screening, import, purchase, or
   treatment changes without qualified clinician review of the private packet.

## Doctor-Facing Wording

Safe wording:

> A July 9 public BPOM product search did not show Casgevy, Zynteglo,
> Reblozyl, or Aqvesme by product or ingredient term. Can a hematologist or
> hospital pharmacy confirm whether any formal local, special-access, referral,
> or payer route exists, and what records are required before that question can
> be answered?

Unsafe wording:

> BPOM proves these therapies are impossible, hydroxyurea should be used, or
> Case-001 should pursue import, purchase, referral, trial screening, or
> treatment changes.

## Islamic Motivation Boundary

Quran 49:6 supports verification before acting on consequential reports. Quran
4:58 supports routing entrusted questions to their proper owner. Quran 16:43
supports asking qualified people when knowledge is missing. These are process
ethics only and are not biomedical evidence for product availability,
eligibility, import, referral, dosing, or treatment.

## Sources

- [BPOM Cek Produk medicine page](https://cekbpom.pom.go.id/produk-obat)
- [July 9 BPOM search snapshot](../../../data/regulatory/bpom/2026-07-09-thalassemia-advanced-therapy-product-search-refresh.json)
- [April 27 BPOM baseline finding](./2026-04-27-bpom-advanced-therapy-product-search.md)
- [Indonesia regulatory access gap](./2026-04-26-indonesia-regulatory-access-gap.md)
- [July 8 Casgevy source consistency gate](./2026-07-08-casgevy-source-consistency-gate.md)
- [Quran 49:6 anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 4:58 anchor](../../islamic/quran/004-an-nisa/058.md)
- [Quran 16:43 anchor](../../islamic/quran/016-an-nahl/043.md)
