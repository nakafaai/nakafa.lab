# Case-001 Minimum Hematologist Packet Gate

Date: 2026-04-28
Status: de-identified integration gate, not treatment advice
Evidence label: existing case gates + GeneReviews + TIF 2025 synthesis

## Bottom Line

The next highest-value case-001 action is not another candidate claim. It is a
single minimum hematologist packet.

Case-001 currently has four active blockers:

- `phenotype_only`
- `immune_transfusion_packet_missing`
- `iron_packet_missing`
- `trial_referral_not_ready`

Until those labels are corrected or closed by a hematologist, Nakafa Lab should
keep all patient-specific candidate claims as `patient_relevance_blocked`.

## Why This Gate Exists

The case now has separate genotype, immune/transfusion, and iron/chelation
gates. That is scientifically safer, but hard to manage in a doctor visit. This
gate turns them into one checklist without merging their meanings.

The practical sequence is:

1. establish current subtype, genotype, and Hb fractions;
2. quantify transfusion burden and response;
3. resolve immune/blood-bank risk;
4. resolve iron/chelation organ-risk;
5. document autoimmune, spleen, infection, and access context;
6. only then judge standard-care optimization, referral, trial, or assay
   patient relevance.

## Notebook Result

The notebook ranked record areas by four blockers: diagnosis,
transfusion-explanation, safety, and referral. The top three were:

1. current subtype/genotype/Hb-fraction packet;
2. transfusion burden and response packet;
3. immune and blood-bank packet.

The iron/chelation organ-risk packet remains close behind because it controls
safety and referral interpretation.

## Practical Output

The durable doctor-facing artifact is:

- [Case-001 minimum hematologist packet](../case-context/case-001-minimum-hematologist-packet.md)

Use it as the first page before the longer clinician brief and hematologist
question sheet.

## Research Boundary

This gate does not diagnose the patient and does not recommend treatment.
It only defines the minimum source-backed record packet needed before Nakafa Lab
can responsibly connect the broader cure-search work to this case.

## Islamic Research Boundary

Quran 16:43 supports asking qualified experts when knowledge is missing. Quran
55:7-9 supports balance and measurement. In this repo, those anchors require
better questions and cleaner records, not biomedical shortcuts.

## Sources

- [Case-001 high-HbF genotype evidence gate](2026-04-28-case001-high-hbf-genotype-evidence-gate.md)
- [Case-001 immune transfusion record gate](2026-04-28-case001-immune-transfusion-record-gate.md)
- [Case-001 iron chelation organ-risk record gate](2026-04-28-case001-iron-chelation-organ-risk-record-gate.md)
- [Case-001 research routing matrix](../case-context/case-001-research-routing-v0.md)
- [Case-001 minimum hematologist packet notebook](../notebooks/2026-04-28-case001-minimum-hematologist-packet-gate.ipynb)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [GeneReviews alpha-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1435/)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
