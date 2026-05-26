# Epic: Notifiche In-App Spese Ricorrenti

**Stato:** To Do · **Priorità:** Should — v1.1

> As a user, I want to receive in-app notifications when a recurring expense is approaching so that I'm not caught off guard when money leaves my account.

---

## Come funziona

Un centro notifiche accessibile dall'icona campana nella top bar. Ogni volta che una spesa ricorrente è in scadenza nei prossimi 3 giorni, viene generata una notifica in-app. Le notifiche possono essere lette e dismesse dall'utente.

Un badge rosso sull'icona campana indica il numero di notifiche non lette.

```
Top bar → icona 🔔 (con badge se ci sono notifiche non lette)
    ↓
[Centro notifiche]     ← lista notifiche, ordinate dalla più recente
    ↓ tap notifica
Segna come letta → naviga al Calendario Spese del mese corrente
```

Le notifiche sono generate automaticamente dal sistema ogni giorno in base alle spese ricorrenti attive (`recurring_expenses.active = true`) con `day_of_month` nei 3 giorni successivi alla data corrente. Le spese annuali seguono la stessa logica ma vengono considerate solo nel mese configurato.

---

## Requisiti

| # | Requisito | Priorità |
|---|-----------|----------|
| NO-01 | Icona 🔔 nella top bar dell'app, visibile in tutte le schermate principali | Must |
| NO-02 | Badge rosso sull'icona con il conteggio delle notifiche non lette; nascosto se non ci sono notifiche non lette | Must |
| NO-03 | Tap sull'icona → apre il centro notifiche (bottom sheet o schermata dedicata) | Must |
| NO-04 | Centro notifiche: lista notifiche ordinate per data decrescente (più recente in cima) | Must |
| NO-05 | Ogni notifica mostra: titolo "Spesa in arrivo", nome spesa ricorrente, importo, data di scadenza (es. "Domani · 28 mag"), badge bucket | Must |
| NO-06 | Notifiche generate automaticamente per le spese ricorrenti con scadenza nei prossimi 3 giorni | Must |
| NO-07 | Tap su una notifica → segna come letta + naviga al Calendario Spese sul mese corrente | Must |
| NO-08 | CTA "Segna tutte come lette" in cima al centro notifiche | Should |
| NO-09 | Notifiche già lette rimangono visibili nel centro notifiche con stile attenuato (per consultazione storica del giorno corrente) | Should |
| NO-10 | Stato vuoto del centro notifiche: "Nessuna notifica" con messaggio "Le spese in arrivo nei prossimi 3 giorni appariranno qui" | Must |
| NO-11 | Le notifiche relative a spese già sostenute (presenti in `expenses` con data corrispondente) non vengono generate o vengono rimosse automaticamente | Should |

---

## Logica di generazione

Le notifiche sono calcolate lato client all'apertura dell'app, confrontando la data corrente con `day_of_month` delle spese ricorrenti attive:

```
oggi = data corrente
per ogni recurring_expense (active = true):
  se frequency = monthly:
    scadenza = giorno <day_of_month> del mese corrente
  se frequency = annual:
    scadenza = giorno <day_of_month> del mese <month_of_year> dell'anno corrente
  se scadenza è nei prossimi 3 giorni (incluso oggi):
    genera notifica (se non già presente e non già pagata)
```

Non serve una tabella persistita: le notifiche sono computate al volo e lo stato "letta/non letta" è tracciato localmente o in una tabella leggera.

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Nessuna notifica | Icona campana senza badge, centro notifiche con placeholder |
| Notifiche non lette | Badge rosso con conteggio, lista notifiche evidenziate |
| Notifiche lette | Badge scompare, notifiche visibili ma attenuate |
| Spesa già pagata | Notifica non generata o rimossa automaticamente |

---

## Dipendenze

- **[Budget](../budget/epic.md)** — fonte dati delle spese ricorrenti attive (BU-09/BU-10); `frequency` e `month_of_year` per le annuali
- **[Calendario Spese](../expense/calendar/epic.md)** — destinazione del tap su notifica
- **[Riepilogo Spese](../expense/summary/epic.md)** — cross-reference per determinare se una ricorrente è già stata pagata (EC-08)
