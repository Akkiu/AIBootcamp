# Stories — Budget

> Ogni story è un prompt autonomo per Lovable.
> Brand system e PRD sono allegati come project context — non vanno ripetuti nel prompt.

---

## BU-1 · Schermata Budget con stipendio e allocazioni bucket

> As a user, I want to see my income and bucket allocations in one place so that I always know how my money is distributed.

**Prompt Lovable**

DreamJar è un'app di gestione budget personale. Crea la schermata "Budget", accessibile dal tab "Budget" nella bottom navigation.

**Card Stipendio** — in cima alla schermata: etichetta "Stipendio mensile netto", importo corrente in grande, icona matita per la modifica. Tap sulla card (o sull'icona) → bottom sheet con campo importo (numpad), anteprima del nuovo Free to Dream ("Free to Dream: €X → €Y"), bottone "Salva". Al salvataggio: le percentuali sui bucket si aggiornano automaticamente, gli importi assoluti restano fissi, il Free to Dream in Home si aggiorna.

**Sezione "Allocazioni"** — sotto la card stipendio: 6 card bucket (Spese fisse 💸, Svago 🎉, Imprevisti 🛡️, Utenze ⚡, Altro 📦, Obiettivi 🌍) con importo allocato e % sul reddito. Colori dal brand system allegato.

Tap su una card bucket (escluso Obiettivi) → bottom sheet con importo modificabile (numpad) e anteprima del nuovo Free to Dream. Al salvataggio: card aggiornata, Free to Dream in Home aggiornato.

Il bucket Obiettivi mostra solo i dati (non è modificabile da questa schermata): tap → messaggio "Gli obiettivi si gestiscono dalla sezione Obiettivi".

**Loading:** skeleton loaders su card stipendio e bucket durante il fetch.
**Errore fetch:** banner "Impossibile caricare il budget. Riprova."

---

## BU-2 · Gestione spese ricorrenti

> As a user, I want to add, edit, and remove my recurring expenses so that my budget always reflects my real fixed costs.

**Prompt Lovable**

DreamJar — nella schermata Budget, aggiungi la sezione "Spese ricorrenti" sotto le allocazioni bucket.

**Lista spese ricorrenti:** ogni riga mostra nome, importo e giorno del mese di addebito (es. "Affitto · €800 · giorno 1"). Ordinate per giorno del mese crescente.

**Aggiunta:** pulsante "+" in alto a destra della sezione → bottom sheet con tre campi: nome (testo), importo (numpad), giorno del mese (1–31, selettore o numpad). Bottone "Aggiungi" disabilitato finché tutti i campi non sono validi.

**Modifica:** tap su una riga → bottom sheet con gli stessi campi precompilati + preview del ricalcolo automatico sui bucket variabili (Svago, Imprevisti, Utenze, Altro): mostra i nuovi importi con variazione (+/− €X) rispetto ai valori attuali. Obiettivi e Free to Dream restano invariati nel preview.

**Salvataggio modifica:** i bucket variabili vengono ricalcolati proporzionalmente. Se il ricalcolo porta un bucket sotto €0: salvataggio bloccato, messaggio inline "La variazione è troppo grande. Rivedi la tua allocazione manualmente."

**Eliminazione:** swipe a sinistra sulla riga → pulsante "Elimina" rosso → conferma "Eliminare questa spesa ricorrente?" → conferma → ricalcolo automatico (i bucket variabili aumentano proporzionalmente).

**Stato vuoto:** "Nessuna spesa ricorrente" con CTA "Aggiungi la tua prima spesa ricorrente".

**Feedback:** toast non bloccante "Budget aggiornato 👍" dopo ogni salvataggio riuscito.

---

## Sequenza

| # | Story | Dipendenze |
|---|-------|------------|
| 1 | BU-1 Schermata + stipendio + allocazioni | Onboarding completato (valori iniziali già presenti) |
| 2 | BU-2 Spese ricorrenti | BU-1 (schermata Budget esistente) |
