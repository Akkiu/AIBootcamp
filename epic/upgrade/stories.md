# Stories: DreamJar Pro — Upgrade

Sequence consigliata: S1 → S2

---

## S1 — Card upgrade in Settings

**Goal:** aggiungere la card "DreamJar Pro" in cima alla schermata Impostazioni per gli utenti in piano gratuito; sostituirla con la card "Piano attivo" per gli utenti Pro.

**Requisiti coperti:** UP-01, UP-02, UP-03, UP-04, UP-14, UP-15

---

**Prompt Lovable:**

DreamJar è un'app per gestire budget e risparmi. Stiamo aggiungendo il piano Pro con integrazione bancaria automatica.

Nella schermata **Impostazioni**, aggiungi in cima (prima di qualsiasi altra card) una card "DreamJar Pro" visibile solo agli utenti in piano gratuito.

La card contiene:
- Badge "PRO" nell'angolo superiore destro
- Headline: "Smetti di inserire le spese a mano"
- Sottotitolo: "Collega il tuo conto e importa tutto automaticamente"
- CTA: "Scopri il piano Pro"

Tap sulla card → apre un bottom sheet (non naviga fuori dalla pagina Settings).

Per gli utenti già in piano Pro, la card viene sostituita da una card "Piano attivo" con:
- Piano corrente (es. "Pro mensile" o "Pro annuale")
- Data prossimo rinnovo
- Stato connessione bancaria (collegata / non collegata)
- Link "Gestisci piano" → porta al portale clienti Stripe

---

## S2 — Bottom sheet: presentazione piano e checkout

**Goal:** bottom sheet inline che mostra i benefici del piano Pro, il pricing e avvia il checkout Stripe.

**Requisiti coperti:** UP-05, UP-06, UP-07, UP-08, UP-09, UP-10, UP-11, UP-12, UP-13

**Dipendenza:** S1

---

**Prompt Lovable:**

DreamJar ha un piano Pro a pagamento che sblocca la connessione bancaria automatica. L'upgrade si fa inline dalla schermata Settings tramite bottom sheet.

Implementa il bottom sheet "DreamJar Pro" che si apre quando l'utente tocca la card upgrade.

**Contenuto del bottom sheet:**

Titolo: "DreamJar Pro"

Lista benefici (icone check):
- Connessione automatica al conto bancario
- Import automatico di stipendio e transazioni
- Categorizzazione automatica delle spese
- Nessun inserimento manuale

Selector mensile / annuale:
- Mensile: mostra prezzo/mese
- Annuale: mostra prezzo/anno con badge "Risparmia X%" rispetto al mensile
- Il selector aggiorna il prezzo in tempo reale

Accordion "Come funziona l'Open Banking?":
- Si espande inline (non naviga fuori)
- Testo: "Usiamo l'Open Banking (PSD2) per leggere le tue transazioni. Non vediamo mai le tue credenziali bancarie. I tuoi dati sono protetti e puoi disconnettere il conto in qualsiasi momento."

CTA primaria: "Attiva DreamJar Pro" → avvia Stripe Checkout
Link secondario: "Forse più tardi" → chiude il bottom sheet

**Comportamenti:**
- Durante il checkout: CTA disabilitata con spinner
- Checkout fallito: ritorno al bottom sheet con toast "Pagamento non riuscito. Riprova."
- Checkout ok: chiude il bottom sheet e avvia il flusso di connessione bancaria (epic Open Banking)
