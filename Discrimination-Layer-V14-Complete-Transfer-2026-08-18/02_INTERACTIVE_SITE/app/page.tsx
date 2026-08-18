/* eslint-disable @next/next/no-img-element, jsx-a11y/no-noninteractive-tabindex -- Static export uses audited local rasters; the labelled overflow region is intentionally keyboard-focusable. */
import ReadingNav from "./ReadingNav";
import CollapseControl from "./CollapseControl";
import { componentMaturity, families, glossary, researchPaths, sources } from "./content";

const distinctions = [
  ["Attention priority", "Truth"],
  ["Domain source authority", "Universal trust"],
  ["Claim support", "Source popularity"],
  ["Recurrence", "Independence"],
  ["Independence", "Different URLs, wording, or unknown origin"],
  ["Relevance", "General importance"],
  ["Operational authorization", "Source authority or technical access"],
  ["Enrichment value", "Action priority or acceptance"],
  ["Action priority", "A factual conclusion or truth probability"],
  ["Provenance", "Correctness"],
  ["Owner disposition", "External truth"],
  ["Signal candidate", "A verified event or conclusion"],
];

const counterarguments = [
  ["Old work, new label", "The mechanisms reviewed here already have mature precedents. The plausible contribution is a boundary-preserving synthesis and an evaluation agenda—not a new mechanism family."],
  ["A new gatekeeper", "Any selection policy can reinforce institutional bias or erase peripheral evidence. Exclusions, unknowns, reasons, appeal, and source diversity must stay inspectable."],
  ["Rigor theater", "Detailed provenance can trace a false claim perfectly. Lineage never upgrades correctness, independence, or permission by itself."],
  ["More cost than value", "The architecture may be too slow and cognitively heavy. It must beat strong simple baselines under matched time, tokens, retrieval, and review effort."],
  ["Decorative human review", "A person placed after an opaque route may only rubber-stamp it. Review must expose the evidence path and permit a consequential correction."],
  ["Learning the wrong lesson", "Outcome feedback can encode preference, contaminated proxies, or hindsight. Updates need a predefined outcome, attribution limits, versioning, and approval."],
];

const limitations = [
  ["No empirical evaluation.", "This project reports no experiment, participant study, field outcome, or comparative performance result."],
  ["No claim of mechanism novelty.", "The components have extensive prior art, and the proposed integration may overlap a framework not yet found by the targeted review."],
  ["No proven minimum.", "Eleven components are an analytical decomposition, not evidence that every task needs eleven implemented modules."],
  ["No validated constructs.", "Reviewers may not reliably distinguish authority, support, independence, relevance, attention, enrichment value, action priority, and disposition."],
  ["Open-world evidence remains hard.", "Sources change, origins are obscured, important evidence is inaccessible, and support can remain contested."],
  ["Costs and utilities are uncertain.", "A clean stopping rule can still stop before rare decisive evidence or encode the wrong consequence model."],
  ["Human control is not guaranteed.", "Interfaces and organizational incentives can turn review into ceremony."],
  ["Memory can amplify error.", "Retention, retrieval, and summarization can preserve stale, biased, or manipulated content."],
  ["The name may fail.", "Discrimination layer may remain ambiguous or harmful despite an explicit technical definition."],
  ["The historical HTML is still pending.", "The original v13 diagram is now preserved and its supplied hash is verified; the expected standalone HTML remains unavailable and unverified."],
  ["Product cases are illustrative.", "Alpha Solver and Signal Foundry are related cases, not independent validation."],
  ["No publication or owner approval.", "This is a local review draft."],
];

const originObservationIds = ["O01", "O02", "O03", "O04", "O05", "O06", "O07", "O08", "O09"];

