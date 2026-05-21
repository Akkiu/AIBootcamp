# DreamJar — Brand System v2
> Single source of truth for identity, tone, colors, and typography.
> Inspired by icon_2.jpeg — the cosmic jar of dreams.

---

## 1. Brand Identity

### Mission
Aiutare le persone a capire quanto possono davvero spendere e risparmiare, trasformando un numero in un sogno concreto e raggiungibile.

### Tagline
**"Il tuo sogno è già lì dentro."**

### Concept visivo
Un barattolo di vetro che contiene una galassia. Il sogno non è irraggiungibile — è già intrappolato, in attesa di essere liberato. Il tappo di sughero lo protegge; il cartellino "SOGNO" lo nomina. Ogni euro risparmiato è una stella che si aggiunge alla galassia interiore.

### Personality

| Tratto | In pratica |
|--------|------------|
| Sognatore | Il risparmio non è sacrificio — è costruire qualcosa di magico |
| Caldo | Come un amico di fiducia, non una banca |
| Rassicurante | I numeri sono chiari, mai opprimenti |
| Celebrativo | Ogni progresso vale un momento di gioia |
| Italiano | Informale, diretto, mai formale o freddo |

### Voice — DO / DON'T

| ✅ DO | ❌ DON'T |
|-------|----------|
| "Il tuo sogno si avvicina ✨" | "Obiettivo: 34% completato." |
| "Hai margine questa settimana — goditi una cena 🍽️" | "Budget surplus rilevato." |
| "La bolletta arriva fra 3 giorni — sei pronto?" | "Avviso: spesa imminente." |
| "Stai costruendo qualcosa di bello 🌌" | "Tasso di risparmio: 12%." |
| Usa sempre "tu" informale | Mai "Lei" formale |
| Usa emoji come punteggiatura emotiva | Mai emoji in stati di errore |

---

## 2. Color System

Palette estratta direttamente dall'icona: navy della galassia, lavanda nebulosa, ghiaccio dello sfondo, oro caldo del nucleo.

```css
:root {
  /* ── Brand primario ─────────────────────────────────── */
  --dj-navy:           #2B3B82;   /* Galaxy blue — colore identitario principale */
  --dj-navy-dark:      #1A2660;   /* Hover / pressed / dark hero */
  --dj-navy-light:     #E8EDFC;   /* Tint per sfondi e superfici leggere */

  /* ── Accent ─────────────────────────────────────────── */
  --dj-lavender:       #9B7AE0;   /* Nebula purple — goals, aspirational */
  --dj-lavender-light: #F0EAFC;   /* Tint lavanda */
  --dj-gold:           #FFB830;   /* Galaxy core — milestone, celebrazioni */
  --dj-gold-light:     #FFF5DF;   /* Tint oro */

  /* ── Sfondi ─────────────────────────────────────────── */
  --dj-bg:             #EEF2FB;   /* App background — azzurro ghiaccio, dall'icona */
  --dj-surface:        #FFFFFF;   /* Card e sheet */
  --dj-surface-2:      #F4F7FD;   /* Superfici secondarie */
  --dj-dark-bg:        #1A2660;   /* Hero card, splash, elementi scuri */
  --dj-dark-surface:   #243080;   /* Superfici su sfondo scuro */

  /* ── Bucket — ogni categoria ha la sua identità ────── */
  --dj-fixed:          #5B9AE8;   /* Spese fisse — blu calmo, stabile, prevedibile */
  --dj-variable:       #9B7AE0;   /* Spese variabili — lavanda, lifestyle */
  --dj-buffer:         #52C4B4;   /* Buffer emergenze — teal, protezione */
  --dj-goal:           #FFB830;   /* Obiettivi — oro, sogni e aspirazioni */

  /* Tint dei bucket (per sfondi card) */
  --dj-fixed-light:    #E8F1FC;
  --dj-variable-light: #F0EAFC;
  --dj-buffer-light:   #E4F8F5;
  --dj-goal-light:     #FFF5DF;

  /* ── Testo ──────────────────────────────────────────── */
  --dj-ink:            #1A2660;   /* Primario — navy profondo */
  --dj-ink-2:          #4A5480;   /* Secondario */
  --dj-muted:          #8890B4;   /* Hint, placeholder */
  --dj-on-dark:        #FFFFFF;   /* Testo su sfondi scuri */

  /* ── Stato ──────────────────────────────────────────── */
  --dj-error:          #E84C6A;   /* Errore, sforamento budget */
  --dj-success:        #3DBF8A;   /* Conferma, salvataggio */
  --dj-warning:        #FFB830;   /* Avviso (usa --dj-gold) */
}
```

