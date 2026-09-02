## 2025-05-18 - Visible Focus for Custom Toggle Switches
**Learning:** Custom styled toggle switches that visually hide native checkbox inputs (`opacity: 0`) obscure default browser focus indicators, rendering them invisible during keyboard navigation.
**Action:** Always link focus indicators to adjacent sibling track elements using `input:focus-visible + .switch-track` to maintain accessible keyboard focus states without adding unnecessary DOM elements or Javascript handlers.
