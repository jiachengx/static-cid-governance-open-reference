#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Create a public-safe projection from governed content JSON."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

PUBLIC_FIELDS = [
    "schema_version",
    "type",
    "id",
    "route",
    "title",
    "summary",
    "status",
    "cid",
    "version",
    "reference",
    "source_ref",
]
DENY_FIELDS = {"governance", "credentials", "secrets", "private_registry_path", "release_gate_internal_log"}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def sanitize_object(obj: dict[str, Any]) -> dict[str, Any]:
    for forbidden in DENY_FIELDS:
        if forbidden in obj:
            raise ValueError(f"Object {obj.get('id', '<unknown>')} contains private field {forbidden!r}")
    projected = {key: obj[key] for key in PUBLIC_FIELDS if key in obj}
    if "version" in projected and isinstance(projected["version"], dict):
        projected["version"] = {"digest": projected["version"].get("digest")}
    if "reference" in projected and isinstance(projected["reference"], dict):
        ref = projected["reference"]
        projected["reference"] = {
            "stable_ref": ref.get("stable_ref"),
            "snapshot_cid": ref.get("snapshot_cid"),
            "policy": ref.get("policy"),
        }
    return {k: v for k, v in projected.items() if v is not None}


def project(data: Any) -> Any:
    if isinstance(data, list):
        return [sanitize_object(item) for item in data if isinstance(item, dict)]
    if isinstance(data, dict) and isinstance(data.get("items"), list):
        return {"items": [sanitize_object(item) for item in data["items"] if isinstance(item, dict)]}
    if isinstance(data, dict):
        return sanitize_object(data)
    raise ValueError("Input must be a JSON object, array, or object containing an 'items' array")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate public-safe Static CID projection JSON.")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args(argv)
    try:
        projected = project(load_json(args.input))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(projected, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return 0
    except Exception as exc:  # defensive CLI boundary
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
