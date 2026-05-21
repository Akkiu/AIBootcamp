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
| `monthly_income` | numeric | Stipendio mensile netto |
| `fixed_expenses` | numeric | Totale spese fisse mensili |
| `variable_expenses` | numeric | Totale spese variabili mensili |
| `buffer` | numeric | Buffer emergenze mensile |
| `onboarding_completed` | boolean | Default false. True dopo step 5 |
| `updated_at` | timestamptz | |

**Campo calcolato (non persistito):**
```
free_to_dream = monthly_income - fixed_expenses - variable_expenses - buffer
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

### `recurring_expenses`
Spese fisse e ricorrenti inserite dall'utente (onboarding + gestione successiva). Usate per la sezione "In arrivo" della Home.

| Campo | Tipo | Note |
|-------|------|------|
| `id` | uuid PK | |
| `user_id` | uuid FK → users.id | |
| `name` | text | Es. "Affitto", "Spotify" |
| `amount` | numeric | |
| `day_of_month` | int | Giorno del mese di addebito (1–31) |
| `bucket` | enum | `fixed` · `variable` · `buffer` |
| `active` | boolean | Default true |
| `created_at` | timestamptz | |

**Logica "In arrivo":** le spese con `day_of_month` nei prossimi 7 giorni dal giorno corrente vengono mostrate in Home, ordinate per data crescente.

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
        numeric variable_expenses
        numeric buffer
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

    users ||--|| profiles : "ha"
    users ||--o{ goals : "ha"
    users ||--o{ recurring_expenses : "ha"
```

---

## Note

- Row Level Security (RLS) abilitata su tutte le tabelle: ogni utente accede solo ai propri dati.
- `profiles.onboarding_completed = false` → la Home mostra placeholder e CTA setup invece dei numeri reali.
- I valori dei bucket in `profiles` sono importi assoluti mensili, non percentuali. La % mostrata in UI è calcolata sul client: `importo / monthly_income * 100`.
- La tabella `recurring_expenses` copre sia le spese fisse (bucket `fixed`) che quelle variabili ricorrenti (bucket `variable`). La distinzione guida solo il colore in UI.
