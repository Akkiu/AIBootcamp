# Stories — Analytics

> Ogni story è un prompt autonomo per Lovable.
> Brand system e PRD sono allegati come project context — non vanno ripetuti nel prompt.

---

## AN-1 · Schermata Statistiche con grafico e lista bucket

> As a user, I want to see a chart of my monthly expenses by category so that I have an immediate picture of where my money goes.

**Prompt Lovable**

DreamJar è un'app di gestione budget personale. Aggiungi un tab "Statistiche" nella bottom navigation.

**Selettore mese** in cima alla schermata con frecce ← →. Default: mese corrente. La freccia → è disabilitata sul mese corrente (nessun mese futuro). Navigazione libera verso i mesi passati.

**Grafico ad anello** al centro della schermata: mostra la distribuzione delle spese registrate nel mese per bucket. Ogni slice usa il colore del bucket corrispondente (i colori dei bucket sono già definiti nel brand system). Il totale speso nel mese è mostrato al centro dell'anello (es. "€ 842").

**Lista bucket** sotto il grafico. Ogni riga mostra:
- Emoji e nome del bucket (es. 🎉 Svago)
- Importo speso nel mese e importo allocato (es. "€ 210 / €300")
- Barra di avanzamento: speso / allocato, con colore del bucket

I bucket senza spese nel mese sono visibili con importo €0 e barra vuota.

**Stato vuoto:** se nessuna spesa registrata nel mese, il grafico non viene mostrato e compare un messaggio "Nessuna spesa registrata in questo mese".

**Loading:** skeleton loader su grafico e lista durante il fetch.

**Errore fetch:** banner "Impossibile caricare i dati. Riprova." con bottone Riprova.

---

## AN-2 · Dettaglio tipologie per bucket

> As a user, I want to expand a category to see the breakdown by typology so that I understand exactly what I spent money on.

**Prompt Lovable**

DreamJar — nella schermata Statistiche (già implementata in AN-1), aggiungi l'espansione delle tipologie per bucket.

**Tap su una riga bucket** → la riga si espande mostrando la lista delle tipologie di spesa registrate in quel bucket nel mese selezionato. Ogni riga tipologia mostra:
- Emoji e nome tipologia (es. 🍽️ Ristorante)
- Importo speso
- Percentuale sul totale del bucket (es. "34%")

Le tipologie sono ordinate per importo decrescente (la più alta in cima).

Un secondo tap sulla riga bucket collassa la lista. Un solo bucket alla volta può essere espanso; aprirne uno nuovo collassa il precedente.

Le spese senza tipologia associata sono raggruppate sotto la voce "Altro" in fondo alla lista.

---

## AN-3 · Andamento storico (ultimi 6 mesi)

> As a user, I want to see how my total spending has changed over the last 6 months so that I can spot trends over time.

**Prompt Lovable**

DreamJar — nella schermata Statistiche, aggiungi una sezione "Andamento" sotto la lista bucket.

**Grafico a barre verticali** con gli ultimi 6 mesi (incluso il mese corrente). Ogni barra rappresenta il totale speso in quel mese. Il mese corrente è evidenziato con il colore primario del brand; i mesi passati usano una tonalità attenuata.

Sull'asse Y: importi in €. Sull'asse X: abbreviazione del mese (es. "Gen", "Feb"). Tap su una barra → seleziona quel mese nel selettore e aggiorna grafico ad anello e lista bucket di conseguenza.

---

## Sequenza

| # | Story | Dipendenze |
|---|-------|------------|
| 1 | AN-1 Schermata base + grafico + lista bucket | EX-1 (spese già registrabili), BU-04 (importi bucket configurati) |
| 2 | AN-2 Dettaglio tipologie | AN-1 |
| 3 | AN-3 Andamento storico 6 mesi | AN-1 |
