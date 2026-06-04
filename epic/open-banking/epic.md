# Epic: Open Banking — Connessione Conto Bancario

**Stato:** Planned · Giugno 2026 · **Priorità:** Must — v3

> As a Pro user, I want to connect my bank account via Open Banking so that my income and transactions are imported automatically without any manual entry.

---

## Come funziona

Dopo che l'utente ha attivato il piano Pro (→ [epic Upgrade](../upgrade/epic.md)), parte il flusso di connessione bancaria tramite Enable Banking (PSD2). L'utente seleziona la propria banca, si autentica sul portale della banca e autorizza la lettura delle transazioni. Da quel momento stipendio e spese vengono importati automaticamente.

L'utente può ricollegare o scollegare il conto in qualsiasi momento dalla schermata Settings. Se la connessione scade o viene revocata, un banner avvisa e propone la riconnessione.

```
[Checkout Upgrade completato]
        ↓
     Bottom sheet "Collega il tuo conto"
        ↓ "Seleziona la tua banca"
     Widget Enable Banking (selezione istituto + autenticazione)
        ↓ connessione ok
     Toast conferma + Settings aggiornate (stato "Collegata")
        ↓ (in futuro)
     Import automatico transazioni → Dashboard / Budget
```

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

---

## Dipendenze

- **[Upgrade](../upgrade/epic.md)** — l'utente deve essere in piano Pro per accedere a questo flusso; il checkout ok è il trigger per OB-01
- **[Settings](../settings/epic.md)** — card "Piano attivo" ospita i controlli di connessione (OB-06, OB-07, OB-08) e il banner warning (OB-09)
- **[Dashboard](../dashboard/epic.md)** — le transazioni importate alimentano il tracking spese; in v3+ sostituiscono l'inserimento manuale
- **[Budget](../budget/epic.md)** — lo stipendio importato può aggiornare automaticamente il valore in Budget
- **Enable Banking** — widget PSD2 per selezione banca e autenticazione; richiede registrazione AISP presso Banca d'Italia

---

## Rischi e note

> **Registrazione AISP:** per operare come aggregatore bancario in Italia serve autorizzazione Banca d'Italia (6–12 mesi). Va avviato in parallelo alla v2, non dopo. Enable Banking può coprire provvisoriamente l'iter con una licenza passthrough.

> **GDPR:** i dati bancari importati sono dati personali di categoria sensibile. Serve DPA aggiornato con Enable Banking e informativa chiara nel flusso di connessione (OB-02).
