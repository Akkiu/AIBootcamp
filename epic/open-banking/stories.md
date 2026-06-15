# Stories: Open Banking — Connessione Conto Bancario

Sequence consigliata: S1 → S2

**Prerequisito:** l'epic Upgrade (checkout Paddle) deve essere completato prima di implementare queste stories.

---

## S1 — Connessione bancaria post-upgrade

**Goal:** dopo il pagamento del piano Pro, guidare l'utente a collegare il proprio conto bancario tramite Enable Banking.

**Requisiti coperti:** OB-01, OB-02, OB-03, OB-04, OB-05

**Dipendenza:** epic Upgrade S2 (pagamento completato)

---

**Prompt Lovable:**

DreamJar ha un piano Pro che sblocca l'importazione automatica delle transazioni bancarie tramite Open Banking (Enable Banking API).

Dopo che l'utente ha completato il pagamento del piano Pro, apri automaticamente un bottom sheet "Collega il tuo conto".

**Contenuto del bottom sheet:**

Titolo: "Collega il tuo conto"
Sottotitolo: "Seleziona la tua banca per iniziare a importare le transazioni automaticamente."

Illustrazione o icone placeholder di banche comuni.

CTA primaria: "Seleziona la tua banca" → apre il widget Enable Banking per la selezione dell'istituto bancario e l'autenticazione Open Banking.

Link secondario: "Forse più tardi" → chiude il bottom sheet; il piano Pro resta attivo e l'utente può collegarsi in seguito.

**Comportamenti dopo il widget Enable Banking:**

Connessione riuscita:
- Toast: "Conto collegato! Le tue transazioni saranno importate a breve."
- Chiude il bottom sheet
- La card "Piano attivo" in Settings mostra stato connessione "Collegata"

Connessione annullata o fallita:
- Toast: "Connessione non riuscita."
- Link nel toast: "Riprova" → riapre il widget Enable Banking
- Il piano Pro rimane comunque attivo; l'utente può ricollegarsi dalla card "Piano attivo" in Settings

---

## S2 — Gestione connessione e banner scadenza

**Goal:** permettere all'utente Pro di collegare/scollegare il conto in qualsiasi momento e avvisarlo quando la connessione scade.

**Requisiti coperti:** OB-06, OB-07, OB-08, OB-09, OB-10, OB-11

**Dipendenza:** S1 + epic Upgrade S1 (card "Piano attivo" già presente in Settings)

---

**Prompt Lovable:**

Gli utenti DreamJar Pro devono poter gestire la connessione bancaria dalla schermata Settings e ricevere un avviso quando la connessione scade.

**Card "Piano attivo" in Settings — aggiungi:**

Se il conto non è collegato: pulsante "Collega conto" → apre il widget Enable Banking (stesso flusso di S1).

Se il conto è collegato: pulsante "Scollega conto" → dialog di conferma "Sei sicuro? Le transazioni già importate rimarranno." → conferma → rimuove la connessione, stato torna "Non collegata".

**Banner connessione scaduta:**

Se la connessione bancaria scade o viene revocata, mostra in cima a Settings (sopra la card "Piano attivo") un banner:
- Testo: "Connessione bancaria scaduta. Ricollegati per continuare a importare le transazioni."
- CTA: "Ricollegati" → apre il widget Enable Banking
- Icona × per dismissione: il banner torna a ogni apertura di Settings finché l'utente non si ricollega con successo

**Comportamenti riconnessione:**
- Stessi di S1: connessione ok → toast + aggiornamento stato; fallimento → toast con "Riprova"

---

## S3 — Import transazioni bancarie e Inbox

**Goal:** dopo la connessione bancaria, importare automaticamente le transazioni che hanno un match certo e presentare quelle ambigue in un Inbox per la revisione dell'utente.

**Requisiti coperti:** OB-12, OB-13, OB-14, OB-15, OB-16, OB-17, OB-18, OB-19, OB-20, OB-21, OB-22, OB-23, OB-24, OB-25, OB-26, OB-27, OB-28, OB-29, OB-30, OB-31, OB-32, OB-33, OB-34

**Dipendenza:** S1 (conto collegato), epic Budget S1 (recurring_expenses esistenti)

---

**Prompt Lovable:**

DreamJar Pro importa automaticamente le transazioni bancarie tramite Enable Banking. Le transazioni vengono classificate in tre livelli di confidenza e gestite in modo diverso.

**Logica di import (backend/sync):**

Ogni giorno alle 07:00 (e su richiesta manuale), il sistema recupera le nuove transazioni dal conto collegato e applica:

1. **Filtri:** ignora entrate (importo > 0), trasferimenti interni (GIROCONTO, BONIFICO A SE, TOP UP) e duplicati (stessa banca, importo ±10%, data ±2 giorni).

2. **Matching a 3 livelli:**
   - `auto_recurring` — il merchant corrisponde a una spesa ricorrente attiva dell'utente (importo ±5%): auto-import silenzioso. La ricorrente risulta "pagata" nel Calendario. Nessuna notifica push (salvo preferenza "Avvisami anche per import automatici" attiva).
   - `auto_preset` — il merchant è nella lista preset noti (Esselunga, Conad, Netflix, Spotify, Trenitalia, ecc.): auto-import. Incluso nella push aggregata di fine sync.
   - `low` — nessun match: resta in `pending_review` nell'Inbox.

3. **Push aggregata a fine sync** (una sola per utente, rispettando le quiet hours):
   - Solo pending: "Spese dalla banca da rivedere 🔍" / "{N} spese ({€tot}) aspettano un tuo ok"
   - Solo auto-import (se preferenza attiva): "Ho aggiunto {N} spese dalla banca 👀" / "€{tot} scalati dal residuo"
   - Misto: "{N} spese dalla banca 👀" / "{X} importate, {Y} da rivedere"
   - Tap → naviga a /spese tab Inbox

**Schermata /spese — nuovo tab "Inbox":**

Aggiungi un tab "Inbox" alla schermata /spese. Il tab mostra un badge con il numero di transazioni `pending_review`.

Sopra la lista: pulsante "Sincronizza ora" che avvia una sync manuale.

Ogni transazione in lista mostra: nome merchant, importo, data, categoria suggerita (modificabile). Tre azioni:
- **"Importa"** → bottom sheet per confermare o modificare bucket e tipologia → spesa registrata, FtD aggiornato, transazione rimossa dalla lista.
- **"Ignora"** → modale di conferma → transazione scartata, nessuna spesa creata.
- **"È un duplicato"** → transazione marcata come duplicata e rimossa dalla lista, nessuna spesa creata.

Stato vuoto del tab: "Nessuna spesa in attesa" con testo "Le nuove transazioni dal tuo conto appariranno qui".

**Home — banner pending:**

Quando ci sono transazioni in attesa nell'Inbox, mostra sotto al numero "Free to Dream" un banner:
"⚠️ €{tot} da rivedere dalla banca" con link "Apri Inbox" → naviga a /spese tab Inbox.
Il banner scompare quando l'Inbox è vuota.

**Settings > Notifiche — nuovi toggle:**

Aggiungi due toggle nella sezione notifiche delle Impostazioni (visibili solo agli utenti Pro):
- "Notifiche transazioni bancarie" (default attivo): se disattivato, nessuna push per sync bancaria.
- "Avvisami anche per import automatici" (default disattivato): se attivato, ricevi push anche quando le spese vengono importate automaticamente.
