## 2026-09-26 - Shared Canvas Reuse, Map Caching, and RAF Idling

**Learning:** SVG filter displacement map generation via 2D Canvas in `liquid-glass.js` incurred high GC pressure from dynamic canvas creation (`document.createElement('canvas')`) and expensive synchronous PNG base64 encoding (`canvas.toDataURL()`). Furthermore, spring physics animation loops in floating glass card components continuously triggered `requestAnimationFrame` when idle.

**Action:** Reuse a shared singleton 2D canvas/context across map renders, maintain a bounded Map-based LRU cache for generated displacement data URIs, cache last-measured element dimensions on instances to short-circuit redundant updates, and pause spring physics `requestAnimationFrame` loops when velocity and displacement settle below threshold (`0.005`).
