# Epic: Onboarding

**Stato:** Draft · Maggio 2026 · **Priorità:** Must — v1

> As a new user, I want to set up my budget in a few guided steps so that I can immediately see my "Free to Dream" number without any manual configuration.

---

## Come funziona

Flusso a 5 step sequenziali. Al termine, `profiles.onboarding_completed = true` e l'utente atterra sulla Home con tutti i numeri popolati.

```
Splash → Stipendio → Spese fisse → Lifestyle quiz → Primo obiettivo → Home
```

| Step | Cosa raccoglie | Dove va |
|------|---------------|---------|
| 1 · Splash | — | — |
| 2 · Stipendio | `monthly_income` | `profiles` |
| 3 · Spese fisse | Lista `recurring_expenses` (bucket `fixed`) | `recurring_expenses` |
| 4 · Lifestyle quiz | `variable_expenses`, `buffer` | `profiles` |
| 5 · Primo obiettivo | Primo record `goals` | `goals` |

---

## Requisiti

| # | Requisito | Priorità |
|---|-----------|----------|
| O-01 | Splash con valore del prodotto e CTA "Inizia" | Must |
| O-02 | Input stipendio mensile netto | Must |
| O-03 | Aggiunta spese fisse ricorrenti (nome, importo, giorno del mese) | Must |
| O-04 | Possibilità di aggiungere più spese fisse prima di andare avanti | Must |
| O-05 | Lifestyle quiz per stimare spese variabili e buffer (domande chiuse) | Must |
| O-06 | Creazione primo obiettivo (nome, emoji, importo target, data target) | Must |
| O-07 | Indicatore di progresso (step X di 5) visibile in ogni schermata | Should |
| O-08 | Navigazione "Indietro" tra gli step senza perdere i dati inseriti | Should |
| O-09 | Validazione inline: importi > 0, campi obbligatori | Must |
| O-10 | Al termine, `onboarding_completed = true` e redirect alla Home | Must |
| O-11 | Se l'utente torna all'app a metà onboarding, riparte dall'ultimo step | Should |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Primo accesso | Parte dallo Splash |
| Onboarding a metà | Riparte dall'ultimo step incompleto |
| Validazione fallita | Errore inline sul campo, bottone "Avanti" disabilitato |
| Loading salvataggio | Spinner sul bottone, input disabilitati |

---

## Dipendenze

- **Dashboard** — legge `profiles` e `recurring_expenses` popolati qui
- **Goals** — il primo obiettivo creato appare immediatamente nella Home
- **Auth** — l'utente deve essere autenticato prima di accedere all'onboarding
