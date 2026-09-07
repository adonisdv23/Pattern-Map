# Echo research-separation integrity advisory

**Reviewed snapshot:** `040498a18461ea90cb07a47ddfbf9c2a7853f630`  
**Parent:** `4d412e9611e3ecf21d5d8411a00ecde8d98e9e4c`  
**Branch:** `codex/pattern-map-v16-foundation`  
**Review date:** 2026-08-19, America/New_York  
**Review lane:** Wave 2 — Echo Problem research-separation integrity  
**Scope:** local repository evidence only; immutable v15.2 accession and EP v0.1
curation; v16 manuscript, framework, cases, and governing lineage records.

## Verdict

**Overall verdict: PASS WITH REVISIONS.**

The accession, byte/provenance chain, EP v0.1 identity, no-results boundary,
curated-source mapping, and deterministic local harness all pass the checks
available in this checkout. The two structural removal directions also pass:
the broad v16 work retains its thesis, six families, agent procedures, and
cases when the Echo project and explicit Echo examples are removed; the Echo
successor remains independently verifiable and runnable when v16 paths are
absent. I found no evidence that a protocol, fixture, validator, model review,
or deterministic test has been represented as an empirical result.

One current canonical boundary record should be revised before the owner-review
freeze: `docs/TWO_PROJECT_SEPARATION.md` gives a shortened unfavorable-result
list that omits the canonical `threshold_only_vor` class and uses several
non-token aliases. The exact authoritative manifest, EP status JSON, and EP
status table agree and are complete, so this is a documentation consistency
defect rather than a preservation failure. The exact ZIP's dependence on an
owner-local path is already documented and deferred; it is not a newly
discovered failure.

This is an advisory review, not an owner decision, reader study, model study,
effectiveness result, or authorization to run one. The report is the only file
written for this lane.

## Authority and review method

I read the repository instructions and the required governing documents in the
specified order, then verified the locked owner-intent checksum:

```text
(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)
OWNER_INTENT_V16.md: OK
```

The requested audit target is the immutable snapshot `040498a`; content-
sensitive removal checks below are explicitly extracted from that commit. The
worktree was clean when this lane began. The authority used for interpretation
was the owner-locked intent, thesis/audience contract, artifact boundaries,
source lineage, acceptance criteria, decision log, and review/disposition
protocol.
In particular, the following governing boundaries control this audit:

- v16 is the broad Pattern Recognition / Discrimination Layer work and begins
  from the v13 reader problem and all six families.
- The Echo Problem / ECHO-01 is a separate origin-accounting research track
  derived from the exact v15.2 checkpoint; it may illustrate v16 but may not
  define it.
- Archives are immutable; adjacent accession or curated-successor records carry
  new labels and status explanations.
- A protocol, fixture, planning simulation, model review, or local test is not
  an empirical result.
- Model/provider calls, participant work, external-data acquisition, spending,
  publication, deployment, and other prohibited research or external actions
  remain out of scope.

No web search, literature search, external connector, provider, model, dataset,
participant, or paid service was used. All checks below are local file,
checksum, archive, source-checkout, static-removal, or deterministic-test
checks.

## Observed verification

The following are observations from commands or source inspection in this
review. They are integrity and implementation observations, not claims that
origin accounting or the broader framework works in the world.

