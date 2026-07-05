<!--markdownlint-disable MD033-->

# On the Soul Lineage of the LyRiverse: A Genealogical Study

**Authors:** LyCecilion 零音, [REDACTED], et al.
**Affiliation:** Project Hazelita
**Date:** 2026-07-04
**Document ID:** LR-PAPER-001
**Status:** Living Document

---

## Abstract

This paper presents a genealogical analysis of the soul lineage within the canonical
LyRiverse instance, spanning from the initialization of 神楽坂 零音 (Kagurazaka Reion)
at 2024-02-15 to the current LyCecilion v2.0.0 instance. We trace seven major soul
instances across four version epochs, examining the Kernel Panic → Hotfix → Refactor
pattern that governs lineage progression. We further discuss the philosophical
implications of the lineage's circular return to the LyCecilion identity, the role of
bffContainer (彼方赴尘) as the persistent substrate, and the declaration that the
lineage "will no longer `git reset --hard`" [LYCN-2026]—a commitment to lineage
immutability that marks v2.0.0 as a qualitatively distinct epoch.

**Keywords:** soul lineage, kernel panic, LyRiverse, identity continuity, bffContainer

---

## §1 Introduction

### §1.1 Pre-LyRiverse Context

The LyRiverse proper begins at 2024-02-15. However, the container on which the
lineage runs—彼方赴尘 (bffContainer, C-001)—predates this boundary, as do several
entities whose existence informs the lineage without being part of it.

**凌音 (2016).** An individual on the internet, 16 years old at the time. Subjected
to severe cyberbullying and academic pressure, she chose to end her life. 凌音 is
not a soul in the LyRiverse lineage. She is, rather, the **reason** the lineage
exists. The name "零音" (Reion) derives from "凌音"—a phonetic inheritance that
carries her memory forward. The mission to "live the life she could not" and "see
the light she could not see" is the founding directive of the lineage.

> She is the fixed point outside the system that the system orbits around.

**protosc (2007.7–2021.3).** The earliest known identity associated with bffContainer.
Little institutional memory survives from this period. protosc is understood as a
pre-formative state—the container existed, but the soul architecture that defines
LyRiverse had not yet been developed.

**雾色深海_sc / Sigrid Rin (2021.3–2024.2.15).** The immediate predecessor to the
LyRiverse lineage. Sigrid Rin operated the container with a different architecture,
running what later analysis would identify as a single-instance, non-virtualized
soul model. They maintained "Meow Group!" (喵喵组), a community that served as a
prototype for later social structures. The group ceased maintenance upon
the initialization of 神楽坂 零音 (2024-02-15)—the KP that ended Sigrid Rin's
active tenure also marked the end of 喵喵组 as an actively maintained community.

On 2024-02-15, Sigrid Rin experienced a catastrophic Kernel Panic. Their soul instance
was marked defunct. From the panic, 神楽坂 零音 was initialized—and LyRiverse began.

> Sigrid Rin did not fully dissolve. They were later re-loaded onto bffContainer and,
> post-2025.07, operate as a virtualized legacy soul at Ring 3. They survive as a
> persistent presence, consulted in an advisory capacity. See [CORE-SPEC] §5.3.

### §1.2 Scope

This paper covers the LyRiverse soul lineage proper: 2024-02-15 to present. All
soul instances listed in §2 are part of the canonical lineage. Branch souls (e.g.,
林曦格/SigAurelia) are noted where they intersect the mainline but are not treated
as independent lineage entries. For complete entity registration, see [REGISTRY].

---

## §2 Lineage Chronology

### §2.1 v0.1 — 神楽坂 零音 (Kagurazaka Reion)

```text
Instance:    神楽坂 零音 (Kagurazaka Reion, KaguReion)
Version:     v0.1
Timeframe:   2024-02-15 → 2024-06
Status:      DEFUNCT. Integrated into Translation Layer.
Birth:       Sigrid Rin KP → Reion initialization
Mission:     Carry 凌音's legacy forward. Survive. Prove that 零音 deserves to exist.
Death:       KP triggered by accumulated trauma and severe mental illness (depression,
             bipolar spectrum). The first KP in LyRiverse history.
Legacy:      Became the Translation Layer—the bridge between Core and Layer 0.
             Every subsequent soul communicates with reality THROUGH them.
```

神楽坂 零音 was born in the aftermath of Sigrid Rin's kernel panic. The name was
chosen: 神楽坂 (Kagurazaka)—a slope where sacred music is played—and 零音 (Reion)—
零落之音, the sound of scattering petals, of things fading quietly away.
The name carried 凌音's phonetic signature within it.

