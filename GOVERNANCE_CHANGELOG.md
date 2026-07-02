# Governance Changelog

This document records governance-level changes to the Static CID Governance model.

Unlike a normal software changelog, this file focuses on model evolution, integrity rules, public/private data boundaries, reference behavior, Offline Editor public behavior, and release verification logic.

## Governance areas tracked

### 1. Identity model

Tracks changes to stable logical identity, route identity, content-derived CID snapshots, version metadata, source reference metadata, and reference policy.

### 2. CID calculation model

Tracks changes to canonicalization rules, hash input scope, excluded self-reference fields, digest algorithms, CID formatting, and snapshot version handling.

### 3. Reference consistency model

Tracks changes to latest-tracking references, pinned snapshot references, source reference preservation, stale reference detection, and public display of reference metadata.

### 4. Public-safe projection

Tracks changes to public JSON output, static HTML display, public-safe schema fields, exclusion of private registry data, and AI/search-engine readable output.

### 5. Offline Editor governance behavior

Tracks changes to offline content editing, CID lookup, source reference import, validation timing, defensive coding assumptions, and public/private separation in editor workflows.

### 6. Release-gate verification

Tracks changes to reference verification, package inventory guarding, missing-file detection, public asset validation, schema validation, and static-site readiness checks.

## Governance principle

Every release should preserve the following rule:

> Public outputs may expose stable identity, route, CID snapshot, and public reference metadata, but must not expose private registry records, internal governance logs, credentials, organization-specific restricted content, or hidden account workflows.
