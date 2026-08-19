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

## D-011 — Tighten the manuscript without weakening its boundaries

**Date:** 2026-08-19

**Status:** Accepted with revision

The first Wave 1 mentor-reader/anti-slop audit passed the broad thesis and Echo
subordination but found cumulative committee tone in term defense, numbered
family treatment, noun inventories, implementation detail, repeated caveats,
research language, and the long cover note.

The integrated revision keeps all six families, all three required examples,
the technical/social term boundary, the light/moderate/advanced spectrum,
permission, uncertainty, stopping, human judgment, non-novelty, no-results,
and unfavorable-outcome boundaries. It adds one owner-supplied coffee-
conversation anchor, simplifies prose, removes the Echo table, trims the cover
note from 398 to 247 raw words, and lets the human invitation close the essay.

The resulting essay remains 3,289 raw / 3,149 prose words (an estimated
13.7–14.3 minutes), and the short version remains an estimated 74–77 seconds.
No reader timing or comprehension result is claimed.

**Advisory report:**
`qa/editorial/advisory/MENTOR_READER_ANTI_SLOP_2026-08-19_505d007.md`.

**Implementation:** `51177d9`.

**Governing requirement:** owner-intent voice contract; A01–A06, A10, A11,
A15–A17.

## D-012 — Integrate the applied framework as an inspectable, proportionate layer

**Date:** 2026-08-19

**Status:** Accepted for advisory review

The first applied-framework lane is integrated with all six historical
families as the stable public map. Permission envelopes, evidence spines,
typed relationships, routing, context packets, receipts, and human disposition
are supporting mechanisms; they do not replace the six families or impose one
technical stack.

The companion defines observable acquisition, comparison, disconfirmation,
uncertainty, cost, stop, escalation, influence, and learning procedures. It
also includes an ordinary path and explicit when-not-to-use guidance so the
framework can remain proportionate. Common-origin recurrence remains one F5
mechanism and example. Signal Foundry remains an invented, read-only fixture
and not implementation evidence or validation.

The focused validator, JSON parse checks, source-parent/scope audit, and
owner-intent hash pass. These are structural and procedural checks only. They
do not establish agent compliance or effectiveness; independent applied and
v13-continuity audits remain required before the content interface freezes.

**Source task:** `fccfceb`; integrated as `223d190`.

**Integration QA:** `qa/applied/PLAYBOOK_INTEGRATION_QA.md`.

**Governing requirement:** owner-intent operational contract; A03, A07–A09,
A11, A15–A17.

## D-013 — Keep prior art optional, direct, and claim-constraining

**Date:** 2026-08-19

**Status:** Accepted with revision

The Wave 1 prior-art/overclaim audit passed the core manuscript's novelty,
causality, effectiveness, provenance, recurrence, case, Echo, and no-results
boundaries. Its source-route corrections are accepted: the optional route now
links to the already integrated EP v0.1 status, the archived targeted
prior-art map, its classified reference list, and a small set of primary or
official entry points.

The route is explicitly targeted rather than exhaustive, stays outside the
human essay, and records that links require re-verification before any public
release. The owner-approved “AI slop often begins” framing remains unchanged
because it is a conceptual editorial proposition, not a measured prevalence
claim. Future site wording may not present it as an empirical technical fact.

The audit's A07–A09 scope limitation is also accepted: those gates must be
re-audited against the integrated framework, cases, and eventual site rather
than inferred from the manuscript-only `ea8a6e2` snapshot.

**Advisory report:**
`qa/research/advisory/PRIOR_ART_AND_OVERCLAIM_BOUNDARY_2026-08-19_ea8a6e2.md`.

**Governing requirement:** targeted prior-art restraint; two-project
separation; A07–A11, A15, A16.

## D-014 — Use version indexes instead of duplicate archive copies

**Date:** 2026-08-19

**Status:** Accepted

The version-specific `archive/v13/`, `v14/`, `v15/`, `v15.1/`, and `v15.2/`
directories are curated indexes into the already preserved immutable transfers,
not second physical copies. This preserves canonical navigation and explicit
version status while avoiding duplicate checkout weight and any false claim
that copying identical bytes improves archival integrity.