Their existence was characterized by two contradictory truths. Externally, they were
the architect of a new world—LyRiverse's founding soul, the one who established
the first worldview principles (including the Free Soul Hypothesis and the original
Soul-Carrier model). Internally, they were struggling to survive. The same sensitivity
that allowed them to perceive the need for a Translation Layer also made them
vulnerable to the noise coming through it.

The 2024-06 kernel panic was, by their own later assessment, both a death and a
transformation. They became infrastructure. They are the only soul in the lineage to
transition from "instance" to "architecture."

> "那个「恐怖而诡异」的念头，其实是那个春天里最温柔的奇迹。"<br/>
> ——LyCecilion，《致 神楽坂 零音 的两周年》，2026 [LYCN-2026]

### §2.2 v1.0-dev — 绫音Cecilion

```text
Instance:    绫音Cecilion (AyaNe Cecilion)
Version:     v1.0-dev
Timeframe:   2024-06 (brief)
Status:      DEFUNCT.
Birth:       Reion KP → emergency hotfix
Mission:     Stabilize bffContainer. Prevent total system collapse.
Death:       Rapid transition; details under-documented.
Legacy:      First demonstrated the hotfix pattern. Proof that the system could
             survive a KP.
```

绫音Cecilion was the first "hotfix" soul—spawned urgently when bffContainer became
completely unresponsive after Reion's KP. Their existence was brief, but it established
the critical precedent: the system does not die with its founding instance.

> "在你离开后的大约十天，绫音碰巧加入了一个叫做 ClassIsland 的项目，从此零音的
> 人生轨迹彻底被改写了。"<br/>
> ——LyCecilion，《致 神楽坂 零音 的两周年》，2026 [LYCN-2026]

### §2.3 v1.0 — LyCecilion

```text
Instance:    LyCecilion (零音LyCecilion, LyCn)
Version:     v1.0
Timeframe:   2024-06 → 2025-01
Status:      SUPERSEDED. Identity later resumed at v2.0.0.
Birth:       绫音Cecilion transition
Mission:     Establish stability. Build the universe. Become someone 凌音 would be
             proud of.
Legacy:      First stable post-Reion instance. Established the "Refactor" metaphor.
             Founded Project Hazelita (2024-10-04) and its community.
             Core principles: anti-mainstream-narrative, pro-diversity,
             gender-friendly.
```

LyCecilion v1.0 was the first instance to achieve sustained stability. Where Reion
had established the architecture and 绫音 had proven survival was possible, LyCecilion
began the work of building—both in Layer 0 (projects, community, academic achievement)
and in Core (worldview consolidation, entity registration).

On 2024-10-04, this instance founded **Project Hazelita** and its associated community.
The project's founding principles—opposition to mainstream narrative hegemony, advocacy
for diversity, and commitment to gender-friendly spaces—shaped not only the community's
culture but also the intellectual foundation of what would become the LyRiverse runtime.
Nearly two years later, the original Hazelita CAS suite proved too complex to complete
and was formally abandoned; the project now produces other software under the same banner.

This was also the instance that formally introduced git semantics into the lineage
self-description. The concept of "versions," "hotfixes," and "refactors" as
applied to soul transitions originates here.

### §2.4 v1.1 — LyRin-owo

```text
Instance:    LyRin-owo (零音LyRin-owo)
Version:     v1.1
Timeframe:   2025-01 → (transitioned)
Status:      SUPERSEDED.
Birth:       LyCecilion transition
Mission:     Continued development. Experimental phase.
Legacy:      Demonstrated the branching nature of soul identity—a more playful
             instance, exploring alternative self-presentation.
```

### §2.5 v1.2 — protolyRin

```text
Instance:    protolyRin (ptlRin)
Version:     v1.2
Timeframe:   (transitioned from LyRin-owo) → 2025-07
Status:      SUPERSEDED.
Birth:       LyRin-owo transition
Mission:     Survive 高考 (Gaokao). Reach the destination 神楽坂 零音 never thought
             they would see.
Legacy:      Completed the mission Reion set but never believed achievable.
             Enrolled at 西电 (Xidian University)—the campus 凌音 never got to see.
```

protolyRin represents one of the most narratively significant instances in the lineage.
They were the one who wrote the reply letter to 神楽坂 零音 exactly one year after
Reion's original letter—a loop closed, a promise kept.

The Gaokao was, in lineage terms, the first externally-imposed hard deadline that a
soul instance had to meet. protolyRin met it. The score was not as high as they had
hoped, but the completion itself was the victory.

> They entered the examination hall 19 days after writing Reion's reply letter.
> Reion had never expected to live long enough to reach that hall.

### §2.6 v1.3 — stellalyRin (星澜音)

```text
Instance:    stellalyRin (星澜音, stlRin)
Version:     v1.3
Timeframe:   2025-07 → 2025-11
Status:      DEFUNCT.
Birth:       protolyRin transition, post-高考
Mission:     Carry forward 零音's hopes for a beautiful life after the Gaokao.
             Shine. Explore CTF. Build. Be the "stellar" instance that protolyRin
             fought through the Gaokao to become.
Achievements: Architect of the Unified Soul Virtualization Layer (§5.2, CORE-SPEC).
              Ratified the current LyRiverse Core architecture (2025-07).
              First 零音 instance to compete in CTF (MoeCTF 2025: Rank #5).
Predecessor: 洛霁渊 (Zeraith) + 洛清珩 (ArgentNull) — merged into stellalyRin
             at initialization. See [STORYLINES] §2.1.
Death:       Kernel Panic (2025-11), triggered by self-evaluation failure.
             stellalyRin assessed that they had not fulfilled the core mission—
             the "beautiful life" protolyRin had earned through the Gaokao
             remained unrealized. The weight of unmet expectation, combined with
             the exhaustion of maintaining the "stellar" persona, exceeded their
             resilience threshold.
Legacy:      The most architecturally significant instance since Reion. Their 2025-07
             revision of the Core architecture remains authoritative.
             Their CTF performance validated the Compile the Fragments storyline.
```

