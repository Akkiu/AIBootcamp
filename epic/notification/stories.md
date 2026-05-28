# Stories — Notifiche In-App Spese Ricorrenti

> Ogni story è un prompt autonomo per Lovable.
> Brand system e PRD sono allegati come project context — non vanno ripetuti nel prompt.

---

## NO-1 · Icona campana e centro notifiche

> As a user, I want to see a notification bell in the app that alerts me when a recurring expense is due in the next 3 days so that I'm never caught off guard.

**Prompt Lovable**

DreamJar è un'app di gestione budget personale. Aggiungi un sistema di notifiche in-app per le spese ricorrenti in scadenza.

**Icona campana 🔔** nella top bar, visibile in tutte le schermate principali. Se ci sono notifiche non lette, mostra un badge rosso con il conteggio. Il badge scompare quando tutte le notifiche sono state lette.

**Logica di generazione:** all'apertura dell'app, il sistema calcola quali spese ricorrenti attive hanno scadenza nei prossimi 3 giorni (incluso oggi). Per le spese mensili, la scadenza è il `day_of_month` del mese corrente. Per le spese annuali, la scadenza è il `day_of_month` del `month_of_year` configurato — vengono considerate solo nel mese corretto.

**Tap sull'icona campana** → apre il centro notifiche (bottom sheet o schermata dedicata). La lista mostra le notifiche ordinate dalla più recente in cima. Ogni notifica mostra:
- Titolo "Spesa in arrivo"
- Nome della spesa ricorrente (es. "Affitto")
- Importo (es. "€ 850")
- Data di scadenza relativa (es. "Oggi · 27 mag", "Domani · 28 mag", "Tra 2 giorni · 29 mag")
- Badge bucket con emoji e colore (es. 💸 Spese fisse)

**Tap su una notifica** → segna la notifica come letta e naviga al Calendario Spese sul mese corrente.

**Stato vuoto:** se nessuna spesa è in scadenza nei prossimi 3 giorni, il centro notifiche mostra il messaggio "Nessuna notifica" con sottotitolo "Le spese in arrivo nei prossimi 3 giorni appariranno qui".

---

## NO-2 · Stato letto e filtro spese già pagate

> As a user, I want read notifications to be visually distinct and already-paid expenses to not generate alerts so that the notification center stays relevant.

**Prompt Lovable**

DreamJar — nel centro notifiche (già implementato in NO-1), aggiungi la gestione dello stato letto e il filtro delle spese già pagate.

**Notifiche lette:** le notifiche già aperte tramite tap rimangono visibili nel centro notifiche con stile attenuato (opacità ridotta o colore grigio), così l'utente può rivedere cosa è in scadenza anche dopo averle lette.

**CTA "Segna tutte come lette"** in cima al centro notifiche, visibile solo se ci sono notifiche non lette. Tap → tutte le notifiche passano allo stato letto, il badge sull'icona campana scompare.

**Filtro spese già pagate:** se una spesa ricorrente ha già una spesa registrata nella stessa data (collegata tramite `recurring_expense_id`), la notifica corrispondente non viene generata. Se la spesa viene registrata mentre la notifica è già visibile, la notifica scompare automaticamente dal centro notifiche.

---

## Sequenza

| # | Story | Dipendenze |
|---|-------|------------|
| 1 | NO-1 Icona campana + centro notifiche | BU-09/BU-10 (spese ricorrenti configurate), EC-1 (Calendario Spese già implementato come destinazione) |
| 2 | NO-2 Stato letto + filtro spese pagate | NO-1, ES-2 (registrazione spesa con `recurring_expense_id`) |
