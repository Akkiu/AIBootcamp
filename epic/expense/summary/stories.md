# Stories — Riepilogo Spese

> Ogni story è un prompt autonomo per Lovable.
> Brand system e PRD sono allegati come project context — non vanno ripetuti nel prompt.

---

## ES-1 · Schermata Riepilogo Spese con spese future

> As a user, I want to see recorded and upcoming expenses in one place so that I have a complete picture of my current month.

**Prompt Lovable**

DreamJar è un'app di gestione budget personale. Crea la schermata "Riepilogo Spese".

La schermata è accessibile dalla bottom navigation (aggiungi una voce "Spese" o inseriscila nel tab Budget, a tua scelta in base al layout più coerente).

**Header:** titolo "Riepilogo Spese", mese corrente ("Maggio 2026"), totale speso nel mese in evidenza (es. "Totale speso: €342,50").

La schermata è divisa in due sezioni:

**Sezione "In arrivo questo mese"** — spese ricorrenti/fisse già pianificate ma non ancora sostenute nel mese corrente (stessa fonte della sezione "In arrivo" in Home, ma con orizzonte mensile invece di 7 giorni). Ogni riga mostra:
- Data prevista (es. "28 mag")
- Nome spesa (es. "Affitto")
- Badge bucket con colore del bucket (💸 Spese fisse, 🎨 Spese variabili, 🛡️ Buffer emergenze, 🌌 Obiettivi)
- Importo allineato a destra

Ordinate per data crescente (la più vicina prima). Sezione nascosta se non ci sono spese future nel mese corrente.

**Sezione "Spese registrate"** — spese già sostenute, ordinate per data decrescente (la più recente in cima). Ogni riga mostra:
- Data (es. "23 mag")
- Tipologia con emoji (es. "🍽️ Cena fuori") — se non specificata, mostra il nome del bucket
- Badge bucket con colore del bucket
- Importo allineato a destra

**Stato vuoto sezione "Spese registrate":** se nessuna spesa ancora registrata nel mese, mostra testo "Nessuna spesa registrata" e CTA "Aggiungi la tua prima spesa" che apre il bottom sheet di aggiunta (già implementato in EX-1).

**Loading:** skeleton loaders su entrambe le sezioni durante il fetch.
**Errore fetch:** banner "Impossibile caricare le spese. Riprova." con bottone Riprova.

---

## ES-2 · Dettaglio spesa ed eliminazione

> As a user, I want to tap on a recorded expense to see its details and delete it if needed so that I can correct mistakes.

**Prompt Lovable**

DreamJar — nella schermata Riepilogo Spese, aggiungi interazioni sulle righe della sezione "Spese registrate".

**Tap su riga spesa registrata** → apre un bottom sheet di dettaglio con: importo, bucket (con emoji e colore), tipologia, data, nota (se presente). Il bottom sheet ha un pulsante "Elimina spesa" in rosso in fondo.

**Eliminazione:** tap "Elimina spesa" → alert di conferma "Eliminare questa spesa?" con opzioni "Annulla" e "Elimina" → conferma → la spesa viene rimossa e si propagano i seguenti aggiornamenti:
- La riga scompare dalla lista "Spese registrate" e il totale mensile in header si riduce dell'importo eliminato
- Il saldo del bucket da cui era stata scalata la spesa viene ripristinato (es. se era una spesa su 🎨 Svago, il bucket Svago torna a +importo)
- Il Free to Dream in Home aumenta dello stesso importo (il budget disponibile del mese torna libero)
- Le card bucket in Dashboard si aggiornano immediatamente a riflettere i nuovi saldi

**Stato vuoto post-eliminazione:** se dopo la rimozione non restano spese nel mese, la sezione "Spese registrate" mostra lo stato vuoto con CTA "Aggiungi la tua prima spesa".

Le righe della sezione "In arrivo questo mese" non sono tappabili in questa story (nessuna interazione prevista per ora).

Nessun'altra modifica alla spesa è prevista (la spesa non è editabile, solo consultabile ed eliminabile).

---

## ES-3 · Selettore mese (storico)

> As a user, I want to browse past months so that I can review my spending history anytime.

**Prompt Lovable**

DreamJar — nella schermata Riepilogo Spese, aggiungi la navigazione tra i mesi.

Sotto l'header principale, inserisci un selettore mese con frecce "←" e "→". La freccia "→" è disabilitata quando si visualizza il mese corrente.

Quando si visualizza un mese precedente: la sezione "In arrivo questo mese" non viene mostrata; le righe della sezione "Spese registrate" sono read-only e il bottom sheet di dettaglio non mostra il pulsante "Elimina spesa". I mesi senza spese mostrano lo stato vuoto "Nessuna spesa in questo mese" senza CTA di aggiunta.

---

## Sequenza

| # | Story | Dipendenze |
|---|-------|------------|
| 1 | ES-1 Schermata + lista + in arrivo | EX-1, EX-2 (spese già registrabili e bucket aggiornati), D-8 (fonte spese ricorrenti) |
| 2 | ES-2 Dettaglio ed eliminazione | ES-1 |
| 3 | ES-3 Selettore mese | ES-1 |
