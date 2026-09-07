# Image selection ledger - v14 decisions reconciled for v15.2

- **Decision date:** 2026-08-18
- **Status:** historical scoring record reconciled with the current v15.2
  rendered build; no publication authorized
- **Rubric:** 0–4 on conceptual fidelity (CF), non-misleading structure (NM),
  complementarity (CO), editorial fit (EF), crop resilience (CR),
  accessibility support (AS), and craft/distinctiveness (CD). A production
  candidate must score at least 20/28, receive no zero in CF/NM/CR, and exist
  as a clean local asset without interface chrome.

## Provenance boundary

- The files under `candidates/` were generated through the OpenAI image-generation tool. The exact model name was not exposed in the tool result, so this ledger does not infer one.
- The files under `chatgpt-images/previews/` are audit screenshots of candidates generated through **ChatGPT Images** in the signed-in Signal Foundry Pro project. The interface did not expose an exact generator model name. They are therefore not labeled DALL-E 3 or attributed to a model that was not shown.
- The ChatGPT Images files are preview evidence only: the available session did not yield a clean exported local image without interface chrome. They are not production assets even when their visible concept score is high.
- The recovered v13 map is separate from this experiment. It is the unchanged historical DALL-E-created anchor supplied through the live reference, not a regenerated candidate.

## Role H — hero editorial image

| Candidate | Route | CF | NM | CO | EF | CR | AS | CD | Total | Disposition |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| H1 — Evidence aperture | OpenAI image-generation tool | 4 | 2 | 4 | 4 | 4 | 4 | 4 | **26** | **Archived after Loop 3; omitted from the final rendered site and PDF.** The aperture, arrowheads, and cleaner right-hand field can imply a mandatory one-way filtering pipeline or gatekeeper that the framework does not claim. |
| H2 — Braided origins | OpenAI image-generation tool | 3 | 2 | 3 | 4 | 4 | 3 | 4 | 23 | Retained as audit candidate. Beautiful, but the dominant channels read too much like a pipeline and duplicate the deterministic relationship figure. |
| H3 — Cartography of attention | OpenAI image-generation tool | 3 | 1 | 2 | 3 | 4 | 2 | 3 | 18 | Rejected. It introduces a question mark, a checkmark, and magnifying-lens truth semantics explicitly excluded by the prompt. |
| H1 — Evidence aperture | ChatGPT Images preview | 4 | 3 | 4 | 4 | 4 | 4 | 3 | 26 | Strong alternate; not production-eligible because only an authenticated UI preview was recovered. The selected H1 is also more legible at wide crop. |
| H2 — Braided origins | ChatGPT Images preview | 3 | 2 | 3 | 4 | 4 | 3 | 3 | 22 | Not selected. Clear craft, but still reads as channelized processing; preview-only. |
| H3 — Cartography of attention | ChatGPT Images preview | 3 | 2 | 2 | 4 | 3 | 3 | 4 | 21 | Not selected. The lens/terrain metaphor competes with the exact map and is harder to summarize without implying privileged truth; preview-only. |

### Archived hero experiment

- Candidate source: `candidates/H1-evidence-aperture.png`
- Archived derivative: `assets/imagegen/archive/context-before-answer.jpg`
- Production dimensions: 1672 × 941
- Production SHA-256: `59e0f6908e48e0c4cce2d5e247ce344cf41c77aca8b9d87a6c4fad04a1119ad7`
- Final placement: none. The file remains as design-process evidence, but the rendered site and PDF use a text-led opening.
- Reason: the semantic risk remained material after the Loop 3 reader/design review; a caption cannot reliably neutralize an immediately perceived topology.

## Role E — worked-example editorial image

