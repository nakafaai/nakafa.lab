"""Validate the required Nakafa Lab scaffold files."""

import pathlib


REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "docs/research-protocol.md",
    "docs/next-steps.md",
    "docs/parallel-research-tracks.md",
    "docs/zed-latex.md",
    ".zed/tasks.json",
    "research/thalassemia/README.md",
    "research/thalassemia/case-context/deidentified-case-001.md",
    "research/thalassemia/findings/2026-04-26-carrier-malaria.md",
    "research/thalassemia/findings/2026-04-26-bee-product-research-scope.md",
    "research/thalassemia/findings/2026-04-26-bee-derived-materials-beyond-honey.md",
    "research/thalassemia/findings/2026-04-26-clinical-baseline-checklist.md",
    "research/thalassemia/findings/2026-04-26-clinical-trials-snapshot.md",
    "research/thalassemia/findings/2026-04-26-disease-taxonomy.md",
    "research/thalassemia/findings/2026-04-26-indonesia-access-context.md",
    "research/thalassemia/findings/2026-04-26-indonesia-regulatory-access-gap.md",
    "research/thalassemia/findings/2026-04-26-mechanism-priority-map.md",
    "research/thalassemia/findings/2026-04-26-therapy-decision-matrix.md",
    "research/thalassemia/findings/2026-04-26-treatment-landscape.md",
    "research/thalassemia/hypotheses/README.md",
    "research/thalassemia/hypotheses/bee-derived-materials.md",
    "research/thalassemia/references/source-registry.md",
    "research/islamic/README.md",
    "research/islamic/findings/2026-04-26-healing-and-caution.md",
    "research/islamic/quran/016-an-nahl/068-069.md",
    "research/islamic/quran/quran-wide-healing-search-plan.md",
    "paper/main.tex",
    "paper/notes/carrier-malaria.tex",
    "paper/references.bib",
    "pyproject.toml",
    "scripts/fetch_clinical_trials.py",
    "templates/clinician-review-brief-template.md",
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
