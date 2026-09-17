## 2025-09-17 - Dynamic DOM updates in glassmorphic card containers
**Learning:** Dynamic status updates or DOM height changes inside glassmorphic containers cause background displacement misalignment if the glass matrix is not updated.
**Action:** When updating content inside liquid-glass components, sequentially invoke `.measure()`, `.clampTarget()`, and `.refresh()` on card/effect instances.
