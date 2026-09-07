type MicroVisualProps = {
  variant: "origin-count" | "trace-hold" | "conditions";
};

export default function MicroVisual({ variant }: MicroVisualProps) {
  if (variant === "origin-count") {
    return (
      <figure className="microvisual microvisual-origin" aria-labelledby="origin-count-caption">
        <div className="origin-observations" aria-label="Nine report observations">
          {Array.from({ length: 9 }, (_, index) => (
            <span key={index}>O{String(index + 1).padStart(2, "0")}</span>
          ))}
        </div>
        <div className="origin-trace" aria-hidden="true">
          <i /><i /><i /><i /><i /><i /><i /><i /><i />
        </div>
        <div className="origin-node">
          <small>Known shared path</small>
          <strong>Origin A</strong>
          <span>one launch announcement</span>
        </div>
        <dl className="origin-counts">
          <div><dt>observations</dt><dd>09</dd></div>
          <div><dt>known shared paths</dt><dd>01</dd></div>
          <div><dt>counted support paths</dt><dd>00</dd></div>
          <div><dt>human next step</dt><dd>HOLD</dd></div>
        </dl>
        <figcaption id="origin-count-caption">
          <strong>Nine observations remain visible; repetition does not create eight new roots.</strong>
          <span>One path is known. Zero paths support the broad claim yet. That is a hold, not a rejection or a truth verdict.</span>
        </figcaption>
      </figure>
    );
  }

  if (variant === "trace-hold") {
    return (
      <figure className="microvisual microvisual-decision" aria-labelledby="trace-hold-caption">
        <ol>
          <li><small>Trace</small><strong>Origin A → O01–O09</strong><span>shared path</span></li>
          <li><small>Claim state</small><strong>INSUFFICIENT</strong><span>unresolved is not independent</span></li>
          <li><small>Human next step</small><strong>HOLD · VERIFY</strong><span>recorded action, not external truth</span></li>
        </ol>
        <figcaption id="trace-hold-caption">
          <strong>Trace, support, and action remain different judgments.</strong>
          <span>A lineage record does not prove the claim, and a hold does not reject it.</span>
        </figcaption>
      </figure>
    );
  }

  return (
    <figure className="microvisual microvisual-conditions" aria-labelledby="conditions-caption">
      <ol>
        <li><small>Ordinary version · F0</small><strong>Evidence</strong><span>no counting rule or supplied relation note</span></li>
        <li><small>Rule-only version · F1</small><strong>Same evidence + rule</strong><span>repeated paths should not count as separate support</span></li>
        <li><small>Added-cue version · F2</small><strong>Same evidence + same rule + supplied note</strong><span>shared / separate-in-this-test / unresolved</span></li>
      </ol>
      <figcaption id="conditions-caption">
        <strong>One planned difference is isolated between F1 and F2.</strong>
        <span>No winner, effect, or model result exists. The relation note is supplied by the fictional benchmark.</span>
      </figcaption>
    </figure>
  );
}
