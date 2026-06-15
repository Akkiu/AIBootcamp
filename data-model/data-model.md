# DreamJar — Data Model

**Versione:** 1.4 · Giugno 2026
**Scope:** MVP v1 + Budget, Expense Summary, Expense Calendar, Notifiche, Coach AI, Open Banking

---

## Entità principali

### `users`
Gestita da Supabase Auth. Estesa con un profilo applicativo.

| Campo | Tipo | Note |
|-------|------|------|
| `id` | uuid PK | Supabase Auth user ID |
| `email` | text | |
| `full_name` | text | Usato nel saluto personalizzato |
| `created_at` | timestamptz | |

---

### `profiles`
Un record per utente. Contiene il setup budget inserito nell'onboarding.

| Campo | Tipo | Note |
|-------|------|------|
| `id` | uuid PK FK → users.id | |
| `name` | text | Nome utente (da raw_user_meta_data al signup) |
| `email` | text | Copia dell'email da auth.users |
| `monthly_income` | numeric | Stipendio mensile netto |
| `fixed_expenses` | numeric | Budget mensile Spese fisse |
| `leisure` | numeric | Budget mensile Svago |
| `unexpected` | numeric | Budget mensile Imprevisti |
| `utilities` | numeric | Budget mensile Utenze |
| `other` | numeric | Budget mensile Altro |
| `onboarding_completed` | boolean | Default false. True dopo step 5 |
| `onboarding_data` | jsonb | Dati grezzi dell'onboarding (usati in transizione) |
| `created_at` | timestamptz | |
| `updated_at` | timestamptz | |

**Campo calcolato (non persistito):**
```
free_to_dream = monthly_income - fixed_expenses - leisure - unexpected - utilities - other
```

---

### `goals`
Obiettivi di risparmio dell'utente.

| Campo | Tipo | Note |
|-------|------|------|
| `id` | uuid PK | |
| `user_id` | uuid FK → users.id | |
| `name` | text | Es. "Viaggio in Asia" |
| `emoji` | text | Es. "✈️" |
| `target_amount` | numeric | Importo obiettivo |
| `saved_amount` | numeric | Importo già accantonato. Default 0 |
| `target_date` | date | Data target opzionale |
| `status` | enum | `active` · `completed` |
| `created_at` | timestamptz | |
| `updated_at` | timestamptz | |

**Campo calcolato:**
```
progress_pct  = saved_amount / target_amount * 100
amount_left   = target_amount - saved_amount
```

---

### `expense_typologies`
Tipologie di spesa create dall'utente (es. "Cena", "Aperitivo", "Dentista"). Alcune sono pre-caricate al primo accesso come suggerimenti; tutte sono modificabili e riutilizzabili per le spese future.

| Campo | Tipo | Note |
|-------|------|------|
| `id` | uuid PK | |
| `user_id` | uuid FK → users.id | |
| `name` | text | Es. "Cena", "Aperitivo", "Dentista" |
| `bucket` | enum | `fixed` · `leisure` · `unexpected` · `utilities` · `other` · `goal` — bucket di default suggerito per questa tipologia |
| `emoji` | text | Opzionale. Es. "🍽️" |
| `is_preset` | boolean | True per le tipologie pre-caricate dal sistema. Non eliminabili. |
| `created_at` | timestamptz | |

**Tipologie preset (caricate alla creazione del profilo):**

| name | bucket | emoji |
|------|--------|-------|
| Affitto / Mutuo | fixed | 🏠 |
| Trasporti | fixed | 🚌 |
| Luce | utilities | ⚡ |
| Gas | utilities | 🔥 |
| Internet / Telefono | utilities | 📡 |
| Cena fuori | leisure | 🍽️ |
| Aperitivo | leisure | 🥂 |
| Abbigliamento | leisure | 👗 |
| Concerti / Eventi | leisure | 🎵 |
| Dentista | unexpected | 🦷 |
| Farmacia | unexpected | 💊 |
| Auto / Riparazioni | unexpected | 🚗 |
| Spesa supermercato | other | 🛒 |
| Carburante | other | ⛽ |
| Viaggi | goal | ✈️ |
| Acquisti speciali | goal | 🎁 |

L'utente può aggiungere tipologie personalizzate senza limite. Le tipologie vengono mostrate ordinate per: preset prima, poi custom per data di creazione decrescente (le più recenti in cima).

