# moneyCoach — Brand System
> Single source of truth for identity, tone, colors, and typography.
> Use this as the creative foundation for all UI decisions.

---

## 1. Brand Identity

### Mission
Help people who struggle to save for travel or special purchases by giving them a clear,
joyful, and motivating system to manage fixed expenses, variable expenses, and saving goals.

### Tagline
**"Save smart. Live full."** (EN) · **"Risparmia con testa. Vivi a pieno."** (IT)

### Personality
moneyCoach is a **supportive friend who happens to be great with money** — not a bank,
not a financial advisor, not a lecturer. The brand is warm, playful, and celebratory.

| Trait | What it means in practice |
|---|---|
| Joyful | Saving is progress toward dreams, not sacrifice |
| Honest | Clear numbers, zero hidden complexity |
| Encouraging | Every euro saved is a win worth celebrating |
| Human | Understands lifestyle, not just spreadsheets |
| Playful | Gamified progress, emoji, micro-celebrations |

### Voice — DO / DON'T

| ✅ DO | ❌ DON'T |
|---|---|
| "Ottimo lavoro! Sei al 50% del tuo viaggio 🎉" | "Deficit rilevato nel budget mensile." |
| "Questa settimana arriva la bolletta — sei pronto!" | "Avviso: spesa prevista €65,00." |
| "Hai risparmiato €247 questo mese. Stai volando 🚀" | "Budget surplus: €247,00." |
| "Parliamo un po' del tuo stile di vita 👋" | "Inserire dati obbligatori." |
| Always use informal "tu" in Italian | Never use formal "Lei" |
| Use emoji as emotional punctuation | Never use emoji in error states |

---

## 2. Color System

```css
:root {
  /* Primary */
  --mc-leaf:           #3DBF7F;   /* Growth, savings, success — main brand color */
  --mc-leaf-dark:      #27A06A;   /* Hover / pressed */
  --mc-leaf-light:     #E8FAF2;   /* Subtle tint for backgrounds */

  /* Accent */
  --mc-sun:            #FFB830;   /* Achievements, celebrations, milestones */
  --mc-sun-light:      #FFF5E0;

  /* Backgrounds */
  --mc-bg:             #FAFAF8;   /* App background — warm white, not pure white */
  --mc-surface:        #FFFFFF;   /* Cards and sheets */
  --mc-dark-bg:        #1A1E2E;   /* Hero cards, splash, dark elements */
  --mc-dark-surface:   #252A3E;

  /* Category colors — each expense type has its own color identity */
  --mc-fixed:          #3DBF7F;   /* Fixed expenses (rent, utilities) */
  --mc-variable:       #FF6B5B;   /* Variable expenses (dinners, concerts) */
  --mc-buffer:         #B08FFF;   /* Risk buffer (car repair, dentist) */
  --mc-goal:           #6BBFFF;   /* Saving goals (travel, purchases) */

  /* Text */
  --mc-ink:            #1A1E2E;   /* Primary — never pure black */
  --mc-ink-2:          #4A4F66;   /* Secondary */
  --mc-muted:          #7A8099;   /* Hints, placeholders */
}
```

### Color Meaning
- **Green** = savings, success, positive momentum. The dominant brand color.
- **Coral** = variable expenses only. Warm, not alarming — it is not an error color.
- **Lilac** = protection, buffer, safety net. Calm and reassuring.
- **Sky blue** = dreams and goals. Light, open, aspirational.
- **Sunrise yellow** = celebration, milestones, achievements. Never for warnings.
- **Midnight** = focus and depth. Used for hero elements to create contrast with the light UI.

---

## 3. Typography

### Fonts
```
Display / Numbers / Logo → Syne 800
Body / UI / Labels       → DM Sans 400, 500
```
Import: `https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap`

### Hierarchy

| Role | Font | Weight | Notes |
|---|---|---|---|
| Hero numbers (€ amounts) | Syne | 800 | Large, tight letter-spacing. Money should feel bold. |
| Screen titles | Syne | 800 | Distinctive, never generic |
| Section headings | Syne | 700 | |
| Body text | DM Sans | 400 | Warm and readable |
| Labels / captions | DM Sans | 500 | Slightly heavier for legibility |
| Supporting / hints | DM Sans | 300 | Creates contrast with bold numerals |

### Rules
- Financial numbers always use **Syne 800**. A big green number is the hero of every screen.
- Use **sentence case** everywhere. No ALL CAPS except very short overline labels.
- **Emoji are encouraged** in titles, goal names, notifications, and achievement states.
- Never use Arial, Inter, Roboto, or system fonts — Syne + DM Sans define the brand.

---

## 4. Logo

### Wordmark
```
moneyCoach
```
- "money" → Syne 800, `--mc-ink` (or white on dark backgrounds)
- "Coach" → Syne 800, `--mc-leaf`
- Always lowercase "money", always Title case "Coach". Never alter this.

### Icon Mark
A circle with a checkmark inside, with a small filled coin (circle in `--mc-sun`) overlapping
the top-right edge. Container: `--mc-leaf` rounded square.
The mark communicates: *goal achieved + reward*.

