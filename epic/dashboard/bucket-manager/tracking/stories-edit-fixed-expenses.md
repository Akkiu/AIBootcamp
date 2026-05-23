# Stories — Modifica Spese Fisse con Ricalcolo Automatico

> Ogni story è un prompt autonomo per Lovable.
> Brand system e PRD sono allegati come project context — non vanno ripetuti nel prompt.

---

## EF-1 · Lista spese fisse e modifica importo con preview ricalcolo

> As a user, I want to edit a fixed expense and immediately see how the change affects my other buckets before confirming.

**Prompt Lovable**

DreamJar è un'app di gestione budget personale con un modello a bucket. Aggiungi la funzionalità di modifica delle spese fisse con ricalcolo automatico.

Dal dettaglio del bucket "💸 Spese fisse" mostra una lista delle spese fisse ricorrenti dell'utente (quelle inserite in onboarding). Ogni riga mostra: nome della spesa, importo mensile, giorno del mese di addebito.

Tap su una riga → bottom sheet "Modifica spesa fissa" con questi campi precompilati:
1. **Nome** — testo, obbligatorio
2. **Importo** — numpad, obbligatorio, > 0
3. **Giorno del mese** — selettore 1–31

**Sezione preview ricalcolo** — appare sotto i campi, aggiornata in tempo reale mentre l'utente digita l'importo. Mostra i nuovi budget dei 4 bucket variabili (Svago, Imprevisti, Utenze, Altro) con la variazione rispetto all'attuale (+€X in verde o −€X in rosso). Titolo della sezione: "Come cambia il tuo budget". Obiettivi e Free to Dream non compaiono in questa sezione perché restano invariati.

Bottone "Salva" — disabilitato se l'importo non è cambiato rispetto al valore attuale.

Al salvataggio: bottom sheet si chiude, tutte le bucket card in Home mostrano i nuovi importi aggiornati, toast non bloccante "Budget aggiornato 👍".

Errore salvataggio: toast "Errore. Riprova."

---

## EF-2 · Aggiungi, elimina e guardrail sul ricalcolo

> As a user, I want to add or remove a fixed expense, and be warned when the change is too large to redistribute automatically.

**Prompt Lovable**

DreamJar — estendi la schermata lista spese fisse (costruita in EF-1) con le azioni di aggiunta, eliminazione e il guardrail sul ricalcolo.

**Aggiunta spesa fissa** — pulsante "+" in alto a destra nella lista. Apre un bottom sheet "Nuova spesa fissa" con gli stessi campi di EF-1 (nome, importo, giorno del mese) ma vuoti. La sezione preview ricalcolo funziona allo stesso modo. Al salvataggio: nuova riga aggiunta in lista, bucket variabili aggiornati in Home.

**Eliminazione spesa fissa** — swipe a sinistra su una riga → pulsante "Elimina" rosso → modale di conferma: "Sei sicuro di voler eliminare «[nome spesa]»? I bucket variabili verranno ricalcolati." con pulsanti "Annulla" e "Elimina". Al conferma: riga rimossa, ricalcolo applicato, bucket in Home aggiornati.

**Guardrail** — se il ricalcolo (in aggiunta, modifica o eliminazione) porterebbe uno o più bucket variabili sotto €0, il bottone "Salva" resta disabilitato e nella sezione preview appare il messaggio: "La variazione è troppo grande per essere distribuita automaticamente. Rivedi la tua allocazione manualmente." I bucket che andrebbero in negativo sono evidenziati in rosso nella preview.

Caso limite — pool variabile già a €0 (tutti i bucket variabili sono a zero): bottone "Salva" disabilitato con messaggio "Non c'è budget variabile da ridistribuire."

---

## Sequenza

| # | Story | Dipendenze |
|---|-------|------------|
| 1 | EF-1 Lista + modifica con preview | EX-3 (dettaglio bucket deve esistere) |
| 2 | EF-2 Aggiungi / elimina + guardrail | EF-1 |
