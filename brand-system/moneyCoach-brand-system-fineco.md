# moneyCoach — Brand System v2
> Ispirazione: Fineco Bank — professionale, moderno, affidabile.
> Alternativa alla v1 (playful/green). Stessa app, tono più premium e istituzionale.

---

## 1. Brand Identity

### Mission
Help people who struggle to save for travel or special purchases by giving them a clear,
confident, and structured system to manage fixed expenses, variable expenses, and saving goals.

### Tagline
**"Your money, under control."** (EN) · **"I tuoi soldi, sotto controllo."** (IT)

### Personality
moneyCoach v2 is a **smart, reliable financial companion** — not a bank, but almost as trustworthy as one. The brand is calm, precise, and empowering. Less celebration, more clarity.

| Trait | What it means in practice |
|---|---|
| Confident | Numbers are displayed boldly — no ambiguity |
| Structured | Information is hierarchical and scannable |
| Trustworthy | Navy and white convey stability |
| Modern | Clean geometry, no clutter |
| Empowering | Users feel in control, not coached |

### Voice — DO / DON'T

| ✅ DO | ❌ DON'T |
|---|---|
| "Questo mese hai €340 liberi da investire." | "Stai volando! 🚀 Sei incredibile!" |
| "Bolletta in arrivo il 18 maggio — €65." | "Ehi! Arriva la bolletta, sei pronto?" |
| "Obiettivo completato. Ottimo lavoro." | "CE L'HAI FATTA!! 🎉🎉🎉" |
| "Il tuo budget è bilanciato." | "I tuoi soldi sono in ottima salute 💪" |
| Use informal "tu" in Italian | Never use formal "Lei" |
| Emoji sparingly, only in goals and milestones | Never emoji in navigation or data |

---

## 2. Color System

```css
:root {
  /* Primary — Navy */
  --mc-navy:           #0A2347;   /* Main brand color — trust, depth, authority */
  --mc-navy-dark:      #061730;   /* Hover / pressed */
  --mc-navy-light:     #E8EDF5;   /* Subtle tint for backgrounds */

  /* Accent — Orange */
  --mc-orange:         #F5820A;   /* CTAs, highlights, active states */
  --mc-orange-dark:    #D46E00;   /* Hover / pressed */
  --mc-orange-light:   #FEF3E8;   /* Subtle tint */

  /* Backgrounds */
  --mc-bg:             #F4F6FA;   /* App background — cool grey, not white */
  --mc-surface:        #FFFFFF;   /* Cards and sheets */
  --mc-dark-bg:        #0A2347;   /* Hero cards, splash, dark elements */
  --mc-dark-surface:   #0F2E5A;

  /* Category colors — refined, desaturated palette */
  --mc-fixed:          #0A2347;   /* Fixed expenses — navy */
  --mc-variable:       #F5820A;   /* Variable expenses — orange */
  --mc-buffer:         #4A7FC1;   /* Buffer — mid blue */
  --mc-goal:           #2BB5A0;   /* Goals — teal */

  /* Text */
  --mc-ink:            #0A2347;   /* Primary — navy, never pure black */
  --mc-ink-2:          #3D5278;   /* Secondary */
  --mc-muted:          #7A8BA8;   /* Hints, placeholders */

  /* Semantic */
  --mc-positive:       #2BB5A0;   /* Positive balance, success */
  --mc-negative:       #D64045;   /* Negative balance, warning */
  --mc-divider:        #DDE3EE;   /* Borders, separators */
}
```

### Color Meaning
- **Navy** = trust, structure, authority. The dominant brand color — backgrounds, headers, primary text.
- **Orange** = action, energy, progress. Used exclusively for CTAs, active states, and key metrics.
- **Mid blue** = protection, security. Buffer bucket only.
- **Teal** = growth, goals, forward motion. Goal bucket and positive states.
- **Red** = alert only. Never used for category colors — only for negative balance or errors.

---

## 2. Typography

### Fonts
```
Display / Numbers / Logo → Plus Jakarta Sans 700, 800
Body / UI / Labels       → Plus Jakarta Sans 400, 500
```
Import: `https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;700;800&display=swap`

> **Why Plus Jakarta Sans:** closest Google Fonts equivalent to Avenir — geometric, humanist, neutral. Professional without being cold. Single family simplifies the system.

### Hierarchy

| Role | Font | Weight | Notes |
|---|---|---|---|
| Hero numbers (€ amounts) | Plus Jakarta Sans | 800 | Tight tracking, tabular figures |
| Screen titles | Plus Jakarta Sans | 700 | Clean, confident |
| Section headings | Plus Jakarta Sans | 600 | |
| Body text | Plus Jakarta Sans | 400 | |
| Labels / captions | Plus Jakarta Sans | 500 | |
| Supporting / hints | Plus Jakarta Sans | 300 | |

