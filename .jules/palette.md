## 2025-05-18 - Visible Focus States for Custom Switch Inputs
**Learning:** Custom-styled switch inputs that set `opacity: 0` on `<input type="checkbox">` obscure default browser focus rings, leaving keyboard users without visual feedback when navigating forms.
**Action:** Use adjacent sibling selectors with `:focus-visible` (e.g. `input:focus-visible + .switch-track`) to display clear focus rings when custom controls receive keyboard focus.
