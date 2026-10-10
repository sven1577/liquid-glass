## 2026-03-31 - Pausing Spring Physics Loops on Settlement
**Learning:** Spring physics UI widgets using continuous `requestAnimationFrame` loops cause persistent CPU/GPU usage even when visually static. Checking velocity and residual displacement against a settlement threshold (`< 0.005`) allows safely pausing the loop until reactivated by input events.
**Action:** When working with spring physics or custom interactive animation loops, implement a settlement check in `tick()` to pause `rAF` and resume via event handlers (`pointerdown`, `pointermove`, `resize`).
