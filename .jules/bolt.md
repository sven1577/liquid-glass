# Bolt's Journal

## 2025-05-14 - Idle animation loop sleep in spring physics demo
**Learning:** Continuous `requestAnimationFrame` loops in custom spring physics simulations (like `GlassCard`) cause perpetual 60+ FPS idle rendering, draining CPU/GPU and battery even when UI elements are stationary.
**Action:** Track active animation state (`this.animating`) and pause the rAF loop once velocities and position deltas fall below a perceptual threshold (e.g., `< 0.005`), then cleanly snap values and restart the loop only upon user interaction (pointermove/resize/drag).
