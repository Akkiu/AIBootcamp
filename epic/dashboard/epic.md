# Epic: Dashboard (Home)

**Stato:** Draft · Maggio 2026 · **Priorità:** Must — v1

> As a user, I want to see my financial status at a glance so that I always know how much I can spend without stress.

---

## Come funziona

La Home mostra: hero number "Free to Dream" (`stipendio − spese fisse − spese variabili − buffer`), riepilogo 4 bucket, obiettivi attivi con progress bar, spese ricorrenti in arrivo nei 7 giorni.

---

## Requisiti

| # | Requisito | Priorità |
|---|-----------|----------|
| D-01 | Saluto personalizzato con nome utente e ora del giorno | Must |
| D-02 | Hero card con "Free to Dream" in real-time | Must |
| D-03 | Indicatore positivo/negativo sotto l'hero | Must |
| D-04 | 4 bucket cards con importo e % sul reddito | Must |
| D-05 | Tap su bucket → dettaglio bucket | Should |
| D-06 | Lista obiettivi attivi con progress bar e importo residuo | Must |
| D-07 | Tap su obiettivo → dettaglio obiettivo | Must |
| D-08 | Sezione "In arrivo": spese ricorrenti nei 7 giorni con nome, importo, data | Must |
| D-09 | Sezione "In arrivo" nascosta se nessuna spesa nei 7 giorni | Should |
| D-10 | Stato vuoto se onboarding non completato (placeholder + CTA setup) | Must |
| D-11 | Pull-to-refresh | Should |
| D-12 | Bottom navigation: Home, Budget, Obiettivi, Profilo | Must |

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

## Dipendenze

- **Onboarding** — fornisce stipendio, spese fisse, variabili, buffer
- **Goals** — obiettivi mostrati in Home
- **Budget** — valori bucket aggiornabili in v1.1
