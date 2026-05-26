# Epic: Riepilogo Spese

**Stato:** Done · Maggio 2026 · **Priorità:** Should — v1.1

> As a user, I want to see all my recorded expenses and upcoming ones in one place so that I have a complete picture of the current month without jumping between buckets.

---

## Come funziona

Una schermata dedicata mostra il quadro completo delle spese del mese corrente, diviso in due sezioni:

1. **Spese registrate** — spese già sostenute, in ordine cronologico inverso (la più recente in cima).
2. **In arrivo questo mese** — spese ricorrenti/fisse già pianificate ma non ancora sostenute nel mese corrente (es. affitto, abbonamenti, rate). Ogni voce mostra la data prevista e l'importo.

```
Home → tap "Spese" (o voce nel menu) → Riepilogo Spese
         ↓
[In arrivo questo mese]  ← spese future pianificate
[Spese registrate]       ← spese già sostenute, cronologico inverso
```

Il mese di riferimento è lo stesso usato dal tracking: si resetta a inizio mese e lo storico dei mesi precedenti rimane consultabile tramite selettore mese. Nei mesi precedenti la sezione "In arrivo" non viene mostrata.

---

## Requisiti

| # | Requisito | Priorità |
|---|-----------|----------|
| ES-01 | Schermata "Riepilogo Spese" accessibile dalla navigazione principale | Must |
| ES-02 | Sezione "Spese registrate": lista spese del mese corrente in ordine cronologico inverso (più recente in cima) | Must |
| ES-03 | Ogni riga spesa registrata mostra: data, tipologia con emoji, bucket (con colore/icona), importo | Must |
| ES-04 | Totale speso nel mese mostrato in evidenza in cima alla schermata | Must |
| ES-05 | Sezione "In arrivo questo mese": lista delle spese ricorrenti/fisse pianificate ma non ancora sostenute nel mese corrente | Must |
| ES-06 | Ogni riga "in arrivo" mostra: data prevista, nome spesa, bucket, importo; ordinate per data crescente (la più vicina prima) | Must |
| ES-07 | Sezione "In arrivo" nascosta se non ci sono spese future nel mese corrente | Should |
| ES-08 | Stato vuoto se nessuna spesa registrata nel mese: placeholder + CTA "Aggiungi la tua prima spesa" | Must |
| ES-09 | Selettore mese (← mese precedente / mese corrente →) per consultare lo storico; nei mesi precedenti la sezione "In arrivo" non viene mostrata | Should |
| ES-10 | Tap su una spesa registrata → bottom sheet di dettaglio con tutti i campi (importo, bucket, tipologia, data, nota) | Should |
| ES-11 | Da dettaglio spesa: eliminazione con conferma → ricalcolo immediato Free to Dream e bucket | Should |
| ES-12 | Raggruppamento opzionale per giorno nella sezione "Spese registrate" (header di sezione con data e subtotale giornaliero) | Could |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Nessuna spesa registrata, nessuna in arrivo | Placeholder + CTA "Aggiungi la tua prima spesa" |
| Solo spese in arrivo (nessuna registrata ancora) | Sezione "In arrivo" visibile, sezione "Spese registrate" con stato vuoto |
| Solo spese registrate (nessuna in arrivo) | Sezione "Spese registrate" visibile, sezione "In arrivo" nascosta |
| Entrambe le sezioni con dati | Layout completo con entrambe le sezioni |
| Mese precedente (storico) | Solo sezione "Spese registrate", read-only, eliminazione disabilitata |
| Loading | Skeleton loaders sulle righe |
| Errore caricamento | Messaggio di errore + retry |

---

## Dipendenze

- **[Registrazione Spese Manuali](../bucket-manager/tracking/epic-expense-tracking.md)** — fonte dati per la sezione "Spese registrate" (EX-01/EX-07)
- **[Dashboard](../epic.md)** — la sezione "In arrivo questo mese" riusa la stessa fonte delle spese ricorrenti di D-08; il Free to Dream si aggiorna se una spesa viene eliminata da questa schermata
- **Onboarding** — il mese di riferimento è allineato al ciclo mensile dell'app; le spese fisse configurate in onboarding alimentano la sezione "In arrivo"
