# Phase 3 content-interface freeze audit

**Reviewed commit:** `6f672f26bc5e537cdcb23ebc44fa3a619ed659c5` (`6f672f2`)

**Reviewed artifacts:**

- `docs/CONTENT_INTERFACE_FREEZE_V16.md`
- `docs/CONTENT_INTERFACE_V16.json`
- `qa/editorial/validate_content_interface.py`
- `site/README.md`

**Verdict:** **CONDITIONAL — the declared content contract is coherent and
passes its current structural validator, but this commit is not evidence of a
rendered-site freeze or a full Phase 3 acceptance pass.** The local site is not
implemented at this commit (`site/README.md` is the only path under `site/`),
so first-screen rendering, semantic heading order, three-door discoverability,
no-script/print behavior, keyboard/accessibility behavior, cross-link wording,
Echo removal, and reader comprehension remain open. In addition, the validator
has material false-negative paths that could allow content-interface drift to
pass.

This is a structural/editorial audit, not a reader study, model review,
effectiveness assessment, or empirical result. No web browsing, provider/model
call, external action, or study was performed.

## Checks performed

All checks below were run against the clean `6f672f2` checkout or against the
immutable commit with `git show`/`git ls-tree` where the check concerned commit
contents.

- `(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)` — **PASS**.
- `python3 qa/editorial/validate_content_interface.py` — **PASS**:
  owner-intent hash, three doors/five secondary routes, six-family alignment,
  human-problem first-screen fields, essay/short-version word bands, late Echo
  essay placement, and declared external-action flags.
- Committed JSON parse — **PASS** (`3` principal doors, `5` secondary routes,
  `6` families).
- `python3 -B archive/verify_checkpoint_index.py` — **PASS** (`5` versions,
  `26` selected anchors, v15.2 ZIP hash anchor).
- `git diff --check 6f672f2^ 6f672f2` for the four assigned files — **PASS**.
- Commit inventory — `site/README.md` is the only committed path below
  `site/`; `qa/visual/VISUAL_NEEDS.md` is not present (only
  `qa/visual/.gitkeep` is present).

The positive checks establish structural consistency at this checkpoint. They
do not establish that the interface is rendered, readable, accessible, or
faithful after site implementation.

## Gate-oriented assessment

| Gate | Assessment at `6f672f2` | Reason |
| --- | --- | --- |
| A01 | **Partial / not reader-evidenced** | The approved hero and short version are broad and human-first, and the short version names the six families and boundaries. There is no rendered first stop or cold-reader evidence in this commit. |
| A02 | **Open** | The freeze specifies a human-first screen, but no site DOM or rendered capture exists. |
| A03 | **Structural partial** | JSON and essay contain six-family names/order/questions/headings. Meaning, v13 continuity in the rendered map, and current-vs-historical visual distinction are not tested. |
| A04 | **Not assessed** | Voice is a reader-facing judgment; this commit contains no new cold-reader or mentor-reader observation. |
| A05 | **Structural estimate pass** | Validator reports `3289` raw essay words and `288` raw short-version words. These are estimates, not measured reading times. |
| A06 | **Open** | Progressive-disclosure requirements are declared, but no no-script, closed-popover, print, or standalone export exists to inspect. |
| A07 | **Source-map partial** | Builder and agent sources are named and present, but wildcard/index omissions and route coverage are not enforced. |
| A08 | **Source-map partial** | Agent-playbook sources are named and present; site exposure and inspectability of procedures are not rendered or tested. |
| A09 | **Declared boundary pass; site open** | The Signal Foundry source is explicitly illustration-only/not validation, but no site cross-link wording is present to inspect. |
| A10 | **Declared boundary pass; removal open** | Echo is subordinate in the contract and its canonical README/status say unrun/no results. The validator does not run the site removal test or require cross-link labels. |
| A11 | **Partial** | Boundary language is present in the contract and source artifacts, but the validator does not enforce the claims list, status text, or rendered claims. |
| A14 | **Archive evidence pass; site-label open** | Owner/archive integrity checks pass. The validator checks a label value in JSON, not the historical map asset/use or visible rendered label. |
| A15 | **Declared current flags pass; schema incomplete** | Current action flags are false, but the key set is not locked and omits owner-level prohibited categories such as preregistration and outreach/contact. No deployment/publication occurred. |
| A16 | **Current owner hash pass; validator gap** | The locked hash passes now, but the validator compares only with the mutable current owner file, not the checked-in `.sha256` checkpoint. |
| A17 | **No current unauthorized edit observed; validator gap** | The owner-intent file and checkpoint agree at this commit. A future synchronized edit of the owner file and JSON hash could pass the content validator. |

