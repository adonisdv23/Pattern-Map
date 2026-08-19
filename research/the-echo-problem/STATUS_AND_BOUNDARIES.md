# EP v0.1 status and evidence boundary

**Status:** `PRESERVED_SUCCESSOR_UNRUN_NO_RESULTS_NOT_PUBLISHED`
**Source package status:** `LOCAL_OWNER_REVIEW_NO_EMPIRICAL_RESULTS_NOT_PUBLISHED`
**Source commit:** `36568cb6e8afce9544606c968319b063fc9b79ce`
**Accession:** `archive/transfers/v15.2-owner-handoff/`

## Explicit no-results declaration

No model study, empirical study, pilot, or participant study has run for EP
v0.1. No model or provider was called by this curation. No participants were
contacted or enrolled. No external dataset was acquired. The preserved v15.2
package is a protocol-and-implementation checkpoint, not a result.

The source manifest records design image generation and model-assisted
editorial review as having occurred in the historical package; it explicitly
labels both as not empirical evidence. Preserving those records does not turn
them into study outcomes.

## Preserved source boundary

The accession contains the manifest-listed v15.2 payload exactly: 239 files and
48,717,432 payload bytes. Its external manifest and ZIP sidecar are copied
unchanged. The exact 41,436,496-byte ZIP container remains outside Git at the
verified local source path and is checked by the accession verifier when that
path is supplied. The source ZIP is not split or re-created here.

Historical source validation metadata is retained as metadata, not reissued as
new evidence:

| Source field | Preserved value |
| --- | --- |
| Empirical results present | `false` |
| Empirical study/model/provider calls | `0` |
| Participants | `0` |
| External dataset acquisition | `false` |
| Confirmatory conditions | Planned `F0`, `F1`, `F2`; not run |
| Planned primary cases | `300`; planning value, not a denominator with results |
| Planned fixed safety subset | `75`; planning value, not a result |
| Static site and route tests | `PASS` in the source package record |
| Offline harness tests | `PASS` in the source package record |
| PDF page render review | `PASS` in the source package record |
| Manual browser/assistive technology | Explicit owner residual in the source package record |

## Unfavorable-result classes retained

The following classes are preserved as possible outcomes, stopping reasons, or
analysis categories. They are **not observed results** in EP v0.1, because no
study ran:

| Canonical source token | Plain-language reading |
| --- | --- |
| `null` | no meaningful difference or support under the planned comparison |
| `rule_only` | an apparent effect is fully attributable to the rule or implementation |
| `invalidity_driven` | invalid, malformed, or inadmissible outputs drive the apparent result |
| `threshold_only_vor` | a value-of-research threshold is crossed without broader evidence |
| `harmful` | the intervention creates or increases a material risk |
| `shortcut_driven` | a shortcut, artifact, or surface cue explains the apparent effect |
| `surface_or_semantic_audit_failure` | surface checks or semantic review fail |
| `unstable` | the result changes materially across permitted runs or slices |
| `noise_fragile` | the apparent result disappears under small noise or perturbation |
| `nontransfer` | the behavior does not transfer beyond the bounded setup |
| `stopped_or_quarantined` | the run is stopped or held from interpretation for safety or validity |

These categories protect against selective reporting. A null, harmful,
shortcut-driven, unstable, non-transfer, or stopped outcome remains a valid
planned outcome; it is not a failure of the recordkeeping process.

## Action boundary

The current branch performs preservation, local verification, and offline
source checks only. It does not deploy, publish, create a Release, preregister,
spend, acquire data, contact people, or imply that unrun research produced a
result.
