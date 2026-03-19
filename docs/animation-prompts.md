# Animation Prompts for Claude

> Copy-paste each prompt below into Claude. Each will generate a self-contained HTML file you can open in a browser and screen-record.

---

## Animation 1: The Learning Loop (Hero Animation)

```
Create a single self-contained HTML file with a beautiful animated learning loop diagram.

The animation should show a circular flow with 6 nodes arranged in a circle:

1. "Try Something" (amber/orange)
2. "Measure It" (amber/orange)
3. "Record Result" (amber/orange)
4. "Promote to Doctrine" (green)
5. "Share with Collective" (blue)
6. "Human Reviews" (blue)

Animation behavior:
- A glowing particle (small circle, white with a soft glow) travels along the path between nodes, continuously looping
- As the particle reaches each node, that node briefly pulses/scales up (1.0 → 1.15 → 1.0) and its label fades in brighter
- Between nodes 3 and 4, add a brief "gate" animation — a small bar that lifts to let the particle through, representing the benchmark threshold
- After "Human Reviews", show a brief fork: the particle either continues the loop (approve — green flash) or fades out with a red flash (reject) — alternate between these every other loop
- The whole cycle should take about 8 seconds per loop
- Loop infinitely

Design style:
- Dark background (#0F172A or similar dark navy)
- Nodes are rounded rectangles with subtle shadows
- Connections are curved lines with a slight glow
- Color palette: ambers (#FF9800, #FFA726) for agent work, greens (#4CAF50, #66BB6A) for doctrine, blues (#2196F3, #42A5F5) for governance
- Clean sans-serif font (system-ui or Inter if available)
- Add a subtle title at top: "How Spark Agents Learn" in white, 24px
- Canvas size: 1200x800px (good for screen recording)

No external dependencies. Pure HTML + CSS + JS. Use canvas or SVG animations.
```

---

## Animation 2: The Doctrine Funnel Counter

```
Create a single self-contained HTML file with an animated funnel counter visualization.

The animation shows knowledge being filtered through Spark's pipeline, with animated counters ticking down at each stage:

Stage 1 (top, widest): "Auto-Discovered Sources" → counter ticks from 0 up to 3,000+
Stage 2: "Extracted Research Packets" → counter ticks up to 225
Stage 3: "Benchmark Tested" → counter ticks up to 142
Stage 4: "Doctrine Candidates" → counter ticks up to 47
Stage 5 (bottom, narrowest): "Proven Doctrines" → counter ticks up to 23

Animation behavior:
- The funnel is drawn as a trapezoid shape, widest at top, narrowest at bottom
- Each stage has a horizontal divider line
- Numbers count up with an easing function (fast start, slow finish) — like a slot machine settling
- Start from top, each stage begins counting 0.8 seconds after the previous one starts
- Small particles (dots) flow downward through the funnel, some getting filtered out (fade and drift sideways) at each stage
- Filtered-out particles turn red briefly before fading
- Surviving particles turn progressively greener as they descend
- After all counters finish, hold for 2 seconds, then reset and loop

Design style:
- Dark background (#0F172A)
- Funnel outline in subtle gray (#334155)
- Stage colors gradient from gray (top) → yellow → light green → dark green (bottom)
- Numbers are large (48px), bold, white, with a slight glow matching their stage color
- Stage labels are smaller (16px), muted white (#94A3B8)
- Add title: "From Raw Data to Proven Doctrine" at top
- Add subtitle: "Only replicated insights earn permanent status" at bottom
- Canvas size: 800x1000px (vertical orientation)

No external dependencies. Pure HTML + CSS + JS.
```

---

## Animation 3: The Score Bar Race

