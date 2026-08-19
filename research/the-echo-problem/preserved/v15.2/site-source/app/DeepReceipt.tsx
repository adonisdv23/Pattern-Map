/* eslint-disable jsx-a11y/no-noninteractive-tabindex -- the labelled table overflow region is intentionally keyboard-focusable on narrow screens. */
const observationIds = ["O01", "O02", "O03", "O04", "O05", "O06", "O07", "O08", "O09"];

export default function DeepReceipt() {
  return (
    <section className="section deep-receipt-section" id="deep-receipt" aria-labelledby="deep-receipt-title" tabIndex={-1}>
      <div className="section-marker"><span>01</span><small>Detailed receipt</small></div>
      <div className="section-body">
        <p className="status-pill">Fictional illustration · no live data · no result</p>
        <p className="kicker">The technical record behind 09 / 01 / 00 / HOLD</p>
        <h2 id="deep-receipt-title">Preserve the observations; expose the relation rule.</h2>
        <p className="lead">The first reading route uses four values. This optional record shows the identities, typed relations, contrast roots, permission, and human next step that make those values inspectable.</p>

        <section className="route-receipt" aria-labelledby="deep-receipt-card-title">
          <header className="route-receipt-header">
            <p className="kicker">Receipt ORIGIN-EX-01 · version 0.3</p>
            <h3 id="deep-receipt-card-title">Nine report observations follow one known shared path.</h3>
            <p>A supplied illustration records relationships and a human next step. It does not discover the real web, establish truth, or decide automatically.</p>
            <p className="route-receipt-meta">Fictional bundle · sandbox decision · not a live system</p>
          </header>

          <dl className="route-receipt-frame">
            <div><dt>Decision in view</dt><dd>Whether a sandbox pilot of a data-migration tool is warranted</dd></div>
            <div><dt>Permission and budget</dt><dd>Sandbox only · ninety minutes · no production data</dd></div>
            <div><dt>Claim under review</dt><dd>“The tool is broadly validated.”</dd></div>
            <div><dt>Human next step</dt><dd><strong>HOLD · VERIFY ANOTHER ORIGIN RELATION</strong></dd></div>
          </dl>

          <section className="route-receipt-count" aria-labelledby="deep-receipt-count-title">
            <h4 id="deep-receipt-count-title">Count snapshot</h4>
            <dl>
              <div><dt>Report observations</dt><dd>09</dd></div>
              <div><dt>Known shared paths</dt><dd>01</dd></div>
              <div><dt>Counted support paths</dt><dd>00</dd></div>
              <div><dt>Contrast roots</dt><dd>02 <small>support unassessed</small></dd></div>
            </dl>
            <p className="route-receipt-unknown"><strong>UNRESOLVED stays unresolved.</strong> Do not move an unknown relation into either the shared-path or separate-root total.</p>
          </section>

          <section className="route-receipt-ledger" aria-labelledby="deep-receipt-ledger-title">
            <h4 id="deep-receipt-ledger-title">Observation ledger · nine unordered records</h4>
            <p>These rows preserve nine observations. Their order is not a workflow, ranking, or confidence scale.</p>
            <p className="route-receipt-mobile-summary">O01–O09 · Origin A · SHARED PATH / DPND · zero support paths counted for the broad claim</p>
            <div className="route-receipt-table-scroll" role="region" aria-labelledby="deep-receipt-ledger-title" aria-describedby="deep-receipt-scroll-note" tabIndex={0}>
              <p id="deep-receipt-scroll-note" className="scroll-hint">On narrow screens, scroll this data table horizontally; the page itself does not scroll sideways.</p>
              <table>
                <caption>Typed relation ledger for the nine illustrative observations</caption>
                <thead><tr><th scope="col">Record</th><th scope="col">Kind</th><th scope="col">Plain relation</th><th scope="col">Technical code</th><th scope="col">Counting treatment</th></tr></thead>
                <tbody>
                  {observationIds.map((record) => (
                    <tr key={record}>
                      <th scope="row">{record}</th>
                      <td>Report observation</td>
                      <td>Shared path to Origin A</td>
                      <td><strong>DPND</strong></td>
                      <td>Preserve; do not count as separately rooted support.</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>

          <div className="route-receipt-lower">
            <section aria-labelledby="deep-receipt-key-title">
              <h4 id="deep-receipt-key-title">Plain state first; technical code second</h4>
              <dl className="route-receipt-key">
                <div><dt>Shared path · DPND</dt><dd>Traceable to an existing artifact. Preserve the observation; do not count a new root.</dd></div>
                <div><dt>Separate only in this test · INDP</dt><dd>A separate root stipulated by the illustration—not discovered independence.</dd></div>
                <div><dt>Unresolved · UNKN</dt><dd>The relation is not established. Preserve it; do not guess either way.</dd></div>
              </dl>
            </section>
            <section aria-labelledby="deep-receipt-contrast-title">
              <h4 id="deep-receipt-contrast-title">Separate roots shown for contrast</h4>
              <ul><li><strong>B1</strong> · separate only in this illustration</li><li><strong>C1</strong> · separate only in this illustration</li></ul>
              <p>Claim support is not assessed. B1 and C1 are not counted as support for the claim in this packet.</p>
            </section>
          </div>

          <section className="route-receipt-disposition" aria-labelledby="deep-receipt-decision-title">
            <p className="card-label">Recorded human next step</p>
            <h4 id="deep-receipt-decision-title">HOLD · VERIFY ANOTHER ORIGIN RELATION</h4>
            <p>Inspect the announcement, then look for one separately authored benchmark and document its relation before changing the claim state.</p>
            <p>No automatic admission, rejection, or truth verdict. A reviewer may correct the relation; the original fictional observations remain preserved.</p>
          </section>

          <p className="route-receipt-footer">Illustrative only · not a reported dataset · not an audit of where real sources came from · not a live system · not a model result. The labels describe a supplied teaching record.</p>
        </section>
      </div>
    </section>
  );
}
