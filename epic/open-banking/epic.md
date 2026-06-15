# Epic: Open Banking — Connessione Conto Bancario

**Stato:** Planned · Giugno 2026 · **Priorità:** Must — v3

> As a Pro user, I want to connect my bank account via Open Banking so that my income and transactions are imported automatically without any manual entry.

---

## Come funziona

Dopo che l'utente ha attivato il piano Pro (→ [epic Upgrade](../upgrade/epic.md)), parte il flusso di connessione bancaria tramite Enable Banking (PSD2). L'utente seleziona la propria banca, si autentica sul portale della banca e autorizza la lettura delle transazioni.

Da quel momento le transazioni bancarie vengono sincronizzate giornalmente (ore 7:00) o su richiesta manuale. Per ciascuna, il sistema applica prima un filtro, poi un matching a tre livelli:

- **Filtrate e ignorate:** entrate (importo > 0), trasferimenti interni (GIROCONTO, BONIFICO A SE, TOP UP, Revolut topup), duplicati (spesa già presente ±2gg e ±10% importo).
- **`auto_recurring`** — merchant corrisponde a una spesa ricorrente attiva (importo ±5%) → **auto-import silenzioso**: la spesa viene registrata, il FtD si aggiorna, la ricorrente risulta "pagata" nel Calendario. Nessuna push, salvo preferenza attivata dall'utente.
- **`auto_preset`** — merchant è in lista preset nota (Esselunga, Conad, Netflix, Spotify…) → **auto-import con push raggruppata** al termine della sync.
- **`low`** — nessun match → transazione accodata nell'**Inbox "Da rivedere"**. Una push aggregata avvisa l'utente.

```
[Transazione arriva dalla banca]
        ↓
   Filtro: entrate / trasferimenti / duplicati → ignorati
        ↓
   Matching
      ├── auto_recurring → auto-import silenzioso → FtD aggiornato
      ├── auto_preset    → auto-import + push raggruppata → FtD aggiornato
      └── low            → Inbox "Da rivedere"
                               ↓
                          Push: "N spese aspettano un tuo ok"
                               ↓ tap "Importa" → assegna bucket → FtD aggiornato
                               ↓ tap "Ignora" → scartata
                               ↓ tap "È un duplicato" → marcata duplicate
```

Quando ci sono transazioni in attesa, un banner compare nella Home sotto al FtD ("⚠️ €X da rivedere dalla banca → Apri Inbox").

L'utente può ricollegare o scollegare il conto in qualsiasi momento da Settings. Se la connessione scade o viene revocata, un banner avvisa e propone la riconnessione.

---

## Requisiti

### Connessione iniziale (post-upgrade)

| # | Requisito | Priorità |
|---|-----------|----------|
| OB-01 | Dopo il pagamento del piano Pro parte automaticamente un bottom sheet "Collega il tuo conto" con CTA "Seleziona la tua banca" | Must |
| OB-02 | Tap su "Seleziona la tua banca" → apertura del widget Enable Banking per selezione istituto e autenticazione Open Banking | Must |
| OB-03 | Connessione riuscita → toast "Conto collegato! Le tue transazioni saranno importate a breve." + chiusura bottom sheet + Settings aggiornate con stato connessione "Collegata" | Must |
| OB-04 | Connessione fallita o annullata → toast "Connessione non riuscita." con link "Riprova" che riapre il widget; il piano Pro rimane attivo | Must |
| OB-05 | L'utente può saltare la connessione in questa fase e ricollegarsi in seguito dalla card "Piano attivo" in Settings | Should |

### Gestione connessione (utente Pro)

| # | Requisito | Priorità |
|---|-----------|----------|
| OB-06 | Dalla card "Piano attivo" in Settings: pulsante "Collega conto" se non collegata, pulsante "Scollega conto" se collegata | Must |
| OB-07 | "Scollega conto" → conferma → rimozione connessione; stato torna a "Non collegata"; le transazioni già importate restano | Should |
| OB-08 | "Collega conto" → apre il widget Enable Banking (stesso flusso di OB-02) | Must |