---

### `recurring_expenses`
Spese fisse e ricorrenti inserite dall'utente (onboarding + gestione successiva). Usate per la sezione "In arrivo" della Home.

| Campo | Tipo | Note |
|-------|------|------|
| `id` | uuid PK | |
| `user_id` | uuid FK → users.id | |
| `name` | text | Es. "Affitto", "Spotify" |
| `amount` | numeric | |
| `day_of_month` | int | Giorno del mese di addebito (1–31) |
| `month_of_year` | int | 1–12. Nullable. Obbligatorio se `frequency = annual` |
| `frequency` | enum | `monthly` · `annual` — default `monthly` |
| `bucket` | enum | `fixed` · `leisure` · `unexpected` · `utilities` · `other` |
| `active` | boolean | Default true |
| `created_at` | timestamptz | |

**Logica "In arrivo":** le spese con `day_of_month` nei prossimi 7 giorni dal giorno corrente vengono mostrate in Home, ordinate per data crescente.

**Logica Calendario:** le spese `monthly` appaiono ogni mese nel `day_of_month` configurato. Le spese `annual` appaiono una volta l'anno nel `month_of_year` e `day_of_month` configurati.

---

### `expenses`
Spese manuali registrate dall'utente dalla Dashboard.

| Campo | Tipo | Note |
|-------|------|------|
| `id` | uuid PK | |
| `user_id` | uuid FK → users.id | |
| `name` | text | Campo libero opzionale (legacy, affiancato da `note`) |
| `amount` | numeric | Importo > 0 |
| `bucket` | enum | `fixed` · `leisure` · `unexpected` · `utilities` · `other` · `goal` |
| `typology_id` | uuid FK → expense_typologies.id | Tipologia selezionata. Nullable |
| `recurring_expense_id` | uuid FK → recurring_expenses.id | Nullable. Valorizzato se la spesa è il pagamento di una ricorrente (usato per lo stato "pagata" nel Calendario) |
| `note` | text | Descrizione libera opzionale |
| `expense_date` | date | Data della spesa. Default oggi. |
| `spent_at` | timestamptz | Timestamp pieno della spesa (derivato da expense_date). Default now(). |
| `created_at` | timestamptz | |

**Campo calcolato per il bucket mensile (lato client):**
```
spent_this_month = SUM(amount) WHERE bucket = ? AND expense_date IN current month
remaining        = profiles.<bucket_budget> - spent_this_month
```

---

### `notification_reads`
Traccia le notifiche lette dall'utente. Le notifiche non sono persistite — vengono calcolate al volo confrontando `recurring_expenses` con la data corrente. Solo lo stato "letta" viene salvato, identificando la spesa ricorrente e la scadenza specifica.

| Campo | Tipo | Note |
|-------|------|------|
| `id` | uuid PK | |
| `user_id` | uuid FK → users.id | |
| `recurring_expense_id` | uuid FK → recurring_expenses.id | |
| `due_date` | date | Data di scadenza specifica per cui la notifica è stata letta (es. 2026-05-28) |
| `read_at` | timestamptz | |

**Vincolo di unicità:** `(user_id, recurring_expense_id, due_date)` — una notifica per scadenza può essere letta una sola volta.

**Logica badge:** il conteggio notifiche non lette è calcolato come: notifiche generate (spese in scadenza nei 3 giorni) − record presenti in `notification_reads` per le stesse `(recurring_expense_id, due_date)`.

---

## Entity Relationship Diagram

