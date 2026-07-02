# Offline Editor Reference Components

This directory contains public, neutral Offline Editor reference components.

It does not include production workflows, private registries, organization-specific content, credential tooling, account recovery workflows, or internal governance records.

## Licensing

| Path | License | Meaning |
|---|---|---|
| `core/**` | GPL-3.0-or-later | Core governance logic should remain open when redistributed. |
| `ui/**` | MIT | Standalone UI templates may be reused broadly. |
| `examples/**` | MIT | Neutral examples may be reused broadly. |

## Boundary

The Offline Editor reference is intentionally minimal. It demonstrates how an offline tool can separate:

- stable logical identity;
- content-derived snapshot identity;
- source reference metadata;
- public-safe output projection;
- pre-release validation.

Production-specific operational controls, private registries, organization-specific content, and sensitive recovery workflows are outside the public release scope.
