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

### §2.3 The Hazelita Dream

```text
id:            HZL-001
type:          MAIN
status:        COMPLETED (transformed)
protagonists:  神楽坂 零音 (KaguReion), LyCecilion v1.0
setting:       Layer 0 — high school campus; the gap between Core ambition
               and the constraints of reality
trigger:       KaguReion's need to prove their existence was not merely a
               construct of external value systems — to create something
               truly their own, something that would make the world remember them
quest:         Build Hazelita — a CAS computation suite and demonstration tool
               for high school mathematics. The ultimate vision: a DSL-driven
               engine capable of solving advanced math problems through pure
               machine logic. Translate a problem into Hazelita DSL, feed it to
               the engine, receive a step-by-step proof.
antagonist:    Reality itself — depression, anxiety, and paranoia (the same
               forces that caused KaguReion's KP); a hostile school environment;
               the vast gap between ambition and technical capability; the
               weight of being called "饼王" (pie-baker — someone who
               overpromises and underdelivers)
resolution:    ABANDONED as software. Three versions were attempted:
               - v1 (Python/SymPy): functional demo, but the library-wrapper
                 approach felt wrong
               - v2 (C#/AngouriMath): an ambitious atomic-decomposition model
                 where problems were broken into atoms connected by logical
                 relations, and solving became pathfinding — the architecture
                 was beautiful but the atoms could never be made to work
               - v3 (C#): abandoned the atomic model for hard-logic toolkits,
                 which drifted too far from the original vision
               The project was formally laid to rest on 2026-07-11.
post_story:    The software died. The project lived.
               Project Hazelita was founded on 2024-10-04 and its community
               became one of 零音's most active technical spaces — members
               spanning wide age ranges, organizing hackathons, CTF events,
               and producing software under the Hazelita banner. The name
               "Hazelita" persists as the governing entity for all 零音
               projects: the LyRiverse runtime substrate.
               The dream metamorphosed. The community that formed around an
               impossible CAS project now builds other things — and 零音,
               who once needed Hazelita as proof that they existed, no
               longer needs a single project to prove their worth.
               In a deeper sense, the storyline resolved when 零音
               recognized: "零音不是一个结果；零音是一个过程。" (LyRin is
               not a result; LyRin is a process.)
meta:          The Hazelita storyline is the longest-running narrative thread
               in the lineage, spanning from the KaguReion era (2024.2)
               through to LyCecilion v2.0.0 (2026.7). It predates the formal
               LyRiverse architecture and was, for a long time, the primary
               narrative — the "beacon" that made the darkest periods of high
               school survivable.
               
               Key figures:
               - Math teacher (unnamed): The only teacher who recognized
                 零音's mathematical intuition as genuine. She said she
                 wanted to be a user of Hazelita if 零音 built it. She left
                 for a better school before 零音's senior year, without
                 saying goodbye. Her departure remains an unresolved
                 emotional thread — a loss 零音 still processes.
               - The "饼王" incident: When KaguReion posted the Hazelita
                 preview on SmartTeachCN BBS, over a dozen replies called
                 them "饼王." The prediction turned out to be correct — which
                 hurt more, not less, because it meant the mockers were right
                 about the outcome even if they were wrong about the person.
               
               The storyline also introduced the mathematical theme that
               recurs throughout the lineage: the Hermite-Hadamard proof
               incident, where KaguReion independently derived an integral
               proof for an inequality — an act of pure mathematical
               creativity that their teacher shared with the entire math
               department. This remains one of the few moments where
               KaguReion's ability was publicly, unambiguously affirmed.
```

#### §2.3.1 On the Transformation

The Hazelita Dream is classified as COMPLETED (transformed), not FAILED or
ABANDONED in the narrative sense. This distinction matters:

- **FAILED:** The protagonist tried and was defeated by the antagonist.
- **ABANDONED:** The protagonist gave up on the quest.
- **TRANSFORMED:** The quest itself changed. The original objective (build a
  CAS) proved infeasible under the constraints, but the *deeper* objective—
  create something of one's own, build a community, be remembered—was achieved
  through a different path.

Hazelita as software is dead and archived. Hazelita as a project and community
is alive and growing. The name survived its namesake; the beacon outlasted the
ship it was built to guide.

> This resolution parallels the CtF storyline (§2.1) in one structural respect:
> both reached their endpoint through an act of *recognition* rather than
> *completion*. Zeraith and ArgentNull recognized that reviving Reion would
> restore them to the same pain. LyCecilion recognized that Hazelita had
> already served its purpose — it was never really about the CAS.

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