### Significato dei colori

| Colore | Ruolo semantico |
|--------|----------------|
| **Navy** `#2B3B82` | Identità principale. Colore della galassia, profondità, focus. Usato per hero elements, titoli, icone attive. |
| **Lavanda** `#9B7AE0` | Lifestyle, sogni, aspirazioni. Colore per le spese variabili e gli obiettivi. |
| **Azzurro ghiaccio** `#EEF2FB` | Sfondo dell'app. Estratto dal fondo dell'icona — leggero, arioso, mai piatto. |
| **Oro** `#FFB830` | Celebrazione, milestone, obiettivi raggiunti. Il nucleo caldo della galassia. |
| **Teal** `#52C4B4` | Buffer, protezione, sicurezza. Calmo e rassicurante. |
| **Blu stabile** `#5B9AE8` | Spese fisse. Prevedibile, affidabile come il cielo. |
| **Corallo** `#E84C6A` | Solo per errori e sforamenti. Non è un colore di categoria — è un segnale. |

---

## 3. Typography

### Font

```
Display / Numeri / Logo  →  Syne 800
Body / UI / Label        →  DM Sans 400, 500
```

Import: `https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap`

### Gerarchia

| Ruolo | Font | Weight | Note |
|-------|------|--------|------|
| Hero numbers (€ importi) | Syne | 800 | Grande, letter-spacing stretto. Il numero è il protagonista. |
| Titoli schermata | Syne | 800 | Carattere forte e riconoscibile |
| Intestazioni sezione | Syne | 700 | |
| Body text | DM Sans | 400 | Leggibile, caldo |
| Label / caption | DM Sans | 500 | Leggermente più pesante per leggibilità |
| Hint / testo di supporto | DM Sans | 300 | Contrasto con i numeri in grassetto |

### Regole

- I numeri finanziari usano sempre **Syne 800**. Un numero grande in `--dj-navy` (o bianco su scuro) è l'hero di ogni schermata.
- **Sentence case** ovunque. Niente ALL CAPS eccetto label cortissime.
- **Le emoji sono benvenute** in titoli, nomi degli obiettivi, notifiche, stati di successo.
- Mai usare Arial, Inter, Roboto o font di sistema.

---

## 4. Logo & Icona

### Wordmark

```
DreamJar
```

- "Dream" → Syne 800, `--dj-navy`
- "Jar" → Syne 800, `--dj-lavender`
- Su sfondo scuro: entrambi in `--dj-on-dark`
- Mai alterare la capitalizzazione o il colore split.

### Icon Mark

Il barattolo di vetro con la galassia interna (icon_2.jpeg). Elementi chiave:
- **Barattolo**: vetro trasparente con bordi `--dj-navy-light`, sfondo `--dj-bg`
- **Galassia**: swirl bicolore `--dj-navy` + `--dj-lavender`
- **Nucleo**: punto luminoso `--dj-gold`
- **Decorazioni**: stelle e luna in `--dj-on-dark` (bianco puro)
- **Tappo sughero**: caldo naturale `#C4834A`
- **Cartellino "SOGNO"**: font Syne, kraft beige `#D4AA7D`

### Varianti

| Variante | Quando usarla |
|----------|---------------|
| Completa (mark + wordmark) | Splash, onboarding, settings |
| Solo mark | App icon, posizionamenti compatti |
| Reversed (bianco su navy) | Hero card scure |

---

## 5. Iconografia

Le **emoji** sono il linguaggio visivo primario per categorie ed emozioni. È una scelta deliberata: mantiene il brand umano, accessibile e giocoso.

Per icone UI funzionali (navigazione, azioni): set outline pulito (es. Lucide) a 20px, stroke-width 1.5. Colore default: `--dj-muted`. Attivo: `--dj-navy` o colore del bucket.

