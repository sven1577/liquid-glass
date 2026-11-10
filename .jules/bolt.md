## 2026-07-09 - Pause Spring Physics Loops on Idle
**Learning:** In interactive spring physics widgets (`GlassCard`), continuous `requestAnimationFrame` loops run unconditionally at 60fps even when displacement and velocity are virtually zero, causing constant GPU/CPU style recalcs and battery drain while the card is idle.
**Action:** Track an `animating` flag, break the `requestAnimationFrame` chain once velocity and distance to target drop below an imperceptible threshold (e.g. `0.005`), and provide a `wake()` method called on pointer/resize events.
