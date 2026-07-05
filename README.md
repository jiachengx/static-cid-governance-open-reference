Static CID Governance Open Reference

Author / Maintainer: Stephen Chia-Cheng Hsu
Chinese Name: 許家誠
Contact: chiacheng.hsu@owasp.org
GitHub: https://github.com/jiachengx
Public reference version: v1.1.3
DOI: https://doi.org/10.5281/zenodo.21139438

GitHub repository

Recommended public repository URL:

https://github.com/jiachengx/static-cid-governance-open-reference

How to cite

If you use or reference this project, please cite:

«Hsu, Stephen Chia-Cheng. Static CID Governance: An Original CID-Native Governance Model for Static Publishing. Version v1.1.3. 2026. Zenodo. https://doi.org/10.5281/zenodo.21139438»

GitHub repository:

https://github.com/jiachengx/static-cid-governance-open-reference

A "CITATION.cff" file is included for citation metadata.

Overview

Static CID Governance is an original CID-native governance architecture developed by Stephen Chia-Cheng Hsu for static publishing, offline content governance, public-safe projection, release integrity, and reference consistency.

It is designed for non-medical use cases such as public websites, digital archives, nonprofit publishing, educational content, documentation systems, and static public-data portals. Its purpose is to make static publishing more predictable, verifiable, and governable without requiring a database-backed server.

This project is not another CMS, not another data catalog, and not a database replacement. It is a lightweight governance pattern for trustworthy static publishing.

Why this project exists

Many governance tools exist, but they are usually optimized for enterprise data platforms, software supply chains, digital preservation repositories, or static-site editing as separate concerns.

Enterprise data governance platforms are powerful but often too heavy for nonprofit static publishing. Open-source metadata platforms focus on data catalogs and lineage. Software supply-chain frameworks focus on artifact integrity and build provenance. Digital preservation tools focus on long-term preservation. Static CMS tools focus on editing content.

Static CID Governance focuses on the gap between these domains: how a small nonprofit, educational, public-interest, or digital archive team can maintain stable content identity, CID-based snapshots, public-safe projection, source-reference metadata, release-gate verification, inventory guarding, and governance-oriented changelog records without operating a heavy database-backed platform.

This project is released as an open reference because hybrid governance patterns of this kind are still uncommon, and their value increases when they can be studied, audited, adapted, and improved by others.

File-as-NoSQL DB model

Static CID Governance uses a file-as-NoSQL DB approach.

It does not require a database server, and it does not depend on Git as the internal data store. Instead, structured files act as records, directories act as collections or namespaces, registries act as governance indexes, CID snapshots provide immutable content identities, manifests provide package integrity maps, and changelog records provide governance history.

A release package, together with SHA256 checksums, CID snapshots, manifests, release notes, and release-gate validation, forms the version and integrity layer of the system.

GitHub may be used as a public distribution, citation, and collaboration platform, but the governance model itself is designed to work without Git.

In short:

structured files   = governance records
directories        = collections or namespaces
registry           = governance index
CID                = immutable content snapshot identity
manifest           = package integrity map
SHA256             = package and file integrity proof
CHANGELOG          = governance history
release gate       = consistency checker
release package    = portable release unit
public projection  = publishable read-only view

Original CID-native governance model

This repository documents Stephen Chia-Cheng Hsu’s original CID-native governance model for static publishing and offline content governance.

The model keeps the core governance layer stable and minimal. Core records define logical identity, public route, content-derived CID snapshots, version metadata, reference behavior, and public-safe projection. Additional governance capabilities may be attached through modular components without expanding the core model.

This repository does not implement, depend on, or derive from any external domain-specific data standard. Its contribution is the governance composition: combining stable logical identity, content-derived snapshots, public-safe projection, source-reference metadata, registry policy, release-gate verification, inventory guarding, and governance-oriented changelog practice into a reusable static publishing governance pattern.

In this project:

* "stable_id" identifies which logical object is being referenced.
* "route" identifies where the object is publicly published.
* "cid" identifies a content-derived immutable snapshot.
* "version" records digest metadata derived from the CID.
* "reference" records whether a link tracks the latest object or pins a specific snapshot.
* "public_view" exposes only public-safe data without leaking private registry or internal governance records.

This model may be described as:

original CID-native static publishing governance model
modular CID-native governance architecture
static publishing governance pattern with CID-based reference consistency

It should not be described as:

a CMS
a database replacement
an enterprise data governance platform
an implementation of an external domain-specific standard
a derivative standard
an organization-specific private governance system

