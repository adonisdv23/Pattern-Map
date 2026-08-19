/* eslint-disable @next/next/no-img-element -- the historical v13 raster is a verified local archive asset. */
import MicroVisual from "./MicroVisual";
import ReadingNav from "./ReadingNav";
import Term from "./Term";

const objections = [
  {
    title: "Is this old work under a new label?",
    body: "Much of it is. If a strong, matched-budget retrieval-and-citation baseline performs as well at lower cost, the extra structure should lose for that task.",
  },
  {
    title: "Could it become a gatekeeper?",
    body: "Yes. Selection can erase peripheral sources or make exclusion look like quality control. Exclusions, unknowns, reasons, permissions, source coverage, and appeal must remain inspectable.",
  },
  {
    title: "Could the receipt become rigor theater?",
    body: "Yes. Perfect lineage for a false claim is still perfect lineage for a false claim. A receipt earns its place only when a recorded distinction changes a decision or permits a real correction.",
  },
  {
    title: "Will human review be decorative?",
    body: "It will be if a reviewer sees only a polished recommendation, cannot inspect the route, or cannot change the packet. Oversight must be a control, not a signature at the bottom.",
  },
  {
    title: "Will it cost more than it saves?",
    body: "It may. The deeper map is an analytical decomposition, not required ceremony. It should collapse whenever a simpler route delivers the same decision quality for less cost.",
  },
];

