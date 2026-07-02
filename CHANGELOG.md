# Changelog

All notable changes to this project are documented here.

This changelog is not only a software release log. For this project, it also serves as a public governance trail for the Static CID Governance model, including changes to CID identity handling, reference consistency, public-safe projection, release-gate verification, Offline Editor public behavior, and nonprofit-oriented maintainability.

## [1.1.0] - 2026-07-02

### Added

- Added public Offline Editor reference structure using layered GPL/MIT licensing.
- Added public licensing statements in English and Traditional Chinese.
- Added FHIR-safe repository positioning: FHIR-informed, not FHIR implementation, not FHIR Lite, and not a non-medical edition of FHIR.
- Added clearer directory-level licensing matrix for Offline Editor core, UI templates, examples, schemas, policies, tests, and documentation.

### Governance Notes

- The release clarifies that the project is an inventor-developed open reference implementation by Stephen Hsu (許家誠).
- The release keeps organization-specific content, private registries, credential flows, internal release logs, and production deployment data outside the public release boundary.
- Offline Editor core governance logic is separated from reusable UI templates so nonprofit users can study the governance pattern without inheriting production-specific implementation details.

### Public/Private Boundary Notes

- Public examples remain neutral and do not contain organization-specific content or media.
- The package is suitable for public GitHub release as an open reference repository.

## [1.0.0] - 2026-07-02

### Added

- Initial public reference release of Static CID Governance.
- Added CID-based reference consistency model for static publishing and offline content governance.
- Added stable logical identity, content-derived CID snapshots, reference policy, public-safe projection, and release-gate verification concepts.
- Added minimal reference tools for CID generation, public projection, reference verification, and inventory guarding.
- Added public static-site examples using neutral sample data.
- Added Mermaid diagrams for system architecture, reference modes, and release governance flow.
- Added layered licensing for tools, examples, schemas, policies, tests, and docs.

### Governance Notes

- This release establishes the core distinction between stable logical identity and content-derived immutable snapshots.
- Public examples are designed to show reference consistency without exposing private registry data or organization-specific content.
- The model is FHIR-informed but is not a FHIR implementation, FHIR profile, FHIR Implementation Guide, or non-medical edition of FHIR.

## [1.1.1] - 2026-07-02

### Added

- Added `CITATION.cff` with the public GitHub namespace `jiachengx`.
- Added `GITHUB_UPLOAD_GUIDE.md` with repository URL, topics, upload commands, and first-release notes.
- Added `docs/WHY_THIS_PROJECT.md` for public explanation and citation context.

### Governance Notes

- This release prepares the repository for public publication under the author's GitHub account while preserving neutral naming, layered licensing, and public/private boundary separation.
