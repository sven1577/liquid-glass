# Palette Journal - UX & Accessibility Learnings

## 2026-10-16 - Focus Rings for Visually Hidden Switch Inputs
**Learning:** Custom switch toggles that visually hide native `<input type="checkbox">` controls lose standard browser focus indicators, making keyboard navigation invisible unless explicit focus styles are applied to the visible track element.
**Action:** Use adjacent sibling selectors linked with `:focus-visible` (e.g., `input:focus-visible + .switch-track`) to display clear focus rings on custom controls when keyboard focus lands on the hidden input.
