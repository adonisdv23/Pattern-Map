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

## D-018 — Freeze the site content interface without claiming a rendered site

**Date:** 2026-08-19

**Status:** Accepted with revision

The pre-site interface fixes the human-first headline and standfirst, three
principal doors, five secondary routes, six-family public tuple, source
manifests, example classes, progressive-disclosure obligations, Echo/history
placement, claim boundaries, visual policy, output requirements, and external-
action prohibitions. It freezes hierarchy and meaning while leaving layout and
technical implementation to the site lane.

An independent audit found that the first validator could pass several forms
of lockstep drift. The revised validator now compares the immutable owner-
intent checkpoint, a fixed six-family tuple and boundaries, exact source and
action manifests, required examples/levels/outputs, Echo and Signal Foundry
status, glossary coverage, and the bitmap-needs gate. The current visual-needs
record justifies no generated bitmap: code-native treatments and the preserved
historical v13 diagram cover the teaching needs.

This checkpoint authorizes the isolated site task to begin. It does not pass
rendered first-screen, reader comprehension, no-script, keyboard, responsive,
print, PDF, historical-map-display, link-wording, or site-removal gates. Those
remain explicit Phase 4/6 work.

**Implementation:** initial freeze `6f672f2`; audit revision `9079fcb`.

**Advisory report:**
`qa/editorial/advisory/CONTENT_INTERFACE_FREEZE_AUDIT_2026-08-19_6f672f2.md`.

**Governing requirement:** site dependency rule; A01–A17 as scoped.

## D-019 — Integrate the local site with an explicit renderer correction and manual residuals

**Date:** 2026-08-19

**Status:** Accepted with revision for final advisory review

The site lane produced a dependency-free nine-route local review surface with
the three frozen principal doors, five secondary routes, all six families,
progressive technical disclosure, ordinary through advanced application paths,
three required teaching patterns, bounded Signal Foundry and Echo routes, a
historical/current topology distinction, a standalone HTML export, and a
six-page PDF companion. No deployment, hosting API, publication, provider,
study, external dataset, or spend occurred.

Primary integration review found one defect before any canonical remote push:
the small Markdown renderer allowed emphasis parsing to alter `_blank` inside
generated anchor attributes, and its link regex truncated a DOI containing
parentheses. The renderer now token-protects completed inline markup, preserves
balanced parentheses in destinations, and tests both safe external attributes
and the exact parenthesized URL across the Sources route and standalone export.
All site, content-interface, applied, and research-boundary validators pass
after the correction.

The visual-needs record found no justified generated-bitmap need. The site uses
code-native teaching treatments and a byte-identical 1,961,204-byte recovered
v13 diagram. That active historical copy is an explicit binary-policy
exception, hash-verified, and labeled `Historical v13 origin — not the current
v16 topology.` No generated image was created.

Responsive screenshots and rendered PDF pages are implementation QA, not
reader or research evidence. Static focus order, focus handoff, accessible
names, no-script meaning, reduced motion, forced colors, reflow, and print CSS
pass. Physical keyboard traversal and a human print-preview pass remain honest
owner-review residuals because the automation surface could not establish
them reliably.

**Implementation:** site task `a3cd7c7`; renderer correction `932366a`.

**Evidence:** `qa/site/SITE_QA_REPORT.md`,
`qa/visual/VISUAL_QA_REPORT.md`, `qa/visual/VISUAL_NEEDS.md`, and
`assets/IMAGE_USE_LEDGER.md`.

**Governing requirement:** three-door site contract; progressive disclosure;
historical integrity; A01–A17 as scoped; no-deploy/no-publish boundary.

## D-020 — Accept final rendered corrections as artifact evidence, not human or effectiveness results

**Date:** 2026-08-19

**Status:** Accepted with revision for owner review

The final advisory wave found bounded, correctable defects in the rendered
owner-review surface: underscore-bearing operational identifiers could be
mutated by emphasis parsing; some local source links fell back to inaccurate or
missing destinations; the standalone export repeated level-one headings and
IDs; narrow headers hid the principal route links; Map cards led with builder
vocabulary; several contrast pairs were weak; five promised glossary entries
were incomplete; and the PDF's untagged status was not explicit enough.

The integrated source checkpoint `2a54b24ec01707bb2a73032ab3f662cd995669ae`
repairs those implementation defects without changing the locked owner intent
or the canonical six-family framework. Exact follow-up reviews report one
standalone `h1`, 282 unique IDs, complete local fragments, intact route/stop/
learning tokens, direct Echo anchoring, plain-language Map bridges, populated
glossary entries, visible narrow-width principal routes, stronger contrast,
and an explicitly visual-only PDF with semantic standalone HTML as the
accessibility route. A final browser evidence refresh replaced the two stale
mobile/Map screenshots; it changed review evidence only, not canonical copy.

The post-site applied reviews pass A07, A08, and A09 as artifact gates. That
means the repository exposes concrete builder paths, specifies observable agent
records and states, and keeps Signal Foundry bounded as an illustration. It is
not evidence that a live agent complied, a product improved, a reader
understood the idea, or the framework is effective.

