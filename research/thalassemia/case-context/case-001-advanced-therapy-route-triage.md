# Case-001 Advanced-Therapy Route Triage

Date checked: 2026-05-28
Status: public-safe branch map, not treatment advice

## Purpose

Use this only after the May 26 owner packet and May 27 answer ladder. It keeps
advanced-therapy discussion from mixing different routes.

## Branch Questions

| Branch | Ask this owner question |
| --- | --- |
| Allogeneic HSCT | Does HLA/donor-based transplant evaluation belong in scope after packet review? |
| Autologous gene-cell therapy | Does a gene-addition or gene-editing center consider screening reasonable after packet review? |
| Non-curative disease-modifying drugs | Should transfusion-reduction or disease-modifying drugs be reviewed separately from curative routes? |
| Standard-care stabilization | Must iron, immune, infection, organ, or transfusion blockers be stabilized first? |
| Registry or trial benchmark | Is this registry record benchmark context only unless a specialist asks a specific screening question? |

## Safe Labels

- `allogeneic_hsct_branch_owner_question`
- `autologous_gene_cell_branch_owner_question`
- `disease_modifying_noncurative_branch_owner_question`
- `standard_care_stabilization_first`
- `trial_registry_benchmark_only`
- `route_selection_blocked_until_specialist_review`
- `release_blocked_private_material`

## Privacy Boundary

Do not publish raw records, doctor messages, owner replies, HLA details, donor
details, family identifiers, exact private dates, product-access replies, trial
screening messages, travel discussion, import discussion, or dosing
instructions.

## Sources

- [May 28 route-triage finding](../findings/2026-05-28-case001-advanced-therapy-route-triage-gate.md)
- [May 28 workflow map](../../../data/workflows/case-001/2026-05-28-advanced-therapy-route-triage.json)
- [May 27 clinician-answer ladder](case-001-advanced-therapy-clinician-answer-ladder.md)
