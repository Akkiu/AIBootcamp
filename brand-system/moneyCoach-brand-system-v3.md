# moneyCoach — Brand System v3
> Blend tra base (giocoso, umano) e Fineco (professionale, strutturato).
> Caldo ma affidabile. Incoraggiante ma preciso.

---

## 1. Brand Identity

### Mission
Help people who struggle to save for travel or special purchases by giving them a clear,
motivating, and trustworthy system to manage fixed expenses, variable expenses, and saving goals.

### Tagline
**"Save with confidence."** (EN) · **"Risparmia con sicurezza."** (IT)

### Personality
moneyCoach v3 is a **knowledgeable friend you trust with money** — warm enough to feel human, sharp enough to feel reliable. The brand balances encouragement with clarity: it celebrates wins without feeling like a toy, and shows numbers without feeling like a bank.

| Trait | What it means in practice |
|---|---|
| Trustworthy | Structure and precision in data, no ambiguity in numbers |
| Encouraging | Progress is always acknowledged, never ignored |
| Clear | Information is scannable, hierarchy is obvious |
| Human | Informal "tu", real language, no fintech jargon |
| Measured | Celebrations are earned, not automatic |

### Voice — DO / DON'T

| ✅ DO | ❌ DON'T |
|---|---|
| "Hai €340 liberi questo mese — ottimo punto di partenza." | "Stai VOLANDO 🚀🚀🚀 Sei una star!!" |
| "La bolletta arriva il 18 maggio. Sei coperto." | "Avviso: spesa prevista €65,00." |
| "Sei al 50% del tuo obiettivo. Continua così 🎯" | "Deficit rilevato nel budget mensile." |
| "Qualcosa non ha funzionato. Riprova." | "Errore critico nel sistema." |
| Always use informal "tu" in Italian | Never use formal "Lei" |
| Emoji in goal names and milestone completions | Emoji in navigation, tables, or error states |

---

## 2. Color System

```css
:root {
  /* Primary — Teal */
  --mc-teal:           #1FA884;   /* Main brand color — growth, confidence, forward motion */
  --mc-teal-dark:      #178A6D;   /* Hover / pressed */
  --mc-teal-light:     #E6F7F3;   /* Subtle tint for backgrounds */

  /* Accent — Orange */
  --mc-orange:         #F5820A;   /* CTAs, active states, key highlights */
  --mc-orange-dark:    #D46E00;   /* Hover / pressed */
  --mc-orange-light:   #FEF3E8;   /* Subtle tint */

  /* Backgrounds */
  --mc-bg:             #FAFAF8;   /* App background — warm white from v1 */
  --mc-surface:        #FFFFFF;   /* Cards and sheets */
  --mc-dark-bg:        #0A2347;   /* Hero cards, splash — navy from v2 */
  --mc-dark-surface:   #0F2E5A;

  /* Category colors */
  --mc-fixed:          #0A2347;   /* Fixed expenses — navy: predictable, structured */
  --mc-variable:       #F5820A;   /* Variable expenses — orange: warm, not alarming */
  --mc-buffer:         #4A7FC1;   /* Buffer — mid blue: calm, protective */
  --mc-goal:           #1FA884;   /* Goals — teal: aspirational, brand color */

  /* Text */
  --mc-ink:            #1A2B40;   /* Primary — dark navy, never pure black */
  --mc-ink-2:          #3D5278;   /* Secondary */
  --mc-muted:          #7A8BA8;   /* Hints, placeholders */

  /* Semantic */
  --mc-positive:       #1FA884;   /* Positive balance, success */
  --mc-negative:       #D64045;   /* Negative balance — used sparingly */
  --mc-divider:        #E4E9F0;   /* Borders, separators */
}
```

### Color Meaning
- **Teal** = growth, confidence, goals achieved. Primary brand color — hero numbers, CTAs on light bg, goal fills.
- **Orange** = action, energy, key moments. CTAs on dark bg, active nav, highlights.
- **Navy** = structure, reliability. Dark hero cards, fixed expense bucket, primary text.
- **Mid blue** = protection, stability. Buffer bucket only.
- **Red** = negative balance and system errors only. Never used for expense categories.
- **Warm white** = the default canvas — keeps the app from feeling cold or clinical.

---

## 3. Typography

### Fonts
```
Display / Numbers / Logo → Plus Jakarta Sans 700, 800
Body / UI / Labels       → DM Sans 400, 500
```
Import: `https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap`

> **Why this pair:** Plus Jakarta Sans (geometric, confident) handles numbers and headlines — giving structure. DM Sans (humanist, warm) handles body and labels — keeping the tone human. Professional structure, human delivery.

### Hierarchy

| Role | Font | Weight | Notes |
|---|---|---|---|
| Hero numbers (€ amounts) | Plus Jakarta Sans | 800 | Tight tracking, tabular figures |
| Screen titles | Plus Jakarta Sans | 700 | Confident, not loud |
| Section headings | Plus Jakarta Sans | 700 | |
| Body text | DM Sans | 400 | Readable, warm |
| Labels / captions | DM Sans | 500 | |
| Supporting / hints | DM Sans | 300 | |

### Rules
- Financial numbers always use **Plus Jakarta Sans 800**, color `--mc-teal` (positive) or `--mc-negative` (negative).
- **Sentence case** everywhere. ALL CAPS only for short overline labels ("FREE TO DREAM", "QUESTO MESE").
- Emoji allowed in goal names, onboarding steps (one per screen), and milestone completions.
- Never use Syne, Inter, Roboto, or system fonts.

