#!/usr/bin/env python3
"""Generate branded graphic mockup PNGs (navy+gold LLA) for the Courtney deck.
Renders crisp SVG to PNG via cairosvg. 9:16 portrait to match vertical ad frames."""
import cairosvg, os

OUT = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1920  # 9:16

NAVY = "#02091C"
CARD = "#0A1633"
BLUE = "#1A7FFF"
SKY  = "#7EC8FF"
GOLD = "#C9A24B"
GOLD2= "#E3C579"
PAPER= "#F4EEE2"
MUTED= "#8AA0C6"

FONT = "Georgia, 'Times New Roman', serif"
SANS = "Arial, Helvetica, sans-serif"

def base(inner, bg=NAVY):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
<radialGradient id="glow" cx="50%" cy="38%" r="75%">
  <stop offset="0%" stop-color="#0C1A3A"/>
  <stop offset="100%" stop-color="{NAVY}"/>
</radialGradient>
<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="{GOLD2}"/>
  <stop offset="100%" stop-color="{GOLD}"/>
</linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#glow)"/>
{inner}
</svg>'''

def render(name, inner, bg=NAVY):
    svg = base(inner, bg)
    p = os.path.join(OUT, name)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=p, output_width=W, output_height=H)
    print("wrote", p)

# ---------- 1. Trajectory line graph (Film 1 Act II) ----------
graph = f'''
<text x="{W/2}" y="300" text-anchor="middle" font-family="{SANS}" font-size="34" letter-spacing="6" fill="{GOLD2}">AGING IS A TRAJECTORY</text>
<!-- axes -->
<line x1="180" y1="1400" x2="900" y2="1400" stroke="{MUTED}" stroke-width="3" opacity="0.5"/>
<line x1="180" y1="1400" x2="180" y2="560" stroke="{MUTED}" stroke-width="3" opacity="0.5"/>
<text x="90" y="980" font-family="{SANS}" font-size="26" fill="{MUTED}" transform="rotate(-90 90 980)" text-anchor="middle">VITALITY</text>
<text x="{W/2}" y="1470" text-anchor="middle" font-family="{SANS}" font-size="26" fill="{MUTED}">AGE  &#8594;</text>
<!-- steep declining line (default) -->
<path d="M 200 620 C 400 720, 560 980, 880 1360" fill="none" stroke="{MUTED}" stroke-width="10" opacity="0.65"/>
<text x="905" y="1360" font-family="{SANS}" font-size="26" fill="{MUTED}">decline</text>
<!-- bent, flatter line (gold) -->
<path d="M 200 620 C 420 660, 640 720, 900 820" fill="none" stroke="url(#gold)" stroke-width="14"/>
<circle cx="640" cy="720" r="16" fill="{GOLD2}"/>
<text x="905" y="820" font-family="{SANS}" font-size="30" fill="{GOLD2}" font-weight="bold">bend it</text>
<text x="{W/2}" y="1650" text-anchor="middle" font-family="{FONT}" font-style="italic" font-size="52" fill="{PAPER}">Two people. Same birthday.</text>
<text x="{W/2}" y="1720" text-anchor="middle" font-family="{FONT}" font-style="italic" font-size="52" fill="{GOLD2}">One bends the curve.</text>
'''
render("g_trajectory.png", graph)

# --- simple gold vector icons (no emoji fonts in sandbox) ---
def ic_move(cx, cy, s=1.0):  # running figure
    return f'<g transform="translate({cx},{cy}) scale({s})" stroke="{GOLD2}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="0" cy="-58" r="18" fill="{GOLD2}" stroke="none"/><path d="M -6 -36 L 8 -8 L 34 2"/><path d="M 8 -8 L 2 30 L -24 52"/><path d="M 2 30 L 26 46"/><path d="M -6 -30 L -34 -18"/></g>'
def ic_eat(cx, cy, s=1.0):  # apple
    return f'<g transform="translate({cx},{cy}) scale({s})"><path d="M 0 -30 C 26 -52, 60 -30, 46 12 C 40 40, 20 58, 0 46 C -20 58, -40 40, -46 12 C -60 -30, -26 -52, 0 -30 Z" fill="none" stroke="{GOLD2}" stroke-width="9"/><path d="M 0 -34 C 4 -54, 16 -62, 28 -62" fill="none" stroke="{GOLD2}" stroke-width="9" stroke-linecap="round"/></g>'
def ic_recover(cx, cy, s=1.0):  # moon
    return f'<g transform="translate({cx},{cy}) scale({s})"><path d="M 34 -44 A 56 56 0 1 0 44 46 A 44 44 0 1 1 34 -44 Z" fill="none" stroke="{GOLD2}" stroke-width="9" stroke-linejoin="round"/></g>'
def ic_sleep(cx, cy, s=1.0):
    return ic_recover(cx, cy, s)
def ic_connect(cx, cy, s=1.0):  # two people
    return f'<g transform="translate({cx},{cy}) scale({s})" fill="none" stroke="{GOLD2}" stroke-width="9" stroke-linecap="round"><circle cx="-22" cy="-30" r="16"/><circle cx="22" cy="-30" r="16"/><path d="M -48 40 C -48 4, -4 4, -4 40"/><path d="M 4 40 C 4 4, 48 4, 48 40"/></g>'

ICON = {"MOVE": ic_move, "EAT": ic_eat, "RECOVER": ic_recover, "SLEEP": ic_sleep, "CONNECT": ic_connect}

# ---------- 2. Move / Eat / Recover icon row (Film 1 Act IV) ----------
def lever(cx, label):
    return f'''
