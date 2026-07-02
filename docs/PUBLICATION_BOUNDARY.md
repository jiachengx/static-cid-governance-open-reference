---
license: CC-BY-SA-4.0
author: Stephen Hsu (許家誠)
contact: chiacheng.hsu@owasp.org
---

# Publication Boundary

This package is intended as a public open reference implementation.

## Public/open layer

The following are safe for public release in this package:

- neutral model documentation;
- synthetic example static site;
- public-safe JSON examples;
- generic CID governance schema and policy templates;
- defensive reference tools without organization-specific configuration;
- high-level Mermaid diagrams.

## Private/non-included layer

The following should remain outside this public repository unless separately reviewed:

- production static-site output from a specific organization;
- internal offline editor credentials and account logic;
- private registries and production source indexes;
- press assets, profile images, and third-party media;
- organization-specific content;
- deployment secrets or cloud provider configuration;
- internal account recovery tooling;
- internal release logs and private audit materials.

## Rationale

Public release should establish authorship, reusable technical language, and a practical reference implementation without disclosing private operational materials or assigning organization-specific content to an open-source license.
