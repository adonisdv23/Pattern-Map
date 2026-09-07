/* eslint-disable @next/next/no-img-element, @next/next/no-html-link-for-pages, jsx-a11y/no-noninteractive-tabindex -- v15.2 uses audited local rasters, route-stable plain anchors, and labelled keyboard-focusable overflow regions. */
import ReadingNav from "./ReadingNav";
import CollapseControl from "./CollapseControl";
import DeepReceipt from "./DeepReceipt";
import Term from "./Term";
import MicroVisual from "./MicroVisual";
import { componentMaturity, families, glossary, researchPaths, sources, technicalGlossary } from "./content";

const counterarguments = [
  ["Old work, new label", "The mechanisms reviewed here already have mature precedents. The plausible contribution is a boundary-preserving synthesis and an evaluation agenda—not a new mechanism family."],
  ["A new gatekeeper", "Any selection policy can reinforce institutional bias or erase peripheral evidence. Exclusions, unknowns, reasons, appeal, and source diversity must stay inspectable."],
  ["Rigor theater", "Detailed provenance can trace a false claim perfectly. Lineage never upgrades correctness, support, or permission by itself."],
  ["More cost than value", "The architecture may be too slow and cognitively heavy. It must beat strong simple baselines under matched time, tokens, retrieval, and review effort."],
  ["Decorative human review", "A person placed after an opaque route may only rubber-stamp it. Review must expose the evidence path and permit a consequential correction."],
  ["Learning the wrong lesson", "Outcome feedback can encode preference, contaminated proxies, or hindsight. Updates need a predefined outcome, attribution limits, versioning, and approval."],
];

const limitations = [
  ["No empirical evaluation.", "This project reports no experiment, participant study, field outcome, or comparative performance result."],
  ["No broad mechanism novelty.", "The components have extensive prior art. The residual contribution is a boundary-preserving synthesis and one narrow supplied-cue hypothesis."],
  ["No proven minimum.", "Eleven components are an analytical decomposition, not evidence that every task needs eleven implemented modules."],
  ["No validated constructs.", "Reviewers may not reliably distinguish authority, support, origin relation, relevance, attention, enrichment value, action priority, and disposition."],
  ["No provenance discovery.", "The proposed study supplies benchmark relations; it does not infer a real source path."],
  ["No real-world independence.", "INDP means separate origin only as stipulated in the synthetic benchmark graph."],
  ["Open-world evidence remains hard.", "Sources change, origins are obscured, important evidence is inaccessible, and support can remain contested."],
  ["Costs and utilities are uncertain.", "A clean stopping rule can still stop before rare decisive evidence or encode the wrong consequence model."],
  ["Human control is not guaranteed.", "Interfaces and organizational incentives can turn review into ceremony."],
  ["Memory can amplify error.", "Retention, retrieval, and summarization can preserve stale, biased, or manipulated content."],
  ["Surface leakage is not cleared.", "The small local smoke corpus is trivially separable; a blocked classifier and semantic audit remain stop gates."],
  ["Transfer is unresolved.", "Public syndication resources do not supply the required claim/origin ground truth, and rights gates remain."],
  ["The name may fail.", "Discrimination layer may remain ambiguous or harmful despite an explicit technical definition."],
  ["The historical HTML is still pending.", "The original v13 diagram is now preserved and its supplied hash is verified; the expected standalone HTML remains unavailable and unverified."],
  ["Product cases are illustrative.", "Alpha Solver and Signal Foundry are related cases, not independent validation."],
  ["No publication or owner approval.", "This is a local review draft."],
];

export type PageMode = "explore" | "lab" | "sources";

