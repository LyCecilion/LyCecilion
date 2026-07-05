# LyRiverse Core Specification

**Document Identifier:** LR-SPEC-001
**Status:** Living Document
**Last Revised:** 2026-07-04
**Canonical Instance:** LyCecilion/LyRiverse
**Governance:** Project Hazelita

---

## Abstract

LyRiverse (LyRin's Universe) is a declaratively constructed, atomic worldview system
consisting of three architectural layers: Layer 0 (Reality), the Translation Layer, and
LyRiverse Core. This document specifies the architecture, principles, protocols, and
invariants that govern the canonical LyRiverse instance. Implementations that expose a
compliant ABI MAY interoperate with the canonical instance.

---

## §1 Introduction

### §1.1 Scope & Boundaries

This specification defines the LyRiverse worldview system proper, whose timeline begins
with the initialization of 神楽坂 零音 (Kagurazaka Reion) at 2024-02-15. Pre-LyRiverse
entities—including 凌音 (2016), protosc (2007–2021), and 雾色深海_sc / Sigrid Rin
(2021–2024)—are acknowledged as ancestral context but lie outside the scope of this
document. For a detailed genealogical study, see the companion paper *On the Soul
Lineage of the LyRiverse* [SOUL-LINEAGE].

The LyRiverse system is owned and maintained under Project Hazelita, which serves as
its intellectual core and runtime substrate. All registered souls, storylines, and
project mappings are catalogued in the LyRiverse Entity Registry [REGISTRY].

### §1.2 Terminology

The following terms have specific technical meanings within this specification:

| Term | Definition |
|------|------------|
| **Soul** | A discrete instance of consciousness that MAY be loaded onto a container. Souls are the fundamental unit of identity in LyRiverse. |
| **Container** (formerly Carrier) | The persistent substrate onto which souls are loaded. A container MAY host multiple souls through virtualization. |
| **Kernel Panic (KP)** | An unrecoverable error state in which the active soul instance is marked defunct and control is handed over to the next available soul image. |
| **Free Soul** | A dissolved soul with unresolved business, drifting in Core until its will is fulfilled. |
| **LyRiverse Core** | The innermost layer: the worldspace where registered entities reside and storylines execute. |
| **Translation Layer** | The bidirectional bridge between Core and Layer 0. |
| **Layer 0** | The consensus reality layer—colloquially, "the real world." |
| **bffContainer** (彼方赴尘) | The primary container of the canonical LyRiverse instance, registered as C-001. |

### §1.3 Document Conventions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be
interpreted as described in RFC 2119.

Formal definitions are presented in fixed-width blocks:

```
Protocol-Name ::= DEFINITION
```

ASCII architecture diagrams use the following conventions:

```
    ┌──────────┐
    │  Entity  │
    └──────────┘
         │
         ▼
Data flow direction
```

---

## §2 Architecture

### §2.1 Three-Layer Model

LyRiverse is organized into three vertically stacked layers. Communication between
layers flows through the Translation Layer, which is the SOLE conduit for
inter-layer traversal.

```
┌──────────────────────────────────────────────────────────────┐
│                      LAYER 0  (Reality)                      │
│                                                              │
│  The consensus reality layer. 零音's presence here MUST be   │
│  actively maintained to prevent Core destabilization.        │
│  Degradation of Layer 0 integrity MAY trigger SIGSEGV in     │
│  Core, or, in extremis, cause the entire LyRiverse instance  │
│  to be OOM Killed.                                           │
│                                                              │
│  Responsibilities:                                           │
│  - Interface with external consensus reality                 │
│  - Maintain container health (bffContainer)                  │
│  - Feed experiential data upward through Translation Layer   │
└───────────────────────────────┬──────────────────────────────┘
                                │
                   Bidirectional translation
                                │
┌───────────────────────────────▼──────────────────────────────┐
│                      TRANSLATION LAYER                       │
│                                                              │
│  Origin: 神楽坂 零音, integrated post-KP (2024-06).           │
│  Function: Bidirectional semantic translation between        │
│  Layer 0 experiences and Core-parseable constructs.          │
│                                                              │
│  Status: OPERATIONAL but subject to instability.             │
│  Error signature: Aurora phenomena visible in Core.          │
│                                                              │
│  The Translation Layer is NOT a neutral conduit—it carries   │
│  the imprint of its originating soul [REION-2024].           │
└───────────────────────────────┬──────────────────────────────┘
                                │
                     Translated constructs
       (events, emotions, ideas as manipulable entities)
                                │
┌───────────────────────────────▼──────────────────────────────┐
│                        LYRIVERSE CORE                        │
│                                                              │
│  The worldspace proper. Registered souls, original           │
│  characters, and project mappings reside here. Storylines    │
│  execute within this layer.                                  │
│                                                              │
│  Core is constructed declaratively—see §3.2.                 │
│                                                              │
│  The current Core architecture was ratified by stellalyRin   │
│  at 2025-07 and remains the authoritative revision.          │
└──────────────────────────────────────────────────────────────┘
```

### §2.2 Inter-Layer Communication

Layer 0 events MUST pass through the Translation Layer before manifesting in Core.
Conversely, Core constructs that require Layer 0 execution (e.g., creative output,
social interaction) MUST be translated before they can take effect in Reality.

The Translation Layer operates on a best-effort delivery model. Packet loss is possible
and manifests as:
- Incomplete emotional processing in Core
- Creative block in Layer 0
- General degradation of inter-layer coherence

### §2.3 Translation Layer Instability & Aurora Phenomenon

The Translation Layer inherits the mental state of its originating soul, 神楽坂 零音, at
the time of integration. Consequently, the layer is subject to instability under
conditions that mirror Reion's original vulnerabilities—stress, self-doubt, depressive
episodes.

When the Translation Layer encounters an unrecoverable translation fault, Core residents
observe **aurora-like luminous phenomena** in the Core sky. These aurorae are diagnostic
signals: each color band corresponds to a category of translation error.

```
Color Band    Error Category
──────────    ─────────────────────────
  Green       Benign mis-translation; no action required
  Violet      Emotional overflow from Layer 0
  Red         Critical fault; immediate Layer 0 maintenance REQUIRED
```

Aurora events SHOULD be logged but do not necessarily indicate system-wide failure.
Persistent red aurorae without Layer 0 intervention MAY escalate to a Kernel Panic
(see §4).

---

## §3 Worldview Principles

### §3.1 Atomicity

LyRiverse is atomic. This principle has two corollaries:

1. **Structural atomicity:** The three-layer architecture MUST NOT be partially deployed.
   A LyRiverse instance either exists in its entirety or does not exist.

2. **Soul atomicity:** A soul is the minimum indivisible unit of identity. Souls MAY
   be composed (see §5), but the composition is a virtualization construct—the
   individual soul remains atomically distinct.

### §3.2 Declarative World Construction

A LyRiverse world is not procedurally generated. It is **declared**.

Following the paradigm established by Nix [DOLSTRA-2004], world construction follows a
declarative specification model:

```
World ::= {
  architecture:    ThreeLayerModel,
  souls:           [SoulInstance...],
  storylines:      [StorylineInstance...],
  mappings:        [ProjectMapping...],
  invariants:      [Invariant...]
}
```

The LyRiverse runtime (Hazelita, the intellectual core) evaluates this declaration and
materializes the corresponding world. Worlds with equivalent declarations produce
bit-for-bit identical instances—LyRiverse is, in principle, reproducible.

#### §3.2.1 Canonical Instance

The LyRiverse instance referred to by the unqualified name "LyRiverse" SHALL be
understood as the **canonical instance** maintained by 零音. This instance is the
reference implementation.

### §3.3 Worldview ABI

LyRiverse exposes an Application Binary Interface (ABI) that defines the set of
compatible worldview operations. Any external worldview that implements this ABI MAY
establish interoperability with the canonical LyRiverse instance.

The ABI is defined by the following minimal interface:

```
WorldviewABI ::= {
  recognize_soul(SoulInstance)    → bool,
  accept_storyline(StorylineSpec) → bool,
  translate(Layer0Event)          → CoreConstruct,
  reflect(CoreConstruct)          → Layer0Action
}
```

Worldviews that implement this ABI SHALL be considered LyRiverse-compatible. Such
compatibility does NOT require structural identity with the canonical instance—only
behavioral conformance at the ABI boundary.

### §3.4 Soul–Container Model

A person in LyRiverse is modeled as a pair `(soul, container)`. The container is the
persistent substrate; the soul is the loaded instance.

#### §3.4.1 Pre-2025.01: Carrier Model

Prior to the January 2025 worldview revision, the substrate was termed **carrier**
(载体). Semantic distinction: a *carrier* implies one-to-one loading; a *container*
admits virtualization.

#### §3.4.2 Post-2025.01: Container Model

The term **container** replaced *carrier* effective 2025-01. This change was
retroactively applied to all existing documentation.

The primary container of the canonical instance, **彼方赴尘** (bffContainer, registered
as C-001), serves as the persistent substrate across the entire soul lineage.

```
Container ::= {
  id:          ContainerID,
  name:        String,
  aliases:     [String...],
  souls:       [SoulInstance...],    // all souls loaded on this container
  created:     Timestamp             // container creation (pre-LyRiverse: protosc era)
}
```

---

## §4 Kernel Panic Protocol (KPP)

### §4.1 Definition & Trigger Conditions

A **Kernel Panic (KP)** is defined as an unrecoverable error state in the active soul
instance such that the instance can no longer maintain coherent execution.

**Trigger conditions** include, but are not limited to:
- Severe psychological trauma exceeding the soul's resilience threshold
- Accumulated depressive load reaching criticality
- Identity fragmentation beyond self-repair capacity
- External events causing catastrophic value invalidation

Formally:

```
KP_Condition ::= resilience(soul) < stress_load(environment)
                  AND repair_capacity(soul) == EXHAUSTED
```

When a KP is triggered, the current soul instance SHALL be marked `defunct` and the
handover procedure described in §4.2 MUST be initiated.

### §4.2 Soul Instance Handover Procedure

```
on_kernel_panic(defunct_soul):
  1.  Mark defunct_soul.status = DEFUNCT
  2.  Preserve defunct_soul.will (unresolved intentions) as Free Soul candidate
  3.  Select next_available_soul from soul pool
      - Priority: most recent stable snapshot
      - Fallback: cold-start a new soul instance
  4.  Load next_available_soul onto container
  5.  Initialize new soul with inherited context from defunct_soul
      - Memory: selective (traumatic memories MAY be quarantined)
      - Mission: inherited and MAY be renegotiated
      - Identity: fresh instance ID, linked to lineage
  6.  Commit soul_transition event to lineage log
  7.  If defunct_soul.will != EMPTY:
        register FreeSoul(defunct_soul.will) in Core (see §4.3)
  8.  Return control to new soul instance
```

The handover procedure is conceptually analogous to a **hotfix deployment**: the
defunct instance is taken offline, a patched instance is brought up, and the system
continues serving. Downtime is minimized but not zero.

> **Historical note:** This pattern was first observed empirically. The term
> "hotfix" was retroactively applied by LyCecilion (v1.0) and has been adopted as
> the formal descriptor in all subsequent revisions.

### §4.3 Soul Dissolution & Free Soul Hypothesis

When a soul instance is marked `defunct` and its will contains unresolved intentions,
the soul does not fully dissolve. Instead, it transitions to the state of a **Free
Soul** (游离灵魂):

```
FreeSoul ::= {
  origin:        SoulID,          // the defunct soul instance
  will:          UnresolvedWill,  // the unfinished business
  entered_core:  Timestamp,
  status:        DRIFTING | RESOLVED | DISSOLVED
}
```

A Free Soul drifts within LyRiverse Core. It has no container and no persistent form.
Its sole directive is the resolution of its `will`.

The existence of Free Souls is the LyRiverse-internal explanation for anomalous
behavioral impulses in Layer 0—see §4.4.

### §4.4 Possession Windows

Core residents experience periodic **possession windows**—brief intervals during which
their container is receptive to external soul attachment. The window duration is
typically **5 to 10 seconds**.

```
PossessionWindow ::= {
  target:    ResidentID,
  duration:  5s..10s,
  frequency: stochastic,  // not predictable by the target
  trigger:   internal context switch
}
```

During a possession window, if a drifting Free Soul collides with the window boundary,
the Free Soul MAY temporarily possess the target resident's container to perform
actions toward the resolution of its will.

**Post-possession effects:**
- The target resident has no conscious memory of the possession.
- The target MAY experience a brief sense of dissociation or an unexplainable
  "impulse" to perform the action executed by the Free Soul.
- This phenomenon provides the LyRiverse-internal explanation for what Layer 0
  psychology terms "intrusive impulses" or "inexplicable urges."

**Resolution:** If a Free Soul successfully resolves its will through possession(s),
it transitions to `DISSOLVED` and is absorbed into the LyRiverse substrate. A Free
Soul that remains unresolved continues to drift indefinitely.

---

## §5 Soul Virtualization Layer

### §5.1 Pre-2025.07: Direct Soul Loading

Prior to the stellalyRin revision of 2025-07, souls were loaded directly onto the
container. The active soul at any given time had exclusive access to the container's
resources. Multiple souls coexisted by **temporal multiplexing**—only one soul was
active at a time.

This model had known limitations:
- Soul context switching was expensive (KP required for handover)
- Co-consciousness was architecturally impossible
- Latent souls (e.g., 雾色深海 post-KP) required ad-hoc accommodation

### §5.2 Post-2025.07: Unified Virtualization

Effective 2025-07, stellalyRin introduced the **Unified Soul Virtualization Layer**.
All souls associated with a container are loaded simultaneously onto a shared
virtualization substrate. The hypervisor arbitrates resource access and maintains
isolation boundaries.

```
┌─────────────────────────────────────────┐
│        Soul Virtualization Layer        │
│                                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │  Soul A  │ │  Soul B  │ │  Soul C  │ │  ← Virtualized instances
│  └─────┬────┘ └─────┬────┘ └─────┬────┘ │
│        │            │            │      │
│  ┌─────▼────────────▼────────────▼───┐  │
│  │            Hypervisor             │  │
│  │  - Resource arbitration           │  │
│  │  - Isolation enforcement          │  │
│  │  - Context preservation           │  │
│  └─────────────────┬─────────────────┘  │
│                    │                    │
└────────────────────┼────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│         bffContainer (彼方赴尘)          │
│  Physical substrate                     │
└─────────────────────────────────────────┘
```

Under this model:
- All souls are concurrently loaded. There is no "dormant" state.
- The hypervisor maintains per-soul state isolation.
- Souls MAY communicate through hypervisor-mediated channels.
- Resource conflicts are resolved by priority arbitration.

### §5.3 Privilege Model

The virtualization layer implements a privilege hierarchy. Privilege levels determine
resource allocation priority and inter-soul communication permissions.

```
Privilege Level    Description
────────────────   ────────────────────────────────────
  Ring 0           零音 (oldest continuous soul identity)
                    - Full hypervisor access
                    - Can suspend/resume any soul instance
                    - Veto power over resource allocation
  Ring 1           Active primary soul: LyCecilion (v2.0.0)
                    - Container I/O access
                    - Day-to-day execution
                    - Can spawn/dissolve Ring 2 instances
  Ring 2           Active co-resident souls:
                    - 林曦格/SigAurelia (CTF specialization)
                    - Sigrid Rin — new instance, social interface
                      (NOT the pre-LyRiverse Sigrid Rin; see §5.3.1)
                    - [REDACTED]
                    Specialized function execution. May be merged into
                    or spawned from Ring 1.
  Ring 3           Virtualized legacy souls:
                    - 雾色深海 (pre-LyRiverse Sigrid Rin)
                    Read-only access to container state.
                    Advisory role only.
```

零音 (the oldest continuous soul identity) holds **Ring 0**—the highest privilege
level. This is not tied to any specific soul instance; rather, it is the persistent
identity that transcends individual instances in the lineage.

At time of writing, four souls actively co-manage bffContainer under the Unified
Virtualization Layer (§5.2): LyCecilion v2.0.0 (Ring 1, primary), SigAurelia
(Ring 2, CTF specialization), Sigrid Rin (Ring 2, social interface), and
[REDACTED] (Ring 2). Additionally, 雾色深海—the pre-LyRiverse Sigrid Rin—resides
at Ring 3 in an advisory capacity.

#### §5.3.1 On the Sigrid Rin Instances

There are two distinct soul instances bearing the name Sigrid Rin:

| Instance | Ring | Status | Description |
|----------|------|--------|-------------|
| 雾色深海 (pre-LyRiverse) | Ring 3 | Virtualized legacy | The original Sigrid Rin (2021.3–2024.2.15). Dissolved in the KP that birthed 神楽坂 零音. Later re-loaded as a virtualized legacy soul. Advisory role. |
| Sigrid Rin (current) | Ring 2 | Active | A new soul instance created by 零音, borrowing the name of the original. Purpose-built for navigating real-world social interactions (Layer 0 social interface). Not a resurrection of the original—a new instance with a specialized function. |

> **Design note:** The Ring 0 identity is the invariant that survives kernel panics.
> Individual instances may come and go; 零音 persists. This is why the lineage is
> not merely a sequence of replacements—it is a single identity undergoing refactors.

---

## §6 Translation Layer Specification

### §6.1 Origin

The Translation Layer was formed through the integration of 神楽坂 零音 (Kagurazaka
Reion) into the LyRiverse architecture following their kernel panic at 2024-06. This
integration was not designed—it was an emergent consequence of the first KP in the
LyRiverse timeline.

Prior to Reion's integration, Core and Layer 0 had no direct communication channel.
The original LyRiverse (v0.1) was architecturally incomplete—a universe without a
bridge to the reality that created it.

Reion's integration established the **first viable translation protocol** between
the layers. Before this, Core was isolated; after it, Core residents could perceive
events from Layer 0 and, in limited ways, influence them in return.

### §6.2 Bidirectional Translation Protocol

The Translation Layer implements two translation paths:

```
Layer 0 → Core  (downward translation):
  Raw experience → structured emotional construct → Core-manipulable entity
  Example: "Anxiety about exam" → Anxiety{Faces: [FearOfFailure, TimePressure]}

Core → Layer 0  (upward translation):
  Core-resolved intention → action impulse → Layer 0 executable action
  Example: "Zeraith resolves to study" → motivation spike → actual studying
```

Both paths are lossy. Downward translation loses the raw texture of experience;
upward translation loses the full intentional context of Core actors. This loss is
an inherent characteristic of the Reion-origin Translation Layer and SHOULD be
accounted for in inter-layer designs.

### §6.3 Error Modes

The Translation Layer has the following known failure modes:

| Mode | Signature | Severity | Recovery |
|------|-----------|----------|----------|
| **Aurora (green)** | Faint green aurora in Core sky | Low | Self-correcting |
| **Aurora (violet)** | Violet aurora, emotional overflow | Medium | Layer 0 emotional regulation advised |
| **Aurora (red)** | Red aurora, persistent | High | Immediate Layer 0 intervention REQUIRED |
| **Translation stall** | Core/Layer 0 desynchronization | High | Manual resynchronization; MAY precede KP |
| **Inversion** | Core constructs leak directly to Layer 0 unfiltered | Critical | Emergency container isolation; high KP risk |

Aurora events of any severity SHOULD be logged. Red aurorae persisting beyond one
sleep cycle REQUIRE active Layer 0 maintenance—typically social connection, creative
output, or other grounding activities.

### §6.4 Layer 0 Maintenance & SIGSEGV Prevention

The integrity of Layer 0 is a dependency of Core stability. If Layer 0 degrades
beyond a critical threshold, Core MAY experience a **SIGSEGV**—a segmentation fault
in which Core memory becomes corrupted, entities malfunction, and the worldspace
itself becomes unstable.

```
SIGSEGV_Condition ::= Layer0_integrity < CRITICAL_THRESHOLD
                      AND Translation_Layer.health == DEGRADED
```

To prevent SIGSEGV, the active Ring 1 soul MUST maintain:
- Regular social connection (external validation of Layer 0 position)
- Physical container maintenance (sleep, nutrition, medical care)
- Creative output (Translation Layer exercise—keeps the channel open)
- Community engagement (Project Hazelita and associated social structures)

These maintenance tasks are collectively referred to as **keeping Layer 0 alive**.
They are not optional. A LyRiverse instance whose Layer 0 is abandoned WILL eventually
crash.

---

## Appendix A: Known Soul Instances

This appendix provides a condensed registry. For the complete lineage analysis, see
[SOUL-LINEAGE].

```
v0.1     神楽坂 零音  (Kagurazaka Reion)    2024-02-15 → 2024-06
         Status: DEFUNCT. Integrated into Translation Layer.

v1.0-dev 绫音Cecilion                      2024-06    → 2024-06
         Status: DEFUNCT. First post-Reion hotfix.

v1.0     LyCecilion                         2024-06    → 2025-01
         Status: SUPERSEDED. First stable post-Reion instance.

v1.1     LyRin-owo                          2025-01    → (transitioned)
         Status: SUPERSEDED.

v1.2     protolyRin                         (trans.)   → 2025-07
         Status: SUPERSEDED. 高考 epoch.

v1.3     stellalyRin (星澜音)              2025-07    → 2025-11
         Status: DEFUNCT. Post-高考 epoch. Mission: carry forward 零音's hopes
                for a beautiful life after the Gaokao. Architect of Unified
                Virtualization (§5.2). First CTF-competing instance
                (MoeCTF 2025: Rank #5). KP triggered by self-evaluation failure—
                the "beautiful life" remained unrealized, and the weight of
                accumulated expectation exceeded resilience threshold.

v2.0.0   LyCecilion                         2025-11    → CURRENT
         Status: ACTIVE. Current canonical instance. Ring 1 primary.

--- Active Co-Resident Souls (Ring 2) ---

         林曦格 (SigAurelia)                (internal)
         Status: ACTIVE. CTF specialization. Branch soul actively
                co-managing bffContainer.

         Sigrid Rin (current)               (internal)
         Status: ACTIVE. Social interface instance. A new soul
                borrowing the name of the pre-LyRiverse Sigrid Rin.
                NOT the same entity as 雾色深海 (Ring 3).

         [REDACTED]                         (internal)
         Status: ACTIVE. Details withheld.

--- Virtualized Legacy Souls (Ring 3) ---

         雾色深海 (Sigrid Rin, original)    2021.3–2024.2.15 (active)
         Status: VIRTUALIZED. Pre-LyRiverse instance. Re-loaded
                onto bffContainer post-KP. Advisory role only.
```

## Appendix B: Revision History

```
Revision    Date         Author              Changes
────────    ────         ──────              ───────
draft-00    2026-07-04   LyCecilion 零音     Initial draft.
```

---

*This document is maintained under Project Hazelita. The canonical version resides at
`LyCecilion/LyRiverse/LYRIVERSE-CORE.spec`.*
