# Stories — Dashboard (Home)

> Ogni story è un prompt autonomo per Lovable.
> Brand system e PRD sono allegati come project context — non vanno ripetuti nel prompt.

---

## D-1 · Hero "Free to Dream" e navigazione

> As a user, I want to see my "Free to Dream" number as soon as I open the app so that I immediately know my available budget.

**Prompt Lovable**

DreamJar è un'app di gestione budget personale. Costruisci la Home principale.

In cima: saluto con nome utente, testo contestuale per ora del giorno (buongiorno / buon pomeriggio / buonasera).

Hero card a piena larghezza (sfondo scuro):
- Etichetta "Free to Dream"
- Numero grande: `stipendio - spese_fisse - spese_variabili - buffer_emergenze`
- Riga sotto: "Hai margine 🎉" se > 0, "Attenzione: sei in rosso" se < 0

In fondo: bottom navigation con 4 tab — Home (attiva), Budget, Obiettivi, Profilo.

Se onboarding non completato: hero mostra "—" e banner "Completa il setup per vedere i tuoi numeri" con CTA. Loading: skeleton loaders.

---

## D-2 · Riepilogo 4 bucket

> As a user, I want to see how my income is split across the 4 buckets so that I understand where my money goes.

**Prompt Lovable**

Nella Home di DreamJar, sotto l'hero, aggiungi sezione "Il tuo mese" con 4 card (griglia 2×2).

Ogni card: emoji + nome bucket, importo allocato (€), % sul reddito. Colori dal brand system allegato (Corallo, Lilla, Azzurro, Verde).

Tap su card → placeholder navigazione (nessun errore, schermata Budget in futuro).

---

## D-3 · Obiettivi attivi

> As a user, I want to see my goals progress on the Home so that I stay motivated every day.

**Prompt Lovable**

Nella Home di DreamJar, dopo i bucket, aggiungi sezione "I tuoi obiettivi".

Ogni riga: emoji + nome, progress bar (risparmiato / target), "Mancano €X".

Tap → dettaglio obiettivo. Max 3 in Home, link "Vedi tutti" se ce ne sono di più. Stato vuoto: "Aggiungi il tuo primo obiettivo" con CTA.

---

## D-4 · Spese in arrivo (7 giorni)

> As a user, I want to see upcoming recurring expenses so that I'm never caught off guard.

**Prompt Lovable**

Nella Home di DreamJar, dopo gli obiettivi, aggiungi sezione "In arrivo" con le spese ricorrenti nei prossimi 7 giorni.

Ogni riga: nome spesa, importo, data ("Domani" / "18 mag"). Ordinate per data crescente. Sezione nascosta completamente se nessuna spesa nel periodo.

---

## D-5 · Pull-to-refresh e loading

> As a user, I want to refresh my dashboard manually so that I always see up-to-date numbers.

**Prompt Lovable**

Nella Home di DreamJar aggiungi:
- Pull-to-refresh: aggiorna hero, bucket, obiettivi, spese in arrivo
- Skeleton loaders al posto di ogni sezione durante il caricamento (layout stabile, niente shift)
- Errore fetch: banner "Impossibile aggiornare i dati. Riprova." con bottone Riprova

---

## Sequenza

| # | Story | Dipendenze |
|---|-------|------------|
| 1 | D-1 Hero + nav | Onboarding completato |
| 2 | D-2 Bucket | D-1 |
| 3 | D-3 Obiettivi | D-1 + epica Goals |
| 4 | D-4 In arrivo | D-1 |
| 5 | D-5 Loading | D-1 → D-4 |
