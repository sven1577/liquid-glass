## 2025-02-15 - Canvas Reuse and Cache Optimization
**Learning:** Initializing canvas elements repeatedly triggers major garbage collection overhead. Invoking `toDataURL` repeatedly is CPU intensive and slow. By introducing a shared module-level canvas and an LRU cache for already rendered dataURLs, garbage collection pressure is significantly reduced and rendering performance is greatly improved.
**Action:** When working on dynamic image generation or displacement maps, reuse a single DOM/canvas resource and cache generated data URLs using a simple Map-based LRU.
