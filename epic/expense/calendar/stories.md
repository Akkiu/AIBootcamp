# Stories — Calendario Spese

> Ogni story è un prompt autonomo per Lovable.
> Brand system e PRD sono allegati come project context — non vanno ripetuti nel prompt.

---

## EC-1 · Vista Calendario Spese Ricorrenti

> As a user, I want to see my recurring expenses on a calendar so that I know exactly when money will leave my account each month.

**Prompt Lovable**

DreamJar è un'app di gestione budget personale. Nella schermata "Riepilogo Spese" (già esistente), aggiungi un toggle "Lista / Calendario" in cima alla schermata per passare tra le due viste.

**Vista Calendario:**

**Header:** nome mese + anno (es. "Maggio 2026"), totale spese ricorrenti del mese in evidenza (es. "Ricorrenti: €1.240"). Frecce ← → per navigare tra i mesi, senza limiti di passato o futuro.

**Griglia mensile:** calendario mensile standard (lun–dom). I giorni con una o più spese ricorrenti mostrano un marker visivo (dot o badge con importo totale del giorno). I giorni senza spese sono vuoti.

**Tap su un giorno con spese** → bottom sheet con la lista delle spese ricorrenti previste per quel giorno. Ogni riga mostra:
- Nome spesa (es. "Affitto")
- Badge bucket con emoji e colore (es. 💸 Spese fisse)
- Importo allineato a destra

**Spese mensili** (configurate in Budget) compaiono ogni mese nel giorno configurato.

**Spese annuali** compaiono una volta l'anno nel mese e giorno configurati.

**Stato vuoto:** se il mese non ha spese ricorrenti, la griglia è vuota e compare il messaggio "Nessuna spesa ricorrente in questo mese".

**Loading:** skeleton loader sulla griglia durante il fetch.

---

## EC-2 · Stato "pagata" e link al dettaglio

> As a user, I want to see which recurring expenses have already been paid this month so that I know what's still pending.

**Prompt Lovable**

DreamJar — nel Calendario Spese (già implementato in EC-1), aggiungi la distinzione tra spese pagate e pianificate nel mese corrente e nei mesi passati.

**Giorni passati nel mese corrente e mesi precedenti:** se una spesa ricorrente è stata effettivamente registrata come spesa (stessa data e importo corrispondente), il marker del giorno cambia aspetto (es. colore attenuato o icona check) per indicare che la spesa è stata sostenuta.

**Bottom sheet del giorno:** ogni riga mostra lo stato della spesa:
- **Pianificata** — spesa ricorrente non ancora registrata
- **Pagata** — spesa registrata nel tracking, con data effettiva

**Tap su una riga "Pagata"** → chiude il bottom sheet e apre il dettaglio della spesa registrata (bottom sheet già implementato in ES-2).

I mesi futuri mostrano sempre tutte le spese come "Pianificate" (non esiste uno stato pagata per il futuro).

---

## Sequenza

| # | Story | Dipendenze |
|---|-------|------------|
| 1 | EC-1 Vista calendario base | ES-1 (schermata Riepilogo Spese già esistente), BU-09/BU-10 (spese ricorrenti configurate in Budget) |
| 2 | EC-2 Stato pagata + link dettaglio | EC-1, ES-2 (dettaglio spesa registrata) |
