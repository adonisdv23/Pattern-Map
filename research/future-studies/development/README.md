# Development cases and candidate pilot packets

These are deliberately authored synthetic materials, not collected data, model
outputs, participant observations or empirical results. `DISCOVERY_CASES.json`
contains four decision cases with explicit counterexamples and removal tests.
`observation_cases.py` constructs six observation cases and 12 candidate pilot
packets, with hidden-world keys separate from model payloads. Running the script
only validates design invariants and an intentionally invalid oracle control.
It invokes no network or model.

```sh
python research/future-studies/development/observation_cases.py
```

The candidate payload digest binds the deterministic packet definitions. These
are **not approved frozen pilot materials**. An independent reviewer must check
the semantic equality of prose and structured views, the expected observation
universe and accepted decisions. The two currently generated surface forms
reverse field/sentence order; they are an order robustness check, not independent
paraphrases. Independently authored surface forms remain required by the pilot
proposal before execution. Candidate domains are intentionally easy to inspect;
success on them would not establish transfer to open-world work.

There is no runner or provider selection. A future runner must receive only
`model_payload`, never the full case, oracle keys, case names or repository
access. Hash the finalized independent surface forms and keys separately before
calls. Use the common instruction and error rubric in the research proposal.
The schema cannot prove semantic equality or key correctness. The validation
message means only that the specified mechanical invariants and negative
control behaved as intended.
