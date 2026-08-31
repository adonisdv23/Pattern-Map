import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, "../..");
const read = (relative) => fs.readFileSync(path.join(root, relative), "utf8");

await import("../../site/src/recommendation.js");
const api = globalThis.PatternMapRecommendation;

const ordinaryTemplate = read("framework/templates/ORDINARY_RECORD.md");
const quickstart = read("framework/agent-playbook/QUICKSTART.md");
const implementationChoices = read("framework/IMPLEMENTATION_CHOICES.md");
const applyHtml = read("site/public-dist/apply/index.html");
const guidedHtml = read("site/public-dist/guided/index.html");
const siteScript = read("site/src/site.js");
const pdfSource = read("site/scripts/generate_review_pdf.py");
const manuscript = read("manuscript/PATTERN_RECOGNITION_V16.md");

for (const phrase of ["Supplied scope", "Material assumptions", "Unchecked boundaries", "Output"]) {
  assert.match(ordinaryTemplate, new RegExp(`- ${phrase}:`));
  assert.match(applyHtml, new RegExp(phrase, "i"), `public Apply lost ordinary field ${phrase}`);
}
assert.match(ordinaryTemplate, /terminal; it is not an ANSWER, route, stop,\s*learning, or influence receipt/);
assert.match(ordinaryTemplate, /Do not add layered evidence, outcome, or\s*six-family fields/);
assert.match(quickstart, /use the ordinary path[\s\S]*supplied scope[\s\S]*material assumptions[\s\S]*unchecked boundaries[\s\S]*output[\s\S]*stop/i);
for (const [label, artifact] of [["Apply", applyHtml], ["Guided", guidedHtml], ["PDF source", pdfSource]]) {
  assert.match(artifact, /material claim judgment[\s\S]*comparison[\s\S]*selection or withholding[\s\S]*permission resolution[\s\S]*memory reuse[\s\S]*acquisition[\s\S]*human action gate[\s\S]*consequential external influence/i, `${label} lost the complete Stage 0 disqualifier`);
}
const staticGuide = applyHtml.match(/<details class="static-route-equivalent"[\s\S]*?<\/details>/)?.[0] ?? "";
assert.match(staticGuide, /material claim judgment[\s\S]*comparison[\s\S]*selection or withholding[\s\S]*permission resolution[\s\S]*memory reuse[\s\S]*acquisition[\s\S]*human action gate[\s\S]*consequential external influence/i, "Apply static guide lost the exact Stage 0 predicate");
assert.match(staticGuide.match(/<tr><th scope="row">ordinary<\/th>[\s\S]*?<\/tr>/)?.[0] ?? "", /permission resolution[\s\S]*consequential external influence/i, "Apply static ordinary row drifted from the exact Stage 0 predicate");
assert.doesNotMatch(guidedHtml, /If the work only formats, translates, rewrites, summarizes, or transforms supplied material, use the ordinary path/);
assert.doesNotMatch(pdfSource, /weighing information beyond supplied material/);
assert.match(guidedHtml, /Ordinary remains available only when every Stage 0 condition immediately above holds/);
assert.match(guidedHtml, /Reformat supplied prose exactly[\s\S]*reversible format without changing, selecting, or omitting its content/);
assert.doesNotMatch(guidedHtml, /<h3>Rewrite supplied prose\.<\/h3>/);
assert.match(applyHtml, /Test the exact Stage 0 choice below; if any disqualifier is present/);
assert.match(manuscript, /For consequential, contested, or repeated work, software might help track/);
assert.doesNotMatch(manuscript, /For consequential, contested, or repeated work, an advanced implementation/);

const ordinary = api.recommend({ evidenceSelection: "none" });
assert.equal(ordinary.recommendedAction, "ORDINARY_RECORD");
assert.match(ordinary.learningOption, /LEARNING_NOT_APPLICABLE/);
assert.match(applyHtml, /data-recommendation-action>ORDINARY_RECORD</);
assert.match(applyHtml, /four-field ordinary record/i);
assert.doesNotMatch(applyHtml.match(/<tr><th scope="row">ordinary<\/th>[\s\S]*?<\/tr>/)?.[0] ?? "", /<code>ANSWER<\/code>/);
for (const field of ["route", "stop_status", "learning_status", "evidence_records", "outcome", "humanDisposition"]) {
  assert.throws(
    () => api.recommend({ evidenceSelection: "none", [field]: "fabricated-value" }),
    /exact declared fields/,
    `ordinary API accepted undeclared ${field}`,
  );
}
const hiddenExtra = { evidenceSelection: "none" };
Object.defineProperty(hiddenExtra, "route", { value: "ANSWER", enumerable: false });
assert.throws(() => api.recommend(hiddenExtra), /exact declared fields/, "ordinary API accepted a non-enumerable extra field");
const symbolExtra = { evidenceSelection: "none", [Symbol("route")]: "ANSWER" };
assert.throws(() => api.recommend(symbolExtra), /exact declared fields/, "ordinary API accepted a symbol extra field");
const inheritedExtra = Object.assign(Object.create({ route: "ANSWER" }), { evidenceSelection: "none" });
assert.throws(() => api.recommend(inheritedExtra), /exact declared fields/, "ordinary API accepted inherited fields");
const accessorInput = {};
Object.defineProperty(accessorInput, "evidenceSelection", { enumerable: true, get: () => "none" });
assert.throws(() => api.recommend(accessorInput), /Invalid evidenceSelection/, "ordinary API accepted an accessor-shaped declared field");

