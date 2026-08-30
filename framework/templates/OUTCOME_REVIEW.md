# Outcome review

Complete after the defined outcome window, not by hindsight.

## Executable state boundary

- `LEARNING_PLANNED`: `applicable` is true, but both
  `expectation_recorded` and `outcome_window_recorded` are false. No observed
  outcome, review, disposition, or applied update field is permitted.
- `LEARNING_PENDING_OUTCOME`: the expectation and outcome window are both
  recorded before the event. No observed outcome, review, disposition, or
  applied update field is permitted.
- `LEARNING_REVIEWED`: the locked expectation/window, recorded review,
  observed-or-explicitly-missing outcome, and human disposition are present.
  `update_applied` remains false; the record proposes an update but does not
  apply it.
- `LEARNING_NOT_APPLICABLE`: `applicable` is false and the object contains no
  expectation, result, review, disposition, or update fields.

Missing or mistyped applicability is invalid. A result or human disposition
cannot be carried backward into a planned, pending, or non-applicable state.

## Link to original record

- Outcome review ID:
- Decision ID / brief version:
- Original route receipt:
- Original influence receipt:
- Original expectation date:
- Outcome observer:
- Learning status before review: LEARNING_PENDING_OUTCOME

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
