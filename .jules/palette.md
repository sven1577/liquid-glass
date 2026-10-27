## 2025-05-18 - Visible Focus Outlines on Custom Inputs and Controls
**Learning:** Custom UI elements like hidden checkboxes (`input[type="checkbox"]`) with styled track siblings (`.switch-track`) hide native browser focus indicators.
**Action:** Use adjacent sibling selectors with `:focus-visible` (`input:focus-visible + .switch-track`) and explicit focus rings (`outline: 2px solid var(--accent)`) on custom interactive elements to preserve keyboard accessibility.