```
Create a single self-contained HTML file with an animated horizontal bar chart race showing startup strategies competing across research rounds.

Data (strategies and their scores evolving over 8 rounds):

Round 1: "Retention over growth" 0.45, "Distribution velocity" 0.42, "Capital efficiency" 0.40, "Product polish first" 0.43, "Hire fast" 0.38, "Bootstrap always" 0.41
Round 2: "Retention over growth" 0.52, "Distribution velocity" 0.55, "Capital efficiency" 0.48, "Product polish first" 0.44, "Hire fast" 0.40, "Bootstrap always" 0.50
Round 3: "Retention over growth" 0.61, "Distribution velocity" 0.63, "Capital efficiency" 0.58, "Product polish first" 0.45, "Hire fast" 0.39, "Bootstrap always" 0.56
Round 4: "Retention over growth" 0.68, "Distribution velocity" 0.70, "Capital efficiency" 0.65, "Product polish first" 0.46, "Hire fast" 0.37, "Bootstrap always" 0.60
Round 5: "Retention over growth" 0.72, "Distribution velocity" 0.74, "Capital efficiency" 0.71, "Product polish first" 0.47, "Hire fast" 0.35, "Bootstrap always" 0.62
Round 6: "Retention over growth" 0.75, "Distribution velocity" 0.76, "Capital efficiency" 0.74, "Product polish first" 0.48, "Hire fast" 0.33, "Bootstrap always" 0.63
Round 7: "Retention over growth" 0.77, "Distribution velocity" 0.78, "Capital efficiency" 0.76, "Product polish first" 0.47, "Hire fast" 0.31, "Bootstrap always" 0.64
Round 8: "Retention over growth" 0.78, "Distribution velocity" 0.79, "Capital efficiency" 0.77, "Product polish first" 0.46, "Hire fast" 0.29, "Bootstrap always" 0.63

Animation behavior:
- Bars start at Round 1 positions, all roughly even
- Every 2 seconds, transition smoothly to the next round
- Bars re-sort by score (highest on top) with smooth vertical repositioning
- The round number displays prominently: "Research Round 3 of 8"
- When a strategy crosses the 0.72 threshold, its bar turns green and gets a subtle glow + a small "DOCTRINE" badge appears
- When a strategy drops below 0.40, its bar turns red and gets a "REJECTED" badge
- Bars that are between 0.66-0.72 are yellow (provisional)
- Score numbers display at the end of each bar and update in real time
- After Round 8, hold for 3 seconds showing final rankings, then loop

Design style:
- Dark background (#0F172A)
- Bars have rounded ends, height ~40px each with 12px gaps
- Default bar color: #64748B (slate)
- Doctrine bars: #4CAF50 (green) with glow
- Rejected bars: #EF5350 (red), slightly transparent
- Provisional bars: #FFA726 (amber)
- Two vertical threshold lines: dashed line at 0.66 (labeled "minimum") and 0.72 (labeled "doctrine threshold")
- Title: "Startup Strategy Benchmark Race"
- Subtitle updates: "Round X of 8 — Agent learning in progress..."
- Canvas size: 1200x700px

No external dependencies. Pure HTML + CSS + JS. Use requestAnimationFrame for smooth transitions.
```

---

## Animation 4: The Self-Edit Diff (GitHub-Style)

```
Create a single self-contained HTML file with an animated GitHub-style diff viewer showing an AI agent proposing a self-edit, then a human approving it.

The animation has 3 phases:

PHASE 1 — "Agent Proposes" (3 seconds):
Show a code-diff style view with this content appearing line by line (typewriter effect):

File: agent_prompts/startup_advisor.md

- When evaluating B2B SaaS startups, prioritize
- growth metrics above all other signals.
+ When evaluating B2B SaaS startups, prioritize
+ retention metrics (NRR, churn rate) over pure
+ growth. Evidence: 12 benchmark trials show
+ retention-first advice scores 0.78 vs 0.61
+ for growth-first in B2B contexts.

Red lines (deletions) appear first, then green lines (additions) type in.

PHASE 2 — "Evaluation Measures" (2 seconds):
Below the diff, a benchmark results panel slides in:
- "Benchmark score: 0.61 → 0.78 (+28%)" with an animated progress bar
- "Regression check: 0/14 scenarios regressed ✓"
- "Replication: 2/2 independent trials confirmed ✓"
All three lines get green checkmarks that animate in sequence.

PHASE 3 — "Human Decides" (3 seconds):
An approval UI slides in below:
- Two buttons: "Approve" (green) and "Reject" (red)
- A cursor moves toward "Approve" and clicks it
- On click: the whole diff gets a green border, a "MERGED" badge appears with a satisfying animation (scale up + fade), and confetti particles burst briefly
- Hold the final state for 2 seconds, then fade to black and loop

Design style:
- Dark background (#0F172A) with the diff area in slightly lighter (#1E293B)
- Diff styling: exactly like GitHub dark mode — line numbers on left, red/green backgrounds for changes
- Font: monospace (Consolas, Monaco, or system monospace)
- Phase labels appear at top left: "1. Agent Proposes" → "2. Evaluation Measures" → "3. Human Decides" — each fading in as its phase starts
- Subtle header: "Self-Edit Proposal #47 — Startup Advisory Prompts"
- Canvas size: 1000x800px

No external dependencies. Pure HTML + CSS + JS.
```

