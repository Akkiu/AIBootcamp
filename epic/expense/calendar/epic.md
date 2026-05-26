# Epic: Calendario Spese

**Stato:** To Do · **Priorità:** Should — v1.1

> As a user, I want a calendar view of my recurring expenses so that I can see at a glance when money will leave my account each month and plan ahead.

---

## Come funziona

Una vista calendario accessibile dalla schermata Riepilogo Spese (toggle lista/calendario in alto). Mostra il mese corrente e permette di navigare liberamente verso i mesi futuri e passati.

Ogni giorno con una o più spese ricorrenti pianificate mostra un indicatore visivo. Tappando sul giorno si vedono le spese in dettaglio. Le spese annuali compaiono solo nel mese e giorno configurati.

```
Riepilogo Spese → toggle "Calendario"
    ↓
[Header: mese + totale ricorrenti del mese]
[Griglia mensile]    ← giorni con spese hanno marker
    ↓ tap giorno
[Bottom sheet: lista spese del giorno]
```

---

## Requisiti

| # | Requisito | Priorità |
|---|-----------|----------|
| EC-01 | Toggle lista/calendario in cima alla schermata Riepilogo Spese per passare alla vista calendario | Must |
| EC-02 | Griglia mensile con navigazione ← → tra mesi (passati e futuri) | Must |
| EC-03 | Header del calendario: nome mese + anno, totale spese ricorrenti del mese (es. "Totale ricorrenti: €1.240") | Must |
| EC-04 | Giorni con spese ricorrenti mostrano un marker visivo (dot o badge con importo totale del giorno) | Must |
| EC-05 | Tap su un giorno con spese → bottom sheet con lista delle spese: nome, importo, bucket (emoji + colore) | Must |
| EC-06 | Spese ricorrenti mensili (configurate in Budget) appaiono ogni mese nel giorno configurato | Must |
| EC-07 | Spese ricorrenti annuali appaiono una volta l'anno nel mese e giorno configurati | Must |
| EC-08 | Nel mese corrente, i giorni passati mostrano se la spesa è stata effettivamente registrata (stato "pagata") o è ancora pianificata | Should |
| EC-09 | Stato vuoto: nessuna spesa ricorrente in questo mese → messaggio "Nessuna spesa ricorrente in questo mese" | Must |
| EC-10 | Tap su spesa già pagata nel bottom sheet → rimanda al dettaglio della spesa registrata (bottom sheet ES-2) | Could |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Mese senza spese ricorrenti | Griglia vuota + messaggio placeholder |
| Giorno con spese pianificate | Marker visivo (dot o importo) sul giorno |
| Giorno con spese pagate (mese corrente, passato) | Marker differenziato (es. check o colore diverso) |
| Bottom sheet giorno | Lista spese con nome, importo, bucket |
| Loading | Skeleton loader sulla griglia |

---

## Dipendenze

- **[Budget](../../budget/epic.md)** — fonte dati delle spese ricorrenti mensili e annuali (BU-09/BU-10)
- **[Riepilogo Spese](../summary/epic.md)** — schermata ospite del toggle lista/calendario; il dettaglio spesa (ES-02) è riusato per le spese già pagate
