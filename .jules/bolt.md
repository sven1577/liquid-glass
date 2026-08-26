## 2025-05-18 - Pausing Spring Physics Animation Loops When Idle
**Learning:** In spring physics UI animation loops (like `GlassCard`), running continuous `requestAnimationFrame` calls even when stationary causes permanent CPU/GPU usage and layout recalculations. Checking settlement thresholds (`Math.hypot(tx - x, ty - y) < 0.001 && Math.hypot(vx, vy) < 0.001`) allows snapping state and safely pausing the loop.
**Action:** Always implement a settlement check and an animation flag in rAF-based spring loops, restarting the loop only when new user interactions or window resizes occur.