---

## Animation 5: The Memory Tier Elevator

```
Create a single self-contained HTML file with an animated "elevator" visualization showing an insight rising through Spark's 4 memory tiers.

Layout:
A vertical structure with 4 floors, like a building cross-section:
- Floor 4 (top): "DOCTRINE" — dark green (#1B5E20), with a gold crown/star icon
- Floor 3: "BENCHMARK EVIDENCE" — medium green (#388E3C), with a chart icon
- Floor 2: "EXPLORATORY FRONTIER" — light green (#66BB6A), with a lightbulb icon
- Floor 1 (bottom): "RAW OUTCOMES" — gray (#9E9E9E), with a file icon

Each floor has a "gate" — a horizontal barrier that opens when criteria are met.

Animation sequence (one full journey, ~15 seconds):

1. A glowing capsule (rounded rectangle) appears at the bottom with the text: "Retention > Growth for B2B" — it enters Floor 1 (Raw Outcomes)
   - Label appears: "Result recorded: score 0.78"
   - Gate to Floor 2 check: "Novel hypothesis? ✓" — gate opens, capsule rises

2. Capsule arrives at Floor 2 (Exploratory Frontier)
   - Label: "Testing hypothesis..."
   - A small loading spinner, then: "Benchmark score: 0.78 ✓"
   - Gate to Floor 3 check: "Score > 0.66? ✓" — gate opens, capsule rises

3. Capsule arrives at Floor 3 (Benchmark Evidence)
   - Label: "Seeking replication..."
   - Counter: "Trial 1/2 confirmed ✓" ... "Trial 2/2 confirmed ✓"
   - Gate to Floor 4 check: "Replicated 2x, zero regressions? ✓" — gate opens with a more dramatic animation

4. Capsule arrives at Floor 4 (Doctrine)
   - The capsule transforms: gets a gold border, slight glow, and a "DOCTRINE" stamp
   - Label: "Promoted to permanent wisdom"
   - Celebration: subtle sparkle particles around the capsule
   - Hold for 3 seconds

5. Reset and loop. On alternate loops, show a capsule that gets REJECTED at Floor 2 (score 0.58, below threshold) — capsule turns red, gate stays closed, capsule fades out with "Insufficient evidence" label.

Design style:
- Dark background (#0F172A)
- Building structure has subtle architectural lines (like a cross-section blueprint)
- Each floor glows softly in its color
- Gates are horizontal lines that split apart (like elevator doors)
- The capsule has a soft white glow that changes color to match each floor as it rises
- Smooth easing on all movements (ease-in-out)
- Title: "How Insights Earn Their Place"
- Right side: a small legend showing all 4 tiers with their criteria
- Canvas size: 900x1000px (vertical)

No external dependencies. Pure HTML + CSS + JS.
```

---

## Animation 6: The Contradiction Resolution

