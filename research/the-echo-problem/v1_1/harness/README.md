# EP v1.1 offline harness

This is a provider-free, standard-library Python scaffold for design audits.
It is not the preserved v15.2 harness and does not replace it. The preserved
bytes remain under `../preserved/v15.2/`.

## What is implemented

- strict four-field JSON parsing with duplicate-key rejection and no repair;
- canonical `FC_cons` and fixed-set `VOR` scoring, with invalid/valid
  decomposition;
- separate full-content and ordered-membership SHA-256 receipts;
- exact paired McNemar/binomial p-values;
- deterministic paired power/MDE surface across discordance, effect, and N;
- context-sensitive exact parity search using a caller-selected tokenizer;
- optional `tiktoken` loading only when explicitly requested by a local test.

There is deliberately no provider adapter, network import, dataset loader,
credential path, retry path, or model runtime. A raw model output cannot enter
the harness through an implicit call; callers must provide bytes explicitly.

## Local checks

From the repository root:

```sh
python3 -m unittest discover -s research/the-echo-problem/v1_1/harness -p 'test_*.py' -v
python3 research/the-echo-problem/v1_1/harness/planning.py \
  --output /tmp/echo-v1-1-planning.json --repetitions 10000 \
  --invalidity-pair 0,0 --invalidity-pair 0.02,0.05
```

The second command is a synthetic planning calculation. Its output must retain
the `planning_only_no_model_or_corpus_outputs` status and must never be cited
as a study result. Invalidity pairs are explicit and repeatable; `0,0` is the
default when no pair is supplied, so an unrequested sweep cannot silently
multiply the planning workload.

For a real BPE parity audit, install `tiktoken` in a temporary environment and
run the optional test. The selected model/checkpoint/tokenizer/chat template
receipt remains a future gate; this local encoding check does not authorize a
model run.

## Recorded real-tokenizer audit

On 2026-08-23, the optional test was run in an ephemeral `uv` environment with
`tiktoken 0.14.0`, encoding `cl100k_base`, 100,256 mergeable ranks, and the
encoding-table fingerprint
`5af8a02a651e9db4366b5b14c2cc8f506d721ebdab0db3294337dd8ba15c4528`.

The checked fixture
`../fixtures/CLAUDE_PRIMARY_RENDER_AUDIT_SEED1_N300.json` contains the 300
F1/F2 prompt pairs produced by Claude's supplied `oa.generate.generate_set`
and `oa.conditions.render` path for `seed=1`. It records the source archive
SHA-256, exact generator and renderer hashes, report order, report-text hashes,
render hashes, base token counts, and rendered bytes. The fixture itself has
SHA-256
`98b29d886a839e8adada99737d6a001e269f21b2dbea89f1d5bbf09091f131e8`.

The new bounded solver achieved exact F1/F2 parity for all 300 pairs. The
unpadded F2-minus-F1 difference was not a constant: its observed values were
`[-7,-6,-5,-4,-3,-1,0,1,3,4,5,6,7,8]`, and the final equal count ranged from
292 to 486 tokens. The render receipt is
`a056878990dfb0bcc8ab0af24e20ed5d757c3fdc07c7c3377faa06e4c892fd82`.
These are synthetic prompt-rendering implementation checks, not a selected
model/chat-template receipt and not a research result.

`generate_claude_primary_fixture.py` can reproduce the checked fixture only
when it is given the exact owner-supplied archive and extracted package root.
It verifies the archive hash before importing the advisory generator. A replay
against the supplied archive produced byte-identical fixture output.

The optional test is skipped when `tiktoken` is unavailable; that skip is not a
parity pass. Claude's older solver is separately recorded as failing real-BPE
parity: its suite was 3 failed / 6 passed, with representative one-token
mismatches 386/387, 402/403, and 390/391. Broader diagnostic enumerations found
44/300 failures at seed 1, 22/120 at seed 3, 10/60 at seed 5, and 38/200 at
seed 8. Those failures motivated the new solver; they are not silently
relabelled as EP v1.1 research results.