### Rules
- Financial numbers always use **weight 800**, color `--mc-navy` or `--mc-orange`.
- **ALL CAPS** allowed for short overline labels only (e.g. "FREE TO DREAM", "QUESTO MESE").
- Limit emoji: only in goal names and milestone notifications.
- Never use Syne, DM Sans, or display fonts — Plus Jakarta Sans is the only typeface.

---

## 4. Logo

### Wordmark
```
money COACH
```
- "money" → Plus Jakarta Sans 800, `--mc-navy`
- "COACH" → Plus Jakarta Sans 800, `--mc-orange`
- "money" lowercase, "COACH" all caps. Never alter this.

### Icon Mark
A navy rounded square containing a stylized white crescent/arc shape (inspired by Fineco's geometric symbol), with a small orange dot at the arc's endpoint. The mark communicates: *direction + precision*.

### Variants

| Variant | When to use |
|---|---|
| Full (mark + wordmark) | Splash screen, onboarding, settings |
| Mark only | App icon, compact placements |
| Reversed (white + orange on navy) | Dark hero cards |

---

## 5. Iconography

Use **Lucide** outline icons throughout — 20px, stroke-width 1.5. Default color: `--mc-muted`. Active: `--mc-orange`.

Emoji are limited to:
- Goal names (user-assigned)
- Milestone notifications (one emoji max)
- Onboarding steps (one per screen for warmth)

No emoji in navigation, data tables, or error states.

### Category Icon Map (Lucide)

| Category | Icon |
|---|---|
| Spese fisse | `home` |
| Affitto / mutuo | `building` |
| Bollette | `zap` |
| Abbonamenti | `repeat` |
| Spese variabili | `shopping-bag` |
| Ristoranti | `utensils` |
| Buffer emergenze | `shield` |
| Obiettivi | `target` |
| Viaggi | `map-pin` |
| Milestone | `check-circle` |

---

## 6. App Concept & Key Screens

Same four-bucket model as v1. Presentation is data-first, not emotion-first.

### The four-bucket model

1. **Spese fisse** — Color: `--mc-fixed` (navy)
2. **Spese variabili** — Color: `--mc-variable` (orange)
3. **Buffer emergenze** — Color: `--mc-buffer` (mid blue)
4. **Obiettivi** — Color: `--mc-goal` (teal)

### Key UI patterns
- **Hero card**: navy background, "FREE TO DREAM" in white overline (ALL CAPS, 500), amount in white weight-800, positive/negative state in teal or red
- **Bucket cards**: white surface, colored left-border (4px) per bucket, amount in navy 700, % in muted
- **Goal progress bars**: teal fill on `--mc-divider` track, thin (6px), no rounded ends
- **CTAs**: `--mc-orange` fill, white label, 8px radius. No gradients.
- **Navigation**: bottom bar with navy active state, muted inactive, no color-coded tabs

---

## 7. Motion Principles

- **Linear or ease-out** — no spring or bounce. Precision over playfulness.
- **Short**: 120ms micro-interactions, 250ms transitions.
- **Milestone**: single subtle scale-up animation (no confetti). Achievement badge fades in.
- **Count-up**: numbers animate on load, fast (400ms), ease-out.
- Motion is functional, never decorative.

---

## 8. Tone by Context

| Context | Tone | Example copy |
|---|---|---|
| Onboarding | Clear, welcoming | "Iniziamo con il tuo stipendio netto mensile." |
| Home | Precise, neutral | "Hai €340 disponibili questo mese." |
| Budget screen | Data-first | Clean numbers, no copy |
| Goals screen | Focused | "Mancano €680 al tuo obiettivo." |
| Expense reminder | Factual, direct | "Bolletta luce: €65 il 18 maggio." |
| Milestone reached | Concise, warm | "Obiettivo raggiunto. Ottimo lavoro." |
| Empty state | Neutral CTA | "Nessun obiettivo. Aggiungine uno." |
| Error state | Calm, factual | "Impossibile aggiornare. Riprova." |

---

## 9. v1 vs v2 — Key Differences

| Dimension | v1 (Playful) | v2 (Premium) |
|---|---|---|
| Primary color | Green `#3DBF7F` | Navy `#0A2347` |
| Accent | Yellow `#FFB830` | Orange `#F5820A` |
| Typography | Syne + DM Sans | Plus Jakarta Sans |
| Emoji use | First-class, frequent | Rare, goal-names only |
| Tone | Supportive friend | Reliable companion |
| Animations | Springy, confetti | Precise, minimal |
| Target user | Giulia, 28, Milano | Marco, 42, Torino |

---

*moneyCoach Brand System v2 — Fineco-inspired · premium · data-first*
