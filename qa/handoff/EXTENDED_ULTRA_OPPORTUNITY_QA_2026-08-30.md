# Pattern Map v16 extended ultra opportunity QA

Status: **BOUNDED CORRECTIONS INTEGRATED; FINAL EXACT-COMMIT SEAL FOLLOWS**

Date: 2026-08-30

Reviewed baseline:
`18128005d79b19e3a9d36ac68096acf264ff08d0`

This pass used the owner's additional time for three independent read-only
challenges—public design/accessibility, current primary research, and hostile
receipt-contract mutations—plus direct integrator reproduction. It did not
reopen the thesis, add a family or route, alter Echo, mutate the sealed Signal
Foundry packet, run a study, select a provider, acquire a dataset, publish, or
deploy.

The findings are implementation, structural, browser, and source-status
evidence only. They are not human comprehension, framework-effectiveness,
memory-defense, screen-reader-support, or research-result evidence.

## Accepted public-design corrections

### Family focus controls

The six enhanced Map buttons all displayed `Focus this family` and exposed
that same undifferentiated accessible name. A screen-reader button list could
not identify which family each control affected. The renderer now retains the
visible words and appends the family ID and name, for example:

`Focus this family: F4 · Absence + memory`

The built Map exposes six distinct names in both the DOM and Chrome
accessibility tree. This follows the W3C ARIA Authoring Practices
[names-and-descriptions guidance](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/)
to distinguish same-role controls while retaining the visible words inside the
accessible name, consistent with WCAG's
[Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html)
criterion. It does not claim a physical supported-screen-reader test.

### Planned-stop mobile microvisual

At 320 × 568 CSS pixels, the `if triggered →` phrase inherited a 90-degree
rotation intended for arrow-only connectors. It overlapped both neighboring
boxes by approximately 544.64 square pixels each. The mobile rule now keeps
that phrase horizontal.

The post-correction live geometry is:

- plan/connector intersection: `0`;
- connector/stop-event intersection: `0`;
- connector transform: `none`;
- connector bounds: 90.71 × 19.02 CSS pixels, fully inside the 254-pixel
  microvisual;
- document horizontal overflow: `0`.

Static checks lock the family-name and mobile-transform contracts. Direct live
geometry was remeasured only after opening the affected disclosure; a hidden
zero-size copy was not accepted as evidence.

## Accepted current-research corrections

The active source route and research records now use the official publication
status for:

- [GroupQA](https://aclanthology.org/2026.findings-acl.2003/): peer-reviewed
  Findings of ACL 2026, not only its earlier arXiv/ARR state;
- [Memory-R1](https://aclanthology.org/2026.acl-long.583/): ACL 2026 long
  paper, not only its earlier preprint state; and
- [PROV-AGENT](https://impact.ornl.gov/en/publications/prov-agent-unified-provenance-for-tracking-ai-agent-interactions-/):
  IEEE e-Science 2025 proceedings, with official ORNL metadata and DOI.

Three directly relevant peer-reviewed records earned one narrow addition:

- NeurIPS 2025
  [AbsenceBench](https://proceedings.neurips.cc/paper_files/paper/2025/hash/36b31e1bb8ecd4f4081686448e9eff2d-Abstract-Datasets_and_Benchmarks_Track.html)
  makes explicit-baseline omission detection direct prior art and reports
  bounded errors even with original and edited contexts;
- NeurIPS 2025
  [MINJA](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42a97bbd9844d2bf68596730af80bcdf-Abstract-Conference.html)
  reports query-only persistent-memory injection; and
- USENIX Security 2026
  [FragFuse](https://www.usenix.org/conference/usenixsecurity26/presentation/rao)
  reports cross-interaction reconstruction that bypasses tested agent access
  controls.

The resulting boundary is negative and deliberately small. An explicit
expectation is necessary but not sufficient for reliable omission detection.
A `CURRENT`, source-bound, versioned, and reuse-authorized memory record remains
untrusted data; retrieval does not make stored text instruction, policy, or
authority. These papers do not validate Pattern Map or establish that its
records prevent either attack class.

C16-007 and C16-017 were constrained without adding a claim ID. Candidate B
remains provisional, unselected, and distinct only as an unresolved question
about the orthogonal observation/process/access/permission/currency record and
its downstream decision effect. The human essay, Echo, and Signal Foundry did
not change.

## Accepted receipt-contract corrections

The repository-internal structural validator now fails closed on the
following previously accepted fixture mutations:

1. duplicate JSON object keys and non-finite `NaN`/infinity values, including
   nested permission keys and numeric overflow;
2. extra layered top-level fields, including ordinary Stage 0 fields or
   contradictory action booleans;
3. Boolean, non-finite, negative, over-limit, or nonpositive-limit time
   budgets, including raw negative-underflow and large-decimal literals that
   would otherwise collapse to an accepted binary floating-point value;
4. cross-kind record-ID collisions before evidence and memory indexes can be
   merged;
5. an `INDEPENDENT` comparison whose linked evidence does not consistently
   record independent origin; and
6. a high-consequence final `ANSWER` with no selected `SUPPORTED` evidence;
   and
7. a `STOPPED_DEADLINE` status whose reason names only budget exhaustion.

Positive controls retain a supported high-consequence final answer, an
unsupported high-consequence provisional answer, and a consistent independent
relation. The change remains fixture-scoped procedural QA, not a production
parser, permission service, security boundary, or proof that an agent follows
the contract.

The first exact-commit fuzz cycle caught the remaining decimal-conversion seam:
`-1e-9999` became `-0.0`, and `9007199254740993.0` collapsed to the same float
as `9007199254740992.0`. The strict loader now rejects a decimal token when its
exact value cannot survive the parser's binary-float representation. Both raw
byte cases are permanent negative mutations; the clean-cycle count restarted
on the successor rather than treating the superseded checkpoint as clean.

Two operator-template contradictions were also corrected. Origin and
recurrence now have distinct Evidence Register columns. A reviewed outcome
uses `LEARNING_REVIEWED` and cannot say that its proposed update was silently
applied.

## Controlled deferrals

The following findings are real hardening opportunities but were not safe to
fold into this bounded correction without changing the executable receipt
shape or claiming more than the current validator does:

| Finding | Disposition | Reason and exact reopening condition |
| --- | --- | --- |
| Machine-enforce the complete Advanced conjunction | **Deferred** | Current receipts lack separately typed high-uncertainty and capacity-approval fields. Reopen only with an explicit receipt-shape revision, updated fixtures/templates, and cross-artifact parity; do not infer “substantial” from a minute count. |
| Add outcome chronology and accountable disposition-actor/authority fields | **Deferred** | This changes pending/reviewed record topology. Reopen with an explicit migration that orders expectation, window, observation, and review timestamps and keeps synthetic fixtures from impersonating human approval. |
| Restrict pointer schemes and normalize portable IDs | **Deferred** | The current validator checks fixture syntax and does not dereference pointers. Reopen with a documented scheme registry and ASCII-or-NFC identity contract rather than an ad hoc denylist. |
| Execute the full Draft 2020-12 six-family schema instead of a partial manual mirror | **Deferred** | Reopen after choosing either a locked validator dependency or a complete dependency-free mirror plus negative mutations. The checked-in spec is not shown to violate its schema. |
| Claim accessibility or human comprehension from browser/model review | **Rejected** | Automated and advisory evidence cannot replace supported assistive-technology, owner, mentor, or cold-human review. |
| Add a security subsystem, trust score, seventh family, study, route, or new public dashboard | **Rejected** | None is required to state the earned negative memory boundary; each would expand topology or imply unsupported capability. |

## Verification performed before final sealing

- locked owner-intent SHA-256 checkpoint: pass;
- targeted research-boundary validator: pass;
- seven research claim-convergence tests: pass;
- applied structural validator and permanent hostile mutations: pass;
- Python compilation of the applied validator: pass;
- ten-route review/public site build and complete site contract suite: pass;
- direct 320-pixel live geometry and accessibility-tree recheck: pass;
- `git diff --check`: pass;
- archive, Echo, and sealed Signal Foundry source diffs: empty.

The complete twelve-stage clean-checkout runner, regenerated owner manifest,
exact remote readback, and successor ZIP verification occur only after all
source, generated standalone, QA, decision, and disposition bytes stop moving.
Those observations remain external to the manifest-covered narrative to avoid
a self-referential seal.