export default function HomeEssay() {
  return (
    <main id="main-content">
      <a className="skip-link" href="#stop-60-90">Skip to the first reading stop</a>

      <aside className="rail" aria-label="Reading paths and status">
        <a className="wordmark" href="#start" aria-label="Pattern Recognition, return to start">
          <span>Pattern<br />Recognition</span><small>v15.2</small>
        </a>
        <ReadingNav initialActive="start" />
        <p className="rail-status"><span aria-hidden="true" /> Local owner review</p>
      </aside>

      <div className="page-shell">
        <header className="masthead masthead-v15-2" id="start">
          <div className="masthead-meta">
            <p className="eyebrow">Local owner review · v15.2 · conceptual synthesis</p>
            <p className="masthead-status">No model selected · no study run · no empirical result · not published</p>
          </div>
          <h1>Pattern Recognition<span aria-hidden="true"> / </span><em>The Discrimination Layer</em></h1>
          <p className="dek">What an AI system should preserve before repetition becomes corroboration.</p>
          <p className="title-definition"><strong>Here, discrimination means technical differentiation among information and possible actions—not social classification or discriminatory treatment.</strong></p>
          <nav className="route-choice route-choice-v15-2" aria-label="Choose a reading path">
            <a className="route-card route-primary" href="#stop-60-90">
              <span className="route-time">60–90 seconds</span>
              <strong>See the failure</strong>
              <span>Nine reports, one path, zero counted support, and a hold.</span>
            </a>
            <a className="route-card" href="#stop-5">
              <span className="route-time">About 4 minutes</span>
              <strong>Use the receipt</strong>
              <span>Three questions, one correction rule, and a human next step.</span>
            </a>
            <a className="route-card" href="#stop-12-15">
              <span className="route-time">About 9 minutes</span>
              <strong>Test the argument</strong>
              <span>Loops, use boundary, objections, research bridge, and history.</span>
            </a>
            <a className="route-card route-lab" href="/explore">
              <span className="route-time">Optional deeper records</span>
              <strong>Inspect the framework</strong>
              <span>Explore contains the records and cases; Lab contains the no-results protocol; Sources explains evidence and terms.</span>
            </a>
          </nav>
        </header>

        <section
          className="section essay-route route-stop-section"
          id="stop-60-90"
          data-route-stop="60-90"
          aria-labelledby="stop-60-90-title"
          tabIndex={-1}
        >
          <div className="section-marker"><span>01</span><small>60–90 sec</small></div>
          <div className="section-body">
            <p className="status-pill">Fictional illustration · no live data · no result</p>
            <p className="kicker">Nine reports, one announcement</p>
            <h2 id="stop-60-90-title">The summary changed the structure of the evidence.</h2>
            <p className="lead">A team is deciding whether a sandbox pilot of a data-migration tool is worth ninety minutes of investigation. Production data are off limits. The claim on the table is broad: “The tool is broadly validated.”</p>
            <p>Nine favorable reports arrive through nine different sites. Their headlines, layouts, and wording differ. A summary says:</p>
            <blockquote className="essay-quote">Nine sources agree that the new tool is broadly validated.</blockquote>
            <p>Then someone traces the reports backward. All nine came from the same launch announcement.</p>
            <p>The reports have not become false. They may still show reach, timing, or how the announcement travelled. But repetition alone did not create eight new roots. The summary has not merely shortened the evidence. <strong>It has changed its structure:</strong> nine observations became nine apparent paths, then apparent plurality became corroboration.</p>
            <p>If that relationship disappears from the evidence record, an AI system can inherit the inflated plurality when it writes the answer.</p>

            <MicroVisual variant="origin-count" />

            <p>One path is known; zero paths are counted as support for this broad claim yet. That does not mean no source exists, the reports are false, or the tool is rejected. A vendor can be the right source for what it announced and still not establish that its product is validated in independent use.</p>
            <p>The next action is deliberately small: inspect the announcement, find one separately authored benchmark or failure report, record how it relates to the earlier material, and then reconsider the claim. The receipt does not make the pilot decision. It makes a hidden change in route visible.</p>
            <aside className="route-stop-end" aria-label="End of the 60–90-second route">
              <strong>Stop here after 60–90 seconds.</strong>
              <span>Preserve the nine observations. Do not silently count them as nine supporting paths. Hold the broad claim and inspect one more relation.</span>
              <a href="#stop-5">Continue to the four-minute route ↓</a>
            </aside>
          </div>
        </section>

        <section
          className="section essay-route route-stop-section"
          id="stop-5"
          data-route-stop="5"
          aria-labelledby="stop-5-title"
          tabIndex={-1}
        >
          <div className="section-marker"><span>02</span><small>About 4 min</small></div>
          <div className="section-body">
            <p className="kicker">The smallest useful record</p>
            <h2 id="stop-5-title">Three questions before the answer.</h2>

            <div className="relation-state-grid" aria-label="Three plain relation states">
              <article><span>Shared path</span><p>A report traces to an earlier artifact. Preserve the report; do not count it as a new support path under this rule.</p></article>
              <article><span>Separate only in this test</span><p>An illustration stipulates a separate root. That is a property of the test, not a discovery about the real web.</p></article>
              <article><span>Unresolved</span><p>The relationship has not been established. Missing knowledge is not dependence or independence.</p></article>
            </div>

            <p>Unknown is where a polished summary is most tempted to put a guess. Leaving the relation unresolved is how an incomplete trail stays incomplete instead of becoming invented corroboration.</p>

            <section className="compact-receipt" aria-labelledby="compact-receipt-title">
              <div>
                <p className="card-label">Receipt ORIGIN-EX-01</p>
                <h3 id="compact-receipt-title">A five-field record another person can contest.</h3>
                <p>This is not a ranking, provenance discovery, truth verdict, or automatic decision.</p>
              </div>
              <dl>
                <div><dt>Claim</dt><dd>“The tool is broadly validated.”</dd></div>
                <div><dt>Observations</dt><dd>O01–O09 · nine report records</dd></div>
                <div><dt>Relation</dt><dd>All nine trace to Origin A · one announcement</dd></div>
                <div><dt>Permission</dt><dd>Sandbox only · no production data · ninety minutes</dd></div>
                <div><dt>Human next step</dt><dd><strong>HOLD · verify another origin relation</strong></dd></div>
              </dl>
            </section>

            <div className="three-question-list">
              <article>
                <span>01</span>
                <div>
                  <h3>Can we inspect what we saw and where it came from?</h3>
                  <p>Keep a report distinct from the thing it reports, a capture from a mutable page, a normalized extract from the capture, and a later summary. Record which transformation happened, when, and by whom or what.</p>
                  <p>The technical word for that trace is <Term id="home-provenance" label="Provenance" definition="A record of where material came from, how it changed, who or what handled it, and when." example="Nine reports can trace to one launch announcement while remaining nine preserved observations." boundary="Provenance does not prove correctness, authority, permission, claim support, or real-world independence.">provenance</Term>. The trace is useful precisely because it does not silently upgrade the material.</p>
                </div>
              </article>
              <article>
                <span>02</span>
                <div>
                  <h3>Does it bear on this exact claim?</h3>
                  <p>A report can be relevant without supporting the claim in view. A source can be authoritative for one narrow question and silent about another. A citation can be present while the passage contradicts, qualifies, or never reaches the proposition being made.</p>
                  <p>Keep three judgments visible: where the report came from; what exact claim it supports, refutes, or leaves unsettled; and what authority, relevance, and permission it has for this decision. Relation and support are connected, but they are not interchangeable.</p>
                </div>
              </article>
              <article>
                <span>03</span>
                <div>
                  <h3>May we use it, and what should happen next?</h3>
                  <p>Technical access is not permission. A team may inspect material but not retain it. It may have enough evidence for one bounded sandbox check but not for production use. It may hold, clarify, acquire one missing perspective, answer provisionally, defer, escalate, or refuse.</p>
                  <p>Record the permission and the accountable person’s <Term id="home-disposition" label="Recorded human next step" definition="The action an accountable person records after reviewing the evidence and constraints." example="HOLD means do not act on the broad claim yet; verify another relation first." boundary="The decision is not a new fact about the world and does not erase the evidence.">next step</Term>.</p>
                </div>
              </article>
            </div>

            <MicroVisual variant="trace-hold" />

            <div className="correction-invariant">
              <p className="card-label">The correction test</p>
              <h3>A review control must change something downstream.</h3>
              <p>If a reviewer changes a relation from shared path to unresolved, the count and route should change while the original report remains in history. If nothing downstream changes, the control is decorative.</p>
              <p><strong>Recurrence is not support; provenance is not correctness; access is not permission; a human next step is not a fact.</strong></p>
            </div>

            <p className="status-boundary">No study has run and no empirical improvement is claimed. The argument here is a design proposal that can be inspected before any experiment exists.</p>
            <aside className="route-stop-end" aria-label="End of the four-minute route">
              <strong>Stop here after about four minutes.</strong>
              <span>Inspect the path, test support against the exact claim, preserve permission and uncertainty, and let a person change the route without erasing what was observed.</span>
              <a href="#stop-12-15">Continue to the full argument ↓</a>
            </aside>
          </div>
        </section>

        <section
          className="section essay-route route-stop-section"
          id="stop-12-15"
          data-route-stop="9"
          aria-labelledby="stop-12-15-title"
          tabIndex={-1}
        >
          <div className="section-marker"><span>03</span><small>About 9 min</small></div>
          <div className="section-body">
            <p className="kicker">One preserved history</p>
            <h2 id="stop-12-15-title">Two loops, a use boundary, and a proposal that can lose.</h2>

            <div className="essay-loop-grid">
              <article>
                <p className="card-label">While the current question is open</p>
                <h3>Change what is available to this decision.</h3>
                <p>A missing expected perspective may justify one targeted search. A contradiction may justify comparison. A permission boundary or budget may stop the route. A corrected relation may change which support is counted.</p>
              </article>
              <article>
                <p className="card-label">After a defined outcome exists</p>
                <h3>Propose a rule for a future decision.</h3>
                <p>Compare what was expected with what happened, then propose a new policy with an owner and version. A later outcome cannot travel backward and make the original evidence omniscient.</p>
              </article>
            </div>
            <p>Both loops preserve observations, interpretations, decisions, outputs, corrections, and outcomes as different records. A correction supersedes an interpretation; it does not erase a report.</p>
            <p>The responsibility can live in careful practice, in a coordinating workflow, or partly in model behavior. Prompts and training may encourage search, abstention, and uncertainty, but they cannot replace identity, authorization, receipts, append-only history, or accountable human authority. These are placements, not maturity levels. A named component earns nothing merely by being named.</p>

            <div className="use-boundary">
              <div>
                <p className="card-label">The receipt may earn its cost when</p>
                <ul>
                  <li>a decision is consequential, contested, or likely to be revisited;</li>
                  <li>reports are likely to share sources or missing perspectives matter;</li>
                  <li>research is costly, permissions constrain use, or the source path affects the decision.</li>
                </ul>
              </div>
              <div>
                <p className="card-label">Use a lighter route when</p>
                <ul>
                  <li>the task is a low-stakes rewrite or direct format conversion;</li>
                  <li>the supplied inputs are complete and the calculation is bounded;</li>
                  <li>a short brief, exact inputs, clear citations, and ordinary review already solve the problem.</li>
                </ul>
              </div>
            </div>
            <p>A framework that cannot say when it is not worth using becomes a demand for ceremony.</p>

            <section className="precedent-boundary" aria-labelledby="precedent-boundary-title">
              <p className="kicker">The easy novelty claim is gone</p>
              <h3 id="precedent-boundary-title">Selected precedents narrow what remains.</h3>
              <p>Source dependence, double-counting controls, provenance, duplicate detection, claim graphs, retrieval diversity, evidence synthesis, and human review are established territory. The linked ledger keeps standards, published work, datasets, and preprints in their actual status categories rather than calling them one authority class.</p>
              <p>The remaining contribution is smaller: a synthesis that keeps those boundaries visible, plus one proposed test. In plain language, the test asks whether a supplied relation note stops one model from counting repeated material as independent support any better than simply telling it the rule in words. It does not infer provenance, establish real-world independence, prove truth, demonstrate human benefit, or validate the whole framework.</p>
              <a className="text-link" href="/sources">Inspect the source and status ledger →</a>
            </section>

            <section className="essay-objections" aria-labelledby="essay-objections-title">
              <p className="kicker">How this could lose</p>
              <h3 id="essay-objections-title">A serious proposal names its retirement conditions.</h3>
              <div className="counter-grid">
                {objections.map((objection, index) => (
                  <article key={objection.title}>
                    <span>Challenge {String(index + 1).padStart(2, "0")}</span>
                    <h4>{objection.title}</h4>
                    <p>{objection.body}</p>
                  </article>
                ))}
              </div>
            </section>

            <section className="research-bridge" aria-labelledby="research-bridge-title">
              <p className="status-pill">Proposed comparison · no model selected · no study run · no result</p>
              <p className="kicker">One narrow empirical question</p>
              <h3 id="research-bridge-title">Does a supplied origin-relation note change counting beyond an explicit rule?</h3>
              <p>Put simply: does showing the model a relationship note change how it counts repeated material, beyond merely telling it the counting rule?</p>
              <p>Local test machinery can create fictional bundles, reject malformed records, and exercise scoring code. That is not a model finding.</p>
              <ol className="plain-condition-list">
                <li><strong>Ordinary version:</strong> evidence assessment without an origin-counting rule or supplied relation note.</li>
                <li><strong>Rule-only version:</strong> the same evidence plus an explicit rule not to count repeated paths as separate support.</li>
                <li><strong>Added-cue version:</strong> the same rule and evidence plus supplied notes for shared, separate-in-this-test, or unresolved relations.</li>
              </ol>
              <p>The narrow comparison is added-cue against rule-only. A positive difference could show a response to the visible field in this frozen configuration. It could also reflect code identity, formatting, position, invalid-output differences, or another shortcut. It could not show that the model discovered provenance or understood real-world independence.</p>
              <p>One draft proposes 300 fictional cases, subject to design checks; no run has occurred. Exact sample and safety intervals, the selected model and its text processing, matched resources, shortcut controls, semantic review, and count/claim/evidence coherence remain open Lab gates. Real syndication is a later descriptive, rights-gated track outside the primary comparison.</p>
              <p><strong>The program commits in advance to keeping an unhelpful result.</strong> If the cue does nothing, makes the model worse, only changes invalid answers, works by reading a direct code, breaks under noise, or behaves unstably, that is what the record will say. A negative result shrinks or retires the mechanism claim; it is not hidden or spun into success.</p>
              <a className="text-link" href="/lab">Inspect the exact open gates in Lab →</a>
            </section>

            <section className="continuity-note continuity-note-v15-2" aria-labelledby="history-title">
              <span className="continuity-mark" aria-hidden="true">v13 → v15.2</span>
              <div>
                <p className="kicker">The map that came before</p>
                <h3 id="history-title">The center moved; the caution survived.</h3>
                <p>The v13 map asked how to find specialist comments, unanswered questions, unusual changes, and prior observations that generic workflows miss. Its original image remains unchanged as a historical anchor.</p>
                <p className="pull-quote">Underweighted is a starting condition, not a conclusion.</p>
                <p>Peripheral material is a candidate acquisition strategy, not a truth signal. A velocity anomaly deserves attention, not belief. The old picture is not the current topology; v15.2 keeps typed relations, recorded decisions, correction, and separately versioned outcomes visible.</p>
              </div>
              <figure className="origin-map-figure">
                <p className="origin-boundary">Historical reference · v13 · not the v15.2 system map</p>
                <a href="/images/v13-six-families-origin-map.png" aria-label="Open the full-resolution historical v13 Six Families Map">
                  <img
                    src="/images/v13-six-families-origin-map.png"
                    width="1024"
                    height="1536"
                    alt="Historical v13 Six Families Map: peripheral signal mining at the center, surrounded by source weighing, absence and memory, structured patterns, velocity, implementation, and a learning loop, followed by a seven-step workflow."
                  />
                </a>
                <figcaption><strong>Historical origin map · v13</strong><span>Preserved unchanged. Its seven-step strip is historical—not the v15.2 topology or evidence.</span></figcaption>
                <details className="origin-text-summary">
                  <summary>Read the historical map as text</summary>
                  <p>V13 placed Peripheral Signal Mining at the center of six families: source weighing; velocity; absence and memory; structured patterns; learning; and implementation.</p>
                  <ol>
                    <li>Collect widely, including weak signals and non-traditional sources.</li>
                    <li>Score and weight sources by convergence and quality.</li>
                    <li>Detect gaps and what is missing using memory and longitudinal context.</li>
                    <li>Compare patterns and sources to surface repeats and outliers.</li>
                    <li>Measure velocity to catch early change and anomalies.</li>
                    <li>Produce a ranked shortlist of signals for decision and action.</li>
                    <li>Update weights and baselines through the learning loop.</li>
                  </ol>
                </details>
              </figure>
            </section>

            <div className="closing-habit">
              <p className="kicker">What to remember</p>
              <blockquote>Before saying “many sources agree,” count the observations, inspect how many distinct information paths they represent, ask what exact claim each path supports, leave unresolved relations unresolved, and record what a person will do next.</blockquote>
              <p>The aim is not to count less. It is to count the declared unit and keep unlike judgments from laundering one another.</p>
              <p>That is a design proposition, not a result. The next honest step is to try the smaller receipt, then run or retire the narrow comparison only if its gates are authorized.</p>
            </div>

            <aside className="route-stop-end" aria-label="End of the full argument">
              <strong>Stop here after the roughly nine-minute full argument.</strong>
              <span>The public thought piece is complete. The framework records, bounded cases, protocol gates, source statuses, glossary, and historical evidence remain optional deeper routes.</span>
              <div><a href="/explore">Explore the records →</a><a href="/lab">Open the no-results Lab →</a><a href="/sources">Read sources and terms →</a></div>
            </aside>
          </div>
        </section>

        <footer>
          <p>Local owner review · conceptual synthesis · not published · no empirical result</p>
          <p>Pattern Recognition · The Discrimination Layer · v15.2</p>
        </footer>
      </div>
    </main>
  );
}
