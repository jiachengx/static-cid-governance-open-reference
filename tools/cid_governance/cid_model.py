#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Generate and normalize Static CID Governance objects.

This is a neutral reference implementation. It intentionally avoids any
organization-specific paths, names, credentials, or deployment assumptions.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

DEFAULT_EXCLUDED_TOP_LEVEL = {"cid", "version", "reference", "source_ref", "governance", "meta"}
CANONICALIZATION = "static-cid-canonical-json-v1"
SCHEMA_VERSION = "static-cid-governance-v1"


class CIDModelError(ValueError):
    """Raised when an input object cannot be normalized safely."""


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError as exc:
        raise CIDModelError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise CIDModelError(f"Invalid JSON in {path}: {exc}") from exc


def dump_json(data: Any, path: Path | None = None) -> None:
    payload = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=False) + "\n"
    if path is None:
        sys.stdout.write(payload)
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(payload, encoding="utf-8")


def strip_governance_fields(obj: Any, excluded_top_level: Iterable[str] = DEFAULT_EXCLUDED_TOP_LEVEL) -> Any:
    """Return a copy with self-referential governance fields removed.

    The purpose is to prevent the digest from depending on the CID/version
    fields that the digest itself produces.
    """
    excluded = set(excluded_top_level)
    if isinstance(obj, list):
        return [strip_governance_fields(item, excluded) for item in obj]
    if isinstance(obj, dict):
        cleaned: dict[str, Any] = {}
        for key, value in obj.items():
            if key in excluded:
                continue
            cleaned[key] = strip_governance_fields(value, excluded)
        return cleaned
    return obj


def canonicalize(obj: Any) -> bytes:
    """Serialize JSON deterministically for hashing."""
    clean = strip_governance_fields(obj)
    return json.dumps(clean, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def compute_digest(obj: Any) -> str:
    return hashlib.sha256(canonicalize(obj)).hexdigest()


def generate_cid(content_type: str, digest: str) -> str:
    if not content_type or not content_type.replace("-", "_").replace("_", "").isalnum():
        raise CIDModelError(f"Unsafe content type: {content_type!r}")
    if len(digest) != 64 or any(ch not in "0123456789abcdef" for ch in digest):
        raise CIDModelError(f"Invalid sha256 digest: {digest!r}")
    return f"cid:{content_type}:sha256-{digest}"


def stable_ref(content_type: str, stable_id: str) -> str:
    if not stable_id:
        raise CIDModelError("Missing stable id")
    return f"{content_type}:{stable_id}"


def normalize_object(obj: dict[str, Any], *, reference_policy: str | None = None) -> dict[str, Any]:
    if not isinstance(obj, dict):
        raise CIDModelError("A governed object must be a JSON object")
    result = copy.deepcopy(obj)
    content_type = str(result.get("type") or "content")
    stable_id = str(result.get("id") or "").strip()
    route = str(result.get("route") or "").strip()
    if not stable_id:
        raise CIDModelError("Object requires a stable 'id'")
    if not route.startswith("/"):
        raise CIDModelError("Object requires a public 'route' starting with '/'")

    result.setdefault("schema_version", SCHEMA_VERSION)
    digest = compute_digest(result)
    cid = generate_cid(content_type, digest)
    policy = reference_policy or result.get("reference", {}).get("policy") or "track-latest"
    if policy not in {"track-latest", "pinned-version"}:
        raise CIDModelError(f"Unsupported reference policy: {policy}")

    result["cid"] = cid
    result["version"] = {
        "algorithm": "sha256",
        "digest": digest,
        "canonicalization": CANONICALIZATION,
    }
    result["reference"] = {
        "stable_ref": stable_ref(content_type, stable_id),
        "snapshot_cid": cid,
        "policy": policy,
    }
    return result


def normalize_collection(data: Any) -> Any:
    if isinstance(data, list):
        return [normalize_object(item) if isinstance(item, dict) else item for item in data]
    if isinstance(data, dict) and isinstance(data.get("items"), list):
        data = copy.deepcopy(data)
        data["items"] = [normalize_object(item) if isinstance(item, dict) else item for item in data["items"]]
        return data
    if isinstance(data, dict):
        return normalize_object(data)
    raise CIDModelError("Input JSON must be an object, an array, or an object containing an 'items' array")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Normalize Static CID Governance JSON.")
    parser.add_argument("input", type=Path, help="Input JSON file")
    parser.add_argument("-o", "--output", type=Path, help="Output JSON file; defaults to stdout")
    args = parser.parse_args(argv)
    try:
        data = load_json(args.input)
        normalized = normalize_collection(data)
        dump_json(normalized, args.output)
        return 0
    except CIDModelError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
