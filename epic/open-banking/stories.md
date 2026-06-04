# Stories: Open Banking — Connessione Conto Bancario

Sequence consigliata: S1 → S2

**Prerequisito:** l'epic Upgrade (checkout Stripe) deve essere completato prima di implementare queste stories.

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
