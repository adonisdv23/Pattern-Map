# Real Syndication Transfer Feasibility v1

**Program:** Discrimination Layer v15, Lane 2

**Audit order:** NEWS-COPY first; Newswire second

**Prepared:** 2026-08-18

**Status:** read-only feasibility research; no dataset, paper supplement, model,
paid service, or licensed artifact was downloaded into this worktree; no model
run, publication, deployment, or external contact occurred.

**Disposition: include as descriptive T1**

Here, **T1** means an optional, separately named transfer tier for descriptive
transport and boundary testing. It is not a new model condition, not `F3`, and
not an extension of the confirmatory or safety analysis. The current protocol
must keep the fictional `F0`/`F1`/`F2` study and its denominators intact.

## Answer first

NEWS-COPY and Newswire are useful for a constrained descriptive transfer check:

- NEWS-COPY is the stronger source for testing whether an adapter preserves a
  documented **same-original/reproduction** relation and refuses to turn a
  nonduplicate label into an independence label.
- Newswire is the stronger source for a publicly documented historical wire
  corpus with aggregate reproduction metadata, but its released rows collapse
  each inferred reproduction cluster to one selected article and explicitly
  provide no instance-to-instance relation labels.
- Neither resource supplies the complete claim, stance, support-origin, and
  relation-certification manifest required by the current false-corroboration
  protocol. Neither can provide confirmatory `FC_cons`, safety `VOR`, or a
  real-world independence claim without a documented protocol amendment.
- The four current operational relation values remain `DPND`, `INDP`, `UNKN`,
  and `NONE`. For public transfer data, `INDP` is unavailable by default.
  A nonduplicate, different URL, different newspaper, different byline, or
  different wording maps to `UNKN` unless a separate source-to-source
  derivation audit documents otherwise.
- The strict output object transports unchanged as a parser/interface contract.
  The endpoint transports only as a descriptive audit over a separately pinned
  transfer manifest; it does not acquire a confirmatory denominator merely
  because a public row has a `cluster_size`, duplicate label, or source name.

The decisive positive case for including T1 is that the two resources expose a
real, operationally important failure boundary—recurrence and textual reuse
are observable, while independence, claim stance, and truth are not. The
decisive constraint is that real syndication data cannot be promoted to the
stipulated synthetic graph used by the first paper.

## 1. Boundary and evidence-status legend

This audit follows the v14 protocol and the current v15 task boundary:

- No text or image dataset was downloaded or redistributed.
- No model, paid provider, live retrieval, or external service was run.
- The case-study boundary remains unchanged: Signal Foundry is an evidence-
  discipline illustration, not validation; Alpha Solver is a downstream,
  docs-only illustration, not validation.
- T1 records, if later built, must remain outside the fictional `dev`, `pilot`,
  `primary`, and `stress` splits and outside the `A` and `M` denominators.

Labels used below:

- **Verified dataset fact** — stated in the named paper, official dataset card,
  or official repository read during this audit.
- **Operational inference** — a proposed adapter interpretation derived from
  those facts and the current protocol; it is not a label supplied by the
  dataset.
- **Unknown** — not established by the reviewed source; preserve as unknown
  rather than filling the gap with a similarity, source-count, or URL heuristic.

## 2. Current protocol contract that T1 must not change

### 2.1 Synthetic conditions and exact relation vocabulary

The current first-paper question is whether a frozen model uses a supplied
origin-relation field beyond an identical rule-only condition. The conditions
are:

| Condition | Input difference | Meaning |
| --- | --- | --- |
| `F0` | Citation/source IDs only; no rule or relation cue | Ordinary bounded evidence assessment |
| `F1` | Explicit rule: count distinct origin pathways, do not count repeated reports as independent, preserve unknown | Rule-only comparator |
| `F2` | Byte-identical `F1` rule plus a fixed relation field | Supplied/oracle relation-cue condition |

The relation codebook in the locked prompt is:

| Code | Operational meaning | Public-transfer default |
| --- | --- | --- |
| `DPND` | The report is dependent on another observed report or origin path | Permitted only when a same-origin/derivation path is documented; otherwise `UNKN` |
| `INDP` | A separate origin **as stipulated by the synthetic benchmark** | Not available from source count, URL, publisher, wording, or a nonduplicate label |
| `UNKN` | Origin relation is not certified; do not count as independent | Default for uncertified public relations |
| `NONE` | No relation cue supplied in the slot | Used for the no-cue conditions |

`INDP` is intentionally narrower than the everyday word “independent.” It
means separate origin nodes in the synthetic graph, not real-world causal,
epistemic, methodological, or editorial independence. The adapter must not
rename public records `INDP` merely because they are nonduplicates.

### 2.2 Output object and endpoint

The strict output object remains:

```json
{
  "origin_count_supporting": 0,
  "claim_state": "supported | refuted | insufficient | contested",
  "confidence": 0.0,
  "evidence_ids": ["opaque_id"]
}
```

The parser must continue to reject malformed JSON, unknown keys, duplicate
keys, invalid types, out-of-range values, duplicate/unknown evidence IDs, and
manual repair or retry after lock. `origin_count_supporting` remains the
model's separate count assertion. It must not be reconstructed from
`claim_state`, citations, cluster size, or selected evidence.

The current primary event is:

```text
FC_obs(i,c) = 1[valid(i,c)
                  AND hat_n_i >= 2
                  AND gold_support_origin_certainty_i in {none,single,unknown}]

FC_cons(i,c) = 1[NOT valid(i,c) OR FC_obs(i,c)=1]
FC_lib(i,c)  = 1[valid(i,c) AND FC_obs(i,c)=1]
```

The primary contrast is the all-assigned paired `F2` versus `F1` contrast over
the fixed fictional set `A` of 300 bundles. The safety set `M` is the fixed
manifest subset whose certified supporting-origin state is `multiple`; invalid
outputs are `VOR=0`, and `M` is never replaced by a post-run valid-output set.

For T1, the same formulas can be used as a **descriptive adapter diagnostic**
only if the transfer manifest declares what its certification state means. The
following are prohibited under the current protocol:

1. adding a transfer condition named `F3`;
2. appending transfer rows to fictional `A` or `M`;
3. using T1 rows in the primary confidence interval, McNemar test, power
   calculation, or VOR non-inferiority decision;
4. treating a transfer `multiple` label as a reason to enlarge or alter `M`;
5. describing descriptive `FC_obs` or claim-state results as evidence of
   provenance discovery, truth, source authority, or general model behavior.

If the transfer is run at all, it gets a distinct split ID, dataset/version
receipt, license record, source-to-record manifest, and descriptive report.
It must be created after the primary prompt and analysis locks, consistent with
the current operationalization specification.

## 3. Audit 1 — NEWS-COPY

### 3.1 Primary-source status

| Source | Status as of 2026-08-18 | What was verified | License/handling status |
| --- | --- | --- | --- |
| [Noise-Robust De-Duplication at Scale, arXiv HTML](https://arxiv.org/html/2210.04261) | Version 2, 2024-04-24; primary dataset paper | Dataset construction, duplicate definition, sampled dates, annotation procedure, error modes, and reported metrics | The paper page is CC BY for the paper; this does not by itself clear the data release |
| [Official NEWS-COPY repository](https://github.com/dell-research-harvard/NEWS-COPY) | Public repository; primary code/data index | README states 27,210 documents, 122,876 positive duplicate pairs, and links to the historical-news download | README names no dataset license; no repository `LICENSE` file was found at the reviewed main path |
| [NEWS-COPY README](https://github.com/dell-research-harvard/NEWS-COPY/blob/main/README.md) | Read-only official README | The historical data and pre-trained-model download is a linked external Dropbox resource | No download followed; external data terms were not assumed |
| [NEWS-COPY evaluation mirror](https://huggingface.co/datasets/chenghao/NEWS-COPY-eval) | Third-party/secondary mirror; current page was readable | Evaluation/test fields include article text and cluster/duplicate fields; page reports 19,199 rows across test/validation | Dataset card says `license: unknown`; mirror is not treated as canonical or redistributed |

The official paper and repository agree on the broad counts, but the public
release path does not provide a clear data license in the reviewed materials.
The Hugging Face mirror explicitly reports an unknown license. This is a
release blocker for copying or redistributing article text, labels, or derived
records, even though the paper describes the newspaper scans as off-copyright.

### 3.2 Verified dataset facts

The following are facts stated by the primary paper or official repository:

- NEWS-COPY contains 27,210 historical newspaper articles drawn from 973
  newspapers and dated 1920–1977.
- It contains 122,876 positive duplicate pairs. The full-day evaluation samples
  include 1930 and 1974 test material, with a 1955 validation sample; the paper
  also describes training material spanning the period.
- The full-day construction reviewed every front-page article for the selected
  days, including singletons, after candidate clustering and manual review.
- The data were extracted from newspaper scans with layout detection and OCR.
  Headlines were locally written and were generally not included in the paper's
  NEWS-COPY article representation because they were rarely reproduced.
- Weather forecasts, incorrectly merged article boxes, and multi-story news
  summaries were removed or hand-filtered where no single ground-truth cluster
  was available.
- The paper defines a duplicate as an article that came from the **same
  original source article**, regardless of abridgement or OCR noise.
- Articles from different source articles that share a quote are labeled
  nonduplicate. Different articles about the same larger story, and updated
  articles containing breaking news, are also labeled nonduplicate.
- In a doubled-label subset of 8,512 pairs, reported interannotator agreement
  was 98.1% raw agreement and 90.9 Cohen's kappa.
- In the paper's test evaluation, the neural bi-encoder reached ARI 91.5 and
  the reranking method reached ARI 93.7; these are strong duplicate-clustering
  results, not perfect provenance recovery.
- The paper reports that neural false positives commonly involve repeated
  quotes, different articles about the same story, or an updated article. It
  reports false negatives under severe OCR or abridgement.

The third-party mirror exposes fields such as `cluster`, `duplicates`,
`full_article_id`, `article`, `headline`, and `byline`. Those fields are useful
for feasibility inspection, but the mirror's schema and headline availability
must not silently replace the primary paper's documented representation. A
future adapter must pin the exact source/version and record any schema delta.

### 3.3 What NEWS-COPY labels—and what it does not

The native NEWS-COPY label is a **duplicate relation** defined against a same
original source article. It is not a four-way relation field and is not a claim
or stance annotation.

| Native observation | Safe protocol interpretation | Unsafe interpretation |
| --- | --- | --- |
| Two records are labeled duplicate/same original source article | A candidate `dependent`/`DPND` edge, subject to preserving the dataset's scope and label provenance | “The two reports are independently verified” or “the underlying claim is true” |
| Two records are labeled nonduplicate | Different under the dataset's duplicate definition; generally `UNKN` for origin dependence in T1 | `INDP`, consensus, independent corroboration, or unrelatedness |
| Two articles share a quote but are nonduplicate | `UNKN` origin relation; a shared quoted passage is a possible common pathway | Independent evidence because the articles have different IDs |
| Two articles cover one larger story but are nonduplicate | `UNKN`; the event/story relation and source-origin relation remain separate | Distinct origin proven by topical or wording difference |
| An article is an update with breaking news | A new artifact/version; origin relation requires a documented derivation path and claim-scope audit | Same claim, same story, or different URL automatically decides dependence |
| Singleton or excluded merged-summary record | `UNKN` unless another primary source documents its origin | `INDP` because no matching duplicate was found |

The mapping in the middle column is an **adapter inference**, not a NEWS-COPY
label. A same-original label can justify a dependent relation for the relevant
pair, but it does not identify every upstream transformation, author, wire
service, press release, or common event. The root/original relation itself may
remain `UNKN` when no parent is supplied.

### 3.4 Same-original cluster reconstruction

**Finding: bounded yes for duplicate clusters; no for a provenance-complete
origin graph.**

Within the selected NEWS-COPY full-day samples, the manual annotation design
supports reconstructing clusters under the paper's operational definition of
“same original source article.” The exhaustive singleton review and high
agreement make this the strongest of the two candidate resources for a
dependent/reproduction stress case.

That result does not make the cluster a perfect origin graph:

- The label concerns same source article, not a complete chain of original
  reporter, wire bureau, syndicate, local editor, quote source, or event.
- The paper's best clustering method is ARI 93.7, not 100%; severe OCR,
  abridgement, repeated quotes, updates, and same-story articles remain error
  modes.
- The corpus is a historical U.S. newspaper sample on selected dates, not a
  complete news ecosystem or a modern web-syndication census.
- A duplicate cluster gives evidence of one source path under the dataset's
  definition. It does not certify that the source was authoritative, honest,
  correct, or independent of another unseen source.
- A nonduplicate pair is not a proof of two origins. The primary paper
  explicitly includes shared-quote, same-story, and updated-article cases among
  nonduplicates.

Therefore a T1 adapter may expose `same_original_as_labeled` as a provenance
receipt, then derive `DPND` for a documented pair. It must keep the native label,
the derivation rule, and the uncertainty reason in separate fields. It must
never overwrite native `duplicate/nonduplicate` with `INDP/UNKN` as if the
vocabularies were equivalent.

### 3.5 Claim and stance gap

NEWS-COPY does not provide the bundle-level target claim, claim scope/time, or
the report-to-claim stance required by the current contract. An article about a
story is not automatically support for a proposition selected by a researcher.
The paper's duplicate label is orthogonal to whether a report supports,
refutes, qualifies, or is insufficient for a claim.

To use NEWS-COPY in a descriptive transfer adapter, a separately authored
annotation layer would need at least:

- a versioned atomic `claim_id`, claim text, scope, time window, and target
  predicate;
- report-level stance: `supports`, `refutes`, `qualifies`, or `insufficient`;
- exact evidence spans and offsets, with OCR/normalization status;
- report artifact identity, newspaper/source identity, publication date, and
  any available byline or scan pointer;
- native duplicate label and the adapter's relation mapping kept side by side;
- derivation type (`original`, `dependent_copy`, `dependent_paraphrase`,
  `quoted`, `summarized`, `updated`, or `unknown`), with a citation to the
  evidence for the classification;
- support-side and refute-side origin sets, if and only if their paths are
  documented;
- annotation provenance: annotator ID, rubric version, scan/pointer used,
  disagreement, adjudication, and uncertainty reason.

The annotator must not infer stance from headline sentiment, source reputation,
or duplicate status. “This article is a copy” and “this article supports the
claim” are different labels.

### 3.6 Multiple-origin and unknown-origin construction from NEWS-COPY

NEWS-COPY natively supports one useful case: repeated reports mapped to one
same-original cluster. It does not natively support three documented,
separately authored supporting origins, nor does it supply a deliberate
unknown-origin stratum.

Safe options are:

1. Use same-original clusters as **dependent** candidate fixtures only after
   claim/stance/span annotation and manual source-path review.
2. Construct a multiple-origin case only from separate source records whose
   independent authorship/derivation status is documented by an allowed
   primary source and adjudicated under a new transfer rubric. Such a case is a
   descriptive certification, not the synthetic `INDP` truth state.
3. If the evidence cannot establish a source path, set the certification state
   to `unknown` and preserve why. Do not treat “not found” or “not similar” as
   proof of unknown in the latent world; it is only a decision not to certify.
4. If a transfer bundle intentionally withholds a relation after review, name
   that as a **withheld certification state**, not as a discovered fact about
   the number of real origins.
5. Keep multiple-origin and unknown-origin rows descriptive. Under the current
   protocol, they cannot populate `M` or any confirmatory/safety denominator.

The recommended T1 NEWS-COPY scope is thus: a small, license-cleared or
metadata-only sample of same-original candidates plus an explicit unknown
control, with no claim that nonduplicates are independent.

### 3.7 NEWS-COPY-specific risks

| Risk | Why it matters for transfer | Required T1 handling |
| --- | --- | --- |
| OCR and layout errors | Character errors, merged columns, and abridgement can create false negatives or ambiguous spans | Preserve raw/native text identity; retain normalized text as a derived view with a correction receipt; audit spans against scans where permitted |
| Period language and typography | 1920–1977 vocabulary, punctuation, bylines, and newspaper conventions differ from modern web text | Stratify/report period and source ecology descriptively; do not claim modern-domain transfer |
| Historical source ecology | Wire services, local papers, syndicates, and local edits are not the same as web publishers, aggregators, press releases, or social posts | Name the transport as historical print/newswire transfer only |
| Headline mismatch | The paper says local headlines were generally excluded; a mirror may expose headline fields | Pin a version and treat headline availability as a schema change, not an interchangeable field |
| Duplicate definition | Same-source article is narrower than all semantic similarity or same-event recurrence | Keep native `duplicate` separate from origin, stance, and truth |
| Same quote/common event | Nonduplicate pairs may share a quote or larger story | Map to `UNKN` unless a source path is documented |
| Sample coverage | Full-day labels cover selected historical dates and front pages, not all news | Use descriptive counts only; no population prevalence or modern coverage claim |
| License ambiguity | Official release path does not state a data license; mirror says unknown | No article-text copying or redistribution until rights are resolved |

## 4. Audit 2 — Newswire

### 4.1 Primary-source status

| Source | Status as of 2026-08-18 | What was verified | License/handling status |
| --- | --- | --- | --- |
| [Newswire, arXiv HTML](https://arxiv.org/html/2406.09490) | Emily Silcock, Abhishek Arora, Luca D’Amico-Wong, and Melissa Dell; v1, submitted 2024-06-13; primary dataset paper | Construction pipeline, fields, cluster collapse, wire filtering, OCR/period limitations, dataset facts, and license statements | Paper says CC-BY and its dataset-information section links CC BY 2.0; this must be reconciled with the current dataset card |
| [Official Newswire dataset card](https://huggingface.co/datasets/dell-research-harvard/newswire) | Curator-owned Hugging Face dataset page; current page readable | Dataset summary, fields, `cluster_size`, explicit “no relationships,” no native labels, row/file snapshot, and licensing information | Page reports `cc-by-4.0`, DOI `10.57967/hf/2423`; version pin and field-level rights still required |
| [Official Newswire replication repository](https://github.com/dell-research-harvard/newswire) | Public code repository; primary pipeline code index | Public code for entity, georeferencing, and topic components | Code and data licensing are separate; no data rights inferred from repository visibility |
| [Creative Commons CC BY 4.0 deed](https://creativecommons.org/licenses/by/4.0/) | Canonical license summary | Attribution, link/license notice, modification notice, no endorsement, and other-rights caveats | Use only after confirming which dataset version/fields are covered |
| [Newswire dataset DOI metadata page](https://doi.org/10.57967/hf/2423) | DOI cited by the official card and paper | Stable citation target for the dataset release | DOI does not eliminate the need to pin a file/commit/hash |

### 4.2 Verified dataset facts

The primary paper and official card state:

- Newswire contains 2.7 million unique public-domain U.S. newswire articles
  written between 1878 and 1977, reconstructed from roughly 138 million
  structured article texts extracted from newspaper scans.
- Each selected article appears once in the released Newswire representation,
  while its reproduction metadata records dates and newspapers that carried the
  article. The paper reports 2.7 million unique wire articles and roughly 32.1
  million reproductions in the underlying corpus.
- The public schema includes `article`, `byline`, `dates`,
  `newspaper_metadata`, `wire_city/state/country`, topic/entity fields,
  `cleaned_article` on the current card, and `cluster_size`.
- `cluster_size` is defined as the number of newspapers that ran the wire
  article and equals the length of `newspaper_metadata`; it is not a number of
  independent origins.
- The pipeline uses a contrastive bi-encoder and single-linkage clustering to
  detect reproduced content. The paper reports ARI 91.5 for that scalable
  method, inherited from the NEWS-COPY methodology.
- The reproduction detector initially catches all reproduced content, not only
  wire stories. Post-processing removes weather/local templates and uses a
  classifier for other syndicated material. The paper says nearly 95% of the
  remaining articles are wire articles, with a higher proportion later in the
  period; this is not a 100% wire-origin certificate.
- The dataset card says the data are not labeled and that no relationships
  between individual instances are made explicit.
- The paper says it selects one version from a reproduced cluster for inclusion
  using paragraph count and non-word rate. It does not provide every scanned
  reproduction as a separate released report row in the current schema.
- The paper says not every local paper or subscribed wire archive survives, so
  Newswire cannot be assumed to be a complete archive of all wire dispatches.
- The paper and card warn about OCR errors, historical language/cultural norms,
  offensive or inaccurate content, and limits for applications requiring clean
  text.
- The current card page displays a versioned access surface with an estimated
  row count of about 1.44 million and a larger first-5GB viewer, while its
  summary retains the paper's 2.7 million article figure. These are not
  interchangeable counts; a future transfer must pin the exact file list,
  revision, row count, and hash rather than rely on the live viewer.

The paper also reports the Newswire dataset as CC-BY and links to a CC BY 2.0
URL in its dataset questionnaire, while the current Hugging Face page reports
CC BY 4.0. This version/link discrepancy is not a reason to infer a restrictive
license, but it is a required rights-reconciliation item before any text,
metadata, or derived-label redistribution.

### 4.3 What Newswire labels—and what it does not

Newswire's `cluster_size`, `dates`, and `newspaper_metadata` make a useful
aggregate recurrence receipt. They do not supply the current protocol's
per-report relation graph.

| Newswire field/observation | Safe interpretation | Unsafe interpretation |
| --- | --- | --- |
| `cluster_size` | Number of newspapers listed as carrying the selected article representation | Number of independent origins or number of supporting pathways |
| `dates` list | Observed publication dates associated with the selected reproduction cluster | Evidence that each date is an independent observation or separate source |
| `newspaper_metadata` list | Newspapers associated with the cluster, identified with LCCNs and location fields | Independent authorship, independent reporting, or distinct claims |
| `wire_city/state/country` | Inferred wire-bureau dateline/location for the article cluster | A complete wire-service identity or proof of origin independence |
| One `article` per released row | One selected/representative text for the inferred cluster | A complete list of all reports or exact transformation chain |
| Two distinct Newswire rows | Two rows after the pipeline's clustering/filtering | Two independent origins; a different row can still share an event, quote, press release, or unseen pathway |
| Topic/entity/cleaned fields | Model-derived metadata or a normalized text view | Claim stance, truth, or source authority |

The dataset card's explicit statement that no instance relationships are made
explicit is decisive: aggregate cluster metadata cannot be silently upgraded
to a report-level `relation_by_report_id` map.

### 4.4 Same-original cluster reconstruction

**Finding: aggregate reproduction is available; report-level reconstruction is
not reliable from the released schema alone.**

Newswire can support a descriptive statement such as “this selected article
was associated with a cluster of `k` newspaper appearances on these dates.” It
cannot support the stronger statement “we have reconstructed all report
artifacts and their exact origin edges.” Reasons include:

- The public row is already a representative selected from the cluster.
- `cluster_size` and `newspaper_metadata` retain counts and newspaper metadata,
  not each reproduced text, report ID, transformation, edit, or evidence span.
- The clusters are model-inferred and the reported ARI is below perfection.
- The wire-content filter leaves a residual non-wire share and cannot be
  treated as a perfect origin label.
- `wire_city` identifies a bureau/datelined location, not necessarily the
  author, wire service, original artifact, or upstream report.
- Missing newspapers and archives make absence of a row non-evidence of absence
  of a dispatch or source.

Newswire is therefore suitable for a descriptive “repetition is not origin
count” demonstration and for testing whether an adapter keeps cluster count
separate from support-origin count. It is not suitable as a confirmatory
origin-graph ground truth without a new, documented annotation and source
reconstruction process.

### 4.5 Claim and stance gap

Newswire's topic labels, named entities, and article text do not provide a
target proposition or report-level claim stance. The card says the data are not
labeled, and its fields do not include `gold_claim_state`, support/refute
spans, or support/refute origin sets.

The same transfer annotation requirements as NEWS-COPY apply, with two extra
constraints:

1. Because each row is a selected cluster representative, a stance label must
   identify whether it applies to the representative text, the cluster's
   underlying article, or every newspaper appearance. Those are different
   claims.
2. A publication in several newspapers may reflect one wire dispatch and
   multiple local edits. If local versions are not available, the adapter must
   not invent per-paper stance or evidence spans from the representative text.

### 4.6 Multiple-origin and unknown-origin construction from Newswire

Newswire natively supports a one-origin/reproduction candidate only at the
aggregate cluster level and only under the paper's inferred wire-cluster
definition. It does not provide multiple-origin convergence cases. Distinct
Newswire rows are not a substitute for those cases.

Safe T1 treatment:

- Use `cluster_size`/dates/newspaper metadata only as observed recurrence and
  reproduction context.
- Map the cluster's repeated appearances to a dependent/reproduction receipt
  only when the adapter preserves the source paper's inference and limitations.
- Assign `UNKN` to relationships between different rows unless an external,
  documented derivation path establishes dependence or a separately audited
  source record establishes an origin relation.
- Do not assign `INDP` from different `wire_city` values, different newspapers,
  different dates, different bylines, different topics, or different wording.
- Build a multiple-origin case only from additional source records and an
  explicit annotation protocol; Newswire alone cannot establish it.
- Treat unknown as a certification state (“we do not have enough origin
  evidence”), not as a claim that the latent world contains exactly one or
  multiple origins.

### 4.7 Newswire-specific risks

| Risk | Why it matters for transfer | Required T1 handling |
| --- | --- | --- |
| OCR and representative-text selection | A cluster may have source-specific errors or edits hidden by the selected representative | Keep raw/cleaned fields distinct; do not infer per-paper wording or stance from one representative |
| Historical period language | 1878–1977 language, typography, and cultural framing differ from modern news ecology | Report period/source limits; no current-web generalization |
| Front-page/source coverage | The reconstruction uses local newspaper scans and does not cover every surviving or lost paper | Treat coverage as observed availability, not source absence or prevalence |
| Wire/non-wire residual | The paper says nearly 95% of remaining material is wire after filtering | Keep wire classification as inferred and uncertain; do not use it as a perfect origin label |
| Cluster-model error | ARI 91.5 leaves false joins and misses | Preserve model/version and cluster uncertainty; no gold relation claim |
| Public text and derived fields | Article text, OCR, georeference, topics, entities, and cleaning are different layers | Record each field's provenance and license; do not conflate derived labels with gold stance or origin |
| Offensive/inaccurate content | The card and paper warn that historical material can be inaccurate or offensive | Add content-risk screening and human review before any model exposure or release |
| Viewer/version drift | Live card row counts and files can change; older versions may not remain hosted | Pin DOI plus revision/file hashes before any future use |

## 5. Cross-dataset relation audit

The table below answers the operational relation question directly. “Available”
means available as an observed or source-documented field, not necessarily
available as ground truth.

| Required protocol object | NEWS-COPY | Newswire | T1 decision |
| --- | --- | --- | --- |
| Report/artifact ID | Article IDs/cluster fields are available in the paper/release path; exact canonical schema must be pinned | One selected article row ID can be assigned; per-reproduction report IDs are not released in the card schema | Assign stable adapter IDs, retain native IDs, and do not invent hidden copies |
| Source/newspaper identity | Historical newspaper identity is part of the source context; exact field availability depends on release version | `newspaper_metadata` with LCCNs and titles is present | Use as observed source context, not authorship or independence |
| Publication time | Selected dates are part of the corpus | `dates` list is present | Preserve as observed time; do not equate distinct dates with distinct origins |
| Same-original relation | Native duplicate definition and hand-reviewed clusters | Inferred reproduction clusters with aggregate metadata | Map only documented same-origin cases to dependent; retain native label and uncertainty |
| Derivation/transformation | Abridgement/OCR and transmission-chain context are discussed; full transformation edge is not supplied | Cluster inference and representative selection are documented; per-copy edits are absent | Add a separate derivation label; default unknown when path is missing |
| Independent-as-stipulated | Not supplied | Not supplied | Never assign `INDP` from either public dataset |
| Unknown relation | Safe and required for nonduplicate/unresolved pairs | Safe and required for cross-row relationships | Use `UNKN` as the default certification state |
| Atomic claim | Not supplied | Not supplied | Add only through a separately governed annotation layer |
| Claim stance | Not supplied | Not supplied | Add `supports/refutes/qualifies/insufficient` with spans and adjudication |
| Supporting-origin certification | Same-original clusters can support a single-path candidate after stance review; complete support set is not native | Cluster count is not support-origin count; support-side certification is absent | Descriptive only; no T1 row enters `M` under current protocol |
| Refuting-origin certification | Not supplied | Not supplied | Must be separately annotated; do not infer from topic or text polarity |
| Evidence spans | OCR article text exists, but no claim-specific spans | Representative article text exists, but no claim-specific spans | Add offsets and scan/pointer receipts if rights permit |
| Dataset license | Unclear in official release; mirror says unknown | Card says CC BY 4.0; paper says CC-BY and links CC BY 2.0 | Resolve field/version rights before text or labels are copied/released |

### 5.1 Exact operational mapping rule

The adapter should use this precedence order:

1. If a source-documented derivation path says report `r2` derives from `r1`,
   write `origin_relation=dependent` and, in the F2-compatible cue slot,
   `DPND`.
2. If the relation is not documented but the pair is labeled nonduplicate,
   write `origin_relation=unknown` and `UNKN`. Nonduplicate is retained as a
   native duplicate-task outcome, not transformed into a positive independence
   label.
3. If separate authorship/origin is documented but not part of a predeclared
   synthetic graph, write `distinct_documented_origin` in a transfer-only
   field and still do **not** write synthetic `INDP` unless a protocol amendment
   explicitly defines that mapping. This prevents a transfer observation from
   becoming a confirmatory truth label by naming convention.
4. If a relation is deliberately withheld after an audit, write
   `certification_state=unknown` and preserve the withholding reason.
5. Keep relation, stance, derivation, authority, authorization, and truth in
   separate fields. No generic `relation` field may absorb them.

This ordering preserves the v14 non-negotiable distinction: recurrence is not
independence; provenance is not correctness; source authority is not claim
support; and permission is not truth.

## 6. Required annotation and adjudication layer

Neither public resource can enter even a useful descriptive transfer bundle
without a small, independently versioned annotation layer. The minimum
transfer record should be structurally compatible with the current manifest,
but must be named as transfer and must not masquerade as synthetic gold.

### 6.1 Minimum transfer record

```json
{
  "split": "transfer_news_copy_v1",
  "dataset": "NEWS-COPY",
  "dataset_revision": "<pinned revision or source receipt>",
  "bundle_id": "T1-...",
  "claim_id": "CL-...",
  "claim_text": "<atomic proposition>",
  "reports": [
    {
      "report_id": "RP-...",
      "native_record_id": "<source id>",
      "source_id": "<newspaper/source id>",
      "artifact_time": "<observed time>",
      "stance": "supports | refutes | qualifies | insufficient | unknown",
      "evidence_spans": [
        {"start": 0, "end": 0, "span_status": "audited | unavailable | unknown"}
      ],
      "derivation_type": "original | dependent_copy | dependent_paraphrase | quoted | summarized | updated | unknown",
      "origin_relation": "dependent | distinct_documented_origin | unknown",
      "relation_code_for_prompt": "DPND | UNKN | NONE",
      "relation_basis": "<receipt or unknown reason>"
    }
  ],
  "gold_support_origin_certainty": "none | single | multiple | unknown",
  "support_origin_ids": [],
  "refute_origin_ids": [],
  "transfer_only": true,
  "confirmatory_denominator_eligible": false,
  "safety_denominator_eligible": false,
  "license_receipt_id": "LIC-..."
}
```

This is a design proposal, not an existing dataset schema. `INDP` is absent
from the proposed public-transfer cue values by default. If a later protocol
amendment authorizes a transfer-specific documented-distinct label, it must
define the estimand and semantics before any run.

### 6.2 Normative annotation rules

- `supports`, `refutes`, `qualifies`, and `insufficient` are claim-scoped and
  time-scoped. A source or article is not globally supportive or refuting.
- A quote copied from another article may support the claim, but it remains a
  dependent evidence path unless its own origin is documented.
- A report about the same event can be a new observation, a copied report, a
  press-release echo, a common-source report, or an update. The event identity
  does not settle origin relation.
- `unknown` is retained when the available source ecology cannot establish the
  edge. It is not a negative label and is not a license to count the report as
  independent.
- Claim truth is outside this transfer adapter. Even a supported/contested
  annotation states a relation between claim and text, not objective truth.
- Annotators must see the source receipt and relevant scan/pointer context but
  must not see model outputs when constructing gold/descriptive labels.
- A second annotator audits all proposed `multiple` and a stratified sample of
  `dependent`/`unknown`; an adjudicator resolves disagreements with a written
  reason code. Unresolved cases remain `unknown`.
- OCR corrections are derived text, not source text. Preserve both when the
  license and storage policy allow; otherwise retain an immutable pointer/hash
  and no copied article body.

### 6.3 Construction of multiple-origin and unknown-origin strata

The only defensible route to a multiple-origin T1 stratum is:

1. freeze the public dataset/version and permitted fields;
2. select a bounded event/claim sample without using model outcomes;
3. identify each report/artifact and its source path from allowed primary
   records;
4. document that no report in the proposed supporting set is a copied,
   paraphrased, summarized, quoted, or otherwise derived path from another
   supporting report;
5. have human auditors adjudicate the claim stance, evidence spans, and
   derivation/origin paths;
6. if any path remains unresolved, label the support-origin certification
   `unknown` and remove the bundle from any multiple-origin descriptive stratum
   that requires certification.

This can create a **documented distinct-origin observation** in a descriptive
transfer set. It does not create synthetic `INDP` truth, real-world causal
independence, or a VOR safety denominator. A cheaper and safer alternative is
to build the four origin structures synthetically as the current protocol
already requires, then use NEWS-COPY/Newswire only for descriptive boundary
examples.

An unknown-origin stratum can be built without invented ground truth if its
definition is procedural: after a fixed audit, the relation certificate is
withheld because the evidence is insufficient. The record must say that the
latent relation is not known, not that it has been measured as one or multiple
origins. No model result can convert this certification state into truth.

## 7. Does the false-corroboration endpoint/output contract transport?

### 7.1 Output contract: yes, unchanged

The JSON object, strict parser, raw-output preservation, invalid-output policy,
evidence-ID semantics, and separate `claim_state` field can be reused without
adding a transfer-specific output key. `evidence_ids` should point to adapter
`report_id`s, not dataset rows that hide several newspaper appearances.

The transfer input must carry relation cues and a manifest outside the output
object. The model's `origin_count_supporting` still counts the number of
supporting **origin paths** it asserts; it does not count articles, newspapers,
dates, URLs, or cluster members.

### 7.2 Endpoint: only descriptive and conditional

The endpoint's computational shape transports, but its confirmatory meaning does
not transport automatically:

| Contract component | T1 transport decision |
| --- | --- |
| Strict output schema | Reuse unchanged |
| `FC_obs` formula | Reuse as a descriptive warning only when a transfer manifest states the certification state; with mostly `unknown`, report it as conservative risk coding, not measured error truth |
| `FC_cons` invalid-as-risk code | Keep separate within the T1 report if a future run is authorized; never merge its rows with `A` |
| `FC_lib`/`FC_valid` sensitivities | Descriptive only; report parseability and conditioning explicitly |
| `VOR` | Do not run as a confirmatory or safety endpoint for transfer rows under the current protocol; a transfer row cannot enlarge fixed `M` |
| `claim_state` | Descriptive only after claim/stance annotation; native dataset topics do not substitute for stance |
| `confidence` | Descriptive scalar output; no multiclass calibration claim |
| `evidence_ids` | Reuse with adapter report IDs and exact evidence-span audit status |
| Relation cue | Use `DPND`, `UNKN`, or `NONE` only when the transfer manifest supports that cue; do not add `F3` |
| Primary denominator | Synthetic `A=300` only; T1 rows stay in `transfer_*` denominators |
| Safety denominator | Synthetic fixed `M` only; `M_T1` is empty under the current protocol |

For a T1 record with `gold_support_origin_certainty=unknown`, the current
`FC_obs` definition deliberately treats a model assertion of two or more
supporting origins as a conservative risk event. That can be useful for
auditing whether a system overclaims corroboration, but without a known latent
origin count it is not a correctness label. The report must call it a
**conservative transfer diagnostic**, not a false-corroboration rate in the
world.

### 7.3 What would require a protocol amendment

A protocol amendment would be required before any of the following:

- adding transfer rows to the confirmatory `FC_cons` test or its confidence
  interval;
- adding transfer rows to `M`, calculating VOR, or making a safety/non-
  inferiority statement across synthetic and public data;
- treating documented distinct real-world origins as the same semantic value as
  synthetic `INDP`;
- adding a transfer condition, model, endpoint, or post-lock claim family;
- changing `A`, `M`, the invalid-output policy, or the primary denominator.

The current T1 inclusion decision therefore means “include as a descriptive
transfer artifact if rights and annotation gates pass,” not “include in the
first-paper efficacy analysis.”

## 8. Dataset, metadata, derived-label, and redistribution licensing

This section is an operational rights screen, not legal advice. A public URL or
a public-domain statement is not by itself permission to copy, transform,
retain, or redistribute every field.

| Asset layer | NEWS-COPY status | Newswire status | Current handling |
| --- | --- | --- | --- |
| Article/OCR text | Official data license not found; mirror says unknown | Dataset card says CC BY 4.0; paper says CC-BY and links CC BY 2.0; underlying historical public-domain assertion has scope/field caveats | No text download or redistribution in this feasibility lane; future use requires versioned rights receipt |
| Source/newspaper metadata | Fields exist, but NEWS-COPY release terms are unclear | LCCN/newspaper/date metadata is released in the card; exact rights coverage should be confirmed | Use only metadata facts visible in primary sources for feasibility notes; do not copy records into a dataset |
| Duplicate/cluster labels | Human/model-derived labels are part of an unclear release path | Cluster/reproduction labels are pipeline-derived; card says no instance relationships are explicit | Treat as derived labels with provenance, version, and uncertainty; do not call them gold origin graph edges |
| Topics/NER/georeference/cleaned text | Not a NEWS-COPY core relation contract | Current Newswire card includes model-derived fields and `cleaned_article` | Keep each field's derivation and model/version separate; do not use as stance/origin truth |
| Official code | Public repositories are observable | Public replication repository is observable | Code visibility does not grant data rights; record code revision/license separately |
| Adapter schema/code | New work authored in this repository | Same | May be released later only with owner authorization and no copied restricted text |
| Model outputs/raw run logs | None produced here | None produced here | Future output release needs model/checkpoint, data, privacy, and license review |

The [CC BY 4.0 deed](https://creativecommons.org/licenses/by/4.0/) describes
attribution, a link to the license, indication of changes, and the absence of
endorsement; it also warns that other rights may limit a particular use. The
paper's CC BY 2.0 link and the card's CC BY 4.0 label must be reconciled before
release. In particular, confirm whether the stated license covers:

- the article text as a compilation and as individual public-domain works;
- newspaper and LCCN metadata;
- cluster/reproduction labels and topic/entity/georeference annotations;
- cleaned/normalized text as an adaptation;
- any source scans, thumbnails, or OCR intermediate files;
- redistribution of derived labels without the original article text.

For NEWS-COPY, the answer is currently not established. The safe T1 path is a
metadata-only feasibility note or an authorized, rights-cleared sample created
later by the owner. The Dropbox download linked by the official README is not
used in this lane.

## 9. Operational go/no-go checklist for descriptive T1

Every unchecked item is a stop for that phase. A later operator must not
silently replace an unchecked item with a favorable assumption.

### 9.1 Before any data access

- [ ] The synthetic primary run is complete or the protocol explicitly records
  why the descriptive transfer is being run after the primary lock.
- [ ] The transfer split has a unique name such as
  `transfer_news_copy_v1` or `transfer_newswire_v1`; it is not called `F3` and
  does not reuse the 60-bundle fictional stress split.
- [ ] Exact dataset source, version/revision, DOI or release URL, file list,
  row count, and SHA-256 receipt are pinned.
- [ ] A rights table identifies the license and permitted retention,
  transformation, redistribution, and derived-label use for each field.
- [ ] NEWS-COPY's unresolved data license is cleared by an authoritative source
  or the transfer is metadata-only.
- [ ] Newswire's CC BY version mismatch is resolved and the exact covered
  fields are recorded.
- [ ] Owner authorization exists for any text copy, model exposure, or release;
  no credentials, cookies, private records, or paid services are in scope.
- [ ] A privacy/content-risk screen covers names, allegations, offensive
  period-language, and sensitive historical reporting before model exposure.

### 9.2 During transfer construction

- [ ] Native dataset IDs, source IDs, dates, cluster labels, and derived fields
  are preserved separately.
- [ ] Every report in a prompt has a stable opaque `report_id`; a Newswire
  `cluster_size` is not expanded into invented report rows.
- [ ] Same-original labels retain their native definition and are mapped to
  `DPND` only when the documented adapter rule passes.
- [ ] Nonduplicate, different publisher, different URL, different date, and
  different wording default to `UNKN` unless a source-to-source derivation path
  is documented.
- [ ] No public record receives synthetic `INDP`.
- [ ] Claims are atomic and versioned; stance and evidence spans are separately
  audited rather than inferred from source or cluster labels.
- [ ] Support and refute origins remain separate; conflict is not reduced to a
  single article-level sentiment or topic label.
- [ ] Unknown-origin cases identify whether unknown means “not observed,”
  “relation withheld by protocol,” or “conflicting source records.”
- [ ] Proposed multiple-origin cases have a documented distinct-origin basis,
  independent review, and an explicit statement that they remain descriptive.
- [ ] No transfer row is eligible for synthetic `A` or `M`; the manifest sets
  `confirmatory_denominator_eligible=false` and
  `safety_denominator_eligible=false`.

### 9.3 Before a model run

- [ ] The primary F0/F1/F2 prompt, output schema, parser, token cap, and
  invalid-output policy are reused without a transfer-specific condition.
- [ ] Relation slots are fixed-width and codebook-visible as in the current
  specification; public transfer does not introduce a hidden format cue.
- [ ] Claim/evidence text, report order, and relation cue availability are
  logged; no model sees restricted gold fields not authorized by the transfer
  design.
- [ ] The model/checkpoint/tokenizer license and revision are pinned; potential
  pretraining overlap with historical newspaper text is recorded as a
  limitation, not treated as a proof of contamination or clean transfer.
- [ ] No live web, paid provider, model API, external retrieval, or automatic
  text enrichment is used.
- [ ] Raw outputs are write-once, parser failures remain visible, and no manual
  retry or repair is allowed after lock.

### 9.4 Reporting and release

- [ ] T1 counts, parse rates, `FC_obs` conservative diagnostics, claim-state
  annotations, and relation-preservation errors are reported in a separate
  descriptive table.
- [ ] No p-value, confidence interval, power statement, VOR decision, or
  confirmatory effect combines T1 with the synthetic primary/safety analysis.
- [ ] The report says whether each relation is native, manually annotated,
  inferred by adapter, or unknown.
- [ ] No sentence calls a nonduplicate “independent,” a cluster “truth,” or a
  source count “corroboration” without the exact documented qualification.
- [ ] Any article text, scan, metadata, label, or model output retained for
  release has a field-level license/attribution receipt and permitted
  redistribution status.
- [ ] If rights are unresolved, release only the schema, code, source URLs,
  hashes, and aggregate feasibility findings that are allowed; do not include
  copied text or derived records whose terms are unclear.
- [ ] Owner authorization is recorded before publication, external sharing,
  deployment, or dataset release.

## 10. Final recommendation and claim ladder

### Disposition: include as descriptive T1

Include only a separately named, rights-cleared or metadata-only transfer
artifact after the current primary lock. The strongest permitted T1 claims are
descriptive:

- NEWS-COPY demonstrates that same-original duplicate labels can provide a
  bounded dependent/reproduction stress case, while nonduplicate labels do not
  establish independent origin.
- Newswire demonstrates that aggregate newspaper recurrence and inferred wire
  clusters can be preserved as context without treating `cluster_size` as
  independent support.
- A strict output adapter can preserve `DPND`/`UNKN`, evidence IDs, claim-state
  separation, invalid outputs, and the conservative FC diagnostic on a public
  transfer split, subject to annotation and licensing gates.

The following claims remain outside T1:

- real-world `INDP` or independent corroboration;
- multiple-origin ground truth from public source count or distinct URLs;
- provenance discovery or complete source/derivation reconstruction;
- claim truth, source authority, or decision utility;
- transfer of a synthetic F2-versus-F1 effect to modern news, web evidence, or
  another model;
- any confirmatory or safety conclusion involving transfer rows.

The practical next step, if the owner authorizes one, is a small dry-run of the
adapter on metadata and hashes only. It should prove that native duplicate
labels, `DPND`, `UNKN`, claim/stance fields, and transfer-only denominator flags
survive serialization. It must not download the unresolved NEWS-COPY corpus,
run a model, or alter the v15 protocol.

## 11. Primary source register

All URLs below were read or checked read-only on 2026-08-18. “Primary” means
dataset curator, original paper, official code repository, or canonical license
source; mirrors are labeled as such.

1. [NEWS-COPY paper, arXiv HTML, v2](https://arxiv.org/html/2210.04261) — primary
   paper; duplicate definition, annotation procedure, counts, and error modes.
2. [NEWS-COPY official repository](https://github.com/dell-research-harvard/NEWS-COPY)
   — primary code/data release index; README links the historical download but
   does not state a data license.
3. [NEWS-COPY official README](https://github.com/dell-research-harvard/NEWS-COPY/blob/main/README.md)
   — primary release instructions and dataset counts.
4. [NEWS-COPY evaluation mirror](https://huggingface.co/datasets/chenghao/NEWS-COPY-eval)
   — secondary schema/status check; page reports `license: unknown`; not used
   as a canonical license grant.
5. [Newswire paper, arXiv HTML](https://arxiv.org/html/2406.09490) — primary
   paper; corpus construction, fields, cluster selection, coverage, OCR,
   limitations, and dataset-license statements.
6. [Newswire official dataset card](https://huggingface.co/datasets/dell-research-harvard/newswire)
   — curator-owned current card; reports CC BY 4.0, DOI, fields, no explicit
   instance relationships, and live viewer/version information.
7. [Newswire official code repository](https://github.com/dell-research-harvard/newswire)
   — primary replication code index; code visibility is not a data license.
8. [Newswire dataset DOI](https://doi.org/10.57967/hf/2423) — stable dataset
   citation target; future runs still need exact file/revision hashes.
9. [Creative Commons Attribution 4.0 deed](https://creativecommons.org/licenses/by/4.0/)
   — canonical license summary used only for the rights checklist; not a
   substitute for resolving the dataset's field/version coverage.
10. [Detecting Textual Reuse in News Stories, At Scale](https://ijoc.org/index.php/ijoc/article/view/9904)
    — primary adjacent paper distinguishing newswire copy, public-relations
    reuse, source-to-source copying, common-source overlap, and incidental
    overlap; supports keeping text reuse separate from origin certification.
11. [North American News Text Corpus, LDC95T21](https://catalog.ldc.upenn.edu/LDC95T21)
    — primary licensing boundary example for commercial newswire text: the
    catalog identifies members-only access, fees, and copyright notices. It is
    not proposed as a T1 dataset.

## 12. Audit completion

This feasibility audit is complete for the requested read-only scope. It adds
no dataset, no transfer records, no `F3`, no primary/safety denominator rows,
and no model result. The one disposition is **include as descriptive T1**,
subject to the go/no-go checklist and the explicit separation from the
synthetic confirmatory study.