```mermaid
erDiagram
    users {
        uuid id PK
        text email
        text full_name
        timestamptz created_at
    }

    profiles {
        uuid id PK_FK
        numeric monthly_income
        numeric fixed_expenses
        numeric leisure
        numeric unexpected
        numeric utilities
        numeric other
        boolean onboarding_completed
        timestamptz updated_at
    }

    goals {
        uuid id PK
        uuid user_id FK
        text name
        text emoji
        numeric target_amount
        numeric saved_amount
        date target_date
        enum status
        timestamptz created_at
        timestamptz updated_at
    }

    recurring_expenses {
        uuid id PK
        uuid user_id FK
        text name
        numeric amount
        int day_of_month
        int month_of_year
        enum frequency
        enum bucket
        boolean active
        timestamptz created_at
    }

    expense_typologies {
        uuid id PK
        uuid user_id FK
        text name
        enum bucket
        text emoji
        boolean is_preset
        timestamptz created_at
    }

    expenses {
        uuid id PK
        uuid user_id FK
        numeric amount
        enum bucket
        uuid typology_id FK
        uuid recurring_expense_id FK
        text note
        date expense_date
        timestamptz created_at
    }

    notification_reads {
        uuid id PK
        uuid user_id FK
        uuid recurring_expense_id FK
        date due_date
        timestamptz read_at
    }

    coach_messages {
        uuid id PK
        uuid user_id FK
        text message
        date month
        timestamptz generated_at
        jsonb context_snapshot
    }

    bank_connections {
        uuid id PK
        uuid user_id FK
        text provider
        text account_uid
        text institution_name
        enum status
        timestamptz valid_until
        timestamptz last_sync_at
        timestamptz created_at
    }

    bank_transactions {
        uuid id PK
        uuid user_id FK
        uuid bank_connection_id FK
        text external_id
        date booking_date
        numeric amount
        text merchant_raw
        text merchant_normalized
        text category_guess
        uuid typology_id FK
        enum confidence
        enum status
        uuid expense_id FK
        timestamptz imported_at
        timestamptz created_at
    }

    notification_preferences {
        uuid id PK
        uuid user_id FK
        boolean recurring_reminders_enabled
        boolean goal_milestones_enabled
        boolean coach_push_enabled
        boolean bank_transactions_enabled
        boolean bank_auto_import_notify
        timestamptz updated_at
    }

    users ||--|| profiles : "ha"
    users ||--o{ goals : "ha"
    users ||--o{ recurring_expenses : "ha"
    users ||--o{ expense_typologies : "ha"
    users ||--o{ expenses : "ha"
    users ||--o{ notification_reads : "ha"
    users ||--o{ coach_messages : "ha"
    users ||--o{ bank_connections : "ha"
    users ||--o{ bank_transactions : "ha"
    users ||--|| notification_preferences : "ha"
    expense_typologies ||--o{ expenses : "classifica"
    recurring_expenses ||--o{ expenses : "pagata da"
    recurring_expenses ||--o{ notification_reads : "letta in"
    bank_connections ||--o{ bank_transactions : "contiene"
    bank_transactions ||--o| expenses : "diventa"
    expense_typologies ||--o{ bank_transactions : "suggerita in"
```

---

### `coach_messages`
Cache dei messaggi AI generati dal Coach. Evita chiamate ridondanti all'LLM ad ogni apertura dell'app.

| Campo | Tipo | Note |
|-------|------|------|
| `id` | uuid PK | |
| `user_id` | uuid FK → users.id | |
| `message` | text | Messaggio AI generato dalla Edge Function |
| `month` | date | Primo giorno del mese di riferimento (es. 2026-06-01) — usato per invalidare il messaggio al cambio mese |
| `generated_at` | timestamptz | Timestamp generazione. Il messaggio è considerato valido per 2 ore se nessuna spesa è stata registrata nel frattempo |
| `context_snapshot` | jsonb | Snapshot del contesto passato all'LLM (bucket balances, spese, ricorrenti future). Utile per debug e per rilevare se il contesto è cambiato |

**LLM:** Gemini (Google). La Edge Function chiama l'API Gemini con il contesto finanziario del mese.

**Logica di invalidazione:** la Edge Function usa il messaggio in cache se:
- `month` = mese corrente, E
- `generated_at` < 2 ore fa, E
- nessuna riga in `expenses` con `created_at > generated_at` per quell'utente

In tutti gli altri casi chiama l'LLM e sovrascrive il record.

**Vincolo:** un solo record per `(user_id, month)` — upsert su conflitto.

---

### `bank_connections`
Connessioni bancarie attive degli utenti Pro tramite Enable Banking (PSD2). Un utente può avere più account collegati.

| Campo | Tipo | Note |
|-------|------|------|
| `id` | uuid PK | |
| `user_id` | uuid FK → users.id | |
| `provider` | text | Default `'enable_banking'` |
| `account_uid` | text | ID account Enable Banking |
| `institution_name` | text | Nome banca (es. "Intesa Sanpaolo") |
| `status` | enum | `active` · `disconnected` · `expired` |
| `valid_until` | timestamptz | Scadenza del consenso PSD2 |
| `last_sync_at` | timestamptz | Ultima sync completata con successo |
| `created_at` | timestamptz | |
| `updated_at` | timestamptz | |

