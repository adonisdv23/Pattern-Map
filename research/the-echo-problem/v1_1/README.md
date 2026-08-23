# The Echo Problem — EP v1.1 design checkpoint

**Project:** ECHO-01

**Status:** design-only; unrun; no results; not published

**Source:** EP v0.1 and the byte-preserved v15.2 protocol

**Effective checkpoint:** 2026-08-23

EP v1.1 is a design reconciliation and offline implementation checkpoint. It
does not authorize or report a model call, empirical study, pilot, participant
activity, external-dataset acquisition, preregistration, publication,
deployment, or paid-provider use.

The v15.2 protocol remains preserved under `../preserved/v15.2/`. Its bytes,
names, no-results boundary, and unfavorable-result classes are historical
evidence and are not rewritten here. This active successor makes the narrow
changes required by the Claude-package audit and the owner-approved
recommendation explicit without silently changing the historical checkpoint.

## What changed in this design checkpoint

- The canonical F0/F1/F2 controlled contrast remains unchanged. Its simple
  `DPND` / `INDP` / `UNKN` labels are stipulated experimental cues, not a claim
  that the harness discovers real-world independence.
- NEWS-COPY is an optional external validation route for same-original and
  origin-cluster recovery only. It cannot supply claim support, truth,
  `FC_cons`, VOR, or independence labels. Nonduplicate pairs remain `UNKNOWN`.
- Newswire is aggregate recurrence context only unless a later, separately
  authorized review verifies member/version and rights truth.
- Real-world measurement uses typed, graded, and uncertain dependence records;
  distinct origin labels never automatically mean independent support.
- The planning script exposes paired discordance, effect, invalidity, and
  sample-size assumptions. Its output is planning information, never power or
  effectiveness evidence from a live study.
- The offline harness has a strict parser, canonical endpoint definitions,
  content and ordered-membership hashes, exact paired McNemar logic, and a
  real-tokenizer parity solver. It contains no provider adapter or network
  path.

## Start here

- [Protocol v1.1 design checkpoint](PROTOCOL_V1_1_DESIGN_CHECKPOINT.md)
- [Targeted prior-measurement matrix](PRIOR_MEASUREMENT_MATRIX.md)
- [Offline harness README](harness/README.md)
- [Design-only QA report](../../../qa/research/ECHO_V1_1_DESIGN_CHECKPOINT_QA_2026-08-23.md)
- [EP v0.1 status and boundaries](../STATUS_AND_BOUNDARIES.md)
- [EP v0.1 future plan](../FUTURE_EXECUTION_PLAN.md)

## Evidence language

The files in this directory describe proposed definitions, deterministic local
checks, synthetic planning calculations, and open gates. A passing test means
that the local implementation satisfies its fixture contract. It does not
mean that an agent, model, retrieval system, corpus, or human reader behaves
as the fixture predicts.
