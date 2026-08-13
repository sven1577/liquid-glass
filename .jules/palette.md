## 2023-11-15 - Preserving Spring Physics in Draggable Elements for Keyboard Users
**Learning:** For draggable/floating UI elements utilizing spring physics, keyboard accessibility can be implemented by mapping Arrow keys (and Shift modifiers for larger step increments) to the physics engine's target coordinates (e.g., tx/ty) to preserve smooth, animated transitions rather than snapping to coordinates.
**Action:** Always map keyboard event handlers to the target variables of physics/interpolation loops instead of overriding element positions directly.

## 2023-11-15 - Focus Visibility on Custom Toggle Inputs
**Learning:** Custom-styled toggle switch inputs that visually hide standard checkboxes can accidentally hide focus indicators if not handled carefully. Linking `:focus-visible` of the hidden checkbox using an adjacent sibling selector (e.g., `input:focus-visible + .switch-track`) ensures keyboard focus remains highly visible to sighted keyboard users.
**Action:** Implement focus indicators on adjacent styled elements matching the native input focus state.
