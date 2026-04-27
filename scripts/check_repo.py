"""Validate the required Nakafa Lab scaffold files."""

from __future__ import annotations

import pathlib

from helpers.manifest import load_manifest

MANIFEST_PATH = pathlib.Path("scripts/manifests/required_paths.txt")


def missing_paths(required_paths: list[str]) -> list[str]:
    """Return required paths that are missing from the working tree."""
    return [path for path in required_paths if not pathlib.Path(path).exists()]


def main() -> int:
    """Check that required repository files exist."""
    missing = missing_paths(load_manifest(MANIFEST_PATH))

    if not missing:
        print("nakafa.lab scaffold is complete.")
        return 0

    print("Missing required repo files:")
    for path in missing:
        print(f"- {path}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
