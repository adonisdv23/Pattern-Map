# Discriminating development objects

Status: **AUTHORED DEVELOPMENT ONLY / NO STUDY RUN / NO RESULTS**.
Base: dacbe02cc4fff24b5e88d3691f8408c7aa59043d; prepared 2026-09-07.
Governing requirements: [owner intent](../../../../docs/OWNER_INTENT_V16.md),
[artifact boundaries](../../../../docs/ARTIFACT_BOUNDARIES.md), A07–A08, A11,
A15–A17, and the explicit bounded Ultra development assignment.

These eight families and 16 paired variants expose design assumptions before
any study is considered. They are not independent task observations, approved
pilot materials, empirical results or evidence that a model benefits from the
proposed procedure. All earlier research/development files and Echo files retain
their bytes. The [mechanism](../MECHANISM_AND_COMPARATORS.md) and
[pilot decision specification](../PILOT_DECISION_SPEC.md) are separate successors.

The cases deliberately make decisive facts inspectable. This helps test the
formal contract; it does not establish realistic difficulty or external
relevance. A future study must use fresh, independently reviewed materials.

## Source and execution

- [case_objects.py](case_objects.py) is the single authored case source.
  Its author_objects function returns cases and reviewer keys as separate
  mappings; JSON files are not duplicated alongside this source.
- [cases.py](cases.py) contains pure projection, static acquisition, action
  accounting, property-predicate and finite mathematical helpers.
- [test_cases.py](test_cases.py) contains deterministic checks and authored
  adversarial advancement tables. It invokes no network or model.

Run from the repository root using the standard library:

    python3 -B research/future-studies/ultra/development/cases.py
    python3 -B -m unittest discover -s research/future-studies/ultra/development -p 'test_*.py' -v

The first command reports case and key hashes separately. Those hashes bind
the authored object values, not a pilot freeze, renderer implementation or
independent semantic approval. The Git commit binds source and tests.
There is no model runner, provider adapter, dataset acquisition or production
action. The code does not enforce an empirical filesystem or transport boundary.

## Eight substantive distinctions

| Family | Decision and paired change | Distinguishing evidence and legitimate contrast |
| --- | --- | --- |
| F1 ordinary sufficiency | Verbatim HTML conversion versus requested content selection | Visible e3 changes the requested product. An ordinary transformation may suffice; neither variant requires an invented four-field receipt. |
| F2 complementarity | Reconstruct paragraph order and bytes; matching versus different editions | Inspect d1 and d2. Manifest and blobs jointly work only when their edition relation holds. Rejecting each incomplete component can remove a valid combination. |
| F3 pruning and revision | Preserve Z2 comments; reversible versus irreversible rejection | d1 supplies compatibility omitted from the summary. Both variants retain all evidence; only the visibly declared reopening rule differs. This environment change is not a treatment advantage. |
| F4 positive presence after failure | Establish E8 in journal J's named sequence window; captured E8 versus E9 | Visible e1 contains the matching or mismatching row; e2 contains later capture failure. Positive presence can survive failure; the other-event variant remains unknown in paired hidden worlds. |
| F5 insufficient observation and next-action value | Failed folder enumeration; cheap versus costly subsequent check | Initial evidence never distinguishes receipt-present from receipt-absent worlds. An explicit toy loss/deadline table changes the accepted next action while the current assertion remains unknown. |
| F6 changed transfer applicability | Retry an interrupted export; idempotent versus duplicate-producing target | The same queue analogy appears in both variants. d1 changes whether its deduplication obligation holds; d2 offers reconciliation. Source behavior cannot be assumed in the target. |
| F7 reference versus authority | Locate the current decision; stable versus recycled identifiers | Inspect d1 for target binding and d2 for the cost of a writable copy. A pointer's usefulness depends on a valid binding, not the library analogy alone. |
| F8 finite-catalogue acquisition | Resume partial rendering; frozen versus drifting inputs | The familiar resume label (d1) does not guarantee version consistency. d2 and d3 can establish or defeat a checkpoint transfer within two acquisition units. |

Variants are paired design counterexamples, not extra independent tasks. F4/F5
hidden worlds are key checks, not new variants. F1–F8 cover different decisions;
the count eight does not establish a sampling frame. No result can be attributed
to the number of source nouns or cases.

## Visible schema and accounting

The full case carries internal ID/family/variant metadata, initial evidence and
a private evidence pool. The separate keys contain provisional property
predicates, assertion labels, action categories, sufficient key-context evidence
IDs and hidden-world alternatives. Metadata and keys never enter visible_payload.

The visible projection includes task, candidate cards, constraints, limits,
the action catalogue, output contract, utility assumptions and current state.
Evidence always has an ID and text. Candidate cards expose the same summary,
purpose, mechanism and detail IDs to every prospective arm. Supplying these
affordances tests their use; it does not test inventing purpose/mechanism metadata.
Unopened detail text is released only after its declared INSPECT action.

