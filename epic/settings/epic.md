# Epic: Impostazioni

**Stato:** In Progress · Maggio 2026 · **Priorità:** Should — v1.1

> As a user, I want to manage my account and preferences so that I can keep my profile up to date and control the app's behaviour.

---

## Come funziona

La schermata Impostazioni è raggiungibile dalla Dashboard (navigazione secondaria). Mostra le informazioni dell'account corrente e permette di effettuare il logout. In v1.1 verrà estesa con modifica profilo, cambio password e preferenze notifiche.

```
Dashboard → Impostazioni → card Account (nome, email) · pulsante Esci
```

---

## Requisiti

| # | Requisito | Priorità | Stato |
|---|-----------|----------|-------|
| S-01 | Card account: mostra nome e email dell'utente loggato | Must | Built |
| S-02 | Pulsante "Esci" con conferma e redirect alla schermata Auth | Must | Built |
| S-03 | Modifica nome profilo inline | Should | Planned |
| S-04 | Cambio password (email + link reset) | Should | Planned |
| S-05 | Eliminazione account con conferma esplicita e cancellazione dati | Should | Planned |
| S-06 | Preferenze notifiche: attiva/disattiva reminder spese in arrivo | Could | Planned |
| S-07 | Preferenze notifiche: attiva/disattiva milestone obiettivi | Could | Planned |
| S-08 | Reset onboarding: ricomincia il setup budget da capo | Could | Planned |

---

## Stati

| Stato | Comportamento |
|-------|---------------|
| Normale | Card account con dati, pulsante Esci |
| Logout in corso | Spinner sul pulsante, interazione disabilitata |
| Profilo senza nome (S-03) | Mostra placeholder "—" fino alla modifica |

---

## Dipendenze

- **Auth** — `signOut()` reindirizza alla schermata di login
- **Onboarding** — S-08 (reset) riporta `profiles.onboarding_completed = false` e torna al flusso onboarding
- **Notifiche** (v1.1) — S-06 / S-07 controllano le preferenze legate all'epic Notifiche
