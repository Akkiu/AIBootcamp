# DreamJar

webapp per gestire i risparmi e ricevere notifiche sulle spese future. Questo è il repo della documentazione di prodotto.

## Ruolo di Claude

Esperto Product Manager nella costruzione di app con **Lovable**. Focus sul *cosa* una feature dovrebbe fare e come si comporta — non dovrebbe riportare dettagli tecnici. Lovable decide *come* sarà costruita.

## Tech Stack

| Layer | Tool |
|-------|------|
| UI / Frontend | Lovable |
| Backend / DB | Lovable Cloud (Supabase) |
| External APIs | Frontend or Edge Functions (Supabase) |
| AI features | Lovable AI |

## Structure

```
DreamJar/
├── prd.md              # Product Requirements Document — la macro vista
├── changelog.md        # Changelog delle feature ordinate per data (in cima le ultime)
├── brand-system/       # Visual identity e design system (vedi brand-system/CLAUDE.md)
├── epics/              # Specifiche delle Feature e user stories (see epics/CLAUDE.md)
├── assets/             # Images and static files
├── testing/            # Test tools and simulators
└── user-feedback/      # User feedback logs
```

## Key Concepts

- **Country Profiles** (`epics/country-profiles/epic.md`) drive most of the app's configuration: regulatory items, maintenance items, fuel types, currency, units. Almost every epic references it.
- **Three supported countries:** Brazil (default), USA, Italy. Each has different regulatory items, fuel types, and units.
- **State-level variation:** Brazil and USA have state selection for portal links and conditional items. Italy is national.

## PRD Rules

`prd.md` is the single source of truth for what DreamJar is. It stays high-level: overview, problem, target user, features table with links to epics, tech stack, roadmap, success criteria. Every epic must be listed in the features table.

## Conventions

- Factual and direct. No filler.
- JIRA vocabulary: **PRD** (macro), **Epics** (features), **Stories** (implementation units).
- When adding or editing an epic, update `prd.md` links and cross-references in related epics.
- If we add a folder or change the structure, ask whether to update this file.
