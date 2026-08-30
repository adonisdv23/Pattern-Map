# Outcome review

Complete after the defined outcome window, not by hindsight.

## Executable state boundary

- `LEARNING_PLANNED`: `applicable` is true, but both
  `expectation_recorded` and `outcome_window_recorded` are false. No observed
  outcome, review, disposition, or applied update field is permitted.
- `LEARNING_PENDING_OUTCOME`: the expectation and outcome window are both
  recorded before the event. No observed outcome, review, disposition, or
  applied update field is permitted.
- `LEARNING_REVIEWED`: one linked outcome-review record binds the complete
  pre-review receipt, locked expectation/window, observed-or-explicitly-missing
  outcome, actual cost or missingness, confounders, attribution boundary,
  bounded update proposal, and human disposition. `update_applied` remains
  false; the record proposes an update but does not apply it.
- `LEARNING_NOT_APPLICABLE`: `applicable` is false and the object contains no
  expectation, result, review, disposition, or update fields.

Missing or mistyped applicability is invalid. A result or human disposition
cannot be carried backward into a planned, pending, or non-applicable state.

## Link to original record

- Outcome review ID:
- Review record status: RECORDED_REVIEW /
  SYNTHETIC_CONTRACT_ONLY_NOT_A_RESULT
- Original decision / route / influence receipt ID:
- Canonical SHA-256 of the reconstructed pre-review pending receipt:
- Expectation record exact pointer:
- Outcome-window record exact pointer:
- Original expectation date:
- Outcome observer:
- Learning status before review: LEARNING_PENDING_OUTCOME

The fixture-scoped executable receipt bundles the decision, route, and
influence record under one receipt ID, so one reconstructed-pending digest
checks consistency across all three without inventing parallel receipt
systems. That digest is not independent historical evidence: an implementation
that needs tamper-resistant history must resolve an independently preserved
receipt. A boolean such as `review_recorded: true` is not a link and cannot
justify `LEARNING_REVIEWED`.

## Predeclared expectation

- Expected outcome:
- Success condition:
- Abstention or escalation condition:
- Measurement window:
- Attribution boundary:

## Observed outcome

- Observed result:
- Observation time:
- Actual cost:
- Corrections or overrides:
- Context changes:
- Confounders:
- Missing outcome or incomplete observation:

## Comparison

- Expected versus observed:
- What the outcome can establish:
- What it cannot establish:
- Was the original evidence or decision record changed? It must be NO.

## Bounded update proposal

- Proposed update to query, baseline, source policy, route, threshold, or
  review rule:
- Why this single update is justified:
- What it must not change:
- New version required:
- Human disposition:
- If rejected or deferred, reason:
- Learning status after disposition: LEARNING_REVIEWED

Learning proposes a bounded update. It does not silently change policy,
overwrite evidence, or turn one outcome into causal proof.