The cold-reader and site reviews are model proxies and implementation audits.
A01 and A04 still require owner/mentor judgment; the A05 durations remain
editorial estimates; and A13 remains partial pending physical keyboard,
supported screen-reader, and browser print-preview checks. The package must
therefore be called an owner-review candidate, not a fully accepted,
accessible, published, deployed, or empirically validated release.

**Evidence:**
`qa/applied/advisory/APPLIED_FINAL_REGRESSION_CHECK_2026-08-19_2a54b24.md`;
`qa/editorial/advisory/COLD_READER_POST_REVISION_VERIFICATION_2026-08-19_2a54b24.md`;
`qa/site/advisory/SITE_POST_REVISION_VERIFICATION_2026-08-19_2a54b24.md`;
`docs/ADVISORY_REVIEW_DISPOSITIONS.md`; and
`qa/FINAL_ACCEPTANCE_MATRIX_V16.md`.

**Governing requirement:** A01/A04–A13/A15–A17; review-and-disposition
protocol; no-results and no-publication boundaries.

## D-021 — Open a draft PR as the bounded owner-review release

**Date:** 2026-08-19

**Status:** Accepted for owner review; owner acceptance remains open

After the 114-file package manifest and full local verification suite passed,
the foundation branch was pushed at owner-review package checkpoint
`63e63c123874a7be7ccc9aff6f2bce102a971ae3`. GitHub repository metadata
confirmed `adonisdv23/Pattern-Map`, default branch `main`, working fetch/push
connectivity, and no pre-existing open PR for the foundation branch.

