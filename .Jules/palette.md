## 2025-05-18 - Accessible custom toggle focus states
**Learning:** For custom-styled toggle inputs that hide semantic checkboxes with `opacity: 0`, standard focus pseudo-classes on the hidden input are invisible. Using adjacent sibling selectors linked with `:focus-visible` (e.g. `input:focus-visible + .switch-track`) accurately projects the keyboard focus indicator onto the visible track.
**Action:** When styling visually hidden or transparent inputs with custom control tracks/indicators, target adjacent sibling focus-visible states (`input:focus-visible + .custom-track`).
