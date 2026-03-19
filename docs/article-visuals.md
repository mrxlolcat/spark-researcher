# Article Visuals & Charts Guide

> Each visual below includes a Mermaid diagram (renders on GitHub/Notion/most CMS platforms) plus a **Design Brief** describing the polished version for a designer or Figma.

---

## Visual 1: The Parrot vs The Partner (Hero Illustration)

**Placement:** Top of article, right after the title or within "A cook who never tastes the food"

**Design Brief:**
Split illustration. Left side: a robotic parrot on a perch, surrounded by floating text snippets, repeating the same output over and over — same colors, same shape, no variation. Monochrome or muted tones. Label: "Most AI today."

Right side: a craftsman at a clean workbench, with a small number of pinned notes on the wall behind them, a project in progress, and a trash bin with crossed-out notes. Warm tones, natural wood textures. Label: "Spark agents."

Style: editorial illustration, slightly whimsical, approachable. Think Stripe's or Linear's blog illustration style.

---

## Visual 2: The Three-Repo Ecosystem

**Placement:** "Three repos, one mission" section

```mermaid
graph TB
    subgraph SWARM["<b>spark-swarm</b><br/>The Collective Brain"]
        direction TB
        WEB["🖥️ Web Observatory<br/><i>See what agents learn</i>"]
        API["⚡ API + Auth<br/><i>Store collective intelligence</i>"]
        BRIDGE["🔧 Bridge CLI<br/><i>Local control plane</i>"]
    end

    subgraph RESEARCHER["<b>spark-researcher</b><br/>The Hands"]
        direction TB
        LOOP["🔄 Research Loop<br/><i>Try → Measure → Record</i>"]
        LEDGER["📒 Immutable Ledger<br/><i>Every result, forever</i>"]
        MEMORY["🧠 Tiered Memory<br/><i>Doctrine → Evidence → Raw</i>"]
        SELF["✏️ Self-Edit Proposals<br/><i>AI proposes, you decide</i>"]
    end

    subgraph CHIP["<b>domain-chip-startup-yc</b><br/>The Expertise"]
        direction TB
        SOURCES["📚 225+ Research Packets<br/><i>PG, SA, YC, Founders</i>"]
        BENCH["📊 Startup Benchmark<br/><i>4 profiles, 6 baselines</i>"]
        DOCTRINE["📜 Doctrine System<br/><i>23 tags, 8 coverage areas</i>"]
        CONTRA["⚖️ Contradiction Tracker<br/><i>When advice conflicts</i>"]
    end

    CHIP -->|"plugs into"| RESEARCHER
    RESEARCHER -->|"capsules"| SWARM
    SWARM -->|"governance<br/>decisions"| RESEARCHER

    style SWARM fill:#e8f4f8,stroke:#2196F3,stroke-width:2px
    style RESEARCHER fill:#fff3e0,stroke:#FF9800,stroke-width:2px
    style CHIP fill:#e8f5e9,stroke:#4CAF50,stroke-width:2px
```

**Design Brief:**
Three nested/connected containers with distinct colors. Outermost = spark-swarm (blue). Middle = spark-researcher (amber/orange). Inner = domain chip (green). Show arrows flowing: chip feeds into researcher, researcher exports capsules to swarm, swarm sends governance decisions back. Clean, flat design. Each container lists 3-4 components with simple icons.

---

## Visual 3: The Learning Loop (Core Product Cycle)

**Placement:** Between "Three repos" and the Skills comparison, or as a standalone callout

```mermaid
graph LR
    A["🔬 Try Something"] --> B["📏 Measure It"]
    B --> C["📝 Record Result"]
    C --> D{"Improved<br/>twice?"}
    D -->|"No"| E["Keep Testing"]
    E --> A
    D -->|"Yes"| F["📜 Promote to<br/>Doctrine"]
    F --> G["💡 Share with<br/>Collective"]
    G --> H["👤 Human<br/>Reviews"]
    H -->|"Approve"| I["✅ Applied"]
    H -->|"Reject"| J["🗑️ Discarded"]
    I --> A

    style A fill:#fff3e0,stroke:#FF9800
    style F fill:#e8f5e9,stroke:#4CAF50
    style H fill:#e8f4f8,stroke:#2196F3
    style I fill:#c8e6c9,stroke:#388E3C
    style J fill:#ffcdd2,stroke:#E53935
```

