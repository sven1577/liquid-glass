# Palette's Journal - Critical UX/A11y Learnings

## 2024-08-12 - Keyboard Focus and Navigation for Interactive/Draggable Elements
**Learning:** Custom components like hidden checkboxes and draggable cards completely bypass standard keyboard navigation and visual focus states if not explicitly handled. For custom-styled checkboxes, linking adjacent sibling selectors with `:focus-visible` ensures keyboard focus is visible. For spring-physics-driven draggable components, mapping standard Arrow keys (and Shift modifier for larger step increments) to target coordinates provides smooth, fully animated keyboard-driven positioning.
**Action:** Always map focus-visible outlines to custom toggle elements and implement keyboard listeners on draggable components that update coordinate targets to ensure an inclusive, delightful UX.