Draft pull request [#1](https://github.com/adonisdv23/Pattern-Map/pull/1) now
targets `main` from `codex/pattern-map-v16-foundation`. Its body states the
two-project separation, artifact inventory, integrity results, manual owner
gates, and exact external-action boundary. The PR remains a review surface; it
does not authorize merge, deployment, public-site replacement, publication,
Release creation, research execution, provider selection/call, spend, data or
participant acquisition, preregistration, outreach, or representation of
unrun work as a result.

The authorized owner-review handoff phase is complete as a repository
artifact. Binding owner/mentor judgment and physical keyboard, supported
screen-reader, and browser print-preview checks remain open, so v16 is not
recorded as fully accepted under every gate.

**Governing requirement:** owner-review release boundary; A01/A04/A05/A13/A15–A17.

## D-022 — Strengthen live-browser evidence without converting automation into manual acceptance

**Date:** 2026-08-19

**Status:** Accepted with manual residuals unchanged

A current-head in-app-browser pass reopened all nine local routes, exercised
the More focus handoff and Escape return, checked Map focus/reset and live-
region behavior, inspected visible focus styles, toggled progressive detail,
and checked route-level headings, landmarks, active links, overflow, and
console errors. Those live behaviors passed at the available 1280×720
viewport.

Synthetic Tab traversal and native default keyboard activation still did not
advance reliably in the automation surface. The browser security layer also
declined the supported developer capability requested for responsive viewport,
print-media, and accessibility-tree inspection. The denial was not bypassed
and no alternate browser-control surface was used.

The evidence therefore improves the live implementation record but does not
close physical keyboard, supported screen-reader, or browser print-preview
acceptance. No canonical site correction was indicated, and A13 remains
partial. Human comprehension, voice, and observed timing remain outside this
browser check.

**Evidence:**
`qa/site/LIVE_BROWSER_BOUNDARY_CHECK_2026-08-19_79a2392.md`.

**Governing requirement:** A02/A06/A13/A15/A17; evidence-scope and browser-
permission boundaries.

## D-023 — Require an authored interactive site before owner review

**Date:** 2026-08-19

**Status:** Accepted for owner review with manual residuals

The owner clarified that the v16 site should feel comparable in ambition to the
preserved prior site, not like a text dump or a PDF-centered handoff. A direct
comparison of the pre-polish v16 build with the v14/v15.2 references found that
the existing build was coherent and accessible in structure but still read as
a polished documentation surface. It lacked persistent publication
orientation, placed the relationship view too late, and made Apply primarily
descriptive.

The bounded site-polish branch restores the useful design qualities without
restoring the provenance-first thesis drift. The routed site now provides:

- a persistent desktop chapter rail and a normal-flow narrow-screen route
  guide;
- three visually distinct principal doors;
- a current F1–F6 relationship view at the start of Map, including the F4
  baseline dependency, F6 learning loop, human-authority boundary, focus state,
  and nearby text equivalent;
- an editorial Read route with cumulative and full reading layers;
- a local, provider-free Apply studio that makes ordinary/lightweight/moderate/
  advanced choice, route, stop, learning, and human disposition visible; and
- full-width teaching narratives for peripheral signal, motion/absence, and
  common-origin recurrence while keeping Echo subordinate and unrun.

The first implementation checkpoint was
`5a37aacccd26d407acf65cea9b33393899514851`. Primary and bounded advisory review
accepted the substantive visual result but identified evidence and standalone
residuals. Checkpoint `a319794f5cf2d395c34e5af4935c9299f12dfd5c`
removes nested standalone route frames, labels the concatenated export `All
routes`, adds regression assertions, and preserves visible F1, advanced/HOLD,
and standalone states. Evidence checkpoint
`85dff94e7b64266a2054d1857b0c012ac9c97736` labels the older black-region mobile
PNG as stale rather than silently overwriting it.

The expanded visual evidence is accepted under the existing binary policy:
every new capture/render remains below 1 MB, canonical text/code remains
diffable, and the files document baseline, revision, final viewport, PDF, and
interaction states. This does not reopen generated-bitmap work. Code-native
visuals remain the better responsive and semantic teaching medium, and the
image-use ledger still records zero generated candidates.

Claude Code/Cowork was attempted as an optional independent reviewer because
the owner requested it. The installed client returned `401` because its
existing OAuth token had been revoked. Credentials were not inspected,
repaired, requested, or replaced; no provider/API call or spend was used; and
the package makes no claim that Claude reviewed the work. The bounded visual
review and primary browser/source verification continued without treating that
optional lane as a blocker.

The site passes artifact, structural, responsive, no-script, interaction-state,
standalone, and visual-review gates. A01/A04/A05 remain owner/mentor judgments.
A13 remains partial pending physical-keyboard traversal, a supported
screen-reader pass, real 200% zoom, and browser print preview. The PDF is still
an untagged secondary visual companion; the routed site and semantic standalone
HTML are primary.

**Evidence:** `qa/site/SITE_POLISH_QA.md`,
`qa/site/advisory/SITE_VISUAL_EXPERIENCE_POST_POLISH_2026-08-19_a319794.md`,
`qa/visual/VISUAL_EXPERIENCE_REVISION_REPORT.md`, `qa/visual/README.md`, and
`docs/ADVISORY_REVIEW_DISPOSITIONS.md`.

**Governing requirement:** owner visual expectation; three-door site contract;
A02/A06–A08/A10–A13/A15–A17; no-deploy/no-publish boundary.

## D-024 — Correct the Pro round-1 blockers without changing the locked thesis

**Date:** 2026-08-20

**Status:** Accepted with owner/assistive-technology residuals unchanged

At the owner's request, an outside ChatGPT Pro project reviewed exact commit
`cc5547def98aeec819eabc68bbf850548e97d4c6` and draft PR #1 against the locked
owner intent, two-project firebreak, acceptance gates, source tree, generated
site, standalone export, playbook, and historical design references. The full
report was read before disposition and is preserved in
`qa/site/advisory/CHATGPT_PRO_INDEPENDENT_REVIEW_2026-08-20_cc5547d.md`.

Two source-deterministic defects were accepted as P0. The old Apply studio
converted planning choices into event-like completion, stop, learning, and
human-decision states, and restricted permission did not dominate every route
shortcut. The old Map combined a 3-column medium layout with a later
821-pixel desktop coordinate override, making collisions and detached lines
possible from 821 through 1100 pixels.

The correction keeps the owner's thesis, headline, six families, three doors,
human-authority boundary, proportional levels, warm visual system, and
Echo/Signal Foundry boundaries intact. It changes the implementation as
follows:

The coherent implementation checkpoint is
`5eb860e8d6918813622a7725eb0d854f6bef6ca2`; its current QA record is
`qa/site/PRO_ROUND_1_CORRECTION_QA_2026-08-20_5eb860e.md`.

- Apply now returns planning recommendations only. Observed execution, stop,
  outcome, learning, and human-decision fields remain explicitly unrun or
  unobserved; optional later-state controls are labeled local simulations and
  never mutate those fields. A pure 54-combination test enforces permission
  precedence and prevents event-token fabrication.
- The Map is flow-native and line-free at every width. Six family questions,
  optional shared records, and four limited relationship bands replace the
  fragile fixed topology. Exact 821-pixel and 1024-pixel browser inspection
  shows the intended 3-column/2-column reflow without horizontal overflow.
- The 60–90-second entry is now 250 raw words, uses a concrete product-release
  case before the family questions, and delays the internal framework name
  until its function is clear. This remains an editorial estimate, not an
  observed reading-time or comprehension result.
- A tenth, optional Guided route provides one authored 8–12-minute path from
  the human problem through the questions, relationships, smallest useful
  application, examples, and boundaries. It is generated from the same
  canonical components and does not replace Read / Map / Apply or fork the
  manuscript.
- Difficult primary-path terms now have inline plain meaning plus optional
  click/touch/keyboard explainers with code-native microvisuals, boundaries,
  and glossary links. No essential meaning is hover-only and no generated
  bitmap was justified.
- Apply is progressively enhanced: without JavaScript, dead controls are
  hidden and the complete static planning guide remains readable. The
  Quickstart and full guide now begin with Stage 0 so ordinary supplied-material
  transformations do not inherit evidence bureaucracy.

The advisory suggestion to soften “AI slop often begins before the model
writes a word” was rejected under D-013/PAOB-03 because the phrase is the
owner-approved editorial center and remains explicitly conceptual rather than
measured. Lower-priority URL focus persistence and broad appendix terminology
rewrites were deferred unless an exact-commit follow-up shows a material need.

Current automated and in-app-browser evidence covers the ten-route build,
54-state planning matrix, no-script contract, 390-pixel Home/Map/Apply reflow,
exact 821-pixel and 1024-pixel Map behavior, term interaction, permission
precedence, and absence of console errors. Physical keyboard traversal,
supported screen-reader review, real 200% zoom, browser print preview, and
owner/mentor judgment remain binding manual residuals. The Pro report is a
model advisory, not owner acceptance or empirical evidence.

**Governing requirement:** owner visual expectation; authority order;
A01–A08/A10–A13/A15–A17; no-deploy/no-publish/no-study boundary.

## D-025 — Close the bounded Pro Round 2 findings and stop at owner/manual gates

**Date:** 2026-08-22

**Status:** Accepted with final draft-PR readback and manual residuals

ChatGPT Pro Round 2 reviewed exact commit
`4d2505e7f3d325fe7b8ef5e2e5c3a634a11aa9fe`. Its full output is preserved in
`qa/site/advisory/CHATGPT_PRO_INDEPENDENT_REVIEW_ROUND_2_2026-08-22_4d2505e.md`
and remains advisory under the authority order. The review found no remaining
P0 and confirmed that the Round 1 Apply event-state and Map collision defects
were resolved. It identified five bounded P1 corrections.

Implementation checkpoint
`c88926034cd75773dcc42d3842983c879dda5b58` closes the source findings without
reopening the thesis:

- Apply now asks the independent Stage 0 evidence-selection question before
  consequence, uncertainty, budget, and permission. The complete 108-case
  contract prevents Stage 0 `yes` from resolving to ordinary, keeps Stage 0
  `no` free of evidence bureaucracy, preserves permission/human-gate
  precedence, and never fabricates an event.
- Home previews Apply as a recommendation and planned boundary, not a receipt,
  stop event, or recorded human disposition.
- contextual term helpers name their concepts for assistive technology, hide
  inert optional controls without JavaScript, and become flow-native across
  601–1100 pixels;
- the mobile route brief remains one column and discrete route controls meet
  the 44-pixel source/computed-layout contract;
- one Map status remains live, no-script progress is hidden, Round 1’s
  budget/repeatability wording is corrected transparently in new evidence,
  and standalone packaging language is narrowed to direct-open within the
  repository.

The old overridden Map CSS is left for a separately bounded maintenance pass:
it does not govern current markup and is not an owner-review blocker. Visual
density, mono labels, rail feel, the public name, voice, and memorability are
owner-taste decisions. Physical keyboard, supported screen reader, real zoom,
forced colors, print preview, and hardware touch remain manual A13 gates.
External-link and public-metadata checks remain publication-time work only.

The draft PR body must be refreshed and read back after the final evidence
push so that it describes the actual head while remaining draft, open,
unmerged, and bounded. No self-referential repository file is treated as proof
of that later GitHub state.

**Evidence:**
`qa/site/PRO_ROUND_2_CORRECTION_QA_2026-08-22_c889260.md`, the full advisory
record, executable contracts, and current in-app-browser layout observations.

**Governing requirement:** authority order; proportionality; three-door and
six-family locks; A02/A06–A08/A11/A13–A17; no-merge/no-deploy/no-publish/no-
study/no-spend boundary.

## D-026 — Adopt the Claude research package selectively and keep F0/F1/F2 first

**Date:** 2026-08-23

**Status:** Accepted with revision; no study or provider call authorized

The owner supplied `PATTERN_MAP_CLAUDE_SESSION_2026-08-19.zip` for adversarial
review. Its SHA-256 is
`b544b734324699a93abbb8cf0bcef3d61cc590ff7b603fc167a46b8f8539a253`.
The handoff, transcript, and Claude self-red-team were read in the requested
order, but remained advisory under the repository authority order.

EP v1.1 adopts Amendment A1 only with the NEWS-COPY narrowing. NEWS-COPY may
support same-original/origin-cluster instrument validation, never claim truth,
support, `FC_cons`, VOR, independence, or a full endpoint arm; nonduplicates
remain unknown. Newswire remains aggregate recurrence context. Pochampally's
graded-correlation lesson is accepted for prospective real-world measurement,
while the controlled F0/F1/F2 labels stay deliberately simple and stipulated.

The proposal to replace the controlled paper with a measurement paper is
rejected as an exclusive reframe. Existing measurements make the claimed
empty field indefensible. The controlled cue-use question remains the
first-paper candidate; a typed, graded, provenance-aware measurement
instrument is a prospective second-paper candidate after targeted prior-art,
rights/version, labelled-threshold, and separate owner gates.

Claude's reported `n=300` planning values (`0.873` at effect `0.10`; `0.327`
at `0.05`) were reproduced as conditional simulations. The active exact-
McNemar surface makes discordance explicit: under one declared cell,
`-0.08` is below the approximate 80% resolution at `n=300`, while `n=400`
reaches about `0.82`. These are design calculations, not observed power.

