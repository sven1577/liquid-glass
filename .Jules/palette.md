## 2025-05-18 - Keyboard Focus Visible Styling on Custom Toggle Inputs
**Learning:** For custom-styled toggle inputs that visually hide the native checkbox input, relying on standard `:focus` on the container or native input is insufficient. Using `input:focus-visible + .switch-track` ensures focus outlines appear properly when navigating via keyboard without appearing on click interactions.
**Action:** Always link hidden interactive inputs with adjacent visual element selectors via `:focus-visible` to maintain accessible keyboard focus states without affecting mouse click styling.
