## 2025-05-18 - Glassmorphic Layout Reflow on Dynamic DOM Content Insertion
**Learning:** In SVG glassmorphism interfaces, inline UI updates (like form success messages) that dynamically expand card container height require re-measuring bounds (`measure()`, `clampTarget()`, `refresh()`) to prevent displacement map misalignment and visual background clipping.
**Action:** Always trigger instance re-measurement (`measure()`, `clampTarget()`, `refresh()`) immediately following any DOM dynamic content insertion inside glassmorphic cards.