Claude's claimed exact real-BPE parity fix was independently refuted: its own
suite produced three failures and six passes. The replacement bounded solver
passes all 300 checked F1/F2 prompt pairs from Claude's frozen seed-1 renderer
under `tiktoken 0.14.0` / `cl100k_base`, with exact source, renderer, prompt,
tokenizer, and receipt hashes. This is an offline implementation check, not a
selected-model/chat-template receipt or research result.

An independent Luna Max audit then found two defects in the replacement
planning helper: its documented invalidity sweep was not exposed by the
surface/CLI, and its naive exact-binomial tail could become negative or
overflow. Both were accepted and corrected with explicit equal/unequal
invalidity pairs, a stable bounded lower-tail calculation, and regression
tests through 2,000 discordant pairs. The active EP v1.1 suite now has 12
tests; the optional real-tokenizer test passes when the pinned dependency is
present.

The installed Claude Code client was also tried as an optional second-model
path, but its existing OAuth state returned `401`/revoked token. Credentials
were not inspected or repaired, no paid API was called, and no successful
Claude Code review is claimed. The supplied Claude package was instead
audited directly and independently.

**Evidence:** `qa/research/ECHO_V1_1_DESIGN_CHECKPOINT_QA_2026-08-23.md`,
`research/the-echo-problem/v1_1/**`, integrated checkpoint `9fa2355`.