---

### `bank_transactions`
Transazioni bancarie ricevute da Enable Banking. Rappresentano lo stato di processing di ogni transazione: dal raw import fino all'eventuale conversione in `expenses`.

| Campo | Tipo | Note |
|-------|------|------|
| `id` | uuid PK | |
| `user_id` | uuid FK → users.id | |
| `bank_connection_id` | uuid FK → bank_connections.id | |
| `account_uid` | text | ID account Enable Banking |
| `external_id` | text | ID transazione dalla banca (idempotenza) |
| `booking_date` | date | Data di addebito |
| `amount` | numeric(12,2) | Negativo = spesa, positivo = entrata |
| `currency` | text | Default `'EUR'` |
| `merchant_raw` | text | Descrizione originale dalla banca |
| `merchant_normalized` | text | Uppercase, spazi normalizzati (usata per matching) |
| `category_guess` | text | Bucket suggerito dal sistema (`fixed`/`leisure`/...) |
| `typology_id` | uuid FK → expense_typologies.id | Nullable. Popolato se il sistema individua una tipologia |
| `confidence` | enum | `auto_recurring` · `auto_preset` · `low` |
| `status` | enum | `pending_review` · `imported` · `ignored` · `duplicate` |
| `expense_id` | uuid FK → expenses.id | Nullable. Popolato dopo import |
| `imported_at` | timestamptz | |
| `reviewed_at` | timestamptz | |
| `created_at` | timestamptz | |
| `updated_at` | timestamptz | |

**Vincolo unique:** `(bank_connection_id, external_id)` — garantisce idempotenza durante la sync.

**Logica `confidence`:**
- `auto_recurring`: merchant normalizzato corrisponde a una `recurring_expenses` attiva con importo ±5%
- `auto_preset`: merchant normalizzato è nella lista preset hardcoded (Esselunga, Conad, Netflix, Spotify…)
- `low`: nessun match → resta in `pending_review`

**Filtri applicati prima del matching:** `amount > 0` (entrate), merchant contenente GIROCONTO / BONIFICO A SE / TOP UP → transazione ignorata. Dedup: stessa banca, importo ±10%, data ±2 giorni → status `duplicate`.

---

### `notification_preferences`
Preferenze utente per tutte le notifiche dell'app. Un record per utente.

| Campo | Tipo | Note |
|-------|------|------|
| `id` | uuid PK | |
| `user_id` | uuid FK → users.id | |
| `recurring_reminders_enabled` | boolean | Default `true` — reminder spese ricorrenti in arrivo (in-app) |
| `goal_milestones_enabled` | boolean | Default `true` — notifiche milestone obiettivi (in-app) |
| `coach_push_enabled` | boolean | Default `false` — notifiche push Coach AI (solo Pro) |
| `bank_transactions_enabled` | boolean | Default `true` — push per sync bancaria (solo Pro) |
| `bank_auto_import_notify` | boolean | Default `false` — push anche per auto-import silenzioso (solo Pro) |
| `created_at` | timestamptz | |
| `updated_at` | timestamptz | |

**Vincolo:** un solo record per `user_id`.

---

## Tabelle infrastrutturali (email)

Tabelle operative create dalla migrazione email infra (22 maggio). Non sono tabelle di prodotto — non espongono dati utente.

| Tabella | Scopo |
|---------|-------|
| `email_send_log` | Audit trail di tutti i tentativi di invio email |
| `email_send_state` | Config rate-limit e throughput (riga singola) |
| `suppressed_emails` | Unsubscribe, bounce, complaint (append-only) |
| `email_unsubscribe_tokens` | Token per link di disiscrizione |

Accesso riservato a `service_role`. RLS abilitata su tutte.

---

## Note

- Row Level Security (RLS) abilitata su tutte le tabelle: ogni utente accede solo ai propri dati.
- `profiles.onboarding_completed = false` → la Home mostra placeholder e CTA setup invece dei numeri reali.
- I valori dei bucket in `profiles` sono importi assoluti mensili, non percentuali. La % mostrata in UI è calcolata sul client: `importo / monthly_income * 100`.
- `expenses.spent_at` è un timestamptz derivato da `expense_date` (settato a mezzogiorno del giorno scelto). `expense_date` è il campo canonico per i calcoli mensili.
