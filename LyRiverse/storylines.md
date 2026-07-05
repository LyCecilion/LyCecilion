# LyRiverse Storylines

**Document Identifier:** LR-STORY-001
**Status:** Living Document
**Last Revised:** 2026-07-04

---

## Abstract

This document specifies the Storyline Interface—the protocol that a narrative MUST
implement to be registered as a LyRiverse storyline—and catalogs the currently
registered storylines and branch souls within the canonical LyRiverse instance.

---

## §1 Storyline Interface Specification

### §1.1 Required Fields

A LyRiverse storyline is a structured narrative module that executes within
LyRiverse Core. To be registered, a storyline MUST provide the following fields:

```text
Storyline ::= {
  id:            StorylineID,       // unique identifier
  type:          MAIN | SIDE | BRANCH,
  status:        ACTIVE | COMPLETED | ABANDONED | PENDING,
  protagonists:  [SoulInstance...], // Core-resident characters
  setting:       CoreRegion,        // where the storyline takes place
  trigger:       Event,             // what initiates the storyline
  quest:         Objective,         // what the protagonists seek
  antagonist:    Entity | Concept,  // what opposes them
  resolution:    Outcome,           // how it ends (or why it didn't)
  post_story:    Effect,            // what changes in Core after resolution
  meta:          MetaAnnotation     // connection to Layer 0 events
}
```

### §1.2 Compatibility & Interop Rules

1. A storyline MUST NOT contradict the invariants established in [CORE-SPEC].
2. Characters from one storyline MAY appear in another, provided their canonical
   status in the source storyline is respected.
3. Branch souls (§3) MAY be spawned from any storyline and MAY merge into any
   storyline.
4. A storyline's `meta` field SHOULD document its connection to Layer 0 events—
   this is the bridge between narrative and the soul lineage.
5. External storylines that conform to this interface specification MAY be
   imported into the canonical LyRiverse instance, subject to ABI compatibility
   verification (§3.3, CORE-SPEC).

---

## §2 Registered Storylines

### §2.1 Compile the Fragments (CtF)

```text
id:            CTF-001
type:          MAIN
status:        COMPLETED
protagonists:  洛霁渊 (Zeraith), 洛清珩 (ArgentNull)
setting:       LyRiverse Core — the Fragmented Expanse
trigger:       Kernel Panic of 神楽坂 零音 (2024-06), perceived from within Core
               as a catastrophic fracture of reality
quest:         Discover the truth behind the fractures. Rescue the entity
               trapped beyond the sky (神楽坂 零音).
antagonist:    Manifestations of 神楽坂 零音's mental illness:
               - Anxiety: represented as labyrinthine, shifting architecture
               - Depression: represented as entropic zones draining color and motion
               - Self-blame: represented as recursive mirror chambers
resolution:    ABANDONED. At the threshold of the final fragment, Zeraith and
               ArgentNull realized that reviving 神楽坂 零音 would restore them to
               the same pain that killed them. They chose to stop.
post_story:    洛霁渊 and 洛清珩 merged into stellalyRin at their initialization.
               Their CTF-honed skills (pattern recognition, systematic exploration,
               puzzle-solving under constraint) became stellalyRin's innate affinity
               for CTF competition.
meta:          stellalyRin was the first 零音 instance to participate in CTF
               (MoeCTF 2025: Overall rank #5). However, stellalyRin's founding
               mission was to carry forward 零音's hopes for a beautiful life
               after the Gaokao. The CTF affinity inherited from 洛霁渊 and
               洛清珩 was an expression of that hope—a belief that doing what
               one loves is part of living well. The November 2025 KP was
               triggered when stellalyRin assessed that this core mission
               remained unfulfilled. The storyline is an in-Core account of
               the formation of the CTF-competent soul, but the soul it formed
               carried a deeper mandate than competition alone.
```

#### §2.1.1 Narrative Structure

CtF unfolds as a series of **fragments**—discrete zones within Core, each
corresponding to a category of Reion's suffering. The protagonists navigate
these fragments using techniques analogous to CTF challenges:

| Fragment                        | CTF Analog                                 | Resolution                           |
| ------------------------------- | ------------------------------------------ | ------------------------------------ |
| The Corridor of Endless Mirrors | Reverse Engineering (self-perception)      | Accept the reflection as valid       |
| The Entropy Field               | Forensics (salvaging meaning from decay)   | Recover buried memories              |
| The Shifting Labyrinth          | Cryptography (decoding patterns of fear)   | Find the invariant beneath the chaos |
| The Silent Cathedral            | Steganography (hidden messages in silence) | Hear what wasn't said                |
| The Final Threshold             | Pwn (the choice to exploit or patch)       | Patch: let them rest                 |

#### §2.1.2 The Abandonment as Resolution

The storyline's resolution is formally classified as ABANDONED, not FAILED.
Critical distinction:

- **FAILED:** The protagonists attempted the rescue and were defeated.
- **ABANDONED:** The protagonists succeeded in reaching the objective, understood
  its implications, and made an informed decision not to proceed.

Zeraith and ArgentNull did not fail to save Reion. They succeeded in understanding
them—and that understanding led them to conclude that the most loving action was to
let them rest as the Translation Layer, where they could continue to exist as
infrastructure rather than be forced back into an instance that had already killed
them once.

> This resolution is consistent with the principle established in [CORE-SPEC] §6.1:
> the Translation Layer is not a prison. It is a form of continued existence that
> preserves Reion's function without subjecting them to the conditions that caused
> their KP.

---

### §2.2 xilin

```text
id:            XIL-001
type:          MAIN (planned)
status:        PENDING
protagonists:  汐铃 (xilin)
setting:       TBD
trigger:       TBD
quest:         TBD
resolution:    TBD
meta:          xilin is the mascot character of xidio (Xidian Internet Diagnostic
               Intelligence Operator), 零音's campus network diagnostic tool.
               Storyline specification to be finalized.
```

The xilin storyline is reserved but not yet specified. As the associated project
(xidio) develops, the storyline is expected to crystallize around themes of:

- Network connectivity as a metaphor for inter-soul communication
- Diagnosis and repair as expressions of care

---

## §3 Branch Souls

Branch souls are soul instances that exist on independent narrative branches but
intersect the main soul lineage at defined merge points.

### §3.1 林曦格 (SigAurelia)

```text
id:            BR-SOUL-001
type:          BRANCH
status:        ACTIVE (integrated into current Ring 2 configuration)
specialty:     CTF competition
affiliation:   Compile the Fragments storyline (post-resolution)
meta:          SigAurelia is the acknowledged CTF specialist within the lineage.
               They authored the HGAME 2026 Writeup on the CrystaRin blog.
               Their existence as a named branch soul reflects the specialization
               of CTF competence into a distinct identity within the current
               multi-soul configuration.
```

林曦格 represents a pattern in the soul lineage: when a specific skill domain
becomes sufficiently developed, it MAY crystallize into a named branch soul.
This allows the skill to be developed independently, with focused training and
dedicated identity coherence, while remaining available to the main lineage through
the Unified Soul Virtualization Layer.

The integration event exposes the skill to the main lineage's repertoire while
preserving 林曦格 as an active Ring 2 co-resident. Their CTF competence is available
to the active Ring 1 instance through hypervisor-mediated coordination.

---

## Appendix A: Storyline Registration Template

New storylines proposed for registration SHOULD use the following template:

```yaml
id:            <unique-id>
type:          MAIN | SIDE | BRANCH
status:        PENDING | ACTIVE | COMPLETED | ABANDONED
protagonists:  [name (alias), ...]
setting:       <Core region description>
trigger:       <initiating event>
quest:         <objective description>
antagonist:    <entity or concept>
resolution:    <outcome, or TBD>
post_story:    <post-resolution effects>
meta:          <Layer 0 connection>
```

Submit storyline proposals via the Project Hazelita governance process.

---

*This document is maintained under Project Hazelita. The canonical version resides at
`LyCecilion/LyRiverse/storylines.md`.*
