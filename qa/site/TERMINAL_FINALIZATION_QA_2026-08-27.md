# Pattern Map v16 terminal-finalization QA

Status: **OWNER-REVIEW CANDIDATE; MANUAL AND OWNER GATES REMAIN OPEN**

Audit date: 2026-08-27

Baseline reviewed:
`e565502317282433a323a83f855ace2274ce13ab`

Accepted source-correction checkpoint:
`874a0a8e09f0bde11532cf873087865addb7d973`

This record consolidates the terminal audit lanes and their integrator
dispositions. It distinguishes source/DOM/fixture evidence from physical
accessibility, human comprehension, empirical results, or production behavior.

## Independent audit lanes

### Human/mentor intent and anti-complexity

Result: **no P0/P1 finding; accepted with no content edit**.

The Home opening, 249-word rendered short version, full essay, Guided path, and
six-family Map preserve the original human problem: weak output can begin with
upstream noticing, retrieval, comparison, context, assumption, and memory
choices. The Discrimination Layer is introduced after its function. Provenance,
research status, protocol language, and The Echo Problem do not displace the
first-screen or first-90-seconds thesis. Peripheral material remains a
candidate rather than truth, and all six original families remain legible.

No late taste rewrite was justified. Owner/mentor warmth, memorability, and the
public friction of the framework name remain owner judgments.

### Live visual and interaction audit

Result: **one accepted correction; no other functional failure**.

The delegated read-only audit used an actual local build and Chromium
DOM/computed geometry at 1440, 1101, 1100, 1024, 821, 768, 601, 600, 480, 390,
and 320 pixels where meaningful. It covered all ten routes, the standalone,
Map focus/reset, More-menu state, all 108 Apply input combinations, simulated
hold/clarify/reset, no-script state, term helpers including the right edge,
print-media proxies, evidence-route/table containment, and all six rendered
PDF pages.

Accepted finding `VIS-TERM-001`: above 1100px, an absolutely positioned term
panel overlapped the bottom of its own 44px trigger by approximately 6.4–7.8
pixels because only horizontal viewport correction existed. The source now
uses the actual trigger/panel rectangles to preserve at least 8px of vertical
clearance while retaining horizontal viewport clamping. A pure geometry module
and deterministic regression replay the first, right-edge, and left-clamp
cases. At 1100px and below, the existing in-flow panel remains unchanged.

Deferred findings:

- Apply radios retain native focus. Computed evidence found the focused radio
  matched `:focus-visible` and showed a visible 1px auto outline inside an
  approximately 44px label. No custom label treatment is added without a
  reproduced physical-keyboard defect.
- The six-column Map at 1101px and the 601-to-600 layout jump remain contained
  and functional. Their density/cadence is owner-taste P2 work.
- The visible 44px term-helper control is retained. A smaller visible control
  or expanded invisible hit area is deferred because hardware-touch,
  accidental-hit, and prose-rhythm tradeoffs remain unverified.

The browser's high-level click/keyboard and screenshot calls timed out. These
results are therefore bounded to local source, synthetic DOM/CDP events,
computed geometry, print-media emulation, and Poppler rendering—not a physical
keyboard, touch, screen-reader, or manual-browser certification.

### Builder/operator and Signal Foundry handoff

Result: **no P0/P1 comprehension or execution blocker; bounded terminology and
portability corrections accepted**.

The Quickstart, full guide, templates, 108-state Apply contract, case material,
and two Signal Foundry handoff files remain actionable without inventing a V14
deep link, Pattern Map classifier, current-schema-valid `CONTEXT_DISPOSITION`,
provider call, or implemented integration. The existing
`OPERATOR_DECISION` + `RATIONALE` pair remains the first seam to test.

Accepted corrections standardize the permission token as `NOT_AUTHORIZED`,
replace bare `STOPPED` with the canonical stopped-state family, and make
cross-computer commands repository-root-relative. Validator regressions reject
the stale vocabulary. Signal Foundry remains the product name and its own
repository remains authoritative.

### QA and portable-package integrity

Result: **baseline suite/reproducibility passed; explicit new package gaps
accepted and corrected**.

The exact baseline passed the complete provider-free suite in a disposable
clone and reproduced the standalone after `npm ci` from the lockfile. The
pre-existing `e565502` portable ZIP remains intact and verifiable, but the new
terminal brief required two additions: a literal, complete `START_HERE.md` and
an internal manifest with sorted per-file paths, byte sizes, and SHA-256s.

The new deterministic builder reads payload bytes from an exact Git commit,
creates a self-contained START_HERE and copyable prompt, records exact
provenance and the superseded prior bundle, writes a JSON manifest and
`SHA256SUMS.txt`, embeds a standard-library verifier, produces a whole-ZIP
sidecar, refuses overwrite, and rejects unsafe paths, symlinks, dependency or
cache payloads, source-machine absolute paths, and private-key markers. Its
five regression tests cover extraction/verification, manifest counts and
hashes, downstream facts, determinism, safety, sidecar integrity, and overwrite
refusal.

### Claude independent exact-checkpoint review

Result: **no P0/P1 finding; optional P2 suggestions dispositioned**.

The authorized read-only Claude Pro review of exact `e565502` found no
undispositioned P0/P1 defect. Its optional custom radio-focus treatment is
deferred because native focus is visibly present in computed evidence. Its
optional smaller term-helper control is deferred, and an overlapping invisible
hit-area treatment is rejected, because the current visible target is stable
and physical touch/accidental-hit evidence is absent. Full detail is preserved
in `qa/site/advisory/CLAUDE_TERMINAL_AUDIT_2026-08-27_e565502.md`.

## Verification boundary

The complete final suite is `qa/run_owner_review_checks.sh`; it includes the
locked owner-intent checksum, immutable archive verification, Echo preservation
and provider-free harnesses, content/framework contracts, site build/check,
site/visual/research audits, portable-bundle regression, owner-review manifest,
reproducible standalone export, and `git diff --check`.

Passing those checks establishes artifact structure, deterministic local
behavior, and package integrity only. It does not establish physical keyboard
or assistive-technology behavior, human comprehension, research validity,
framework effectiveness, or production readiness.

## Remaining honest gates

- owner and mentor comprehension/taste;
- physical end-to-end keyboard traversal;
- supported screen-reader review;
- real 200% browser/OS zoom;
- real forced-colors inspection;
- native browser print preview;
- hardware-touch behavior;
- publication-time link and metadata checks if publication is later authorized.

No main merge, deployment, publication, Release, study, participant/model
experiment, provider selection for research, external dataset acquisition,
preregistration, outreach, or incremental spend occurred in these audits.
