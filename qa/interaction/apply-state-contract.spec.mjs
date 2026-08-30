import assert from "node:assert/strict";

await import("../../site/src/recommendation.js");

const api = globalThis.PatternMapRecommendation;
assert.ok(api?.recommend, "recommendation API is unavailable");

const expectedObserved = {
  executionState: "NOT_RUN",
  stopOutcome: "NOT_TRIGGERED",
  outcomeState: "NOT_OBSERVED",
  learningReview: "NOT_AVAILABLE",
  humanDisposition: "NOT_RECORDED",
};
assert.deepEqual(api.INITIAL_OBSERVED_STATE, expectedObserved);

const resultKeys = [
  "capacityFit",
  "humanActionGate",
  "learningOption",
  "permissionState",
  "plannedStopCondition",
  "recommendedAction",
  "recommendedLevel",
  "requiredGate",
  "summary",
  "title",
];
const fabricatedEventTokens = [
  "STOPPED_",
  "HUMAN_DISPOSITION_RECORDED",
  "LEARNING_PENDING_OUTCOME",
  "LEARNING_REVIEWED",
];
const checkPlanningOnly = (result) => {
  assert.deepEqual(Object.keys(result).sort(), resultKeys);
  const serialized = JSON.stringify(result);
  for (const token of fabricatedEventTokens) {
    assert.equal(serialized.includes(token), false, `planning output fabricated event token ${token}`);
  }
  assert.deepEqual(api.INITIAL_OBSERVED_STATE, expectedObserved, "planning must not mutate observed state");
};

const ordinary = api.recommend({ evidenceSelection: "none" });
checkPlanningOnly(ordinary);
assert.equal(ordinary.recommendedLevel, "ordinary");
assert.equal(ordinary.recommendedAction, "ORDINARY_RECORD");
assert.equal(ordinary.permissionState, "NOT_APPLICABLE");
assert.equal(ordinary.humanActionGate, "NOT_APPLICABLE");
assert.equal(ordinary.capacityFit, "NOT_APPLICABLE");
for (const field of ["supplied scope", "material assumptions", "unchecked boundaries", "output"]) {
  assert.match(ordinary.plannedStopCondition, new RegExp(field, "i"), `ordinary record is missing ${field}`);
}
assert.match(ordinary.learningOption, /LEARNING_NOT_APPLICABLE/);
assert.doesNotMatch(JSON.stringify(ordinary), /ANSWER|COMPARE|ACQUIRE|CLARIFY/);

for (const field of [
  "consequence",
  "uncertainty",
  "budget",
  "permission",
  "humanActionGate",
  "evidence_records",
  "route",
  "stop_status",
  "learning_status",
  "influence",
  "executionState",
  "observedOutcome",
  "outcome",
  "humanDisposition",
  "authorized",
]) {
  assert.throws(
    () => api.recommend({ evidenceSelection: "none", [field]: "not-applicable-placeholder" }),
    /ordinary input must use the exact declared fields/,
    `ordinary input incorrectly accepted undeclared field ${field}`,
  );
}

const choices = {
  consequence: ["reversible", "consequential"],
  uncertainty: ["low", "mixed", "high"],
  budget: ["quick", "bounded", "substantial"],
  permission: ["AUTHORIZED", "UNKNOWN", "NOT_AUTHORIZED", "REVOKED"],
  humanActionGate: ["NOT_REQUIRED", "REQUIRED"],
};

