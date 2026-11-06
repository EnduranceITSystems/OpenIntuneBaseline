# IntuneManagement import roots

Use `Default` as the first Bulk Import root. It contains 13 Settings Catalog policies and one compliance policy. Use `Optional` only to prepare selected alternate or optional objects. Clear Import Assignments, choose the correct object types, and start with Skip if object exists.

The two `%OrganizationId%` values in optional OneDrive KFM are intentional supported tokens, replaced by the reviewed importer with the connected tenant ID. Source settings remain in `NativeImport/`, `Compliance/` and `CustomProfiles/`; regenerate these copies with `scripts/prepare_intunemanagement.py` after editing them.

Read `docs/INTUNEMANAGEMENT.md` and `docs/ASSIGNMENTS.md` in the package before deployment. These import copies are the same policy artifacts in another format, not additional policies to assign alongside the originals.
