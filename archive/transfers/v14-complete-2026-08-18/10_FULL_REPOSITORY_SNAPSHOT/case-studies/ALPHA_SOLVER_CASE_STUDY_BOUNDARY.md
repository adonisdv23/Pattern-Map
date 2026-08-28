# Alpha Solver case-study boundary

Status: bounded read-only case-study input. Alpha Solver is not evidence that the full framework works.

Observed repository revision: `e7a6baa93627c9ef1e27f0660bd4913262267ea2`

The listed source files were unchanged relative to that revision when inspected. Other pre-existing Alpha Solver working-tree changes were preserved and not examined as case-study evidence.

## What Alpha Solver may illustrate

Alpha Solver describes itself as a reasoning and routing layer with gates, scoring, optional tool calls, observability/replay, determinism, and budget controls. Those features can illustrate a bounded downstream portion of the discrimination framework:

- asking a clarifying question when an objective is underspecified;
- stopping before an unsupported or unsafe completion;
- routing among answer, refusal, clarification, and evidence request;
- preserving why a route or stop occurred;
- exposing an evidence gap rather than filling it with fluent conjecture;
- replaying a decision path;
- constraining computation with a budget guard;
- designing evaluations that include ordinary controls so restraint is not rewarded indiscriminately.

The strongest concise formulation in the inspected materials is that the desired output may be “the refusal plus the evidence path.” That is an implementation aspiration in an illustrative packet, not an observed result.

## Exact evidence boundary

| Artifact | What it establishes | What it does not establish | SHA-256 |
| --- | --- | --- | --- |
| `/Users/gpt/Documents/Codex/projects/Alpha-Solver/README.md` | The repository's stated architecture, status, and non-production maturity. | Effectiveness, superiority, or the historical origin of v13. | `b336076614db0f0f0ecd1c7a66a969730b68f7ef13327c2a4b2d74447edb4b4f` |
| `/Users/gpt/Documents/Codex/projects/Alpha-Solver/docs/evals/runs/alpha-solver-discrimination-layer-demo-pack-001/README.md` | A ten-scenario, docs-only demo design with an explicit `DEMO_PACK_CAPTURED_NOT_EXECUTED` verdict. | Executed behavior, scores, benchmark results, or validation. | `48f773d4f77b190a383f0e72386953698ff1a2da78e733fdc3727d085efae2e6` |
| `/Users/gpt/Documents/Codex/projects/Alpha-Solver/docs/evals/runs/alpha-solver-discrimination-layer-demo-pack-001/presenter-script.md` | Intended narrative and claim-safety language. | Evidence that the intended behavior occurs. | `00433fc5e11731a2f73f78a98cd9360b7deb3d05ed65503d97e62084172b4f4d` |
| `/Users/gpt/Documents/Codex/projects/Alpha-Solver/docs/evals/runs/alpha-solver-manual-discrimination-value-read-001/README.md` | A 15-task comparison design whose runtime and simulation tracks were not run. | Any value claim; the packet's verdict is `STOP_INCONCLUSIVE`. | `af06c539ba61b272fb5f9f500fc9432ab9844ab268eac748d809a82452bdef86` |

## Relationship to the framework

Alpha Solver sits downstream of an evidence boundary in the clearest available product contracts. It may consume a bounded context or evidence packet, reason about a question, and produce derived analysis. It does not become the authority for the original evidence and may not erase exclusions, provenance, or guard status.

This makes Alpha Solver useful for illustrating:

`bounded context → route/clarify/withhold/reason → derived result → human review`

It is not sufficient to illustrate the entire upstream process of acquisition, artifact identity, provenance capture, common-origin analysis, claim/evidence construction, and source preservation.

## Claims that remain prohibited

- Alpha Solver implements the whole discrimination layer.
- Alpha Solver invented the discrimination-layer concept.
- Its current runtime reliably knows when not to answer.
- The demo pack proves better decisions, safer output, or lower unsupported-claim rates.
- The design packet is benchmark, provider, or production evidence.
- Alpha Solver validates general AI reasoning, enterprise readiness, or the v14 framework.
- Alpha Solver output may replace or rewrite original evidence.

## Missing evidence

The historical migration packet is missing, so Alpha Solver's exact relationship to the owner-originated v13 concept cannot be reconstructed. The inspected demo and value-read packets are later implementation-context documents. They must not be back-projected into v13 as if they were original authorial intent.

The next research step, if separately authorized later, would be a matched, blinded comparison on defined tasks with ordinary controls, explicit costs, evidence-grounded outcomes, and measures for both under-discrimination (unsupported completion) and over-discrimination (unhelpful refusal). No such study was performed here.