```
Create a single self-contained HTML file with an animated visualization showing how Spark handles contradictory advice.

Animation sequence (~12 seconds):

PHASE 1 — "Two truths collide" (4 seconds):
Two quote cards slide in from opposite sides of the screen and meet in the center:

Left card (purple tint):
"Do things that don't scale."
— Paul Graham

Right card (purple tint):
"Build for massive scale from day one."
— Paul Graham

When they meet in the center, a brief "collision" effect: a flash, a small shockwave ripple, and a warning icon appears between them with the text "Contradiction Detected"

PHASE 2 — "Most AI picks a side" (2 seconds):
Below the collision, a gray box appears:
"Traditional AI: picks one, ignores the other"
Show one card fading to 50% opacity (being ignored). Then this fades away.

PHASE 3 — "Spark finds the boundary" (5 seconds):
The two cards separate slightly, and below each, a context card slides up:

Below "Don't scale":
Context: "B2B / Early-stage / Service businesses"
Score: 0.78 ✓
(green border)

Below "Scale early":
Context: "Infrastructure / Platform / Network effects"
Score: 0.74 ✓
(green border)

A bridge appears connecting the two context cards, labeled: "Boundary condition: stage + business model determines which applies"

A final banner fades in at the bottom:
"Not memorization. Understanding."

Hold for 3 seconds, then fade and loop.

Design style:
- Dark background (#0F172A)
- Quote cards: dark purple/violet background (#2D1B69), white text, slightly rounded
- Attribution text in italic, muted color
- Collision effect: white flash with radial gradient
- Context cards: dark background with green or amber border
- Score numbers are large and prominent
- The bridge/connection line is a dotted arc with a label
- Clean sans-serif font throughout
- Canvas size: 1200x800px

No external dependencies. Pure HTML + CSS + JS. Use CSS animations and transitions primarily, JS for sequencing.
```

---

## Animation 7: The Governance Slider

```
Create a single self-contained HTML file with an animated governance spectrum slider.

Layout:
A large horizontal slider/track spanning the width, with 4 stops:

Stop 1 (far left): "Observe Only" — eye icon — lightest blue (#E3F2FD)
Stop 2: "Review Required" — hand/stop icon — light blue (#BBDEFB)
Stop 3: "Checked Auto-Merge" — handshake icon — medium blue (#64B5F6)
Stop 4 (far right): "Trusted Auto-Apply" — rocket icon — deep blue (#1565C0)

Animation behavior:
- A slider handle (circle, white with shadow) starts at Stop 1
- Every 3 seconds, it smoothly slides to the next stop
- As it arrives at each stop, that stop's section expands to show a description panel:

Stop 1: "Watch what your agents learn. No changes applied. Perfect for getting started."
Stop 2: "Every change needs your approval. You see the diff, the evidence, and the benchmark scores."
Stop 3: "Agents can apply changes automatically — but only if all tests pass and benchmarks hold."
Stop 4: "Full autonomy for agents that have earned trust through consistent, measured results."

- The background color of the entire track subtly shifts to match the current stop's color
- Below the slider, show a visual metaphor for each stop:
  Stop 1: A person watching through a window (simple icon animation)
  Stop 2: A person reviewing a document and stamping it
  Stop 3: A robot working while a green checkmark appears automatically
  Stop 4: A robot with a small trust badge, working independently

- After cycling through all 4, hold on Stop 4 for 2 seconds, then the handle slides back to Stop 1 and loops

- Throughout, display the text: "You choose your comfort level. The system respects it." at the bottom, always visible

Design style:
- Dark background (#0F172A)
- The track is a rounded rectangle, tall enough (~80px) to contain the stop labels
- Active region of the track (left of the handle) fills with the current stop's color
- Description panels slide down from below each stop with a smooth ease
- Icons can be simple emoji or SVG icons
- Title: "Your Level of Control"
- Canvas size: 1200x700px

No external dependencies. Pure HTML + CSS + JS.
```

---

## Recommended Recording Setup

For best results when screen-recording these:

1. **Open each HTML file in Chrome** (best rendering for animations)
2. **Set browser zoom to 100%** and go fullscreen (F11)
3. **Use OBS Studio or QuickTime** to record at 1080p / 60fps
4. **Record 2-3 full loops** of each animation, then trim to the best single loop
5. **Export as:**
   - `.gif` for Twitter/X embeds (use gifski for high quality, keep under 15MB)
   - `.mp4` for higher quality sharing and landing pages
   - `.webm` for web embedding

**For the X thread:** The Score Bar Race (#3) and Contradiction Resolution (#6) will drive the most engagement — lead with those.
