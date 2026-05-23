# Epic: Registrazione Spese Manuali

**Stato:** Built · Maggio 2026 · **Priorità:** Should — v1.1

> As a user, I want to log what I've spent so that I always know how much is actually left for my dreams.

---

## Come funziona

L'utente aggiunge una spesa indicando importo, bucket, **tipologia** (es. "Cena", "Aperitivo", "Dentista") e **data in cui è stata effettuata** (di default oggi, modificabile). La tipologia è un'etichetta riutilizzabile: l'app ne suggerisce alcune preset, ma l'utente può crearne di nuove che tornano disponibili per le spese future.

Il **Free to Dream** diventa un saldo dinamico: parte dall'allocazione iniziale dell'onboarding e decresce man mano che vengono registrate spese nel mese corrente.

```
Home → tap "+" → bottom sheet → importo + bucket + tipologia + data (+ nota opzionale) → Salva
                                                                                     ↓
                                              bucket aggiornato · Free to Dream aggiornato
```

Ogni bucket mostra tre valori: **budget** (allocazione onboarding) · **speso** (somma spese registrate) · **rimanente**. Se le spese superano il budget del bucket, l'eccesso erode direttamente il Free to Dream.

Le spese sono mensili: a inizio mese il contatore riparte da zero, ma lo storico rimane consultabile.

### Tipologie di spesa

Le tipologie sono etichette personalizzabili legate a un bucket di default. Vengono proposte nel bottom sheet come chip selezionabili.

- **Preset di sistema** (non eliminabili): Cena fuori 🍽️, Aperitivo 🥂, Dentista 🦷, Spesa supermercato 🛒, Carburante ⛽, Farmacia 💊, Trasporti 🚌, Abbigliamento 👗
- **Custom utente**: l'utente può aggiungere nuove tipologie direttamente dal bottom sheet digitando un nome. La nuova tipologia viene salvata e riappare nelle spese successive.

---

## Requisiti

| # | Requisito | Priorità |
|---|-----------|----------|
| EX-01 | Pulsante "+" flottante (FAB) sulla Home per aggiungere una spesa | Must |
| EX-02 | Bottom sheet: campo importo (numpad), selezione bucket (6 opzioni con emoji e colore: Spese fisse 💸, Svago 🎉, Imprevisti 🛡️, Utenze ⚡, Altro 📦, Obiettivi 🌍), data (default oggi, modificabile) | Must |
| EX-03 | Nel bottom sheet, dopo aver selezionato il bucket, mostrare le tipologie disponibili come chip orizzontali scrollabili, filtrate per quel bucket (preset + custom utente) | Must |
| EX-04 | L'utente può creare una nuova tipologia direttamente dal bottom sheet: campo di testo "Aggiungi tipologia…" — al salvataggio la nuova tipologia viene persistita e riappare nelle prossime spese | Must |
| EX-05 | Campo nota/descrizione opzionale, distinto dalla tipologia | Should |
| EX-06 | Validazione: importo > 0 e bucket obbligatori; tipologia consigliata ma non bloccante; bottone "Salva" disabilitato finché importo e bucket non sono validi | Must |
| EX-07 | Salvataggio → chiusura sheet + aggiornamento immediato del bucket e del Free to Dream | Must |
| EX-08 | Ogni bucket card in Home mostra: budget allocato, importo speso questo mese, rimanente | Must |
| EX-09 | Se speso > budget del bucket: bucket evidenziato in errore, il surplus riduce il Free to Dream | Must |
| EX-10 | Tap su bucket card → schermata dettaglio con lista spese del mese (data, tipologia con emoji, nota, importo) | Should |
| EX-11 | Da dettaglio bucket: pulsante "+" per aggiungere una spesa già pre-selezionata su quel bucket | Should |
| EX-12 | Da dettaglio bucket: eliminazione spesa con swipe → conferma → ricalcolo | Should |
| EX-13 | Reset mensile automatico: a inizio mese "speso" torna a zero; lo storico dei mesi precedenti è accessibile | Must |
| EX-14 | Feedback visivo post-salvataggio: toast "Spesa aggiunta 👍" (non bloccante) | Should |

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
| Bucket in rosso (speso > budget) | Card evidenziata in errore, Free to Dream ridotto |
| Free to Dream < 0 | Hero in errore (già gestito in [Dashboard](../epic.md)) |
| Nessuna tipologia disponibile per il bucket selezionato | Mostra solo il campo "Aggiungi tipologia…" |
| Salvataggio in corso | Bottone "Salva" con spinner, form disabilitato |
| Errore di salvataggio | Toast "Errore nel salvataggio. Riprova." |

---

## Dipendenze

- **[Dashboard](epic.md)** — le bucket card (D-02) vengono estese con i dati di spesa; il Free to Dream hero (D-01) si aggiorna
- **Onboarding** — fornisce i budget iniziali per ciascun bucket (base di partenza del calcolo)
- **Goals** — le spese verso obiettivi (bucket "Obiettivi") si riflettono sul progresso dei goal