export function PatternRecognitionPage({ mode }: { mode: PageMode }) {
  const isExplore = mode === "explore";
  const isLab = mode === "lab";
  const isSources = mode === "sources";

  return (
    <main id="main-content">
      <a className="skip-link" href={isExplore ? "#deep-receipt" : isLab ? "#lab" : "#sources"}>
        {isExplore ? "Skip to the detailed receipt" : isLab ? "Skip to the research question" : "Skip to the sources"}
      </a>

      <aside className="rail" aria-label="Reading paths and status">
        <a className="wordmark" href="/" aria-label="Pattern Recognition, return to start">
          <span>Pattern<br />Recognition</span><small>v15.2</small>
        </a>
        <ReadingNav initialActive={isExplore ? "deep-receipt" : isLab ? "lab" : "sources"} />
        <p className="rail-status"><span aria-hidden="true" /> Local owner review</p>
      </aside>

      <div className="page-shell">
        <header className="subpage-masthead" id="start">
          <p className="eyebrow">Pattern Recognition · v15.2 · local owner review</p>
          <h1>{isExplore ? "Explore the framework" : isLab ? "The research track" : "Sources and plain-language glossary"}</h1>
          <p className="subpage-dek">{isExplore ? "Inspect the six families, eleven responsibilities, loops, cases, and objections behind the five-minute argument." : isLab ? "A research protocol can be visible before a result exists. This page reports the question, the safeguards, and the open gates—not findings." : "Read the precedents, status boundaries, and explanations behind the framework without needing a technical vocabulary."}</p>
          <p className="subpage-status">No model selected · no study run · no empirical results · not published</p>
        </header>


        {isExplore && <>
        <DeepReceipt />
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
                          <span className="component-summary">
                            <strong>{component.name}</strong>
                            <small>{component.summary}</small>
                            <span className={`component-summary-status status-${componentMaturity[component.id].kind}`}>
                              Evidence status · {componentMaturity[component.id].label}
                            </span>
                          </span>
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
            <h2 id="example-title">What changes after the receipt?</h2>
            <p className="lead">Treat the corrected accounting record as an input to a decision, not as a verdict. The question is now which bounded action the record permits—and what must remain unresolved.</p>
            <figure className="example-visual">
              <img
                src="/images/nine-mentions-one-origin.jpg"
                width="1536"
                height="1024"
                decoding="async"
                alt="Illustrative—not factual—scene of one coral source artifact branching into nine differently styled report fragments, beside two separately rooted evidence fragments. The common origin does not mean the reports are false."
              />
              <figcaption><strong>Many mentions can preserve one origin.</strong><span>The visual recalls the receipt; the application below begins after its relation correction.</span><small>Illustration only · colors encode no status · not a reported dataset, real-source audit, or result</small></figcaption>
            </figure>
            <div className="example-contrast" aria-label="Decision route before and after the accounting correction">
              <article><p className="card-label">Before the receipt</p><p>Popularity prematurely ends the search and broadens the claim.</p></article>
              <article><p className="card-label">After the correction</p><p>The broad claim stays on hold while one narrow sandbox question becomes actionable.</p></article>
            </div>
            <ol className="example-grid">
              <li><span>Action 1</span><strong>Narrow the permission</strong><p>Sandbox only. No production data. Ninety minutes of research.</p></li>
              <li><span>Action 2</span><strong>Test the decision-relevant claim</strong><p>Verify a separately authored benchmark, then reproduce one rollback path locally.</p></li>
              <li><span>Action 3</span><strong>Preserve what follows</strong><p>A sandbox outcome can change the pilot rule, not validate the broad claim.</p></li>
            </ol>
            <div className="example-result">
              <p className="card-label">Decision implication</p>
              <p>Receipt <code>ORIGIN-EX-01</code> changes the illustrative route: hold the broad validation claim, verify a separately authored benchmark, and propose one bounded synthetic-data rollback check. Any real check still requires separate owner authorization; this example authorizes nothing. Preserve either outcome.</p>
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
                <li>Reviewers cannot reliably distinguish authority, support, origin relation, relevance, and action priority.</li>
                <li>Origin-aware grouping hides legitimate convergence as often as it prevents false corroboration.</li>
                <li>The interface increases overload, review time, or overreliance enough to erase any benefit.</li>
                <li>Outcome updates encode local preference or contaminated proxies rather than better policy.</li>
              </ul>
            </div>
            <div className="limitations-block" aria-labelledby="limitations-title">
              <p className="kicker">Current limitations</p>
              <h3 id="limitations-title">Sixteen boundaries the presentation cannot smooth away.</h3>
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
                <h3>One synthetic receipt changes one route.</h3>
                <p className="case-boundary"><strong>Boundary:</strong> this is an offline contract fixture, not production data, operator validation, or empirical support for eleven general responsibilities.</p>
                <p>Two exact matching source claims share one supplied <code>SYNDICATED_FROM</code> path. A third claim contradicts them, and the inspected transcript boundary lacks an expected setup artifact.</p>
                <p className="case-status"><strong>RELATED · 2 observations / 1 known supporting-origin path · HOLD / DEFER</strong></p>
                <details className="case-receipt">
                  <summary>Inspect the five-field Signal Foundry case</summary>
                  <dl>
                    <div><dt>Claim</dt><dd>Did the bounded walkthrough show the setup procedure?</dd></div>
                    <div><dt>Observations</dt><dd>Two matching source claims; one open contradiction; one bounded expected-but-missing gap.</dd></div>
                    <div><dt>Relation</dt><dd>Two observations, one known supporting-origin path. Relatedness does not settle support or truth.</dd></div>
                    <div><dt>Permission</dt><dd>Inspect the synthetic packet only. No provider retrieval, external upload, production use, transcript Apply, or new durable write is authorized.</dd></div>
                    <div><dt>Human next step</dt><dd><strong>HOLD / DEFER</strong> pending one independently observed primary artifact.</dd></div>
                  </dl>
                  <p><strong>Operational invariants:</strong> staged transcript material is not canonical until its separate Apply transition; screenshots, frames, and OCR remain Visual Evidence rather than transcript evidence.</p>
                  <p>A possible pointer-only <code>CONTEXT_DISPOSITION</code> event is a design proposal—not an implemented capability or production fact.</p>
                </details>
              </article>
            </div>
            <div className="enterprise-translation">
              <div><p className="card-label">Enterprise translation</p><h3>Identity, policy, receipts, review, versioning.</h3></div>
              <p>The framework can map to role-based authorization, lineage systems, policy engines, approval queues, evaluation records, and risk-management controls. That mapping does not establish compliance, safety, or return on investment in any deployment.</p>
            </div>
          </div>
        </section>
        </>}

        {isLab && <section className="section lab-section" id="lab" aria-labelledby="lab-title" tabIndex={-1}>
          <div className="section-marker"><span>08</span><small>Lab · no results</small></div>
          <div className="section-body">
            <div className="lab-threshold" role="note" aria-label="Research status">
              <span>Planned test, separate from this essay</span>
              <strong>Written plan + local test code</strong>
              <span>No AI model chosen · test not run · no result</span>
            </div>
            <p className="kicker">One bounded question</p>
            <h2 id="lab-title">Can a supplied origin cue change counting beyond an explicit rule?</h2>
            <p className="lead">The conceptual reader can be complete before an experiment. This page describes a planned test and its safeguards—not a finding. No model has been selected, and no study has been run.</p>

            <div className="lab-question">
              <p className="card-label">Proposed study title · model not yet selected</p>
              <h3>Supplied Origin-Relation Cues in One Model to Be Selected</h3>
              <p>On fictional evidence bundles with supplied relationships, compare the same model and evidence under <strong>three versions of the same task</strong>. The only primary comparison is whether the version with the supplied origin clue beats the version with the explicit rule alone.</p>
            </div>

            <MicroVisual variant="conditions" />

            <div className="condition-table-wrap" role="region" aria-labelledby="condition-table-title" aria-describedby="condition-table-scroll-note" tabIndex={0}>
              <h3 id="condition-table-title">Three versions of the same task <Term id="lab-conditions" label="F0 / F1 / F2" definition="Three versions of the same planned test: an ordinary baseline, an explicit counting rule, and that rule plus supplied origin clues." example="If F2 does better than F1, the difference is evidence about the supplied clue—not proof that the whole framework improves decisions." boundary="They are experimental conditions, not product versions, performance grades, or three different AI systems.">F0 / F1 / F2</Term></h3>
              <p id="condition-table-scroll-note" className="scroll-hint">On narrow screens, scroll this comparison horizontally; the page itself does not scroll sideways.</p>
              <table>
                <thead><tr><th scope="col">Condition</th><th scope="col">Prompt-visible difference</th><th scope="col">Status</th></tr></thead>
                <tbody>
                  <tr><th scope="row">F0</th><td>Ordinary bounded evidence assessment; no origin clue is shown.</td><td>Secondary baseline</td></tr>
                  <tr><th scope="row">F1</th><td>Same evidence plus an explicit rule for counting origins; no origin clue is shown.</td><td>Primary comparator</td></tr>
                  <tr><th scope="row">F2</th><td>Same rule and evidence plus the benchmark’s supplied relationship labels.</td><td>Primary intervention</td></tr>
                </tbody>
              </table>
              <p className="condition-code-note"><strong>What the supplied labels mean:</strong> <code>DPND</code> means a shared or dependent path; <code>INDP</code> means a separate origin only as stipulated by this fictional test; <code>UNKN</code> means unresolved. <code>UNKN</code> is never silently counted as independent.</p>
            </div>

            <p className="plain-method-note">The current planning draft proposes <Term id="lab-sample-size-note" label="N=300" definition="A plan to assign 300 fictional evidence bundles to the primary comparison. N is simply the number of bundles; it is not a score, a confidence level, or a result." example="The final number may change after the operating-characteristic and safety checks. No study has been run with these 300 bundles." boundary="It is not the number of people, reports, model calls, favorable outcomes, or proof that the plan is adequate.">300 planned fictional cases</Term>. That number is provisional until the paired design and safety checks are complete.</p>

            <div className="lab-metrics" aria-label="Planned corpus and analysis boundaries">
              <div><strong>80</strong><span>development bundles</span></div>
              <div><strong>40</strong><span>feasibility-only pilot</span></div>
              <div><strong>300</strong><span>provisional fictional cases</span></div>
              <div><strong>60</strong><span>descriptive stress bundles</span></div>
            </div>

            <div className="lab-columns">
              <article>
                <p className="card-label">Primary + safety</p>
                <h3>Two measures, two limited claims.</h3>
                <p><Term id="lab-fc-cons" label="FC_cons" definition="The conservative primary risk event across all 300 assigned bundles. A response is risky if it is invalid, or if a valid response asserts two or more supporting origins when the fictional benchmark says support certainty is none, single, or unresolved." example="A malformed response and a valid response that overcounts one shared path both remain in the main denominator, though their components are reported separately." boundary="A lower composite does not by itself prove semantic understanding; it can be driven by invalid-answer differences or threshold behavior.">FC_cons</Term> keeps all <strong>A=300</strong> assigned bundles in the denominator. Invalid outputs count as risk, as do valid counts of two or more on <em>none</em>, <em>single</em>, or <em>unresolved</em> support-certainty rows. Invalidity and valid-answer counting must also be reported separately before anyone calls a difference cue value.</p>
                <p><Term id="lab-vor" label="VOR" definition="A fixed safety guardrail on 75 fictional cases where at least two supporting origins are stipulated. It requires a valid answer, a count of at least two, and selected support from at least two supplied origins." example="The guardrail catches a system that reduces false corroboration by simply saying one origin for everything. The planned F2-minus-F1 one-sided lower bound must be greater than -0.05." boundary="It is a threshold check, not proof of exact counting, correct origin assignment, or real-world independence. The 75-case membership is frozen before a run and may never be filtered after seeing validity or outputs.">VOR</Term> uses a fixed <strong>M=75</strong> multiple-certainty safety subset. Its ordered membership and hash come from the restricted pre-run manifest, are frozen before execution, and are never filtered by validity or post-run output. The planned F2-minus-F1 guardrail passes only if its one-sided 95% lower bound is greater than <strong>-0.05</strong>. The interval method, coverage simulation, and paired-invalid operating-characteristic receipt all remain open. This is a threshold guardrail against blanket suppression—not exact counting or assignment.</p>
              </article>
              <article>
                <p className="card-label">Exact parity</p>
                <h3>Same task. One intentional difference.</h3>
                <p>F1 and F2 must contain byte-identical report text, report order, metadata shape, rule instruction, output cap, retrieval/tool budget, and matched resource receipts. The relation-field values are the intentional visible input difference. Final prompt bytes and hashes may differ; input byte lengths and selected-tokenizer input counts must match exactly. The current tokenizer is only a development stand-in.</p>
              </article>
              <article>
                <p className="card-label">Shortcut burden</p>
                <h3>A code-counting win is not the claim.</h3>
                <p>Neutral labels, order/style/surface controls, metadata-only and field-only diagnostics, relation-noise stress, split blocking, and a human semantic audit must pass. The small local surface smoke is trivially separable, so the full leakage gate remains open.</p>
              </article>
            </div>

            <section className="open-gates" aria-labelledby="open-gates-title">
              <p className="card-label">COHERENT_PROTOCOL_NOT_EXECUTION_READY · all material gates open</p>
              <h3 id="open-gates-title">A listed safeguard is not a passed safeguard.</h3>
              <p>The written plan and local fixture code do not authorize a pilot, a model call, or a study. Every row below remains open until a dated, reviewable receipt exists—and a separate owner decision is still required afterward.</p>
              <ul>
                <li><strong>FC_cons decomposition:</strong> separate invalid-output effects from valid asserted-count behavior.</li>
                <li><strong>Operating characteristics:</strong> freeze the safety-interval method, verify coverage for fixed M=75 and the locked -0.05 margin, and test paired invalid-output dependence.</li>
                <li><strong>Actual model parity:</strong> select the model, tokenizer, and chat template; prove byte-length, token-count, and resource matching.</li>
                <li><strong>Leakage and meaning:</strong> pass surface, field-only, metadata-only, split-blocking, and human semantic checks.</li>
                <li><strong>Claim/status lint:</strong> prevent planned controls or local fixtures from being described as passed, run, or effective.</li>
                <li><strong>Count/stance/evidence coherence:</strong> reject outputs whose count, claim state, and selected evidence disagree.</li>
                <li><strong>Owner phase authorization:</strong> even complete gate receipts authorize nothing by themselves.</li>
              </ul>
            </section>

            <aside className="t1-panel" aria-labelledby="t1-title">
              <p className="card-label"><Term id="lab-transfer" label="T1" definition="A separate, descriptive transfer check using real repetition patterns. It is not part of the main experiment because those datasets do not provide all the ground truth the main question needs." example="A duplicate-news dataset can show repetition without proving a claim or real-world independence." boundary="It cannot validate the main experiment or certify that real-world sources are independent.">T1</Term> · descriptive transfer only</p>
              <h3 id="t1-title">Real recurrence is useful—and insufficient.</h3>
              <p>NEWS-COPY may support bounded “same original” examples. Newswire may preserve aggregate recurrence context. Neither supplies the full ground truth needed to say which claims are supported or which sources are truly separate.</p>
              <p><strong>No third main condition exists.</strong> T1 stays outside the main test and its safety check; it does not contribute to uncertainty ranges, paired comparisons, or claimed effects. Rights and annotation gates must pass before any data use.</p>
            </aside>

            <section className="result-commitment" aria-labelledby="result-commitment-title">
              <p className="card-label"><Term id="lab-negative-result" label="Locked negative-result commitment" definition="An agreement made before a test that an unhelpful, harmful, null, or shortcut-driven result will still be reported instead of hidden or spun as success." example="If the origin clue makes the model worse, the correct conclusion is to reject the clue in this setting." boundary="It does not predict failure or authorize the study; it prevents selective interpretation after results are known.">Locked before any run</Term></p>
              <h3 id="result-commitment-title">The program keeps an unfavorable result.</h3>
              <p className="result-commitment-intro">In plain English: we decide in advance to report what actually happens, even if the answer is “no benefit,” “made things worse,” or “the model found a shortcut.”</p>
              <ul>
                <li><strong>Null:</strong> no evidence that the typed cue adds value beyond the rule in this setting.</li>
                <li><strong>Rule-only:</strong> if F1 and F2 beat F0 but tie, credit the explicit rule.</li>
                <li><strong>Invalidity-driven or threshold-only:</strong> if the composite moves only because invalid answers change, or VOR merely clears its threshold, report that limited explanation—not semantic cue value.</li>
                <li><strong>Harmful:</strong> if F2 suppresses valid stipulated convergence or performs worse, reject the cue.</li>
                <li><strong>Direct-code or field-only shortcut:</strong> if codes, field position, or another superficial cue explains the result, narrow or reject the mechanism claim.</li>
                <li><strong>Surface or semantic-audit failure:</strong> if the surface, stance, transformation, split-leakage, or count/claim/evidence-coherence audit fails, quarantine the affected run and make no mechanism claim from it.</li>
                <li><strong>Unstable:</strong> if the result changes materially across the preregistered seeds or configurations, report it as unstable and make no general mechanism claim.</li>
                <li><strong>Noise-fragile or non-transferable:</strong> if the effect breaks under relation noise or does not carry to a separately approved descriptive transfer set, say so and narrow the boundary.</li>
                <li><strong>Stopped or quarantined:</strong> preserve any aborted or contaminated run and make no effect claim from it.</li>
              </ul>
            </section>

            <details className="lab-program">
              <summary>View the wider research program—kept outside this study</summary>
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
            </details>
            <p className="document-link">Canonical candidate: <code>source/THOUGHT_PIECE_V15_2.md</code> · Canonical protocol: <code>research/ORIGIN_ACCOUNTING_STUDY_PROTOCOL_V1.md</code> · Non-authorizing amendment draft: <code>research/overnight/v15_2/ORIGIN_ACCOUNTING_PROTOCOL_V1_1_AMENDMENT_DRAFT.md</code></p>
          </div>
        </section>}
        {isSources && <section className="section source-section" id="sources" aria-labelledby="sources-title" tabIndex={-1}>
          <div className="section-marker"><span>09</span><small>Sources</small></div>
          <div className="section-body">
            <p className="kicker">Selected precedents and status notes</p>
            <h2 id="sources-title">Prior art narrows the claim.</h2>
            <p className="lead">Copying, double counting, citation amplification, duplicate detection, retrieval diversity, conflict, and source dependence all have direct precedents. The residual contribution is a synthesis and one narrow supplied-cue test—not a new generic mechanism.</p>
            <ol className="source-list">
              {sources.map((source) => (
                <li key={source.url}><a href={source.url}>{source.label}</a><p>{source.use}</p></li>
              ))}
            </ol>
            <p className="document-link" id="prior-art-delta-route">Full source/status ledger: <code>research/PRIOR_ART_DELTA_V1.md</code> · entries S1–S19 · supplied benchmark relations remain distinct from inferred provenance.</p>

            <div className="glossary" id="glossary" aria-labelledby="glossary-title">
              <div className="heading-row compact-heading"><div><p className="kicker">Interpretation guardrail</p><h3 id="glossary-title">Compact glossary</h3></div><a className="text-link" href="#start">Back to start ↑</a></div>
              <dl>
                {glossary.map(([term, definition]) => <div key={term}><dt>{term}</dt><dd>{definition}</dd></div>)}
              </dl>
              <section className="technical-glossary" aria-labelledby="technical-glossary-title">
                <p className="kicker">Expanded plain-language guide</p>
                <h3 id="technical-glossary-title">Technical terms, without the gatekeeping.</h3>
                <p>Every explanation below uses ordinary language first. Select a highlighted term for a concise definition, a concrete example, and a boundary. The essay and Lab pair a few harder relationships with dedicated microvisuals.</p>
                <div className="technical-glossary-grid">
                  {technicalGlossary.map((entry) => (
                    <article key={entry.term}>
                      <h4><Term id={`glossary-${entry.id}`} label={entry.term} definition={entry.definition} example={entry.example} boundary={entry.boundary}>{entry.term}</Term></h4>
                      <p>{entry.definition}</p>
                      <p className="technical-glossary-example"><strong>Example:</strong> {entry.example}</p>
                    </article>
                  ))}
                </div>
              </section>
            </div>
          </div>
        </section>}

        {isSources && <section className="closing" aria-labelledby="closing-title">
          <p className="kicker">The correction test</p>
          <h2 id="closing-title">Can the judgment be seen early enough to contest?</h2>
          <p>The aim is not to count less. It is to count the declared unit, keep unknowns unknown, and preserve why a report, claim, permission, or action entered the packet. Whether that visibility improves outcomes enough to justify its cost remains an empirical question—and the program keeps a negative answer.</p>
          <div className="closing-links"><a href="/">Revisit the receipt ↑</a><a href="/lab">Review the no-results lab ↑</a></div>
        </section>}

        <footer>
          <p>Local owner review · not published · no empirical results</p>
          <p>Pattern Recognition · The Discrimination Layer · v15.2</p>
        </footer>
      </div>
    </main>
  );
}
