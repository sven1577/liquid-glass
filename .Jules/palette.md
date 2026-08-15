# Palette's Journal - UX & Accessibility Learnings

## 2025-05-10 - Keyboard focus indication for custom toggle switches
**Learning:** For custom-styled toggle inputs that hide semantic checkboxes behind absolute positioning/zero opacity, standard `:focus` on the container doesn't fire when keyboard tabbing onto the native checkbox element.
**Action:** Use adjacent sibling selectors linked with `:focus-visible` (e.g., `input:focus-visible + .switch-track`) to ensure visible ring indicators appear for keyboard users without showing rings on mouse clicks.