## Controlled findings

### CIF-01 — visual-needs gate is named but absent and unenforced

**Verdict:** **Open structural enforcement gap; no current bitmap-use violation
observed.**

**Severity:** P2 — material before any bitmap candidate or visual-surface
integration.

**Exact evidence:**

- `docs/CONTENT_INTERFACE_FREEZE_V16.md:157-169` says bitmap generation may
  begin only after `qa/visual/VISUAL_NEEDS.md` records a material need and that
  each candidate must enter the image ledger.
- `docs/CONTENT_INTERFACE_V16.json:195-200` sets
  `bitmap_requires_documented_need` to `true` and names
  `qa/visual/VISUAL_NEEDS.md` as `visual_needs_path`.
- At `6f672f2`, `git ls-tree -r --name-only 6f672f2 -- qa/visual` returns only
  `qa/visual/.gitkeep`; `qa/visual/VISUAL_NEEDS.md` does not exist.
- `qa/editorial/validate_content_interface.py:62-73` adds the popover source,
  current-topology source, and image-ledger path to `source_paths`, but never
  adds `contract["visual_policy"]["visual_needs_path"]`. The validator
  therefore passes while its named prerequisite is missing.

**Governing gate:** A12 directly; also affects A13/A15 if visual assets are
introduced. The freeze's own visual policy and `assets/IMAGE_USE_LEDGER.md`
are the applicable boundary.

**Bounded recommendation:** Before the site task introduces a bitmap, add a
scoped visual-needs record and make the validator require the declared path
when `bitmap_requires_documented_need` is true. If no bitmap is intended,
retain the image ledger's blocked/none state and add a validator assertion that
no generated candidate is referenced without a recorded need and disposition.
Do not treat this missing file alone as evidence that a bitmap was used.

### CIF-02 — machine-readable source map is narrower than the frozen prose map

**Verdict:** **Material source-mapping ambiguity; likely implementation drift
unless the JSON is deliberately treated as an index-only map.**

**Severity:** P2.

**Exact evidence:**

- The Markdown Apply route names `framework/templates/**` as a canonical source
  (`docs/CONTENT_INTERFACE_FREEZE_V16.md:97-107`), while the JSON names only
  `framework/templates/README.md` (`docs/CONTENT_INTERFACE_V16.json:43-57`).
  The commit contains seven template files below that directory, not just the
  README.
- The Markdown Examples route names `cases/**`
  (`docs/CONTENT_INTERFACE_FREEZE_V16.md:117-123`), while JSON names only
  `cases/README.md` and one agent example
  (`docs/CONTENT_INTERFACE_V16.json:59-67`). The commit contains the Signal
  Foundry and two domain-neutral case directories.
- JSON History names `archive/README.md` as its archive source
  (`docs/CONTENT_INTERFACE_V16.json:96-102`), while the v13-specific index and
  hash-anchored historical map route are in `archive/v13/README.md:1-19`.
  The frozen contract requires continuity and a historical-map label at
  `docs/CONTENT_INTERFACE_FREEZE_V16.md:157-165`, but the machine-readable
  route does not explicitly name that v13 index or map path.
- `validate_content_interface.py:62-73` checks each source string as one
  literal filesystem path. It neither expands `**` nor follows README/index
  links to confirm the full mapped set.

**Governing gates:** A03, A07, A08, A10, A14; also the artifact firebreak and
builder/agent source-mapping requirements in `docs/ARTIFACT_BOUNDARIES.md` and
`docs/CONTENT_INTERFACE_FREEZE_V16.md:97-123`.

**Bounded recommendation:** Decide and document whether JSON is an index-only
manifest or a complete source manifest. If it is complete, expand the
template/case/history entries to explicit paths (including the v13 index/map)
and make the validator resolve them. If README indexes are intentional, state
that explicitly and validate that each index links to every required child and
that the historical index carries the v13 label/hash boundary. Do not infer
that a source path exists means its contents were exposed by the site.

### CIF-03 — human-first/three-door requirements are not rendered or claim-status tested

**Verdict:** **Contract-level ordering pass; rendered A01/A02 evidence remains
open, and the validator can pass a materially drifted first screen.**

**Severity:** P1 — release-blocking for a site freeze, not a defect in the
approved headline itself.

**Exact evidence:**