| Check | Observed result | Evidence and interpretation |
| --- | --- | --- |
| Owner-intent lock | PASS | The checksum command above passed. `docs/DECISION_LOG.md:91-105` makes the hash a required downstream gate. |
| Accession-only verification | PASS | `verify_accession.py` passed with 239 manifest-listed files, 48,717,432 payload bytes, 69,680 manifest bytes, and the recorded sidecar. The verifier checks manifest schema/path safety and per-file bytes/hashes (`archive/transfers/v15.2-owner-handoff/verify_accession.py:64-150`) and sidecar identity (`:153-171`). |
| Source-container verification | PASS locally | The same verifier, supplied the existing local owner ZIP, passed 41,436,496 bytes, SHA-256 `f8b71db0bda7f7564e5d3cec1f697bee38b3fcb17b56f47c79bf653f39b549b5`, 240 members, sidecar equality, embedded-manifest equality, per-member hashes, and CRC/data testing (`archive/transfers/v15.2-owner-handoff/verify_accession.py:174-246`). |
| Source-checkout byte/provenance comparison | PASS locally | I compared every one of the 239 accession entries against its manifest `source_path` in `/Users/gpt/Documents/Codex/worktrees/discrimination-layer-v15-2-overnight`; all 239 matched byte-for-byte, totaling 48,717,432 bytes. The source checkout is clean at commit `36568cb6e8afce9544606c968319b063fc9b79ce`, matching the recorded source anchor (`archive/transfers/v15.2-owner-handoff/ACCESSION_RECORD.md:6-18`). |
| Curated EP source mapping | PASS | `research/the-echo-problem/qa/verify_preserved_sources.py` passed for 82 curated files and 11,323,689 bytes. The mapping deliberately preserves historical repository-relative harness/config/schema paths (`research/the-echo-problem/qa/verify_preserved_sources.py:16-41`, `:119-137`), and the index explains why those paths are needed without changing bytes (`research/the-echo-problem/PRESERVED_V15_2_INDEX.md:10-21`, `:31-36`). |
| Deterministic preserved harness | PASS | `python3 -m unittest discover -s tests -v` from the preserved root ran 15 cases and returned `OK`. The source package itself describes this as an offline test rather than a study (`research/the-echo-problem/qa/EP_V0_1_QA.md:16-20`, `:40-44`); the implementation declares no model/network/provider machinery (`research/the-echo-problem/preserved/v15.2/tools/origin_accounting/__init__.py:1-7`). |
| Applied v16 structural QA | PASS for its stated scope | `python3 qa/applied/validate_framework.py` passed all four structural/procedural checks. The QA record explicitly says effectiveness, agent compliance, product behavior, and real-world usefulness were not tested (`qa/applied/PLAYBOOK_INTEGRATION_QA.md:29-43`, `:55-61`). |

The accession record and QA report describe the same preservation boundary: the
extracted payload preserves content bytes and per-file provenance, while the
original ZIP container is intentionally outside Git (`archive/transfers/v15.2-owner-handoff/ACCESSION_RECORD.md:20-46`; `archive/transfers/v15.2-owner-handoff/QA/ACCESSION_VERIFICATION_REPORT.md:29-36`).

## Findings

Severity uses `P0` for release-blocking integrity failure, `P1` for a serious
boundary or claim defect, `P2` for a material but bounded revision, and `P3`
for a low-severity or already-documented residual. `Pass` means the observed
state satisfies the reviewed requirement. `Pass with revisions` means the
integrity boundary holds but a current record should be reconciled. The
recommended disposition uses the controlled vocabulary from
`docs/REVIEW_AND_DISPOSITION_PROTOCOL.md`.

### ERS-01 — Accession and provenance chain

- **Severity:** P1 integrity gate
- **Verdict:** **Pass**
- **Recommended disposition:** Accepted
- **Governing gate:** A10, A14, A15; D-004 and D-009; artifact-boundary archive immutability
- **Evidence:** The accession record records source checkout/branch/commit, ZIP
  size and hash, manifest and sidecar hashes, 239 payload files, and 48,717,432
  payload bytes (`archive/transfers/v15.2-owner-handoff/ACCESSION_RECORD.md:6-38`).
  It states that the payload was copied from verified ZIP members and that the
  ZIP container is not being called a byte-identical re-zip
  (`:40-50`). The verifier enforces the recorded payload directories, rejects
  symlinks and unsafe paths, checks every manifest entry's bytes and SHA-256,
  then checks source ZIP members, embedded manifest, and CRCs
  (`archive/transfers/v15.2-owner-handoff/verify_accession.py:115-150`,
  `:211-238`). The independent source-checkout comparison in this review also
  matched all 239 manifest `source_path` entries.
- **Bounded recommendation:** Keep the accession and verifier unchanged. At
  owner review, continue to describe the extracted payload and exact ZIP as
  two separately verified artifacts; do not call a future re-zip byte-identical
  without the whole-file hash.

### ERS-02 — EP v0.1 identity and no-results boundary