### Variants

| Variant | When to use |
|---|---|
| Full (mark + wordmark) | Splash screen, onboarding, settings |
| Mark only | App icon, compact placements |
| Reversed (white on dark) | Dark hero cards |

---

## 5. Iconography

Use **emoji** as the primary visual language for expense categories and emotional tone.
This is intentional — it keeps the brand human, accessible, and fun.

For functional UI icons (navigation, actions), use a clean outline icon set (e.g. Lucide)
at 20px, stroke-width 1.5. Default color: muted. Active: `--mc-leaf`.

### Category Emoji Map

| Category | Emoji |
|---|---|
| Spese fisse (generic) | ⚡ |
| Affitto / mutuo | 🏠 |
| Luce | ⚡ |
| Gas | 🔥 |
| Internet / telefono | 📡 |
| Spese variabili (generic) | 🎉 |
| Ristoranti / cene | 🍽️ |
| Concerti / eventi | 🎵 |
| Shopping | 🛍️ |
| Buffer emergenze | 🛡️ |
| Auto / riparazioni | 🚗 |
| Salute / dentista | 🦷 |
| Obiettivi (generic) | 🎯 |
| Viaggi | ✈️ |
| Acquisti speciali | 🎁 |
| Milestone / successo | 🎉 🏆 🚀 🌱 |

---

## 6. App Concept & Key Flows

The app solves one core problem: **"I can't save because I don't know what's left after all my expenses."**

### The four-bucket model
Every euro of salary falls into one of four buckets:

1. **Spese fisse** — predictable monthly costs (rent, utilities). Color: `--mc-fixed`.
2. **Spese variabili** — lifestyle spending with a monthly budget. Color: `--mc-variable`.
3. **Buffer emergenze** — monthly set-aside for irregular/unexpected costs. Color: `--mc-buffer`.
4. **Obiettivi** — what's left, allocated toward saving goals. Color: `--mc-goal`.

The emotional core: **the user sees their "free to dream" number** — what's truly available
for goals — after all other buckets are filled. This number is always displayed prominently
in green, with Syne 800.

### Onboarding (5 steps)
1. Welcome splash — brand intro, single CTA
2. Enter monthly net salary
3. Add fixed expenses (with pre-filled suggestions: affitto, luce, gas, internet...)
4. Lifestyle quiz — eating out frequency, car ownership, health costs, saving personality
5. First saving goal — name, emoji, target amount, monthly contribution %

### Core screens
- **Home** — greeting, "free to dream" hero number, budget summary, goal progress list, upcoming expenses
- **Budget** — full breakdown of the four buckets, editable
- **Goals** — active goals with progress, completed goals, add new
- **Notifiche** — upcoming expense reminders, milestone alerts, weekly digest

### Notification types
- Monthly kickoff (day 1): motivational summary of the month ahead
- Expense reminder (3 days before due): friendly heads-up with amount
- Goal milestone (25 / 50 / 75 / 100%): celebratory, emoji-rich
- Weekly digest (Monday): quick recap of savings progress

### Saving goal mechanics
- Each goal has a target amount, optional deadline, and monthly contribution
- Contribution set as % of available-after-expenses balance
- Multiple goals share the available balance — user sets priority/split
- Completed goals trigger a celebration state (confetti, achievement badge)

---

## 7. Motion Principles

- **Springy** for progress bars and success states — use overshoot easing
- **Short**: 150ms micro-interactions, 300ms standard transitions
- **Celebrate milestones**: confetti or emoji burst at 50% and 100% goal completion
- **Count-up animation** for monetary amounts on screen load
- Reserve motion for meaningful moments — never animate on every render

---

## 8. Tone by Context

| Context | Tone | Example copy |
|---|---|---|
| Onboarding | Warm, curious | "Parliamo un po' di come vivi 👋" |
| Home | Energetic, positive | "Stai andando alla grande 🌱" |
| Budget screen | Clear, calm | No fluff — just clean numbers |
| Goals screen | Aspirational | "Il Giappone si avvicina ✈️" |
| Expense reminder | Friendly nudge | "La bolletta arriva tra 3 giorni — sei pronto?" |
| Milestone reached | Euphoric | "🏆 Ce l'hai fatta! Obiettivo completato!" |
| Empty state | Encouraging | "Nessun obiettivo ancora. Qual è il tuo primo sogno? 🌟" |
| Error state | Calm, no blame | "Qualcosa non ha funzionato. Riprova 😊" |

---

## 9. What makes moneyCoach different

- **It speaks Italian, informally.** It feels like a friend, not a fintech product.
- **Emoji are first-class citizens**, not decoration.
- **The "free to dream" number** is the emotional hero of the home screen — not total balance.
- **Gamification is structural**: progress bars, milestones, and celebrations are built into the model.
- **No guilt.** Variable spending is coral, not red. The tone never blames — it always coaches.

---

*moneyCoach Brand System v1.1 — identity-focused, Lovable-ready*
