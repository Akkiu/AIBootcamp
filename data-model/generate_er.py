#!/usr/bin/env python3
"""Generates an SVG ER diagram for DreamJar data model."""

W, H = 1620, 780
COL_HEADER = "#3DBF7F"
COL_HEADER_NEW = "#9B7AE0"   # lavanda — tabelle expense tracking
COL_HEADER_TEXT = "#FFFFFF"
COL_PK = "#E8FAF2"
COL_FK = "#FFF5E0"
COL_ROW = "#FFFFFF"
COL_ALT = "#FAFAF8"
COL_BORDER = "#C8D0D8"
COL_REL = "#4A4F66"
FONT = "DM Sans, Helvetica, Arial, sans-serif"

tables = {
    "users": {
        "x": 60, "y": 120, "color": COL_HEADER,
        "fields": [
            ("id",         "uuid",        "PK"),
            ("email",      "text",        ""),
            ("full_name",  "text",        ""),
            ("created_at", "timestamptz", ""),
        ],
    },
    "profiles": {
        "x": 60, "y": 400, "color": COL_HEADER,
        "fields": [
            ("id",                   "uuid",        "PK · FK → users.id"),
            ("monthly_income",       "numeric",     ""),
            ("fixed_expenses",       "numeric",     ""),
            ("variable_expenses",    "numeric",     ""),
            ("buffer",               "numeric",     ""),
            ("onboarding_completed", "boolean",     "default false"),
            ("updated_at",           "timestamptz", ""),
        ],
    },
    "goals": {
        "x": 560, "y": 60, "color": COL_HEADER,
        "fields": [
            ("id",            "uuid",        "PK"),
            ("user_id",       "uuid",        "FK → users.id"),
            ("name",          "text",        ""),
            ("emoji",         "text",        ""),
            ("target_amount", "numeric",     ""),
            ("saved_amount",  "numeric",     "default 0"),
            ("target_date",   "date",        "opzionale"),
            ("status",        "enum",        "active · completed"),
            ("created_at",    "timestamptz", ""),
            ("updated_at",    "timestamptz", ""),
        ],
    },
    "recurring_expenses": {
        "x": 560, "y": 450, "color": COL_HEADER,
        "fields": [
            ("id",           "uuid",        "PK"),
            ("user_id",      "uuid",        "FK → users.id"),
            ("name",         "text",        ""),
            ("amount",       "numeric",     ""),
            ("day_of_month", "int",         "1–31"),
            ("bucket",       "enum",        "fixed · variable · buffer"),
            ("active",       "boolean",     "default true"),
            ("created_at",   "timestamptz", ""),
        ],
    },
    "expense_typologies": {
        "x": 1100, "y": 60, "color": COL_HEADER_NEW,
        "fields": [
            ("id",         "uuid",        "PK"),
            ("user_id",    "uuid",        "FK → users.id"),
            ("name",       "text",        ""),
            ("bucket",     "enum",        "fixed · variable · buffer · goal"),
            ("emoji",      "text",        "opzionale"),
            ("is_preset",  "boolean",     "non eliminabile se true"),
            ("created_at", "timestamptz", ""),
        ],
    },
    "expenses": {
        "x": 1100, "y": 370, "color": COL_HEADER_NEW,
        "fields": [
            ("id",           "uuid",        "PK"),
            ("user_id",      "uuid",        "FK → users.id"),
            ("amount",       "numeric",     "> 0"),
            ("bucket",       "enum",        "fixed · variable · buffer · goal"),
            ("typology_id",  "uuid",        "FK → expense_typologies.id"),
            ("note",         "text",        "opzionale"),
            ("expense_date", "date",        "default oggi"),
            ("created_at",   "timestamptz", ""),
        ],
    },
}

TW = 460
ROW_H = 26
HEADER_H = 36

def table_height(name):
    return HEADER_H + len(tables[name]["fields"]) * ROW_H + 4

def mid_right(name):
    t = tables[name]
    return t["x"] + TW, t["y"] + table_height(name) / 2

