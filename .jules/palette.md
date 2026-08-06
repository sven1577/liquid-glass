## 2024-08-06 - Dynamic Recalculation for Glassmorphic Elements
**Learning:** For custom glassmorphic components leveraging SVG dynamic filters (such as Apple-style refraction), any user action that modifies the DOM structure or dimension of elements within the container can cause background displacement and alignment/clipping bugs. Dynamic layout changes must trigger sequential calls to `.measure()`, `.clampTarget()`, and `.refresh()` on the glassmorphic instance to correctly align the refraction background.
**Action:** Always capture instances of glassmorphic elements and invoke their measure-and-refresh lifecycle hooks immediately after modifying form/content layout.

## 2024-08-06 - Focus-Visible States for Hidden Checkboxes
**Learning:** Standard keyboard accessibility guidelines require all interactive elements to have a clear focus state. For custom toggle switches or switch tracks where the semantic `<input type="checkbox">` is hidden visually, using adjacent sibling selectors with `:focus-visible` (e.g., `input:focus-visible + .switch-track`) is vital to preserve keyboard outline indicators.
**Action:** Never forget to style adjacent or parent elements when styling custom focus states for visually hidden semantic inputs.
