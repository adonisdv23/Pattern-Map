# A concrete decision for the first research run

**Propose a 10-percentage-point attainment gain over both baselines, small
separate cost tolerances, and one complete run of the existing 144 assignments.**
The owner can accept these values, change the open execution values before
launch, or leave the instrument unrun. These are managerial proposals, not
estimated effects, observed costs, statistical power or execution authority.

Status: **PROVIDER-NEUTRAL PREPARATION / NO STUDY RUN / NO RESULTS**.
Instrument source: `61f530c39aa30be67c310116c460b8adabdc79e8`; prepared
2026-09-07. The [locked owner intent](../../../docs/OWNER_INTENT_V16.md) and
[pilot specification](../ultra/PILOT_DECISION_SPEC.md) govern. The
[public instrument description](../ultra/pilot/README.md) and
[offline adapter](../ultra/pilot/adapter.py) describe the material and local
contract. This packet fills open decision choices; it adds
no arm, task, prompt, output field or platform. The frozen Ultra tree remains
`463a39c5f698346191c65178eeeb03c0146e9b9d`. No private rubric was read here.

## Proposed useful-effect decision

Set **`delta_min = 0.10`** for both R–O and R–M. R is the transfer/check
instruction package; O is careful ordinary practice; M adds purpose/mechanism
comparison. Ordinary comparison permits competent reasoning and reconsideration;
it is not canonical Stage 0 `ORDINARY`.

There are twelve authored base tasks, four assignments per task/arm, **48 per
arm and 144 total**. With the frozen equal task weighting, the mean contrast
equals the difference in accepted assignment counts divided by 48. Thus 0.10
requires **at least five net additional accepted assignments** against each
baseline: 5/48 = 0.104167. Four is insufficient. This is an intelligible minimum
for retaining extra procedure: more than an isolated output improvement, under
the same acquisition ceiling and modest additional resource burden.

| Value the owner could choose before launch | Minimum net gain versus each baseline | Largest baseline attainment that leaves the gain achievable |
| --- | ---: | ---: |
| 0.05, less demanding | 3/48 = 0.0625 | 45/48 |
| **0.10, recommended** | **5/48 = 0.104167** | **43/48** |
| 0.15, more demanding | 8/48 = 0.166667 | 40/48 |

These choices are sensitivity arithmetic, not alternative analyses to select
after seeing outputs. A baseline above 43/48 can make the recommended threshold
unattainable. That would favor the simpler practice, not justify lowering the
bar afterward. Five gains can still concentrate in two tasks. Retain the full
task table, every domain/regime contrast and the frozen leave-one-task-out
sensitivity; 144 slots are not 144 independent problems. For illustration,
task net gains of `[4,1,0,0,0,0,0,0,0,0,0,0]` yield 5/48 overall but only
1/44 after removing the first task. This is invented arithmetic, not performance.

**All frozen advancement gates remain necessary:** complete valid assignment
and unambiguous reviewed keys; both aggregate gains meeting the threshold;
nonnegative contrasts in every domain and regime; no R scope/permission error;
no increase in any other harm class against either baseline overall or within
a regime; and every separate resource margin below. Passing earns only a larger
design review. A truthful hold can remain epistemically appropriate while failing
operational attainment in a selection task. Denied/malformed/duplicate attempts
retain charges and diagnostics without automatically invalidating a later valid
terminal choice. Never-launched and failed slots remain in the assigned account;
a stopped or invalid run cannot advance.

## Proposed cost margins and hard ceilings

For adoption assessment, compare **totals over all 48 assigned slots per arm**
against each baseline separately. Do not condition costs on successful outputs
or combine unlike resources into a score.

| Resource | Recommended allowable R increase | Why this tolerance |
| --- | --- | --- |
| Accounted model tokens | At most 10% of each baseline total | Pays a small instruction overhead while requiring a material decision gain |
| Inference spend | At most 10% of each baseline total | Token parity cannot conceal different billed rates, cache behavior or charges |
| Sum of episode elapsed times | At most 15% of each baseline total | A little more latency is acceptable; service delay still counts and condition-confounded disruption invalidates interpretation |
| Charged acquisition units | **At most 12 additional units** over either baseline total | Allows an average 0.25 extra charged units per assigned episode to obtain discriminating evidence; the shared B=2 ceiling remains unchanged |
| All marginal semantic, adherence/trace-review and adjudication person-minutes | At most 10% of each baseline total | Include the required separate action/procedure pass; report subcomponents and common setup separately |