What this repository contains

This repository contains:

* A neutral technical model for stable logical identity and content-derived CID snapshots.
* A minimal reference implementation for canonical hashing, CID generation, public projection, reference verification, and inventory guarding.
* A public Offline Editor reference structure using layered GPL/MIT licensing.
* A small static-site example with public-safe JSON and reference metadata.
* Mermaid diagrams and technical notes for review, teaching, and future revision.
* Layered licensing for code, examples, schemas, policies, documentation, and templates.
* Public license statements for nonprofit, educational, public-interest, and digital archive use cases.
* Governance-oriented changelog examples and release documentation.

What this repository deliberately excludes

This repository does not include organization-specific website content, press images, private registries, credential tools, account recovery workflows, internal account policies, production deployment secrets, production deployment data, project-specific implementation records, or private governance logs.

See:

docs/EXCLUDED_CONTENT.md
docs/PUBLICATION_BOUNDARY.md

These exclusions are intentional. The public reference model is meant to be reusable without exposing project-specific content, credentials, private governance data, or organization-specific operational details.

Offline Editor licensing strategy

The Offline Editor components are released under a layered licensing model.

Core governance tools are licensed under "GPL-3.0-or-later" so that redistributed modified versions of the governance engine remain open. This includes CID generation, canonicalization, reference verification, release-gate checks, public/private projection validation, and package inventory guarding.

Reusable UI templates, demo forms, sample schemas, public-static-site examples, and non-production examples are licensed under "MIT" to lower the adoption barrier for nonprofit institutions, educational projects, digital archives, and small public-interest websites.

Documentation, diagrams, reports, and teaching materials are licensed under "CC BY-SA 4.0" to encourage attribution-based sharing and improvement.

This project is released in this form because it was developed for nonprofit-oriented use cases and is intended to serve as an open reference implementation. It provides a practical starting point that others can study, adopt, improve, and adapt to their own governance environments under the applicable open-source license terms.

Licensing

This repository uses layered licensing:

Path| License| Intent
"tools/**"| GPL-3.0-or-later| Keep the core governance tools open when redistributed.
"offline-editor/core/**"| GPL-3.0-or-later| Keep Offline Editor governance logic open when redistributed.
"offline-editor/ui/**"| MIT| Allow broad reuse of standalone UI templates.
"offline-editor/examples/**"| MIT| Allow broad reuse of neutral Offline Editor examples.
"examples/**"| MIT| Allow broad reuse of the public static-site example.
"schemas/**"| MIT| Allow broad implementation of the public model.
"policies/**"| MIT| Allow adaptation of public policy templates.
"tests/**"| MIT| Allow reuse of tests and smoke checks.
"docs/**"| CC-BY-SA-4.0| Allow sharing and adaptation of documentation with attribution and share-alike.
root metadata files| See file headers| Administrative repository material.

The full license texts are provided under "LICENSES/".

No patent license is granted by this repository except to the extent expressly provided by the applicable open-source license for a specific file or component.

For example, GPL-licensed components are licensed under the terms of "GPL-3.0-or-later", including any patent-related terms contained in that license. MIT-licensed and CC-BY-SA-licensed materials are governed by their respective license terms.

Publication of this repository does not waive any patent rights that may exist outside the scope of the applicable license.

Quick start

Run the reference tools against the included static-site example:

python tools/cid_governance/cid_model.py examples/public-static-site/data/content.json
python tools/cid_governance/project_public_projection.py examples/public-static-site/data/content.json /tmp/public_projection.json
python tools/cid_governance/verify_references.py examples/public-static-site/data/content.json
python tools/cid_governance/inventory_guard.py --root examples/public-static-site --baseline policies/public-static-site-baseline.json
python tests/smoke_test.py

The goal of the quick start is to demonstrate the governance loop:

structured content
→ CID snapshot
→ public-safe projection
→ reference verification
→ inventory guard
→ release readiness

Core model

A governed content object is represented through six distinct layers:

stable_id      = which logical object this is
route          = where the public object is published
cid            = which immutable content snapshot this is
version        = digest metadata derived from the CID
reference      = whether another object tracks latest or pins a specific snapshot
public_view    = public-safe projection without internal registry leakage

The design goal is not to make static sites complicated. It is to make them predictable, verifiable, and easier to govern without requiring a database-backed server.

Reference modes

Static CID Governance distinguishes between stable logical references and pinned snapshot references.

A stable reference answers:

Which logical object is this?

A snapshot reference answers:

Which exact content version is this?

