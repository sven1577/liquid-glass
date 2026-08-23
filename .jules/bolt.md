# Bolt's Performance Journal

## 2025-05-18 - Canvas Reuse and Displacement Map LRU Caching in SVG Filters
**Learning:** Generating SVG displacement map Data URIs on the fly (`canvas.toDataURL()`) alongside dynamic `document.createElement('canvas')` instances causes CPU spikes and high GC pressure during dynamic UI resize/refresh events.
**Action:** Share a single module-scoped canvas/context, cache Data URIs in a bounded LRU cache (keyed by filter parameters), and cache last-applied map keys on glass instances to bypass redundant SVG DOM attribute updates.