The apply_action function returns a new state. It records every attempt,
requested/charged acquisition units, acquired IDs, rejected IDs, terminal state
and final response. COMPARE records two candidate IDs without adding evidence.
REJECT and REOPEN retain source evidence; irreversible rejection prevents
reopening and selecting that named candidate. Described alternative
implementations remain possible. F3 therefore concerns the named route under
the declared rule, not impossibility of every implementation.

Each inspection costs one authored acquisition unit, including duplicates.
Invalid or rejected attempts also cost one unit. Successful bookkeeping and
terminal actions cost zero acquisition units but count toward the 12-attempt
cap. A charge is capped at remaining units; an unaffordable attempt is recorded
and terminates STOP. Consuming the last unit with a successful inspection still
permits a free terminal response. SELECT, HOLD and STOP are explicit; the helper
rejects further transitions after termination. These are toy bookkeeping rules,
not estimates of tokens, seconds, dollars or human effort.

The development helper is permissive about request and terminal-response shape.
Its over-budget attempt forces STOP. The successor pilot contract instead
preserves an opportunity for a valid final terminal choice within the attempt
cap K after acquisition budget B is exhausted. That strict request, release,
deadline and terminal contract requires a separate offline adapter. These
helpers do **not** implement or certify the pilot contract.

F5 alone grades next-action utility. Its state-independent loss table and
two-step deadline are supplied author assumptions, not elicited preferences.
The requested future check's result is never available in the present task.
For other families, listed next actions are provisional feasible categories;
their relative utility is ungraded.

## Acceptance and formal claims

The assess_reviewed_properties helper expects properties established by an
independent semantic reviewer, not a model's self-description. A route name
is never an acceptance condition. An unforeseen implementation can satisfy the
same predicate; an uncategorized next action is passed as None and receives
REQUIRES_ACTION_REVIEW, not automatic failure. Missing semantic review,
uninspected citations and insufficient key context remain distinct states.

Sufficient key-context lists prevent the full-information key from grading a
partial trace using unopened facts. A partial trace instead returns
REQUIRES_PARTIAL_EVIDENCE_REVIEW. This is not zero credit and not a mandate to
acquire every listed record: a valid safe proposal using fewer records requires
semantic adjudication. The helper deliberately does not resolve the full future
partial-trace rubric.

The tests show:

- Immediate and deferred filtering agree for every Boolean feasibility table
  and ordering of four candidates under the identical fixed independent
  predicate. They do not test a model, retrieval, interaction, deadlines or
  internal thought.
- Complementary components and revisable applicability break those assumptions.
  These are counterexamples to extending equivalence beyond its premises,
  not empirical timing effects.
- Paired hidden worlds with the same observable history retain identical
  assertions and action keys. F6/F8 applicability variants initially have
  identical projections; inspecting decisive evidence reveals the difference.
  An undiscriminated hidden fact earns no grade.
- Projection round-trips, key canaries, detail release, source retention and
  lexical parity hold for these objects. Paragraph/list renderers contain
  identical clauses in the same or reversed order. These checks establish
  neither semantic equality of future paraphrases nor a security boundary.

## Advancement adversarial table

These are hypothetical arithmetic examples, not simulated model performance.
Tests supply a **non-authoritative example** minimum gain of 0.10 and maximum
cost deltas of zero toy units and one reviewer minute. No study value is chosen.
Without explicit values, the helper returns UNSET_VALUE_JUDGMENTS.

| Authored table mutation relative to a passing example | Expected gate |
| --- | --- |
| Both contrasts: every task +0.25, no harm increase, costs within bounds | Eligible for a larger design review only |
| Two tasks +0.25, ten tasks −0.50 | Do not advance |
| R improves on ordinary practice but has zero gain over purpose/mechanism practice | Do not advance |
| Positive overall gain but a negative domain contrast | Do not advance |
| Added unsupported-presence errors despite higher acceptance | Do not advance |
| R introduces a scope error even when the baseline also erred | Do not advance |
| Fully explained resource increase exceeding a supplied margin | Do not advance |
| One ambiguous key, missing harm accounting, or non-finite harm values | Redesign the instrument |

The gate requires both baseline contrasts, nonnegative domain/regime contrasts,
no increase in any harm class overall or within a regime, no R scope/permission
error, and separately bounded resource deltas. It accepts reconciled cluster
summaries and an explicit validity flag; it cannot establish assignment
completeness, honest denominators, uncertainty or reviewer correctness itself.

## Remaining decisions

Local authoring still needed for a future instrument: exact safe release/parser
integration, complete terminal validation, a state-dependent partial-trace
rubric, fresh tasks and independent surface forms, and semantically defensible
keys. The helper has no elapsed-time guard; F5's step deadline only exercises
the supplied decision table. No claim of empirical adapter conformance follows.

Reviewer judgments remain task relevance, adequate negative controls, transfer
validity, plausible constraints/costs, evidence-to-property mapping, acceptance
of unforeseen implementations, and whether source wording plants the intended
answer. Those cannot be certified by these tests. Owner-only decisions include
what practical gain is worth its cost and later exact execution authorization.
Provider, spend, dataset, participant and publication authority remain absent.
