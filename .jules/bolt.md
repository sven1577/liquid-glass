## 2026-10-01 - Spring Physics Loop Settlement Thresholds
**Learning:** Continuous requestAnimationFrame animation loops in interactive physics components (e.g. glassmorphic cards) consume excessive main thread CPU/battery resources when idle if not explicitly paused. Settlement thresholds must check both velocity and residual displacement.
**Action:** Always implement a settlement check (e.g. `Math.abs(vx) < threshold && Math.abs(dx) < threshold`) to pause rAF loops when elements settle, and re-trigger `startAnimation()` on user interactions.
