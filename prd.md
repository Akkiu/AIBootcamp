# DreamJar — Product Requirements Document
**Versione:** 1.0 · Maggio 2025
**Stato:** Draft

---

## 01 · Problema

### Job to be done
> "Quando ricevo lo stipendio, voglio sapere immediatamente quanto posso spendere/risparmiare senza rischiare di arrivare a corto a fine mese, così posso pianificare i miei obiettivi senza ansia."

### Pain principale
L'utente non conosce il suo "residuo reale" dopo spese fisse e buffer. Senza quel numero, qualsiasi decisione di spesa o risparmio è fatta alla cieca. Le app di budgeting esistenti sono troppo complesse, colpevolizzanti o richiedono troppo effort di setup.

---

## 02 · Utenti target

### Persona A — Giulia, 28 anni · Milano
Primo lavoro con stipendio fisso. Affitto, bollette, aperitivi, cene fuori. Vuole risparmiare per un viaggio in Asia e comprare un'auto. Non riesce a capire perché i soldi finiscono sempre.

### Persona B — Marco, 42 anni · Torino
Famiglia con 2 figli. Mutuo, bollette, sport dei figli. Vuole costruire un buffer solido per imprevisti (auto, dentista) e pianificare una vacanza estiva senza stress.

---

<!-- ## 03 · Soluzione — il modello a 4 bucket

| Bucket | Descrizione | Colore |
|--------|-------------|--------|
| 💸 Spese fisse | Affitto, mutuo, abbonamenti | Corallo `#FF6B5B` |
| 🎨 Spese variabili | Cene, concerti, shopping | Lilla `#B08FFF` |
| 🛡️ Buffer emergenze | Auto, dentista, imprevisti | Azzurro `#6BBFFF` |
| 🌍 Obiettivi | Viaggi, acquisti, sogni | Verde `#3DBF7F` | -->

### Il numero chiave: "Free to Dream"
`Stipendio − spese fisse − spese variabili − buffer = Free to Dream`

Mostrato in modo prominente nella Home, aggiornato in tempo reale. È il cuore del prodotto.

---

## 04 · Scope MVP (v1)

### Onboarding (5 step)
Splash → Stipendio → Spese fisse → Lifestyle quiz → Primo obiettivo → [epic/onboarding/epic.md](epic/onboarding/epic.md)

### Home
Saluto personalizzato, hero number "Free to Dream", riepilogo 4 bucket, lista obiettivi con progress bar, spese ricorrenti in arrivo. → [epic/dashboard/epic.md](epic/dashboard/epic.md)

### Goals
Lista obiettivi attivi e completati, aggiunta nuovo obiettivo (nome, importo target, data target, emoji), progress bar con proiezione temporale, celebrazione milestone.

---

## 05 · Prioritizzazione MoSCoW

### Must (v1)
- Onboarding 5-step con setup budget iniziale
- Home con hero number "Free to Dream"
- Gestione e visualizzazione Goals
- Autenticazione (email + Google)

### Should (v1.1)
- Schermata Budget: breakdown modificabile 4 bucket
- Notifiche: reminder spese + milestone goal
- Registrazione spese manuale → [epic/dashboard/epic-expense-tracking.md](epic/dashboard/epic-expense-tracking.md)

### Could (v2)
- Digest settimanale via email/push
- App mobile nativa (iOS/Android)
- Offline mode con sync
- Tracker spesa supermercato: registrazione spese della spesa con confronto settimana/mese su mese

### Won't (v1)
- Integrazione bancaria (Enable Banking / PSD2) — rinviata al piano Pro in v3
- AI advisor / suggerimenti automatici
- Multi-valuta / conti multipli

---

## 06 · Metriche di successo (v1)

| Metrica | Target |
|---------|--------|
| Onboarding completion rate | > 70% |
| Retention D7 | > 40% |
| Goals creati per utente | ≥ 1.5 |
| Time to "Free to Dream" | < 3 min |
| CSAT post-onboarding | > 4.0 / 5 |
| DAU/MAU ratio | > 20% |

---

## 07 · Vincoli e assunzioni