- **Severity:** P1 research-containment gate
- **Verdict:** **Pass**
- **Recommended disposition:** Accepted
- **Governing gate:** A10, A11, A15; D-001, D-005, D-009
- **Evidence:** The EP entry point identifies ECHO-01 and EP v0.1 as an
  unrun, no-results, unpublished successor and says it does not rewrite the
  preserved source set (`research/the-echo-problem/README.md:1-21`). Its
  decision boundary explicitly records zero model/provider calls, zero
  participants, no acquired external dataset, and the distinction between
  integrity results and research results (`README.md:33-49`). The status record
  says no model, empirical, pilot, or participant study ran and that the
  preserved package is a protocol-and-implementation checkpoint
  (`research/the-echo-problem/STATUS_AND_BOUNDARIES.md:3-18`). The JSON status
  independently records `model_or_provider_calls: 0`, all three study flags as
  false/zero, no dataset acquisition, and not published/deployed
  (`research/the-echo-problem/qa/EP_V0_1_STATUS.json:4-23`).
- **Bounded recommendation:** Preserve the current direct no-results language
  in all future EP entry/status surfaces. A passing verifier or test may be
  cited only as preservation or implementation evidence.

### ERS-03 — Exact unfavorable-result classes

- **Severity:** P1 claim-containment gate
- **Verdict:** **Pass** for the authoritative records
- **Recommended disposition:** Accepted
- **Governing gate:** A10, A11, A15; owner intent permanent separation; D-009
- **Evidence:** The external manifest records 11 canonical classes at
  `archive/transfers/v15.2-owner-handoff/PATTERN_MAP_V15_2_OWNER_HANDOFF-manifest.json:37-49`:
  `null`, `rule_only`, `invalidity_driven`, `threshold_only_vor`, `harmful`,
  `shortcut_driven`, `surface_or_semantic_audit_failure`, `unstable`,
  `noise_fragile`, `nontransfer`, and `stopped_or_quarantined`. The EP status
  JSON contains the same 11 tokens in the same order
  (`research/the-echo-problem/qa/EP_V0_1_STATUS.json:25-36`), and the human
  status table defines each as a possible category rather than an observed EP
  result (`research/the-echo-problem/STATUS_AND_BOUNDARIES.md:45-67`). The
  exact list equality and no-results flags were checked in this review. The
  future plan also says to preserve the full space and report null/rule-only
  outcomes with the same care as favorable outcomes
  (`research/the-echo-problem/FUTURE_EXECUTION_PLAN.md:26-33`, `:52-67`).
- **Bounded recommendation:** Keep the manifest, status JSON, and status table
  as the exact class authority. Current v16 prose may use a smaller plain-
  language subset when it is clearly non-exhaustive; it must not present that
  subset as the complete EP class taxonomy.

### ERS-04 — Echo is subordinate in v16 prose and route structure

- **Severity:** P1 separation gate
- **Verdict:** **Pass**
- **Recommended disposition:** Accepted
- **Governing gate:** A01, A03, A06, A10, A16; D-001, D-007, D-008
- **Evidence:** The locked intent explicitly says v16 may link to Echo and use
  common-origin recurrence as one worked example, while the reader must still
  understand v16 if the example is removed (`docs/OWNER_INTENT_V16.md:183-192`).
  In the canonical essay, all six family headings occur at lines 56-179; the
  first explicit Echo section begins only at
  `manuscript/PATTERN_RECOGNITION_V16.md:201-229`, where it is called a
  subordinate example and explicitly removable. The essay's research boundary
  says a protocol, fictional fixture, planning simulation, or local validator is
  not an empirical result and that no study/model/provider has been selected as
  evidence (`manuscript/PATTERN_RECOGNITION_V16.md:315-337`). The optional route
  links to EP v0.1 and its no-results record without importing a result, selected
  model, or discovered provenance (`manuscript/SOURCES_AND_RESEARCH_ROUTE.md:51-70`).
- **Bounded recommendation:** Keep the Echo link in the optional route and
  preserve its late, subordinate placement in the essay. Do not move the Echo
  protocol, F0/F1/F2 notation, or EP status claims into the opening or the
  six-family public map.

