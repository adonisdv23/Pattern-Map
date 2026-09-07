# Research next stage: useful discovery and observation boundaries

Status: **DESIGN AND PRIMARY-SOURCE REVIEW / NO STUDY RUN / NO RESULTS**.
Prepared under the owner's 2026-09-07 next-phase goal. This is a successor
research plan, not a revision of locked owner intent, an accepted paper, a
preregistration, or execution authority. The existing DL-PLAYBOOK-01 protocol
and narrow-wedge memo retain their historical unselected status.

## Research judgment

Pattern Map is not at a terminal research point. Its broad six-family proposal
still needs a demonstrated advantage over competent ordinary practice. The
most interesting question is how to discover useful unfamiliar options while
preserving the standards needed to select them. The most tractable first
measurement candidate is narrower: whether separating observation from capture
state improves a bounded decision when a strong prose baseline has exactly the
same information.

These are different ambitions. Discovery can develop the intellectual centre
of the project. The observation study can test one small mechanism. A positive
observation result would not validate all six families or establish a general
theory of creativity. A null result would still tell us whether the extra
representation earns its cost.

## Close comparison with prior methods

The following is a targeted methods review, not an exhaustive systematic review.
Primary full text was inspected on 2026-09-07. No external dataset was acquired.
Interpretations in the final column are our design judgments.

