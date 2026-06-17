# Epic: Header Coach

**Stato:** Done · **Priorità:** Should — v1.1

> As a user, I want the message at the top of the dashboard to reflect how my spending is going this month so that I always have a quick, honest read on my financial situation.

---

## Come funziona

La frase in cima alla Home (attualmente il saluto generico) diventa un messaggio contestuale che cambia in base a quanto budget mensile è ancora disponibile. Il tono è incoraggiante o allarmante a seconda della situazione, mai colpevolizzante.

Il valore di riferimento è il **Free to Dream rimanente** rispetto al **Free to Dream iniziale del mese** (calcolato al momento del reset mensile, dopo l'onboarding o dopo l'ultima modifica alle spese fisse).

```
ratio = free_to_dream_rimanente / free_to_dream_iniziale_del_mese
```

La frase si aggiorna in tempo reale ogni volta che viene registrata una spesa.

---

## Soglie e messaggi

| Soglia | Condizione | Messaggio | Stile |
|--------|------------|-----------|-------|
| Verde | ratio ≥ 80% | "Stai andando alla grande" | Colore positivo |
| Giallo | 60% ≤ ratio < 80% | "Stai gestendo in modo oculato" | Colore neutro |
| Arancione | 35% ≤ ratio < 60% | "Il budget si assottiglia, monitora le spese" | Colore attenzione |
| Rosso chiaro | 10% ≤ ratio < 35% | "Quasi al limite: solo l'essenziale da qui in poi" | Colore errore attenuato |
| Rosso | ratio < 10% | "Attenzione: il tuo sogno è a rischio!" | Rosso errore, testo in grassetto |

---

## Requisiti

| # | Requisito | Priorità |
|---|-----------|----------|
| HC-01 | La frase in cima alla Home mostra il messaggio contestuale basato sul ratio corrente | Must |
| HC-02 | Il messaggio si aggiorna in tempo reale dopo ogni spesa registrata | Must |
| HC-03 | Il messaggio sotto il 10% è in rosso e in grassetto | Must |
| HC-04 | Il saluto con nome utente e ora del giorno (D-01) rimane visibile, sopra o sotto il messaggio coach | Should |
| HC-05 | Al reset mensile (inizio mese) il ratio riparte da 100% e il messaggio torna alla soglia verde | Must |
| HC-06 | Se il Free to Dream iniziale è €0 (budget completamente allocato), il componente è nascosto | Should |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Nessuna spesa registrata (inizio mese) | Soglia verde — "Stai andando alla grande" |
| ratio < 10% | Messaggio rosso in grassetto |
| Free to Dream iniziale = €0 | Componente non mostrato |
| Free to Dream rimanente < 0 (sforato) | Messaggio rosso — stesso testo della soglia < 10% |

---

## Dipendenze

- **[Dashboard](../epic.md)** — il componente sostituisce o affianca il saluto D-01
- **[Registrazione Spese Manuali](../bucket-manager/tracking/epic-expense-tracking.md)** — ogni spesa registrata aggiorna il ratio e può cambiare il messaggio
- **[Modifica Spese Fisse](../bucket-manager/tracking/epic-edit-fixed-expenses.md)** — una modifica alle spese fisse aggiorna il Free to Dream iniziale del mese e ricalcola il ratio
