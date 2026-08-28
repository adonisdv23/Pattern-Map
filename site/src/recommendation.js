(() => {
  const allowed = {
    evidenceSelection: new Set(["none", "needed"]),
    consequence: new Set(["reversible", "consequential"]),
    uncertainty: new Set(["low", "mixed", "high"]),
    budget: new Set(["quick", "bounded", "substantial"]),
    permission: new Set(["supplied", "restricted", "human-gate"]),
  };

  const INITIAL_OBSERVED_STATE = Object.freeze({
    executionState: "NOT_RUN",
    stopOutcome: "NOT_TRIGGERED",
    outcomeState: "NOT_OBSERVED",
    learningReview: "NOT_AVAILABLE",
    humanDisposition: "NOT_RECORDED",
  });

  const assertValid = (input) => {
    for (const [field, values] of Object.entries(allowed)) {
      if (!values.has(input?.[field])) {
        throw new TypeError(`Invalid ${field} choice.`);
      }
    }
  };

  const levelFor = ({ evidenceSelection, consequence, uncertainty, budget }) => {
    if (evidenceSelection === "none") return "ordinary";
    if (budget === "substantial" || (consequence === "consequential" && uncertainty === "high")) {
      return "advanced";
    }
    if (consequence === "consequential" || uncertainty === "high") return "moderate";
    return "lightweight";
  };

  const levelCopy = {
    ordinary: {
      title: "Do less when the task is simple.",
      summary: "Stage 0 found no evidence-selection work. Transform only the supplied material, keep material assumptions visible, and do not manufacture an evidence workflow.",
      action: "ANSWER",
      gate: "No additional gate identified; consequential action still remains with the named person.",
      stop: "Finish the supplied-material transformation. Do not begin external acquisition unless the brief changes.",
      learning: "No learning route is planned. A later outcome would need its own expectation and review window.",
    },
    lightweight: {
      title: "Use one alternate route and one clear limit.",
      summary: "A bounded pass can compare one additional route, challenge the leading interpretation, and preserve the main uncertainty without creating a full evidence system.",
      action: "ANSWER_PROVISIONALLY",
      gate: "Human review before any consequential use of the provisional answer.",
      stop: "Stop after one authorized alternate route and one challenge, or when the stated time limit is reached.",
      learning: "Optional only if an expectation and outcome window are defined before execution.",
    },
    moderate: {
      title: "Make consequential or repeated work reproducible.",
      summary: "Keep source identity, comparison, uncertainty, permission, influence, and a human checkpoint visible before material shapes a consequential answer.",
      action: "COMPARE",
      gate: "Named human review before the recommendation is used for a consequential decision.",
      stop: "Stop when the named comparison is complete, a critical gap remains, or the authorized budget is reached.",
      learning: "Plan only after recording an expectation and outcome window; no outcome has been observed yet.",
    },
    advanced: {
      title: "Engineer only when hidden mistakes justify the cost.",
      summary: "Queryable records and review queues may be warranted, but this recommendation grants no permission to acquire, disclose, spend, publish, or act.",
      action: "COMPARE",
      gate: "Explicit permission and accountable human review before influence or external action.",
      stop: "Stop at the approved resource boundary or when unresolved permission, identity, or evidence gaps block safe influence.",
      learning: "Define and lock the expectation, attribution boundary, and review window before any run.",
    },
  };

  const recommend = (input) => {
    assertValid(input);
    const recommendedLevel = levelFor(input);
    const base = levelCopy[recommendedLevel];

    if (input.permission === "restricted") {
      return Object.freeze({
        recommendedLevel,
        recommendedAction: "CLARIFY",
        requiredGate: "Clarify permission to acquire, use, retain, disclose, and act before the material can influence an answer.",
        plannedStopCondition: "Hold while permission is absent, restricted, or ambiguous.",
        learningOption: "No learning path can be recommended until permission is resolved and an actual outcome route is defined.",
        title: "Clarify permission before influence.",
        summary: "Restricted material cannot be converted into an answer recommendation merely because the task is quick, reversible, or low consequence.",
      });
    }

    if (input.permission === "human-gate") {
      return Object.freeze({
        recommendedLevel,
        recommendedAction: "HOLD",
        requiredGate: "The named human must approve the proposed use before the material influences an answer or action.",
        plannedStopCondition: "Remain on hold until that explicit gate is satisfied; technical access does not satisfy it.",
        learningOption: "No learning path can be recommended until an authorized run defines an expectation and outcome window.",
        title: "Keep the human gate in front of influence.",
        summary: "The system may prepare a question or comparison for review, but it cannot treat the person’s decision as already recorded.",
      });
    }

    return Object.freeze({
      recommendedLevel,
      recommendedAction: base.action,
      requiredGate: base.gate,
      plannedStopCondition: base.stop,
      learningOption: base.learning,
      title: base.title,
      summary: base.summary,
    });
  };

  globalThis.PatternMapRecommendation = Object.freeze({
    INITIAL_OBSERVED_STATE,
    recommend,
  });
})();