def mid_left(name):
    t = tables[name]
    return t["x"], t["y"] + table_height(name) / 2

def mid_bottom(name):
    t = tables[name]
    return t["x"] + TW / 2, t["y"] + table_height(name)

def mid_top(name):
    t = tables[name]
    return t["x"] + TW / 2, t["y"]

def draw_table(name):
    t = tables[name]
    x, y = t["x"], t["y"]
    color = t.get("color", COL_HEADER)
    fields = t["fields"]
    th = table_height(name)
    lines = []

    # shadow
    lines.append(f'<rect x="{x+4}" y="{y+4}" width="{TW}" height="{th}" rx="8" fill="#00000018"/>')
    # border
    lines.append(f'<rect x="{x}" y="{y}" width="{TW}" height="{th}" rx="8" fill="white" stroke="{COL_BORDER}" stroke-width="1.5"/>')
    # header
    lines.append(f'<rect x="{x}" y="{y}" width="{TW}" height="{HEADER_H}" rx="8" fill="{color}"/>')
    lines.append(f'<rect x="{x}" y="{y + HEADER_H - 8}" width="{TW}" height="8" fill="{color}"/>')
    lines.append(f'<text x="{x + TW/2}" y="{y + HEADER_H/2 + 6}" text-anchor="middle" font-family="{FONT}" font-size="15" font-weight="700" fill="{COL_HEADER_TEXT}">{name}</text>')

    for i, (fname, ftype, note) in enumerate(fields):
        ry = y + HEADER_H + i * ROW_H + 2
        bg = COL_PK if "PK" in note else (COL_FK if "FK" in note else (COL_ALT if i % 2 == 0 else COL_ROW))
        lines.append(f'<rect x="{x+1}" y="{ry}" width="{TW-2}" height="{ROW_H}" fill="{bg}"/>')
        lines.append(f'<text x="{x+14}" y="{ry+17}" font-family="{FONT}" font-size="12" font-weight="500" fill="#1A1E2E">{fname}</text>')
        lines.append(f'<text x="{x+180}" y="{ry+17}" font-family="{FONT}" font-size="11" fill="#4A4F66">{ftype}</text>')
        if note:
            lines.append(f'<text x="{x+280}" y="{ry+17}" font-family="{FONT}" font-size="10" fill="#7A8099" font-style="italic">{note}</text>')

    # bottom radius fix
    lines.append(f'<rect x="{x}" y="{y + th - 8}" width="{TW}" height="8" rx="0" fill="white" stroke="{COL_BORDER}" stroke-width="0"/>')
    return "\n".join(lines)


svg_parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <style>text {{ font-family: {FONT}; }}</style>
  </defs>
  <rect width="{W}" height="{H}" fill="#FAFAF8" rx="12"/>

  <!-- title -->
  <text x="50" y="56" font-family="{FONT}" font-size="22" font-weight="800" fill="#1A1E2E">DreamJar — Entity Relationship Diagram</text>
  <text x="50" y="78" font-family="{FONT}" font-size="13" fill="#7A8099">MVP v1.1 · Data Model</text>

  <!-- legend -->
  <rect x="1380" y="30" width="14" height="14" rx="3" fill="{COL_PK}"/>
  <text x="1400" y="43" font-family="{FONT}" font-size="11" fill="#4A4F66">PK</text>
  <rect x="1430" y="30" width="14" height="14" rx="3" fill="{COL_FK}"/>
  <text x="1450" y="43" font-family="{FONT}" font-size="11" fill="#4A4F66">FK</text>
  <rect x="1480" y="30" width="14" height="14" rx="3" fill="{COL_HEADER_NEW}"/>
  <text x="1500" y="43" font-family="{FONT}" font-size="11" fill="#4A4F66">v1.1</text>