### Connessione scaduta o revocata

| # | Requisito | Priorità |
|---|-----------|----------|
| OB-09 | Se la connessione bancaria scade o viene revocata, mostra in cima a Settings un banner: "Connessione bancaria scaduta. Ricollegati per continuare a importare le transazioni." | Should |
| OB-10 | Il banner ha una CTA "Ricollegati" → apre il widget Enable Banking | Should |
| OB-11 | Il banner è dismissibile (icona ×) ma ritorna a ogni apertura di Settings finché l'utente non si ricollega | Should |

### Filtro e deduplicazione

| # | Requisito | Priorità |
|---|-----------|----------|
| OB-12 | Transazioni con importo > 0 (entrate, stipendio, cashback) vengono ignorate automaticamente | Must |
| OB-13 | Transazioni riconducibili a trasferimenti interni (GIROCONTO, BONIFICO A SE, TOP UP) vengono ignorate | Must |
| OB-14 | Deduplicazione: se esiste già una spesa dello stesso utente con importo ±10% e data ±2 giorni dalla stessa banca, la transazione viene marcata `duplicate` e non importata | Must |

### Matching e auto-import

| # | Requisito | Priorità |
|---|-----------|----------|
| OB-15 | Match `auto_recurring`: merchant normalizzato corrisponde a una `recurring_expenses` attiva con importo ±5% → auto-import silenzioso; la ricorrente risulta "pagata" nel Calendario; nessuna push (salvo `bank_auto_import_notify = true`) | Must |
| OB-16 | Match `auto_preset`: merchant normalizzato è in lista preset noti (es. Esselunga, Conad, Netflix, Spotify) → auto-import; incluso nella push raggruppata di fine sync | Must |
| OB-17 | Confidence `low` (nessun match): transazione rimane `pending_review` nell'Inbox | Must |
| OB-18 | Sync giornaliera automatica alle 07:00 per ogni conto collegato attivo | Must |
| OB-19 | Pulsante "Sincronizza ora" nel tab Inbox di /spese: avvia sync manuale e aggiorna la lista | Should |

### Push notification — sync bancaria

| # | Requisito | Priorità |
|---|-----------|----------|
| OB-20 | Una sola push per utente per sessione di sync, aggregata | Must |
| OB-21 | Copy — solo pending: titolo "Spese dalla banca da rivedere 🔍", body "{N} spese ({€tot}) aspettano un tuo ok" | Must |
| OB-22 | Copy — solo auto-import (se `bank_auto_import_notify = true`): titolo "Ho aggiunto {N} spese dalla banca 👀", body "€{tot} scalati dal residuo" | Should |
| OB-23 | Copy — misto: titolo "{N} spese dalla banca 👀", body "{X} importate, {Y} da rivedere" | Must |
| OB-24 | Tap sulla push → deep link a /spese tab Inbox | Must |
| OB-25 | Le push rispettano le quiet hours dell'utente; ogni invio viene loggato in `notification_dispatch_log` con `event_type = 'bank_transactions_sync'` | Should |

### Inbox — Da rivedere

| # | Requisito | Priorità |
|---|-----------|----------|
| OB-26 | Tab "Inbox" in /spese con badge counter delle transazioni `pending_review`; badge visibile anche sull'icona di navigazione della schermata | Must |
| OB-27 | Ogni transazione in inbox mostra: nome merchant, importo, data, categoria suggerita (modificabile), azioni "Importa" / "Ignora" / "È un duplicato" | Must |
| OB-28 | Tap "Importa" → bottom sheet per confermare/modificare bucket e tipologia → spesa registrata, FtD aggiornato, transazione rimossa da inbox | Must |
| OB-29 | Tap "Ignora" → modale conferma → transazione scartata (status `ignored`); nessuna spesa creata | Must |
| OB-30 | Tap "È un duplicato" → transazione marcata `duplicate` e rimossa da inbox senza creare spesa | Should |
| OB-31 | Stato vuoto: "Nessuna spesa in attesa" con testo "Le nuove transazioni dal tuo conto appariranno qui" | Must |

