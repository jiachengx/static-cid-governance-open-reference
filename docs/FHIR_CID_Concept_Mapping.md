---
license: CC-BY-SA-4.0
author: Stephen Hsu (許家誠)
contact: chiacheng.hsu@owasp.org
---

# FHIR / CID Concept Mapping for Non-Medical Static Publishing

This document compares selected FHIR ideas with the Static CID Governance model. It does not claim that the model is a FHIR implementation.

## 1. Useful concepts borrowed from FHIR thinking

| FHIR concept | Useful idea | Static CID Governance adaptation |
|---|---|---|
| Resource logical ID | A resource should have a stable logical identity | `id` identifies the logical object |
| Version identity | A resource can have distinguishable versions | `cid` and `version.digest` identify a content snapshot |
| Version-specific reference | A reference may track a resource or a specific version | `track-latest` and `pinned-version` policies |
| Narrative | Data should remain human-readable | `title`, `summary`, and public HTML remain readable without internal tooling |
| Coding / controlled vocabulary | Categories should avoid uncontrolled wording drift | public taxonomy codes and displays |
| Provenance | A system should be able to explain source and revision lineage | source reference metadata and release-gate logs |

## 2. What is not adopted

The model does not require a FHIR server, clinical resource types, terminology server, patient/encounter semantics, or medical exchange workflow.

## 3. Why the adaptation is useful outside healthcare

FHIR is strong at cross-system exchange and version-aware references. Static CID Governance is targeted at static public sites where public pages, JSON projections, assets, release packages, and private governance records can drift apart.

The fusion is conceptual rather than structural: stable identity, versioned reference, and provenance-style accountability are translated into a simpler static publishing governance workflow.