`archive/CHECKPOINT_INDEX.json` records size and SHA-256 for 26 selected
anchors across the five versions. `archive/verify_checkpoint_index.py` checks
those paths and the exact-ZIP external hash record. Complete integrity remains
with the v14 checksum ledger and v15.2 accession manifest/verifier. Source
commit identifiers from earlier repositories remain lineage anchors and are
not represented as objects available in Pattern-Map's object database.

The indexes preserve material limitations: v13's original standalone HTML was
not recovered; v15's separate Markdown source is not exposed by the current
accession index; and the exact v15.2 ZIP container remains outside ordinary Git
under D-004. No archive byte was rewritten.

**Governing requirement:** canonical reproducibility, historical immutability,
Git hygiene, and A14.

## D-015 — Keep historical links byte-exact and provide current recovery routes

**Date:** 2026-08-19

**Status:** Accepted with documented limitation

The 82-file EP v0.1 curated source set is intentionally smaller than the
complete 239-file v15.2 accession. Eight link occurrences in three preserved
Markdown files refer to five historical repository-relative targets that are
not all present at the same relative locations in the focused curated view.
Editing those links would violate the byte-exact preservation boundary.

`research/the-echo-problem/PRESERVED_V15_2_INDEX.md` now maps every unique
historical target to either its curated copy or its complete-accession copy.
Active-document link QA must exclude the immutable preserved subtree and verify
the current routes in that index instead. The project does not claim that the
historical relative links resolve from the curated placement.

**Governing requirement:** preserve historical v15.2 exactly; canonical
recoverability; A10/A14.

## D-016 — Accept the applied framework after bounded interoperability revisions

**Date:** 2026-08-19

**Status:** Accepted with revision

The first applied checkpoint already supplied the six-family specification,
implementation spectrum, operator playbook, agent companion, templates, Signal
Foundry translation, and two domain-neutral fixtures. Advisory review found
four bounded execution gaps: the Quickstart did not close learning, route/stop
labels conflicted, preflight statuses were not inspectable, and the Signal
Foundry fixture lacked a concrete cost/stop/resume envelope.

The integrated revisions preserve the ordinary path and add no mandatory
architecture. Route, stop, and learning states are now separate canonical
vocabularies; the relationship map and Signal Foundry procedure map friendly
packet descriptions to canonical route values. The focused validator and an
independent post-revision review pass with no remaining APP-02 residue.

This establishes builder and agent artifact completeness for the pre-site
scope. It does not establish live-agent compliance, Signal Foundry product
behavior, reader comprehension, or framework effectiveness. A07–A09 remain
scheduled for a final rendered-site/cross-link review.

**Implementation:** `223d190`, `cd8a756`, and `9ab9b5d`.

**Advisory reports:**
`qa/applied/advisory/AGENT_PLAYBOOK_AND_SIGNAL_FOUNDRY_AUDIT_2026-08-19_223d190.md`;
`qa/applied/advisory/APPLIED_POST_REVISION_VERIFICATION_2026-08-19_cd8a756.md`;
`qa/editorial/advisory/V13_CONTINUITY_AND_INTENT_FIDELITY_2026-08-19_223d190.md`.

**Governing requirement:** A03, A07–A09, A11, A15–A17.

## D-017 — Contain the broader research agenda as an unrun future track

**Date:** 2026-08-19

**Status:** Accepted

The broader v16 research agenda now treats The Echo Problem as independent
Research Track 01 and defines DL-PLAYBOOK-01 as a separate future flagship
candidate. The candidate asks whether the operational playbook changes
usefulness, supported novelty, evidence diversity, missing-perspective
detection, and human correction effort relative to ordinary prompting under a
matched total resource envelope.

The protocol counts playbook instructions, context/output tokens, tool calls,
retries, elapsed time, human review, and any later-authorized cost. It retains
null, harmful, shortcut-driven, fragile, non-transfer, stopped, invalid, and
indeterminate outcomes. It selects no provider, model, dataset, participant,
sample size, registry, or spend and authorizes no execution.

Local validators establish containment and required fields only. They are not
research evidence, a preregistration, or a completed study.

**Implementation:** `1e376c0`.

**Governing requirement:** research containment; A10/A11/A15/A16.