<circle cx="{cx}" cy="820" r="150" fill="{CARD}" stroke="{GOLD}" stroke-width="3"/>
{ICON[label](cx,820,1.15)}
<text x="{cx}" y="1060" text-anchor="middle" font-family="{SANS}" font-size="42" letter-spacing="4" fill="{PAPER}" font-weight="bold">{label}</text>
'''
levers = f'''
<text x="{W/2}" y="330" text-anchor="middle" font-family="{SANS}" font-size="34" letter-spacing="6" fill="{GOLD2}">THE 3 LEVERS</text>
<text x="{W/2}" y="520" text-anchor="middle" font-family="{FONT}" font-size="90" fill="{PAPER}">Move &#183; Eat &#183; Recover</text>
{lever(300,"MOVE")}
{lever(540,"EAT")}
{lever(780,"RECOVER")}
<text x="{W/2}" y="1400" text-anchor="middle" font-family="{FONT}" font-style="italic" font-size="52" fill="{SKY}">Not a hundred rules.</text>
<text x="{W/2}" y="1470" text-anchor="middle" font-family="{FONT}" font-style="italic" font-size="52" fill="{GOLD2}">The handful that move the needle.</text>
'''
render("g_levers.png", levers)

# ---------- 3. Four Pillars row (Film 3 Act V) ----------
def pillar(cx, label):
    return f'''
