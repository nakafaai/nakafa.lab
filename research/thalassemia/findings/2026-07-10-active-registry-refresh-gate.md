# Finding: Active Registry Refresh Gate

Date checked: 2026-07-10
Status: active registry source radar, not treatment advice

## Direct Answer

The July 10 ClinicalTrials.gov refresh shows that country-specific active
queries are more useful than a broad regional query:

- `beta thalassemia` + `China` + active statuses returned 23 records.
- `thalassemia` + `CS-101` returned 8 records.
- `transfusion dependent beta thalassemia` + `Asia` returned 0 records.

The zero-result `Asia` query is a query-quality warning, not evidence that Asia
has no active thalassemia records.

Current label:

`active_registry_source_radar_ready_benchmark_only`

Case-001 state remains:

`branch_review_handoff_packet_incomplete`

## Source Signals

| Source set | Signal | Interpretation boundary |
| --- | --- | --- |
| China active beta-thalassemia query | 16 recruiting, 3 not-yet-recruiting, and 4 enrolling-by-invitation records. | Useful public source map, not eligibility or referral evidence. |
| CS-101 query | 8 records across completed, recruiting, not-yet-recruiting, and invitation-only states. | Fast-moving editing benchmark lane, not a patient action path. |
| `NCT06291961` | Completed Phase 1 CS-101 China record. | Useful because it was not emphasized in the July 6 note; still benchmark-only. |
| `NCT07489196` | Phase 2 CS-101 China record, not yet recruiting. | Good source-radar follow-up ID, not trial-screening advice. |
| PubMed July 10 query | 10 results, including base-editing, limited-resource prioritization, luspatercept meta-analysis, DNMT1 inhibitor, and off-target records. | Literature triage input only; individual papers still need source-by-source interpretation. |

## Practical Meaning

For public helpers or doctors, ask source questions only:

- What does this registry ID represent?
- Which country and public status does it list?
- Is it active, completed, invitation-only, or not yet recruiting?
- Which qualified owner should interpret it privately?

Do not ask public helpers to decide Case-001 eligibility, travel, import,
purchase, referral, trial enrollment, dosing, transfusion changes, chelation
changes, lab contact, private-message routing, or sample routing.

## Method Note

ClinicalTrials.gov regional location terms can be misleading. On July 10, the
`Asia` location query returned zero records while the China country query
returned 23 active-status records. Future Asia surveillance should run
country-specific queries and preserve null broad-query snapshots only as
query-quality evidence.

## Islamic Motivation Boundary

Quran 49:6 supports verification before acting on consequential reports. Quran
4:58 supports routing entrusted questions to their proper owner. Quran 16:43
supports expert consultation when knowledge is missing. These are process
ethics only and are not biomedical evidence for registry status, eligibility,
referral, treatment, import, or purchase.

## Sources

- [ClinicalTrials.gov home](https://clinicaltrials.gov/)
- [July 10 China active registry snapshot](../../../data/registries/clinicaltrials/2026-07-10-china-active-beta-thalassemia-refresh.json)
- [July 10 CS-101 registry snapshot](../../../data/registries/clinicaltrials/2026-07-10-cs101-clinicaltrials-refresh.json)
- [July 10 Asia location null-query snapshot](../../../data/registries/clinicaltrials/2026-07-10-asia-location-query-null.json)
- [July 10 PubMed snapshot](../../../data/literature/pubmed/2026-07-10-asia-thalassemia-current-therapy-refresh.json)
- [NCT06291961](https://clinicaltrials.gov/study/NCT06291961)
- [NCT07489196](https://clinicaltrials.gov/study/NCT07489196)
- [PubMed PMID 41951736](https://pubmed.ncbi.nlm.nih.gov/41951736/)
- [Quran 49:6 anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 4:58 anchor](../../islamic/quran/004-an-nisa/058.md)
- [Quran 16:43 anchor](../../islamic/quran/016-an-nahl/043.md)