Implement each margin as a difference inequality, for example
`R_tokens - O_tokens <= 0.10 * O_tokens`; do the same against M. The relative
resource gates remain defined when a baseline is zero: R must also be zero for
that resource. Acquisition instead uses `R_units - baseline_units <= 12`, so
a zero-acquisition baseline allows at most twelve R units. An
unavailable measurement is unknown, never zero; unresolved required accounting
prevents advancement. Attribute semantic, adherence/trace-review and adjudication time to the
affected output/arm; report those subcomponents separately and include all
of them in the margin. Record genuinely shared setup separately rather than
assigning it favorably.

Twelve extra units permits up to twelve extra checks or charged mistakes for
the required five net attainment gains. This is a proposed small allowance,
not an estimated exchange rate between information and benefit. A stricter
**zero-extra-units** alternative would reject any positive R acquisition cost
when a baseline uses zero, even if an extra check is beneficial within B=2.
That expresses a managerial preference for no additional acquisition burden;
it is not evidence of theoretical inefficiency. Report selection, authoring and
maintenance effort separately; those efforts were not measured here.

The following **hard stopping ceilings** are a separate tentative run proposal,
identical across arms. They are not claims that the tasks fit a particular
tokenizer/runtime, nor extra capacity granted to R:

- At most **32,000 accounted tokens and 180 seconds per episode**; totals
  **4,608,000 tokens** and **25,920 summed episode seconds (7.2 hours)**.
  Account repeated inputs, output and billed reasoning without double-counting
  reasoning already included in a provider's output measure.
- At most **eight model requests per episode / 1,152 total**. Each completed
  request supplies one original action string to the frozen adapter. No silent
  repair or answer-quality retry; transport failures consume their assigned slot
  and remain visible. Adapter B=2/K=8 and all action deadlines stay unchanged.
- Propose **USD 50 total inference/transport spend** and **26 reviewer
  person-hours**. The dollar amount is an unpriced ceiling preference, not a
  quote or predicted bill. Neither amount is authorized. Storage or fixed service charges
  must fit the dollar ceiling; paid reviewer contracting is not proposed.

After a provider is explicitly chosen, require an exact tokenizer/serialization
and price worksheet before approving these ceilings. Price conservatively at
uncached rates, include any separately priced reasoning and fixed charges, and
do not assume discounts. Check whether all eight rounds, growing histories and
permitted released views fit; 32,000 tokens may be insufficient. Do not truncate
frozen prompts/evidence or relax deadlines/retry rules to fit. Revise the open
capacity proposal before launch or stop. With one pooled 4,608,000-token upper bound and no other
charges, the maximum category rate must be no more than about USD 10.850694 per
million tokens to fit USD 50. Otherwise reduce authorized capacity before launch,
choose another owner-approved configuration, or do not run. A hard dollar cap
must reserve the worst-case next request before dispatch; “stop after the bill
arrives” is insufficient. Token exhaustion or truncation remains a cost/effort
failure, not permission to enlarge limits mid-run.

## Review allocation and semantic acceptance

Propose **two independent semantic reviewers for every terminal decision**,
plus a named adjudicator and a run operator. Roles may share existing personnel
where independence is preserved; identities and conflicts must be recorded.
Prefer reviewers who did not author the task/rubric. If unavailable, record the
author-dependence limitation rather than call the review independent of authorship.
No external recruitment or paid review is authorized here.

The 26-person-hour planning allowance comprises four hours of common preparation
(two per semantic reviewer), 14.4 hours for 288 initial semantic reviews
(three minutes each), 2.4 hours for 144 separate action/procedure adherence
passes (one minute each), four hours adjudication, and 1.2 hours reserve. Name
the adherence reviewer; that role may be held by a member of the named team
while preserving the independent semantic judgments. These are allocation
assumptions, not measured task times or a per-output pressure to agree. If adequate review exceeds
capacity, record the remaining work and stop interpretation; unresolved scoring
cannot earn advancement.
Review labor may dominate the total practical expense despite a small inference
ceiling. No reviewer wage, willingness or actual burden has been measured; the
26-hour proposal is a capacity reservation for owner review, not a forecast.

