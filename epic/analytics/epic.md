# Epic: Analytics

**Stato:** Done · **Priorità:** Should — v1.1

> As a user, I want to see charts of my monthly expenses broken down by category and typology so that I can understand where my money actually goes.

---

## Come funziona

Una sezione "Analytics 📊" embedded direttamente nella Dashboard, sotto le bucket card. Mostra le spese del mese corrente raggruppate per tipologia.

> **Divergenza dalla spec originale:** la spec prevedeva un tab "Statistiche" separato con donut chart per bucket, selettore mese e sezione Coach AI. Lovable ha implementato una versione più leggera embedded nella Dashboard.

```
Dashboard
    ↓
[Sezione Analytics 📊]
[Totale mese + numero tipologie]
[Lista tipologie con barre proporzionali e importo]   ← ordinate per importo desc
[Stato vuoto se nessuna spesa]
```

---

## Requisiti

| # | Requisito | Priorità | Stato |
|---|-----------|----------|-------|
| AN-01 | Sezione "Analytics 📊" embedded nella Dashboard, sotto le bucket card | Must | Built |
| AN-02 | Totale speso nel mese corrente + numero di tipologie in intestazione sezione | Must | Built |
| AN-03 | Lista tipologie con barra orizzontale proporzionale al valore massimo, emoji, nome, contatore spese, importo | Must | Built |
| AN-04 | Barre colorate con il colore del bucket di appartenenza della tipologia | Must | Built |
| AN-05 | Tipologie ordinate per importo decrescente | Should | Built |
| AN-06 | Stato vuoto: "Nessuna spesa ancora questo mese 🌱" | Must | Built |
| AN-07 | Tab "Statistiche" separato con selettore mese e navigazione storico | Could | Planned |
| AN-08 | Grafico a torta/anello per bucket con breakdown espandibile | Could | Planned |
| AN-09 | Sezione Coach AI (solo Pro) con analisi mensile | Could | Planned |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Mese con spese | Grafico + lista bucket con dati |
| Mese senza spese | Stato vuoto con placeholder |
| Bucket espanso | Lista tipologie visibile sotto il bucket |
| Bucket collassato | Solo riga riepilogativa del bucket |
| Loading | Skeleton loader su grafico e lista |
| Errore fetch | Banner "Impossibile caricare i dati. Riprova." |

---

## Dipendenze

- **[Registrazione Spese Manuali](../dashboard/bucket-manager/tracking/epic-expense-tracking.md)** — fonte dati delle spese registrate (`expenses` + `expense_typologies`)
- **[Budget](../budget/epic.md)** — fonte degli importi allocati per bucket (usati come riferimento nelle barre di avanzamento)
- **[Riepilogo Spese](../expense/summary/epic.md)** — condivide lo stesso ciclo mensile e la stessa fonte dati
- **[Dashboard](../dashboard/epic.md)** — la mini-donut (D-13) in Home è il punto di ingresso verso questo tab; condivide gli stessi dati e colori bucket
- **[Coach AI](../coach/epic.md)** — la sezione Coach (AN-14…AN-17) è ospitata in /analytics; è la destinazione della CTA "Approfondisci" nella hero card Coach in Home
