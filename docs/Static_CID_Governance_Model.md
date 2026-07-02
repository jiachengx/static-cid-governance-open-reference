---
license: CC-BY-SA-4.0
author: Stephen Hsu (許家誠)
contact: chiacheng.hsu@owasp.org
---

# Static CID Governance Model

## 1. Purpose

Static CID Governance is a content-governance model for static publishing and offline content editing environments. It separates logical identity, public route, immutable content snapshot, reference policy, and public-safe projection so that a static site can remain verifiable without requiring a database-backed server.

The model is designed for non-medical settings such as public knowledge sites, cultural archives, institutional announcements, digital collections, policy documentation, publication catalogues, and static public-data portals.

## 2. Why a new composition is needed

Content hashes are strong for integrity, but weak as long-term public references. Stable IDs are strong for external linking, but weak for detecting tampering. Static sites are easy to deploy, but they tend to lose consistency between public JSON, HTML, JavaScript, assets, and internal release records.

This model combines:

- stable logical identity;
- content-derived CID snapshots;
- route-level public addressability;
- version metadata derived from content hashes;
- reference policy for latest-tracking versus snapshot-pinning;
- public-safe projection without internal registry leakage;
- release-gate verification before publishing.

## 3. Core object envelope

```json
{
  "schema_version": "static-cid-governance-v1",
  "type": "announcement",
  "id": "ann-2026-001",
  "route": "/announcements/2026/001/",
  "title": "Example announcement",
  "summary": "A human-readable public summary.",
  "status": "published",
  "cid": "cid:announcement:sha256-...",
  "version": {
    "algorithm": "sha256",
    "digest": "...",
    "canonicalization": "static-cid-canonical-json-v1"
  },
  "reference": {
    "stable_ref": "announcement:ann-2026-001",
    "snapshot_cid": "cid:announcement:sha256-...",
    "policy": "track-latest"
  }
}
```

## 4. Identity layers

| Layer | Meaning | Stability |
|---|---|---|
| `id` | Logical identity of the object | Stable across content revisions |
| `route` | Public address | Stable unless site structure changes |
| `cid` | Content-derived snapshot identifier | Changes when governed content changes |
| `version.digest` | Digest extracted from CID | Changes with content snapshot |
| `reference.policy` | Latest-tracking or pinned snapshot behavior | Chosen by context |

## 5. Reference policies

`track-latest` is appropriate for public navigation, index pages, homepage cards, and ordinary content feeds.

`pinned-version` is appropriate for signatures, audits, release records, legal notices, citations, and historical reconstruction.

## 6. Public/private boundary

The public site may show IDs, routes, CIDs, source references, and human-readable summaries. It must not expose private registry paths, credential records, internal recovery tooling, internal approval logs, secrets, or release-gate implementation details.

## 7. Technical effect

The combined model provides these technical effects:

1. A public page can maintain stable links while also exposing verifiable content snapshots.
2. Static JSON projections can be checked against a source index before deployment.
3. Reference drift can be blocked before release.
4. Content hashes avoid self-reference instability by excluding governance fields from the canonical hash scope.
5. Public pages can display reference metadata without exposing private registry data.
6. Inventory baselines can prevent accidental deletion of public HTML, CSS, JavaScript, JSON, and assets during repackaging.

