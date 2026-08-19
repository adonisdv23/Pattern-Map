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

## D-006 — Lock the v16 owner intent before downstream drafting

**Date:** 2026-08-19

**Status:** Accepted — owner-fixed

`docs/OWNER_INTENT_V16.md` is the governing intent contract. Agents may improve
expression but may not alter the underlying proposition, audiences, six-family
scope, two-project separation, or action boundaries without a new explicit owner
instruction. Proposed changes remain non-canonical and owner-decision-required.

**Integrity lock:** `docs/OWNER_INTENT_V16.sha256` records the checkpoint's
byte-level SHA-256. Downstream QA must verify it before integration; wording
changes intentionally require a new owner-approved checkpoint rather than an
unexplained hash refresh.

## D-007 — Restore the historical six families as the public map

**Date:** 2026-08-19

**Status:** Accepted — owner-fixed

V16 publicly organizes the framework around peripheral signal, source weighing,
velocity/motion, absence + memory, structured patterns, and the learning loop.
V14/v15 components such as authorization, provenance, claim graphs, routing,
context packets, human disposition, and versioned memory may implement or
qualify those families but may not replace them as the thesis-facing map.

**Reason:** the v14/v15 decomposition improved rigor but contributed to drift
away from the original reader problem and ambition.

## D-008 — Enforce artifact firebreaks and Echo independence

**Date:** 2026-08-19

**Status:** Accepted — owner-fixed

The human essay, builder framework, agent companion, broader research agenda,
The Echo Problem, site, and historical archive have separate canonical paths,
readers, and evidentiary roles. The removal test governs integration: v16 must
remain coherent without the Echo example, and Echo must stand independently as
an unrun origin-accounting project.

## D-009 — Accept the verified v15.2 accession and EP v0.1 successor

**Date:** 2026-08-19

**Status:** Accepted

The immutable accession contains all 239 external-manifest payload files and
48,717,432 payload bytes, plus the unchanged external manifest and sidecar. The
complete verifier also confirms the untouched 41,436,496-byte source ZIP, its
SHA-256, all 240 ZIP members, CRCs, and the embedded-manifest identity. The ZIP
itself remains outside Git under D-004.

EP v0.1 is accepted as a separate, unrun successor with 82 byte-verified
preserved source files covering the v15.2 manuscript, site, protocol, harness,
fixture contract, and prior art. Its QA and status records are preservation and
implementation evidence only, not research results.

**Source task:** `90c64ad`; integrated as `96f8e32`.

**Governing requirement:** two-project separation; A10/A14/A15.

## D-010 — Preserve runnable historical paths in the curated Echo copy

**Date:** 2026-08-19

**Status:** Accepted with revision

The first EP v0.1 commit grouped byte-exact harness and fixture copies under
role-oriented `harness/` and `fixtures/` paths. An independent replay failed
before test collection because the preserved test imports
`tools.origin_accounting` and the preserved loader resolves
`research/origin_accounting/config/frozen_config.json`.

Only the curated copies were moved to the historical repository-relative
`tools/`, `tests/`, and `research/origin_accounting/` paths. No preserved file
byte and no immutable accession path changed. The source-copy verifier still
passes for all 82 files, and all 15 deterministic local tests now run from the
documented preserved root. This is a reproducibility correction, not a study
or result.

**Governing requirement:** canonical reproducibility; archive immutability;
A10/A14/A15.