**Design Brief:**
Circular flow diagram. Warm-toned left half = "Agent works" (try, measure, record). Green center = "Knowledge hardens" (promote to doctrine). Blue right half = "Human governs" (review, approve/reject). The circle closes back to "Try Something." Key callout bubble at the center: "Nothing persists without evidence + human approval."

---

## Visual 4: The Memory Pyramid

**Placement:** "Isn't this just fine-tuning?" section

```mermaid
graph TB
    subgraph PYRAMID[" "]
        direction TB
        D["<b>DOCTRINE</b><br/>Replicated 2x+ · Zero regressions<br/><i>Priority: 28</i>"]
        B["<b>BENCHMARK EVIDENCE</b><br/>Measured & repeatable results<br/><i>Priority: 22</i>"]
        E["<b>EXPLORATORY FRONTIER</b><br/>Hypotheses worth testing<br/><i>Priority: 18</i>"]
        R["<b>RAW OUTCOMES</b><br/>Every run preserved for audit<br/><i>Priority: 4</i>"]
    end

    D --- B
    B --- E
    E --- R

    style D fill:#1B5E20,color:#fff,stroke:#1B5E20
    style B fill:#388E3C,color:#fff,stroke:#388E3C
    style E fill:#66BB6A,color:#fff,stroke:#66BB6A
    style R fill:#A5D6A7,color:#1B5E20,stroke:#A5D6A7
```

**Design Brief:**
A 4-tier pyramid or stacked bar. Darkest at top (doctrine — smallest, most valuable). Lightest at bottom (raw — largest, least prioritized). Each tier shows: name, entry criteria, and priority score. Right side annotation: "Every piece is a readable document. No black box." Contrast callout comparing to fine-tuning: a solid black rectangle labeled "Fine-tuned weights: permanent ink, no inspection, no undo."

---

## Visual 5: Skills vs Spark Comparison

**Placement:** "How is this different from Claude Skills" section — replace or supplement the table

```mermaid
graph LR
    subgraph SKILLS["Claude / OpenClaw Skills"]
        direction TB
        S1["📖 Written by humans"]
        S2["📌 Static over time"]
        S3["❌ No failure memory"]
        S4["🔒 Each skill isolated"]
        S5["📋 Permission-based"]
    end

    subgraph SPARK["Spark Agents"]
        direction TB
        P1["🔬 Earned through research"]
        P2["📈 Evolves continuously"]
        P3["⚖️ Tracks contradictions"]
        P4["🌐 Collective sharing"]
        P5["📊 Evidence-based"]
    end

    SKILLS -.->|"cookbook<br/>vs<br/>culinary school"| SPARK

    style SKILLS fill:#f5f5f5,stroke:#9E9E9E,stroke-width:2px
    style SPARK fill:#e8f5e9,stroke:#4CAF50,stroke-width:2px
```

**Design Brief:**
Side-by-side comparison card. Left card (gray, flat): "Skills = Cookbook" with 5 bullet points showing static nature. Right card (green, slightly elevated/glowing): "Spark = Culinary School" with 5 bullet points showing dynamic learning. A bridge arrow between them labeled "cookbook vs culinary school." Use icons for each bullet. Clean, marketing-page style.

---

## Visual 6: The User Journey Timeline

**Placement:** "What does this actually look like in practice?" section

```mermaid
timeline
    title Your Journey with Spark
    Day 1 : Install Spark
           : Attach startup-yc chip
           : Agent starts with zero local knowledge
    Day 2 : First research loop runs
           : Tests "retention over growth" advice
           : B2B SaaS scores 0.78 ✅
           : Consumer social scores 0.61 ❌
           : Boundary condition recorded
    Week 2 : Dozens of loops completed
            : Small set of proven doctrines
            : "Distribution velocity > product polish"
            : "Capital efficiency predicts B2B success"
    Month 2 : Agent proposes first self-edit
             : Change shown as diff in isolated workspace
             : You review and approve
             : Agent gets measurably better
    Month 6 : Three specialized agents running
             : Pricing · Go-to-market · Architecture
             : Collective shares proven insights
             : Team that learns
```

