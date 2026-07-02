# Licensing Matrix

Copyright © 2026 Stephen Hsu (許家誠).  
Contact: chiacheng.hsu@owasp.org

This repository uses layered licensing so that public examples and schemas can be widely reused while core governance tools remain open when redistributed.

## Directory licenses

| Directory / file group | License |
|---|---|
| `tools/**` | GNU General Public License v3.0 or later (`GPL-3.0-or-later`) |
| `offline-editor/core/**` | GNU General Public License v3.0 or later (`GPL-3.0-or-later`) |
| `offline-editor/ui/**` | MIT License (`MIT`) |
| `offline-editor/examples/**` | MIT License (`MIT`) |
| `examples/**` | MIT License (`MIT`) |
| `schemas/**` | MIT License (`MIT`) |
| `policies/**` | MIT License (`MIT`) |
| `tests/**` | MIT License (`MIT`) |
| `docs/**` | Creative Commons Attribution-ShareAlike 4.0 International (`CC-BY-SA-4.0`) |
| root metadata files | All rights reserved unless otherwise stated in the file header |

The full license texts are provided under `LICENSES/`.

## SPDX identifiers

Where practical, source files should include SPDX headers.

For GPL-licensed core files:

```text
SPDX-FileCopyrightText: 2026 Stephen Hsu (許家誠)
SPDX-License-Identifier: GPL-3.0-or-later
```

For MIT-licensed example, schema, policy, UI-template, or test files:

```text
SPDX-FileCopyrightText: 2026 Stephen Hsu (許家誠)
SPDX-License-Identifier: MIT
```

For documentation:

```text
SPDX-FileCopyrightText: 2026 Stephen Hsu (許家誠)
SPDX-License-Identifier: CC-BY-SA-4.0
```

## Patent notice

No patent license is granted by this repository unless explicitly stated in a separate written license. Publication of this repository does not waive any patent rights that may exist.

## Trademark notice

HL7®, FHIR®, and related marks are trademarks of Health Level Seven International. This repository is independent and is not endorsed, certified, sponsored, or approved by HL7.

References to FHIR are made only for conceptual comparison and attribution. This repository must not be described as an official FHIR implementation, FHIR Implementation Guide, FHIR profile, FHIR derivative standard, or “FHIR Lite.”

## Excluded content

Organization-specific content, third-party media, press images, private registries, credentials, account recovery flows, secrets, internal governance logs, and production deployment data are excluded from this repository and are not licensed here.

Unless explicitly included in this repository and covered by a license statement, such excluded materials remain outside the scope of this open reference release.
