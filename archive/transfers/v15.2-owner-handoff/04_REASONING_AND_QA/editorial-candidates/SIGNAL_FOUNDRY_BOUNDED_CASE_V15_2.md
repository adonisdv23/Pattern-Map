# Signal Foundry: a bounded worked case

**Candidate status:** v15.2 `Explore / Cases` candidate for owner review  
**Evidence status:** synthetic offline Workbench fixture; not live acceptance,
validation, or a product result

This case translates a small part of the Pattern Map into Signal Foundry. It is
an illustration of a decision boundary, not evidence that the full framework is
necessary or effective. The useful question is not whether Signal Foundry has
eleven new components. It is whether preserving a few distinctions changes what
an operator is allowed to conclude or do.

## Identifiers and evidence boundary

- **Signal Foundry revision audited:** `f9bf3775ca3d5b52ea5083cea52306c025727e23`
- **Pattern Map candidate revision:** `22f232701184812489843731b6fe27592118eb29`
- **Transfer audit:** `PATTERN_MAP_V15_2_SIGNAL_FOUNDRY_TRANSFER_AUDIT.md`
- **Fixture version:** `evidence_workbench_offline_fixture_v1`
- **Case ID:** `case.setup-proof`
- **Canonical record reference:** `canonical://youtube/video-a`
- **Episode:** `episode.setup-proof`
- **Synthetic relation:** `relationship.syndicated-a-b`
  (`SYNDICATED_FROM`)
- **Open contradiction:** `contradiction.setup-open`
- **Gap:** `gap.video-a.setup-proof`
  (`EXPECTED_BUT_MISSING`)

The fixture is generated and inspected locally. It contains two exact matching
source claims, a third contradictory claim, a bounded gap, and append-only
synthetic episode history. Hostile prompt- or script-shaped text in the fixture
is data rendered inert; it is not an instruction or an external action.

## The case in one sentence

The question is:

> **Did the bounded walkthrough show the setup procedure?**

`assertion.setup.a` and `assertion.setup.b` make the same exact claim and are
connected by the retained `SYNDICATED_FROM` edge. They produce **two raw
observations but one known supporting-origin path**. `assertion.setup.c`
contradicts them, and that contradiction remains open. The inspected transcript
boundary does not contain the expected setup artifact, so the gap is
`EXPECTED_BUT_MISSING`, not confirmed real-world absence.

The recorded human next step is **HOLD / DEFER**: defer judgment pending an
independently observed primary artifact. That sentence is a disposition, not a
finding that such an artifact exists or that the two synthetic reports are
actually independent in the world.

## Five-field receipt

This is the compact receipt a reader can inspect without reading the whole
framework.

| Field | Fixture value | Boundary it preserves |
| --- | --- | --- |
| **Claim** | `Did the bounded walkthrough show the setup procedure?` (`episode.setup-proof`; condition assertion `assertion.setup.a`) | A question is not the same object as a report, evidence pointer, or later outcome. |
| **Observations** | Two exact matching `SOURCE_CLAIM` observations: `assertion.setup.a` and `assertion.setup.b`; two evidence references; raw occurrence count `2`; known supporting-origin paths `1` | Recurrence is visible, but two reports do not become two supporting origins. |
| **Relation state** | `RELATED` via `relationship.syndicated-a-b` / `SYNDICATED_FROM`; contradiction `contradiction.setup-open` is `OPEN`; gap `gap.video-a.setup-proof` is `EXPECTED_BUT_MISSING` | Relatedness, contradiction, and missingness remain typed. None is silently converted into truth, independence, or absence. |
| **Permission** | The synthetic packet and read-only Workbench fixture may be inspected. Provider retrieval, production use, external upload, transcript `Apply`, and new durable writes are not authorized by the fixture | Availability of a record is not permission to acquire, disclose, retain, or act on it. |
| **Next human action** | `HOLD / DEFER`: inspect or authorize one independently observed primary artifact; preserve the open contradiction and the gap | A human disposition routes the next step; it is not proof, a score, or a recommendation. |

The fixture's existing history records this as `event.operator-decision` and
`event.rationale`:

- “Defer judgment pending an independently observed primary artifact.”
- “Syndicated repetition is not independent corroboration.”

Those are historical identifiers and recorded synthetic text, not a claim that
the system discovered a real source relationship.

## What changes when the fields stay separate?

