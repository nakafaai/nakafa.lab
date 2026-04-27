# Finding: Curative Options Eligibility Gate

Date checked: 2026-04-27
Evidence label: standard-care and gene-cell therapy eligibility map, not
patient-specific treatment advice

## Working Conclusion

The cure search must not skip existing curative-option evaluation.

For a severe transfusion-dependent patient, the doctor-facing question is not
"should we do transplant or gene therapy?" The correct research gate is:

> What exact evidence would a hematologist, transplant center, or gene-therapy
> center need before saying HSCT, gene therapy, CRISPR therapy, or a trial is
> relevant, unsuitable, inaccessible, or unsafe?

This gate does not rank the patient. It defines the minimum data packet needed
for a licensed specialist to evaluate the path.

## Evidence Table

| Source | What it supports | Boundary |
| --- | --- | --- |
| TIF 2025 HSCT chapter, PMID `40367263` | TDT transplant guidance includes pre-transplant evaluation, cell source, conditioning, follow-up, cost, counselling, and gene-therapy comparison. | Guideline context only; local transplant teams decide applicability. |
| PMID `36907612` | Allogeneic HSCT is described as the only consolidated potentially curative treatment for transfusion-dependent thalassemia major; alternative donors are expanding access. | Curative potential does not mean low risk or universal eligibility. |
| PMID `41730859` | A 2026 multicenter phase 4 trial reported high 2-year survival and event-free survival across matched sibling, matched unrelated, and haploidentical donor groups, with higher GVHD burden in alternative donors. | Alternative donors may expand the pool, but GVHD and center expertise remain major gates. |
| PMID `27909215` | HSCT can have high cure rates when accessible; best results are linked to earlier treatment before end-organ damage; access remains limited by donors, services, and cost. | Older review, but its access and timing boundary remains relevant. |
| PMID `41753067` | Curative approaches need criteria for selecting patients between allo-HSCT and gene therapy; gene therapy remains limited by technology, infrastructure, and cost. | Selection criteria must be individualized by specialists. |
| FDA Casgevy page | Casgevy is listed for transfusion-dependent beta-thalassemia in patients 12 years and older. | FDA indication does not equal Indonesian availability or patient eligibility. |
| FDA Zynteglo page | Zynteglo is listed for adult and pediatric beta-thalassemia patients requiring regular RBC transfusions. | FDA indication does not equal Indonesian availability or patient eligibility. |
| PMID `39527960` | Beti-cel HGB-212 studied severe genotypes and used transfusion history, mobilization, busulfan conditioning, and long-term follow-up gates. | Autologous gene therapy still requires myeloablation, manufacturing, and specialist follow-up. |
| PMID `38657265` and PMID `34891223` | Exa-cel and earlier beti-cel studies benchmark transfusion-independence endpoints. | Cure-like endpoints remain infrastructure-heavy. |

## Minimum Eligibility Packet

Ask the hematologist what is missing from this packet:

- exact diagnosis: `TDT`, `NTDT`, HbE/beta-thalassemia, alpha-thalassemia, or
  mixed disease;
- `HBB` and `HBA` genotype, plus HbF modifier context if available;
- hemoglobin fractions: HbA, HbA2, HbF, HbE if present;
- annual transfusion burden in `mL/kg/year`, pre-transfusion hemoglobin, and
  transfusion reactions;
- antibody screen, named alloantibodies, DAT/direct Coombs, crossmatch
  difficulty, and red-cell antigen phenotype or genotype;
- ferritin trend, liver iron concentration MRI, cardiac `T2*`, liver status,
  kidney status, endocrine status, infections, vaccination status, and spleen
  status;
- current chelation, adherence, toxicity monitoring, and organ-damage history;
- exact autoimmune diagnosis, immune medicines, and whether the immune condition
  changes transplant, conditioning, or trial risk;
- HLA typing status for the patient and available family members, if a
  transplant team says this is appropriate;
- fertility counselling, psychosocial readiness, long-term follow-up capacity,
  cost, insurance, referral-center access, and Indonesia-specific availability.

## Doctor-Facing Decision Labels

Use these labels after a specialist conversation:

| Label | Meaning |
| --- | --- |
| `not_yet_evaluated` | No specialist has reviewed HSCT or gene-cell therapy eligibility. |
| `data_missing` | Specialist needs records before judging. |
| `medically_unsuitable` | There is a documented medical reason the option is not appropriate. |
| `access_blocked` | Medically plausible, but unavailable because of cost, center access, payer, registry, or geography. |
| `trial_or_referral_candidate` | Specialist thinks referral or trial screening is reasonable. |
| `under_specialist_review` | Evaluation is active; repo should not speculate. |

## Research Decision

Add a curative-options eligibility gate to case-001 docs.

This gate protects two things at once:

- it prevents false hope from untested supplements or speculative molecules;
- it prevents the research program from missing a real curative referral path
  that only a hematologist or transplant/gene-therapy center can assess.

## Sources

- [Curative-options selected PubMed XML](../../../data/literature/pubmed/2026-04-27-curative-options-eligibility-selected-abstracts.xml)
- [HSCT eligibility PubMed snapshot](../../../data/literature/pubmed/2026-04-27-hsct-beta-thalassemia-eligibility-search.json)
- [HSCT donor-risk PubMed snapshot](../../../data/literature/pubmed/2026-04-27-hsct-thalassemia-donor-risk-search.json)
- [Gene-therapy eligibility PubMed snapshot](../../../data/literature/pubmed/2026-04-27-gene-therapy-eligibility-beta-thalassemia-search.json)
- [TIF 2025 HSCT chapter, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [FDA Casgevy product page](https://www.fda.gov/vaccines-blood-biologics/casgevy)
- [FDA Zynteglo product page](https://www.fda.gov/vaccines-blood-biologics/zynteglo)
- [HSCT in thalassemia, PMID 36907612](https://pubmed.ncbi.nlm.nih.gov/36907612/)
- [Multicenter allo-HSCT TDT trial, PMID 41730859](https://pubmed.ncbi.nlm.nih.gov/41730859/)
- [Cure from HSCT to gene therapy, PMID 27909215](https://pubmed.ncbi.nlm.nih.gov/27909215/)
- [Curative HSCT approach review, PMID 41753067](https://pubmed.ncbi.nlm.nih.gov/41753067/)
- [Beti-cel HGB-212 trial, PMID 39527960](https://pubmed.ncbi.nlm.nih.gov/39527960/)
