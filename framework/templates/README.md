# Operator templates

These templates are intentionally plain text. Copy only the fields needed for
the chosen implementation level. A template is a record shape, not a claim
that every task needs every field.

| Template | Use |
| --- | --- |
| ORDINARY_RECORD.md | End a genuine Stage-0 supplied-material transformation without layered ceremony |
| DECISION_BRIEF.md | Define the real decision, authority, baseline, budget, and outcome |
| ACQUISITION_RECEIPT.md | Record an authorized search, capture, failure, or stop |
| EVIDENCE_REGISTER.md | Link claims to exact evidence while keeping source roles distinct |
| COMPARISON_MATRIX.md | Align peers, periods, attributes, structures, and origins |
| DISCONFIRMATION_LOG.md | Challenge a leading interpretation and preserve unresolved states |
| INFLUENCE_RECEIPT.md | Record what shaped the answer and what was withheld |
| OUTCOME_REVIEW.md | Compare expectation with later outcome and propose a bounded update |
| MEMORY_RECORD.md | Preserve a scoped prior version and append a correction or supersession without overwrite |

For a low-stakes task that passes Stage 0 into a layered route, DECISION_BRIEF,
EVIDENCE_REGISTER, DISCONFIRMATION_LOG, and INFLUENCE_RECEIPT are usually
enough. A genuinely ordinary supplied-material task uses only ORDINARY_RECORD
and stops before the layered route. Add MEMORY_RECORD only when scoped prior
material is actually used. For repeated or consequential work, retain the
needed templates with stable IDs and version links; do not copy every template
merely because it exists.

An `ANSWER` or `ANSWER_PROVISIONALLY` records substantive comparison and
disconfirmation artifacts, or one bounded inactive reason for each:
comparison=`NOT_APPLICABLE`, disconfirmation=`SKIPPED`. Do not create empty
artifacts to satisfy the table. A motion claim needs two distinct authorized,
time-bearing evidence IDs with one alignment key, not a reported count.

When memory is used, hash canonical payload bytes, bind the lineage root to a
separately frozen anchor, keep one linear successor and one `CURRENT` version,
and select only `CURRENT` + `AUTHORIZED` memory. Preserve superseded records as
withheld history. These templates define reviewable records; they do not supply
runtime immutability, legal permission, or evidence that the procedure works.
