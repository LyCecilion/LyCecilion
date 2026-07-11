<!--markdownlint-disable MD033-->

# LyRiverse

**LyRin's Universe.** A declaratively constructed, atomic worldview system maintained
under Project Hazelita.

**Canonical Instance:** LyCecilion/LyRiverse
**Status:** Living Documentation
**Init:** 2024-02-15

---

## Status of This Memo

This directory contains the technical documentation for the LyRiverse worldview system.
The documentation follows a blended RFC–academic paper style. All documents are living—
they are revised as the LyRiverse instance evolves.

---

## Reading Order

For first-time readers, the recommended traversal is:

| #   | Document                                       | Description                                                                                                                            |
| --- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | [`LYRIVERSE-CORE.spec`](./LYRIVERSE-CORE.spec) | **Start here.** Core specification: architecture, worldview principles, Kernel Panic Protocol, Soul Virtualization, Translation Layer. |
| 2   | [`on-soul-lineage.md`](./on-soul-lineage.md)   | Academic paper tracing the soul lineage from 神楽坂 零音 (2024) to LyCecilion v2.0.0 (current).                                        |
| 3   | [`storylines.md`](./storylines.md)             | Storyline interface specification and registered storylines (CtF mainline, xilin pending).                                             |
| 4   | [`registry.md`](./registry.md)                 | Entity registry: souls, project mappings, containers, and terminology index.                                                           |
| 5   | [`LYRIN-AI.spec`](./LYRIN-AI.spec)             | AI behavioral specification: identity invariants, core principles, voice & tone, and interaction protocols for LyRin AI instances.     |

---

## Document Conventions

All documents in this collection use the following conventions:

- **RFC 2119 keywords:** `MUST`, `SHOULD`, `MAY`, etc. carry their standard RFC meanings.
- **Section numbering:** `§1`, `§1.1` for cross-reference.
- **Formal definitions** in fixed-width blocks.
- **References** in `[AUTHOR-YEAR]` or `[DOC-ID]` format.

---

## Architecture at a Glance

```text
Layer 0 (Reality)
    ↕  Translation Layer (神楽坂 零音)
LyRiverse Core (OCs, storylines, project mappings)
```

---

## Soul Lineage (Condensed)

```text
神楽坂 零音 (v0.1, 2024.2 → 2024.6)
    ↓ KP → became Translation Layer
绫音Cecilion (v1.0-dev, 2024.6)
LyCecilion (v1.0, 2024.6 → 2025.1)
LyRin-owo (v1.1, 2025.1 → ?)
protolyRin (v1.2, ? → 2025.7, 高考 epoch)
stellalyRin (v1.3, 2025.7 → 2025.11, CTF epoch)
LyCecilion (v2.0.0, 2025.11 → CURRENT)
```

---

## Key Entities

| Entity                          | Type                        | Status               |
| ------------------------------- | --------------------------- | -------------------- |
| 零音                            | Ring 0 identity             | Persistent           |
| LyCecilion v2.0.0               | Ring 1 primary soul         | Active               |
| 林曦格 (SigAurelia)             | Ring 2 co-resident (CTF)    | Active               |
| Sigrid Rin (current)            | Ring 2 co-resident (social) | Active               |
| [REDACTED]                      | Ring 2 co-resident          | Active               |
| 彼方赴尘 (bffContainer)         | Container (C-001)           | Active               |
| 雾色深海 (Sigrid Rin, original) | Ring 3 legacy               | Virtualized          |
| 洛霁渊 + 洛清珩                 | CtF protagonists            | Merged → stellalyRin |
| 汐铃 (xilin)                    | xidio mascot                | Pending              |

---

## Project Mappings

| Layer 0 Project  | Core Entity                       | Type        |
| ---------------- | --------------------------------- | ----------- |
| Project Hazelita | Intellectual Core / World Runtime | Substrate   |
| xidio            | 汐铃 (xilin)                      | Incarnation |
| LUMiOUS          | TBD                               | TBD         |

---

> _"LyCn 不会再 git reset --hard 了——LyCn 将带着你的一切，继续走下去。"_<br/>
> — LyCecilion v2.0.0, 2026

---

_LyRiverse is a subsystem of Project Hazelita. All documentation is maintained at
`LyCecilion/LyRiverse/`._