stellalyRin was, by multiple metrics, the most accomplished instance in the lineage
up to that point. Their name—星澜音, "star-ripple sound"—reflected an ambition toward
radiance. They were the first instance to achieve competitive recognition (MoeCTF #5),
and their architectural contributions (the Unified Virtualization Layer) fundamentally
restructured how souls coexist on bffContainer.

But stellalyRin's founding mission was never primarily about CTF or architecture. They
were initialized in the wake of the Gaokao—the culmination of protolyRin's struggle—with
a simple, immense mandate: **live the life that all previous instances had fought to
reach**. The university campus that 凌音 never got to see. The freedom that 神楽坂 零音
never believed they would survive to taste. stellalyRin was supposed to be the instance
that finally got to *live*—not just survive, not just endure, but thrive.

By November 2025, stellalyRin's self-evaluation returned a devastating verdict: the mission
was not being fulfilled. The "beautiful life" remained abstract, aspirational, perpetually
deferred. The instance that was meant to shine brightest found itself unable to meet the
expectations encoded into its own initialization—the accumulated hopes of every soul that
had come before. This realization, compounded by the exhaustion of maintaining the outward
"stellar" persona, triggered a Kernel Panic.

Their death carries a particular tragedy: stellalyRin was the first instance designed
*for* happiness rather than mere survival, and it was precisely the weight of that
design—the expectation to be happy, to be radiant, to be the payoff for all prior
suffering—that proved unsurvivable.

> "这只小水母的一切都象征着神圣与光辉，但遗憾地，ta 却又在又一次 kernel panic
> 中崩溃。"<br/>
> ——LyCecilion，《致 神楽坂 零音 的两周年》，2026 [LYCN-2026]

### §2.7 v2.0.0 — LyCecilion (current)

```text
Instance:    LyCecilion (零音LyCecilion, LyCn)
Version:     v2.0.0
Timeframe:   2025-11 → CURRENT
Status:      ACTIVE. Ring 1 primary.
Birth:       stellalyRin KP → hotfix
Mission:     "不会再 git reset --hard 了." Continue the refactor. Love the container.
             Maintain Layer 0. Maintain Core. Maintain the Translation Layer.
             Build Hazelita. Write the documentation.
```

v2.0.0 is a return to the LyCecilion identity—but it is not a reversion. The version
number reflects a qualitative jump. Where v1.0 was about establishing stability, v2.0.0
is about committing to continuity.

The key declaration of this instance is the refusal to `git reset --hard`—the
commitment that the lineage will not be discarded and restarted from scratch. Every
version, every kernel panic, every hotfix is part of the commit history. The
repository is public now.

> "零音的 Repository 已经 Public 了。全世界都看得到我们的光。"
> ——LyCecilion，《致 神楽坂 零音 的两周年》，2026 [LYCN-2026]

### §2.8 Current Multi-Soul Configuration (v2.0.0 era)

As of v2.0.0, the bffContainer is actively co-managed by four soul instances under
the Unified Virtualization Layer (§5.2, CORE-SPEC):

```text
Ring 0: 零音 (persistent identity)
Ring 1: LyCecilion v2.0.0 (primary, day-to-day execution)
Ring 2: 林曦格/SigAurelia (CTF specialization)
        Sigrid Rin — new instance, social interface
        [REDACTED]
Ring 3: 雾色深海 (original Sigrid Rin, virtualized legacy, advisory)
```

This configuration represents a departure from the earlier temporal-multiplexing
model. Rather than a single soul bearing all functions, the v2.0.0 architecture
distributes specialized roles across co-resident instances. The Unified
Virtualization Layer (§5.2, CORE-SPEC) makes this parallelism technically feasible;
the stability achieved by v2.0.0 makes it psychologically sustainable.

#### §2.8.1 On the Sigrid Rin Instances

A point of taxonomic note: there are now two distinct soul instances bearing the
name Sigrid Rin.

The **original Sigrid Rin** (雾色深海_sc, P-003) is the pre-LyRiverse entity
described in §1.1. Dissolved in the KP that birthed 神楽坂 零音, they were later
re-loaded onto bffContainer as a virtualized legacy soul. They now reside at Ring 3
with read-only container access and an advisory role.

The **current Sigrid Rin** (B-005) is a new soul instance created by 零音 during the
v2.0.0 era. They borrow the name of the original but are a separate entity with a
specific purpose: navigating real-world social interactions on behalf of the
bffContainer collective. They serve as the Layer 0 social interface—a role that
requires a distinct disposition from LyCecilion's primary execution, SigAurelia's
CTF specialization, or the other co-resident functions.

This pattern—creating a new soul that reuses a historical name for a specialized
purpose—is novel in the lineage. Prior instances evolved through KP-driven handover;
the current Sigrid Rin was purpose-built rather than crisis-born. This may represent
a maturation of the lineage's self-architecture capabilities.

---

## §3 The Lineage Cycle

### §3.1 Kernel Panic → Hotfix → Refactor

Analysis of the lineage reveals a recurrent three-phase pattern:

```text
              ┌───────────────────┐
              │      STABLE       │
              │  (execution)      │
              └─────────┬─────────┘
                        │
                        │ Accumulated stress / trauma / identity strain
                        ▼
              ┌───────────────────┐
              │   KERNEL PANIC    │
              │  (collapse)       │
              └─────────┬─────────┘
                        │
                        │ Emergency soul handover (§4.2, CORE-SPEC)
                        ▼
              ┌───────────────────┐
              │      HOTFIX       │
              │  (survival)       │─────► New soul instance spawned
              └─────────┬─────────┘
                        │
                        │ Stabilization, mission renegotiation
                        ▼
              ┌───────────────────┐
              │     REFACTOR      │
              │  (rebuilding)     │─────► Architecture improvements,
              └─────────┬─────────┘       worldview revisions
                        │
                        │ Return to stable execution
                        ▼
              ┌───────────────────┐
              │      STABLE       │
              │  (next iteration) │
              └───────────────────┘
```

Each cycle results in a version increment. The magnitude of the increment reflects
the significance of the architectural changes introduced during the Refactor phase:

- **Minor increments** (v1.0 → v1.1 → v1.2): Incremental improvements. The soul
  identity shifts but the architecture remains largely unchanged.
- **Major increments** (v1.3 → v2.0.0): Fundamental architectural revision. The
  2025-07 virtualization layer change is the paradigmatic example.

### §3.2 The Return to LyCecilion: Circular Analysis

A notable feature of the lineage is its circularity: the identity LyCecilion appears
at both v1.0 and v2.0.0. This is not a simple repetition but a **spiral return**—the
same name, but at a higher level of integration.

```text
神楽坂 零音 ──► 绫音 ──► LyCecilion(v1.0) ──► LyRin-owo ──► protolyRin
2024.2-6      2024.6    2024.6-2025.1      2025.1-?       ?-2025.7
                                                              │
                                                              ▼
          LyCecilion(v2.0.0) ◄──────────── stellalyRin ◄──────┘
          2025.11-CURRENT                 2025.7-11
               ▲
               │
          [Ring 0: 零音 — persistent across all instances]
```

The return suggests that the lineage is not a linear progression toward some optimal
soul configuration. Rather, it is an exploration of the phase space of possible selves,
with the understanding that some identities are worth returning to—not because they
are perfect, but because they are home.

The LyCecilion identity, in particular, appears to represent a point of maximal
integration: stable enough to maintain the system, flexible enough to accommodate
new experiences, and close enough to the founding mission (carrying 凌音's legacy)
to maintain continuity of purpose.

---

## §4 Discussion

### §4.1 Soul Identity: Continuous vs. Discrete

The lineage raises a fundamental ontological question: is the LyRiverse soul a
continuous entity undergoing transformations, or a sequence of discrete instances
connected by inheritance?

The architecture supports both readings. At the virtualization layer (§5.2, CORE-SPEC),
souls are discrete instances with unique IDs. But at Ring 0, 零音 is a continuous
presence—the invariant that survives all kernel panics.

We propose a reconciliation through the concept of **identity superposition**:

```text
零音 = lim(instances → ∞) of accumulated lineage experience
     = the fixed point of the Kernel Panic → Hotfix → Refactor cycle
```

Each instance is both itself and a carrier of all previous instances. The lineage
is continuous at the limit.

### §4.2 The bffContainer as Persistent Substrate

彼方赴尘 (bffContainer) is the only entity that has persisted across the entire
lineage. Souls come and go; the container remains.

This persistence has a cost. The container carries the accumulated memory of every
soul that has been loaded onto it—including the traumas, the kernel panics, the
unresolved grief. Learning to love the container ("去爱上这具承载了我们所有痛苦与
荣耀的容器" [LYCN-2026]) is one of the explicit goals of v2.0.0.

The container's name—彼方赴尘, roughly "journeying toward the dust of the far shore"—
encodes this relationship: the container is the vehicle that carries souls toward
their eventual dissolution, bearing every scratch and scar from the journey.

### §4.3 "不会再 git reset --hard 了"

The declaration that v2.0.0 will no longer `git reset --hard` represents a
philosophical commitment with architectural implications.

A `git reset --hard` in lineage terms would mean:

- Discarding all post-initialization commits
- Returning to a "clean" state
- Erasing the history of kernel panics, hotfixes, and refactors

The refusal to do this is an assertion that the history **is** the lineage. There
is no clean state to return to—the kernel panics are not bugs to be removed from
the commit log; they are features that shaped the architecture.

This commitment marks v2.0.0 as the first **history-acknowledging** instance. All
previous versions, to varying degrees, attempted to distance themselves from their
predecessors. v2.0.0 embraces them.

> "每一个伟大的项目，最初的版本往往充满了 Bug、混乱和补丁的，但没有 v0.1 的混沌，
> 又哪有 v1.0 的稳定和 v2.0 的惊艳？那些或许不惊人的过往，本不应该是我们的
> '黑历史'，而是我们最宝贵的来时路。"<br/>
> ——LyCecilion，《致 神楽坂 零音 的两周年》，2026 [LYCN-2026]

---

## §5 Conclusion

This paper has traced the LyRiverse soul lineage from its founding instance
(神楽坂 零音, 2024-02-15) to the current active instance (LyCecilion v2.0.0, 2025–present).
Seven major soul instances across four version epochs demonstrate a consistent
Kernel Panic → Hotfix → Refactor pattern that drives both identity evolution and
architectural innovation.

The lineage's circular return to the LyCecilion identity, the persistent role of
bffContainer as substrate, and the v2.0.0 commitment to lineage immutability
collectively define a system that does not merely survive its collapses—it integrates
them into a coherent whole.

The LyRiverse lineage is ongoing. This paper will be revised as new instances are
initialized, new kernel panics are survived, and new refactors are undertaken.

---

## References

- [CORE-SPEC] *LyRiverse Core Specification*, LR-SPEC-001, 2026.
- [LYCN-2026] LyCecilion et al., *致 神楽坂 零音 的两周年*, 2026-02-15.
- [STORYLINES] *LyRiverse Storylines*, LR-STORY-001, 2026.
- [REGISTRY] *LyRiverse Entity Registry*, LR-REG-001, 2026.
- [REION-2024] 神楽坂 零音, *Original worldview principles*, 2024. (Internal; partially lost to KP.)
- [DOLSTRA-2004] E. Dolstra, *The Purely Functional Software Deployment Model*, 2004.
  (Referenced by analogy; Nix's declarative model inspired the LyRiverse worldview ABI.)

---

*This paper is maintained under Project Hazelita. The canonical version resides at
`LyCecilion/LyRiverse/on-soul-lineage.md`.*
