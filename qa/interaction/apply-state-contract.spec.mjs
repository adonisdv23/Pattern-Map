import assert from "node:assert/strict";

await import("../../site/src/recommendation.js");

const api = globalThis.PatternMapRecommendation;
assert.ok(api?.recommend, "recommendation API is unavailable");

assert.deepEqual(api.INITIAL_OBSERVED_STATE, {
  executionState: "NOT_RUN",
  stopOutcome: "NOT_TRIGGERED",
  outcomeState: "NOT_OBSERVED",
  learningReview: "NOT_AVAILABLE",
  humanDisposition: "NOT_RECORDED",
});

const choices = {
  consequence: ["reversible", "consequential"],
  uncertainty: ["low", "mixed", "high"],
  budget: ["quick", "bounded", "substantial"],
  permission: ["supplied", "restricted", "human-gate"],
};
const fabricatedEventTokens = [
  "COMPLETE",
  "STOPPED_",
  "HUMAN_DISPOSITION_RECORDED",
  "LEARNING_PENDING_OUTCOME",
  "LEARNING_REVIEWED",
];

let combinations = 0;
for (const consequence of choices.consequence) {
  for (const uncertainty of choices.uncertainty) {
    for (const budget of choices.budget) {
      for (const permission of choices.permission) {
        combinations += 1;
        const result = api.recommend({ consequence, uncertainty, budget, permission });
        assert.deepEqual(Object.keys(result).sort(), [
          "learningOption",
          "plannedStopCondition",
          "recommendedAction",
          "recommendedLevel",
          "requiredGate",
          "summary",
          "title",
        ]);
        const serialized = JSON.stringify(result);
        for (const token of fabricatedEventTokens) {
          assert.equal(serialized.includes(token), false, `planning output fabricated event token ${token}`);
        }
        if (permission === "restricted") {
          assert.equal(result.recommendedAction, "CLARIFY", "restricted permission must dominate route size");
          assert.match(result.requiredGate, /permission/i);
        }
        if (permission === "human-gate") {
          assert.equal(result.recommendedAction, "HOLD", "human gate must dominate route size");
          assert.match(result.requiredGate, /named human/i);
        }
      }
    }
  }
}

assert.equal(combinations, 54, "expected the complete 2×3×3×3 planning matrix");
assert.throws(() => api.recommend({ consequence: "unknown" }), /Invalid consequence/);

console.log("PASS Apply planning-state contract across 54 combinations");