- The frozen first-screen requirement and desktop/narrow-screen three-door
  requirement are explicit at
  `docs/CONTENT_INTERFACE_FREEZE_V16.md:20-44`. JSON records the headline,
  standfirst, claim status, and `must_precede` list at
  `docs/CONTENT_INTERFACE_V16.json:6-17`, with the three doors at
  `docs/CONTENT_INTERFACE_V16.json:19-57`.
- `site/README.md:3-10` describes the intended local owner-review surface, but
  `git ls-tree -r --name-only 6f672f2 -- site` contains no HTML, component,
  stylesheet, export, or route to inspect.
- The validator checks door IDs/order/labels at
  `qa/editorial/validate_content_interface.py:36-49`, and only phrase snippets
  plus four prohibited words in the contract's own headline/standfirst at
  `:75-83`. It does not inspect a rendered DOM, the `must_precede` array, the
  `claim_status` value, semantic heading order, or whether the three doors are
  actually visible in the first composition.

**Governing gates:** A01, A02, A11, A13; exact three-door requirement in
`docs/CONTENT_INTERFACE_FREEZE_V16.md:41-49`.

**Bounded recommendation:** Keep the current contract-level door check, but do
not call A01/A02 passed until a local site exists and has a rendered first-screen
capture plus semantic inspection. Add a static/DOM assertion for the exact
headline/standfirst, human-first order, conceptual (not measured) claim status,
and all three labels. A cold-reader or comprehension result must remain a
separate, authorized evidence item; DOM assertions are structural QA only.

### CIF-04 — six-family semantics and v13 continuity can drift in lockstep

**Verdict:** **Current six-family tuple is structurally aligned, but the
validator does not protect the full semantic lock or v13 continuity.**

**Severity:** P2.

**Exact evidence:**

- JSON currently carries six families and reader questions at
  `docs/CONTENT_INTERFACE_V16.json:105-141`; the essay contains all six ordered
  headings, which the validator checks at
  `qa/editorial/validate_content_interface.py:110-122`.
- The validator constructs `expected_families` from the mutable current
  `framework/SIX_FAMILIES.json` and projects only `id`, `slug`, `name`, and
  `reader_question` (`qa/editorial/validate_content_interface.py:51-60`). It
  does not assert the owner-locked literal tuple, family boundaries, purposes,
  mechanisms, or invariants. If the source JSON and interface JSON drift
  together, this check still passes.
- The essay check confirms heading strings and order, not the body meaning,
  six-family continuity from v13, or the current-map/historical-map distinction.
  The v13 label check at `qa/editorial/validate_content_interface.py:89-92`
  checks only a string value in JSON, not a map asset or rendered label.
- The current framework source does contain meaningful boundaries and
  invariants (for example `framework/SIX_FAMILIES.json:14-27` and `:130-140`),
  but those fields are not part of the interface comparison.

**Governing gates:** A03, A14, A16, A17; v13 continuity and current-topology
firebreaks in `docs/SOURCE_AUTHORITY_AND_LINEAGE.md` and
`docs/CONTENT_INTERFACE_FREEZE_V16.md:157-165`.

**Bounded recommendation:** Add a small immutable expected map (or explicit
  owner/thesis fixture) covering the six exact IDs, names, questions, and
  essential boundaries; compare it to both JSON and the canonical source. Add
  a structural check that the v13 index/map is reachable only through a
  historical route and that the current relationship map is separately named.
  Leave semantic reader effectiveness to rendered and reader review rather
  than pretending these checks measure it.

### CIF-05 — Echo, Signal Foundry, and no-results boundaries are declarations, not enforced site checks

**Verdict:** **Canonical source boundaries are presently sound; site placement,
cross-link wording, and removal independence are unverified and can drift while
the validator passes.**

**Severity:** P1.

**Exact evidence:**

- The freeze requires the common-origin example to follow the broad thesis and
  complete map, requires every Signal Foundry link to say illustration/not
  validation, requires every Echo link to say separate/unrun/no-results, and
  requires principal routes to survive Echo removal
  (`docs/CONTENT_INTERFACE_FREEZE_V16.md:141-155`).
- JSON declares the required example classes at `:143-146`, Echo placement and
  label at `:178-182`, and claim boundaries including Signal Foundry and
  unrun/no-results research at `:184-193`.
- The validator checks only `echo.principal_door == false` and the removal-test
  boolean (`qa/editorial/validate_content_interface.py:85-88`), plus one exact
  Echo heading after the essay family headings (`:123-125`). It does not check
  `echo.placement`, `echo.required_label`, the claims array, route/link copy,
  Signal Foundry wording, canonical Echo status, or an actual removal test.