<rect x="{cx-105}" y="700" width="210" height="300" rx="24" fill="{CARD}" stroke="{GOLD}" stroke-width="3"/>
{ICON[label](cx,840,0.9)}
<text x="{cx}" y="960" text-anchor="middle" font-family="{SANS}" font-size="30" letter-spacing="2" fill="{PAPER}" font-weight="bold">{label}</text>
'''
pillars = f'''
<text x="{W/2}" y="330" text-anchor="middle" font-family="{SANS}" font-size="34" letter-spacing="6" fill="{GOLD2}">THE 4 PILLARS</text>
<text x="{W/2}" y="520" text-anchor="middle" font-family="{FONT}" font-size="82" fill="{PAPER}">The 4 things that matter</text>
{pillar(180,"MOVE")}
{pillar(420,"EAT")}
{pillar(660,"SLEEP")}
{pillar(900,"CONNECT")}
<text x="{W/2}" y="1380" text-anchor="middle" font-family="{FONT}" font-style="italic" font-size="52" fill="{SKY}">Boring. Repeatable. Affordable.</text>
<text x="{W/2}" y="1450" text-anchor="middle" font-family="{FONT}" font-style="italic" font-size="52" fill="{GOLD2}">That&#8217;s what actually works.</text>
'''
render("g_pillars.png", pillars)

# ---------- 4. Result card (all films [RESULT]) ----------
result = f'''
<rect x="130" y="640" width="820" height="640" rx="40" fill="{CARD}" stroke="url(#gold)" stroke-width="4"/>
<text x="{W/2}" y="770" text-anchor="middle" font-family="{SANS}" font-size="32" letter-spacing="8" fill="{GOLD2}">MY RESULT</text>
<text x="{W/2}" y="970" text-anchor="middle" font-family="{FONT}" font-size="150" fill="{PAPER}" font-weight="bold">[ RESULT ]</text>
<text x="{W/2}" y="1080" text-anchor="middle" font-family="{SANS}" font-size="34" fill="{MUTED}">Courtney&#8217;s real, verifiable number</text>
<line x1="330" y1="1150" x2="750" y2="1150" stroke="{GOLD}" stroke-width="2" opacity="0.5"/>
<text x="{W/2}" y="1230" text-anchor="middle" font-family="{SANS}" font-size="30" fill="{SKY}">No extreme diet. No fortune.</text>
<text x="{W/2}" y="1470" text-anchor="middle" font-family="{FONT}" font-style="italic" font-size="46" fill="{GOLD2}">On a normal schedule.</text>
<text x="{W/2}" y="1540" text-anchor="middle" font-family="{FONT}" font-style="italic" font-size="46" fill="{GOLD2}">On a normal budget.</text>
'''
render("g_result.png", result)

# ---------- 5. Course UI mockup (Film 1/2 Act V) ----------
def module(y, name, done):
    check = f'<circle cx="240" cy="{y+38}" r="26" fill="url(#gold)"/><path d="M 228 {y+38} l 8 9 l 16 -18" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>' if done else f'<circle cx="240" cy="{y+38}" r="26" fill="none" stroke="{MUTED}" stroke-width="3"/>'
    return f'''
<rect x="180" y="{y}" width="720" height="76" rx="18" fill="{CARD}" stroke="{'#1c2c52' if not done else GOLD}" stroke-width="2" opacity="{'1' if done else '0.75'}"/>
{check}
<text x="300" y="{y+50}" font-family="{SANS}" font-size="34" fill="{PAPER if done else MUTED}">{name}</text>
'''
ui = f'''
<text x="{W/2}" y="300" text-anchor="middle" font-family="{SANS}" font-size="34" letter-spacing="6" fill="{GOLD2}">LONGEVITY LIFE ACADEMY</text>
<text x="{W/2}" y="420" text-anchor="middle" font-family="{FONT}" font-size="76" fill="{PAPER}">A guided path</text>
<!-- progress bar -->
<rect x="180" y="500" width="720" height="26" rx="13" fill="{CARD}"/>
<rect x="180" y="500" width="430" height="26" rx="13" fill="url(#gold)"/>
<text x="900" y="560" text-anchor="end" font-family="{SANS}" font-size="28" fill="{MUTED}">60% complete</text>
{module(640,"Energy &#183; your daily baseline", True)}
{module(736,"Strength &#183; move for life", True)}
{module(832,"Sleep &#183; deep recovery", True)}
{module(928,"Mind &#183; a clear head", False)}
{module(1024,"Connect &#183; people &amp; purpose", False)}
<text x="{W/2}" y="1300" text-anchor="middle" font-family="{FONT}" font-style="italic" font-size="52" fill="{SKY}">Lesson by lesson.</text>
<text x="{W/2}" y="1370" text-anchor="middle" font-family="{FONT}" font-style="italic" font-size="52" fill="{GOLD2}">You always know your next step.</text>
'''
render("g_courseui.png", ui)

print("ALL GRAPHICS DONE")
