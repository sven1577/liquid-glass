## 2025-03-06 - Keyboard accessibility for draggable/floating UI elements with physics
**Learning:** Adding draggable cards or widgets with spring-based or physics-based inertia can completely lock out keyboard users unless key events are integrated with the underlying target coordinates (`tx`/`ty`). Moving the element directly via DOM coordinates breaks the visual illusion of inertia, so modifying the physics target coordinates (`tx`/`ty`) preserves smooth, animated spring transitions.
**Action:** Map Arrow keys (with optional Shift modifier for larger steps) directly to the physics engine's target positions.

## 2025-03-06 - Custom-styled checkbox/switch toggles
**Learning:** Modern custom toggles that visually hide the semantic checkbox input are often invisible to keyboard-only users because the standard focus outline on the checkbox itself is hidden. Sighted keyboard users cannot tell if the element is focused.
**Action:** Use adjacent sibling selectors combined with `:focus-visible` (e.g., `input:focus-visible + .switch-track`) to visual-style focus outlines or rings on the custom track component.
