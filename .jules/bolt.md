## 2025-05-15 - Idle Animation Settlement in Physics Components
**Learning:** Spring physics loops running an un-throttled requestAnimationFrame consume unnecessary CPU/GPU resources even when elements are stationary.
**Action:** Always check combined velocity and distance-to-target against a settlement threshold (e.g., 0.005) to snap final coordinates and pause the rAF loop, resuming only on user interaction or resize events.
