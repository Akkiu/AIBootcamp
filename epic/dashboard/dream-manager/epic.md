# Epic: Gestione Sogni

**Stato:** Done · Maggio 2026 · **Priorità:** Must — v1

> As a user, I want to add, edit, and delete my dreams so that my list always reflects what I'm actually saving for.

---

## Come funziona

L'utente accede ai sogni dalla Home (sezione Sogni) o dalla schermata dedicata. Da lì può aggiungere un nuovo sogno, modificare i dati di un sogno esistente, oppure eliminarlo. Il vincolo fondamentale è che almeno un sogno deve sempre esistere: l'eliminazione è bloccata se rimane un solo sogno nell'elenco.

**Limite Free:** gli utenti nel piano gratuito possono avere al massimo 1 sogno attivo. Il pulsante "+" è visibile ma porta a un paywall se l'utente è Free e ha già 1 sogno (→ DM-11).

```
Home (sezione Sogni)
  ├── tap "+" → bottom sheet Nuovo sogno
  └── tap su sogno → Dettaglio sogno
        ├── pulsante Modifica → bottom sheet Modifica dati
        └── pulsante Elimina → modale conferma
                                 └── bloccato se è l'ultimo sogno
```

Ogni sogno ha: nome, emoji, importo target e data target (opzionale). Il progresso (`saved_amount / target_amount`) è calcolato e mostrato come barra nella card.

---

## Requisiti

| # | Requisito | Priorità |
|---|-----------|----------|
| DM-01 | Pulsante "+" nella sezione Sogni in Home per aggiungere un nuovo sogno | Must |
| DM-02 | Bottom sheet Nuovo sogno: campo nome, emoji picker, importo target, data target (opzionale) | Must |
| DM-03 | Validazione: nome e importo target obbligatori; bottone "Salva" disabilitato finché non validi | Must |
| DM-04 | Tap su sogno → schermata Dettaglio con nome, emoji, importo target, data target, barra progresso, importo mancante | Must |
| DM-05 | Da Dettaglio: pulsante "Modifica" che apre un bottom sheet precompilato con i dati del sogno | Must |
| DM-06 | Bottom sheet Modifica: campi nome, emoji, importo target, data target — tutti modificabili | Must |
| DM-07 | Da Dettaglio: pulsante "Elimina" che apre una modale di conferma | Must |
| DM-08 | Eliminazione bloccata se è l'ultimo sogno rimasto: modale di errore "Devi avere almeno un sogno 🌟" | Must |
| DM-09 | Dopo eliminazione confermata: redirect alla Home, lista sogni aggiornata | Must |
| DM-10 | Dopo salvataggio (aggiunta o modifica): bottom sheet si chiude, card aggiornata in tempo reale | Must |
| DM-11 | Utente Free con 1 sogno esistente tappa "+": mostra bottom sheet paywall "Sogni illimitati è una funzionalità Pro" con CTA "Scopri DreamJar Pro" → naviga a Settings | Must |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| 1 solo sogno | Pulsante "Elimina" in Dettaglio visibile ma al tap mostra errore "Devi avere almeno un sogno 🌟" |
| Salvataggio in corso | Bottone "Salva" con spinner, form disabilitato |
| Errore salvataggio | Toast "Non riesco a salvare. Riprova." |
| Data target assente | Campo opzionale — la card mostra solo la barra progresso senza scadenza |
| `saved_amount` = 0 | Barra progresso vuota, importo mancante = target_amount |
| `saved_amount` ≥ `target_amount` | Barra al 100%, stato "Completato 🎉" |

---

## Dipendenze

- **[Dashboard](../epic.md)** — le card sogni (D-06, D-07) vengono estese con le azioni di modifica ed eliminazione
- **Onboarding** — il primo sogno viene creato nell'onboarding (step 5); il dream manager gestisce quelli successivi
