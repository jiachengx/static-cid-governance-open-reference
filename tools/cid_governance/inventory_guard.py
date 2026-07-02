#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Verify that a public static-site output still contains baseline files."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_baseline(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise ValueError("Baseline must be a JSON object")
    return data


def verify(root: Path, baseline: dict) -> list[str]:
    errors: list[str] = []
    required = baseline.get("required_files") or []
    allowed_ext = set(baseline.get("allowed_public_extensions") or [])
    max_json_bytes = int(baseline.get("maximum_json_bytes") or 0)

    for rel in required:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if allowed_ext and path.suffix and path.suffix not in allowed_ext:
            errors.append(f"disallowed extension: {rel}")
        if max_json_bytes and path.suffix == ".json" and path.stat().st_size > max_json_bytes:
            errors.append(f"JSON too large: {rel} ({path.stat().st_size} bytes)")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify public static-site inventory baseline.")
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--baseline", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        errors = verify(args.root, load_baseline(args.baseline))
        if errors:
            for err in errors:
                print(f"ERROR: {err}", file=sys.stderr)
            return 1
        print("PASS: public inventory baseline is satisfied")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
