## 2025-05-18 - Focus Visible States on Custom Toggle Switch Inputs
**Learning:** In custom toggle switches using hidden checkboxes (`opacity: 0` or visually hidden), standard `:focus` on the input element is not visible to keyboard users. Linking `input:focus-visible` to the adjacent track sibling (`input:focus-visible + .switch-track`) ensures visible focus indicators without cluttering pointer interactions.
**Action:** Always map `:focus-visible` on visually hidden inputs to their visible custom sibling element (`.switch-track`).