### Dashboard Home

| # | Requisito | Priorità |
|---|-----------|----------|
| OB-32 | Quando esistono transazioni `pending_review`, mostra sotto al FtD un banner: "⚠️ €{tot} da rivedere dalla banca" con link "Apri Inbox" → naviga a /spese tab Inbox | Must |

### Preferenze notifiche bancarie (Settings)

| # | Requisito | Priorità |
|---|-----------|----------|
| OB-33 | Toggle "Notifiche transazioni bancarie" in Settings > Notifiche (default ON): se OFF, nessuna push per sync bancaria | Must |
| OB-34 | Toggle "Avvisami anche per import automatici" in Settings > Notifiche (default OFF): se ON, riceve push anche per le transazioni auto-importate | Should |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Post-upgrade (primo accesso) | Bottom sheet "Collega il tuo conto" aperto automaticamente |
| Connessione in corso | Widget Enable Banking attivo |
| Connessione ok | Toast conferma, Settings mostra stato "Collegata" |
| Connessione fallita / annullata | Toast errore con link "Riprova" |
| Banca collegata (stato stabile) | Card "Piano attivo" con stato verde "Collegata" |
| Banca non collegata (Piano Pro attivo) | Card "Piano attivo" con warning e CTA "Collega conto" |
| Connessione scaduta / revocata | Banner warning in cima a Settings |
| Transazione `auto_recurring` | Spesa registrata silenziosamente, FtD aggiornato, ricorrente "pagata" nel Calendario |
| Transazione `auto_preset` | Spesa registrata, FtD aggiornato, inclusa nella push aggregata di fine sync |
| Transazione `low` / pending | Badge Inbox aggiornato, push aggregata inviata |
| Transazione `duplicate` | Ignorata, nessuna spesa creata, nessuna push |
| Inbox vuota | Placeholder "Nessuna spesa in attesa" |
| Pending_review presenti | Banner in Home sotto FtD con totale €X e link Inbox |

---

## Dipendenze

- **[Upgrade](../upgrade/epic.md)** — l'utente deve essere in piano Pro per accedere a questo flusso; il checkout ok è il trigger per OB-01
- **[Settings](../settings/epic.md)** — card "Piano attivo" ospita i controlli di connessione (OB-06, OB-07, OB-08) e il banner warning (OB-09)
- **[Dashboard](../dashboard/epic.md)** — banner pending_review (OB-32) mostrato sotto al FtD; le auto-import aggiornano il FtD in tempo reale
- **[Budget](../budget/epic.md)** — `recurring_expenses` è la fonte dati per il matching `auto_recurring`
- **[Calendario Spese](../expense/calendar/epic.md)** — le ricorrenti auto-importate risultano "pagate" nel Calendario
- **[Notifiche](../notification/epic.md)** — push bancarie si appoggiano all'infrastruttura notifiche esistente; quiet hours e dispatch log condivisi
- **[Settings](../settings/epic.md)** — toggle OB-33/OB-34 aggiunti in Settings > Notifiche
- **Enable Banking** — widget PSD2 per selezione banca, autenticazione e sync transazioni; richiede registrazione AISP presso Banca d'Italia

---

## Rischi e note

> **Registrazione AISP:** per operare come aggregatore bancario in Italia serve autorizzazione Banca d'Italia (6–12 mesi). Va avviato in parallelo alla v2, non dopo. Enable Banking può coprire provvisoriamente l'iter con una licenza passthrough.

> **GDPR:** i dati bancari importati sono dati personali di categoria sensibile. Serve DPA aggiornato con Enable Banking e informativa chiara nel flusso di connessione (OB-02).
