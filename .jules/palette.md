## 2025-10-01 - Interactive Form Status with Dynamic Glass Resizing
**Learning:** Adding status messages inside dynamic glassmorphic card elements changes element dimensions; calling `.measure()`, `.clampTarget()`, and `.refresh()` prevents glass effect background displacement alignment and clipping bugs.
**Action:** Always trigger glass layout updates after inline DOM modifications within glass containers.
