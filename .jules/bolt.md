## 2026-07-09 - Spring Physics Idle Animation Pause
**Learning:** Continuous `requestAnimationFrame` loops in UI physics engines (such as `GlassCard`) consume unnecessary CPU/battery cycles when resting at full stop.
**Action:** Always check settlement conditions (e.g. speed and residual distance < 0.005) to halt the rAF loop, and implement a `wake()` trigger on pointer/keyboard interaction events to resume execution seamlessly.