export default function Home() {
  return (
    <main id="main-content">
      <a className="skip-link" href="#five-minute">Skip to the five-minute overview</a>

      <aside className="rail" aria-label="Reading paths and status">
        <a className="wordmark" href="#start" aria-label="Pattern Recognition, return to start">
          <span>Pattern<br />Recognition</span><small>v14</small>
        </a>
        <ReadingNav />
        <p className="rail-status"><span aria-hidden="true" /> Local owner review</p>
      </aside>

      <div className="page-shell">
        <header className="masthead" id="start">
          <div className="masthead-meta">
            <p className="eyebrow">Personal systems memo · v14 · provisional</p>
          </div>
          <h1>Pattern Recognition<span aria-hidden="true"> / </span><em>The Discrimination Layer</em></h1>
          <p className="dek">A visual systems framework for deciding what information deserves acquisition, comparison, enrichment, and influence before AI generates.</p>
          <p className="title-definition"><strong>Here, discrimination means technical differentiation among information and possible actions—not social classification.</strong></p>
          <div className="thesis-callout">
            <span className="label">Working proposition<small>Conceptual synthesis · not empirical validation</small></span>
            <p><strong>Make the judgment before generation visible.</strong> Some evidence-sensitive AI workflows may benefit from an explicit, inspectable responsibility for deciding what context can influence generation. Whether that responsibility improves outcomes enough to justify its cost is an empirical question.</p>
          </div>
          <div className="route-choice" aria-label="Choose a reading path">
            <a className="route-card route-primary" href="#five-minute">
              <span className="route-time">Start here · about 5 minutes</span>
              <strong>Understand the idea</strong>
              <span>Problem, thesis, map, one example, and what remains unproven.</span>
            </a>
            <a className="route-card" href="#mechanisms">
              <span className="route-time">Complete path · about 25 minutes</span>
              <strong>Inspect the system</strong>
              <span>Eleven responsibilities, relationships, failures, cases, and research horizon.</span>
            </a>
          </div>
        </header>

        <section className="section section-intro" id="five-minute" aria-labelledby="five-minute-title">
          <div className="section-marker"><span>01</span><small>Five-minute overview</small></div>
          <div className="section-body">
            <p className="kicker">The problem</p>
            <h2 id="five-minute-title">The visible answer is often where hidden decisions surface.</h2>
            <p className="lead">A model can write a polished answer from a poor evidence environment. The failure appears at the end, but the consequential choices often happened before generation.</p>
            <aside className="quick-example" aria-label="Concrete preview of the worked example">
              <p className="card-label">Concrete preview</p>
              <p className="quick-example-line">Nine positive articles can still trace to one launch announcement.</p>
              <p>Repeated mentions remain separate observations, but they do not establish distinct-origin support under this packet’s relation rule.</p>
              <a href="#example">See the worked example ↓</a>
            </aside>

            <section className="route-receipt" id="origin-receipt" aria-labelledby="origin-receipt-title" aria-describedby="origin-receipt-boundary">
              <header className="route-receipt-header">
                <p className="kicker">Illustrative origin-accounting receipt · no verdict</p>
                <h3 id="origin-receipt-title">Nine observations can still represent one origin.</h3>
                <p id="origin-receipt-boundary">A receipt records relationships and a human disposition. It does not depict a required workflow, discover provenance, or establish truth.</p>
                <p className="route-receipt-meta">Receipt ORIGIN-EX-01 · fictional bundle · version 0.2 · no live data</p>
              </header>

              <dl className="route-receipt-frame" aria-label="Decision frame">
                <div><dt>Decision in view</dt><dd>Sandbox pilot of a data-migration tool</dd></div>
                <div><dt>Permission and budget</dt><dd>Sandbox only · 90 minutes of research · no production data</dd></div>
                <div><dt>Packet state</dt><dd><strong>HOLD</strong> · inspect separately authored evidence</dd></div>
                <div><dt>State meaning</dt><dd>The packet is insufficient for a broad validation claim. No automatic action is taken.</dd></div>
              </dl>

              <section className="route-receipt-claim" aria-labelledby="origin-receipt-claim-title">
                <h4 className="card-label" id="origin-receipt-claim-title">Claim under review</h4>
                <p>“The tool is broadly validated.”</p>
                <p><strong>INSUFFICIENT</strong> · nine mentions do not establish nine distinct origins.</p>
              </section>

              <section className="route-receipt-count" aria-labelledby="origin-receipt-count-title">
                <h4 id="origin-receipt-count-title">Count snapshot</h4>
                <dl>
                  <div><dt>Observations under review</dt><dd>09</dd></div>
                  <div><dt>Known common-origin clusters for those records</dt><dd>01</dd></div>
                  <div><dt>Supporting origins counted under the stated relation rule</dt><dd>00</dd></div>
                  <div><dt>Separate roots shown for comparison</dt><dd>02 <small>illustrative; support not assessed</small></dd></div>
                </dl>
                <p className="route-receipt-unknown"><strong>UNKNOWN stays unknown.</strong> Do not move an unresolved origin relation into the dependent or independent total.</p>
              </section>

              <section className="route-receipt-ledger" aria-labelledby="origin-receipt-ledger-title" aria-describedby="origin-receipt-ledger-note">
                <h4 id="origin-receipt-ledger-title">Observation ledger · nine unordered records</h4>
                <p id="origin-receipt-ledger-note">These rows preserve nine observations. Their order is not a workflow or confidence ranking.</p>
                <p className="route-receipt-mobile-summary">O01–O09 · Origin A · DEPENDENT · zero supporting origins counted under the stated relation rule</p>
                <div className="route-receipt-table-scroll" role="region" aria-labelledby="origin-receipt-ledger-title" aria-describedby="origin-receipt-scroll-note" tabIndex={0}>
                  <p id="origin-receipt-scroll-note" className="scroll-hint">On narrow screens, scroll this data table horizontally; the page itself does not scroll sideways.</p>
                  <table>
                    <caption>Typed relation ledger for the nine illustrative observations</caption>
                    <thead><tr><th scope="col">Record</th><th scope="col">Record kind</th><th scope="col">Origin relation</th><th scope="col">What this counts as</th></tr></thead>
                    <tbody>
                      {originObservationIds.map((record) => (
                        <tr key={record}><th scope="row">{record}</th><td>Report observation</td><td>Origin A · <strong>DEPENDENT</strong></td><td>Repeats the launch announcement; not separately rooted support under this relation rule.</td></tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </section>

              <div className="route-receipt-lower">
                <section aria-labelledby="origin-receipt-key-title">
                  <h4 id="origin-receipt-key-title">Origin relation key</h4>
                  <dl className="route-receipt-key">
                    <div><dt>DEPENDENT</dt><dd>Traceable to an existing artifact. Preserve the observation; do not count it as separately rooted support.</dd></div>
                    <div><dt>INDEPENDENT-AS-STIPULATED</dt><dd>A separate root declared by this illustration or benchmark—not provenance discovery.</dd></div>
                    <div><dt>UNKNOWN</dt><dd>The relation is not established. Preserve it; do not guess either way.</dd></div>
                  </dl>
                </section>
                <section aria-labelledby="origin-receipt-contrast-title">
                  <h4 id="origin-receipt-contrast-title">Separate roots shown for contrast</h4>
                  <ul><li><strong>B1</strong> · separate root · illustrative</li><li><strong>C1</strong> · separate root · illustrative</li></ul>
                  <p>Claim support is not assessed. These roots are not counted as support for the claim in this packet.</p>
                </section>
              </div>

              <section className="route-receipt-disposition" aria-labelledby="origin-receipt-disposition-title">
                <p className="card-label">Human disposition</p>
                <h4 id="origin-receipt-disposition-title">HOLD · VERIFY ANOTHER ORIGIN RELATION</h4>
                <p>Inspect the originating announcement, then look for a separately authored benchmark and document its origin relation before changing the claim state.</p>
                <p>No automatic admission, rejection, or truth verdict. A reviewer may correct this receipt; the fictional observations remain preserved.</p>
              </section>

              <p className="route-receipt-footer">Illustrative only · not a reported dataset · not a provenance audit · not a system runtime. No image is required to interpret the counts, relation types, or disposition.</p>
            </section>

            <ul className="question-grid">
              <li>What was available at all?</li><li>Which repetitions shared one origin?</li><li>What supported each claim?</li>
              <li>Was another search worth its cost?</li><li>What entered the final context?</li><li>Who could correct the decision?</li>
            </ul>
            <div className="definition-note">
              <p><strong>What the layer separates</strong> Authority, support, independence, relevance, authorization, and action priority remain different judgments.</p>
              <p><strong>Layer</strong> means a systems responsibility, not necessarily one service, model, prompt, or box.</p>
            </div>

            <div className="overview-grid">
              <article>
                <p className="card-label">The proposition</p>
                <h3>Make the pre-generation judgment inspectable.</h3>
                <p>The responsibility connects acquisition, source and artifact identity, common origin, claim support, task relevance, action cost, human disposition, and revisable memory.</p>
              </article>
              <article>
                <p className="card-label">The boundary</p>
                <h3>Coherence is not effectiveness.</h3>
                <p>No experiment here shows that the framework improves a decision. A simpler cited-retrieval workflow may perform just as well at lower cost.</p>
              </article>
            </div>

            <div className="continuity-note">
              <span className="continuity-mark" aria-hidden="true">v13 → v14</span>
              <div>
                <h3>The center of gravity moved, but the pulse remains.</h3>
                <p>The <a href="https://pattern-recognition-map.adonisdv23.chatgpt.site/">v13 visual map</a> asked how to find the specialist comment, anomalous change, repeated unanswered question, or memory that generic workflows miss. V14 asks the harder follow-on: what gives any item the right to influence the answer?</p>
                <p className="pull-quote">Underweighted is a starting condition, not a conclusion.</p>
              </div>
              <figure className="origin-map-figure">
                <p className="origin-boundary">Historical reference · v13 · not the v14 system map</p>
                <a href="/images/v13-six-families-origin-map.png" aria-label="Open the full-resolution historical v13 Six Families Map">
                  <img
                    src="/images/v13-six-families-origin-map.png"
                    width="1024"
                    height="1536"
                    loading="lazy"
                    alt="Historical v13 Six Families Map: peripheral signal mining at the center, surrounded by source weighing, absence and memory, structured patterns, velocity, implementation, and a learning loop, followed by a seven-step workflow."
                  />
                </a>
                <figcaption><strong>Historical origin map · v13</strong><span>Original diagram, hash verified. Its seven-step strip is historical—not the v14 system topology.</span></figcaption>
                <details className="origin-text-summary">
                  <summary>Read the historical map as text</summary>
                  <p>V13 placed Peripheral Signal Mining at the center of six families: source weighing; velocity; absence and memory; structured patterns; learning; and implementation.</p>
                  <ol>
                    <li>Collect widely, including weak signals and non-traditional sources.</li>
                    <li>Score and weight sources by convergence and quality.</li>
                    <li>Detect gaps and what is missing using memory and longitudinal context.</li>
                    <li>Compare across the patterns engine and source sets to surface repeats and outliers.</li>
                    <li>Measure velocity to catch early change and anomalies.</li>
                    <li>Produce a ranked shortlist of signals for decision and action.</li>
                    <li>Continuously update weights and baselines through the learning loop.</li>
                  </ol>
                  <p>V14 replaces that center-and-sequence emphasis with inspectable responsibilities, typed relations, terminal states, human correction, and separately versioned outcome updates.</p>
                </details>
              </figure>
            </div>

            <div className="distinction-block" aria-labelledby="distinction-title">
              <div className="heading-row compact-heading">
                <div><p className="kicker">The distinction contract</p><h3 id="distinction-title">Keep unlike judgments unlike.</h3></div>
                <a className="text-link" href="#glossary">Full glossary ↓</a>
              </div>
              <div className="distinction-grid">
                {distinctions.map(([left, right]) => (
                  <p key={left}><strong>{left}</strong><span>is not</span>{right}</p>
                ))}
              </div>
            </div>

            <div className="use-boundary">
              <div>
                <p className="card-label">Worth the overhead when</p>
                <ul>
                  <li>claims are consequential, disputed, time-sensitive, or source-dependent;</li>
                  <li>reports may share one origin or missing perspectives matter;</li>
                  <li>acquisition is costly, permissions constrain use, or later outcomes can be defined.</li>
                </ul>
              </div>
              <div>
                <p className="card-label">Probably unnecessary when</p>
                <ul>
                  <li>the task is a low-stakes rewrite or direct creative work;</li>
                  <li>the supplied inputs are complete and the calculation is bounded;</li>
                  <li>ordinary retrieval, clear citations, and review solve the problem.</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <section className="section system-section" id="map" aria-labelledby="map-title">
          <div className="section-marker"><span>02</span><small>System map</small></div>
          <div className="section-body">
            <div className="heading-row">
              <div><p className="kicker">Six families · eleven responsibilities</p><h2 id="map-title">The judgment before generation</h2></div>
              <a className="text-link" href="#map-text">Skip the family map → text version</a>
            </div>
            <div className="system-map" role="group" aria-label="Six framework families; the two-loop relationship diagram follows in section 04">
              {families.map((family) => (
                <a className={`family family-${family.tone}`} href={`#family-${family.number}`} key={family.number}>
                  <span className="family-number">{family.number}</span>
                  <strong>{family.name}</strong>
                  <small>{family.question}</small>
                  <span className="component-count">{family.components.map((component) => component.id).join(" · ")}</span>
                </a>
              ))}
              <div className="loop-note"><span aria-hidden="true">↺</span> Human correction and later outcomes can revise the route without rewriting the evidence.</div>
            </div>
            <ol className="map-text" id="map-text">
              <li>A bounded question and permission envelope governs acquisition.</li>
              <li>Captured material receives source, artifact, version, and derivation records.</li>
              <li>Relationship and claim views expose origin, support, contradiction, and gaps.</li>
              <li>Separate assessments inform a cost-bounded next action.</li>
              <li>A human can correct the route; evidence and decisions remain separately versioned.</li>
              <li>A defined later outcome may motivate an approved policy update.</li>
            </ol>
            <div className="legend" aria-label="Evidence status legend">
              <span><i className="dot dot-evidence" aria-hidden="true" /> Evidence: a bounded mechanism has cited precedent</span>
              <span><i className="dot dot-hypothesis" aria-hidden="true" /> Hypothesis: a synthesis, design, or relationship still needs evaluation</span>
              <span><i className="dot dot-example" aria-hidden="true" /> Example: illustrative, not a result</span>
              <span><i className="dot dot-unresolved" aria-hidden="true" /> Unresolved: open design or research question</span>
            </div>
          </div>
        </section>

        <section className="section mechanism-section" id="mechanisms" aria-labelledby="mechanisms-title">
          <div className="section-marker"><span>03</span><small>Mechanisms</small></div>
          <div className="section-body">
            <p className="kicker">Complete path</p>
            <h2 id="mechanisms-title">Eleven responsibilities, each open to inspection.</h2>
            <p className="lead">The map is deliberately more explicit than an eventual interface. Expand any component for its inputs, outputs, dependencies, failure modes, evidence boundary, and unresolved questions.</p>

            <div className="family-stack">
              {families.map((family) => (
                <section className={`family-detail family-detail-${family.tone}`} id={`family-${family.number}`} key={family.number} aria-labelledby={`family-title-${family.number}`}>
                  <header className="family-detail-head">
                    <span className="family-index">Family {family.number}</span>
                    <div>
                      <h3 id={`family-title-${family.number}`}>{family.name}</h3>
                      <p>{family.question}</p>
                    </div>
                    <p className="family-output"><span>Principal output</span>{family.output}</p>
                  </header>
                  <div className="component-list">
                    {family.components.map((component) => (
                      <details className="component" id={component.id.toLowerCase()} key={component.id}>
                        <summary>
                          <span className="component-id">{component.id}</span>
                          <span className="component-summary"><strong>{component.name}</strong><small>{component.summary}</small></span>
                          <span className="expand-label" aria-hidden="true">Inspect</span>
                        </summary>
                        <div className="component-body">
                          <p className="component-progress">{component.id} · eight-field inspection record</p>
                          <dl>
                            <div><dt>Why it exists</dt><dd>{component.why}</dd></div>
                            <div><dt>Consumes</dt><dd>{component.consumes}</dd></div>
                            <div><dt>Produces</dt><dd>{component.produces}</dd></div>
                            <div><dt>How it interacts</dt><dd>{component.interacts}</dd></div>
                            <div><dt>What can go wrong</dt><dd>{component.risks}</dd></div>
                            <div><dt>Example</dt><dd><span className="inline-status status-example">Illustrative</span>{component.example}</dd></div>
                            <div><dt>Evidence boundary</dt><dd><span className={`inline-status status-${componentMaturity[component.id].kind}`}>{componentMaturity[component.id].label}</span>{component.support}</dd></div>
                            <div><dt>What remains speculative</dt><dd><span className="inline-status status-unresolved">Unresolved</span>{component.speculative}</dd></div>
                          </dl>
                          <div className="component-exits">
                            <CollapseControl componentId={component.id} />
                            <a className="return-link" href="#map">Return to system map ↑</a>
                          </div>
                        </div>
                      </details>
                    ))}
                  </div>
                </section>
              ))}
            </div>
          </div>
        </section>

        <section className="section connections-section" id="connections" aria-labelledby="connections-title">
          <div className="section-marker"><span>04</span><small>Connections</small></div>
          <div className="section-body">
            <p className="kicker">Two loops · one preserved history</p>
            <h2 id="connections-title">The flow is not a conveyor belt.</h2>
            <p className="lead">A gap can trigger another acquisition. A reviewer can revise the question. A failed capture can end a branch. An outcome can propose—but never silently apply—a new policy.</p>
            <figure className="loop-figure" aria-labelledby="loop-figure-title">
              <figcaption>
                <p className="card-label">Relationship diagram</p>
                <h3 id="loop-figure-title">One fast loop. One slower loop.</h3>
                <p>The first can change the evidence available to a current decision. The second can propose a policy for a future decision. Neither rewrites history.</p>
              </figcaption>
              <div className="loop-lane loop-lane-evidence">
                <div className="loop-lane-title"><span>Loop A</span><strong>Evidence enrichment</strong><small>within one decision</small></div>
                <ol className="loop-track" aria-label="Evidence enrichment loop sequence">
                  <li><small>Observe</small><strong>Evidence graphs</strong></li>
                  <li className="loop-arrow" aria-hidden="true">→</li>
                  <li><small>Separate</small><strong>Assessments</strong></li>
                  <li className="loop-arrow" aria-hidden="true">→</li>
                  <li><small>Choose</small><strong>Router</strong></li>
                  <li className="loop-arrow" aria-hidden="true">→</li>
                  <li><small>Permit</small><strong>Acquisition</strong></li>
                </ol>
                <p className="loop-return"><span aria-hidden="true">↶</span><strong>New captured evidence returns to the graphs.</strong> A stop rule, cost, or permission boundary can end the loop.</p>
              </div>
              <div className="loop-lane loop-lane-learning">
                <div className="loop-lane-title"><span>Loop B</span><strong>Outcome revision</strong><small>across decisions</small></div>
                <ol className="loop-track" aria-label="Outcome revision loop sequence">
                  <li><small>Preserve</small><strong>Decision</strong></li>
                  <li className="loop-arrow" aria-hidden="true">→</li>
                  <li><small>Observe</small><strong>Outcome</strong></li>
                  <li className="loop-arrow" aria-hidden="true">→</li>
                  <li><small>Propose</small><strong>Update</strong></li>
                  <li className="loop-arrow" aria-hidden="true">→</li>
                  <li><small>Review</small><strong>Human disposition</strong></li>
                </ol>
                <p className="loop-return"><span aria-hidden="true">↶</span><strong>Only an approved new policy changes future routing.</strong> The original evidence, decision, and policy version remain intact.</p>
              </div>
            </figure>
            {/* Keyboard focus makes the horizontally scrollable comparison reachable at narrow widths. */}
            <div className="state-table" role="region" aria-labelledby="state-table-title" tabIndex={0}>
              <h3 id="state-table-title">Four record types that must not overwrite one another</h3>
              <p className="scroll-hint">On narrow screens, scroll this comparison horizontally.</p>
              <table>
                <thead><tr><th scope="col">Record</th><th scope="col">Example</th><th scope="col">Revision rule</th></tr></thead>
                <tbody>
                  <tr><th scope="row">Observation</th><td>A captured issue report contains a rollback account.</td><td>Preserve; append a correction or supersession.</td></tr>
                  <tr><th scope="row">Interpretation</th><td>The report may indicate a failure mode.</td><td>Revise with reason; never recast as observed fact.</td></tr>
                  <tr><th scope="row">Decision</th><td>Run one synthetic-data rollback check.</td><td>Version with the brief, route, owner, and cost.</td></tr>
                  <tr><th scope="row">Outcome</th><td>The predefined sandbox check passed or failed.</td><td>Record horizon and confounders; propose policy change separately.</td></tr>
                </tbody>
              </table>
            </div>
            <section className="implementation-paths" aria-labelledby="implementation-paths-title">
              <p className="kicker">Three implementation paths</p>
              <h3 id="implementation-paths-title">Different placements, not maturity levels.</h3>
              <p>The responsibility can live in team practice, workflow coordination, model behavior, or a combination. None is inherently deeper or more defensible.</p>
              <div className="path-grid">
                <article><span>Practice</span><strong>Make the judgment explicit in existing work.</strong><p>Define the decision, separate evidential judgments, record material exclusions, and state why research stopped.</p></article>
                <article><span>System</span><strong>Coordinate evidence, policy, review, and memory.</strong><p>Assemble an inspectable context packet while preserving provenance, permissions, and correction.</p></article>
                <article><span>Model</span><strong>Encourage information seeking and abstention.</strong><p>Training or agent policies may help, but cannot replace external identity, receipts, permissions, or human authority.</p></article>
              </div>
            </section>
          </div>
        </section>

        <section className="section example-section" id="example" aria-labelledby="example-title">
          <div className="section-marker"><span>05</span><small>Worked example</small></div>
          <div className="section-body">
            <p className="status-pill">Illustrative example · not a reported result</p>
            <h2 id="example-title">Nine positive articles. One launch announcement.</h2>
            <p className="lead">A technical team is deciding whether to run a sandbox pilot of a data-migration tool. A flat summary sees popularity. The framework sees a chain of different questions.</p>
            <figure className="example-visual">
              <img
                src="/images/nine-mentions-one-origin.jpg"
                width="1536"
                height="1024"
                loading="lazy"
                decoding="async"
                alt="Illustrative—not factual—scene of one coral source artifact branching into nine differently styled report fragments, beside two separately rooted evidence fragments. The common origin does not mean the reports are false."
              />
              <figcaption><strong>Many mentions can preserve one origin.</strong><span>In this illustration: nine observations share one known origin; two artifacts have separate roots. Repetition is neither erased nor treated as proof—and common origin does not make a report false.</span><small>Illustration only · colors encode no status · not a reported dataset, provenance audit, or result</small></figcaption>
            </figure>
            <div className="example-contrast" aria-label="Flat summary compared with discrimination-layer questions">
              <article><p className="card-label">A flat summary says</p><p>“Nine positive articles make the tool look broadly validated. A pilot appears low-risk.”</p></article>
              <article><p className="card-label">The layer asks</p><p>How many distinct origins are documented under the packet’s relation rule? Which exact claims are supported? What would change a sandbox-only decision?</p></article>
            </div>
            <ol className="example-grid">
              <li><span>Step 1</span><strong>Bound the decision</strong><p>Sandbox only. No production data. Ninety minutes of research.</p></li>
              <li><span>Step 2</span><strong>Trace the material</strong><p>Nine positive articles paraphrase the same vendor announcement.</p></li>
              <li><span>Step 3</span><strong>Split the claims</strong><p>Nine mentions remain nine observations, but not nine separately rooted confirmations under the packet’s relation rule.</p></li>
              <li><span>Step 4</span><strong>Keep judgments separate</strong><p>Official documentation can be authoritative while still sharing a known origin under that rule.</p></li>
              <li><span>Step 5</span><strong>Choose one bounded step</strong><p>Inspect the benchmark method and reproduce one rollback path locally.</p></li>
              <li><span>Step 6</span><strong>Preserve the outcome</strong><p>A later sandbox result may change a pilot rule, not external truth.</p></li>
            </ol>
            <div className="example-result">
              <p className="card-label">What the packet says</p>
              <p>“The tool documents rollback. Its comparative speed claim remains vendor-supported only. Two failure reports are relevant but not prevalence evidence. Nine positive articles share one known origin. A bounded synthetic-data check is warranted before a sandbox-only pilot decision.”</p>
            </div>
          </div>
        </section>

        <section className="section challenge-section" id="challenges" aria-labelledby="challenges-title">
          <div className="section-marker"><span>06</span><small>Challenges &amp; limits</small></div>
          <div className="section-body">
            <p className="kicker">Failure is part of the specification</p>
            <h2 id="challenges-title">A serious framework names how it could lose.</h2>
            <div className="counter-grid">
              {counterarguments.map(([title, body], index) => (
                <article key={title}><span>Challenge {String(index + 1).padStart(2, "0")}</span><h3>{title}</h3><p>{body}</p></article>
              ))}
            </div>
            <div className="falsifier-panel">
              <p className="card-label">What would materially weaken or retire the framework for a named task class?</p>
              <ul>
                <li>A strong retrieval-plus-citation baseline performs equivalently at lower cost.</li>
                <li>Reviewers cannot reliably distinguish authority, support, independence, relevance, and action priority.</li>
                <li>Origin-aware grouping hides legitimate convergence as often as it prevents false corroboration.</li>
                <li>The interface increases overload, review time, or overreliance enough to erase any benefit.</li>
                <li>Outcome updates encode local preference or contaminated proxies rather than better policy.</li>
              </ul>
            </div>
            <div className="limitations-block" aria-labelledby="limitations-title">
              <p className="kicker">Current limitations</p>
              <h3 id="limitations-title">Twelve boundaries the presentation cannot smooth away.</h3>
              <ol className="limitations-list">
                {limitations.map(([title, body]) => <li key={title}><strong>{title}</strong><span>{body}</span></li>)}
              </ol>
            </div>
            <p className="rename-note"><strong>Terminology test:</strong> if representative readers keep inferring a social-classification thesis after the definition, rename it. <em>Context judgment layer</em> is the current clean alternative.</p>
          </div>
        </section>

        <section className="section case-section" id="cases" aria-labelledby="cases-title">
          <div className="section-marker"><span>07</span><small>Bounded cases</small></div>
          <div className="section-body">
            <p className="kicker">Translation, not validation</p>
            <h2 id="cases-title">Two products make the responsibilities concrete.</h2>
            <div className="case-grid">
              <article>
                <p className="case-name">Alpha Solver</p>
                <h3>A reasoning posture, not proof.</h3>
                <p className="case-boundary"><strong>Boundary:</strong> repository structure and product intent do not show that the framework improves reasoning quality, safety, or outcomes.</p>
                <p>The inspected Alpha Solver documents are intended to illustrate how a decision brief, explicit assumptions, alternatives, tool permissions, and reviewable reasoning can constrain a solution path.</p>
              </article>
              <article>
                <p className="case-name">Signal Foundry</p>
                <h3>Evidence responsibilities, not a universal model.</h3>
                <p className="case-boundary"><strong>Boundary:</strong> those safeguards are product-specific design choices, not empirical support for eleven general responsibilities.</p>
                <p>The inspected Signal Foundry boundary documents specify examples of immutable raw acquisition, exclusion boundaries, source-aware evidence, staged import, and separation between transcript and visual evidence.</p>
              </article>
            </div>
            <div className="enterprise-translation">
              <div><p className="card-label">Enterprise translation</p><h3>Identity, policy, receipts, review, versioning.</h3></div>
              <p>The framework can map to role-based authorization, lineage systems, policy engines, approval queues, evaluation records, and risk-management controls. That mapping does not establish compliance, safety, or return on investment in any deployment.</p>
            </div>
          </div>
        </section>

        <section className="section research-section" id="research" aria-labelledby="research-title">
          <div className="section-marker"><span>08</span><small>Research horizon</small></div>
          <div className="section-body">
            <p className="kicker">One immediate study · wider program remains provisional</p>
            <h2 id="research-title">The next artifact depends on the claim we choose to test.</h2>
            <p className="lead">The current work is a practitioner thought piece with an academic readiness path. It should not be styled as a paper until a contribution type, prior-art protocol, methods, data, participants, outcomes, and falsifiers are fixed in advance.</p>
            <aside className="first-paper-panel" aria-labelledby="first-paper-title">
              <p className="card-label">Narrowest credible first paper</p>
              <h3 id="first-paper-title">Does oracle origin-relation metadata change false corroboration in one frozen model?</h3>
              <div>
                <p><strong>Proposed design—not a result.</strong> Eighty development and forty feasibility-only pilot bundles before locking three hundred primary and sixty stress bundles.</p>
                <p><strong>Compare exactly.</strong> Citation-only, an explicit origin-counting rule, and the byte-identical rule plus relation metadata, with exact F1/F2 token parity and one frozen model.</p>
                <p><strong>Let it lose.</strong> The all-assigned typed-cue condition must reduce risk-coded false corroboration beyond the rule while passing a fixed-set, five-point candidate safety margin for recall of stipulated supporting origins. This measures an observable condition effect—not internal reasoning, provenance discovery, or the full layer.</p>
              </div>
            </aside>
            <div className="research-grid">
              {researchPaths.map((path, index) => (
                <article key={path.name}>
                  <span>{String(index + 1).padStart(2, "0")}</span>
                  <h3>{path.name}</h3>
                  <p><strong>Question.</strong> {path.question}</p>
                  <p><strong>Evidence burden.</strong> {path.proof}</p>
                </article>
              ))}
            </div>
            <div className="research-sequence" aria-label="Recommended research sequence">
              <span>1 · implement + audit</span><i aria-hidden="true">→</i><span>2 · feasibility-only pilot</span><i aria-hidden="true">→</i><span>3 · preregistered F2 vs F1</span><i aria-hidden="true">→</i><span>4 · choose one separate next study</span>
            </div>
            <p className="document-link">Canonical manuscript: <code>source/THOUGHT_PIECE_V14.md</code></p>
          </div>
        </section>

        <section className="section source-section" id="sources" aria-labelledby="sources-title">
          <div className="section-marker"><span>09</span><small>Sources</small></div>
          <div className="section-body">
            <p className="kicker">Selected primary and official references</p>
            <h2 id="sources-title">Prior art narrows the claim.</h2>
            <p className="lead">The mechanisms reviewed here have mature precedents in adjacent fields. These sources support only the bounded points named below; they do not validate the synthesis.</p>
            <ol className="source-list">
              {sources.map((source) => (
                <li key={source.url}><a href={source.url}>{source.label}</a><p>{source.use}</p></li>
              ))}
            </ol>

            <div className="glossary" id="glossary" aria-labelledby="glossary-title">
              <div className="heading-row compact-heading"><div><p className="kicker">Interpretation guardrail</p><h3 id="glossary-title">Compact glossary</h3></div><a className="text-link" href="#start">Back to start ↑</a></div>
              <dl>
                {glossary.map(([term, definition]) => <div key={term}><dt>{term}</dt><dd>{definition}</dd></div>)}
              </dl>
            </div>
          </div>
        </section>

        <section className="closing" aria-labelledby="closing-title">
          <p className="kicker">Owner review prompt</p>
          <h2 id="closing-title">Does the framework make the hidden judgment easier to inspect—or merely more elaborate?</h2>
          <p>The strongest current claim is deliberately modest: this is a coherent, historically grounded synthesis worth examining. It is not complete, empirically validated, or novel as a scientific mechanism.</p>
          <div className="closing-links"><a href="#map">Revisit the map ↑</a><a href="#challenges">Revisit the counterarguments ↑</a></div>
        </section>

        <footer>
          <p>Local owner review · not published · not empirically validated</p>
          <p>Pattern Recognition · The Discrimination Layer · v14</p>
        </footer>
      </div>
    </main>
  );
}
