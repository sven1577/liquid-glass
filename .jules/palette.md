## 2025-05-18 - Keyboard Focus Indicators for Custom Toggle Inputs
**Learning:** Custom-styled toggle switches that visually hide standard `<input type="checkbox">` elements can obscure keyboard focus unless `:focus-visible` is specifically targeted on the hidden input and styled on the adjacent visible sibling (e.g. `input:focus-visible + .switch-track`).
**Action:** When implementing custom form controls or toggle switches, always bind `:focus-visible` styles on the semantic hidden input to highlight its adjacent visual track/container for keyboard accessibility.
