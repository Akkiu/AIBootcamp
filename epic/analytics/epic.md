# Epic: Analytics

**Stato:** To Do · **Priorità:** Should — v1.1

> As a user, I want to see charts of my monthly expenses broken down by category and typology so that I can understand where my money actually goes.

---

## Come funziona

Un tab dedicato "Statistiche" nella bottom navigation. Mostra i dati di spesa del mese corrente attraverso due livelli di dettaglio:

1. **Per bucket** — quanto ho speso in ciascuna categoria (Svago, Utenze, Spese fisse, Imprevisti, Altro) rispetto al budget allocato.
2. **Per tipologia** — suddivisione delle spese all'interno di ciascun bucket per tipologia (es. Ristoranti, Aperitivi, Bollette).
3. **Coach AI** (solo utenti Pro) — sezione sotto i grafici con l'analisi AI del mese: pattern di spesa, tipologia più frequente/costosa, suggerimento contestuale basato sul residuo disponibile. È la destinazione della CTA "Approfondisci" nella hero card Coach in Home.

Il mese di riferimento è selezionabile tramite navigazione ← →. Il confronto con il budget allocato è sempre visibile per dare contesto ai numeri.

```
Bottom nav → "Statistiche"
    ↓
[Selettore mese]
[Grafico a torta / barre — spese per bucket]
[Lista bucket espandibile → tipologie]
[Sezione Coach AI]             ← solo utenti Pro
```

---

## Requisiti

| # | Requisito | Priorità |
|---|-----------|----------|
| AN-01 | Tab "Statistiche" accessibile dalla bottom navigation | Must |
| AN-02 | Selettore mese ← → in cima; default mese corrente, navigazione libera verso i mesi passati | Must |
| AN-03 | Grafico a torta o ad anello: distribuzione delle spese registrate per bucket nel mese selezionato | Must |
| AN-04 | Ogni slice del grafico usa il colore del bucket corrispondente | Must |
| AN-05 | Totale speso nel mese mostrato al centro del grafico (se ad anello) o sopra (se a torta) | Must |
| AN-06 | Lista bucket sotto il grafico: nome bucket, importo speso, importo allocato, barra di avanzamento (speso / allocato) | Must |
| AN-07 | Tap su un bucket → espande la lista delle tipologie di spesa di quel bucket con importo e % sul totale del bucket | Must |
| AN-08 | Tipologie ordinate per importo decrescente (la più alta in cima) | Should |
| AN-09 | Bucket senza spese nel mese sono visibili ma con importo €0 e barra vuota | Must |
| AN-10 | Stato vuoto: nessuna spesa registrata nel mese → illustrazione + messaggio "Nessuna spesa registrata in questo mese" | Must |
| AN-11 | Grafico a barre mensile (ultimi 6 mesi) per vedere l'andamento nel tempo — totale speso per mese | Could |
| AN-12 | Mesi futuri non selezionabili (freccia → disabilitata sul mese corrente) | Must |
| AN-13 | Mini-donut chart in Home (D-13), posizionata sotto le bucket card: stessi dati e colori del grafico principale; tap → naviga al tab Statistiche | Should |
| AN-14 | Sezione Coach AI in fondo a /analytics (solo utenti Pro): mostra l'analisi completa del mese con suggerimenti contestuali basati sulle tipologie di spesa | Must |
| AN-15 | La sezione Coach mostra il messaggio completo (non troncato), con riferimento alla tipologia più frequente/costosa e al residuo disponibile | Must |
| AN-16 | Skeleton loader nella sezione Coach durante la generazione del messaggio AI | Must |
| AN-17 | Per gli utenti Free la sezione Coach mostra un teaser con CTA "Scopri DreamJar Pro" → naviga a Settings | Should |

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
