# Palette's Journal

## 2025-02-17 - Custom Toggle Accessibility and Focus Indicators
**Learning:** Hiding semantic `<input type="checkbox">` elements via absolute positioning and opacity:0 to replace them with beautiful custom-styled elements (like track/thumb toggles) completely destroys keyboard focus indicators for sighted keyboard users. Sighted users using tab navigation are left with no feedback as to which element currently has focus. Linking the semantic checkbox focus state to the visual track using the adjacent sibling selector with `:focus-visible` (e.g., `input:focus-visible + .switch-track`) is an elegant, non-disruptive, and highly accessible way to maintain visual state synchronization.
**Action:** Whenever implementing a custom form element (switch, checkbox, radio button) that visually conceals the native input, ensure focus states are explicitly wired to the visual wrapper using `input:focus-visible + .custom-ui-class`.

## 2025-02-18 - Keyboard Accessibility for Spring Physics Floating Cards
**Learning:** Custom interactive widgets positioned with spring physics and pointer drag listeners isolate keyboard-only users unless explicitly wired to keyboard events. Adding `tabindex="0"` to the container with a clear `:focus-visible` outline allows keyboard focus, but keyboard event handlers must strictly verify `if (e.target !== this.el) return;` so that Arrow keys pressed within embedded child elements (such as text input fields) do not trigger card movements or break form input navigation.
**Action:** When adding keyboard navigation to draggable container components, always guard against event bubbling from child input/button elements and map Arrow keys directly into the physics target coordinates.