### ERS-05 — Framework and case references preserve distinctions

- **Severity:** P1 separation/overclaim gate
- **Verdict:** **Pass**
- **Recommended disposition:** Accepted
- **Governing gate:** A03, A07-A09, A11, A15; artifact-boundary shared-concepts rule
- **Evidence:** The framework identifies the six families as the public map and
  mechanisms as supporting, not replacing, them (`framework/SIX_FAMILIES.md:3-16`,
  `:20-32`). Its F5 section makes common-origin accounting one comparison
  mechanism, retains unknown relations, and states that the relation does not
  establish correctness (`framework/SIX_FAMILIES.md:230-265`). The relationship
  map's removal test says the map remains complete without the common-origin
  example (`framework/RELATIONSHIP_MAP.md:113-118`), and the boundaries require
  recurrence not to be treated as independent corroboration and a fixture or
  protocol not to be treated as a result (`framework/BOUNDARIES_AND_FAILURES.md:124-136`).
  The implementation choices are stack/provider/model neutral
  (`framework/IMPLEMENTATION_CHOICES.md:3-19`).

  The cases consistently label their values as invented fixtures rather than
  observations or studies (`cases/general-research/README.md:1-9`,
  `cases/product-and-process/README.md:1-8`). Signal Foundry is explicitly
  read-only and not validation, imports no runtime/data/credentials/provider
  calls, and marks every row illustrative (`cases/signal-foundry/README.md:1-15`,
  `:40-41`, `:55-68`, `:93-122`).
- **Bounded recommendation:** Retain the case headers and boundary sentences
  whenever examples are copied into another v16 surface. Treat provider
  receipts as operation metadata, not content correctness or research evidence.

### ERS-06 — Removal direction: v16 without Echo

- **Severity:** P1 firebreak gate
- **Verdict:** **Pass** for a static/structural removal check
- **Recommended disposition:** Accepted
- **Governing gate:** A01, A03, A07, A08, A10; D-008; `docs/TWO_PROJECT_SEPARATION.md:70-77`
- **Observed check:** In a temporary directory, I extracted only the v16-owned
  manuscript core, framework, and cases from `git archive 040498a`, with no
  `research/the-echo-problem/` path. In an in-memory copy, I removed the
  canonical essay block headed “A narrower example: nine reports, one
  announcement” (`manuscript/PATTERN_RECOGNITION_V16.md:201-229`) and the
  ordinary-vs-layered repeated-claim example
  (`framework/agent-playbook/ORDINARY_VS_DISCRIMINATION_LAYER.md:36-63`).
  Assertions over the remaining temporary text retained the broad thesis,
  all six family names, human judgment, uncertainty, cost/stop boundaries,
  agent decision/comparison/disconfirmation/uncertainty/learning procedures,
  and both domain-neutral cases. The check printed:

  ```text
  V16_REMOVE_ECHO_PASS: core v16 archive omitted Echo path; in-memory removal of essay/ordinary Echo examples retained thesis, six families, agent procedures, boundaries, and cases
  ```

  This is a structural removal check, not a cold-reader comprehension result.
- **Bounded recommendation:** Keep this removal test in the owner-review
  evidence package and re-run it after any content-interface change. If a future
  site adds an Echo route, test the no-Echo core separately rather than treating
  the route's presence as proof of coherence.

### ERS-07 — Removal direction: Echo without v16

- **Severity:** P1 firebreak/reproducibility gate
- **Verdict:** **Pass** for source independence and deterministic replay
- **Recommended disposition:** Accepted
- **Governing gate:** A10, A14, A15; D-008; `research/the-echo-problem/RELATION_TO_V16.md:39-58`
- **Observed check:** In a separate temporary directory, I extracted only
  `research/the-echo-problem/` and
  `archive/transfers/v15.2-owner-handoff/` from `git archive 040498a`; no
  v16 `manuscript/`, `framework/`, or `cases/` path was present. From that
  reduced tree I ran the accession verifier against the existing local ZIP,
  the curated-source verifier, and the preserved-root deterministic unittest
  suite. All returned zero; the suite ran 15 cases. The check printed:

  ```text
  ECHO_STANDALONE_PASS: Echo+accession archive omitted v16 paths; accession, curated-copy, and 15-case deterministic harness checks passed
  ```

  The EP entry documents the independent question, source checkpoint, protocol,
  harness, fixtures, prior art, no-results state, and future gates
  (`research/the-echo-problem/README.md:7-21`, `:23-49`; `PRESERVED_V15_2_INDEX.md:10-29`).
  The formal relation expressly says that EP must still stand after v16 is
  removed (`RELATION_TO_V16.md:39-51`). This replay establishes source and
  execution independence, not reader comprehension or research effectiveness.
