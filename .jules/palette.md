# Palette's Journal - Critical UX & Accessibility Learnings

## 2025-05-18 - Keyboard Navigation for Draggable Container Components
**Learning:** When adding keyboard navigation (e.g., Arrow key movement) to interactive draggable containers that contain child inputs or controls, verify `e.target === containerElement` in `keydown` listeners. Otherwise, child input interactions (e.g. moving cursor in text fields or adjusting sliders) will unexpectedly trigger physics movement on the parent container.
**Action:** Always check `if (e.target !== this.el) return;` in keydown listeners on focusable container widgets.
