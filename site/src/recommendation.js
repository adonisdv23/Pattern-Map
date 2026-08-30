(() => {
  const layeredChoices = {
    consequence: new Set(["reversible", "consequential"]),
    uncertainty: new Set(["low", "mixed", "high"]),
    budget: new Set(["quick", "bounded", "substantial"]),
    permission: new Set(["AUTHORIZED", "UNKNOWN", "NOT_AUTHORIZED", "REVOKED"]),
    humanActionGate: new Set(["NOT_REQUIRED", "REQUIRED"]),
  };

  const INITIAL_OBSERVED_STATE = Object.freeze({
    executionState: "NOT_RUN",
    stopOutcome: "NOT_TRIGGERED",
    outcomeState: "NOT_OBSERVED",
    learningReview: "NOT_AVAILABLE",
    humanDisposition: "NOT_RECORDED",
  });

  const ordinaryPlan = Object.freeze({
    recommendedLevel: "ordinary",
    recommendedAction: "ORDINARY_RECORD",
    permissionState: "NOT_APPLICABLE",
    humanActionGate: "NOT_APPLICABLE",
    capacityFit: "NOT_APPLICABLE",
    requiredGate: "Use Stage 0 only when the supplied-material transformation is already permitted and needs no permission decision, evidence judgment, memory reuse, human action gate, or external influence.",
    plannedStopCondition: "Return only the supplied scope, material assumptions, unchecked boundaries, and output; then stop.",
    learningOption: "LEARNING_NOT_APPLICABLE — this ordinary record creates no route, stop event, outcome, or learning event.",
    title: "End ordinary work with four fields.",
    summary: "Stage 0 found no evidence-selection work. Perform the reversible supplied-material transformation, write the four-field ordinary record, and do not manufacture a layered workflow.",
  });

  const layeredCopy = {
    lightweight: {
      title: "Use one alternate route and one clear limit.",
      summary: "A bounded pass can compare one additional route, challenge the leading interpretation, and preserve the main uncertainty without creating a full evidence system.",
      action: "ANSWER_PROVISIONALLY",
      gate: "Human review before any consequential use of the provisional answer.",
      stop: "Stop after one authorized alternate route and one challenge, or when the stated resource limit is reached.",
      learning: "Optional only if an expectation and outcome window are defined before execution.",
    },
    moderate: {
      title: "Make consequential or highly uncertain work reproducible.",
      summary: "Keep source identity, comparison, uncertainty, permission, influence, and a human checkpoint visible before material shapes a consequential answer.",
      action: "COMPARE",
      gate: "Named human review before the recommendation is used for a consequential decision.",
      stop: "Stop when the named comparison is complete, a critical gap remains, or the authorized resource boundary is reached.",
      learning: "Plan only after recording an expectation and outcome window; no outcome has been observed yet.",
    },
    advanced: {
      title: "Engineer only when consequence, uncertainty, and approved capacity converge.",
      summary: "High-consequence, high-uncertainty evidence selection with substantial approved capacity may warrant queryable records and repeated review. Capacity alone never justifies this route.",
      action: "COMPARE",
      gate: "Explicit permission and accountable human review before influence or external action.",
      stop: "Stop at the approved resource boundary or when unresolved permission, identity, or evidence gaps block safe influence.",
      learning: "Define and lock the expectation, attribution boundary, and review window before any run.",
    },
  };

  const assertEvidenceSelection = (input) => {
    if (!input || !new Set(["none", "needed"]).has(input.evidenceSelection)) {
      throw new TypeError("Invalid evidenceSelection choice.");
    }
  };

  const assertExactInputKeys = (input, expectedKeys, label) => {
    const suppliedKeys = Object.keys(input).sort();
    const expected = [...expectedKeys].sort();
    const unexpected = suppliedKeys.filter((key) => !expectedKeys.has(key));
    const missing = expected.filter((key) => !Object.prototype.hasOwnProperty.call(input, key));
    if (unexpected.length || missing.length) {
      const details = [
        unexpected.length ? `unexpected: ${unexpected.join(", ")}` : "",
        missing.length ? `missing: ${missing.join(", ")}` : "",
      ].filter(Boolean).join("; ");
      throw new TypeError(`${label} input must use the exact declared fields (${details}).`);
    }
  };

  const assertOrdinaryIsTerminal = (input) => {
    assertExactInputKeys(input, new Set(["evidenceSelection"]), "Stage 0 ordinary");
  };

  const assertLayeredInput = (input) => {
    assertExactInputKeys(
      input,
      new Set(["evidenceSelection", ...Object.keys(layeredChoices)]),
      "Layered planning",
    );
    for (const [field, values] of Object.entries(layeredChoices)) {
      if (!values.has(input[field])) throw new TypeError(`Invalid ${field} choice.`);
    }
  };

  const levelFor = ({ consequence, uncertainty, budget }) => {
    if (consequence === "consequential" && uncertainty === "high" && budget === "substantial") return "advanced";
    if (consequence === "consequential" || uncertainty === "high") return "moderate";
    return "lightweight";
  };

  const capacityFitFor = ({ consequence, uncertainty, budget }, recommendedLevel) => {
    if (consequence === "consequential" && uncertainty === "high" && budget !== "substantial") {
      return "NARROW_OR_ESCALATE";
    }
    if (recommendedLevel === "lightweight" && budget === "substantial") {
      return "EXCEEDS_WARRANTED_SCOPE";
    }
    return "WITHIN_SELECTED_BOUNDARY";
  };

  const finalizeLayeredPlan = (input, recommendedLevel, copy) => Object.freeze({
    recommendedLevel,
    permissionState: input.permission,
    humanActionGate: input.humanActionGate,
    capacityFit: capacityFitFor(input, recommendedLevel),
    ...copy,
  });

  const blockedPermissionPlan = (input, recommendedLevel) => {
    const permissionPlans = {
      UNKNOWN: {
        recommendedAction: "ESCALATE",
        requiredGate: "Establish a scoped permission decision for acquisition, use, retention, disclosure, and influence; preserve UNKNOWN until that decision exists.",
        plannedStopCondition: "Do not acquire, use, retain, disclose, or let the material influence an answer while permission remains UNKNOWN.",
        title: "Establish permission before influence.",
        summary: "Technical access does not resolve an unestablished permission state. Ask the authorized person or policy owner; do not infer consent.",
      },
      NOT_AUTHORIZED: {
        recommendedAction: "HOLD",
        requiredGate: "A new, explicit scoped authorization is required before the prohibited operation or material may influence an answer.",
        plannedStopCondition: "Stop immediately while permission is absent or denied; do not acquire, use, retain, disclose, or act on the material.",
        title: "Keep unauthorized material out of influence.",
        summary: "The operation is not authorized. A quick budget, reversible task, or fluent answer cannot convert that state into permission.",
      },
      REVOKED: {
        recommendedAction: "HOLD",
        requiredGate: "Require a new scoped authorization; the earlier authorization must not be reused or treated as current.",
        plannedStopCondition: "Stop immediately and keep the previously authorized material out of reuse, disclosure, and influence.",
        title: "Honor the revoked boundary.",
        summary: "A prior permission no longer applies. Preserve the revoked state and its history instead of silently resetting it to unknown or authorized.",
      },
    };
    const copy = permissionPlans[input.permission];
    if (!copy) return null;
    return finalizeLayeredPlan(input, recommendedLevel, {
      ...copy,
      learningOption: "LEARNING_NOT_APPLICABLE — no authorized run or outcome route exists while permission is unresolved or blocked.",
    });
  };

  const recommend = (input) => {
    assertEvidenceSelection(input);
    if (input.evidenceSelection === "none") {
      assertOrdinaryIsTerminal(input);
      return ordinaryPlan;
    }

    assertLayeredInput(input);
    const recommendedLevel = levelFor(input);
    const permissionPlan = blockedPermissionPlan(input, recommendedLevel);
    if (permissionPlan) return permissionPlan;

    const capacityMismatch = capacityFitFor(input, recommendedLevel) === "NARROW_OR_ESCALATE";
    if (input.humanActionGate === "REQUIRED") {
      return finalizeLayeredPlan(input, recommendedLevel, {
        recommendedAction: "HOLD",
        requiredGate: capacityMismatch
          ? "The named human must approve consequential use, and the decision must be narrowed to the selected capacity or receive a separately approved larger boundary."
          : "The named human must approve the proposed consequential use or action before it occurs.",
        plannedStopCondition: capacityMismatch
          ? "Remain on hold until both the human action gate and the capacity mismatch are resolved; do not silently under-scope the evidence work."
          : "Remain on hold until that explicit human action gate is satisfied; technical access and evidence quality do not satisfy it.",
        learningOption: "No learning route begins until an authorized run defines an expectation and outcome window.",
        title: "Keep the human action gate in front of action.",
        summary: capacityMismatch
          ? "The system may prepare a narrower question for review, but neither the named person's decision nor enough capacity for the high-consequence, high-uncertainty route has been recorded."
          : "The system may prepare an authorized comparison or recommendation for review, but it cannot treat a person's decision as already recorded.",
      });
    }

    if (capacityMismatch) {
      return finalizeLayeredPlan(input, recommendedLevel, {
        recommendedAction: "CLARIFY",
        requiredGate: "An authorized person must narrow the decision to fit the selected capacity or approve a larger resource boundary before evidence influences a consequential answer.",
        plannedStopCondition: "Hold before influence while the high-consequence, high-uncertainty route exceeds its selected capacity; do not silently under-scope it.",
        learningOption: "No learning route begins until an authorized run defines an expectation and outcome window.",
        title: "Narrow the decision or escalate capacity.",
        summary: "High consequence and high uncertainty may warrant deeper work, but the selected quick or bounded capacity does not support it. Budget constrains the route; it does not prove sufficiency.",
      });
    }

    const base = layeredCopy[recommendedLevel];
    return finalizeLayeredPlan(input, recommendedLevel, {
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
