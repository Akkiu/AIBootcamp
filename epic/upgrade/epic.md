# Epic: DreamJar Pro — Upgrade

**Stato:** Done · Giugno 2026 · **Priorità:** Must — v3

> As a free user, I want to upgrade to DreamJar Pro directly from Settings so that I can unlock automatic bank sync and stop entering expenses manually.

---

## Come funziona

Il piano gratuito prevede inserimento manuale di stipendio e spese. Il piano Pro sblocca la sincronizzazione automatica con il conto bancario.

Il punto di ingresso è una card prominente nella schermata Impostazioni. Toccandola si apre un bottom sheet inline (senza cambio di pagina) con benefici, pricing e la CTA di acquisto. Dopo il pagamento il piano utente viene aggiornato e parte il flusso di connessione bancaria (→ [epic Open Banking](../open-banking/epic.md)).

```
Settings
  └─ [Card "Passa a DreamJar Pro"]
        ↓ tap
     Bottom sheet: benefici + pricing + selector mensile/annuale
        ↓ "Attiva DreamJar Pro"
     Checkout Stripe
        ↓ pagamento ok
     → avvia epic Open Banking (connessione conto)
```

---

## Requisiti

### Card upgrade in Settings

| # | Requisito | Priorità |
|---|-----------|----------|
| UP-01 | Card "DreamJar Pro" visibile in Settings per gli utenti in piano gratuito, posizionata in cima prima delle card account | Must |
| UP-02 | La card mostra: badge "PRO", headline "Smetti di inserire le spese a mano", sottotitolo "Collega il tuo conto e importa tutto automaticamente", CTA "Scopri il piano Pro" | Must |
| UP-03 | Tap sulla card → apre bottom sheet inline (non naviga fuori dalla pagina Settings) | Must |
| UP-04 | Per gli utenti Pro la card è sostituita da una card "Piano attivo" con: piano corrente (mensile/annuale), data prossimo rinnovo, stato connessione bancaria, link "Gestisci piano" | Must |

### Bottom sheet: presentazione piano

| # | Requisito | Priorità |
|---|-----------|----------|
| UP-05 | Bottom sheet mostra: titolo "DreamJar Pro", lista benefici, prezzo, CTA "Attiva DreamJar Pro" | Must |
| UP-06 | Lista benefici (icone check): ① Connessione automatica al conto bancario ② Import automatico stipendio e transazioni ③ Categorizzazione automatica delle spese ④ Nessun inserimento manuale | Must |
| UP-07 | Selector mensile / annuale: il prezzo si aggiorna in tempo reale; il piano annuale mostra il risparmio percentuale rispetto al mensile | Should |
| UP-08 | Link "Come funziona l'Open Banking?" → espande accordion inline con testo: "Usiamo l'Open Banking (PSD2) per leggere le tue transazioni. Non vediamo mai le tue credenziali bancarie. I tuoi dati sono protetti e puoi disconnettere il conto in qualsiasi momento." | Should |
| UP-09 | Pulsante "Attiva DreamJar Pro" → avvia il checkout Stripe | Must |
| UP-10 | Link "Forse più tardi" → chiude il bottom sheet senza azione | Must |

### Checkout

| # | Requisito | Priorità |
|---|-----------|----------|
| UP-11 | Il checkout è gestito tramite Stripe Checkout (redirect o embedded) | Must |
| UP-12 | Pagamento fallito → ritorno al bottom sheet con toast "Pagamento non riuscito. Riprova." | Must |
| UP-13 | Pagamento ok → aggiornamento immediato del piano utente e avvio dell'epic [Open Banking](../open-banking/epic.md) (flusso connessione conto) | Must |

### Gestione piano (utente Pro)

| # | Requisito | Priorità |
|---|-----------|----------|
| UP-14 | Card "Piano attivo" in Settings: piano corrente, data prossimo rinnovo, stato connessione bancaria | Must |
| UP-15 | Link "Gestisci piano" → porta al portale clienti Stripe per disdetta o modifica abbonamento | Must |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Piano gratuito | Card "Passa a DreamJar Pro" in cima a Settings |
| Bottom sheet aperto | Card dimmed in background, sheet visibile |
| Checkout in corso | CTA disabilitata con spinner |
| Pagamento fallito | Ritorno al sheet con toast di errore |
| Pagamento ok | Sheet chiuso, avvia flusso Open Banking |
| Piano Pro attivo | Card "Piano attivo" al posto della card upgrade |

---

## Design notes

- La card upgrade deve essere visivamente distinta ma non aggressiva: colore primario del brand con gradiente sottile, non rosso o arancione.
- Il prezzo va mostrato in modo trasparente, senza asterischi nascosti.
- Il bottom sheet deve trasmettere sicurezza: nessun gergo tecnico o bancario.

---

## Dipendenze

- **[Settings](../settings/epic.md)** — la card Pro è aggiunta alla schermata Impostazioni
- **[Open Banking](../open-banking/epic.md)** — il flusso connessione conto parte immediatamente dopo il pagamento ok
- **Stripe** — gestione abbonamento (mensile/annuale), portale clienti, webhook per aggiornamento stato piano
