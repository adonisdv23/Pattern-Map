(() => {
  const translateTermPanel = ({
    panel,
    trigger,
    viewportWidth,
    viewportInset = 16,
    blockClearance = 8,
  }) => {
    const required = [
      panel?.left,
      panel?.right,
      panel?.top,
      trigger?.bottom,
      viewportWidth,
      viewportInset,
      blockClearance,
    ];
    if (!required.every(Number.isFinite)) {
      throw new TypeError("term-panel geometry requires finite numeric bounds");
    }
    if (viewportWidth <= 0 || viewportInset < 0 || blockClearance < 0) {
      throw new RangeError("term-panel viewport and clearance values are invalid");
    }

    let inline = 0;
    if (panel.right > viewportWidth - viewportInset) {
      inline -= panel.right - (viewportWidth - viewportInset);
    }
    if (panel.left + inline < viewportInset) {
      inline += viewportInset - (panel.left + inline);
    }

    const block = Math.max(0, trigger.bottom + blockClearance - panel.top);
    return {
      inline: inline < 0 ? Math.floor(inline) : Math.ceil(inline),
      block: Math.ceil(block),
    };
  };

  globalThis.PatternMapTermPopoverGeometry = Object.freeze({ translateTermPanel });
})();
