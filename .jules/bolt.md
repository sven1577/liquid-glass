# Bolt's Journal

## 2025-05-18 - Canvas Reuse and LRU Data URL Caching in SVG Filters
**Learning:** In SVG glassmorphism effects, dynamically calling `document.createElement("canvas")` and `canvas.toDataURL()` on every render frame creates significant GC pressure and main thread stalls.
**Action:** Reuse a single shared canvas context and cache generated data URIs in a bounded LRU `Map` keyed by target dimensions and parameters (`width:height:radius:borderWidth`). Bypassing `toDataURL()` execution for cached dimensions yields immediate FPS and latency gains.