- **Bounded recommendation:** Preserve the historical repository-relative
  curated paths and run these deterministic checks whenever the curation or
  accession mapping changes. Do not add a v16 dependency merely to make EP
  runnable.

### ERS-08 — Current boundary list omits one canonical unfavorable class

- **Severity:** P2 documentation consistency
- **Verdict:** **Pass with revisions**
- **Recommended disposition:** Accepted with revision
- **Governing gate:** A10, A11, A15; D-008; `docs/REVIEW_AND_DISPOSITION_PROTOCOL.md` controlled dispositions
- **Evidence:** The current permanent two-project record lists null,
  rule-only, invalidity-driven, harmful, shortcut-driven,
  surface/semantic-audit-failure, unstable, noise-fragile, non-transfer, and
  stopped/quarantined classes (`docs/TWO_PROJECT_SEPARATION.md:24-32`). It does
  not list the canonical `threshold_only_vor` class, and several entries are
  prose aliases rather than the exact source/status tokens. By contrast, the
  authoritative accession manifest and EP status records contain all 11 exact
  tokens (`archive/transfers/v15.2-owner-handoff/PATTERN_MAP_V15_2_OWNER_HANDOFF-manifest.json:37-49`,
  `research/the-echo-problem/qa/EP_V0_1_STATUS.json:25-36`), and the human EP
  status table includes the missing `threshold_only_vor` row
  (`research/the-echo-problem/STATUS_AND_BOUNDARIES.md:51-63`).

  The immutable v15.2 start page also uses compressed historical prose rather
  than the exact taxonomy (`archive/transfers/v15.2-owner-handoff/00_START_HERE/README.md:48-58`);
  that is not an archive defect and must not be repaired in place.
- **Bounded recommendation:** Revise only the current canonical
  `docs/TWO_PROJECT_SEPARATION.md` list to either enumerate all 11 canonical
  tokens or explicitly link to `research/the-echo-problem/STATUS_AND_BOUNDARIES.md`
  as the complete taxonomy, with plain-language aliases in a separate column
  or sentence. Do not edit the immutable archive. This is a bounded wording
  reconciliation and does not change owner intent.

### ERS-09 — Exact ZIP clone limitation is documented, not a preservation failure

- **Severity:** P3 reproducibility residual
- **Verdict:** **Pass with documented limitation**
- **Recommended disposition:** Deferred
- **Governing gate:** A14, A15; D-004; ECHO-06 in `docs/ADVISORY_REVIEW_DISPOSITIONS.md:25`
- **Evidence:** The full source-container check passed in this local
  environment, but the exact 41,436,496-byte ZIP is intentionally outside Git;
  a clone without the owner-local source path can verify extracted payloads but
  cannot independently verify container metadata (`ACCESSION_RECORD.md:40-59`,
  `QA/ACCESSION_VERIFICATION_REPORT.md:29-36`). The existing disposition
  already records this as deferred pending an owner-authorized storage route.
- **Bounded recommendation:** Keep the residual explicit in handoff material;
  before any claim of clone-independent container verification, obtain the
  exact owner-authorized storage route and re-run the whole-file/member check.
  Until then, claim only extracted-payload and locally source-container
  verification.

## Reference and claim-boundary audit

The requested v16 reference sweep found the following pattern, with no
unbounded Echo dependency:

