# Palette's Journal

## 2025-05-18 - Keyboard Navigation for Physics-Driven Containers
**Learning:** Interactive floating/draggable components driven by physics loops (e.g. spring animation targets `tx`/`ty`) can be made fully keyboard accessible by mapping Arrow keys to position increments on the target coordinates. Additionally, checking `e.target !== containerElement` prevents child inputs/buttons inside the container from capturing or triggering container movements.
**Action:** Always check target identity on container keyboard listeners and update physics target coordinates when adding arrow key support to draggable UI elements.
