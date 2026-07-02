# Static CID Governance Open Reference

**Author / Maintainer:** Stephen Chiacheng Hsu  
**Chinese Name:** 許家誠
**Contact:** chiacheng.hsu@owasp.org  
## GitHub repository

Recommended public repository URL:

```text
https://github.com/jiachengx/static-cid-governance-open-reference
```

If you use or reference this project, please cite it using `CITATION.cff`.

**Public reference version:** v1.1.0  

Static CID Governance is an inventor-developed open reference model for CID-based reference consistency governance in static publishing and offline content governance environments.

It is designed for non-medical use cases such as public websites, digital archives, nonprofit publishing, educational content, documentation systems, and static public-data portals. Its purpose is to make static publishing more predictable, verifiable, and governable without requiring a database-backed server.

## Relationship to FHIR

This repository is **not** an implementation of HL7 FHIR, not a FHIR Implementation Guide, not a FHIR profile, and not a non-medical edition of FHIR.

FHIR is referenced only as a mature source of design ideas. This project selectively adapts concepts such as logical identity, versioned references, human-readable narrative, controlled coding, and provenance-style auditability into a non-medical static publishing context.

In this project:

- `stable_id` identifies which logical object is being referenced.
- `route` identifies where the object is publicly published.
- `cid` identifies a content-derived immutable snapshot.
- `version` records digest metadata derived from the CID.
- `reference` records whether a link tracks the latest object or pins a specific snapshot.
- `public_view` exposes only public-safe data without leaking private registry or internal governance records.

This project does not claim ownership over FHIR, IPFS, Git, W3C PROV, content addressing, hashing, provenance, or versioned references. Its contribution is the governance composition: combining stable logical identity, content-derived snapshots, public-safe projection, source-reference metadata, registry policy, and release-gate verification into a reusable static publishing governance pattern.

## What this repository contains

- A neutral technical model for stable logical identity and content-derived CID snapshots.
- A minimal reference implementation for canonical hashing, CID generation, public projection, reference verification, and inventory guarding.
- A public Offline Editor reference structure using layered GPL/MIT licensing.
- A small static-site example with public-safe JSON and reference metadata.
- Mermaid diagrams and technical notes for review, teaching, and future revision.
- Layered licensing for code, examples, schemas, policies, documentation, and templates.

## What this repository deliberately excludes

This repository does not include organization-specific website content, press images, private registries, credential tools, account recovery workflows, internal account policies, production deployment secrets, or private governance logs.

See [`docs/EXCLUDED_CONTENT.md`](docs/EXCLUDED_CONTENT.md) and [`docs/PUBLICATION_BOUNDARY.md`](docs/PUBLICATION_BOUNDARY.md).

## Offline Editor licensing strategy

The Offline Editor components are released under a layered licensing model.

Core governance tools are licensed under `GPL-3.0-or-later` so that redistributed modified versions of the governance engine remain open. This includes CID generation, canonicalization, reference verification, release-gate checks, public/private projection validation, and package inventory guarding.

Reusable UI templates, demo forms, sample schemas, public-static-site examples, and non-production examples are licensed under `MIT` to lower the adoption barrier for nonprofit institutions, educational projects, digital archives, and small public-interest websites.

Documentation, diagrams, reports, and teaching materials are licensed under `CC BY-SA 4.0` to encourage attribution-based sharing and improvement.

This project is released in this form because it was developed for nonprofit-oriented use cases and is intended to serve as an open reference implementation. The goal is not to create a patent barrier, but to provide a practical starting point that others can study, adopt, improve, and adapt to their own governance environments.

## Licensing

This repository uses layered licensing:

| Path | License | Intent |
|---|---|---|
| `tools/**` | GPL-3.0-or-later | Keep the core governance tools open when redistributed. |
| `offline-editor/core/**` | GPL-3.0-or-later | Keep Offline Editor governance logic open when redistributed. |
| `offline-editor/ui/**` | MIT | Allow broad reuse of standalone UI templates. |
| `offline-editor/examples/**` | MIT | Allow broad reuse of neutral Offline Editor examples. |
| `examples/**` | MIT | Allow broad reuse of the public static-site example. |
| `schemas/**` | MIT | Allow broad implementation of the public model. |
| `policies/**` | MIT | Allow adaptation of public policy templates. |
| `tests/**` | MIT | Allow reuse of tests and smoke checks. |
| `docs/**` | CC-BY-SA-4.0 | Allow sharing and adaptation of documentation with attribution and share-alike. |
| root metadata files | See file headers | Administrative repository material. |

No patent license, trademark license, or endorsement is granted unless explicitly stated in a separate written license.

## Quick start

```bash
python tools/cid_governance/cid_model.py examples/public-static-site/data/content.json
python tools/cid_governance/project_public_projection.py examples/public-static-site/data/content.json /tmp/public_projection.json
python tools/cid_governance/verify_references.py examples/public-static-site/data/content.json
python tools/cid_governance/inventory_guard.py --root examples/public-static-site --baseline policies/public-static-site-baseline.json
python tests/smoke_test.py
```

## Core model

A governed content object is represented through six distinct layers:

```text
stable_id      = which logical object this is
route          = where the public object is published
cid            = which immutable content snapshot this is
version        = digest metadata derived from the CID
reference      = whether another object tracks latest or pins a specific snapshot
public_view    = public-safe projection without internal registry leakage
```

The design goal is not to make static sites complicated. It is to make them predictable, verifiable, and easier to govern without requiring a database-backed server.

## Trademark and attribution notice

HL7®, FHIR®, and related marks are trademarks of Health Level Seven International. This repository is independent and is not endorsed, certified, sponsored, or approved by HL7.

FHIR is cited only for conceptual comparison and attribution. The project should be described as “FHIR-informed” or “inspired by selected FHIR concepts,” not as “FHIR for non-medical platforms” or “FHIR Lite.”
