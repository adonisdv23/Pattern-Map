# Stage 0 ordinary-contract convergence QA

Status: **STRUCTURAL / PROCEDURAL QA ONLY — NOT A LIVE-AGENT OR EFFECTIVENESS RESULT**

Date: 2026-08-30

Reviewed baseline:
`0beee9add00593e77eb5aafa41fdc447c833e83c`

Branch: `codex/pattern-map-v16-final-applied`

## Scope

This pass reviewed and corrected only the applied contract under `framework/**`,
`cases/**`, and `qa/applied/**`. It inspected the Stage 0 entry points, the
ordinary record shape and fixture, implementation-level proportionality, the
focused validator, and the two neutral cases. It did not edit the locked owner
intent, site, manuscript, research, handoff, archive, or assets; call a model or
provider; run a live agent; execute a study; or perform an external action.

## Reproduced ambiguity

At the reviewed baseline, `python3 qa/applied/validate_framework.py` passed all
four focused groups. The pass did not catch either of these coexisting facts:

1. Stage 0 asked whether selection, acquisition, comparison, preservation, or
   weighing occurred *beyond* the user-supplied material.
2. The full guide and ordinary-versus-layered example treated a selective
   supplied-material summary as normally ordinary.

A summary can materially judge claims or select and withhold content entirely
inside the supplied material. The old question therefore admitted a task that
the intended ordinary escape hatch excludes, while the existing validator
still passed. This is the reproduced defect; it is a prose/contract ambiguity,
not evidence that a live agent behaved incorrectly.

## Findings and dispositions

| ID | Finding | Disposition | Correction and governing reason |
| --- | --- | --- | --- |
| SZ-01 | “Beyond supplied material” did not cover material judgment or selection/withholding within supplied inputs. | Accepted with revision | Quickstart, full guide, copied prompt, preflight, ordinary template, and implementation choices now carry one complete conjunction: ordinary is only a reversible user-supplied-material transformation with none of the seven named disqualifiers. Governing requirements: D-033/D-034 proportionality and A08 observable procedure. |
| SZ-02 | The existing four-key JSON shape was correct, but the ordinary summary fixture contradicted the narrower eligibility rule. | Accepted with revision | The shape remains exactly supplied scope, assumptions, unchecked boundaries, and output. The fixture now performs an exact reversible Markdown wrapper with no content selection or omission. The record is explicitly not an ANSWER, route, stop, learning, or influence receipt. |
| SZ-03 | Permission vocabulary was already typed, but Stage 0 needed to avoid implying action authority. | Accepted | The existing exact states `AUTHORIZED`, `UNKNOWN`, `NOT_AUTHORIZED`, and `REVOKED` remain unchanged. Each Stage 0 entry point says that Stage 0 grants no external-action authority and leaves externally consequential action with an explicitly authorized human. |
| SZ-04 | Implementation guidance bounded costs but did not state directly that available budget cannot select complexity. | Accepted with revision | The implementation choices and operational entry points now state that budget records capacity and constraint and cannot independently justify advanced machinery. Consequence, reuse, failure modes, and governance need select the smallest layered level. |
| SZ-05 | The ordinary-versus-layered guide and Signal Foundry table called uncontrolled evidence shortcuts “ordinary.” | Accepted with revision | The genuine ordinary example is now lossless supplied-material formatting. Evidence-sensitive shortcuts are labeled uncontrolled and explicitly not valid Stage 0 ordinary paths. No new route or record type was added. |
| SZ-06 | The neutral cases might have depended on the broad ordinary label. | Accepted — no file change | `cases/general-research/README.md` already performs claim-level source weighing, comparison, disconfirmation, and permission-bounded recommendation; `cases/product-and-process/README.md` already performs comparison, permission resolution, motion/absence judgment, and a proposed learning loop. Both correctly remain layered and require no correction. |

## Contract checks added

The focused validator now:

- requires the complete ordinary eligibility, terminal-record, and separate
  human-action-authority language in Quickstart, full guide, copied brief,
  preflight, ordinary template, and implementation choices;
- rejects the former beyond-supplied gate and the former default treatment of
  supplied-material summarization as ordinary;
- requires exactly four ordered ordinary-template fields;
- exercises a QA-only truth table with one valid exact transformation and a
  separate fail-closed mutation for irreversibility, material outside the
  supplied input, material claim judgment, comparison within supplied input,
  selection/withholding within supplied input, permission resolution, memory
  reuse, new acquisition, and externally consequential influence;
- rejects a supplied-material summary carrying material judgment and
  selection/withholding;
- rejects evidence, ANSWER route, stop, outcome/learning, influence, or family
  additions to the ordinary JSON record; and
- requires the budget/complexity boundary in the implementation and copied
  operating entry points.

The truth table is a focused prose-contract test. It is not a universal runtime
router, score, store, queue, adapter, or claim that every downstream system
must use this JSON fixture.

## Checks

| Check | Result |
| --- | --- |
| `python3 qa/applied/validate_framework.py` | PASS — six-family, inventory, Stage 0, receipt, and fail-closed mutation groups |
| `python3 -m json.tool qa/applied/receipts/ordinary-supplied-material.json` | PASS |
| `(cd docs && shasum -a 256 -c OWNER_INTENT_V16.sha256)` | PASS — `OWNER_INTENT_V16.md: OK` |
| `git diff --check` | PASS |
| Owned-path status audit | PASS — every changed path is under `framework/**`, `cases/**`, or `qa/applied/**` |

## Evidence ceiling

These checks establish only that the edited artifacts carry the same Stage 0
boundary and that selected malformed contract fixtures fail closed. They do not
establish that an agent will follow the text, that a permission assertion is
legally valid, that a decision or answer is correct, that the framework improves
outcomes, that the neutral cases are effective, or that any research result
exists. No live-agent compliance, reader-comprehension, product-behavior, or
effectiveness result is claimed.