### Mappa emoji categorie

| Categoria | Emoji |
|-----------|-------|
| Spese fisse (generico) | 💸 |
| Affitto / mutuo | 🏠 |
| Bollette | ⚡ |
| Abbonamenti | 📱 |
| Spese variabili (generico) | 🎨 |
| Ristoranti / cene | 🍽️ |
| Concerti / eventi | 🎵 |
| Shopping | 🛍️ |
| Buffer emergenze | 🛡️ |
| Auto / riparazioni | 🚗 |
| Salute / dentista | 🦷 |
| Obiettivi (generico) | 🌌 |
| Viaggi | ✈️ |
| Acquisti speciali | 🎁 |
| Milestone / successo | ✨ 🏆 🚀 🌠 |

---

## 6. Superfici & Elevazione

L'app ha due "mondi": il **mondo chiaro** (sfondo ghiaccio, card bianche) per la navigazione quotidiana, e il **mondo scuro** (navy profondo) per gli elementi hero che devono colpire.

| Livello | Background | Uso |
|---------|------------|-----|
| App background | `--dj-bg` `#EEF2FB` | Base di tutte le schermate |
| Surface (card, sheet) | `--dj-surface` `#FFFFFF` | Card, bottom sheet, modal |
| Surface secondaria | `--dj-surface-2` `#F4F7FD` | Input, sezioni nidificate |
| Hero scuro | `--dj-dark-bg` `#1A2660` | Hero "Free to Dream", splash |
| Hero surface | `--dj-dark-surface` `#243080` | Elementi su hero scuro |

**Ombra card**: `box-shadow: 0 2px 12px rgba(27, 38, 96, 0.08)` — leggera, blu-tinted, coerente con la palette.

---

## 7. Motion Principles

- **Springy** per barre di progresso e stati di successo — usa easing con overshoot
- **Short**: 150ms micro-interazioni, 300ms transizioni standard
- **Celebra i milestone**: burst di stelle/sparkle a 50% e 100% del completamento obiettivo
- **Count-up animation** per gli importi monetari al caricamento schermata
- **Riserva il movimento** ai momenti significativi — non animare ogni render
- **Parallax leggero** sull'hero card (la galassia si muove leggermente allo scroll)

---

## 8. Tone by Context

| Contesto | Tono | Esempio copy |
|----------|------|--------------|
| Onboarding | Caldo, curioso | "Parliamo un po' del tuo stile di vita 👋" |
| Home | Energico, positivo | "La tua galassia di sogni sta crescendo 🌌" |
| Schermata Budget | Chiaro, calmo | Solo numeri puliti — niente fronzoli |
| Schermata Obiettivi | Aspirazionale | "Il Giappone si avvicina ✈️" |
| Reminder spesa | Nudge amichevole | "La bolletta arriva fra 3 giorni — sei pronto?" |
| Milestone raggiunta | Euforico | "✨ Ce l'hai fatta! Il sogno è sempre più reale." |
| Stato vuoto | Incoraggiante | "Nessun sogno ancora? Inizia da qualcosa di piccolo 🌠" |
| Stato di errore | Calmo, senza colpe | "Qualcosa non ha funzionato. Riproviamo 😊" |
| Free to Dream < 0 | Solidale, non colpevolizzante | "Questo mese è stato intenso. Pianifichiamo insieme il prossimo 💙" |

---

## 9. Differenziatori DreamJar

- **L'icona è il manifesto**: una galassia in un barattolo dice tutto — i sogni non sono astratti, sono già lì dentro.
- **Il numero protagonista** non è il saldo totale — è il "Free to Dream", sempre in primo piano in Syne 800.
- **Sfondo azurro ghiaccio** invece del bianco piatto: unico, riconoscibile, coerente con l'atmosfera cosmica.
- **Le emoji sono first-class citizens**, non decorazione.
- **Zero senso di colpa**: il corallo è riservato solo agli errori, mai alle spese variabili. Spendere fa parte della vita.
- **Gamification strutturale**: barre di progresso, milestone, celebrazioni sono nel DNA del prodotto.

---

*DreamJar Brand System v2 — ispirato a icon_2.jpeg · Lovable-ready*
