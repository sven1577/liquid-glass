# Palette's Journal — Critical UX/Accessibility Learnings

This journal documents critical, codebase-specific UX and accessibility insights discovered during development.

## 2026-08-11 - Accessible Draggable Floating Cards and Custom Switches
**Learning:** For floating or draggable UI elements using spring physics, we can implement seamless keyboard accessibility by mapping keyboard Arrow keys to the physics engine's target coordinates rather than directly translating the elements. This preserves the satisfying, fluid inertia and squashing animations of the spring physics. Additionally, custom-styled toggle switches that hide native checkboxes require explicit adjacent sibling `:focus-visible` styling (e.g. `input:focus-visible + .switch-track`) to ensure keyboard users have a visible focus indicator without cluttering pointer interaction styles.
**Action:** When working with spring-physics components, map Arrow/Shift-Arrow key listeners to the target properties (e.g., tx/ty). Always define `:focus-visible` selectors for keyboard-navigable elements, particularly custom toggles, to maintain high accessibility.
