# Finding: Trial Referral No-Lab Gate

Date checked: 2026-04-27
Evidence label: registry-backed referral data packet, not treatment advice

## Working Conclusion

We have not found a new cure. Without a lab partner, the highest-value next
move is to make the patient record packet strong enough that a hematologist can
decide whether existing advanced options, disease-modifying drugs, or trial
referral are worth screening.

The current registry refresh supports this practical conclusion:

- Indonesia active thalassemia trial snapshot returned `0` active records.
- Nearby country snapshots are not empty: Malaysia returned `7`, Thailand
  returned `8`, and Singapore returned `1` active or active-not-recruiting
  thalassemia records.
- The global active referral snapshot for transfusion-dependent beta
  thalassemia returned `38` records, including gene-modified autologous HSC
  studies, mitapivat, luspatercept, transplant-related studies, CRISPR/editing
  studies, and long-term follow-up records.
- Dedicated active snapshots returned `26` HSCT-related, `18` gene-therapy
  keyword, `4` CRISPR, `9` luspatercept, and `5` mitapivat beta-thalassemia
  records.

This does not mean the patient can join any trial. It means the repo should now
separate the next doctor conversation into a strict screening gate: what data
is missing, which options are medically irrelevant, which are medically
plausible but access-blocked, and which deserve referral-center review.

## Why This Matters For A No-Lab Path

Nakafa Lab cannot run a transplant, gene-therapy, CRISPR, luspatercept, or
mitapivat eligibility assessment. But the repo can do the pre-work that makes a
specialist conversation sharper:

- collect and de-identify the exact records;
- map each existing option to required screening fields;
- stop candidate claims until subtype, iron, immune, and access blockers are
  known;
- distinguish active registry evidence from Indonesia access reality;
- keep a dated snapshot trail so doctors and collaborators can inspect what was
  checked.

This is useful now because weekly transfusion plus reported autoimmune disease
could be driven by more than the thalassemia genotype alone. Trial and therapy
screening should not ignore alloantibodies, autoantibodies, DAT/direct Coombs,
crossmatch difficulty, iron overload, spleen status, infection history, organ
status, and chelation toxicity.

## Decision Labels

Use these labels after each clinician or referral-center conversation:

| Label | Meaning |
| --- | --- |
| `trial_referral_not_ready` | Core records are missing, so referral screening would be low quality. |
| `trial_referral_screenable` | Records are complete enough for a hematologist or referral center to screen. |
| `therapy_access_question` | An option is scientifically relevant, but local access, price, or regulatory status is unclear. |
| `trial_or_referral_candidate` | A licensed specialist thinks referral or trial screening is reasonable. |
| `medically_unsuitable` | A licensed specialist documents why an option is not appropriate. |
| `access_blocked` | Medically plausible, but blocked by center access, country, payer, cost, visa, manufacturing, or logistics. |
| `under_specialist_review` | Evaluation is active; the repo should not speculate. |

Current case-001 label: `trial_referral_not_ready`.

Reason: exact subtype, genotype, Hb fractions, transfusion burden, antibody/DAT
status, iron MRI, organ-risk packet, autoimmune diagnosis, and access history
are still incomplete in the repo.

## Minimum Trial/Referral Packet

Before asking a center about HSCT, gene therapy, CRISPR/editing, luspatercept,
mitapivat, hydroxyurea, iron-axis trials, or other studies, ask the hematologist
which of these are missing:

- exact diagnosis: `TDT`, `NTDT`, HbE/beta-thalassemia, alpha-thalassemia, or
  mixed disease;
- `HBB` and `HBA` genotype, plus HbF modifier context if available;
- HPLC or electrophoresis fractions: HbA, HbA2, HbF, HbE if present;
- transfusion log: dates, units, volume, pre-transfusion hemoglobin, reactions,
  and annual `mL/kg/year`;
- blood-bank record: ABO, Rh C/c, D, E/e, Kell, extended matching policy,
  antibody screen, named alloantibodies, DAT/direct Coombs, and crossmatch
  difficulty;
- red-cell antigen phenotype or genotype, especially if recent transfusion or
  antibodies make serology difficult;
- iron packet: ferritin trend, liver iron concentration MRI, cardiac `T2*`,
  chelation drug, dose, adherence, side effects, kidney/liver monitoring, and
  toxicity review;
- organ and infection packet: liver, heart, endocrine, bone, spleen, viral
  hepatitis, vaccination, and fertility counselling status;
- autoimmune packet: exact diagnosis, tests, medicines, symptoms, specialist
  notes, and whether immunosuppression changes trial or transplant risk;
- access packet: BPJS/private insurance, hospital referral route, travel
  feasibility, language/visa barriers, estimated cost, and local pharmacist or
  regulatory access status.

## Option-Specific Questions For The Doctor

HSCT / transplant:

- Is HLA typing appropriate for the patient and family, or is there a medical
  reason not to start?
