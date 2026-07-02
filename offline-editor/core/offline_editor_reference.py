# SPDX-FileCopyrightText: 2026 Stephen Hsu (許家誠)
# SPDX-License-Identifier: GPL-3.0-or-later
"""Minimal Offline Editor governance reference.

This module is intentionally small. It demonstrates the public governance pattern
without exposing any production-specific registry or credential workflow.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.cid_governance.cid_model import compute_digest


@dataclass(frozen=True)
class OfflineDraft:
    """Neutral content draft with optional source-reference metadata."""

    stable_id: str
    route: str
    title: str
    body: str
    source_ref_cid: str | None = None
    source_ref_id: str | None = None
    source_ref_route: str | None = None

    def to_governed_record(self) -> dict[str, Any]:
        public_body = {
            "stable_id": self.stable_id,
            "route": self.route,
            "title": self.title,
            "body": self.body,
        }
        digest = compute_digest(public_body)
        record: dict[str, Any] = {
            **public_body,
            "cid": f"cid:content:sha256-{digest}",
            "version": {"algorithm": "sha256", "digest": digest},
            "reference": {"policy": "track-latest", "snapshot_cid": f"cid:content:sha256-{digest}"},
        }
        if self.source_ref_cid:
            record["source_reference"] = {
                "source_ref_cid": self.source_ref_cid,
                "source_ref_id": self.source_ref_id,
                "source_ref_route": self.source_ref_route,
            }
        return record


def save_record(record: Mapping[str, Any], output_path: str | Path) -> None:
    """Save a governed record as deterministic JSON."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    draft = OfflineDraft(
        stable_id="note-001",
        route="/notes/001/",
        title="Neutral sample note",
        body="This sample demonstrates offline drafting with a content-derived snapshot.",
    )
    print(json.dumps(draft.to_governed_record(), ensure_ascii=False, indent=2, sort_keys=True))
