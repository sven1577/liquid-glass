# Bolt's Journal - Critical Performance Learnings

## 2025-01-24 - SVG Displacement Map Performance and DOM Reflow Avoidance
**Learning:** High-frequency event handling combined with SVG filters can cripple frame rates. The main bottlenecks identified were:
1. *GC Pressure from Dynamic Allocation:* Instantiating HTML5 canvas elements repeatedly within a resizing or dragging loop causes frequent and noticeable Garbage Collection pauses.
2. *Blocking `toDataURL()` Overhead:* Serializing a canvas into a base64 Data URL via `toDataURL()` is a CPU-bound, synchronous operation. When elements are resized or redrawn repeatedly with matching dimensions, re-generating these data URLs blocks the main thread.
3. *Layout Thrashing and DOM Write Overhead:* Repeatedly querying `offsetWidth`, `offsetHeight`, and computed styles (`getComputedStyle`), followed immediately by updating attributes on SVG filter elements, forces the browser to synchronously recalculate layouts (reflow).

**Action:**
1. Recycle canvas instances using a single file-scoped or static reference to avoid continuous heap allocations.
2. Build a Map-based bounded LRU cache (such as 100 entries) to memoize dynamic data URLs, so the same container sizes can bypass the expensive serialization entirely.
3. Cache local layout dimensions (`lastW`/`lastH`) on the instance level and implement early-returns to bypass DOM queries and SVG attribute writes whenever dimensions remain unchanged.
