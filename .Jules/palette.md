## 2025-05-18 - Keyboard Event Isolation on Interactive Container Widgets
**Learning:** When adding keyboard navigation to a custom interactive container widget, event listeners (such as Arrow key listeners) will catch events bubbling up from child inputs, textareas, or buttons if `e.target` is not restricted.
**Action:** Always filter keydown events in container widgets with `if (e.target !== containerElement) return;` to allow child inputs to process arrow keys natively.

## 2025-05-18 - Dynamic Glassmorphic Card Reflow Recalculations
**Learning:** Adding dynamic content (e.g., success message or form feedback) into a glassmorphic container changes its dimensions. Without explicit re-measurement, glass displacement maps become misaligned or clipped.
**Action:** Whenever container dimensions change dynamically, trigger `.measure()`, `.clampTarget()`, and `.refresh()` sequentially on the glassmorphism instances.