- **Piattaforma v1:** Web app responsive (PWA-ready). App mobile nativa in v2.
- **Backend:** Necessario da subito per auth e sync dati.
- **Dati locali:** Supporto offline rinviato a v2. In v1, l'app richiede connessione.
- **Inserimento dati:** Manuale in v1 e nel piano gratuito. L'integrazione bancaria (PSD2) è riservata al piano a pagamento e richiede partnership, conformità ABI e tempi non compatibili con un MVP.
- **Monetizzazione:** Non nel scope v1. Il modello Freemium si basa sulla distinzione inserimento dati: **piano gratuito = manuale** (stipendio e spese inseriti a mano); **piano Pro = automatico** (sync con il conto bancario via PSD2 per importare stipendio e transazioni in automatico).

---

<!-- ## 08 · Stack tecnico consigliato

| Layer | Tecnologia | Motivazione |
|-------|-----------|-------------|
| Frontend | Next.js 14 + TypeScript | App router, SSR, PWA-ready. Tailwind CSS per styling coerente col brand. |
| Backend / BaaS | Supabase | Auth integrata, Postgres hosted, Row Level Security, realtime. Elimina mesi di infrastruttura custom. |
| Autenticazione | Supabase Auth | Email/password + Google OAuth. Magic link per onboarding frictionless. |
| Database | PostgreSQL (via Supabase) | Relazionale, GDPR-compliant, backup automatici. Nessun vendor lock-in. |
| Hosting | Vercel | Deploy automatico da Git, edge network, preview URL per ogni PR. |
| Notifiche (v1.1) | Resend + React Email | Email transazionali con alta deliverability. Push notification via web push API in v2. |
| Analytics | Posthog | Event tracking, funnel onboarding, session recording. Fondamentale per misurare le metriche del PRD. |
| Banking (v3) | Enable Banking API | Aggregazione PSD2 per il mercato italiano. Richiede registrazione come AISP presso Banca d'Italia. | -->

---

## 09 · Roadmap di rilascio

### v1 — MVP · Settimane 1–6
- Onboarding 5-step completo
- Home con hero number "Free to Dream"
- Gestione Goals (lista, aggiunta, progress bar)
- Calcolo real-time free_to_dream
- Autenticazione (email + Google)

### v1.1 — Consolidamento · Settimane 7–10
- Schermata Budget: breakdown modificabile 4 bucket
- Registrazione spese manuali
- Notifiche: reminder spese + milestone goal
- Digest settimanale via email
- Celebrazioni milestone animate

### v2 — Mobile & Monetizzazione · Mesi 4–6
- App mobile nativa (iOS + Android)
- Offline mode con sync
- Push notification native
- Piano Pro: Goals illimitati + feature avanzate
- Referral program
- **Tracker spesa supermercato:** registrazione veloce delle spese della spesa all'interno delle spese variabili, con storico e confronto settimana su settimana / mese su mese

### v3 — Piano Pro & Integrazione bancaria · Mesi 7–12
- **Piano Pro:** sblocca sync bancario automatico come upgrade dal piano gratuito (inserimento manuale)
- Connessione al conto bancario via PSD2 (Enable Banking)
- Import automatico stipendio e transazioni dal conto
- Categorizzazione automatica delle transazioni
- Suggerimenti basati su pattern di spesa

---

## 10 · Rischi principali

**🔴 Alto — Registrazione AISP**
L'iter regolatorio per operare come aggregatore bancario in Italia richiede 6–12 mesi e risorse legali. Va avviato in parallelo alla v2, non dopo.

**🔴 Alto — GDPR e dati finanziari**
I dati di reddito e spesa sono dati personali sensibili. Serve DPA con Supabase, informativa chiara, e diritto all'oblio implementato fin dalla v1.

**🟡 Medio — Onboarding drop-off**
5 step con inserimento dati è lungo per mobile. Monitorare con Posthog step per step. Se completion < 70%, semplificare step 3 e 4 per primi.

**🟡 Medio — Accuratezza del free_to_dream**
Se l'utente inserisce spese fisse errate o incomplete, il numero chiave è fuorviante. Soluzione: suggerimenti intelligenti in onboarding + revisione mensile guidata.

**🟢 Basso — Scalabilità Supabase**
Il piano free ha limiti di connessioni. Per MVP (sotto i 500 utenti attivi) non è un problema. Pianificare upgrade a piano Pro prima del lancio pubblico.
