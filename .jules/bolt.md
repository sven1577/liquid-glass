# Bolt's Journal - Critical Learnings

## 2025-08-20 - Canvas reuse and DataURL caching in liquid-glass.js
**Learning:** In liquid-glass.js, dynamic canvas creation on every `makeMap()` call creates significant GC pressure, and `canvas.toDataURL()` incurs expensive CPU PNG encoding.
**Action:** Reuse a single shared canvas instance and context across map generation calls, and cache data URIs in a bounded LRU Map keyed by map parameters `(w, h, radius, border, mapBlur)`. Also cache last-measured dimensions on instance `refresh()` to avoid unnecessary SVG attribute updates.
