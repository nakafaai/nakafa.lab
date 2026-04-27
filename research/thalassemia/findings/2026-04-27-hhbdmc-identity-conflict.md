# Finding: HHBDMC Identity Conflict

Date checked: 2026-04-27
Evidence label: reduced curcuminoid biology signal and chemistry conflict, not treatment advice

## Working Conclusion

`HHBDMC` has a strong enough biology signal to keep in the HbF discovery funnel,
but it is not chemistry-resolved.

PubMed PMID `23079892` reports that
`hexahydrobisdemethoxycurcumin (HHBDMC)` induced gamma-globin mRNA and HbF in
human primary erythroid precursor cells. The reported fold changes in the
abstract were `3.6 +/- 0.4` for gamma-globin mRNA and `2.0 +/- 0.4` for HbF.

The problem is identity. Direct PubChem and ChEMBL searches for
`hexahydrobisdemethoxycurcumin` returned no clean compound record. Searches for
nearby reduced-curcuminoid names produce different molecules, including
`hexahydrocurcumin` and `octahydrocurcumin`, which retain methoxy groups and
therefore are not clean stand-ins for a bisdemethoxycurcumin-derived compound.

## Evidence Extracted

| Source | Result | Interpretation |
| --- | --- | --- |
| PubMed PMID `23079892` | reduced curcuminoid analog title and abstract | direct HbF biology signal |
| Crossref DOI `10.1007/s00277-012-1604-1` | article metadata resolves to Springer / Annals of Hematology | source identity confirmed |
| PubChem `hexahydrobisdemethoxycurcumin` | no CID found | exact name unresolved |
| ChEMBL `hexahydrobisdemethoxycurcumin` | zero molecules | exact name unresolved |
| PubChem `hexahydro-bisdemethoxycurcumin` | no CID found | hyphenated exact name unresolved |
| ChEMBL `hexahydro-bisdemethoxycurcumin` | noisy search returns `BISDEMETHOXYCURCUMIN`, not reduced analog | not usable as identity resolution |
| PubChem `1,7-bis(4-hydroxyphenyl)-3,5-heptanediol` | `CID 14427394`, formula `C19H24O4` | plausible bisdemethoxy reduced scaffold, but not proven HHBDMC from the paper |
| ChEMBL same parent-diol text search | top hit `CHEMBL474475` / `(+)-HANNOKINOL`, formula `C19H24O4` | stereochemical diarylheptanoid neighbor, not a clean HHBDMC assertion |
| PubChem `hexahydrocurcumin` | `CID 5318039`, formula `C21H26O6` | methoxy-containing curcumin metabolite, not bisdemethoxy |
| PubChem `octahydrocurcumin` | `CID 11068834`, formula `C21H28O6` | methoxy-containing curcumin metabolite, not bisdemethoxy |

## Current Candidate Chemistry Boundary

Do not collapse these labels:

- `BDMC`: bisdemethoxycurcumin parent, not reduced;
- `HHBDMC`: paper label for reduced bisdemethoxycurcumin analog, currently
  unresolved;
- `1,7-bis(4-hydroxyphenyl)-3,5-heptanediol`: PubChem `CID 14427394`, a
  plausible reduced bisdemethoxy scaffold but not proven as the paper compound;
- `hexahydrocurcumin`: PubChem `CID 5318039`, methoxy-containing;
- `octahydrocurcumin`: PubChem `CID 11068834`, methoxy-containing.

This boundary matters because a wrong compound would produce a false wet-lab
test and waste scarce primary-cell access.

## Research Decision

Track `HHBDMC` as a high-interest, identity-blocked reduced-curcuminoid seed.

It should not enter assay procurement until one of these is obtained:

- the full paper methods/supplementary chemistry table with structure;
- a compound structure file from the authors or a synthesis partner;
- a supplier certificate matching the paper structure, not only a name synonym;
- an InChIKey or `CID` that can be reconciled with the article structure.

If the identity is resolved, its first assay position should be next to
`T-BDMC`, because both have curcuminoid analog HbF signals and primary-cell
context. Until then, `T-BDMC` remains the cleaner assay seed.

## Sources

- [HHBDMC PubMed ESummary](../../../data/literature/pubmed/2026-04-27-hhbdmc-reduced-curcuminoid-esummary.json)
- [HHBDMC PubMed abstract XML](../../../data/literature/pubmed/2026-04-27-hhbdmc-reduced-curcuminoid-abstract.xml)
- [HHBDMC Crossref snapshot](../../../data/literature/pubmed/2026-04-27-hhbdmc-reduced-curcuminoid-crossref.json)
- [HHBDMC PubChem exact-name negative snapshot](../../../data/chemistry/pubchem/curcuminoid-analogs/2026-04-27-hhbdmc-name-properties.json)
- [HHBDMC ChEMBL exact-name negative snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-hhbdmc-full-name-search.json)
- [HHBDMC hyphenated PubChem negative snapshot](../../../data/chemistry/pubchem/curcuminoid-analogs/2026-04-27-hexahydro-bisdemethoxycurcumin-properties.json)
- [HHBDMC hyphenated ChEMBL noisy snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-hexahydro-bisdemethoxycurcumin-search.json)
- [Reduced bisdemethoxy parent-diol PubChem snapshot](../../../data/chemistry/pubchem/curcuminoid-analogs/2026-04-27-hhbdmc-parent-diol-properties.json)
- [Reduced bisdemethoxy parent-diol PubChem description](../../../data/chemistry/pubchem/curcuminoid-analogs/2026-04-27-hhbdmc-parent-diol-description.json)
- [Reduced bisdemethoxy parent-diol ChEMBL search snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-hhbdmc-parent-diol-search.json)
- [Hannokinol ChEMBL molecule snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-hannokinol-chembl474475.json)
- [Hannokinol ChEMBL activity snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-hannokinol-chembl-activities.json)
- [Hexahydrocurcumin PubChem snapshot](../../../data/chemistry/pubchem/curcuminoid-analogs/2026-04-27-hexahydrocurcumin-properties.json)
- [Hexahydrocurcumin ChEMBL search snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-hexahydrocurcumin-search.json)
- [Octahydrocurcumin PubChem snapshot](../../../data/chemistry/pubchem/curcuminoid-analogs/2026-04-27-octahydrocurcumin-properties.json)
- [Octahydrocurcumin ChEMBL search snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-octahydrocurcumin-search.json)
