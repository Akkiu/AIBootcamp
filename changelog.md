# Changelog

---

## 2026-05-26

### Product — Nuove epiche
- **Epic: Analytics** — tab "Statistiche" con grafico a torta/anello delle spese per bucket, lista bucket espandibile per tipologia, confronto con budget allocato, navigazione mesi

---

## 2026-05-25

### Product — Nuove epiche
- **Epic: Budget** — tab dedicato alla configurazione finanziaria: stipendio, allocazioni bucket e spese ricorrenti (mensili)
- **Epic: Riepilogo Spese** — schermata cronologica con spese registrate e in arrivo nel mese corrente; include eliminazione spesa con ricalcolo immediato di bucket e Free to Dream
- **Epic: Calendario Spese** — vista calendario delle spese ricorrenti (mensili e annuali) con navigazione mesi, marker sui giorni e stato "pagata" per i giorni passati
- **Epic: Notifiche In-App** — avvisi in-app per spese ricorrenti in scadenza nei 3 giorni successivi; icona campana con badge, centro notifiche, stato letta/non letta

### Data Model — v1.2
- `recurring_expenses`: aggiunti `frequency` (`monthly` · `annual`) e `month_of_year` per supportare le spese annuali
- `expenses`: aggiunto `recurring_expense_id` FK nullable per collegare una spesa al pagamento di una ricorrente (stato "pagata" nel Calendario)
- Nuova tabella `notification_reads`: traccia le notifiche lette per `(user_id, recurring_expense_id, due_date)`

### Struttura epiche
- Creata cartella `epic/expense/` con le sottocartelle `summary/` (ex `dashboard/expense-summary`) e `calendar/` (ex `dashboard/expense-calendar`)
- Aggiornati tutti i link interni e il PRD

---

## 2026-05-23

### Dashboard
- BucketCard ridisegnata in orizzontale con gradienti
- Aggiunti pulsanti "+" per aggiungere spesa direttamente dalla card del bucket
- Chip % stipendio: mostra la percentuale del reddito allocata a ciascun bucket
- Chip editabile inline sulle card
- Card Sogni rimossa dalla Home (spostata altrove nel layout)
- Layout e colori aggiornati (fondo, colore stipendio)

### Expense Tracking
- Aggiunto campo data spesa nel dialog (DatePicker brandizzato, default oggi, max oggi)
- Validazione: salvataggio bloccato se data mancante

### Onboarding
- Quiz ridisegnato
- Mostra quota mensile disponibile per budget durante il setup

### DB — migrazione 6 bucket (`20260523130511`)
- Enum `expense_bucket` ricreato: `fixed · leisure · unexpected · utilities · other · goal`
- `profiles`: rimossi `variable_expenses` e `buffer`; aggiunti `leisure`, `unexpected`, `utilities`, `other`
- Preset typologies aggiornate a 16 voci con i nuovi bucket
- Reset onboarding per tutti gli utenti esistenti (necessario per rifare il setup con il nuovo modello)

### Sicurezza
- Rimossi permessi `EXECUTE` superflui su funzioni interne (`handle_new_user`, `seed_preset_typologies`, `update_updated_at_column`)
- Hardened `search_path` sulle funzioni pgmq wrapper

---

## 2026-05-22

### Auth & Email
- Template email di autenticazione tradotti in italiano (oggetto, corpo, email change, reauth)
- Font Manrope applicato alle email
- Route Lovable bypass aggiunta per preview

### Email Infra
- Setup infrastruttura email completa: pgmq, pg_cron, pg_net, supabase_vault
- Code queue (`auth_emails`, `transactional_emails`) con dead-letter queue
- Tabelle: `email_send_log`, `email_send_state`, `suppressed_emails`, `email_unsubscribe_tokens`
- Edge function `process-email-queue` con cron job ogni 5 secondi
- RPC wrappers per pgmq esposti solo a `service_role`

### Infra
- Rinominato progetto da `app-dreamjar` a `dreamjar` (site info pubblicato)

---

## 2026-05-21

### Onboarding
- Aggiunto flusso onboarding completo (5 step)
- DB: aggiunte colonne budget su `profiles` (`monthly_income`, `fixed_expenses`, `variable_expenses`, `buffer`)

### Dashboard
- Sezione Analytics aggiunta in Home
- Hero giara "Sogni" con gradiente sole
- Icona sostituita con giara DreamJar
- Rinominato in DreamJar (da MoneyCoach)

### Expense Tracking
- Aggiunta spesa manuale dalla Dashboard (`AddExpenseDialog`)
- DB: tabella `expenses` creata con `typology_id`, `note`, `expense_date`
- DB: tabella `expense_typologies` creata con RLS e seed preset
- DB: enum `expense_bucket` esteso con `goal`

### PWA
- Aggiunto manifest e icone PWA
- Aggiunto supporto offline

### Brand
- Applicato nuovo brand v2
- Font Outfit applicato

---

## 2026-05-20

### Auth
- Aggiunto flusso autenticazione (email/password + Google OAuth)
- Onboarding cache fix (stale data)

### Infra
- Cloud infrastructure abilitata (Supabase)
- DB: tabella `profiles` creata con RLS, trigger `handle_new_user`, trigger `updated_at`
- DB: tabelle `goals`, `recurring_expenses` create con RLS e indici
