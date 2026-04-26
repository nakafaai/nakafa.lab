from pathlib import Path


REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "docs/research-protocol.md",
    "docs/zed-latex.md",
    ".zed/tasks.json",
    "research/thalassemia/README.md",
    "research/thalassemia/references/source-registry.md",
    "research/islamic/README.md",
    "paper/main.tex",
    "paper/references.bib",
    "pyproject.toml",
]


def main() -> int:
    missing = [path for path in REQUIRED_PATHS if not Path(path).exists()]

    if missing:
        print("Missing required repo files:")
        for path in missing:
            print(f"- {path}")
        return 1

    print("nakafa.lab scaffold is complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
