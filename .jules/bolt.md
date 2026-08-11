# Bolt's Journal - Performance Learnings

## 2026-08-11 - GC Pressure and Data URL Overhead in SVG-Filtered Backdrops
**Learning:** In a dynamic DOM where glassmorphic card containers are resized or dragged, repeatedly creating canvas elements causes high garbage collection pressure. Additionally, calling `canvas.toDataURL()` synchronously on every resize is extremely CPU-heavy because it compresses the full image to a PNG data URL on the main thread.
**Action:** Re-use a single module-level `sharedCanvas` instead of instantiating new canvas objects. Implement an LRU-style cache for the generated data URLs based on the canvas dimensions and drawing options to eliminate redundant, expensive `toDataURL` calls.
