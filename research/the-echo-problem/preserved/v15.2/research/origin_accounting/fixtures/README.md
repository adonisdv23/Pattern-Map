# Deterministic fixtures

Fixtures are generated in memory by the standard-library package rather than
checked in as mutable model outputs. `generate_corpus(..., small=True)` emits
one bundle per origin structure in each split; the parser fixture suite emits
18 strict valid/invalid raw byte cases, including duplicate keys, malformed
UTF-8, unknown evidence IDs, non-finite numbers, code fences, and leading or
trailing prose.

The `relation_noise_fixture()` helper covers `DPND`, `INDP`, and `UNKN` with a
deterministic 20% perturbation while leaving gold relation metadata untouched.
Smoke artifacts are receipts, not efficacy data and must not be included in a
primary denominator.
