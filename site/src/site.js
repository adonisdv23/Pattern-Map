(() => {
  const familyGrid = document.querySelector(".family-grid");
  const focusStatus = document.querySelector("#family-focus-status");
  const familyCards = [...document.querySelectorAll("[data-family-card]")];
  const focusButtons = [...document.querySelectorAll("[data-family-focus]")];
  const clearButton = document.querySelector("[data-family-clear]");

  const clearFamilyFocus = () => {
    familyGrid?.classList.remove("has-focus");
    familyCards.forEach((card) => card.classList.remove("is-focused"));
    focusButtons.forEach((button) => button.setAttribute("aria-pressed", "false"));
    if (focusStatus) focusStatus.textContent = "All six families are visible. Focus controls add emphasis; they never hide essential meaning.";
  };

  focusButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const family = button.dataset.familyFocus;
      const card = document.querySelector(`[data-family-card="${CSS.escape(family)}"]`);
      const wasFocused = card?.classList.contains("is-focused");
      clearFamilyFocus();
      if (!wasFocused && card) {
        familyGrid?.classList.add("has-focus");
        card.classList.add("is-focused");
        button.setAttribute("aria-pressed", "true");
        if (focusStatus) focusStatus.textContent = `${family} is focused. The other families remain visible for comparison.`;
      }
    });
  });

  clearButton?.addEventListener("click", clearFamilyFocus);

  const moreButton = document.querySelector(".nav-more");
  const secondary = document.querySelector(".secondary-nav-wrap");
  const setMoreOpen = (isOpen, moveFocus = false) => {
    moreButton?.setAttribute("aria-expanded", String(isOpen));
    secondary?.classList.toggle("is-open", isOpen);
    if (isOpen && moveFocus) secondary?.querySelector("a")?.focus();
  };
  moreButton?.addEventListener("click", () => {
    const isOpen = moreButton.getAttribute("aria-expanded") === "true";
    setMoreOpen(!isOpen, !isOpen);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape" || moreButton?.getAttribute("aria-expanded") !== "true") return;
    setMoreOpen(false);
    moreButton.focus();
  });
})();
