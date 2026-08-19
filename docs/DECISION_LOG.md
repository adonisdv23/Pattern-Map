# Decision log

Canonical decisions are append-only. Later changes receive a new entry and do
not silently rewrite history.

## D-001 — Permanent two-project separation

**Date:** 2026-08-19
**Status:** Accepted — owner-fixed

Pattern Recognition / The Discrimination Layer v16 is the principal broad work.
The Echo Problem / ECHO-01 is a separate successor project derived from the
exact v15.2 checkpoint. V15.2 remains historically named and unchanged. The
Echo Problem begins at EP v0.1. Origin accounting may illustrate v16 but may
not define it.

**Governing requirement:** approved v16 handoff, sections 2 and 4.

## D-002 — Authority order

**Date:** 2026-08-19
**Status:** Accepted — owner-fixed

Owner handoff and locked intent outrank archives; v13 controls historical
intent; v14/v15 inform rigor and implementation; v15.2 governs Echo; reviews
are advisory only.

**Affected files:** `AGENTS.md`, `docs/SOURCE_AUTHORITY_AND_LINEAGE.md`.

## D-003 — Preserve v14 as one immutable transfer

**Date:** 2026-08-19
**Status:** Accepted

The complete v14 transfer moved with Git history into
`archive/transfers/v14-complete-2026-08-18/`. It is not unpacked into the active
root. Selective active successors must cite the archive and may not rewrite it.

**Evidence:** complete transfer SHA-256 ledger passed before the move.

## D-004 — Accession the v15.2 payload as verified extracted source

**Date:** 2026-08-19
**Status:** Accepted for implementation by the Echo task; supersedes the
uncommitted chunk proposal

Preserve every manifest-listed payload byte and its provenance by extracting
directly from the verified owner ZIP into an immutable accession, copying the
original sidecar and manifest unchanged, and automatically verifying every
file's byte count and SHA-256. Keep the exact 41,436,496-byte ZIP untouched at
its verified local source path until an exact owner instruction authorizes Git
LFS or a GitHub Release with known budget controls.

**Evidence:** 102 of 239 payload files and 30,298,057 of 48,717,432 payload bytes
(62.19%) exactly match files already preserved in the v14 transfer. Git can
deduplicate those blobs. The remaining new or changed raw payload is 18,419,375
bytes before Git compression/delta reuse, versus a fully opaque 41,436,496-byte
ZIP object.

**Alternatives:**

- **One exact ordinary-Git blob — Rejected.** It is below GitHub's 50 MiB warning
  threshold but adds the full opaque payload to every clone and cannot reuse
  existing v14 blobs.
- **Git LFS — Deferred.** It would keep the Git object database small, but LFS is
  not installed and is metered after the plan allowance. Existing API scope did
  not expose account usage or budget settings, so zero hidden cost cannot be
  guaranteed without broader owner-authorized setup.
- **Canonical extracted source — Accepted.** It is self-contained for every
  material package file, diffable where possible, deduplicable, independently
  verifiable, and has no new external dependency.
- **Deterministic chunks — Rejected.** They would make the exact ZIP
  reconstructable but would not reduce total Git history or checkout weight and
  would add ordering, reconstruction, and verification burden.

**Boundary:** Extracted payload cannot reproduce original ZIP container metadata
by itself. The exact original ZIP remains separately preserved and hash-anchored;
a later re-zipped copy must never be called byte-identical unless it matches the
recorded whole-file SHA-256.

## D-005 — External-action boundary

**Date:** 2026-08-19
**Status:** Accepted — owner-fixed

Scoped branches, worktrees, commits, pushes, and draft PRs are authorized. No
merge to `main`, deploy, publication, Release, study, paid provider, spending,
dataset acquisition, preregistration, outreach, or result implication is
authorized.