**Governing requirement:** D-001/D-008; A01/A10/A11/A14–A17; authority order;
unknown-stays-unknown; no-results/no-provider/no-study boundary.

## D-027 — Finish site hygiene without reducing the publication to text or PDF

**Date:** 2026-08-23

**Status:** Accepted for artifact scope; owner and physical checks remain open

The owner required an authored interactive site comparable in ambition to the
prior site, not a crude text page or a PDF substitute. The current ten-route
site, continuous Guided path, line-free Map, contextual term explainers with
code-native microvisuals, and planning-only Apply studio remain canonical.

The final hygiene pass removes stale unreachable Map CSS, gives current JPEG
QA images truthful `.jpg` extensions, adds an image-signature verifier, and
makes the standalone export begin with the locked human problem as its only
`h1`. The complete Home hero now precedes package metadata. Immutable archive
image/type mismatches remain unchanged and explicitly exempt under archive
policy. No bitmap generation was justified, so the image-use ledger remains at
zero generated candidates.

The routed site is the primary review experience; the direct-open all-routes
HTML is the semantic portable companion; the six-page untagged PDF is a
secondary visual review artifact. None is deployed or published. Physical
keyboard, supported screen reader, real 200% zoom, forced colors, browser
print preview, hardware touch, and owner/mentor taste remain manual gates.

**Evidence:** commits `de3535f`, `28b936b`, and `5e5bfef`;
`qa/site/SITE_HYGIENE_QA_2026-08-23_d4b7b9e.md`;
`qa/visual/verify_image_formats.py`; site build/check contracts.

**Governing requirement:** owner visual expectation; first-screen human
problem; progressive disclosure; A02/A03/A06–A08/A12/A13/A15–A17.

## D-028 — Give Signal Foundry two exact handoff artifacts and reuse its smallest seam

**Date:** 2026-08-23

**Status:** Accepted with downstream implementation still unauthorized

The owner's garbled downstream request is resolved by two canonical artifacts:
`handoff/signal-foundry/PATTERN_MAP_V16_CANONICAL_HANDOFF.md` and
`handoff/signal-foundry/SIGNAL_FOUNDRY_INTEGRATION_BRIEF.md`. They must travel
together. If either is absent from the receiving checkout, the next operator
must attach/copy the exact file or stop and request it rather than infer it.

Signal Foundry `main` and `origin/main` were independently verified at
`f9bf3775ca3d5b52ea5083cea52306c025727e23`; its pre-existing modified
`.gitignore` and untracked `AGENTS.md`/`CLAUDE.md` were preserved. The local
read-only audit branch `codex/pattern-map-signal-foundry-transfer-audit` at
`4a6ed78` is recoverable but not integrated or pushed.

The smallest valid design seam is the existing closed-schema
`OPERATOR_DECISION` plus `RATIONALE` pair, proven first with an offline fixture
showing a real before/after decision delta. The proposed
`CONTEXT_DISPOSITION` object is conceptual, not valid against the current
schema, and cannot become a new event unless a later authorized fixture shows
the existing pair is insufficient. `VISUAL_NOT_REVIEWED` is likewise proposed
local vocabulary, not an existing accepted enum.

No verified V14 deep link or Pattern Map classifier exists. Neither may be
invented. The handoff does not mutate Signal Foundry, deploy it, rename it
“Sigma,” run its models, or claim integration/validation.

**Evidence:** commits `c73c470` and `59a11ca`; both handoff files; independent
Signal Foundry audit summarized in the owner-review packet.

**Governing requirement:** smallest useful seam; closed-schema truth;
A07–A11/A15–A17; no external mutation or invented implementation.

## D-029 — Repair standalone structure, visual geometry, and export containment

**Date:** 2026-08-23

**Status:** Accepted with revision; owner/manual gates remain open

The owner's 83,215,636-byte, 11-page attachment is a jsPDF 2.5.1 full-page-
style export with 3572 × 14400 pt pages, not the repository's 18,199-byte,
six-page US-letter ReportLab companion. Its Sources/Research collision,
collapsed History pages, and unreadable evidence tables are accepted as real.
The routed site and dedicated PDF did not reproduce the narrow columns, but a
later standalone-DOM red team did: an extra closing `</div>` in Boundaries let
later sections escape the main content column. A broad redesign is rejected;
the generator defect is fixed at its source.