| Flattened reading | Discriminated reading | Decision delta |
| --- | --- | --- |
| “Two sources support the setup claim.” | Two observations, one known origin path, `RELATED`. | Do not count syndication as independent corroboration. |
| “The majority wins.” | `contradiction.setup-open` remains `OPEN`. | Preserve the incompatible assertion; do not average or majority-vote. |
| “The setup artifact is absent.” | The bounded inspection yields `EXPECTED_BUT_MISSING`. | Hold the gap; do not assert that the artifact does not exist outside the inspected boundary. |
| “The item is important, so its evidence is stronger.” | Attention priority only orders inspection. | Priority cannot change support, origin count, authority, or truth. |
| “The record is available, so the next operation is allowed.” | Record availability and operational authorization are separate. | No provider call, upload, disclosure, or Apply follows merely from presence. |

The Workbench's support display means that evidence references were recorded; it
does not mean that the references establish the claim. The relation state is
computed from exact claim and relationship identifiers, not from source count,
URL count, wording difference, or a ranking field.

## Five boundaries the case must keep visible

These are existing Signal Foundry contract distinctions that bound the case;
they are not new capabilities claimed by this candidate.

| Distinction | Safe interpretation in this case | Unsafe collapse |
| --- | --- | --- |
| **Attention vs support** | Daily Intelligence priority or `needs_manual_watch` can explain why an item is inspected. Support still requires an exact claim/evidence relationship. | Priority, recurrence, or salience becomes truth, authority, or a recommendation. |
| **Availability vs permission** | A packet, source, or artifact can be present or technically readable while provider transport, disclosure, retention, or external action remains `NOT_AUTHORIZED`. | A visible or available record becomes authorization, or a blocked lane becomes confirmed absence. |
| **Staged vs applied** | A transcript in `staged`/`pending` is not canonical active evidence. Only the receipt-bound `Apply` transition can promote it, and the receipt proves the operation—not transcript correctness or completeness. | Staged content enters exports, or a successful Apply receipt is treated as truth. |
| **Transcript vs Visual Evidence** | Screenshots, frames, and OCR remain Visual Evidence. Transcript text remains transcript evidence. Either may be cited as a separate class with its own limitation. | Visual text silently becomes transcript text, timestamps, transcript success, or a source claim. |

The case therefore demonstrates a decision discipline rather than a universal
data model: preserve the exact pointer, class, state, and permission boundary
long enough for a person to correct the route.

## Optional `CONTEXT_DISPOSITION` event — design proposal only

The transfer audit identifies one small missing connection: which existing
evidence a named operator question was permitted to use, and what was withheld
or deferred. A possible append-only event could reuse Signal Foundry's existing
decision-memory path instead of creating another ledger:

```json
{
  "event_type": "CONTEXT_DISPOSITION",
  "subject_ref": "canonical://youtube/video-a",
  "question_ref": "episode.setup-proof",
  "decision_cutoff_at": "2026-08-01T20:04:00Z",
  "included_evidence_refs": ["evidence.video-a", "evidence.syndicated-b"],
  "excluded_or_missing": [
    {"ref": "gap.video-a.setup-proof", "reason_code": "EXPECTED_BUT_MISSING"},
    {"ref": "contradiction.setup-open", "reason_code": "OPEN_CONTRADICTION"}
  ],
  "disposition": "HOLD_DEFER",
  "next_action": "REQUEST_INDEPENDENTLY_OBSERVED_PRIMARY_ARTIFACT",
  "actor_ref": "operator.fixture",
  "existing_context_refs": ["relationship.syndicated-a-b", "event.snapshot"],
  "limitation": "Does not establish truth, completeness, or real-world independence."
}
```

This event is **not implemented by this candidate and is not present as a
durable production fact**. Its exact name and schema require a separate
integration-owner decision, authority review, migration plan, and tests. If
implemented, it should carry pointers, IDs, digests, cutoff, reason codes, and
the next allowed action—not copied transcript bodies, images, credentials,
provider payloads, scores, ranks, source weights, or truth labels. A correction
would append and supersede the disposition while leaving the original evidence
and decision history intact.

## Correction scenario

The fixture already contains the conservative correction path:

1. `event.operator-decision` records **HOLD / DEFER**.
2. `event.expected-outcome` defines a later authorized synthetic check that may
   contain an independently observed artifact.
3. `event.actual-outcome` and `assertion.outcome-fact` record that the later
   bounded synthetic fixture did **not** add independent setup support.
