# DreamJar — Data Model

**Versione:** 1.0 · Maggio 2026
**Scope:** MVP v1 — Dashboard, Onboarding, Goals

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
| `bucket` | enum | `fixed` · `leisure` · `unexpected` · `utilities` · `other` |
| `active` | boolean | Default true |
| `created_at` | timestamptz | |

**Logica "In arrivo":** le spese con `day_of_month` nei prossimi 7 giorni dal giorno corrente vengono mostrate in Home, ordinate per data crescente.

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
        text note
        date expense_date
        timestamptz created_at
    }

    users ||--|| profiles : "ha"
    users ||--o{ goals : "ha"
    users ||--o{ recurring_expenses : "ha"
    users ||--o{ expense_typologies : "ha"
    users ||--o{ expenses : "ha"
    expense_typologies ||--o{ expenses : "classifica"
```

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
