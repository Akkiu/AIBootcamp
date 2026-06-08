# Stories — Coach AI

> Ogni story è un prompt autonomo per Lovable.
> Brand system e PRD sono allegati come project context — non vanno ripetuti nel prompt.

---

## CO-1 · Coach Card con messaggio AI

> As a user, I want a card in the Home that uses AI to tell me something specific and useful about my spending this month.

**Prompt Lovable**

DreamJar è un'app di gestione budget personale. Aggiungi nella schermata Home una "Coach Card", posizionata sotto il grafico Donut.

**La card mostra tre valori numerici:**
- **Già speso questo mese** — totale spese variabili registrate nel mese corrente
- **Spese variabili future** — totale spese variabili con data futura già pianificate per il mese (le ricorrenti sono già detratte nel centro del Donut — non si ripetono qui)
- **Fine mese stimato** — valore centro Donut meno le spese variabili future; mostrato in verde se positivo, in rosso se negativo o sotto il 10% del Free to Dream iniziale del mese

**Messaggio AI — genera una Supabase Edge Function** che viene chiamata:
- All'apertura dell'app (se il messaggio salvato ha più di 2 ore o non esiste per il giorno corrente)
- Dopo la registrazione di una nuova spesa (con debounce di 30 secondi)

La Edge Function raccoglie e passa all'LLM il seguente contesto:
- Importo allocato e speso per ciascuno dei 6 bucket nel mese corrente
- Lista spese variabili del mese: importo, bucket, tipologia, data
- Lista spese ricorrenti non ancora addebitate nel mese: nome, importo, data prevista
- Lista spese variabili future pianificate per il mese: nome, importo, data
- FtD corrente (valore centro Donut)
- FtD iniziale del mese (valore al reset mensile)
- Giorni rimanenti al mese corrente

Il prompt all'LLM deve richiedere: 1-3 frasi in italiano, tono da coach personale, che citino almeno una spesa futura reale per nome se presente (es. "bollo auto", "affitto"), che citino il bucket più a rischio per categoria concreta (es. "cene fuori", "vestiti"), e che propongano un'azione specifica ("riduci", "pianifica", "puoi permetterti"). Mai colpevolizzante.

Il messaggio generato viene salvato in cache (Supabase o localStorage) per evitare chiamate ridondanti.

**Comportamento:**
- Skeleton loader sulla sezione testo durante la generazione
- Se l'API fallisce: mostra i dati numerici normalmente + testo neutro "Analisi temporaneamente non disponibile. Riprova tra poco." — la card non si blocca
- Tap sulla card → bottom sheet con lista delle spese variabili future pianificate: nome, importo, data (ordinate per data crescente)
- La card è nascosta se siamo nei primi 2 giorni del mese e non ci sono ancora spese registrate né in arrivo

> **Nota tecnica:** richiede una API key LLM (Anthropic Claude) configurata nelle variabili d'ambiente Supabase (`ANTHROPIC_API_KEY`). Va impostata manualmente prima di pubblicare questa feature.

---

## CO-2 · Notifiche push Coach AI

> As a user, I want to receive a push notification when my spending puts my Free to Dream at risk, with a message that references my actual situation.

**Prompt Lovable**

DreamJar — aggiungi le notifiche push per il Coach AI. Le notifiche si appoggiano all'infrastruttura notifiche già esistente; il testo di ogni notifica è generato dalla stessa Edge Function del Coach con il contesto del momento.

**Tre trigger:**

1. **Spesa grande** — quando una spesa variabile appena registrata supera il 20% del FtD disponibile. La Edge Function genera un testo che cita l'importo della spesa, il bucket, e il FtD rimanente.

2. **Check-in metà mese** — il giorno 15, se il Fine mese stimato (Donut center − spese variabili future) è inferiore al 30% del FtD iniziale. Il testo cita le spese future più rilevanti e suggerisce cosa ridurre.

3. **Spesa imminente con budget ridotto** — quando una ricorrente è prevista entro 3 giorni e il FtD disponibile è inferiore all'importo della spesa. Il testo cita il nome della spesa, l'importo e i giorni mancanti.

**Consenso e preferenze:**
- La prima volta che la Coach Card viene visualizzata → banner opt-in: "Vuoi ricevere consigli anche fuori dall'app? Attiva le notifiche Coach." con CTA "Attiva" e "Non ora".
- In Impostazioni: voce "Notifiche Coach" (toggle on/off) separata dalle altre notifiche.

---

## Sequenza

| # | Story | Dipendenze |
|---|-------|------------|
| 1 | CO-1 Coach Card AI | Donut (valore centro), Riepilogo Spese (spese variabili), Budget (ricorrenti), API key Anthropic configurata |
| 2 | CO-2 Notifiche push | CO-1 (Edge Function già attiva), Notifiche (infrastruttura push) |