- Would matched sibling, unrelated, haploidentical, or cord blood routes ever
  be considered?
- Do iron, cardiac `T2*`, liver, endocrine, infection, antibody, autoimmune, or
  spleen factors make transplant too risky?

Gene therapy / CRISPR / editing:

- Is the case subtype and genotype compatible with currently available
  gene-addition or HbF-reactivation approaches?
- Would myeloablation, fertility risk, long-term follow-up, manufacturing,
  organ status, or cost make this unsuitable?
- Is domestic Indonesia access possible, or would this require referral abroad?

Luspatercept:

- Is the subtype and transfusion pattern compatible with a luspatercept
  discussion?
- What response endpoint would the doctor use: >=33% transfusion-burden
  reduction, >=50% reduction, improved pre-transfusion hemoglobin, ferritin
  effect, or another endpoint?
- Is it legally and financially accessible in the patient's care setting?

Mitapivat:

- Is the patient TDT or NTDT, and is mitapivat medically relevant for that
  category?
- What liver, drug-interaction, pregnancy/fertility, and monitoring gates would
  apply?
- Is this approved, importable, or trial-only in the local setting?

Iron-axis trials:

- Is the patient TDT, NTDT, or mixed, and is iron overload mainly transfusional,
  ineffective-erythropoiesis driven, or both?
- Are liver iron concentration and cardiac `T2*` available before judging an
  iron-axis option?

## Registry Readout For Referral Planning

| Snapshot | Total count | Practical read |
| --- | ---: | --- |
| TDT beta-thalassemia active referral | 38 | Broad active landscape; includes gene/cell therapy, mitapivat, luspatercept, transplant, CRISPR, and follow-up records. |
| Indonesia active thalassemia | 0 | No active Indonesia-located trial in this snapshot. |
| Malaysia active thalassemia | 7 | Regional signal includes mitapivat, luspatercept, genetic modifiers, iron-axis, and education/screening records. |
| Thailand active thalassemia | 8 | Regional signal includes mitapivat, luspatercept, iron-axis, and gene-therapy follow-up records. |
| Singapore active thalassemia | 1 | Regional signal in this pass is luspatercept alpha-thalassemia. |
| HSCT beta-thalassemia | 26 | Mostly specialist-center transplant, conditioning, gene/editing, or follow-up records. |
| Gene therapy beta-thalassemia | 18 | Includes lentiviral beta-globin and HbF-reactivation/editing records, but keyword noise remains. |
| CRISPR beta-thalassemia | 4 | Compact editing-specific set with CTX001, EDIT-301, VGB-Ex01, and CTX001 follow-up/combined records. |
| Luspatercept beta-thalassemia | 9 | Transfusion burden, safety, real-world, pediatric, and post-marketing endpoints. |
| Mitapivat beta-thalassemia | 5 | TDT/NTDT phase 3 and pediatric records, including transfusion-reduction response. |

## Research Decision

Add a trial/referral no-lab gate to case-001. The repo should not wait for a
lab partner before becoming useful to a doctor. It should first make the case
screenable, then use specialist feedback to decide whether the next path is
standard-care optimization, referral, trial search, or affordable candidate
discovery.

## Islamic Research Boundary

Quran 16:43 supports asking people of knowledge when knowledge is missing. For
this project, that means a hematologist, transfusion specialist, transplant or
gene-therapy center, and lab scientist must review the relevant lane.

Quran 55:7-9 supports careful measurement and balance. For this project, that
means referral claims need measured endpoints, documented blockers, and honest
boundaries. It does not turn any option, supplement, verse, or registry record
into a treatment claim.

## Sources

- [TDT beta-thalassemia active referral snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-referral-transfusion-dependent-beta-thalassemia.json)
- [Asia thalassemia location-query snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-referral-asia-thalassemia.json)
- [Indonesia active thalassemia snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-referral-indonesia-thalassemia.json)
- [Malaysia active thalassemia snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-referral-malaysia-thalassemia.json)
- [Thailand active thalassemia snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-referral-thailand-thalassemia.json)
- [Singapore active thalassemia snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-referral-singapore-thalassemia.json)
- [HSCT beta-thalassemia referral snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-referral-hsct-beta-thalassemia.json)
- [Gene therapy beta-thalassemia referral snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-referral-gene-therapy-beta-thalassemia.json)
- [CRISPR beta-thalassemia referral snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-referral-crispr-beta-thalassemia.json)
- [Luspatercept beta-thalassemia referral snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-referral-luspatercept-beta-thalassemia.json)
- [Mitapivat beta-thalassemia referral snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-referral-mitapivat-beta-thalassemia.json)
- [Curative options eligibility gate](2026-04-27-curative-options-eligibility-gate.md)
- [Indonesia access deep dive](2026-04-27-indonesia-access-deep-dive.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
