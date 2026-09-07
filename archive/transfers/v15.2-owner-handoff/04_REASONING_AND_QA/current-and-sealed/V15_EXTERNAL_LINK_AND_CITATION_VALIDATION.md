# V15 external-link and citation-status validation

- **Checked:** 2026-08-18 (America/New_York)
- **Scope:** canonical manuscript, prior-art delta, T1 feasibility audit,
  reference ledger, and reader citation source
- **Verdict:** `PASS_WITH_DISCLOSED_AUTOMATION_BLOCKS`
- **Empirical status:** link and bibliographic validation only; no model result,
  dataset acquisition, or publication action

## 1. Scope and method

The check deduplicated HTTP(S) targets found in:

- `source/THOUGHT_PIECE_V15.md`;
- `research/PRIOR_ART_DELTA_V1.md`;
- `research/REAL_SYNDICATION_TRANSFER_FEASIBILITY_V1.md`;
- `research/REFERENCES.md`; and
- `site/app/content.ts`.

There were **131 unique targets**. Each received a public read-only request
with redirects enabled, a 25-second timeout, a bounded byte range, and no
authentication. Non-2xx responses were then separated into DOI-resolver,
publisher bot-policy, official-site bot-policy, and repository-server cases.
Primary records with ambiguous automated responses were independently opened
or located through the browsing surface. No paid API, private account, external
dataset download, message, or mutation was used.

This is a current reachability and status receipt. It is not a promise that an
external host will remain available or that every publisher permits automated
access from every network.

## 2. Reachability result

| Class | Count | Interpretation |
| --- | ---: | --- |
| Direct 2xx after redirects | 110 | Target returned content to the bounded automated request |
| DOI resolver succeeded; publisher denied automated range request | 16 | `doi.org` returned an exact 302 destination; the publisher destination returned 403 to this client |
| Official BMJ/HHS page denied curl but was independently located/opened | 3 | Host policy, not a missing citation target |
| ETH repository returned 500 to curl but exact record/PDF was independently indexed and content-checked | 2 | Repository automation/server limitation, not evidence of a missing record |
| Transport failure or timeout | 0 | None |
| 404 / 410 | 0 | None |

All 131 targets therefore had either a direct successful response, a working
DOI resolver, or an independent exact-record confirmation. No link required a
canonical-source replacement during this pass.

## 3. DOI destination blocks

The following DOI URLs each returned an exact `302` resolver destination before
the publisher returned `403` to the automated range request:

```text
10.1001/jama.2012.87802
10.1002/asi.20672
10.1037/0033-295X.106.4.643
10.1111/j.1468-0017.2010.01394.x
10.1126/science.1193147
10.1136/bmj.b2680
10.1145/290941.291025
10.1145/3290605.3300233
10.1145/3449287
10.1145/3586183.3606763
10.1145/3772318.3791101
10.1177/001316446002000104
10.1287/orsc.1050.0133
10.14778/1687627.1687690
10.14778/1687627.1687691
10.3233/SW-233467
```

These are recorded as `RESOLVER_OK_DESTINATION_AUTOMATION_DENIED`, not as
direct 2xx successes and not as broken links.

## 4. Direct-site automation exceptions

| Target | Automated result | Independent confirmation | Disposition |
| --- | --- | --- | --- |
| BMJ PRISMA 2020 article | 403 | Exact title, BMJ 2021 citation, DOI, author list, and canonical article/PDF located through the browsing index | Keep; `OFFICIAL_RECORD_CONFIRMED_BOT_DENIED` |
| HHS Belmont Report | 403 | Exact official HHS page opened; title and current official content present | Keep; `OFFICIAL_RECORD_CONFIRMED_BOT_DENIED` |
| HHS 45 CFR 46 | 403 | Exact official HHS page opened; current 45 CFR 46 navigation present | Keep; `OFFICIAL_RECORD_CONFIRMED_BOT_DENIED` |
| ETH Strittmatter et al. record | 500 | Exact repository record located with title, authors, 2024 conference-paper status, open-access label, and CC BY 4.0 notice | Keep; `PRIMARY_RECORD_CONFIRMED_REPOSITORY_LIMITATION` |
| ETH Strittmatter et al. PDF | 500 | Exact 622 KB published-version PDF indexed; title and authors match the source card | Keep; `PRIMARY_PDF_CONFIRMED_REPOSITORY_LIMITATION` |

The exception labels deliberately preserve the observed HTTP behavior instead
of converting an independent confirmation into a claimed curl 2xx response.

## 5. Citation-status audit

`research/PRIOR_ART_DELTA_V1.md` contains **19** numbered source cards, S1–S19.
Static structure checks found exactly 19 instances of every required field:

- sourced fact;
- exact finding used;
- project inference;
- claim blocked;
- residual contribution; and
- accept/modify/defer/reject disposition.

The publication ledger remains intentionally mixed and explicit:

| Status class | Records | Count |
| --- | --- | ---: |
| Published papers or conference contributions | S1–S4, S6–S7, S9, S11–S13, S18–S19 | 12 |
| Unreviewed working manuscripts or preprints with no checked acceptance | S5, S8, S10, S15–S16 | 5 |
| ArXiv record reporting ACL acceptance while an ACL publication page was not located in the bounded pass | S14 | 1 |
| Current official methods handbook chapter | S17 | 1 |

The published Zhang, Ives, and Roth ACL 2020 page was opened directly and
confirmed the title, authors, venue, year, pages, DOI, abstract, and PDF link.
The published Dong, Berti-Équille, and Srivastava PVLDB PDF was opened
directly and confirmed the copied-source/truth-discovery setting used by the
project. NEWS-COPY and Cochrane official records also opened directly.

No preprint was promoted to peer-reviewed status. S14 retains its qualified
language. No current citation status supports a “first,” “nobody has studied
this,” provenance-ground-truth, or generic mechanism-novelty claim.

## 6. Gate decision

**PASS WITH DISCLOSED AUTOMATION BLOCKS.** There are no observed 404/410 links,
no transport failures, and no citation-status promotion defect. Twenty-one
targets did not return direct 2xx content to the bounded curl client, but all
were resolved or independently confirmed with their limitation preserved. The
prior-art novelty boundary and descriptive T1 licensing cautions remain
unchanged.
