# Epic: Dashboard (Home)

**Stato:** Done · Maggio 2026 · **Priorità:** Must — v1

> As a user, I want to see my financial status at a glance so that I always know how much I can spend without stress.

---

## Come funziona

La Home mostra: hero number "Free to Dream" (`stipendio − spese fisse − svago − imprevisti − utenze − altro`), riepilogo 6 bucket, sezione Analytics con breakdown delle spese, obiettivi attivi con progress bar, spese ricorrenti in arrivo nei 7 giorni.

---

## Requisiti

| # | Requisito | Priorità |
|---|-----------|----------|
| D-01 | Saluto personalizzato con nome utente e ora del giorno | Must |
| D-02 | Hero card con "Free to Dream" in real-time | Must |
| D-03 | Indicatore positivo/negativo sotto l'hero | Must |
| D-04 | 6 bucket cards (Spese fisse, Svago, Imprevisti, Utenze, Altro, Obiettivi) con importo e % sul reddito | Must |
| D-05 | Tap su bucket → dettaglio bucket | Should |
| D-06 | Lista obiettivi attivi con progress bar e importo residuo | Must |
| D-07 | Tap su obiettivo → dettaglio obiettivo | Must |
| D-08 | Sezione "In arrivo": spese ricorrenti nei 7 giorni con nome, importo, data | Must |
| D-09 | Sezione "In arrivo" nascosta se nessuna spesa nei 7 giorni | Should |
| D-10 | Stato vuoto se onboarding non completato (placeholder + CTA setup) | Must |
| D-11 | Pull-to-refresh | Should |
| D-12 | Bottom navigation: Home, Budget, Obiettivi, Profilo | Must |
| D-13 | Sezione Analytics: breakdown grafico delle spese per bucket del mese corrente | Should |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Normale | Visualizzazione completa |
| Free to Dream < 0 | Hero in corallo, messaggio di supporto non colpevolizzante |
| Nessun obiettivo | CTA "Aggiungi il tuo primo obiettivo" |
| Nessuna spesa in arrivo | Sezione "In arrivo" nascosta |
| Onboarding incompleto | Placeholder + CTA setup |
| Loading | Skeleton loaders |

---

## Sub-epiche

- **[Dream Manager](dream-manager/epic.md)** — aggiunta, modifica ed eliminazione sogni
- **[Bucket Manager / Tracking](bucket-manager/tracking/epic-expense-tracking.md)** — registrazione spese manuali e modifica spese fisse
- **[Riepilogo Spese](expense-summary/epic.md)** — schermata con lista cronologica di tutte le spese del mese
- **[Header Coach](header%20coach/epic.md)** — messaggio contestuale sul budget rimanente

## Dipendenze

- **Onboarding** — fornisce stipendio e i budget dei 6 bucket
- **Goals** — obiettivi mostrati in Home
- **Budget** — valori bucket aggiornabili in v1.1
