"""Validate the required Nakafa Lab scaffold files."""

import pathlib


REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "docs/research-protocol.md",
    "docs/next-steps.md",
    "docs/parallel-research-tracks.md",
    "docs/discovery-pipeline.md",
    "docs/zed-latex.md",
    ".zed/tasks.json",
    "data/README.md",
    "data/literature/pubmed/2026-04-26-bcl11a-hbf-beta-thalassemia.json",
    "data/literature/pubmed/2026-04-26-hbf-assay-screening.json",
    "data/literature/pubmed/2026-04-26-hemolysis-assay-safety.json",
    "data/literature/pubmed/2026-04-27-tdt-alloimmunization-autoimmunization.json",
    "data/literature/pubmed/2026-04-27-tdt-direct-antiglobulin-autoantibodies.json",
    "data/literature/pubmed/2026-04-27-thalassemia-antigen-matching.json",
    "data/literature/pubmed/2026-04-26-hydroxyurea-beta-thalassemia.json",
    "data/literature/pubmed/2026-04-27-bee-venom-adverse-events.json",
    "data/literature/pubmed/2026-04-27-melittin-erythrocyte-hemolysis.json",
    "data/literature/pubmed/2026-04-27-melittin-hbf-gap.json",
    "data/literature/pubmed/2026-04-26-propolis-red-cell-oxidative-stress.json",
    "data/literature/pubmed/2026-04-27-royal-jelly-hbf-gap.json",
    "data/literature/pubmed/2026-04-27-royal-jelly-oxidative-stress.json",
    "data/literature/pubmed/2026-04-27-exagamglogene-autotemcel-beta-thalassemia.json",
    "data/literature/pubmed/2026-04-27-betibeglogene-autotemcel-beta-thalassemia.json",
    "data/literature/pubmed/2026-04-27-indonesia-thalassemia-gene-therapy.json",
    "data/literature/pubmed/2026-04-27-indonesia-thalassemia-access.json",
    "data/literature/pubmed/2026-04-27-indonesia-beta-thalassemia-mutations.json",
    "data/literature/pubmed/2026-04-27-hbe-beta-thalassemia-hydroxyurea-xmni.json",
    "data/literature/pubmed/2026-04-27-hbe-beta-thalassemia-hbf-modifiers.json",
    "data/literature/pubmed/2026-04-26-sirolimus-beta-thalassemia.json",
    "data/literature/pubmed/2026-04-26-thalidomide-beta-thalassemia.json",
    "data/registries/clinicaltrials/2026-04-27-gene-therapy-beta-thalassemia.json",
    "data/registries/clinicaltrials/2026-04-27-indonesia-thalassemia-trials.json",
    "data/registries/clinicaltrials/2026-04-26-beta-thalassemia-fetal-hemoglobin.json",
    "data/registries/clinicaltrials/2026-04-26-sirolimus-beta-thalassemia.json",
    "data/registries/clinicaltrials/2026-04-26-thalidomide-beta-thalassemia.json",
    "research/thalassemia/README.md",
    "research/thalassemia/case-context/deidentified-case-001.md",
    "research/thalassemia/findings/2026-04-26-carrier-malaria.md",
    "research/thalassemia/findings/2026-04-26-bee-product-research-scope.md",
    "research/thalassemia/findings/2026-04-26-bee-derived-materials-beyond-honey.md",
    "research/thalassemia/findings/2026-04-26-bee-derived-hbf-evidence-gap.md",
    "research/thalassemia/findings/2026-04-26-clinical-baseline-checklist.md",
    "research/thalassemia/findings/2026-04-27-immune-transfusion-complication-lane.md",
    "research/thalassemia/findings/2026-04-26-clinical-trials-snapshot.md",
    "research/thalassemia/findings/2026-04-26-cure-strategy-map.md",
    "research/thalassemia/findings/2026-04-26-hbf-target-map.md",
    "research/thalassemia/findings/2026-04-26-hbf-target-priority-ranking.md",
    "research/thalassemia/findings/2026-04-26-hbf-reactivation-explainer.md",
    "research/thalassemia/findings/2026-04-26-hydroxyurea-deep-dive.md",
    "research/thalassemia/findings/2026-04-26-sirolimus-deep-dive.md",
    "research/thalassemia/findings/2026-04-26-thalidomide-class-deep-dive.md",
    "research/thalassemia/findings/2026-04-26-propolis-red-cell-deep-dive.md",
    "research/thalassemia/findings/2026-04-27-melittin-bee-venom-hazard-deep-dive.md",
    "research/thalassemia/findings/2026-04-27-royal-jelly-oxidative-stress-deep-dive.md",
    "research/thalassemia/findings/2026-04-27-gene-therapy-access-frontier.md",
    "research/thalassemia/findings/2026-04-26-assay-ready-hbf-screen.md",
    "research/thalassemia/findings/2026-04-26-assay-funnel-for-cure-discovery.md",
    "research/thalassemia/findings/2026-04-26-disease-taxonomy.md",
    "research/thalassemia/findings/2026-04-27-indonesia-genotype-first-rule.md",
    "research/thalassemia/findings/2026-04-26-indonesia-access-context.md",
    "research/thalassemia/findings/2026-04-26-indonesia-regulatory-access-gap.md",
    "research/thalassemia/findings/2026-04-27-indonesia-access-deep-dive.md",
    "research/thalassemia/findings/2026-04-26-mechanism-priority-map.md",
    "research/thalassemia/findings/2026-04-26-therapy-decision-matrix.md",
    "research/thalassemia/findings/2026-04-26-treatment-landscape.md",
    "research/thalassemia/findings/2026-04-26-repurposed-hbf-inducers.md",
    "research/thalassemia/hypotheses/README.md",
    "research/thalassemia/hypotheses/bee-derived-materials.md",
    "research/thalassemia/hypotheses/cure-oriented-hbf-mimicry.md",
    "research/thalassemia/hypotheses/hbf-small-molecule-triage.md",
    "research/thalassemia/hypotheses/hydroxyurea-evidence-map.md",
    "research/thalassemia/hypotheses/sirolimus-evidence-map.md",
    "research/thalassemia/hypotheses/thalidomide-class-evidence-map.md",
    "research/thalassemia/prioritization/2026-04-26-candidate-ranking.md",
    "research/thalassemia/references/source-registry.md",
    "research/islamic/README.md",
    "research/islamic/findings/2026-04-26-healing-and-caution.md",
    "research/islamic/findings/2026-04-26-theology-of-means.md",
    "research/islamic/quran/009-at-tawbah/014.md",
    "research/islamic/quran/010-yunus/057.md",
    "research/islamic/quran/016-an-nahl/068-069.md",
    "research/islamic/quran/017-al-isra/082.md",
    "research/islamic/quran/026-ash-shuara/080.md",
    "research/islamic/quran/041-fussilat/044.md",
    "research/islamic/quran/shifa-root-map.md",
    "research/islamic/quran/quran-wide-healing-search-plan.md",
    "paper/main.tex",
    "paper/notes/carrier-malaria.tex",
    "paper/references.bib",
    "pyproject.toml",
    "scripts/fetch_clinical_trials.py",
    "scripts/fetch_pubmed.py",
    "templates/clinician-review-brief-template.md",
    "templates/assay-run-template.md",
    "templates/hypothesis-card-template.md",
    "templates/patient-context-template.md",
]


def main() -> int:
    """Check that required repository files exist."""
    missing = [path for path in REQUIRED_PATHS if not pathlib.Path(path).exists()]

    if missing:
        print("Missing required repo files:")
        for path in missing:
            print(f"- {path}")
        return 1

    print("nakafa.lab scaffold is complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