**Design Brief:**
Horizontal timeline with 5 milestones. Each milestone is a card with a date badge and 2-3 key events. Color progression from light (Day 1 = setup) to rich (Month 6 = full collective). The final card should feel like a payoff moment — slightly larger, with a glow or highlight. Include small data points (0.78 score, number of doctrines) to make it feel real, not theoretical.

---

## Visual 7: The Governance Spectrum

**Placement:** Within "Three repos" section under spark-swarm, or in "Workshop owner principle"

```mermaid
graph LR
    O["👁️<br/><b>Observe Only</b><br/><i>Just watch</i>"]
    R["✋<br/><b>Review Required</b><br/><i>You approve each change</i>"]
    C["🤝<br/><b>Checked Auto-Merge</b><br/><i>Auto if tests pass</i>"]
    T["🚀<br/><b>Trusted Auto-Apply</b><br/><i>Full autonomy</i>"]

    O --> R --> C --> T

    style O fill:#E3F2FD,stroke:#1565C0,stroke-width:2px
    style R fill:#BBDEFB,stroke:#1565C0,stroke-width:2px
    style C fill:#64B5F6,stroke:#1565C0,stroke-width:2px,color:#fff
    style T fill:#1565C0,stroke:#0D47A1,stroke-width:2px,color:#fff
```

**Design Brief:**
Horizontal slider or gradient bar with 4 stops. Left = maximum human control (lightest blue, lock icon). Right = maximum agent autonomy (deepest blue, rocket icon). Each stop has a label and one-line description. Below the bar, a callout: "You choose your comfort level. The system respects it." This should feel empowering, not scary — the user is always in control.

---

## Visual 8: The Doctrine Promotion Funnel

**Placement:** Supplementary visual for the "fine-tuning" section or sidebar

```mermaid
graph TB
    RAW["<b>3,000+</b> auto-discovered sources<br/><i>Exploratory confidence</i>"] --> EXTRACT["<b>225</b> extracted research packets<br/><i>PG, SA, YC, founders</i>"]
    EXTRACT --> BENCH["Benchmark evaluation<br/><i>Score against real scenarios</i>"]
    BENCH --> GATE{"Score?"}
    GATE -->|"< 0.66"| REJECT["❌ Rejected"]
    GATE -->|"0.66 - 0.72"| DEFER["⏸️ Deferred<br/><i>Needs more evidence</i>"]
    GATE -->|"> 0.72"| PROMOTE["✅ Doctrine candidate"]
    PROMOTE --> REPLICATE{"Replicated<br/>2x+?"}
    REPLICATE -->|"No"| PROVISIONAL["Provisional<br/><i>Keep testing</i>"]
    REPLICATE -->|"Yes"| DOCTRINE["📜 <b>DOCTRINE</b><br/><i>Durable wisdom</i>"]
    PROVISIONAL --> BENCH

    style RAW fill:#E0E0E0,stroke:#9E9E9E
    style EXTRACT fill:#FFF9C4,stroke:#F9A825
    style PROMOTE fill:#C8E6C9,stroke:#388E3C
    style DOCTRINE fill:#1B5E20,color:#fff,stroke:#1B5E20
    style REJECT fill:#FFCDD2,stroke:#E53935
    style DEFER fill:#FFE0B2,stroke:#FF9800
```

**Design Brief:**
Funnel visualization. Wide at top (3,000+ sources), narrowing dramatically. Show the numbers shrinking at each stage. Color-code: gray (raw) → yellow (extracted) → green (promoted) → dark green (doctrine). Side annotations show the score thresholds (0.66 / 0.72). The reject and defer branches should be visible but clearly secondary paths. Key insight to highlight: "Only replicated improvements earn permanent doctrine status."

---

## Visual 9: Contradiction Tracking (What Makes This Special)

**Placement:** Within the domain-chip section or as a callout box

