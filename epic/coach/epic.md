# Epic: Coach AI

**Stato:** To Do · **Priorità:** Should — v1.2 · **Piano:** Pro

> As a **Pro user**, I want an AI coach that reads my spending data and tells me — in plain language — what I should watch out for this month, referencing my actual upcoming expenses and spending patterns by category.

---

## Come funziona

Il Coach AI è un layer intelligente che analizza le spese del mese e genera suggerimenti personalizzati tramite LLM (Gemini). Non usa soglie statiche: il suggerimento è prodotto dall'AI in base al contesto reale.

**Dati analizzati:** spese manuali registrate + spese auto-importate dalla banca. Le transazioni ancora in Inbox (pending_review) sono escluse perché non ancora confermate dall'utente.

Si manifesta in tre superfici:

1. **Hero card in Home** — card sintetica con 1-2 frasi del coach + CTA "Approfondisci" → naviga a /analytics. Solo utenti Pro; gli utenti Free vedono una card teaser.
2. **Analisi completa in /analytics** — sezione Coach nel tab Statistiche. Analisi dettagliata delle tipologie di spesa, pattern del mese, suggerimento contestuale con riferimento al residuo disponibile e ai giorni rimanenti (es. "Questo mese hai speso molto al ristorante. Con €200 di residuo ti consiglio di evitare cene fuori fino a fine mese").
3. **Notifiche push** — alert nei momenti critici generati dall'AI in base al contesto del momento.

Il tono è sempre incoraggiante e forward-looking. Mai colpevolizzante. Mai generico.

```
Home
├── [Grafico Donut]
├── [Hero Card Coach]          ← frase sintetica + CTA "Approfondisci"
└── [...]

/analytics
├── [Grafico spese per bucket]
├── [Lista bucket/tipologie]
└── [Sezione Coach]            ← analisi completa + suggerimento contestuale
```

---

## Architettura

Il Coach AI funziona tramite una **Supabase Edge Function** che viene chiamata:
- All'apertura dell'app (se il messaggio è più vecchio di 2 ore o non esiste ancora per il giorno)
- Dopo la registrazione di una nuova spesa (debounce 30s)

La Edge Function raccoglie il contesto e chiama **Gemini (Google)**. Il messaggio generato viene salvato in cache e mostrato senza aspettare la risposta ad ogni tap.

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

## Requisiti — Hero Card in Home

| # | Requisito | Priorità |
|---|-----------|----------|
| CO-01 | Hero card Coach in Home — visibile solo agli utenti Pro; per gli utenti Free mostra card teaser con CTA "Scopri DreamJar Pro" → naviga a Settings | Must |
| CO-02 | La card mostra il messaggio AI sintetico (1-2 frasi) sul comportamento di spesa del mese | Must |
| CO-03 | CTA "Approfondisci" nella card → naviga a /analytics con la sezione Coach visibile | Must |
| CO-04 | Skeleton loader durante la generazione del messaggio | Must |
| CO-05 | Fallback se API non disponibile: "Analisi temporaneamente non disponibile. Riprova tra poco." | Must |
| CO-06 | La card è nascosta nei primi 2 giorni del mese se non ci sono ancora spese registrate | Should |

---

## Requisiti — Analisi completa in /analytics

| # | Requisito | Priorità |
|---|-----------|----------|
| CO-07 | Sezione Coach in /analytics: analisi completa del mese con suggerimenti contestuali basati sulle tipologie di spesa | Must |
| CO-08 | Il Coach analizza spese manuali + spese auto-importate dalla banca; le transazioni in Inbox (pending_review) sono escluse | Must |
| CO-09 | Il messaggio AI cita la tipologia più frequente o più costosa del mese (es. "cene fuori") e la relaziona al FtD residuo e ai giorni rimanenti | Must |
| CO-10 | Il messaggio AI propone un'azione concreta calibrata sul residuo disponibile (es. "con €200 di residuo, evita cene fuori fino a fine mese") | Must |
| CO-11 | Il messaggio si aggiorna dopo ogni nuova spesa registrata (debounce 30s) | Must |
| CO-12 | Il messaggio è cached: riusato se generato nelle ultime 2 ore e nessuna nuova spesa nel frattempo | Should |

---

## Requisiti — Notifiche Push

| # | Requisito | Priorità |
|---|-----------|----------|
| CO-13 | Notifica push "Spesa grande" quando una singola spesa supera il 20% del FtD disponibile: testo generato dall'AI con riferimento al contesto attuale — **solo utenti Pro** | Should |
| CO-14 | Notifica push "Check-in metà mese" il giorno 15 se il Fine mese stimato è inferiore al 30% del FtD iniziale: testo AI con riferimento alle spese future rilevanti — **solo utenti Pro** | Should |
| CO-15 | Notifica push "Spesa imminente con budget ridotto" quando una ricorrente è prevista entro 3 giorni e il FtD disponibile è inferiore all'importo: testo AI con nome spesa e importo — **solo utenti Pro** | Should |
| CO-16 | Le notifiche push sono opt-in; il consenso è richiesto la prima volta che la Coach Card viene visualizzata da un utente Pro | Must |
| CO-17 | L'utente Pro può disabilitare le notifiche Coach dalle Impostazioni senza disabilitare le notifiche in-app di base | Should |

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

- **[Dashboard](../dashboard/epic.md)** — la Hero Card Coach è ospitata nella Home; il valore centro Donut è il riferimento per il FtD residuo
- **[Analytics](../analytics/epic.md)** — la sezione Coach completa è ospitata in /analytics; "Approfondisci" naviga qui
- **[Riepilogo Spese](../expense/summary/epic.md)** — fonte dati spese variabili manuali
- **[Open Banking](../open-banking/epic.md)** — fonte dati spese auto-importate; le transazioni pending_review sono escluse dall'analisi Coach
- **[Budget](../budget/epic.md)** — fonte dati spese ricorrenti future (trigger CO-15)
- **[Notifiche](../notification/epic.md)** — le notifiche push del Coach si appoggiano all'infrastruttura notifiche esistente

> **Requisito tecnico:** richiede una Supabase Edge Function e una API key **Gemini (Google)**. Va impostata manualmente nelle variabili d'ambiente Supabase prima del deploy.
