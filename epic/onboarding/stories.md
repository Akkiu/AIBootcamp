# Stories — Onboarding

> Ogni story è un prompt autonomo per Lovable.
> Brand system e PRD sono allegati come project context — non vanno ripetuti nel prompt.

---

## O-1 · Splash

> As a new user, I want to see what DreamJar does before I start so that I understand the value before giving any data.

**Prompt Lovable**

DreamJar è un'app di gestione budget personale. Costruisci la schermata Splash dell'onboarding.

Schermata a piena altezza (sfondo scuro, brand color) con:
- Logo e nome app
- Headline: "Scopri quanto puoi davvero spendere"
- Sottotitolo: "Setup in 2 minuti. Niente fogli Excel."
- Bottone primario "Inizia"
- Link secondario "Ho già un account" → login

Tap su "Inizia" → step 2 (Stipendio).

---

## O-2 · Stipendio

> As a new user, I want to enter my monthly income so that the app can calculate my available budget.

**Prompt Lovable**

Nella schermata Onboarding step 2 di DreamJar, chiedi all'utente il suo stipendio mensile netto.

Contenuto: titolo "Quanto guadagni al mese?", sottotitolo "Il netto che ti arriva in banca", input numerico grande con prefisso €.

Indicatore step "2 di 5" in cima. Bottone "Avanti" disabilitato finché il valore è 0 o vuoto. Validazione inline se il valore non è numerico.

Salva in `profiles.monthly_income`. Tap "Avanti" → step 3.

---

## O-3 · Spese fisse

> As a new user, I want to list my recurring fixed expenses so that the app knows what's already committed every month.

**Prompt Lovable**

Nella schermata Onboarding step 3 di DreamJar, l'utente aggiunge le sue spese fisse mensili.

Titolo: "Quali spese hai ogni mese?" — lista di spese già aggiunte (vuota all'inizio), bottone "+ Aggiungi spesa" che apre un form inline con: nome spesa (es. "Affitto"), importo €, giorno del mese di addebito (1–31).

Ogni spesa aggiunta appare nella lista con nome, importo e giorno, e un'icona per eliminarla. Totale spese fisse mostrato in fondo alla lista.

Indicatore step "3 di 5". Bottone "Avanti" attivo anche con lista vuota (le spese fisse sono opzionali). Salva ogni spesa in `recurring_expenses` con `bucket = fixed`. Tap "Avanti" → step 4.

---

## O-4 · Lifestyle quiz

> As a new user, I want to answer a few lifestyle questions so that the app estimates my variable expenses and buffer without manual calculation.

**Prompt Lovable**

Nella schermata Onboarding step 4 di DreamJar, stima le spese variabili e il buffer tramite un quiz a domande chiuse.

Titolo: "Com'è il tuo stile di vita?" Mostra 3–4 domande in sequenza (una alla volta o a scorrimento), ognuna con 3 opzioni selezionabili. Esempi:

- "Quante volte mangi fuori a settimana?" → Raramente / Qualche volta / Spesso
- "Come descriveresti i tuoi acquisti?" → Essenziale / Bilanciato / Generoso
- "Quanto tieni alla sicurezza finanziaria?" → Poco / Abbastanza / Molto

In base alle risposte, calcola e salva in `profiles`: `variable_expenses` (% del reddito) e `buffer` (% del reddito). Mostra un riepilogo dei valori stimati prima di procedere, con possibilità di modificarli manualmente.

Indicatore step "4 di 5". Tap "Avanti" → step 5.

---

## O-5 · Primo obiettivo

> As a new user, I want to add my first savings goal so that I feel motivated to use the app from day one.

**Prompt Lovable**

Nella schermata Onboarding step 5 di DreamJar, l'utente crea il suo primo obiettivo di risparmio.

Titolo: "Per cosa stai risparmiando?" Campi: nome obiettivo (es. "Viaggio in Asia"), emoji picker, importo target €, data target (mese e anno, opzionale).

Indicatore step "5 di 5". Bottone "Concludi setup" disabilitato finché nome e importo sono vuoti.

Al tap: salva in `goals` con `status = active`, imposta `profiles.onboarding_completed = true`, redirect alla Home. Mostra una micro-celebrazione (animazione o confetti) prima del redirect.

---

## Sequenza

| # | Story | Dipendenze |
|---|-------|------------|
| 1 | O-1 Splash | Auth |
| 2 | O-2 Stipendio | O-1 |
| 3 | O-3 Spese fisse | O-2 |
| 4 | O-4 Lifestyle quiz | O-3 |
| 5 | O-5 Primo obiettivo | O-4 + epica Goals |