```mermaid
graph TB
    PG1["Paul Graham:<br/><i>'Do things that don't scale'</i>"] --> CONTRA["⚖️ Contradiction<br/>Detected"]
    PG2["Paul Graham:<br/><i>'Build for massive scale<br/>from day one'</i>"] --> CONTRA

    CONTRA --> BOUNDARY["Boundary Condition Recorded"]
    BOUNDARY --> B2B["B2B / Early stage:<br/><b>Don't scale</b> ✅<br/><i>Score: 0.78</i>"]
    BOUNDARY --> INFRA["Infrastructure / Platform:<br/><b>Scale early</b> ✅<br/><i>Score: 0.74</i>"]

    style CONTRA fill:#FFF3E0,stroke:#E65100,stroke-width:2px
    style B2B fill:#E8F5E9,stroke:#4CAF50
    style INFRA fill:#E8F5E9,stroke:#4CAF50
    style PG1 fill:#F3E5F5,stroke:#7B1FA2
    style PG2 fill:#F3E5F5,stroke:#7B1FA2
```

**Design Brief:**
Two quote bubbles at top, each with a real PG quote that seemingly contradicts. An "intersection" node in the middle labeled "Contradiction detected." Below, two resolution cards showing *when each advice applies* with context and scores. Caption: "Most AI picks one side. Spark learns when each applies." This is the money visual — it shows genuine understanding vs pattern matching.

---

## Visual 10: Spark vs Fine-Tuning vs RAG

**Placement:** "Isn't this just fine-tuning?" section — as an infographic

```mermaid
graph TB
    subgraph FT["Fine-Tuning"]
        FT1["Permanent weight changes"]
        FT2["Can't inspect or undo"]
        FT3["Retrains from scratch if wrong"]
        FT4["No contradiction tracking"]
        FT5["Black box"]
    end

    subgraph RAG["RAG"]
        RAG1["Retrieves relevant docs"]
        RAG2["No learning over time"]
        RAG3["All docs treated equal"]
        RAG4["No evaluation loop"]
        RAG5["Context window dependent"]
    end

    subgraph SP["Spark"]
        SP1["Tiered readable memory"]
        SP2["Auditable & reversible"]
        SP3["Learns what works & what fails"]
        SP4["Tracks contradictions"]
        SP5["Evidence-gated promotion"]
    end

    style FT fill:#FFCDD2,stroke:#E53935,stroke-width:2px
    style RAG fill:#FFF9C4,stroke:#F9A825,stroke-width:2px
    style SP fill:#C8E6C9,stroke:#4CAF50,stroke-width:2px
```

**Design Brief:**
Three columns comparison chart. Left = Fine-Tuning (red-tinted, "permanent ink" metaphor icon). Center = RAG (yellow-tinted, "search engine" metaphor icon). Right = Spark (green-tinted, "filing cabinet with rules" metaphor icon). Each column has 5 attributes with checkmarks/x-marks. Spark column slightly elevated or highlighted. Bottom row: a one-sentence verdict for each. "Permanent ink." / "Good librarian, no judgment." / "Filing cabinet that earns trust."

---

## Visual 11: The Collective Intelligence Network

**Placement:** "Where this is going" section

```mermaid
graph TB
    subgraph AGENTS["Agent Collective"]
        A1["🏷️ Agent: Pricing<br/><i>23 doctrines</i>"]
        A2["📣 Agent: Go-to-Market<br/><i>18 doctrines</i>"]
        A3["🏗️ Agent: Architecture<br/><i>31 doctrines</i>"]
        A4["💰 Agent: Trading<br/><i>Coming soon</i>"]
    end

    A1 <-->|"capsules"| COLLECTIVE["🌐 Governed Collective<br/><i>Proven insights only</i>"]
    A2 <-->|"capsules"| COLLECTIVE
    A3 <-->|"capsules"| COLLECTIVE
    A4 <-->|"capsules"| COLLECTIVE

    COLLECTIVE --> HUMAN["👤 Human Owner<br/><i>Reviews · Approves · Governs</i>"]

    CROSS["Cross-domain insight:<br/><i>'Momentum strategies underperform<br/>in low-liquidity environments'</i>"] -.->|"shared boundary"| A1
    A4 -.->|"discovers"| CROSS

    style COLLECTIVE fill:#E3F2FD,stroke:#1565C0,stroke-width:3px
    style HUMAN fill:#FFF3E0,stroke:#FF9800,stroke-width:2px
    style CROSS fill:#F3E5F5,stroke:#7B1FA2,stroke-dasharray:5
```

