# Palette's Journal

## 2026-03-29 - Draggable Spring Physics Container Keyboard Navigation
**Learning:** When making floating/draggable spring physics containers keyboard-navigable via arrow keys, check `if (e.target !== containerElement) return;` inside the keydown listener. This prevents arrow key navigation inside interactive child components (like text inputs, select elements, or buttons) from triggering container physics movements or interfering with default child component interactions.
**Action:** Always filter `e.target === containerElement` on interactive physics container keydown handlers to safeguard child accessibility.
