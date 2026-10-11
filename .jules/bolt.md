# Bolt's Journal - Critical Performance Learnings

## 2025-05-18 - Pause Spring Physics rAF Loops When Resting
**Learning:** Continuous `requestAnimationFrame` animation loops in spring physics widgets continue firing 60-120fps forever even when stationary if not explicitly paused when settlement thresholds are reached, causing unnecessary idle CPU/GPU usage and battery drain.
**Action:** Always pause `requestAnimationFrame` when physics velocity and displacement decay below a threshold (`0.005`), and restart the animation loop (`startLoop()`) on user interactions (`pointerdown`, `pointermove`) or layout changes (`resize`).