This separation allows static publishing systems to support both:

track-latest references
pinned-version references

This is important for public websites, digital archives, nonprofit publishing, and documentation systems where pages may update over time but citations, signatures, audit records, or source references must remain anchored to a specific content snapshot.

Public-safe projection

A public projection is a read-only publishable view generated from governed content records.

It may expose:

stable_id
route
cid
version snapshot
public title
public summary
public category
public reference metadata

It must not expose:

private registry records
internal governance logs
credentials
deployment secrets
account recovery workflows
organization-specific restricted content
production-only operational records

The public projection is designed for static hosting, search engines, AI crawlers, accessibility, and long-term public readability.

Modular governance extensions

The core model is intentionally kept small. Additional governance capabilities should be attached through modular components rather than added directly into the core record.

Examples of optional governance modules include:

evidence governance
source registry
citation registry
video reference registry
field note registry
transcript registry
timeline enrichment
marketing projection

This keeps the core model stable while allowing future projects to extend the governance layer according to their actual needs.

The recommended boundary is:

core model      = identity, route, CID, version, reference behavior, public-safe projection
extensions      = evidence, source confidence, citations, video references, transcripts, marketing use
public output   = only approved public-safe projection
internal layer  = private governance records, audit details, restricted source metadata

Governance changelog

This project treats changelog records as governance artifacts, not merely software release notes.

A governance changelog should record:

* what changed;
* why it changed;
* what governance risk was reduced;
* whether identity behavior changed;
* whether reference behavior changed;
* whether public/private boundaries changed;
* whether release-gate validation changed;
* whether migration is required;
* what future maintainers should know.

The companion repository documents this pattern:

https://github.com/jiachengx/static-cid-governance-changelog-pattern

Public licensing statement

Static CID Governance and its related Offline Editor reference components are publicly released by Stephen Chia-Cheng Hsu as an open reference implementation for nonprofit, educational, public-interest, digital archive, and static publishing use cases.

This release is intended to help nonprofit organizations legally study, adopt, modify, and improve the model under clear open-source terms. It provides a practical governance foundation for content integrity, offline editing, static publishing, reference consistency, and public/private data boundary protection.

The project uses a layered licensing model:

* Core governance tools are licensed under GPL-3.0-or-later.
* Public examples, schemas, policies, templates, and sample static-site components are licensed under MIT.
* Documentation, diagrams, reports, and teaching materials are licensed under CC BY-SA 4.0.

This means nonprofit organizations may use the materials according to the applicable license terms, while preserving author attribution and respecting the openness requirements of each license.

Suggested repository topics

Suggested GitHub topics:

static-site
content-addressing
cid
data-governance
digital-archives
nonprofit
offline-editor
release-gate
provenance
public-data
governance
open-source

Suggested repository description

Original CID-native governance model for static publishing and offline content governance.

Scope and non-goals

This project is intended to provide a reusable governance pattern and reference implementation.

It is not intended to be:

* a full enterprise data governance platform;
* a database server;
* a traditional CMS;
* a replacement for digital preservation systems;
* a replacement for software supply-chain security frameworks;
* a complete production deployment for any specific organization;
* a repository for private registries, production logs, or organization-specific content.

Citation metadata

This repository includes:

CITATION.cff

Recommended citation:

Hsu, Stephen Chia-Cheng. Static CID Governance: An Original CID-Native Governance Model for Static Publishing. Version v1.1.3. 2026. Zenodo. https://doi.org/10.5281/zenodo.21139438

Release and DOI

Current public reference release:

v1.1.3

Zenodo DOI:

https://doi.org/10.5281/zenodo.21139438

GitHub releases:

https://github.com/jiachengx/static-cid-governance-open-reference/releases

Latest release:

https://github.com/jiachengx/static-cid-governance-open-reference/releases/latest

Independence notice

This repository documents an original CID-native governance model by Stephen Chia-Cheng Hsu. The DOI is provided for citation, preservation, and research traceability only.

The DOI does not represent institutional endorsement, third-party certification, or adoption of an external standard. This repository is an open reference implementation and should be evaluated on its own architecture, documentation, source code, governance model, and release artifacts.

Author

Stephen Chia-Cheng Hsu
Chinese name: 許家誠
Contact: chiacheng.hsu@owasp.org
GitHub: https://github.com/jiachengx

Copyright

Copyright © 2026 Stephen Chia-Cheng Hsu.

See "LICENSE.md", "NOTICE", and "COPYRIGHT" for licensing and attribution details.
