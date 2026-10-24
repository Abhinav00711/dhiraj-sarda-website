"""Vector assets shared by print, social and website: mark, mandala, icons, Ram-heart emblem, QR."""
import math
from urllib.parse import quote
import segno
from content import PHONE_LINK, WA_TEXT

GOLD = "#C9A24B"


def spiral(cx, cy, turns, rmax, n=90):
    pts = []
    for i in range(n + 1):
        t = i / n
        th = t * turns * 2 * math.pi
        r = rmax * t
        pts.append((cx + r * math.cos(th), cy + r * math.sin(th)))
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)


def mark(color=GOLD, bindu="#E38B3A"):
    """Lotus whose centre turns into a spiral, inside a double ring, with a saffron bindu above."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" fill="none" stroke="{color}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="100" cy="100" r="92" stroke-width="2.4"/>
  <circle cx="100" cy="100" r="86" stroke-width="0.8" opacity="0.7"/>
  <g transform="translate(0,6)">
    <g transform="rotate(-62 100 148)"><path d="M100 148 C 84 128, 84 98, 100 78 C 116 98, 116 128, 100 148 Z" opacity="0.85"/></g>
    <g transform="rotate(62 100 148)"><path d="M100 148 C 84 128, 84 98, 100 78 C 116 98, 116 128, 100 148 Z" opacity="0.85"/></g>
    <g transform="rotate(-31 100 148)"><path d="M100 148 C 80 124, 80 84, 100 54 C 120 84, 120 124, 100 148 Z"/></g>
    <g transform="rotate(31 100 148)"><path d="M100 148 C 80 124, 80 84, 100 54 C 120 84, 120 124, 100 148 Z"/></g>
    <path d="M100 148 C 78 122, 78 78, 100 40 C 122 78, 122 122, 100 148 Z" stroke-width="2.6"/>
    <path d="{spiral(100, 104, 2.6, 17)}" stroke-width="1.7"/>
    <path d="M70 154 H130" stroke-width="1.6" opacity="0.8"/>
    <path d="M82 160 H118" stroke-width="1.2" opacity="0.5"/>
  </g>
  <circle cx="100" cy="25" r="4.2" fill="{bindu}" stroke="none"/>
</svg>"""


def mandala(color=GOLD, petals=(12, 16, 24, 32), size=1000, sw=1.1):
    """Concentric rings of pointed petals + dotted circles. Returns an inline SVG (viewBox size x size)."""
    c = size / 2
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round">']
    radii = [(0.10, 0.20), (0.18, 0.30), (0.28, 0.40), (0.38, 0.49)]
    for (r0, r1), n in zip(radii, petals):
        r0 *= size; r1 *= size
        w = math.pi * r0 / n * 1.05
        g = []
        for i in range(n):
            a = 360 / n * i
            # petal pointing up from (c, c-r0) to (c, c-r1)
            g.append(f'<path transform="rotate({a:.2f} {c} {c})" d="M{c-w:.1f} {c-r0:.1f} Q {c-w:.1f} {c-(r0+r1)/2:.1f} {c:.1f} {c-r1:.1f} Q {c+w:.1f} {c-(r0+r1)/2:.1f} {c+w:.1f} {c-r0:.1f}"/>')
            g.append(f'<path transform="rotate({a:.2f} {c} {c})" d="M{c:.1f} {c-r0-(r1-r0)*0.15:.1f} L{c:.1f} {c-r1+(r1-r0)*0.35:.1f}" opacity=".55"/>')
        out.append("".join(g))
        out.append(f'<circle cx="{c}" cy="{c}" r="{r0:.1f}" opacity=".8"/>')
    for rr, dash in ((0.06, "2 6"), (0.235, "1 9"), (0.445, "1 12"), (0.495, "")):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        out.append(f'<circle cx="{c}" cy="{c}" r="{rr*size:.1f}"{d}/>')
    out.append(f'<path d="{spiral(c, c, 3, size*0.05)}" stroke-width="{sw*1.3}"/>')
    out.append("</svg>")
    return "".join(out)


def icon(body, color=GOLD, size=46, sw=2):
    return f'<svg viewBox="0 0 48 48" width="{size}" height="{size}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'


