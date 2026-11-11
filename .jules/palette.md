# Palette's Journal - UX & Accessibility Learnings

## 2026-11-11 - Keyboard Navigation for Spring-Physics Draggable Cards
**Learning:** When making physics-based draggable containers accessible via keyboard (Arrow keys), mapping keydown events directly to physics target coordinates (`tx`, `ty`) preserves smooth spring-damper motion rather than jumping discontinuously. However, because containers often host form controls (inputs, buttons), bubbling keydown events will inadvertently move the container while navigating child inputs unless an explicit `e.target !== container` guard is enforced.
**Action:** Always verify `e.target === container` in parent container keyboard handlers, and update target physics coordinates with a step delta (supporting Shift for coarse adjustments) rather than setting absolute positions.