4. `event.correction` supersedes `event.operator-decision` and leaves the
   question unresolved: later fixture review did not add independent support.
5. `event.limitation` records that this offline behavior does not establish
   empirical operator value.

A future real or authorized test could append a new artifact and a new
   disposition, but only after checking identity, relation, permission, and
   cutoff. It would not rewrite the original two observations or turn the old
   hold into a retroactive success. If the new artifact's origin is unresolved,
   the correct correction is still `UNKNOWN`/`HOLD`, not `INDP` by default.

## Why this earns its cost

This small receipt earns its cost when the question is consequential,
contested, dependence-heavy, time-sensitive, expensive to revisit, or likely to
be audited. In this case it prevents several concrete errors with existing
identifiers:

- counting two syndicated appearances as two origins;
- erasing an open contradiction through a majority summary;
- converting a bounded missingness observation into real-world absence;
- letting source or artifact availability authorize an external operation;
- allowing staged transcript material or Visual Evidence to contaminate a
  canonical transcript decision; and
- losing the reason for a human hold when a later correction arrives.

The marginal intervention is deliberately small: a readable five-field receipt
and, optionally, one pointer-only event in the existing decision-memory path.
It does not require an 11-service architecture, a second queue, a master score,
or a new canonical evidence store.

## When to skip it

Use the lighter path—a task brief, existing source/artifact pointers, and a
short human note—when the work is low-stakes, uncontested, single-origin, easy
to reverse, and has no external action, sensitive disclosure, or likely review.

Do not add `CONTEXT_DISPOSITION` if it cannot change at least one of:

- an allowed or withheld action;
- which evidence is included in the bounded context;
- the distinction between a gap and confirmed absence; or
- the correction/supersession path.

The full framework should disappear when it is only producing vocabulary,
duplicate receipts, decorative dashboards, or an attention score that does not
change what may happen next.

## Exact non-claims

This candidate does **not** claim that:

1. Signal Foundry implements, validates, or needs the complete Pattern Map.
2. The synthetic `SYNDICATED_FROM` edge establishes real-world provenance,
   truth, causality, editorial dependence, or epistemic independence.
3. Two raw observations, one known origin, or an `OPEN` contradiction predict
   an operator's correct answer.
4. The Workbench improves decision quality, operator calibration, speed, cost,
   safety, or information overload relative to a simpler workflow.
5. A successful operation, Apply receipt, available source, or readable packet
   proves correctness, completeness, authority, permission, or value.
6. Visual Evidence is transcript evidence, or a transcript is a complete view
   of what appeared on screen.
7. The `CONTEXT_DISPOSITION` event exists in production, has a frozen schema,
   or has been integrated into Signal Foundry's write path.
8. Any provider, model, Cloud job, hosted runtime, production dataset, IAM
   boundary, deployment, or external service was used in producing this case.
9. The fixture demonstrates natural syndication, independent support, source
   discovery, or a general model behavior.
10. Signal Foundry and Alpha Solver are currently integrated, or that either
    product case proves the conceptual thesis.

## Audit anchors

The candidate is grounded in the independent transfer audit and preserves its
shorthand identifiers:

- `SF-FIXTURE` — Signal Foundry
  `tools/evidence_workbench_offline_fixture.py:203`
- `SF-WB` — Signal Foundry `docs/evidence_workbench_v1.md:3`
- `SF-WB-TEST` — Signal Foundry `tests/test_evidence_workbench.py:97`
- `SF-GRAPH` — Signal Foundry `docs/evidence_graph_v1.md:5`
- `SF-TRANSCRIPT-DURABLE` — Signal Foundry
  `docs/transcript_durable_stage_apply_v1.md:38`
- `SF-VISUAL` — Signal Foundry `docs/visual_evidence_app_workflow.md:1`
- `SF-DECISION-MEMORY` — Signal Foundry
  `docs/decision_memory_retrospective_v1.md:5`
- `PM-SF-BOUNDARY` — Pattern Map
  `case-studies/SIGNAL_FOUNDRY_CASE_STUDY_BOUNDARY.md:1`

**Bottom line:** the case earns its place as a bounded Explore example because
it makes one changed decision visible: two matching reports remain two
observations but only one known origin path, while contradiction and missingness
stay open and the human disposition remains hold/defer. It should remain
clearly labeled as an offline contract fixture, not a validation result.