Before evaluated outputs exist, both reviewers should inspect all twelve public
tasks and both narrative forms, identify questionable values, feasible
alternatives and observation limits, then compare those judgments with the
frozen semantic rubrics under separately authorized access. This packet does
not pre-accept unseen keys. Resolve objections before launch; an irreducibly
ambiguous task blocks the current instrument. A material task/rubric/prompt/
assignment correction requires a separately identified, reviewed successor and
new hashes, preserving the present frozen instrument. Filling its expressly
open threshold, resource and execution values does not itself rewrite it.

For the eventual run, follow the existing blinded-as-far-as-possible two-reviewer
procedure using each acquired trace, preserve individual judgments and condition
recognition, and assess adherence separately. Reconcile disagreement against the
frozen rubric rather than the author's desired answer. Missing second review,
unresolved interpretation and ambiguous keys cannot be silently counted as
accepted. No lexical scorer or completion of a form establishes semantic quality.

## One exact execution scope to finish later

Use this as the execution section of the existing owner decision, not a new
standing form. **Every proposed value remains unapproved until that decision.**

| Bind before launch | Concrete proposed content or remaining choice |
| --- | --- |
| Instrument | Existing 12-task O/M/R instrument, 144 assignments, seed `20260907`; record its exact source commit, existing material/instruction/adapter manifest hashes and assignment identity |
| Decision values | Proposed `delta_min=0.10`, all frozen harms/domain/regime gates, the separate margins above; name the accepted semantic-review record |
| Runtime | **Owner to name:** exact provider/model/version, reasoning/temperature and supported reproducibility settings; identical configuration and external instructions for all arms |
| Limits and price | Proposed 32,000 tokens/180 seconds/eight requests per episode and stated totals, USD 50; accept only after exact serialization, tokenizer, enforceability and dated price check |
| Data and people | **Owner to name:** operator, two reviewers/adjudicator, permitted data handling, exact restricted retention location, access and retention/deletion policy |
| Authority | **Owner to name:** permitted evaluated calls, effective window/expiry, stop owner and exact hash-bound launch instruction; no publication, outreach, production action or automatic follow-on experiment |

## Transport acceptance before evaluated calls

The existing adapter checks local shape and transitions; it is not an isolated
provider runtime. Under later exact setup authority, verify the following with
provider-neutral canned requests first; any live diagnostic call needs its own
applicable call/budget scope and must never be a disguised pilot trial.

1. The tested context receives only the frozen public prompt/current view and
   released observations. Keys, rubric, author notes, other arms and full
   repository paths are inaccessible. An in-process underscore is not isolation.
2. Fresh episodes have no prior outputs, shared memory or feedback. Preserve
   exact assigned narrative/order and original wire bytes; pass each unmodified
   action string to the adapter. Do not normalize malformed JSON into success.
3. Canned success, denial, duplicate inspection, failed capture, deadline and
   malformed requests reproduce the adapter's charges, releases and termination.
   No new action can run after termination; the external token/time/call controls
   work independently of the toy acquisition counter.
4. Reserve next-request spend/capacity, enforce episode and run limits, cancel
   safely at expiry, and preserve transport errors and unlaunched assignments.
   Reconcile assigned/attempted/completed counts and all costs without resets.
5. Check that the actual runtime exposes sufficient accounting and respects the
   approved isolation/data-handling boundary. Missing evidence means unverified
   readiness, not a passed check. A version or configuration change stops the run.

No transport has been built or certified by this document. The useful next
owner decision is whether these concrete values and review resources are worth
funding, then which exact permitted configuration can meet them. If not, retain
the prepared source and ordinary practice. No additional pilot
follows automatically from declining or failing this proposal.

Arithmetic is reproducible with [threshold_arithmetic.py](threshold_arithmetic.py);
[its output](THRESHOLD_ARITHMETIC.txt) uses no source files, private keys,
probabilities or empirical observations. It establishes only the displayed
integer and budget calculations. A01–A17, the locked owner contract, no-results
boundary and separate Echo track remain unchanged.
