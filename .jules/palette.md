# Palette's Journal - UX & Accessibility Learnings

## 2025-08-22 - Focus-visible States and Keyboard Navigation for Floating Physics Containers
**Learning:** Custom interactive container widgets utilizing pointer-based drag/spring physics (like `.glass-card`) often exclude keyboard-only users unless explicitly configured with `tabindex="0"`, focus indicators, and keyboard event handlers. When adding keydown listeners (e.g., arrow keys) to parent container widgets, it is essential to check `if (e.target !== containerElement) return;` so input fields or buttons inside the container do not trigger unwanted movement physics or block keyboard text editing.
**Action:** Always add keyboard arrow key navigation to physics-based draggable containers, check event targets to prevent event leakage from child elements, and provide visible `:focus-visible` focus rings on custom inputs/controls.