Standalone extraction now uses explicit page-content markers rather than a
greedy closing-tag regex. The build contract checks balanced main markup and
requires all ten standalone route sections to remain inside `.page-content`.
Post-repair Chromium measurements at 1440, 821, and 390 px show Sources,
Research, and History in the intended content column with no document overflow.

The source also makes browser print/export more defensive: standalone routes
start on deliberate pages; Sources, Research, History, their notes, and page
content occupy the full print frame; and wide evidence tables receive an
explicit fixed full-width print contract. Transfer guidance names the routed
site and standalone HTML as primary and the composed six-page PDF as secondary,
and warns that custom full-page/jsPDF captures are not equivalent artifacts.

One genuine current-source visual defect is accepted directly. The common-
origin example's nine absolutely positioned rotated lines are no longer
painted. A flow-native bridge now reads from nine observations through traced
known paths to one known shared origin, while `independence: UNKNOWN` remains
explicit. Complex term microvisuals stack below 480 px, and desktop term panels
receive a calculated bounded shift so a right-edge trigger cannot be clipped.
No bitmap generation or decorative network graph is justified.

Real Chromium DOM checks scrolled the long routes at desktop and mobile widths,
exercised the revised recurrence and term controls, and emulated print media.
They found no horizontal document overflow; the three evidence routes occupy
the full print frame and representative tables use the declared print layout.
These are implementation checks, not reader or accessibility results.

The requested authenticated Claude web thread could not be attached because
the in-app Browser runtime rejected its trusted service path. The cloud session
ID/title also did not map to a local Claude Code session, and a new read-only
Opus/max Plan review returned a revoked-OAuth `401`. Credentials were not
inspected or repaired, and no successful Claude review is claimed.

**Evidence:** `qa/site/OWNER_VISUAL_EXPORT_CLOSEOUT_2026-08-23.md`, current
site build/check contracts, exact rendered PDF inspection, and bounded
Chromium DOM/print observations.

**Governing requirement:** owner visual expectation; progressive disclosure;
flow-native teaching objects; A02/A03/A06/A08/A12/A13/A15–A17; no-merge/no-
deploy/no-publish/no-study/no-spend boundary.

## D-030 — Close terminal defects with geometry evidence and a portable exact-commit packet

**Date:** 2026-08-27

**Status:** Accepted with revision; owner/manual gates remain open

Independent intent, operator, package, live visual/interaction, and bounded
Claude reviews of exact baseline
`e565502317282433a323a83f855ace2274ce13ab` found no undispositioned P0 and one
actionable visual defect: above 1100px, an absolute term panel could overlap
the lower 6.4–7.8px of its own 44px trigger. The smallest correction preserves
the existing horizontal viewport clamp and adds trigger-relative translation
for at least 8px of vertical clearance. A pure geometry contract replays the
measured first, right-edge, and left-clamp cases. The flow-native panel at
1100px and below is unchanged.

Custom radio/label focus styling is deferred because current computed evidence
shows a visible native `:focus-visible` outline and no physical keyboard defect
was reproduced. Shrinking the visible 44px term-helper control or adding an
overlapping invisible hit target is likewise deferred/rejected pending hardware
touch and owner-taste evidence. The 1101/1100 and 601/600 Map transitions are
contained P2 cadence questions, not functional failures.

The operator record now uses canonical `NOT_AUTHORIZED` and `STOPPED_*` state
language, with regressions that reject stale tokens. The two Signal Foundry
handoffs use receiving-repository-relative instructions rather than executable
source-machine paths. Signal Foundry's existing `OPERATOR_DECISION` plus
`RATIONALE` seam remains the first seam to test;
`CONTEXT_DISPOSITION` remains conceptual and not current-schema-valid.

The new portable builder reads an exact Git commit, creates one complete
`START_HERE.md`, an exact copyable prompt, sorted per-file path/byte/SHA-256
manifest, portable hash list, standard-library verifier, and whole-ZIP sidecar.
It is deterministic, refuses overwrite, excludes dependencies/caches/unsafe
paths/source-machine absolute paths, and records the prior `e565502` packet as
superseded without deleting it. This packet grants no downstream app mutation.

The accepted source checkpoint is
`874a0a8e09f0bde11532cf873087865addb7d973`. The evidence commit that records
this decision may advance the branch head without changing that source
checkpoint.

**Evidence:** `qa/site/TERMINAL_FINALIZATION_QA_2026-08-27.md`;
`qa/site/advisory/CLAUDE_TERMINAL_AUDIT_2026-08-27_e565502.md`;
`qa/interaction/term-popover-geometry-contract.spec.mjs`;
`qa/handoff/test_portable_bundle.py`; full owner-review runner.

**Governing requirement:** locked owner intent; progressive disclosure;
cross-computer reproducibility; A01–A17; no-merge/no-deploy/no-publish/no-
study/no-spend boundary.

## D-031 — Finalize the reusable contracts without expanding the framework

**Date:** 2026-08-28

**Status:** Accepted with revision; owner/manual gates remain open

Claude Ultracode and two independent Luna Max lanes reviewed exact baseline
`d5b3431a02d5ffc4d084baa278d7a18fd98a71ad`. Their reports are advisory under
the repository authority order. Findings were reproduced before acceptance;
the broad essay, six-family thesis, three-door site, and permanent Echo split
were not reopened merely because an outside review was detailed.

