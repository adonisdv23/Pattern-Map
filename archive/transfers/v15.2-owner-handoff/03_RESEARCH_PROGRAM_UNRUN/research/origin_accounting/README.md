# Offline origin-accounting implementation scaffold

This directory contains the machine contracts and frozen configuration for
the F0/F1/F2 protocol. It is design-time infrastructure only. No model,
provider, network, Cloud Run job, paid service, or human-participant workflow
is called by the implementation.

The standard-library implementation lives in
[`tools/origin_accounting/`](../../tools/origin_accounting/). The canonical
offline smoke command is:

```sh
python3 -m tools.origin_accounting.cli smoke --out /private/tmp/oa-smoke
```

It emits a four-structure smoke corpus, F0/F1/F2 prompt instances, split and
surface diagnostics, and an immutable local receipt. Use `generate --out`
without `--small` only when a protocol-sized synthetic artifact is needed.

The committed config keeps `model_id=UNSELECTED` and
`tokenizer_revision=null`. Prompt parity is checked with the explicitly
labelled `deterministic-regex-surrogate-v1`; this surrogate cannot authorize a
primary model run. A publication/release lock requires the intended frozen
model tokenizer and an independent RFC 8785 conformance check.

The schema files are JSON Schema Draft 2020-12 contracts with
`additionalProperties=false` on every record. Cross-record graph, split,
unknown-origin, parity, and denominator invariants are enforced by the
scaffold and should be rechecked by an independent validator before any
primary run.

## Descriptive scorer metrics

The offline scorer keeps the locked `FC_cons` primary endpoint and fixed-set
`VOR` safety gate unchanged, while returning a separate descriptive sidecar.
For valid outputs on certified, non-contested support-origin rows it reports
absolute origin-count error and selected supporting-origin-set
precision/recall/exact match. These origin metrics inspect only selected
reports whose benchmark stance is `supports`. The output contract defines
`evidence_ids` as reports used for the assessment, so neutral or refuting
selections are preserved and are not treated as support-selection errors.
Contested rows remain visible as a separate scope but are not scored for a
support-only set. Invalid outputs and unknown-origin rows remain undefined for
the support-origin diagnostics; they are never silently imputed.

When no selected supporting origins exist, support-origin precision is
undefined (`None`), not zero. When the certified gold support-origin set is
empty, recall is undefined; exact-set match remains `1` when both sets are
empty.

The generator invariant makes every `stance=supports` report part of the
restricted support set, so a wrong-stipulated-origin fixture is not logically
possible without breaking that contract. No false-origin or misassignment
metric is emitted; the retained set metrics expose omission and exact-set
coverage only.

The paired analysis exposes the same measures under
`secondary_descriptive`, with scope summaries that keep certified
non-conflict, certified conflict, unknown, and invalid rows distinct. These
fields are descriptive audit outputs only and cannot change the primary
contrast, safety denominator, confirmatory decision, or the protocol's
no-model/no-provider boundary.