---

## 4. Logo

### Wordmark
```
moneyCoach
```
- "money" → Plus Jakarta Sans 800, `--mc-ink`
- "Coach" → Plus Jakarta Sans 800, `--mc-teal`
- Always lowercase "money", always Title case "Coach". Never alter this.

### Icon Mark
A navy rounded square (`--mc-dark-bg`) containing a white geometric arc (from v2's Fineco-inspired symbol), with a small teal-filled circle at the arc's endpoint. The mark communicates: *direction + growth*.

### Variants

| Variant | When to use |
|---|---|
| Full (mark + wordmark) | Splash screen, onboarding, settings |
| Mark only | App icon, compact placements |
| Reversed (white wordmark, orange "Coach") | Dark hero cards |

---

## 5. Iconography

**Navigation and UI actions** → Lucide outline icons, 20px, stroke-width 1.5. Default: `--mc-muted`. Active: `--mc-teal`.

**Expense categories** → emoji (curated set below). Emoji bring warmth to an otherwise data-heavy screen without overwhelming it.

**Goal names** → user-assigned emoji, always.

No emoji in: navigation bar, data tables, error states, form labels.

### Category Emoji Map

| Category | Emoji |
|---|---|
| Spese fisse (generic) | 📌 |
| Affitto / mutuo | 🏠 |
| Bollette | ⚡ |
| Abbonamenti | 🔁 |
| Spese variabili (generic) | 🛍️ |
| Ristoranti / cene | 🍽️ |
| Concerti / eventi | 🎵 |
| Buffer emergenze | 🛡️ |
| Auto / riparazioni | 🚗 |
| Salute / dentista | 🦷 |
| Obiettivi (generic) | 🎯 |
| Viaggi | ✈️ |
| Acquisti speciali | 🎁 |
| Milestone 100% | 🏆 |

---

## 6. App Concept & Key Screens

### The four-bucket model

Every euro of salary falls into one of four buckets:

1. **Spese fisse** — Color: `--mc-fixed` (navy)
2. **Spese variabili** — Color: `--mc-variable` (orange)
3. **Buffer emergenze** — Color: `--mc-buffer` (mid blue)
4. **Obiettivi** — Color: `--mc-goal` (teal)

The hero of every screen: **"Free to Dream"** — shown large, in teal, with Plus Jakarta Sans 800.

### Key UI patterns
- **Hero card**: navy bg, "FREE TO DREAM" overline in white DM Sans 500, amount in white Plus Jakarta Sans 800, positive state in teal / negative in red
- **Bucket cards**: white surface, 4px colored left-border per bucket, amount in ink 700, % in muted. Subtle shadow.
- **Goal progress bars**: teal fill on `--mc-divider` track, 8px height, fully rounded ends
- **CTAs primary**: `--mc-teal` fill, white label, 10px radius
- **CTAs on dark bg**: `--mc-orange` fill, white label
- **Navigation**: bottom bar, teal active icon + label, muted inactive

---

## 7. Motion Principles

- **Ease-out** for standard transitions — 200ms. Crisp, not stiff.
- **Subtle spring** on milestone completion (100% goal) only — one meaningful bounce.
- **Count-up animation** for monetary amounts on screen load — 350ms ease-out.
- **Confetti** only at 100% goal completion. Not at 25/50/75%.
- Motion reinforces progress — never decorates idle states.

---

## 8. Tone by Context

| Context | Tone | Example copy |
|---|---|---|
| Onboarding | Warm, welcoming | "Parliamo un po' delle tue spese fisse 👋" |
| Home | Grounded, positive | "Hai €340 disponibili. Buon mese." |
| Budget screen | Clear, no fluff | Clean numbers only |
| Goals screen | Focused, aspirational | "Sei al 68% del tuo viaggio ✈️" |
| Expense reminder | Friendly, factual | "La bolletta arriva il 18 maggio — sei coperto." |
| Milestone 100% | Celebratory, earned | "🏆 Obiettivo raggiunto. Ottimo lavoro!" |
| Empty state | Encouraging, light | "Nessun obiettivo ancora. Qual è il tuo primo sogno?" |
| Error state | Calm, no blame | "Qualcosa non ha funzionato. Riprova." |

---

## 9. v1 / v2 / v3 — Comparison

| Dimension | v1 Base (Playful) | v2 Fineco (Premium) | v3 Blend |
|---|---|---|---|
| Primary color | Green `#3DBF7F` | Navy `#0A2347` | Teal `#1FA884` |
| Accent | Yellow `#FFB830` | Orange `#F5820A` | Orange `#F5820A` |
| Dark hero | Midnight `#1A1E2E` | Navy `#0A2347` | Navy `#0A2347` |
| Background | Warm white `#FAFAF8` | Cool grey `#F4F6FA` | Warm white `#FAFAF8` |
| Display font | Syne | Plus Jakarta Sans | Plus Jakarta Sans |
| Body font | DM Sans | Plus Jakarta Sans | DM Sans |
| Emoji use | First-class, frequent | Rare, goals only | Curated: categories + milestones |
| Tone | Supportive friend | Reliable companion | Trusted knowledgeable friend |
| Celebrations | Springy + confetti always | Minimal, no confetti | Spring + confetti at 100% only |
| Target user | Giulia, 28 | Marco, 42 | Both |

---

*moneyCoach Brand System v3 — balanced · warm-professional · Lovable-ready*
