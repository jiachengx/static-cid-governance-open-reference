#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Smoke test for the Static CID Governance reference package."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable

COMMANDS = [
    [PY, str(ROOT / "tools/cid_governance/cid_model.py"), str(ROOT / "examples/public-static-site/data/content.json")],
    [PY, str(ROOT / "tools/cid_governance/verify_references.py"), str(ROOT / "examples/public-static-site/data/content.json")],
    [PY, str(ROOT / "tools/cid_governance/inventory_guard.py"), "--root", str(ROOT / "examples/public-static-site"), "--baseline", str(ROOT / "policies/public-static-site-baseline.json")],
]


def main() -> int:
    for cmd in COMMANDS:
        result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
        if result.returncode != 0:
            print(result.stdout)
            print(result.stderr, file=sys.stderr)
            return result.returncode
    print("PASS: smoke tests completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Offline Editor reference smoke check
import subprocess, sys
subprocess.check_call([sys.executable, "offline-editor/core/offline_editor_reference.py"], stdout=subprocess.DEVNULL)
