# Stories — Header Coach

> Ogni story è un prompt autonomo per Lovable.
> Brand system e PRD sono allegati come project context — non vanno ripetuti nel prompt.

---

## HC-1 · Messaggio coach contestuale in Home

> As a user, I want to see a message at the top of the dashboard that tells me honestly how my spending is going this month.

**Prompt Lovable**

DreamJar è un'app di gestione budget personale. Sostituisci il saluto generico in cima alla Home con un componente "Header Coach" che mostra un messaggio dinamico basato sul budget rimanente del mese.

Il messaggio si calcola sul **ratio** tra il Free to Dream rimanente e il Free to Dream iniziale del mese:

| Condizione | Messaggio | Stile |
|------------|-----------|-------|
| ratio ≥ 80% | "Stai andando alla grande" | Colore positivo del brand |
| 60% ≤ ratio < 80% | "Stai gestendo in modo oculato" | Colore neutro |
| 35% ≤ ratio < 60% | "Il budget si assottiglia, monitora le spese" | Colore attenzione (arancione) |
| 10% ≤ ratio < 35% | "Quasi al limite: solo l'essenziale da qui in poi" | Colore errore attenuato |
| ratio < 10% | "Attenzione: il tuo sogno è a rischio!" | Rosso errore, testo in grassetto |

Il saluto con nome utente e ora del giorno rimane visibile sopra il messaggio coach.

Il componente è nascosto se il Free to Dream iniziale del mese è €0.

Se il Free to Dream rimanente è negativo (budget sforato), mostra il messaggio rosso in grassetto.

Il messaggio si aggiorna in tempo reale ogni volta che l'utente registra una spesa — nessun refresh manuale necessario.

---

## Sequenza

| # | Story | Dipendenze |
|---|-------|------------|
| 1 | HC-1 Messaggio coach | EX-1 (registrazione spese, per il trigger real-time) |