| Candidate | Route | CF | NM | CO | EF | CR | AS | CD | Total | Disposition |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| E1 — Nine windows, one origin | OpenAI image-generation tool | 4 | 4 | 4 | 4 | 4 | 4 | 4 | **28** | Strong alternate. Exact nine reports, one source, and two independent observations; retained as the clearest literal backup. |
| E2 — Echo sheets and watermark | OpenAI image-generation tool | 4 | 4 | 4 | 4 | 4 | 4 | 4 | **28** | **Selected.** The same image survives across nine transformations, making shared origin visible before the reader traces every line; the two materially different artifacts remain independent. |
| E3 — Provenance constellation | OpenAI image-generation tool | 1 | 2 | 3 | 4 | 3 | 2 | 4 | 19 | Rejected. The report-node count is wrong and the topology requires too much decoding for the example’s one-glance job. |
| E1 — Nine windows, one origin | ChatGPT Images preview | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 27 | Strong alternate; exact visible counts and excellent lineage. Not production-eligible because only a UI preview was recovered. |
| E2 — Echo sheets and watermark | ChatGPT Images preview | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 27 | Strong alternate; exact visible counts and useful document framing. Not production-eligible because only a UI preview was recovered. |
| E3 — Provenance constellation | ChatGPT Images preview | 2 | 2 | 2 | 4 | 3 | 2 | 3 | 18 | Rejected. The requested report count and distinction among common, independent, and unresolved origins are not reliably readable; preview-only. |

### Selected worked-example asset

- Candidate source: `candidates/E2-echo-sheets-watermark.png`
- Production derivative: `site/public/images/nine-mentions-one-origin.jpg`
- Production dimensions: 1536 × 1024
- Production SHA-256: `88222893a08a52bbca3f1d855aaa575827c829b09766d743a5db931930a3e325`
- Placement: immediately before the deterministic six-step worked example.
- Final alt text: “Editorial illustration of one coral source artifact branching into nine differently styled report fragments, beside two separately rooted evidence fragments.”
- Caption boundary: “Illustration · not a reported dataset or result.”

## Role S — social-share card

| Candidate | Route | CF | NM | CO | EF | CR | AS | CD | Total | Disposition |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| S1 — Nine observations, one shared origin | OpenAI image-generation tool | 4 | 4 | 4 | 4 | 4 | 4 | 4 | **28** | **Retained, not rendered in v15.2.** It remains a strong future share-preview candidate, but the local owner-review metadata intentionally references no social card. |

### Retained social-card candidate

- Candidate source: `candidates/S1-social-card-chatgpt-images.png`
- Production derivative: `site/public/og.png`
- Production dimensions: 1200 × 630
- Candidate SHA-256: `3f3adae00f2aeb80bf8eb5bd87da27dd3ec700497f81aa1ece60853a528951ff`
- Production SHA-256: `26d87ad92d12edabebb829daabf7ca60681ac720ff15705c86bb677a99bf3b24`
- Provenance: generated once through the current OpenAI image-generation tool. The interface did not expose an exact model name, so it is recorded as ChatGPT Images/OpenAI image generation without inferring a legacy DALL-E version.
- Current placement: none. `site/public/og.png` is preserved but not referenced
  by the v15.2 metadata.
- Scope: possible future share-preview art after a separate publication
  decision. It does not define the framework topology or provide evidence.

## Historical anchor

- Archive file: `archive/v13/pattern-recognition-diagram-v12.png`
- Site copy: `site/public/images/v13-six-families-origin-map.png`
- Dimensions: 1024 × 1536
- SHA-256: `8a8204a05e993e84f2bd9037c59b7beb2ab6b4bca89304e299f66b3961f203ae`
- Disposition: preserve unchanged and caption as the historical v13 origin map. Its seven-step strip is historical context, not the v14 runtime topology.

## Production decision

The final v15.2 local site uses one generated worked-example derivative and the
unchanged historical v13 anchor. No generated hero or social-share card is
referenced by the current build. The risky hero experiment and the otherwise
strong social-card candidate remain as design-process evidence. The six-family
map, component count, two-loop relationship, route states, evidence labels,
and citations remain deterministic HTML and live text. No generated raster
defines a component, sequence, truth state, or empirical result.
