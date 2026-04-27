"""Helpers for reading line-oriented repository manifests."""

from __future__ import annotations

import pathlib


def load_manifest(path: pathlib.Path) -> list[str]:
    """Load non-empty, non-comment lines from a manifest file."""
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if should_keep_line(line)]


def should_keep_line(line: str) -> bool:
    """Return whether a manifest line contains a required path entry."""
    stripped = line.strip()
    return bool(stripped and not stripped.startswith("#"))