for (const state of ["AUTHORIZED", "UNKNOWN", "NOT_AUTHORIZED", "REVOKED"]) {
  assert.match(quickstart, new RegExp(`\\b${state}\\b`));
  assert.match(applyHtml, new RegExp(`name="permission" value="${state}"`));
}
for (const stale of ['value="supplied"', 'value="restricted"', 'value="human-gate"']) {
  assert.equal(applyHtml.includes(stale), false, `public Apply retained stale permission value ${stale}`);
}
assert.match(applyHtml, /name="humanActionGate" value="NOT_REQUIRED"/);
assert.match(applyHtml, /name="humanActionGate" value="REQUIRED"/);
assert.match(applyHtml, /Permission state[\s\S]*Separate human action gate/);
assert.match(applyHtml, /data-recommendation-permission>NOT_APPLICABLE/);
assert.match(applyHtml, /data-recommendation-human-gate>NOT_APPLICABLE/);
assert.match(applyHtml, /data-recommendation-capacity>NOT_APPLICABLE/);

for (const dependent of ["consequence", "uncertainty", "budget", "permission", "humanActionGate"]) {
  assert.match(applyHtml, new RegExp(`data-stage0-dependent="${dependent}"[^>]*disabled`));
}
assert.match(siteScript, /evidenceSelection === "none"[\s\S]*?\? \{ evidenceSelection \}/);
assert.match(siteScript, /humanActionGate: fieldValue\("humanActionGate"\)/);

const substantialCapacityOnly = api.recommend({
  evidenceSelection: "needed",
  consequence: "reversible",
  uncertainty: "mixed",
  budget: "substantial",
  permission: "AUTHORIZED",
  humanActionGate: "NOT_REQUIRED",
});
assert.equal(substantialCapacityOnly.recommendedLevel, "lightweight");
assert.equal(substantialCapacityOnly.capacityFit, "EXCEEDS_WARRANTED_SCOPE");
const insufficientCapacity = api.recommend({
  evidenceSelection: "needed",
  consequence: "consequential",
  uncertainty: "high",
  budget: "bounded",
  permission: "AUTHORIZED",
  humanActionGate: "NOT_REQUIRED",
});
assert.equal(insufficientCapacity.recommendedLevel, "moderate");
assert.equal(insufficientCapacity.capacityFit, "NARROW_OR_ESCALATE");
assert.equal(insufficientCapacity.recommendedAction, "CLARIFY");
assert.match(`${insufficientCapacity.requiredGate} ${insufficientCapacity.plannedStopCondition}`, /narrow|capacity|resource boundary/i);
assert.throws(
  () => api.recommend({
    evidenceSelection: "needed",
    consequence: "reversible",
    uncertainty: "low",
    budget: "quick",
    permission: "AUTHORIZED",
    humanActionGate: "NOT_REQUIRED",
    executionState: "COMPLETE",
  }),
  /exact declared fields/,
  "layered API accepted a fabricated execution state",
);
const advanced = api.recommend({
  evidenceSelection: "needed",
  consequence: "consequential",
  uncertainty: "high",
  budget: "substantial",
  permission: "AUTHORIZED",
  humanActionGate: "NOT_REQUIRED",
});
assert.equal(advanced.recommendedLevel, "advanced");
assert.equal(advanced.capacityFit, "WITHIN_SELECTED_BOUNDARY");
assert.match(applyHtml, /consequential \+ high uncertainty \+ substantial approved capacity/);
assert.match(applyHtml, /capacity[^.]*never (?:makes Advanced appropriate|justifies it) by itself/i);
assert.match(implementationChoices, /Advanced is justified only when consequence is high,\s*uncertainty is high, and substantial capacity has been separately approved/i);
assert.doesNotMatch(implementationChoices, /Advanced \| Consequential, high-volume, or long-lived/i);
assert.match(applyHtml, /Capacity mismatch:[\s\S]*Do not silently under-scope/);
assert.match(applyHtml, /When conditions overlap, resolve them in this order:/);
assert.match(applyHtml, /unresolved or blocked permission[\s\S]*required human action gate[\s\S]*insufficient capacity[\s\S]*base level action/);
assert.match(applyHtml, /capacity mismatch[\s\S]*<code>CLARIFY<\/code>[\s\S]*<code>NARROW_OR_ESCALATE<\/code>/);

console.log("PASS Apply cross-artifact parity: ordinary exit, typed permission, human gate, and proportional Advanced trigger");