let layeredCombinations = 0;
for (const consequence of choices.consequence) {
  for (const uncertainty of choices.uncertainty) {
    for (const budget of choices.budget) {
      for (const permission of choices.permission) {
        for (const humanActionGate of choices.humanActionGate) {
          layeredCombinations += 1;
          const result = api.recommend({
            evidenceSelection: "needed",
            consequence,
            uncertainty,
            budget,
            permission,
            humanActionGate,
          });
          checkPlanningOnly(result);

          const expectedLevel = consequence === "consequential" && uncertainty === "high" && budget === "substantial"
            ? "advanced"
            : (consequence === "consequential" || uncertainty === "high" ? "moderate" : "lightweight");
          assert.equal(result.recommendedLevel, expectedLevel, "route size diverged from the proportionality contract");
          assert.notEqual(result.recommendedLevel, "ordinary", "Stage 0 yes must not resolve to ordinary");
          assert.equal(result.permissionState, permission, "permission state was collapsed or rewritten");
          assert.equal(result.humanActionGate, humanActionGate, "human action gate was not kept separate");
          const expectedCapacityFit = consequence === "consequential" && uncertainty === "high" && budget !== "substantial"
            ? "NARROW_OR_ESCALATE"
            : (expectedLevel === "lightweight" && budget === "substantial" ? "EXCEEDS_WARRANTED_SCOPE" : "WITHIN_SELECTED_BOUNDARY");
          assert.equal(result.capacityFit, expectedCapacityFit, "capacity fit did not preserve the planning boundary");

          if (permission === "UNKNOWN") {
            assert.equal(result.recommendedAction, "ESCALATE");
            assert.match(`${result.requiredGate} ${result.summary}`, /establish|unestablished|unknown/i);
          } else if (permission === "NOT_AUTHORIZED") {
            assert.equal(result.recommendedAction, "HOLD");
            assert.match(`${result.requiredGate} ${result.summary}`, /not authorized|absent|denied|new.*authorization/i);
          } else if (permission === "REVOKED") {
            assert.equal(result.recommendedAction, "HOLD");
            assert.match(`${result.requiredGate} ${result.summary}`, /revok|prior authorization|new scoped authorization/i);
          } else if (humanActionGate === "REQUIRED") {
            assert.equal(result.recommendedAction, "HOLD");
            assert.match(result.requiredGate, /named human/i);
          } else if (expectedCapacityFit === "NARROW_OR_ESCALATE") {
            assert.equal(result.recommendedAction, "CLARIFY");
            assert.match(`${result.requiredGate} ${result.summary}`, /narrow|capacity|resource boundary/i);
          } else if (expectedLevel === "lightweight") {
            assert.equal(result.recommendedAction, "ANSWER_PROVISIONALLY");
          } else {
            assert.equal(result.recommendedAction, "COMPARE");
          }
        }
      }
    }
  }
}

assert.equal(layeredCombinations, 144, "expected the complete 2×3×3×4×2 layered matrix");
for (const field of [
  "evidence_records",
  "route",
  "stop_status",
  "learning_status",
  "influence",
  "executionState",
  "observedOutcome",
  "outcome",
  "humanDisposition",
  "authorized",
]) {
  assert.throws(
    () => api.recommend({
      evidenceSelection: "needed",
      consequence: "reversible",
      uncertainty: "low",
      budget: "quick",
      permission: "AUTHORIZED",
      humanActionGate: "NOT_REQUIRED",
      [field]: "fabricated-execution-value",
    }),
    /Layered planning input must use the exact declared fields/,
    `layered input incorrectly accepted undeclared field ${field}`,
  );
}
for (const uncertainty of ["low", "mixed"]) {
  const capacityOnly = api.recommend({
    evidenceSelection: "needed",
    consequence: "reversible",
    uncertainty,
    budget: "substantial",
    permission: "AUTHORIZED",
    humanActionGate: "NOT_REQUIRED",
  });
  assert.equal(capacityOnly.recommendedLevel, "lightweight", "substantial capacity alone must not trigger Advanced");
  assert.equal(capacityOnly.capacityFit, "EXCEEDS_WARRANTED_SCOPE", "excess capacity should not enlarge the warranted route");
}

assert.throws(() => api.recommend({ evidenceSelection: "unknown" }), /Invalid evidenceSelection/);
assert.throws(() => api.recommend({
  evidenceSelection: "needed",
  consequence: "reversible",
  uncertainty: "low",
  budget: "quick",
  permission: "AUTHORIZED",
}), /exact declared fields \(missing: humanActionGate\)/);

console.log("PASS Apply terminal Stage 0 and planning-state contract across 1 ordinary + 144 layered combinations");