The accepted post-Ultracode source checkpoint is
`c86e53764f6e33b62097f0424125b5922441ce58`. It makes five bounded classes of
correction:

1. F2 now records source role, relevant track-record evidence, claim-scoped
   authority, support, origin/recurrence, relevance, and permission separately.
   Track record is scoped and may remain `UNKNOWN`; it is not a reputation
   score.
2. F6 cannot claim `LEARNING_REVIEWED` without a review, an observed outcome or
   explicit missing-outcome reason, and human disposition. No observed result
   fixture was invented.
3. Stage 0 has a genuinely ordinary supplied-material receipt with no layered
   evidence records; the former “ordinary” fixture is correctly labeled
   lightweight. `OUTCOME_REVIEW` remains an artifact rather than a route, and
   selected influence requires authorized material plus an actual selected
   item.
4. The Draft 2020-12 schema locks the exact ordered F1–F6 ID/slug/name tuple,
   while site presentation adapters retain editorial freedom behind an exact
   coverage contract.
5. The cross-computer packet distinguishes required tracked inputs from
   optional source-machine evidence. Local audit `4a6ed78` and untracked
   Signal Foundry guidance may be absent in a fresh clone; their absence is
   recorded and nonblocking, while required current contracts still fail
   closed. Package verification scans all payload types for high-signal
   private-key/source-path markers and documents selected-subset links.

A generic project-adoption brief and conformance dictionary are deferred until
a second real downstream project demonstrates repeated transfer friction.
Adding them now would duplicate existing artifacts and weaken the owner's
anti-bureaucracy boundary. A universal source reputation score, new route,
second ledger, and populated outcome “result” fixture are rejected.

The 2026-08-27 `d5b3431` portable packet remains preserved. The builder is
configured to name it as the prior packet only when a new exact-commit packet
is actually sealed; this decision does not preclaim that later file.

**Evidence:** `qa/handoff/POST_ULTRACODE_FINALIZATION_QA_2026-08-28.md`;
`qa/applied/validate_framework.py`; `qa/handoff/test_portable_bundle.py`;
site build/check contracts; accepted source checkpoint `c86e537`.

**Governing requirement:** D-001/D-007/D-008/D-028/D-030; locked owner intent;
A01–A17; source-role/authority/permission separation; ordinary-work escape
hatch; exact cross-computer reproducibility; no-results and prohibited-action
boundaries.

## D-032 — Correct only reproduced late visual defects before sealing

**Date:** 2026-08-28

**Status:** Accepted; owner/manual gates remain open

The final in-app Browser pass preserved the ten-route design and found two
specific composition defects rather than evidence for a broad redesign. First,
standalone route composition demotes each route heading by one level; four dark
callouts styled `h2` but not the resulting `h3`, producing low-contrast dark
headings on navy or purple only in the all-routes export. The inverse-heading
contract now covers both levels. Second, the Home Apply preview placed its
caption absolutely over the second planning row. The caption now occupies a
third normal-flow grid row.

Both changes preserve the human-first opening, three principal doors, all six
families, progressive disclosure, the planning-only Apply boundary, and the
separate unrun Echo track. Live checks found equal full-width containment for
standalone Sources/Research/History, intended light-on-dark computed colors for
all four callouts, no preview text overlap at 1280 or 390 pixels, and no page-
level horizontal overflow. These observations do not certify physical keyboard,
screen-reader, real zoom, forced-colors, native print, hardware-touch, or owner
taste.

**Evidence:** `qa/handoff/POST_ULTRACODE_FINALIZATION_QA_2026-08-28.md`;
`site/check.mjs`; current generated routes and standalone export.

**Governing requirement:** owner visual expectation; A01–A06/A12/A13/A17;
flow-native, comprehensible teaching surfaces; no-deploy/no-publish boundary.

## D-033 — Advance v16 through public and transfer hardening, not thesis expansion

**Date:** 2026-08-30

**Status:** Accepted for local feature-branch implementation; external gates
remain closed

The owner authorized a further high-reasoning audit, adversarial red-team, and
implementation cycle intended to make Pattern Map more useful for future
projects, mentor review, and a possible later public/X release. Three
independent read-only lanes reviewed the exact clean checkpoint
`4d2e11ceb26b36fd7428dc7de963c135802a8dea`: human/public experience,
operator/agent executability and transfer, and current research/claims. A
second convergence loop required the lanes to challenge one another. The
primary integrator reproduced the material cross-artifact findings before
acceptance.

The owner-review baseline remains intact. The next phase is a bounded public
and transfer hardening cycle, not v17 and not a new thesis. It accepts:

1. Stage 0 must exist inside the actual copied agent prompt and must terminate
   ordinary supplied-material work before layered records.
2. Ordinary work receives only a minimal scope/assumption/boundary record; it
   does not manufacture evidence, route, stop, outcome, learning, or six-family
   ceremony.
3. Applied validators must require typed permission states and resolvable
   baseline, comparison, disconfirmation, influence, and memory references
   before those records can claim the corresponding structural state.
4. One existing neutral case must demonstrate sparse family use, and F4 memory
   receives a fail-closed append-only correction/supersession fixture.
