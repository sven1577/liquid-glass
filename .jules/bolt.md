# Bolt's Journal - Critical Learnings

This journal contains critical learnings to avoid mistakes or make better decisions.

## 2023-11-20 - High-Frequency Canvas Displacement Map Generation Bottlenecks
**Learning:** Re-generating SVG displacement maps dynamically on layout/interaction changes causes major CPU/memory bottlenecks on the main thread. Specifically, canvas recreation creates garbage collection pressure, `.toDataURL()` is highly CPU-intensive, and reading computed styles (such as `border-radius`) or offset dimensions inside the refresh loop triggers forced synchronous layouts (layout thrashing).
**Action:** Share a module-level canvas and 2D context to avoid GC churn; cache generated displacement map data URLs in a bounded LRU cache using key parameters as the hash; query layout properties (like `getComputedStyle`) exactly once during initialization; and keep track of previous element dimensions to immediately bail out of refreshes if no resizing has occurred.
