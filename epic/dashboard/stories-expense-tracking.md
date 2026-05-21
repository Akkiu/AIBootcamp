# Stories — Registrazione Spese Manuali

> Ogni story è un prompt autonomo per Lovable.
> Brand system e PRD sono allegati come project context — non vanno ripetuti nel prompt.

---

## EX-1 · Quick Add Expense

> As a user, I want to log a new expense from the Home in a few taps so that tracking never feels like a chore.

**Prompt Lovable**

DreamJar è un'app di gestione budget personale. Aggiungi alla Home la funzionalità di registrazione spesa rapida.

Pulsante "+" flottante in basso a destra (sopra la bottom navigation). Al tap apre un bottom sheet.

Il bottom sheet contiene:
- Campo importo con numpad nativo, placeholder "€ 0,00", focus automatico all'apertura
- Selezione bucket: 4 opzioni a scelta singola con emoji e nome — 💸 Spese fisse, 🎨 Spese variabili, 🛡️ Buffer emergenze, 🌍 Obiettivi. Colori dal brand system allegato.
- Campo "Nome / descrizione" testuale, opzionale, placeholder "es. Cena con amici"
- Campo data, default oggi, modificabile
- Bottone "Salva" — disabilitato finché importo > 0 e bucket selezionato

Al salvataggio: sheet si chiude, toast non bloccante "Spesa aggiunta 👍", bucket card corrispondente si aggiorna con il nuovo importo speso, hero "Free to Dream" si ricalcola.

Errore di salvataggio: toast "Errore nel salvataggio. Riprova."

---

## EX-2 · Bucket card aggiornata (speso / rimanente)

> As a user, I want each bucket to show how much I've spent vs my budget so that I always know where I stand.

**Prompt Lovable**

DreamJar — aggiorna le 4 bucket card nella sezione "Il tuo mese" in Home.

Ogni card ora mostra tre righe: budget allocato (etichetta "Budget"), importo speso questo mese (etichetta "Speso"), rimanente (etichetta "Rimanente" = budget − speso). Aggiungi una barra progresso che rappresenta % spesa sul budget.

Se speso > budget: barra e importo "Rimanente" diventano corallo, testo "Rimanente" diventa "Sforato di €X".

Nessuna spesa ancora registrata: "Speso €0", barra vuota.

---

## EX-3 · Dettaglio bucket con lista spese

> As a user, I want to tap a bucket and see all my logged expenses for the month so that I can review and delete them if needed.

**Prompt Lovable**

DreamJar — crea la schermata "Dettaglio Bucket" raggiungibile dal tap su una bucket card nella Home.

In cima: nome bucket con emoji, budget del mese, barra speso/rimanente (stesso stile di Home).

Lista spese del mese corrente, ordinate per data decrescente. Ogni riga: data, nome/descrizione (o "Spesa" se non specificato), importo. Se nessuna spesa: stato vuoto "Nessuna spesa registrata questo mese".

Eliminazione spesa: swipe a sinistra sulla riga → pulsante "Elimina" rosso → conferma → spesa rimossa, bucket e Free to Dream ricalcolati.

Pulsante "Aggiungi spesa" in basso, che apre lo stesso bottom sheet di EX-1 con il bucket già preselezionato.

Navigazione: freccia "Indietro" in alto a sinistra → torna alla Home.

---

## Sequenza

| # | Story | Dipendenze |
|---|-------|------------|
| 1 | EX-1 Quick Add | D-1, D-2 (bucket cards esistenti) |
| 2 | EX-2 Bucket aggiornata | EX-1 |
| 3 | EX-3 Dettaglio bucket | EX-2 |
