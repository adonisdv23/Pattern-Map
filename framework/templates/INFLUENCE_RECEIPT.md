# Influence receipt

This receipt is the compact answer to: what shaped the output, what was
withheld, and why?

## Packet identity

- Receipt ID:
- Decision ID / brief version:
- Packet ID / version:
- Output ID / version:
- Operator / model / tool:
- Human reviewer:

## Influence summary

- Intended output:
- Allowed disclosure:
- Human action boundary:
- Main uncertainty:
- Route:
- Stop status and reason:

## Selected material

| Item ID | Claim or decision role | Exact span / pointer | Why admitted | What it supports | What it cannot establish | Permission |
| --- | --- | --- | --- | --- | --- | --- |
| E-001 | SUPPORTS / QUALIFIES / CONTRADICTS / FRAMES / ROUTES |  |  |  |  | AUTHORIZED |

## Withheld material

| Item ID | Reason withheld | Still inspectable? | Could change conclusion? | Re-entry condition |
| --- | --- | --- | --- | --- |
| E-002 | DUPLICATE / INSUFFICIENT / NOT_AUTHORIZED / SENSITIVE / OUT_OF_SCOPE / STALE / UNKNOWN |  |  |  |

Only `AUTHORIZED` material may appear in Selected material. `UNKNOWN`,
`NOT_AUTHORIZED`, and `REVOKED` material belongs in Withheld material.
Withholding is not deletion. Provenance is not correctness. A selected item is
allowed to influence this bounded output; it is not permanently trusted or
authorized for external action. If permission to use an item has not been
established, preserve `UNKNOWN` until an authorized person or policy resolves
its use. A selected memory item must also be `CURRENT`; retain a `SUPERSEDED`
version only as withheld history.

Selected memory IDs must exactly match memory_use.record_ids; NOT_USED permits
no selected memory; a used memory record cannot also be withheld. The
memory-use, selected-item, and withheld-item ID lists must contain no
duplicates; selected non-memory evidence remains valid.

This withheld-material table assumes the top-level operation is authorized and
individual items have different states. In the current single-global-permission
receipt, top-level `UNKNOWN`, `NOT_AUTHORIZED`, or `REVOKED` leaves both
Selected and Withheld empty; it does not disclose blocked material to explain
why it was blocked.

## Output boundary

- Observations:
- Interpretations:
- Recommendations:
- Explicit unknowns:
- Abstention or caveat wording:
- External action requiring human authority:

## Disposition

- ACCEPTED / REJECTED / DEFERRED / OVERRIDDEN / REQUEST_ENRICHMENT:
- Decision maker and authority:
- Reason:
- Version or correction link:
