# Bolt's Journal - Critical Learnings

## 2025-05-18 - Canvas Reuse and Map LRU Caching in SVG Filters
**Learning:** In liquid-glass.js, generating SVG displacement maps dynamically creates high GC pressure from canvas allocations and high CPU cost from `canvas.toDataURL()`. Reusing a shared offscreen canvas/context and caching base64 map Data URLs in a bounded LRU Map drastically improves performance during resize and component initialization.
**Action:** Always reuse offscreen 2D canvas contexts and cache serialized canvas Data URLs when generating dynamic SVG filter maps.