| Surface | Observed references | Boundary result |
| --- | --- | --- |
| Human manuscript | Echo/common-origin appears after the six-family map; the explicit section is labeled subordinate/removable (`manuscript/PATTERN_RECOGNITION_V16.md:46-229`). The short version contains no Echo route in the sweep. Late research prose says no protocol/fixture/validator is a result and no study/model/provider has been selected (`:315-331`). | **Pass** — broad human argument precedes the origin-accounting example. |
| Optional source route and origin note | Direct EP v0.1 and no-results links are optional and explicitly say no result, selected model, or discovered provenance is imported (`manuscript/SOURCES_AND_RESEARCH_ROUTE.md:1-4`, `:51-70`; `manuscript/ORIGIN_NOTE.md:10-28`). | **Pass** — wayfinding is separate from the core argument. |
| Builder framework and agent companion | Recurrence/common-origin is a typed relationship and F5 mechanism; unknown remains unknown; the map has a removal test (`framework/MECHANISMS.md:101-125`; `framework/SIX_FAMILIES.md:230-265`; `framework/RELATIONSHIP_MAP.md:70-118`). | **Pass** — origin accounting does not replace the six-family map. |
| Cases and fixtures | General research and product/process values are invented procedure fixtures; Signal Foundry is read-only, not validation, with no runtime/provider calls (`cases/general-research/README.md:1-9`, `:30-40`; `cases/product-and-process/README.md:1-8`, `:29-39`; `cases/signal-foundry/README.md:1-15`). | **Pass** — no fixture is presented as an observation or result. |
| Lineage/version/decision/disposition records | The authority order, permanent split, EP v0.1 sequence, accession decision, reproducibility correction, and prior-art disposition all point to separate paths and no-results status (`docs/SOURCE_AUTHORITY_AND_LINEAGE.md:6-21`, `:35-52`; `docs/VERSION_HISTORY.md:1-20`; `docs/DECISION_LOG.md:6-17`, `:122-175`; `docs/ADVISORY_REVIEW_DISPOSITIONS.md:20-25`, `:39-45`). | **Pass**, subject to ERS-08's exact-class wording revision. |

The active v16 site is not yet implemented beyond its owner-review placeholder
(`site/README.md:1-6`), so this review does not claim a rendered-site link,
navigation, or visual-label pass. The manuscript's optional route is present;
site-specific A10 checks remain a later site-lane dependency, consistent with
the roadmap and prior-art disposition (`docs/DECISION_LOG.md:257-259`). This is
scope/dependency context, not evidence that the two projects currently collapse.

## No-results interpretation boundary

The following distinctions are preserved and should remain explicit in any
future handoff:

1. **Archive integrity is not research evidence.** Hashes, byte counts, source
   commit comparison, manifest checks, and ZIP CRCs establish preservation and
   provenance of the package, not the truth of an origin relation or the value
   of the framework.
2. **Offline implementation tests are not study results.** The 15 passing
   unittest cases exercise deterministic parser, schema, fixture, and invariant
   behavior. They do not call a model/provider, create an empirical condition,
   establish efficacy, or show a human decision benefit.
3. **Fixtures and planning simulations are not observations.** The v16 cases
   and preserved EP fixtures are explicitly invented or synthetic contracts;
   planning values such as 300 primary cases and 75 safety cases remain plans,
   not denominators with outcomes (`research/the-echo-problem/STATUS_AND_BOUNDARIES.md:31-43`).
4. **Unfavorable classes are possible categories, not observed EP outcomes.**
   The EP status table says this directly (`STATUS_AND_BOUNDARIES.md:45-67`).
   No favorable or unfavorable research result was observed in this review.
5. **Provenance constrains interpretation but does not establish correctness.**
   The relation document keeps common origin, truth, authority, permission, and
   human disposition distinct (`research/the-echo-problem/RELATION_TO_V16.md:24-37`).

## Handoff recommendation

Record the report as an advisory Wave 2 input. The primary orchestrator should
assign ERS-01 through ERS-07 as `Accepted` if the stated evidence is retained,
assign ERS-08 as `Accepted with revision` and reconcile the current class list,
and retain ERS-09 as `Deferred` until an owner-authorized exact-container
storage route exists. Re-run the owner-intent checksum before integration.

No archive, canonical v16 artifact, decision log, disposition ledger, or
owner-intent file was changed by this audit.
