#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Verify reference consistency for Static CID Governance JSON."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def iter_objects(data: Any):
    if isinstance(data, list):
        yield from (item for item in data if isinstance(item, dict))
    elif isinstance(data, dict) and isinstance(data.get("items"), list):
        yield from (item for item in data["items"] if isinstance(item, dict))
    elif isinstance(data, dict):
        yield data


def verify(data: Any) -> list[str]:
    errors: list[str] = []
    by_cid: dict[str, dict[str, Any]] = {}
    by_ref: dict[str, dict[str, Any]] = {}

    objects = list(iter_objects(data))
    for obj in objects:
        cid = obj.get("cid")
        ref = obj.get("reference") or {}
        stable_ref = ref.get("stable_ref")
        if not cid:
            errors.append(f"{obj.get('id', '<unknown>')}: missing cid")
        else:
            by_cid[cid] = obj
        if stable_ref:
            by_ref[stable_ref] = obj

    for obj in objects:
        oid = obj.get("id", "<unknown>")
        ref = obj.get("reference") or {}
        if ref.get("snapshot_cid") and ref["snapshot_cid"] != obj.get("cid"):
            errors.append(f"{oid}: reference.snapshot_cid does not match object cid")
        if ref.get("stable_ref") and not str(ref["stable_ref"]).endswith(f":{oid}"):
            errors.append(f"{oid}: reference.stable_ref does not end with object id")
        if ref.get("policy") not in {"track-latest", "pinned-version"}:
            errors.append(f"{oid}: unsupported reference policy {ref.get('policy')!r}")

        source = obj.get("source_ref") or {}
        if source.get("snapshot_cid") and source["snapshot_cid"] not in by_cid:
            errors.append(f"{oid}: source_ref.snapshot_cid not found in collection")
        if source.get("stable_ref") and source["stable_ref"] not in by_ref:
            errors.append(f"{oid}: source_ref.stable_ref not found in collection")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify Static CID Governance references.")
    parser.add_argument("input", type=Path)
    args = parser.parse_args(argv)
    try:
        errors = verify(load_json(args.input))
        if errors:
            for err in errors:
                print(f"ERROR: {err}", file=sys.stderr)
            return 1
        print("PASS: references are consistent")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
