# Epic: Registrazione Spese Manuali

**Stato:** Draft · Maggio 2026 · **Priorità:** Should — v1.1

> As a user, I want to log what I've spent so that I always know how much is actually left for my dreams.

---

## Come funziona

L'utente aggiunge una spesa indicando importo, categoria (uno dei 4 bucket) e un nome opzionale. Ogni spesa viene registrata nel bucket corrispondente e il calcolo del "Free to Dream" si aggiorna in tempo reale.

Il **Free to Dream** diventa un saldo dinamico: parte dall'allocazione iniziale dell'onboarding e decresce man mano che vengono registrate spese nel mese corrente.

```
Home → tap "+" → bottom sheet → importo + bucket + nome → Salva
                                                            ↓
                               bucket aggiornato · Free to Dream aggiornato
```

Ogni bucket mostra tre valori: **budget** (allocazione onboarding) · **speso** (somma spese registrate) · **rimanente**. Se le spese superano il budget del bucket, l'eccesso erode direttamente il Free to Dream.

Le spese sono mensili: a inizio mese il contatore riparte da zero, ma lo storico rimane consultabile.

---

## Requisiti

| # | Requisito | Priorità |
|---|-----------|----------|
| EX-01 | Pulsante "+" flottante (FAB) sulla Home per aggiungere una spesa | Must |
| EX-02 | Bottom sheet: campo importo (numpad), selezione bucket (4 opzioni con emoji e colore), campo nome/descrizione opzionale, data (default oggi, modificabile) | Must |
| EX-03 | Validazione: importo > 0, bucket obbligatorio; bottone "Salva" disabilitato finché non sono validi | Must |
| EX-04 | Salvataggio → chiusura sheet + aggiornamento immediato del bucket e del Free to Dream | Must |
| EX-05 | Ogni bucket card in Home mostra: budget allocato, importo speso questo mese, rimanente | Must |
| EX-06 | Se speso > budget del bucket: bucket evidenziato in rosso, il surplus riduce il Free to Dream | Must |
| EX-07 | Tap su bucket card → schermata dettaglio con lista spese del mese (data, nome, importo) | Should |
| EX-08 | Da dettaglio bucket: pulsante "+" per aggiungere una spesa già pre-selezionata su quel bucket | Should |
| EX-09 | Da dettaglio bucket: eliminazione spesa con swipe o press lungo → conferma → ricalcolo | Should |
| EX-10 | Reset mensile automatico: a inizio mese "speso" torna a zero; lo storico dei mesi precedenti è accessibile | Must |
| EX-11 | Feedback visivo post-salvataggio: toast "Spesa aggiunta 👍" (non bloccante) | Should |

---

## Free to Dream — logica di aggiornamento

| Scenario | Effetto sul Free to Dream |
|----------|--------------------------|
| Spesa entro il budget del bucket | Nessun impatto diretto; il bucket mostra il rimanente |
| Spesa che porta il bucket oltre budget | L'eccesso viene sottratto dal Free to Dream |
| Eliminazione di una spesa | Ricalcolo immediato |
| Fine mese / reset | Free to Dream torna al valore iniziale onboarding |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Nessuna spesa registrata | Bucket mostra solo il budget, "speso €0" |
| Bucket in pareggio | Layout normale, barra progresso al 100% del budget |
| Bucket in rosso (speso > budget) | Card evidenziata in corallo, Free to Dream ridotto |
| Free to Dream < 0 | Hero in corallo (già gestito in [Dashboard](epic.md)) |
| Salvataggio in corso | Bottone "Salva" con spinner, form disabilitato |
| Errore di salvataggio | Toast "Errore nel salvataggio. Riprova." |

---

## Dipendenze

- **[Dashboard](epic.md)** — le bucket card (D-02) vengono estese con i dati di spesa; il Free to Dream hero (D-01) si aggiorna
- **Onboarding** — fornisce i budget iniziali per ciascun bucket (base di partenza del calcolo)
- **Goals** — le spese verso obiettivi (bucket "Obiettivi") si riflettono sul progresso dei goal
