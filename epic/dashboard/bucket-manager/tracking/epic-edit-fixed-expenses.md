# Epic: Modifica Spese Fisse con Ricalcolo Automatico

**Stato:** Planned · Maggio 2026 · **Priorità:** Should — v1.1

> As a user, I want to update a fixed expense when its amount changes so that all my other bucket budgets adjust automatically without touching my dream allocation.

---

## Come funziona

L'utente può modificare l'importo di una spesa fissa ricorrente (es. affitto che aumenta, abbonamento che scade). Quando salva, il sistema ricalcola automaticamente i budget dei bucket variabili per far quadrare il totale con lo stipendio, mantenendo intatto l'importo destinato agli Obiettivi.

```
Dashboard → tap su bucket "Spese fisse" → lista spese fisse → tap su una spesa → modifica importo → Salva
                                                                                                    ↓
                                              Spese fisse aggiornate · Bucket variabili ricalcolati · Obiettivi invariati
```

### Logica di ricalcolo

Quando una spesa fissa cambia di Δ, il sistema distribuisce Δ proporzionalmente sui 4 bucket variabili (Svago, Imprevisti, Utenze, Altro) in base alla loro quota sul pool variabile totale:

```
pool_variabile = svago + imprevisti + utenze + altro

nuovo_bucket_i = bucket_i − (bucket_i / pool_variabile) × Δ
```

**Obiettivi e Free to Dream restano entrambi invariati.** Poiché il pool variabile diminuisce esattamente di Δ e le spese fisse aumentano di Δ, la somma rimane uguale allo stipendio e il Free to Dream non cambia.

**Esempio** — Affitto +€100 (Δ = +€100), pool variabile = €600:

| Bucket | Quota | Assorbimento | Nuovo importo |
|--------|-------|--------------|---------------|
| Svago €300 | 50% | −€50 | €250 |
| Imprevisti €150 | 25% | −€25 | €125 |
| Utenze €100 | 17% | −€17 | €83 |
| Altro €50 | 8% | −€8 | €42 |
| **Obiettivi** | — | **€0** | **invariato** |
| **Free to Dream** | — | **€0** | **invariato** |

Se il ricalcolo porta uno o più bucket variabili sotto €0, il salvataggio è bloccato e l'app chiede all'utente di rivedere manualmente la distribuzione.

---

## Requisiti

| # | Requisito | Priorità |
|---|-----------|----------|
| EF-01 | Dal dettaglio del bucket "Spese fisse", l'utente può vedere la lista delle spese ricorrenti con nome, importo e giorno del mese | Must |
| EF-02 | Tap su una spesa fissa → bottom sheet con importo modificabile (numpad), nome e giorno del mese | Must |
| EF-03 | Al salvataggio, il sistema ricalcola automaticamente i budget di Svago, Imprevisti, Utenze e Altro in proporzione alla loro allocazione corrente | Must |
| EF-04 | L'importo del bucket Obiettivi non viene mai modificato dal ricalcolo | Must |
| EF-05 | Dopo il salvataggio, i bucket card in Home mostrano i nuovi importi aggiornati | Must |
| EF-06 | Il Free to Dream rimane invariato dopo il ricalcolo (la variazione è assorbita interamente dai bucket variabili) | Must |
| EF-07 | Se il ricalcolo porta uno o più bucket variabili sotto zero, mostrare un avviso: "La variazione è troppo grande per essere distribuita automaticamente. Rivedi la tua allocazione." con CTA alla schermata Budget | Must |
| EF-08 | Preview del ricalcolo prima del salvataggio: mostrare nel bottom sheet i nuovi importi dei bucket variabili con variazione (+/−) rispetto all'attuale | Should |
| EF-09 | L'utente può eliminare una spesa fissa dalla lista — il ricalcolo si applica allo stesso modo | Should |
| EF-10 | L'utente può aggiungere una nuova spesa fissa dalla stessa lista | Should |
| EF-11 | Feedback visivo post-salvataggio: toast "Budget aggiornato 👍" | Should |
| EF-12 | Storico delle modifiche non richiesto — i valori correnti sono l'unica fonte di verità | Won't |

---

## Ricalcolo — casi limite

| Scenario | Comportamento |
|----------|---------------|
| Δ negativo (abbonamento eliminato o ridotto) | I bucket variabili aumentano proporzionalmente; Free to Dream e Obiettivi restano invariati |
| Δ = 0 (importo non cambiato) | Bottone "Salva" disabilitato, nessun ricalcolo |
| Pool variabile = €0 (tutti i bucket variabili già a zero) | Salvataggio bloccato; messaggio "Non c'è budget variabile da ridistribuire. Modifica manualmente i bucket." |
| Ricalcolo porta un bucket variabile < €0 | Salvataggio bloccato; avviso con CTA alla schermata Budget |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Lista spese fisse vuota | Placeholder + CTA "Aggiungi spesa fissa" |
| Modifica importo valida | Preview ricalcolo, bottone "Salva" attivo |
| Importo invariato rispetto al valore corrente | Bottone "Salva" disabilitato |
| Ricalcolo impossibile (bucket sotto zero) | Avviso inline, salvataggio bloccato |
| Salvataggio in corso | Spinner, form disabilitato |
| Errore di salvataggio | Toast "Errore. Riprova." |

---

## Dipendenze

- **[Dashboard](../../epic.md)** — i bucket card (D-04) e il Free to Dream hero (D-02) si aggiornano dopo ogni modifica
- **[Registrazione Spese Manuali](epic-expense-tracking.md)** — le spese registrate nel mese non vengono toccate dal ricalcolo; agisce solo sui budget allocati
- **Onboarding** — i valori iniziali dei bucket variabili (lifestyle quiz) sono il punto di partenza per la proporzione di ricalcolo
- **Goals / Obiettivi** — il budget del bucket Obiettivi è intoccabile da questo flusso
