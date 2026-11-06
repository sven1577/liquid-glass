# Palette's Journal

## 2025-05-18 - Keyboard Navigation for Physics-Driven Floating Elements
**Learning:** Making draggable canvas/DOM overlays with spring physics keyboard-accessible requires binding arrow keys to the simulation's target coordinates rather than directly translating DOM style transforms, while ensuring event propagation stops at the container boundary (`e.target !== container`) to prevent interfering with nested inputs.
**Action:** When adding keyboard controls to draggable physics widgets, update target coordinates (`tx`/`ty`), clamp to boundaries, and ignore events bubbling from interactive child controls.