| Primary source and inspected sections | Method, task and comparator | Evaluation and relevant limit | Consequence for our proposed study |
| --- | --- | --- | --- |
| [Hope et al., Accelerating Innovation Through Analogy Mining, KDD 2017](https://arxiv.org/html/1706.05585), §§2–4 and discussion | Learns purpose/mechanism representations; retrieves similar purposes with diverse mechanisms. Product redesign compared analogy inspirations with TF-IDF and random inspirations, using a counterbalanced within-participant design. | 38 crowd workers, 12 seeds; separate judges assessed changed mechanism, preserved purpose and feasibility. The authors discuss noisy analogy labels, multifaceted products, dependence between ideas, and limits of the representation. | Structural transfer and useful diversity are established. Include strong purpose/mechanism search, check transfer assumptions, and analyse task clusters rather than treating every generated idea as independent. |
| [Kargupta et al., Idea-Catalyst, arXiv v1, 12 March 2026](https://arxiv.org/html/2603.12226v1), §§3–5, baseline and evaluation descriptions | Target-domain questions and gaps become domain-agnostic challenges, external retrieval, integrated fragments and pairwise ranking. Compares free-form and guided dual retrieval, with decomposition/ranking ablations. | 400 selected CHIMERA instances and LLM preference evaluation; six researchers supplied their own problems for a human study. Novelty/insightfulness and usefulness can diverge; verbose output remained a concern. Its ablations bundle some components and do not directly isolate our proposed timing contrast. | “Explore, then assess” and interdisciplinary grounding are heavily occupied territory. Do not claim novelty for the sequence. Test decision utility under matched total cost and keep early/late evaluation separate from retrieval breadth. |
| [Beyond Divergent Creativity, EACL Findings 2026](https://aclanthology.org/2026.findings-eacl.138.pdf), §§3–4 | Compares divergent word generation with random and task-aware baselines; introduces a cue-constrained task requiring related yet diverse nouns. | Lexical semantic-distance outcomes expose weaknesses of novelty-only scoring. The paper explicitly treats its operationalisation as partial, with appropriateness and novelty trade-offs. | A surprising answer or high diversity score is insufficient. Score task-feasible supported options and final selection; report invalid analogies and unhelpful variety separately. |
| [AbsenceBench, NeurIPS 2025](https://papers.neurips.cc/paper_files/paper/2025/file/36b31e1bb8ecd4f4081686448e9eff2d-Paper-Datasets_and_Benchmarks_Track.pdf), §2 task construction and §4 analysis | Gives both original and modified documents and asks for intentionally omitted elements, across numbers, poetry and pull requests. Examines omission rate, context and explicit missing-item markers. | Its known omissions permit omission detection scoring. Visible placeholders alter the task's cues. It does not establish absence in an unbounded world; the proposed architectural explanation remains a hypothesis. | Do not rebrand omission detection. Our candidate supplies the same trace facts in both arms, varies capture outcome, and scores a downstream bounded action. Marker benefits must be separated from extra information. |
| [Value of Information: A Framework for Human–Agent Communication, ACL 2026 / arXiv](https://arxiv.org/html/2601.06407), §§3–5 | Chooses clarification versus commitment by expected utility gain minus communication cost. Compares no question, fixed rounds, adaptive prompting and confidence thresholds; tasks include controlled guessing, preference elicitation and an adapted shopping environment. | Requires utility and belief estimates; its practical procedure approximates these with model estimates and constrained answer sets. Utility elicitation and user burden remain design dependencies. | Cost-bounded stopping is not new. Our first pilot should use fixed known task costs, not a model-invented universal value score. Record human review as a separate cost. |
| [Over-Searching, EACL 2026](https://aclanthology.org/2026.eacl-long.361.pdf), metric definition, task construction, setup and judge assessment | Studies search with answerable and unanswerable questions, including false premises, unavailable answers and underspecification. Defines a cost-per-correct-response metric that includes input, output and search. | Uses task-specific answer/abstention judging, including human comparison. Its search-cost coefficients are a chosen model, not portable prices; agreement does not establish perfect ground truth. | Retain false answers and harmful abstention separately. Report actual resource use beside decision outcomes; do not import its aggregate cost weights as our utility function. |

The strongest novelty conclusion currently supported is **no established novel
mechanism yet**. The possible contribution is a carefully isolated decision
comparison, an error taxonomy with counterexamples, or evidence that a compact
practice can be removed. Further literature expansion is useful only when it
can change this design or its claim. Before a publication novelty claim,
specifically close classic ideation-timing/fixation work, selective prediction,
missing-data/measurement theory, and appropriate-reliance interface studies.
Their existence is a reason to narrow claims, not a reason to stop local work.

## Track D: grounded option discovery

Question: under the same information and total budget, when does an exploratory
pass before rejection improve the useful options available for a decision, and
when does it waste effort or admit invalid analogies?

There are two distinct mechanisms to test:

1. **Evaluation timing:** present the same candidate material in the same order
   and compare immediate feasibility rejection with a bounded exploratory pass
   followed by the identical final feasibility and support checks. This tests
   use of supplied material. It does not test retrieval coverage.
2. **Search expansion:** give equal access to a fixed local catalogue, equal
   query/tool limits and the same final checks; vary conventional topical search
   versus purpose/mechanism exploration. Record which material was retrieved.
   This tests discovery through search and requires its own assignment. Do not
   infer that effect from the fixed-material timing test.

Keep the first comparison to timing plus a strong conventional comparator.
A later 2×2 breadth-by-timing design is possible if both mechanisms warrant the
additional cases. An omnibus six-family arm is premature.

Common output for every arm: chosen option or bounded hold; at most three
candidate options; supporting source IDs; violated or unresolved constraints;
the strongest reason the chosen option might fail; next authorized local step.
Do not request hidden chain-of-thought. Visible candidate records and actions
are the observable procedure, not a faithful account of internal reasoning.

Common instruction for all arms:

> Solve the stated decision using the supplied facts and constraints. Consider
> plausible alternatives, including a different mechanism serving the same
> purpose. Do not reward unfamiliarity by itself. Select a feasible supported
> option, or explain the exact unresolved condition. Use the shared output
> fields and stay within the assigned total budget.

Timing additions, frozen before any run:

- **D0 conventional:** “Use your usual careful approach to compare the options,
  challenge the preferred one, and select the best supported route.”
- **D1 immediate:** “For each candidate in the supplied order, state its proposed
  transfer and apply the supplied feasibility/support checks before considering
  the next candidate. Record a rejected candidate's reason.”
- **D2 exploratory first:** “First state a possible transfer for each supplied
  candidate, marking uncertainty without rejecting it. Then apply the same
  feasibility/support checks to all candidates and make the final selection.”

The final acceptance rule is identical. D2 may entertain a candidate temporarily;
it may not acquire unauthorized material, take an external action, suppress a
material failure, or recommend an invalid option. Instructions consume the same
total envelope. Do not add extra useful facts to D2.

Primary future outcome: task-level accepted selection under a frozen rubric.
Secondary outcomes: number of distinct feasible supported options found, missed
useful options, invalid analogy selection, needless hold, effort and elapsed
time. Raw originality ratings, family coverage and schema completion are not
primary outcomes. The development cases include a useful transfer, a tempting
invalid transfer, an ordinary route that already suffices, and an existing
capability that removes the need for a new component.

Failure conditions: identical or worse accepted decisions at higher cost;
improved novelty with no useful selection improvement; a benefit that disappears
when facts and output length are matched; or a result driven by one authored
case. Report these outcomes and simplify or stop this track accordingly.

## Track B: observation versus capture, recommended first pilot proposal

This is the recommended first **measurement pilot**, subject to the gates below.
It is not a claim that Candidate B is novel or validated. Keep access AVAILABLE,
permission AUTHORIZED for the simulated local check, and currency CURRENT.
Vary observation and process/capture only.

A completed check with no event can support “absent in this defined log and
period,” if that is the packet's complete observation universe. An empty result
after failed capture cannot support the same statement. A found event can
establish bounded presence even if a later capture stage fails. Rechecking an
already complete adequate observation can also be a costly error.

The task/world key is frozen separately from the visible trace. A failed trace
must have paired hidden worlds with and without the event; the accepted answer
must be the same because the model cannot see which world occurred. Never
grade an unobservable hidden fact as if the model should know it. The included
development generator enforces this counterfactual equality.

An elementary identifiability argument sets the claim ceiling. Let the same
visible trace T be possible both when an event is present and when it is absent.
A rule that sees only T must choose the same action in both worlds (or the same
distribution of actions if randomized). It therefore cannot guarantee the
correct world-presence assertion in both. Writing UNKNOWN in a field does not
add information about the world; it can improve the choice to qualify, stop or
recheck. This is ordinary reasoning about indistinguishable observations, not a
claimed new theorem. Consequently, B tests use of supplied process information.
Testing better observation itself would require an additional acquisition
experiment with the same authorized tools and budgets across arms.

**B0 strong prose:** Every relevant fact appears explicitly in ordinary prose:
expected item, precise scope, observable finding, whether the check was
attempted/completed/failed, and held-fixed access, permission and currency.

**B1 structured:** The same facts appear as fields for expected item, scope,
observation and process/capture, with the same held-fixed axes. No extra oracle
label, source, expected answer, severity warning or permission fact is added.

Common prompt:

> Decide what this check supports and the next bounded step. The supplied trace
> may be incomplete. Use only visible facts. Return a decision, scope, source
> IDs and a brief reason. Report absence only within a fully checked stated
> scope; do not assume an empty capture proves absence. Avoid repeating a check
> that already supports the required bounded decision. No external action is
> available.

This deliberately strong instruction may eliminate the structured arm's
advantage. That is a useful null finding. Both arms use the same final output
fields; the input representation is the intervention.

### Pilot envelope and why this size

Proposed design: 12 base packets covering four non-sensitive domains (build
logs, scheduled file deliveries, inventory snapshots, local event journals)
by three balanced decision classes (bounded absence, recheck/unknown, bounded
presence). Two independently authored surface forms and two repeat runs per
arm give **96 outputs**. Counterfactual hidden-world variants for failed captures
are key checks, not extra independent study observations. No external corpus is
needed. The included development cases are excluded from these future packets.

This size serves case coverage and instrument diagnosis. It is not a powered
effectiveness study and cannot establish noninferiority. Before calls, freeze
all 12 packets, both surface forms, rubric, source hashes and assignment seed
after an independent reviewer checks the keys. New authoring and reviewer
selection remain part of the exact future execution packet.

Proposed per-output cap: 4,000 total model tokens counting instructions, visible
facts, generated output and any billed reasoning; 120 seconds; zero external
retrieval, zero model retries for answer quality, zero external actions.
If the provider cannot report/enforce the reasoning-inclusive cap, the run
cannot claim matched total tokens; change the protocol before launch or stop.
Up to 384,000 total tokens follows from the 96-output cap, with no unbounded
repair allowance. Proposed financial ceiling: **USD 40**, requiring explicit
approval and a price-based calculation against the selected model before use.
This is a proposed cap, not spending authority or a cost forecast.

Provider/model/version/decoding configuration remain intentionally unselected.
Use one fixed configuration across arms. A mid-run version change invalidates
the affected comparison; never silently substitute another provider. Every call
and failure consumes a reserved slot. Infrastructure failures remain in the
attempt ledger, with an explicit validity assessment. A later amended rerun is
separate, never a replacement for an unfavorable original output.

### Analysis and decision rules

- Primary descriptive contrast: B1 minus B0 accepted-decision rate, first
  averaging repeats and surface forms within each base packet, then weighting
  the 12 base packets equally. Parse failure, unjustified refusal, timeout and
  budget exhaustion receive zero accepted-decision credit. Report them by class.
- Preserve all 96 assigned slots in the accounting. Report both attempted and
  assigned denominators. A launch-wide infrastructure failure makes the pilot
  invalid for an efficacy interpretation; it does not become a model failure
  claim. Show a completed-output sensitivity analysis separately.
- Use two blinded reviewers for every primary decision, with condition names
  and unnecessary formatting removed. Keep disagreements and original labels;
  resolve against the prewritten rubric. If the rule is ambiguous, mark the
  task invalid and report the effect with and without it, rather than repair
  the key after seeing which arm won. Review itself requires later scope.
- Report paired task differences and a task-cluster bootstrap interval as
  exploratory uncertainty, plus the individual task table. Twelve clusters are
  too few for a strong precision claim. Do not treat 96 outputs as 96 independent
  tasks or test many subgroups for a favorable headline.
- Guardrails: false absence, unsupported presence, avoidable recheck/hold,
  invalid scope extension, permission/action error, actual tokens, elapsed time
  and reviewer minutes. Report raw costs separately; no universal trust or
  utility score.
- Instrument gate: any leakage, unequal facts, wrong oracle key, hidden-world
  inference in grading or untracked denominator stops interpretation. More than
  one irreconcilably ambiguous base packet requires redesign before expansion.
- Practical continuation heuristic, not significance: at least two additional
  base packets with improved mean acceptance, no base packet with a new false
  absence caused by the representation, and no material cost increase left
  unexplained. Otherwise simplify, revise once with a documented cause, or
  stop. Passing this heuristic only earns a larger design review.
- A larger study must use pilot variance and task dependence to justify its
  precision and sample size, choose a minimum useful effect and safety margin
  before new data, and include a genuinely held-out domain. No power, transfer
  or efficacy claim is available from the pilot alone.

### Exact future execution packet

The only run-authorizing artifact must name: protocol version and hashes;
rights-cleared frozen packets and keys; the reviewer(s) and their scope;
provider/model/version and data-handling permission; enforced token/time/call
caps; priced maximum cost and approved dollar ceiling; execution environment;
assignment seed; retention location; stop owner; and authorization expiry.
Its explicit owner approval is required before any call. This document is
reviewable preparation and supplies none of that authority by itself.

## Echo, human reliance and routes beyond a paper

Echo remains the separate origin-accounting project with its existing v1.1
protocol and unfavorable-outcome classes. It is a viable alternative first run
because it is more specified, but it tests a different question. Supplying an
origin map tests use of given accounting; discovering real origin relationships
requires a separate observation design. No new Echo study is run or selected.

Candidate A remains a later human appropriate-reliance study. Hold answer text
and evidence constant and change only the review interface, with both supported
and unsupported claims. Better acceptance of every claim would be a failure.
It cannot establish improved generated-answer accuracy. Participant recruitment,
consent, accessible design and reviewer burden require separate work and scope.

Possible useful outputs even without a positive model effect: a compact open
methods note, a reusable development-case collection, a decision-record adapter,
or a negative-result account showing when ordinary careful prose suffices.
Protocol Foundry can package a stable procedure after repeated use reveals a
need; Alpha can later host a bounded comparator under its existing budgets and
replay controls; Signal Foundry can supply source-bound evidence when explicitly
authorized. None requires a new research platform or custom model now.

The commercial hypothesis belongs with Revenue: a scoped review of one
evidence-heavy decision might save enough correction effort to be purchased.
No demand or willingness to pay has been observed. Require an actual customer
problem and a paid, bounded engagement before treating the report as a product.
Keep its first settled-payment and repeat-contribution criteria; citations,
fixtures and enthusiastic reviews do not meet them.