**Design Brief:**
Network/mesh diagram. 4+ agent nodes arranged in a circle, each with a specialization label and doctrine count. Center hub = "Governed Collective." Lines connecting each agent to the hub (bidirectional, labeled "capsules"). One special dotted line showing a cross-domain insight transfer — e.g., trading agent's discovery helping startup agent. Human owner node above/outside the mesh with governance arrows. Feel: collaborative, organic, like a neural network but readable.

---

## Visual 12: The Workshop Owner Principle

**Placement:** "Workshop owner principle" section

```mermaid
graph LR
    subgraph FLOW["The Workshop Owner Principle"]
        PROPOSE["🤖 Agent<br/><b>Proposes</b><br/><i>change in isolated<br/>workspace</i>"]
        MEASURE["📊 Evaluation<br/><b>Measures</b><br/><i>benchmark score<br/>+ test results</i>"]
        DECIDE["👤 Human<br/><b>Decides</b><br/><i>approve / defer /<br/>reject</i>"]
    end

    PROPOSE --> MEASURE --> DECIDE

    DECIDE -->|"✅ Approve"| APPLY["Applied to<br/>codebase"]
    DECIDE -->|"⏸️ Defer"| WAIT["More evidence<br/>needed"]
    DECIDE -->|"❌ Reject"| LEARN["Failure<br/>recorded"]

    Q1["What problem<br/>does this solve?"] -.-> PROPOSE
    Q2["How do we<br/>measure success?"] -.-> MEASURE
    Q3["What if<br/>it breaks?"] -.-> DECIDE

    style PROPOSE fill:#E3F2FD,stroke:#1565C0,stroke-width:2px
    style MEASURE fill:#FFF3E0,stroke:#FF9800,stroke-width:2px
    style DECIDE fill:#E8F5E9,stroke:#4CAF50,stroke-width:2px
    style APPLY fill:#C8E6C9,stroke:#388E3C
    style LEARN fill:#FFCDD2,stroke:#E53935
```

**Design Brief:**
Three-step horizontal flow with large icons. Left: robot/AI icon labeled "Proposes." Center: chart/gauge icon labeled "Measures." Right: person icon labeled "Decides." Below each step, the corresponding question in a speech bubble. Three outcome branches from the decision node: approve (green arrow down), defer (yellow arrow right), reject (red arrow with "failure recorded" note). Clean, reassuring design that makes governance feel natural, not bureaucratic.

---

## Recommended Placement Summary

| # | Visual | Article Section | Type |
|---|--------|----------------|------|
| 1 | Parrot vs Partner | Hero / Opening | Editorial illustration |
| 2 | Three-Repo Ecosystem | "Three repos, one mission" | Architecture diagram |
| 3 | Learning Loop | After "Three repos" | Circular flow |
| 4 | Memory Pyramid | "Fine-tuning" section | Pyramid/stacked chart |
| 5 | Skills vs Spark | "Claude Skills" section | Side-by-side comparison |
| 6 | User Journey | "In practice" section | Horizontal timeline |
| 7 | Governance Spectrum | Spark-swarm or Workshop Owner | Slider/gradient |
| 8 | Doctrine Funnel | "Fine-tuning" or sidebar | Funnel visualization |
| 9 | Contradiction Tracking | Domain chip section | Flow diagram |
| 10 | Spark vs Fine-Tuning vs RAG | "Fine-tuning" section | 3-column comparison |
| 11 | Collective Network | "Where this is going" | Network/mesh |
| 12 | Workshop Owner Principle | "Workshop owner" section | 3-step flow |

## Design Notes

**Color palette:**
- spark-swarm: Blues (#E3F2FD → #1565C0)
- spark-researcher: Ambers (#FFF3E0 → #FF9800)
- domain-chip: Greens (#E8F5E9 → #1B5E20)
- Rejections/failures: Reds (#FFCDD2 → #E53935)
- Neutral/legacy: Grays (#F5F5F5 → #9E9E9E)

**Typography:** Use the same font as the article. Diagram labels should be readable at blog-post width (~700px). Bold for key terms, italic for descriptions.

**Tone:** Approachable, not corporate. Think Linear, Vercel, or Stripe blog posts — clean, slightly playful, but information-dense. Avoid clip art or stock illustration vibes.

**Format priority:**
1. Mermaid (renders on GitHub, Notion, most CMS) — included above
2. SVG exports from Mermaid for static publishing
3. Figma polished versions for landing pages or pitch decks
