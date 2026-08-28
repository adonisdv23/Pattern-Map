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
  evidenceSelection: ["none", "needed"],
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
for (const evidenceSelection of choices.evidenceSelection) {
  for (const consequence of choices.consequence) {
    for (const uncertainty of choices.uncertainty) {
      for (const budget of choices.budget) {
        for (const permission of choices.permission) {
          combinations += 1;
          const input = { evidenceSelection, consequence, uncertainty, budget, permission };
          const result = api.recommend(input);
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

          if (evidenceSelection === "needed") {
            assert.notEqual(result.recommendedLevel, "ordinary", "Stage 0 yes must not resolve to the ordinary path");
          }
          if (evidenceSelection === "none") {
            assert.equal(result.recommendedLevel, "ordinary", "Stage 0 no must remain on the ordinary path");
            if (permission === "supplied") {
              assert.equal(result.recommendedAction, "ANSWER", "Stage 0 no must not introduce acquisition or comparison work");
              assert.match(result.plannedStopCondition, /supplied-material transformation/i);
            }
          }
          if (permission === "restricted") {
            assert.equal(result.recommendedAction, "CLARIFY", "restricted permission must dominate route size");
            assert.match(result.requiredGate, /permission/i);
          }
          if (permission === "human-gate") {
            assert.equal(result.recommendedAction, "HOLD", "human gate must dominate route size");
            assert.match(result.requiredGate, /named human/i);
          }
          assert.deepEqual(api.INITIAL_OBSERVED_STATE, {
            executionState: "NOT_RUN",
            stopOutcome: "NOT_TRIGGERED",
            outcomeState: "NOT_OBSERVED",
            learningReview: "NOT_AVAILABLE",
            humanDisposition: "NOT_RECORDED",
          }, "planning must not mutate observed state");
        }
      }
    }
  }
}

assert.equal(combinations, 108, "expected the complete 2×2×3×3×3 planning matrix");
assert.throws(() => api.recommend({ evidenceSelection: "unknown" }), /Invalid evidenceSelection/);
assert.throws(() => api.recommend({
  evidenceSelection: "none",
  consequence: "unknown",
  uncertainty: "low",
  budget: "quick",
  permission: "supplied",
}), /Invalid consequence/);

console.log("PASS Apply Stage 0 and planning-state contract across 108 combinations");