- The canonical sources are appropriately bounded now: Echo README says
  `unrun; no results; not published` and says it is not v16's opening or
  validation (`research/the-echo-problem/README.md:1-5`, `:33-49`); Signal
  Foundry is explicitly `ILLUSTRATION_ONLY / READ_ONLY / NOT_VALIDATION` and
  says its fixture is not an observed runtime result
  (`cases/signal-foundry/README.md:1-15`, `:115-118`, `:183-190`).

**Governing gates:** A01, A09, A10, A11, A15; D-001/D-008 two-project and Echo
firebreaks.

**Bounded recommendation:** Add static checks for the required Echo label and
  status phrases, the Signal Foundry illustration boundary, all three required
  teaching patterns, and the late route position. Once the site exists, run a
  real removal fixture: remove/hide Echo content and confirm Read/Explore/Apply
  still render coherently. Keep this as a structural independence test, not a
  reader-comprehension or research-effectiveness claim.

### CIF-06 — owner-intent validator checks the mutable file, not the immutable checkpoint

**Verdict:** **Current hash is correct, but the validator is insufficient to
  enforce A16/A17 across later drift.**

**Severity:** P1.

**Exact evidence:**

- The committed checkpoint contains the expected digest in
  `docs/OWNER_INTENT_V16.sha256:1`; the independent checksum command passed at
  this audit.
- `docs/CONTENT_INTERFACE_V16.json:4-5` stores the freeze basis and owner hash.
- `qa/editorial/validate_content_interface.py:30-34` computes SHA-256 from the
  current `docs/OWNER_INTENT_V16.md` and compares it only with the JSON field.
  It never reads or verifies `docs/OWNER_INTENT_V16.sha256`, nor does it assert
  the locked digest as an independent expected value.
- Consequently, an unauthorized edit to the owner-intent file accompanied by
  an edited JSON hash would make this validator pass even while the checked-in
  owner checkpoint fails. This is a static false-negative path, not an action
  performed during this audit.

**Governing gates:** A16 and A17; `AGENTS.md` owner-intent checkpoint rule and
`docs/OWNER_INTENT_V16.sha256`.

**Bounded recommendation:** Make the validator invoke or replicate the
  checkpoint comparison against `OWNER_INTENT_V16.sha256` and fail if the
  expected digest/key is missing or changed. Do not refresh the checkpoint in
  response to validator failures; an intentional owner change still requires
  the explicit owner instruction and decision-log process.

### CIF-07 — external-action boundary schema is incomplete and vacuous under key removal

**Verdict:** **All currently declared JSON action values are false, but the
  machine boundary does not cover the full owner prohibition and the validator
  does not require the key set.**

**Severity:** P1.

**Exact evidence:**

- JSON declares false values for `merge_main`, `deploy`, `publish`,
  `github_release`, `study`, `provider_call`, `dataset_acquisition`,
  `participant_activity`, and `spend` at
  `docs/CONTENT_INTERFACE_V16.json:207-216`.
- Owner intent also prohibits preregistration, outreach/contact, and related
  external/research actions (`docs/OWNER_INTENT_V16.md:208-215`), but the JSON
  action object has no `preregister`, `outreach`, `contact`, or equivalent
  explicit keys.
- `qa/editorial/validate_content_interface.py:100-101` loops over whatever
  keys happen to exist and requires each value to be false; an empty or
  truncated object would therefore pass. It does not validate the claims list
  or site text. `site/README.md:7-10` covers no deployment/publication but is
  not a complete action-boundary manifest.

**Governing gates:** A15, A16, A17; owner external-action boundary and the
  freeze's claim/action boundary at `docs/CONTENT_INTERFACE_FREEZE_V16.md:190-207`.

**Bounded recommendation:** Define one required, versioned false-key set that
  covers merge, deploy, publish, release, empirical/model/provider study calls,
  preregistration, dataset acquisition, participant/outreach/contact activity,
  and spend. Require exact key-set equality and false values. Keep the site
  copy human-readable and local-owner-review-only; this check must not be
  treated as proof that no external action occurred outside the repository.

### CIF-08 — progressive disclosure is specified but not evidenced or validated

**Verdict:** **Good contract requirement; implementation gate remains open and
  the current validator can pass without any no-script/print behavior.**

**Severity:** P1 for site-freeze sign-off; not a claim that the contract itself
is wrong.

**Exact evidence:**

- The freeze requires the essential idea to survive JavaScript-off, closed
  popovers, and print, with visible human problem, definition, six family
  names/questions, human boundary, and implementation levels
  (`docs/CONTENT_INTERFACE_FREEZE_V16.md:125-139`).
