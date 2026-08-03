# Palette's Journal

## 2025-02-17 - Custom Toggle Accessibility and Focus Indicators
**Learning:** Hiding semantic `<input type="checkbox">` elements via absolute positioning and opacity:0 to replace them with beautiful custom-styled elements (like track/thumb toggles) completely destroys keyboard focus indicators for sighted keyboard users. Sighted users using tab navigation are left with no feedback as to which element currently has focus. Linking the semantic checkbox focus state to the visual track using the adjacent sibling selector with `:focus-visible` (e.g., `input:focus-visible + .switch-track`) is an elegant, non-disruptive, and highly accessible way to maintain visual state synchronization.
**Action:** Whenever implementing a custom form element (switch, checkbox, radio button) that visually conceals the native input, ensure focus states are explicitly wired to the visual wrapper using `input:focus-visible + .custom-ui-class`.
