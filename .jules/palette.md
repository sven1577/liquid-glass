## 2025-07-29 - Restoring Custom Toggle Switch Keyboard Focus with Sibling Selectors

**Learning:** Custom toggle switches that visually hide their underlying `<input type="checkbox">` via `position: absolute; opacity: 0; pointer-events: none;` often break keyboard accessibility by losing default focus outlines. While still accessible to screen readers, keyboard-only sighted users cannot track focus without custom styling. Restoring this focus cleanly requires targeting the sibling custom track element when the hidden checkbox is focused.

**Action:** Whenever a design pattern completely hides a semantic form input for aesthetic custom elements, use the adjacent sibling selector linked with `:focus-visible` (e.g., `input:focus-visible + .switch-track`) to render a highly visible, custom-designed focus ring matching the surrounding theme.
