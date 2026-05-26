# Epic: Budget

**Stato:** To Do · **Priorità:** Should — v1.1

> As a user, I want a dedicated place to manage my budget allocations and recurring expenses so that I can keep my financial setup accurate as my life changes.

---

## Come funziona

Il tab Budget è l'area di configurazione finanziaria dell'app. Ha tre sezioni:

1. **Stipendio** — importo mensile netto modificabile, mostrato in cima come base di tutti i calcoli.
2. **Allocazioni bucket** — mostra come lo stipendio è distribuito sui 6 bucket; l'utente può modificare gli importi.
3. **Spese ricorrenti** — lista delle spese ricorrenti mensili (affitto, abbonamenti, rate, ecc.) che alimentano il bucket "Spese fisse". L'utente può aggiungerne di nuove, modificare importo/nome/giorno, ed eliminarle.

```
Bottom nav → "Budget"
    ↓
[Stipendio]            ← importo mensile netto · icona modifica
[Allocazioni]          ← importi bucket modificabili, % sul reddito
[Spese ricorrenti]     ← lista voci ricorrenti · pulsante "+"
```

Quando lo stipendio cambia, le percentuali sui bucket si aggiornano automaticamente ma gli importi assoluti restano fissi — il Free to Dream assorbe la variazione. Quando una spesa ricorrente cambia, il sistema ricalcola automaticamente i bucket variabili per mantenere il totale allineato allo stipendio (vedi logica di ricalcolo).

---

## Requisiti

### Stipendio

| # | Requisito | Priorità |
|---|-----------|----------|
| BU-01 | Card "Stipendio mensile netto" in cima alla schermata con importo corrente e icona modifica | Must |
| BU-02 | Tap sulla card → bottom sheet con importo modificabile (numpad) e preview del nuovo Free to Dream | Must |
| BU-03 | Salvataggio → aggiornamento immediato delle % sui bucket card e del Free to Dream in Home; gli importi assoluti dei bucket restano invariati | Must |

### Allocazioni bucket

| # | Requisito | Priorità |
|---|-----------|----------|
| BU-04 | Sezione "Allocazioni": 6 card con nome bucket, emoji, importo allocato e % sul reddito mensile | Must |
| BU-05 | Tap su una card → bottom sheet con importo modificabile (numpad) | Must |
| BU-06 | Modifica importo bucket → preview impatto su Free to Dream prima del salvataggio | Must |
| BU-07 | Salvataggio → aggiornamento immediato delle card e del Free to Dream in Home | Must |
| BU-08 | Il bucket Obiettivi non è modificabile da questa sezione (gestito tramite Goals) | Must |

### Spese ricorrenti

| # | Requisito | Priorità |
|---|-----------|----------|
| BU-09 | Sezione "Spese ricorrenti": lista delle voci ricorrenti con nome, importo e giorno del mese | Must |
| BU-10 | Pulsante "+" per aggiungere una nuova spesa ricorrente: nome, importo, giorno del mese | Must |
| BU-11 | Tap su una voce → bottom sheet con nome, importo (numpad) e giorno del mese modificabili | Must |
| BU-12 | Preview del ricalcolo nel bottom sheet: mostra i nuovi importi dei bucket variabili con variazione (+/−) prima del salvataggio | Should |
| BU-13 | Salvataggio → ricalcolo automatico dei bucket variabili (Svago, Imprevisti, Utenze, Altro) in proporzione; Obiettivi e Free to Dream restano invariati | Must |
| BU-14 | Se il ricalcolo porta un bucket variabile sotto €0: salvataggio bloccato + messaggio "La variazione è troppo grande. Rivedi la tua allocazione." | Must |
| BU-15 | Eliminazione spesa ricorrente con swipe → conferma → ricalcolo automatico (Δ negativo, i bucket variabili aumentano proporzionalmente) | Should |
| BU-16 | Stato vuoto sezione "Spese ricorrenti": placeholder + CTA "Aggiungi la tua prima spesa ricorrente" | Must |
| BU-17 | Feedback visivo post-salvataggio: toast "Budget aggiornato 👍" | Should |

---

## Logica di ricalcolo (spese ricorrenti)

Quando una spesa ricorrente cambia di Δ, la variazione è distribuita proporzionalmente sui 4 bucket variabili in base alla loro quota sul pool variabile totale:

```
pool_variabile = svago + imprevisti + utenze + altro
nuovo_bucket_i = bucket_i − (bucket_i / pool_variabile) × Δ
```

Obiettivi e Free to Dream restano entrambi invariati.

| Scenario | Comportamento |
|----------|---------------|
| Δ positivo (nuova spesa o aumento) | Bucket variabili diminuiscono proporzionalmente |
| Δ negativo (eliminazione o riduzione) | Bucket variabili aumentano proporzionalmente |
| Pool variabile = €0 | Salvataggio bloccato: "Non c'è budget variabile da ridistribuire." |
| Ricalcolo porta un bucket < €0 | Salvataggio bloccato con avviso |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Normale | Entrambe le sezioni visibili con dati |
| Nessuna spesa ricorrente | Placeholder + CTA nella sezione "Spese ricorrenti" |
| Modifica valida | Preview ricalcolo, bottone "Salva" attivo |
| Importo invariato | Bottone "Salva" disabilitato |
| Ricalcolo impossibile | Avviso inline, salvataggio bloccato |
| Salvataggio in corso | Spinner, form disabilitato |
| Errore di salvataggio | Toast "Errore. Riprova." |

---

## Dipendenze

- **[Dashboard](../dashboard/epic.md)** — i bucket card (D-04) e il Free to Dream hero (D-02) si aggiornano dopo ogni modifica; la sezione "In arrivo" (D-08) legge le stesse spese ricorrenti
- **[Riepilogo Spese](../expense/summary/epic.md)** — la sezione "In arrivo questo mese" è alimentata dalle stesse spese ricorrenti gestite qui
- **Onboarding** — i valori iniziali dei bucket e le prime spese ricorrenti vengono inseriti durante l'onboarding; il Budget tab li rende modificabili in seguito
- **Goals** — il bucket Obiettivi è gestito esclusivamente tramite l'epic Goals

> **Nota:** questa epic assorbe e sostituisce [epic-edit-fixed-expenses.md](../dashboard/bucket-manager/tracking/epic-edit-fixed-expenses.md), che copriva la stessa logica di modifica/ricalcolo ma senza una schermata dedicata.