- JSON declares the same requirements and eight glossary terms at
  `docs/CONTENT_INTERFACE_V16.json:154-172`.
- At this commit there is no site implementation or standalone export to
  inspect (`site/README.md` is the only site file).
- The validator checks only the glossary path and the boolean that closed
  controls may not hide qualifications (`qa/editorial/validate_content_interface.py:62-73`,
  `:94-97`). It does not confirm that glossary terms exist, that visible copy
  carries their qualifications, or that no-script/print routes retain the core
  meaning.

**Governing gates:** A01, A02, A06, A13.

**Bounded recommendation:** Keep A06/A13 open until a local implementation is
  available. Add a no-script/print fixture or export inspection that checks for
  the required visible content and glossary boundaries, then record keyboard,
  responsive, print, and PDF observations separately. Do not use the frozen
  JSON declaration as evidence of reader comprehension or accessibility.

### CIF-09 — required examples, implementation levels, and output obligations are not executable coverage

**Verdict:** **Current canonical sources appear to contain the required content,
but the validator can pass after material route/content omissions.**

**Severity:** P2.

**Exact evidence:**

- JSON declares three required teaching patterns at
  `docs/CONTENT_INTERFACE_V16.json:143-146`, four visible implementation
  levels at `:148-153`, and required local/standalone/PDF/QA outputs at
  `:201-205`.
- The frozen prose additionally requires Examples to expose Signal Foundry and
  two neutral cases (`docs/CONTENT_INTERFACE_FREEZE_V16.md:117-123`) and Apply
  to keep ordinary, lightweight, moderate, and advanced routes visible
  (`:92-111`).
- The validator never reads `required_examples`, `implementation_levels`, or
  `required_outputs`. Its manuscript content check only requires six exact
  family headings and one late Echo heading
  (`qa/editorial/validate_content_interface.py:110-125`).
- Thus a site or canonical content revision could omit the specialist example,
  velocity/absence example, Signal Foundry boundary, neutral cases, ordinary
  route, agent procedures, standalone/PDF output, or QA evidence while this
  validator still prints PASS.

**Governing gates:** A01, A03, A05-A11, A13; builder/agent deliverables in
`docs/V16_ACCEPTANCE_CRITERIA.md` and the frozen route contract.

**Bounded recommendation:** Add a content-coverage manifest or focused checks
for each required example class, Signal Foundry/two-neutral-case presence,
ordinary/lightweight/moderate/advanced language, agent source links, and
required export/QA artifacts. Treat presence checks as structural only; a
reader review is still needed to determine whether the examples are clear and
the progressive route works.

## Positive freeze evidence and limits

The following parts are internally aligned at this commit:

- The first-screen copy begins with the broad human problem and explicitly
  frames the headline as conceptual rather than measured
  (`docs/CONTENT_INTERFACE_FREEZE_V16.md:20-39`; JSON `:6-17`).
- The principal-door list is exactly `Read the idea`, `Explore the map`, and
  `Apply it`, in that order; the validator checks that exact list.
- The six-family JSON tuple matches the current framework source and the essay
  has all six ordered family headings. The short version is broad rather than
  origin-accounting-only and explicitly retains human judgment.
- The canonical Echo README/status and Signal Foundry case carry the required
  separate/unrun/no-results and illustration/not-validation boundaries.
- The archive checkpoint verifier and owner-intent checksum pass. No archive
  bytes were edited by this audit, and no deployment, publication, study,
  provider call, participant action, dataset acquisition, or spend occurred.

These are structural facts about the reviewed commit. They do not demonstrate
that a reader understands the idea in 60–90 seconds, that the site feels like
a coffee conversation, that the map is accessible, that an agent follows the
playbook, that Signal Foundry behaves as described, or that the framework
improves any outcome.

## Recommended disposition posture

The primary orchestrator should treat the contract as a usable implementation
input with the following bounded follow-ups before calling the site freeze
complete:

1. resolve the Markdown/JSON source-map scope and add the visual-needs gate;
2. strengthen validator lock checks (owner checkpoint, fixed six-family tuple,
   required claims/action keys, example/output coverage);
3. build the local site and collect rendered first-screen, three-door,
   current-vs-historical-map, Echo-removal, no-script/print, and cross-link
   evidence; and
4. run the separate A04/A06/A13 reader, accessibility, and visual reviews,
   without converting any structural PASS into a comprehension or effectiveness
   result.