''']

# Draw tables
for name in tables:
    svg_parts.append(draw_table(name))

# ── Relationships ──────────────────────────────────────────────────────────────

# users ||--|| profiles  (vertical, same column)
ux, uy = mid_bottom("users")
px, py = mid_top("profiles")
svg_parts.append(f'''
  <line x1="{ux}" y1="{uy}" x2="{px}" y2="{py}" stroke="{COL_REL}" stroke-width="1.8"/>
  <text x="{ux + 12}" y="{(uy+py)/2}" font-family="{FONT}" font-size="11" fill="{COL_REL}" font-weight="600">1 : 1</text>
  <text x="{ux + 12}" y="{(uy+py)/2 + 14}" font-family="{FONT}" font-size="10" fill="#7A8099" font-style="italic">ha</text>
''')

# users ||--o{{ goals  (horizontal, same row)
rx1, ry1 = mid_right("users")
gx, gy = mid_left("goals")
cx = (rx1 + gx) / 2
svg_parts.append(f'''
  <path d="M {rx1} {ry1} C {cx} {ry1}, {cx} {gy}, {gx} {gy}" fill="none" stroke="{COL_REL}" stroke-width="1.8"/>
  <text x="{cx}" y="{(ry1+gy)/2 - 10}" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{COL_REL}" font-weight="600">1 : N</text>
  <text x="{cx}" y="{(ry1+gy)/2 + 4}" text-anchor="middle" font-family="{FONT}" font-size="10" fill="#7A8099" font-style="italic">ha</text>
''')

# users ||--o{{ recurring_expenses  (curved, dashed)
rx2, ry2 = mid_right("users")
ex, ey = mid_left("recurring_expenses")
cx2 = (rx2 + ex) / 2
svg_parts.append(f'''
  <path d="M {rx2} {ry2} C {cx2} {ry2}, {cx2} {ey}, {ex} {ey}" fill="none" stroke="{COL_REL}" stroke-width="1.8" stroke-dasharray="6,3"/>
  <text x="{cx2}" y="{(ry2+ey)/2 - 10}" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{COL_REL}" font-weight="600">1 : N</text>
  <text x="{cx2}" y="{(ry2+ey)/2 + 4}" text-anchor="middle" font-family="{FONT}" font-size="10" fill="#7A8099" font-style="italic">ha</text>
''')

# users ||--o{{ expense_typologies  (route through top: up → across → down)
utx, uty = mid_top("users")
ttx, tty = mid_top("expense_typologies")
ROUTE_Y = 25
svg_parts.append(f'''
  <path d="M {utx} {uty} L {utx} {ROUTE_Y} L {ttx} {ROUTE_Y} L {ttx} {tty}"
        fill="none" stroke="{COL_HEADER_NEW}" stroke-width="1.8" stroke-dasharray="6,3"/>
  <text x="{(utx+ttx)/2}" y="{ROUTE_Y - 6}" text-anchor="middle" font-family="{FONT}" font-size="11" fill="{COL_HEADER_NEW}" font-weight="600">1 : N</text>
  <text x="{(utx+ttx)/2 + 32}" y="{ROUTE_Y - 6}" text-anchor="middle" font-family="{FONT}" font-size="10" fill="{COL_HEADER_NEW}" font-style="italic">ha</text>
''')

# expense_typologies ||--o{{ expenses  (vertical, same column)
etbx, etby = mid_bottom("expense_typologies")
expx, expy = mid_top("expenses")
svg_parts.append(f'''
  <line x1="{etbx}" y1="{etby}" x2="{expx}" y2="{expy}" stroke="{COL_HEADER_NEW}" stroke-width="1.8"/>
  <text x="{etbx + 12}" y="{(etby+expy)/2}" font-family="{FONT}" font-size="11" fill="{COL_HEADER_NEW}" font-weight="600">1 : N</text>
  <text x="{etbx + 12}" y="{(etby+expy)/2 + 14}" font-family="{FONT}" font-size="10" fill="{COL_HEADER_NEW}" font-style="italic">classifica</text>
''')

svg_parts.append("</svg>")

output = "\n".join(svg_parts)
out_path = "/Users/cristiano.giardi/DreamJar/data-model/er-diagram.svg"
with open(out_path, "w") as f:
    f.write(output)

print(f"SVG generated: {out_path}")
