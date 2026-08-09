# Palette's Journal - Critical Learnings Only

This journal contains critical UX and accessibility learnings discovered during engineering tasks.
Each entry is added ONLY when a critical learning is made, following this format:

## YYYY-MM-DD - [Title]
**Learning:** [UX/a11y insight]
**Action:** [How to apply next time]

## 2024-11-20 - Keyboard Accessibility for Custom Toggles
**Learning:** Custom toggle inputs (such as switches) that hide semantic checkboxes via `position: absolute; opacity: 0; pointer-events: none;` render the element completely invisible to keyboard users when focused unless focus styles are explicitly delegated to the visible adjacent track or sibling element.
**Action:** For custom switch components, always use adjacent sibling selectors linked with `:focus-visible` (e.g., `input:focus-visible + .switch-track`) to ensure keyboard focus states remain visible to sighted users.
