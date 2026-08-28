# Bolt's Journal - Critical Performance Learnings

## 2025-05-18 - Shared Canvas & Bounded Map Cache for SVG Displacement Maps
**Learning:** Generating SVG displacement maps in `liquid-glass.js` via transient HTMLCanvasElement allocation and `canvas.toDataURL()` creates high GC pressure and CPU usage during UI refreshes or resize events.
**Action:** Reuse a single shared canvas context (`sharedCanvas`/`sharedCtx`) and store generated Data URLs in a bounded LRU Map (`mapCache`, max 20 entries) keyed by parameters (`w_h_radius_border_mapBlur`). Cache element dimensions (`lastW`, `lastH`, `lastRadius`) on instance to skip redundant `refresh()` calls when layout is unchanged.
