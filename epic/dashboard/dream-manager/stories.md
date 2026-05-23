# Stories — Gestione Sogni

> Ogni story è un prompt autonomo per Lovable.
> Brand system e PRD sono allegati come project context — non vanno ripetuti nel prompt.

---

## DM-1 · Modifica dati di un sogno

> As a user, I want to edit the name, target amount, and date of a dream so that I can keep it accurate as my plans evolve.

**Prompt Lovable**

DreamJar è un'app di gestione budget personale. Nella schermata Dettaglio sogno aggiungi la funzionalità di modifica.

Il Dettaglio sogno mostra: emoji + nome in cima, barra progresso (saved_amount / target_amount), importo target, importo mancante, data target (se presente). In fondo alla schermata aggiungi un pulsante "Modifica" che apre un bottom sheet.

Il bottom sheet "Modifica sogno" contiene, precompilati con i dati attuali del sogno:
1. **Campo emoji** — picker o input testo, max 2 caratteri
2. **Campo nome** — testo, obbligatorio
3. **Campo importo target** — numerico, obbligatorio, > 0
4. **Campo data target** — date picker, opzionale; se vuoto mostra placeholder "Nessuna scadenza"

Bottone "Salva modifiche": disabilitato finché nome e importo non sono validi. Al salvataggio: aggiorna il record `goals` su Supabase, chiude il bottom sheet, aggiorna la card in Dettaglio in tempo reale, mostra toast "Sogno aggiornato ✨".

Errore salvataggio: toast "Non riesco a salvare. Riprova."

---

## DM-2 · Aggiunta di un nuovo sogno

> As a user, I want to add a new dream so that I can track multiple savings goals at the same time.

**Prompt Lovable**

DreamJar — nella sezione Sogni della Home aggiungi un pulsante "+" (o CTA "Aggiungi sogno") che apre un bottom sheet per creare un nuovo sogno.

Il bottom sheet "Nuovo sogno" contiene:
1. **Campo emoji** — picker o input testo, max 2 caratteri, opzionale
2. **Campo nome** — testo, obbligatorio, placeholder "es. Viaggio in Asia"
3. **Campo importo target** — numerico, obbligatorio, > 0, placeholder "€ 0"
4. **Campo data target** — date picker, opzionale, placeholder "Nessuna scadenza"

Bottone "Aggiungi sogno": disabilitato finché nome e importo non sono validi. Al salvataggio: inserisce un nuovo record in `goals` con `saved_amount = 0` e `status = active`, chiude il bottom sheet, aggiunge la nuova card sogno in cima alla lista nella Home, mostra toast "Sogno aggiunto 🌟".

Errore salvataggio: toast "Non riesco a salvare. Riprova."

---

## DM-3 · Eliminazione di un sogno

> As a user, I want to delete a dream I no longer care about, knowing I'll always have at least one left.

**Prompt Lovable**

DreamJar — nella schermata Dettaglio sogno aggiungi la funzionalità di eliminazione.

Aggiungi un pulsante "Elimina" (distruttivo, colore errore) in fondo alla schermata, separato visivamente dal pulsante "Modifica".

Al tap su "Elimina":

**Caso A — esistono altri sogni:** apre una modale di conferma con titolo "Elimina sogno", testo "Sei sicuro? Questa azione non può essere annullata." e due pulsanti: "Annulla" (chiude la modale) e "Elimina" (distruttivo). Al conferma: elimina il record da `goals`, chiude la modale, torna alla Home, lista sogni aggiornata, toast "Sogno eliminato".

**Caso B — è l'unico sogno rimasto:** invece della modale di conferma, mostra una modale di errore con testo "Devi avere almeno un sogno 🌟" e unico pulsante "Ok". Nessuna eliminazione viene eseguita.

La logica di controllo (conta i sogni attivi prima di procedere) avviene lato client prima di aprire qualsiasi modale.

---

## Sequenza

| # | Story | Dipendenze |
|---|-------|------------|
| 1 | DM-2 Aggiunta nuovo sogno | D-06 (card sogni in Home) |
| 2 | DM-1 Modifica dati sogno | DM-2 (Dettaglio sogno deve esistere) |
| 3 | DM-3 Eliminazione sogno | DM-1 (Dettaglio sogno con pulsanti azioni) |