5. A public presentation mode may remove review chrome and improve reading
   order only as a view adapter over the same canonical sources and route IDs.
6. One deterministic code-native teaching reveal may replace an existing
   static example. It may not call a model, score sources, create an observed
   event, or imply comprehension/effectiveness.
7. The optional source/research route must be updated for directly relevant
   2025–2026 work and preserve the contribution ceiling: authored
   human-governed design/governance synthesis and testable agenda, not novel
   mechanism, exhaustive taxonomy, or validated method.
8. A generic adoption artifact remains deferred until Signal Foundry and a
   materially different second real project expose the same transfer friction.
   Even then it would be a candidate abstraction, not proof of generality.

The canonical essay, 90-second version, mentor note, six families, permanent
Echo split, human-authority boundary, and no-results boundary are not reopened
by these technical findings. Publication identity, physical accessibility,
owner/mentor judgment, publication-time metadata/link checks, deployment,
publication, study execution, and merge remain separate gates.

**Evidence:** `docs/PUBLIC_AND_TRANSFER_HARDENING_PLAN_V16.md`; exact baseline
and locked-intent readback; full owner-review runner; live ten-route desktop and
mobile inspection; read-only human/public, operator/agent, and research/claims
audits and their adversarial convergence.

**Governing requirement:** locked owner intent; D-001/D-007/D-008/D-031;
A01–A17; proportionality and ordinary-work escape; observable rather than
inspirational agent behavior; research may constrain claims but may not
redefine the thesis; no-merge/no-deploy/no-publish/no-study/no-spend boundary.

## D-034 — Integrate public presentation and downstream contract hardening without creating v17

**Date:** 2026-08-30

**Status:** Accepted with revision; local owner/public candidate only

Three isolated high-reasoning lanes began from exact owner-review baseline
`4d2e11ceb26b36fd7428dc7de963c135802a8dea`. They owned applied contracts,
public presentation, and current research/claims boundaries respectively, then
red-teamed one another before integration. Their recommendations remained
advisory under the repository authority order. The locked owner-intent
checksum, human essay, six-family identity, permanent Echo split, and ordinary
work escape were not reopened.

The applied lane makes Stage 0 terminal inside the copyable prompt and gives
ordinary supplied-material work exactly four fields: supplied scope,
assumptions, unchecked boundaries, and output. Layered work now uses typed
`AUTHORIZED`, `UNKNOWN`, `NOT_AUTHORIZED`, and `REVOKED` permission; blocked
global permission leaves no downstream evidence or influence; comparison and
disconfirmation either resolve to substantive records or carry bounded typed
exceptions; motion requires two distinct authorized observations at two real
UTC instants under one alignment key; and memory use is limited to one
accepted, `CURRENT`, `AUTHORIZED` linear lineage whose preserved root is bound
to a frozen fixture anchor. These are structural/procedural contracts, not
proof of source truth, legal authorization, runtime immutability, answer
quality, or effectiveness.

The site remains one content system with a `review | public` presentation
adapter. Public mode keeps all ten routes and canonical source hashes while
removing owner-package chrome from the ordinary reading flow. The actual
90-second prose appears in the first Read viewport. One fixed four-stage
teaching reveal replaces rather than accumulates on an opening example; it has
a static equivalent and no network, model, score, automated action, or
observed-result claim. Release output requires both an explicit release flag
and parsed absolute-HTTPS metadata with a usable host; ordinary public previews
remain `noindex,nofollow`. Author, canonical URL, social image, publication
links, and final release action remain unset and separately gated.

The optional source route now includes targeted, non-exhaustive current work
through 2026 and constrains component-level novelty. The project remains a
human-governed design/governance synthesis and testable agenda, not a validated
new technical mechanism. The narrow-wedge memo separates generation studies,
where answer accuracy may be eligible, from fixed-answer interface studies,
where correction, acceptance, and burden are eligible but answer accuracy is
not. It also separates observation, capture/process, access, permission, and
currency. No first paper, provider, model, corpus, sample, study, or spend was
selected.

The cross-computer Signal Foundry packet includes the ordinary and memory
templates, frozen memory anchor, and distinct permission fixtures, but excludes
the publication adapter, public standalone, visual captures, lane QA, and
narrow-study memo because those are owner-repository review artifacts rather
than Signal Foundry implementation inputs. Every retained relative Markdown
link outside the selected packet is machine-classified as archive,
owner-review-only, or outside-selected-packet; a new unclassified target fails
the build. Signal Foundry's own tracked contracts remain authoritative, and
the packet grants no mutation authority.

**Evidence:** implementation checkpoint `cbc89db`; focused applied, research,
site, 108-state Apply, portable-bundle, and owner-intent checks; public and
transfer hardening plan; lane QA and advisory dispositions. Final
exact-commit/clean-clone/Claude/remote/package evidence is recorded only after
those later gates actually complete.

**Governing requirement:** D-001/D-007/D-008/D-031/D-033; locked owner intent;
A01–A17; progressive disclosure; anti-bureaucracy; shared-source publication;
exact cross-computer provenance; no-results/no-merge/no-deploy/no-publish/no-
study/no-spend boundary.
