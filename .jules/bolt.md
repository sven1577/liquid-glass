## 2025-05-18 - Pause Idle Animation Frame Loops in Physics Simulation
**Learning:** Running continuous `requestAnimationFrame` loops when spring physics elements are stationary leads to unnecessary CPU ticks and battery drain. Checking displacement and velocity against a small settlement threshold (`< 0.005`) allows pausing the loop without compromising animation smoothness.
**Action:** Always include an `animating` flag and a `wake()` trigger on user interaction/resize events when building spring physics or custom animation loops.