HEART = "M24 41 C 9 31, 4 22, 9 14.5 C 13.5 8.5, 21 9.5, 24 15.5 C 27 9.5, 34.5 8.5, 39 14.5 C 44 22, 39 31, 24 41 Z"
ICON_BODIES = {
    "plr": '<path d="M14 6h20M14 42h20M16 6c0 10 16 10 16 18S16 32 16 42M32 6c0 10-16 10-16 18s16 8 16 18"/><path d="M20 38h8" opacity=".6"/>',
    "hypno": f'<path d="{spiral(24, 24, 2.4, 17)}"/>',
    "child": f'<path d="{HEART}"/><circle cx="24" cy="20" r="3"/><path d="M24 23.5v6.5M20 26.5l4-1.5 4 1.5M24 30l-3 4.5M24 30l3 4.5"/>',
    "age": '<path d="M10 24a14 14 0 1 0 4.5-10.3"/><path d="M8 8v8h8"/><path d="M24 15v10l6 4"/>',
    "womb": '<path d="M24 42c-10-4-14-12-12-22 8 0 14 4 12 22z"/><path d="M24 42c10-4 14-12 12-22-8 0-14 4-12 22z"/><circle cx="24" cy="16" r="5"/>',
    "med": '<circle cx="24" cy="10" r="4"/><path d="M17 31c.5-8 3-13 7-13s6.5 5 7 13"/><path d="M18 24c-3 3-5 6-4 9M30 24c3 3 5 6 4 9"/><path d="M7 37c6-5 28-5 34 0-6 4-28 4-34 0z"/>',
    "mind": '<path d="M29 42v-6h5c2 0 3-1 3-3v-5l3.5-1-3.5-6.5C37 11 31 6 23 6 14.5 6 8 12 8 20.5c0 5.5 2.5 9.5 6 12V42"/>' + f'<path d="{spiral(23, 20, 2.2, 7.5)}" stroke-width="1.7"/>',
    "body": '<circle cx="24" cy="10" r="4"/><path d="M24 15v13M15 19l9 3 9-3M24 28l-5 12M24 28l5 12"/><path d="M8 14a20 20 0 0 0 0 20M40 14a20 20 0 0 1 0 20" opacity=".6"/><path d="M4 10a26 26 0 0 0 0 28M44 10a26 26 0 0 1 0 28" opacity=".35"/>',
    "heart": f'<path d="{HEART}"/><path d="M24 33c-5-3.2-7.5-6.5-6-9.5 1.3-2.4 4.4-2.3 6 .3 1.6-2.6 4.7-2.7 6-.3 1.5 3-1 6.3-6 9.5z" opacity=".7"/>',
    "soul": '<path d="M24 6c5 6 7.5 11 5 16-1.2 2.5-3 3.5-5 3.5s-3.8-1-5-3.5c-2.5-5 0-10 5-16z"/><path d="M24 16c1.8 2.3 2.4 4.3 1.5 6"/><path d="M8 30c2 8 8.5 11 16 11s14-3 16-11z"/><path d="M5 30h38"/>',
}
ICONS = {k: icon(v) for k, v in ICON_BODIES.items()}


def icon_c(key, color=GOLD, size=46, sw=2):
    return icon(ICON_BODIES[key], color, size, sw)


def ram_heart(gold=GOLD, saffron="#E38B3A", font="'Tiro Devanagari Hindi','Noto Serif Devanagari',serif", rays=True):
    """'Ram in the heart' emblem - Hanuman ji's devotion, drawn typographically (no figure of the deity)."""
    r = ""
    if rays:
        for i in range(24):
            a = math.radians(i * 15)
            ln = 12 if i % 2 == 0 else 6
            x1, y1 = 100 + 86 * math.cos(a), 104 + 86 * math.sin(a)
            x2, y2 = 100 + (86 + ln) * math.cos(a), 104 + (86 + ln) * math.sin(a)
            r += f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" opacity="{.75 if ln == 12 else .45}"/>'
    heart = "M100 168 C 46 132, 24 98, 40 70 C 54 46, 86 48, 100 74 C 114 48, 146 46, 160 70 C 176 98, 154 132, 100 168 Z"
    heart2 = "M100 158 C 54 127, 35 98, 48 74 C 60 54, 87 56, 100 80 C 113 56, 140 54, 152 74 C 165 98, 146 127, 100 158 Z"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" fill="none" stroke="{gold}" stroke-width="1.6" stroke-linecap="round">
  <defs><radialGradient id="rhg" cx="50%" cy="55%" r="50%"><stop offset="0" stop-color="{saffron}" stop-opacity=".45"/><stop offset="1" stop-color="{saffron}" stop-opacity="0"/></radialGradient></defs>
  <circle cx="100" cy="104" r="80" fill="url(#rhg)" stroke="none"/>
  {r}
  <path d="{heart}" stroke-width="2.4"/>
  <path d="{heart2}" stroke-width="1" opacity=".6"/>
  <text x="100" y="124" text-anchor="middle" font-family="{font}" font-size="46" font-weight="700" fill="{saffron}" stroke="none">राम</text>
</svg>"""


WA = '<svg viewBox="0 0 24 24" width="30" height="30"><path fill="#25D366" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'


def wa_url(lang="en"):
    return f"https://wa.me/{PHONE_LINK}?text={quote(WA_TEXT[lang])}"


def qr_svg(lang="en", dark="#0E1233"):
    # always the short English message: Devanagari URL-encoding makes the code far denser and harder to scan
    q = segno.make(wa_url("en"), error="m")
    return q.svg_inline(dark=dark, light=None, scale=1, border=0, omitsize=True)
