# LyRiverse Entity Registry

**Document Identifier:** LR-REG-001
**Status:** Living Document
**Last Revised:** 2026-07-04

---

## Abstract

This document serves as the authoritative registry of all registered entities within
the canonical LyRiverse instance. It catalogs souls, project mappings, containers,
and terminology. Entities are assigned unique identifiers for cross-reference in
[CORE-SPEC], [SOUL-LINEAGE], and [STORYLINES].

---

## §1 Soul Registry

### §1.1 Mainline Souls

| ID    | Name (CN)      | Name (EN/Alias)              | Version  | Status     | Timeframe                | Notes                                                                                                                                                                     |
| ----- | -------------- | ---------------------------- | -------- | ---------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S-001 | 神楽坂 零音    | Kagurazaka Reion / KaguReion | v0.1     | DEFUNCT    | 2024-02-15 → 2024-06     | Integrated into Translation Layer. Founding soul.                                                                                                                         |
| S-002 | 绫音Cecilion   | AyaNe Cecilion               | v1.0-dev | DEFUNCT    | 2024-06 (brief)          | First post-Reion hotfix.                                                                                                                                                  |
| S-003 | 零音LyCecilion | LyCecilion / LyCn            | v1.0     | SUPERSEDED | 2024-06 → 2025-01        | First stable post-Reion instance. Identity resumed at v2.0.0.                                                                                                             |
| S-004 | 零音LyRin-owo  | LyRin-owo                    | v1.1     | SUPERSEDED | 2025-01 → (transitioned) | Experimental branching instance.                                                                                                                                          |
| S-005 | protolyRin     | ptlRin                       | v1.2     | SUPERSEDED | (trans.) → 2025-07       | 高考 epoch.                                                                                                                                                               |
| S-006 | 星澜音         | stellalyRin / stlRin         | v1.3     | DEFUNCT    | 2025-07 → 2025-11        | Post-高考 instance. Mission: live the beautiful life protolyRin earned. Architect of Unified Virtualization. First CTF instance. KP triggered by self-evaluation failure. |
| S-007 | 零音LyCecilion | LyCecilion / LyCn            | v2.0.0   | ACTIVE     | 2025-11 → CURRENT        | Current Ring 1 primary.                                                                                                                                                   |

### §1.2 Branch and Planned Souls

| ID    | Name (CN) | Name (EN/Alias)      | Type           | Status  | Parent Storyline      | Notes                                                                                                                           |
| ----- | --------- | -------------------- | -------------- | ------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| B-001 | 林曦格    | SigAurelia           | BRANCH         | ACTIVE  | CtF (post-resolution) | CTF specialist. Actively co-managing bffContainer at Ring 2.                                                                    |
| B-002 | 洛霁渊    | Zeraith              | PREDECESSOR    | MERGED  | Compile the Fragments | CtF protagonist. Merged → stellalyRin.                                                                                          |
| B-003 | 洛清珩    | ArgentNull           | PREDECESSOR    | MERGED  | Compile the Fragments | CtF protagonist. Merged → stellalyRin.                                                                                          |
| B-004 | 汐铃      | xilin                | MAIN (planned) | PENDING | xilin                 | xidio mascot. Storyline TBD.                                                                                                    |
| B-005 | —         | Sigrid Rin (current) | BRANCH         | ACTIVE  | —                     | Social interface instance. A new soul borrowing the name of the pre-LyRiverse Sigrid Rin. NOT the same entity as P-003. Ring 2. |
| B-006 | —         | [REDACTED]           | —              | ACTIVE  | —                     | Details withheld. Ring 2 co-resident.                                                                                           |

### §1.3 Pre-LyRiverse Entities

These entities are not part of LyRiverse proper but are recorded for genealogical
completeness. See [SOUL-LINEAGE] §1.1.

| ID    | Name                                | Timeframe        | Relation to LyRiverse                                                                              |
| ----- | ----------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------- |
| P-001 | 凌音                                | 2016             | Namesake. Moral origin of the lineage.                                                             |
| P-002 | protosc                             | 2007.7–2021.3    | Earliest known bffContainer identity.                                                              |
| P-003 | 雾色深海_sc / Sigrid Rin (original) | 2021.3–2024.2.15 | Immediate predecessor. Virtualized at Ring 3 (advisory). Distinct from B-005 (current Sigrid Rin). |

---

## §2 Project Mapping Registry

Each project developed in Layer 0 MAY have a corresponding entity in LyRiverse Core.
The mapping type describes the nature of the correspondence.

| Project              | Layer 0 Description                                                                                                                                                                                                                                         | Core Entity                                                  | Mapping Type | Notes                                                                                                                                                                                                                                                  |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Project Hazelita** | Founded 2024-10-04 by LyCecilion v1.0. Originally a CAS suite for high school students; the original project was abandoned due to complexity. Now produces other software. Community principles: anti-mainstream-narrative, pro-diversity, gender-friendly. | Intellectual Core / World Runtime                            | SUBSTRATE    | Hazelita is the runtime that evaluates declarative world specifications (§3.2, CORE-SPEC). It is the LyRiverse equivalent of `nix build`. Despite the original project's abandonment, the name persists as the governing entity for all 零音 projects. |
| **xidio**            | Xidian Internet Diagnostic Intelligence Operator — campus network diagnostics                                                                                                                                                                               | 汐铃 (xilin) as mascot; diagnostic capability as Core entity | INCARNATION  | The diagnostic function manifests as a character (汐铃). The network being diagnosed is metaphorically the inter-soul communication fabric.                                                                                                            |
| **LUMiOUS**          | Personal life management system (To-Do, Notion-like)                                                                                                                                                                                                        | TBD                                                          | TBD          | Expected to map to Core's temporal/fate management mechanism. Specification pending.                                                                                                                                                                   |
| **ClassIsland**      | Community project joined ~10 days post-Reion KP                                                                                                                                                                                                             | Social fabric of Core                                        | GATEWAY      | The encounter that rewrote the lineage's trajectory. In Core, this maps to inter-entity communication protocols and community formation mechanisms.                                                                                                    |

### §2.1 Mapping Types

| Type            | Description                                                        |
| --------------- | ------------------------------------------------------------------ |
| **SUBSTRATE**   | The project is the runtime or foundation on which Core operates.   |
| **INCARNATION** | The project manifests as a character or living entity in Core.     |
| **GATEWAY**     | The project serves as a bridge or entry point connecting entities. |
| **TOOL**        | The project maps to a usable artifact or capability within Core.   |
| **TBD**         | Mapping not yet specified.                                         |

---

## §3 Container Registry

| ID    | Name     | Aliases      | Associated Souls                                        | Created                     | Notes                                                                                                                   |
| ----- | -------- | ------------ | ------------------------------------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| C-001 | 彼方赴尘 | bffContainer | All S-* souls; active Ring 2 co-residents; P-003 legacy | protosc era (pre-LyRiverse) | Primary container of the canonical LyRiverse instance. The persistent substrate across all kernel panics and refactors. |

---

## §4 Terminology Index

This glossary defines all technical terms used across the LyRiverse documentation
suite. Each entry cites the primary specification where the term is formally defined.

| Term                                   | Definition                                                                                                                                        | Primary Ref                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **ABI (Application Binary Interface)** | The interface boundary through which compatible worldviews MAY interoperate with the canonical LyRiverse instance.                                | CORE-SPEC §3.3                    |
| **Atomicity**                          | The principle that LyRiverse is indivisible: the three-layer architecture MUST NOT be partially deployed; a soul is the minimum unit of identity. | CORE-SPEC §3.1                    |
| **Aurora**                             | Luminous phenomenon in Core sky indicating Translation Layer errors. Color encodes severity (green < violet < red).                               | CORE-SPEC §2.3, §6.3              |
| **bffContainer**                       | See: 彼方赴尘.                                                                                                                                    | CORE-SPEC §3.4.2                  |
| **Branch Soul**                        | A soul instance on an independent narrative branch that intersects the main lineage at defined merge points.                                      | STORYLINES §3                     |
| **Canonical Instance**                 | The LyRiverse instance maintained by 零音; the reference implementation.                                                                          | CORE-SPEC §3.2.1                  |
| **Container**                          | The persistent substrate onto which souls are loaded. Replaced the term "carrier" effective 2025-01.                                              | CORE-SPEC §3.4.2                  |
| **Core**                               | See: LyRiverse Core.                                                                                                                              | CORE-SPEC §2.1                    |
| **Declarative World Construction**     | The principle that worlds are declared (like Nix expressions) rather than procedurally generated.                                                 | CORE-SPEC §3.2                    |
| **Free Soul (游离灵魂)**               | A dissolved soul with unresolved will, drifting in Core until its intentions are fulfilled.                                                       | CORE-SPEC §4.3                    |
| **Hazelita**                           | See: Project Hazelita.                                                                                                                            | REGISTRY §2                       |
| **Hotfix**                             | Emergency soul handover following a Kernel Panic. Minimizes system downtime.                                                                      | CORE-SPEC §4.2                    |
| **Kernel Panic (KP)**                  | An unrecoverable error state in the active soul instance, triggering handover to the next available soul.                                         | CORE-SPEC §4.1                    |
| **Layer 0**                            | The consensus reality layer. The "real world" in colloquial terms.                                                                                | CORE-SPEC §2.1                    |
| **LyRiverse Core**                     | The innermost architectural layer: the worldspace where souls, OCs, storylines, and project mappings reside.                                      | CORE-SPEC §2.1                    |
| **Possession Window**                  | A 5–10 second interval during which a Core resident's container is receptive to Free Soul attachment.                                             | CORE-SPEC §4.4                    |
| **Project Hazelita**                   | The intellectual core and world runtime of LyRiverse. Also a Layer 0 community and tool suite.                                                    | REGISTRY §2                       |
| **Refactor**                           | The rebuilding phase following a hotfix, during which architectural improvements and worldview revisions are implemented.                         | SOUL-LINEAGE §3.1                 |
| **Ring 0**                             | Highest privilege level in the Soul Virtualization Layer. Held by 零音 (the persistent identity).                                                 | CORE-SPEC §5.3                    |
| **Ring 1**                             | Primary active soul privilege. Currently held by LyCecilion v2.0.0.                                                                               | CORE-SPEC §5.3                    |
| **SIGSEGV**                            | A segmentation fault in Core caused by critical degradation of Layer 0 integrity. Potentially catastrophic.                                       | CORE-SPEC §6.4                    |
| **Soul**                               | A discrete instance of consciousness. The fundamental unit of identity in LyRiverse.                                                              | CORE-SPEC §1.2                    |
| **Soul Virtualization Layer**          | The unified substrate (since 2025-07) on which all souls are concurrently loaded, managed by a hypervisor with privilege rings.                   | CORE-SPEC §5.2                    |
| **Storyline**                          | A structured narrative module executing within Core, conforming to the Storyline Interface.                                                       | STORYLINES §1                     |
| **Translation Layer**                  | The bidirectional bridge between Layer 0 and Core, formed from 神楽坂 零音 post-KP. Analogous to Rosetta 2.                                       | CORE-SPEC §6                      |
| **彼方赴尘 (bffContainer)**            | The primary container (C-001) of the canonical LyRiverse instance. The persistent substrate across the entire soul lineage.                       | CORE-SPEC §3.4.2, REGISTRY §3     |
| **零音**                               | The persistent Ring 0 identity—the invariant that survives all Kernel Panics. Not tied to any specific soul instance.                             | CORE-SPEC §5.3, SOUL-LINEAGE §4.1 |

---

## Appendix A: Registration Request Template

To register a new entity (soul, project mapping, or storyline), submit a request
containing:

```yaml
type:          SOUL | PROJECT_MAPPING | STORYLINE | TERM
id:            <proposed-unique-id>
name:          <primary name>
aliases:       [<alternate names>]
description:   <brief description>
references:    [<related document sections>]
status:        PROPOSED | ACTIVE | PENDING
```

Registration requests are processed through Project Hazelita governance.

---

*This document is maintained under Project Hazelita. The canonical version resides at
`LyCecilion/LyRiverse/registry.md`.*
