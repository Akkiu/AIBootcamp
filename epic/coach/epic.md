# Epic: Coach AI

**Stato:** To Do · **Priorità:** Should — v1.2

> As a user, I want an AI coach that reads my spending data and tells me — in plain language — what I should watch out for this month, referencing my actual upcoming expenses and spending patterns by category.

---

## Come funziona

Il Coach AI è un layer intelligente che analizza i dati finanziari dell'utente e genera un messaggio personalizzato tramite LLM. Non usa soglie statiche: il suggerimento è prodotto dall'AI in base al contesto reale del mese.

Si manifesta in due superfici:

1. **Coach Card in Home** — una card sotto il grafico Donut. Mostra i dati chiave del mese e un messaggio AI-generato: specifico, contestuale, con riferimento alle spese reali dell'utente (es. "Ricorda che a fine mese hai il bollo — viste le spese in Svago, riduci le cene fuori").
2. **Notifiche push** — alert nei momenti critici; il testo della notifica è anch'esso generato dall'AI in base al contesto del momento.

Il tono è sempre incoraggiante e forward-looking. Mai colpevolizzante. Mai generico.

```
Home
├── [Grafico Donut]           ← centro = FtD al netto delle ricorrenti del mese
├── [Coach Card]
│     ├── Già speso: €X
│     ├── Spese variabili future: €Y
│     ├── Fine mese stimato: €Z
│     └── [Messaggio AI]      ← generato da LLM, specifico e contestuale
└── [...]
```

---

## Architettura

Il Coach AI funziona tramite una **Supabase Edge Function** che viene chiamata:
- All'apertura dell'app (se il messaggio è più vecchio di 2 ore o non esiste ancora per il giorno)
- Dopo la registrazione di una nuova spesa

La Edge Function raccoglie il contesto e chiama un LLM esterno (Claude di Anthropic). Il messaggio generato viene salvato in cache e mostrato nella card senza aspettare la risposta ad ogni tap.

### Contesto passato all'LLM

| Dato | Dettaglio |
|------|-----------|
| Bucket balances | Importo allocato e speso per ciascuno dei 6 bucket nel mese corrente |
| Spese registrate | Lista spese variabili del mese: importo, bucket, tipologia, data |
| Spese ricorrenti future | Lista ricorrenti non ancora addebitate nel mese: nome, importo, data prevista |
| Spese variabili future | Spese manuali con data futura pianificate per il mese corrente: nome, importo, data |
| FtD corrente | Valore centro Donut (FtD netto ricorrenti) |
| FtD iniziale del mese | Valore al reset mensile (baseline di riferimento) |
| Giorni rimanenti al mese | Per calibrare il tono dell'urgenza |

### Output atteso dall'LLM

1-3 frasi in italiano, tono da coach personale:
- Cita almeno una spesa futura reale per nome se rilevante
- Cita il bucket più a rischio per categoria (non solo "Svago" in astratto, ma "cene fuori" o "abbonamenti")
- Propone un'azione concreta ("riduci", "pianifica", "puoi permetterti")
- Mai colpevolizzante, sempre forward-looking

---

## Requisiti — Coach Card

| # | Requisito | Priorità |
|---|-----------|----------|
| CO-01 | Card Coach visibile nella Home, sotto il grafico Donut | Must |
| CO-02 | La card mostra "Già speso questo mese": totale spese variabili registrate nel mese corrente | Must |
| CO-03 | La card mostra "Spese variabili future": totale delle spese variabili con data futura già pianificate per il mese corrente (le ricorrenti sono già detratte nel Donut) | Must |
| CO-04 | La card mostra "Fine mese stimato": valore centro Donut − spese variabili future; in verde se positivo, in rosso se negativo o sotto il 10% del FtD iniziale | Must |
| CO-05 | Il messaggio AI è generato da una Supabase Edge Function che chiama un LLM con il contesto finanziario completo del mese | Must |
| CO-06 | Il messaggio AI fa riferimento a spese future reali per nome (es. "bollo auto", "affitto") e a categorie di spesa specifiche (es. "cene fuori", "abbonamenti") | Must |
| CO-07 | Il messaggio si aggiorna automaticamente dopo ogni spesa registrata (con debounce di 30s per evitare chiamate eccessive) | Must |
| CO-08 | Il messaggio è cached: se già generato nelle ultime 2 ore e nessuna nuova spesa è stata registrata, viene mostrato quello esistente senza nuova chiamata API | Should |
| CO-09 | Tap sulla card → bottom sheet con la lista delle spese variabili future pianificate itemizzate (nome, importo, data), ordinate per data crescente | Should |
| CO-10 | Fallback se la chiamata API fallisce: messaggio neutro non-AI ("Analisi temporaneamente non disponibile. Riprova tra poco.") senza bloccare la card | Must |
| CO-11 | Skeleton loader durante la generazione del messaggio AI | Must |
| CO-12 | La card è nascosta nei primi 2 giorni del mese se non ci sono ancora spese registrate né in arrivo | Should |

---

## Requisiti — Notifiche Push

| # | Requisito | Priorità |
|---|-----------|----------|
| CO-13 | Notifica "Spesa grande" quando una singola spesa supera il 20% del FtD disponibile: testo generato dall'AI con riferimento al contesto attuale | Should |
| CO-14 | Notifica "Check-in metà mese" il giorno 15 se il Fine mese stimato è inferiore al 30% del FtD iniziale: testo AI con riferimento alle spese future rilevanti | Should |
| CO-15 | Notifica "Spesa imminente con budget ridotto" quando una ricorrente è prevista entro 3 giorni e il FtD disponibile è inferiore all'importo: testo AI con nome spesa e importo | Should |
| CO-16 | Le notifiche push sono opt-in; il consenso è richiesto la prima volta che la Coach Card viene visualizzata | Must |
| CO-17 | L'utente può disabilitare le notifiche Coach dalle Impostazioni senza disabilitare le altre notifiche dell'app | Should |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Messaggio in generazione | Skeleton loader sulla sezione testo |
| Messaggio disponibile | Card completa con dati + messaggio AI |
| API non disponibile | Dati numerici visibili + fallback message neutro |
| Nessun dato (primi 2 giorni, nessuna spesa) | Card nascosta |
| Fine mese stimato negativo | Importo in rosso, messaggio AI con tono di allerta |

---

## Dipendenze

- **[Dashboard](../dashboard/epic.md)** — la Coach Card è ospitata nella Home, sotto il grafico Donut; il valore centro Donut è il valore di riferimento del Coach
- **[Riepilogo Spese](../expense/summary/epic.md)** — fonte dati per le spese variabili registrate (ES-02) e le spese variabili future pianificate (ES-13/14/15)
- **[Budget](../budget/epic.md)** — fonte dati per le spese ricorrenti future (passate come contesto all'LLM e usate dal trigger CO-15)
- **[Notifiche](../notification/epic.md)** — le notifiche push del Coach si appoggiano all'infrastruttura notifiche esistente
- **[Header Coach](../dashboard/header%20coach/epic.md)** — rimane come indicatore rapido nell'header (ratio-based); la Coach Card aggiunge l'analisi AI e il suggerimento contestuale

> **Requisito tecnico:** richiede una Supabase Edge Function e una API key LLM (Anthropic Claude raccomandato). Non configurabile in automatico da Lovable — va impostata manualmente nelle variabili d'ambiente Supabase.
