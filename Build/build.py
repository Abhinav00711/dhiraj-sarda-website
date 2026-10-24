"""Builds every print + social piece for Dhiraj Sarda as HTML in Build/html/ (EN + HI).
Run:  python build.py   then   python render.py   (outputs land in Build/out/)
Copy lives in content.py, vector art in assets.py, photos/backgrounds in art/."""
import pathlib
from content import T, PHONE_DISPLAY, EMAIL, WEBSITE
from assets import mark, mandala, ICONS, icon_c, ram_heart, WA, wa_url, qr_svg

ROOT = pathlib.Path(__file__).parent
HTML = ROOT / "html"
HTML.mkdir(exist_ok=True)
(ROOT / "brand").mkdir(exist_ok=True)

# ---------- shared files ----------
(ROOT / "brand" / "mark.svg").write_text(mark(), encoding="utf-8")
(ROOT / "brand" / "mark-ink.svg").write_text(mark("#0E1233"), encoding="utf-8")
(ROOT / "brand" / "mandala.svg").write_text(mandala(), encoding="utf-8")
(ROOT / "brand" / "mandala-dk.svg").write_text(mandala("#8a6a1f"), encoding="utf-8")
(ROOT / "brand" / "ram-heart.svg").write_text(ram_heart(), encoding="utf-8")

ART = "../art"
P_FORMAL, P_WARM = f"{ART}/portrait-formal.jpg", f"{ART}/portrait-warm.jpg"
BG_PAPER, BG_POSTER = f"{ART}/bg-brochure.jpg", f"{ART}/bg-poster.jpg"
CERT = "../../Certificate.png"  # kept on file only - shows the trainer's name, so not printed
HANUMAN = f"{ART}/hanuman-dhyan.jpg"
MARK, MARK_INK, MANDALA, MANDALA_DK = "../brand/mark.svg", "../brand/mark-ink.svg", "../brand/mandala.svg", "../brand/mandala-dk.svg"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?'
         'family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Jost:wght@300;400;500;600'
         '&family=Noto+Serif+Devanagari:wght@500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600'
         '&family=Tiro+Devanagari+Hindi:ital@0;1&display=swap" rel="stylesheet">')

BASE = """
:root{--ink:#0E1233;--indigo:#1A1F4D;--gold:#C9A24B;--goldlt:#E6CB8A;--ivory:#F6EFDD;--mist:#B9BDDA;--golddk:#8a6a1f;--saffron:#E38B3A;--text:#2a2f55}
*{box-sizing:border-box;margin:0;padding:0}
html,body{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'Jost','Noto Sans Devanagari',sans-serif;color:var(--ivory)}
body.hi{font-family:'Noto Sans Devanagari','Jost',sans-serif}
.serif{font-family:'Cormorant Garamond','Noto Serif Devanagari',serif}
.hi .serif{font-family:'Noto Serif Devanagari','Cormorant Garamond',serif;letter-spacing:0!important}
.tiro{font-family:'Tiro Devanagari Hindi','Noto Serif Devanagari',serif}
.caps{text-transform:uppercase;letter-spacing:.26em}
.hi .caps{letter-spacing:.03em!important;text-transform:none!important}
.it{font-style:italic}.hi .it{font-style:normal}
.rule{height:1px;background:var(--gold);position:relative;margin:0 auto}
.rule:after{content:"";position:absolute;left:50%;top:-3px;width:7px;height:7px;background:var(--gold);transform:translateX(-50%) rotate(45deg)}
.rule.l{margin-left:0}.rule.l:after{left:0;transform:rotate(45deg)}
.dark{background:radial-gradient(ellipse at 50% 14%,#283080 0%,#151b55 36%,var(--ink) 78%);color:var(--ivory)}
.light{background:var(--ivory) url('BG_PAPER') center/cover;color:var(--ink)}
.stars{position:absolute;inset:0;pointer-events:none;opacity:.32;background-image:radial-gradient(rgba(230,203,138,.6) 1px,transparent 1.4px),radial-gradient(rgba(230,203,138,.35) 1px,transparent 1.4px),radial-gradient(rgba(255,255,255,.35) .8px,transparent 1.2px);background-size:90px 90px,53px 53px,137px 137px;background-position:0 0,27px 31px,61px 13px}
.mand{position:absolute;pointer-events:none}
.rel{position:relative}
.kicker{display:flex;align-items:center;gap:10px;font-size:10.5px;color:var(--gold);font-weight:500}
.dark .kicker{color:var(--goldlt)}
.kicker:before,.kicker.c:after{content:"";width:26px;height:1px;background:currentColor;opacity:.7}
.kicker.c{justify-content:center}
.arch{border-radius:999px 999px 0 0;overflow:hidden;border:3px solid var(--gold);box-shadow:0 0 0 7px rgba(14,18,51,.92),0 0 0 8.5px var(--gold),0 22px 60px rgba(0,0,0,.45)}
.arch img{width:100%;height:100%;object-fit:cover;object-position:50% 12%;display:block}
.chk{list-style:none}
.chk li{position:relative;padding-left:18px}
.chk li:before{content:"";position:absolute;left:2px;top:.62em;width:6px;height:6px;background:var(--gold);transform:rotate(45deg)}
.wa-pill{display:inline-flex;align-items:center;gap:12px;background:var(--ivory);color:var(--ink);border-radius:999px;border:2px solid var(--gold);text-decoration:none}
.wa-pill .num{font-family:'Jost',sans-serif;font-weight:600;letter-spacing:.03em}
.qr{background:var(--ivory);border-radius:10px;border:1.5px solid var(--gold)}
.qr svg{display:block;width:100%;height:100%}
""".replace("BG_PAPER", BG_PAPER)


def page(title, lang, css, body, cls=""):
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{title}</title>{FONTS}'
            f'<style>{BASE}{css}</style></head><body class="{lang} {cls}">{body}</body></html>')


def wa_icon(px):
    return WA.replace('width="30" height="30"', f'width="{px}" height="{px}"')


def write(name, html):
    (HTML / name).write_text(html, encoding="utf-8")


# =====================================================================
# BROCHURE  A4 x 6 pages
# =====================================================================
BRO_CSS = """
@page{size:210mm 297mm;margin:0}
.pg{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page}
.pg:last-child{break-after:auto}
/* 1 cover */
.cv{display:flex;flex-direction:column;align-items:center}
.cv .devo{margin-top:10mm;font-size:15px;color:var(--goldlt);opacity:.9;letter-spacing:.06em}
.cv .mk{width:15mm;margin-top:4mm}
.cv .mand{width:205mm;left:2.5mm;top:22mm;opacity:.13}
.cv .arch{width:124mm;height:154mm;margin-top:7mm}
.cv h1{font-size:56px;font-weight:600;letter-spacing:.14em;line-height:1;margin-top:11mm}
.hi .cv h1{font-size:60px;line-height:1.25;margin-top:8mm}
.cv .rule{width:70mm;margin-top:5mm}
.cv .ttl{margin-top:5mm;font-size:11.5px;color:var(--goldlt);text-align:center;line-height:1.9}
.hi .cv .ttl{font-size:15px;line-height:1.6}
.cv .tag{margin-top:6mm;font-size:25px;color:var(--ivory)}
.cv .tag span{color:var(--goldlt)}
.cv .cred{margin-top:6mm;font-size:10.5px;color:var(--mist);display:flex;align-items:center;gap:10px}
.cv .cred:before,.cv .cred:after{content:'';width:18px;height:1px;background:var(--gold);opacity:.7}
.hi .cv .cred{font-size:13px}
.hi .cv .tag{font-size:23px}
.cv .foot{position:absolute;bottom:0;left:0;right:0;height:17mm;background:rgba(14,18,51,.88);border-top:1px solid var(--gold);display:flex;align-items:center;justify-content:center;gap:12mm;font-size:12.5px}
.cv .foot .ph{display:flex;align-items:center;gap:8px;font-weight:500;letter-spacing:.06em}
/* 2 about */
.ab{padding:22mm 20mm 0}
.ab .col{width:112mm}
.ab h2{font-size:34px;line-height:1.12;font-weight:600;margin:4mm 0 0}
.hi .ab h2{font-size:28px;line-height:1.45}
.ab .rule{width:44mm;margin:6mm 0 6mm}
.ab p{font-size:13.6px;line-height:1.75;color:var(--text)}
.hi .ab p{font-size:13px;line-height:1.85}
.ab p+p{margin-top:9px}
.ab p b{color:var(--ink)}
.ab .ph{position:absolute;right:20mm;top:24mm;width:52mm;height:68mm;border-radius:999px 999px 8px 8px;overflow:hidden;border:2px solid var(--gold);box-shadow:0 0 0 6px var(--ivory),0 0 0 7px var(--gold),0 14px 30px rgba(14,18,51,.18)}
.ab .ph img{width:100%;height:100%;object-fit:cover;object-position:50% 20%}
.ab .phc{position:absolute;right:20mm;top:96mm;width:52mm;text-align:center;font-size:19px;font-style:italic;color:var(--golddk)}
.hi .ab .phc{font-style:normal;font-size:17px}
.meet{position:absolute;left:20mm;right:20mm;top:137mm;background:var(--ink);color:var(--ivory);border-radius:14px;border:1px solid var(--gold);padding:8mm 9mm;display:grid;grid-template-columns:1.35fr 1fr;gap:8mm;overflow:hidden}
.meet .mand{width:120mm;right:-40mm;top:-30mm;opacity:.1}
.meet h3{font-size:25px;color:var(--goldlt);font-weight:600;margin-bottom:6px}
.meet p{font-size:12.8px;line-height:1.72;color:#dfe0f0}
.hi .meet p{font-size:11.8px;line-height:1.8}
.meet ul{font-size:12.8px;line-height:1.55;color:var(--ivory);display:grid;gap:7px;align-content:center;border-left:1px solid rgba(201,162,75,.4);padding-left:7mm}
.btm{position:absolute;left:20mm;right:20mm;top:214mm;text-align:center}
.btm .mk{width:11mm;opacity:.9}
.btm .q{font-size:27px;font-style:italic;color:var(--golddk);margin-top:2mm}
.hi .btm .q{font-style:normal;font-size:22px}
.pil{display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;margin-top:8mm}
.pil div{border-top:1px solid var(--gold);padding-top:4mm}
.pil h5{font-size:21px;font-weight:600;color:var(--ink)}
.pil p{font-size:11.5px;color:#4a4f75;margin-top:2px}
/* 3 services */
.sv{padding:17mm 15mm 0}
.sv .mand{width:260mm;left:-25mm;bottom:-150mm;opacity:.08}
.sv h2{font-size:38px;font-weight:600;text-align:center;margin-top:3mm}
.hi .sv h2{font-size:30px}
.sv .rule{width:48mm;margin:5mm auto 8mm}
.grid6{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.sc{display:flex;gap:12px;background:linear-gradient(160deg,rgba(255,255,255,.07),rgba(255,255,255,.02));border:1px solid rgba(201,162,75,.45);border-radius:12px;padding:8mm 7mm 8mm 6mm;position:relative;min-height:53mm}
.sc.new{border-color:var(--gold);box-shadow:0 0 0 1px rgba(201,162,75,.3),0 0 30px rgba(201,162,75,.12) inset}
.sc .ic{flex:none;width:46px;height:46px}
.sc h4{font-size:22px;color:var(--goldlt);font-weight:600;line-height:1.15;margin-bottom:5px}
.hi .sc h4{font-size:17px;line-height:1.4}
.sc p{font-size:13px;line-height:1.62;color:#dfe0f0}
.hi .sc p{font-size:12.4px;line-height:1.75}
.fmts{display:grid;grid-template-columns:repeat(3,1fr);margin-top:11mm;border-top:1px solid rgba(201,162,75,.5);border-bottom:1px solid rgba(201,162,75,.5)}
.fmts div{text-align:center;padding:5mm 3mm}
.fmts div+div{border-left:1px solid rgba(201,162,75,.3)}
.fmts h5{font-size:21px;color:var(--goldlt);font-weight:600}
.hi .fmts h5{font-size:16px}
.fmts p{font-size:12.5px;color:var(--mist);margin-top:2px}
.sv .q{position:absolute;left:15mm;right:15mm;bottom:12mm;text-align:center;font-size:24px;font-style:italic;color:var(--goldlt)}
.hi .sv .q{font-style:normal;font-size:20px}
/* 4 areas */
.ar{padding:20mm 17mm 0}
.ar h2{font-size:33px;font-weight:600;text-align:center;margin-top:3mm}
.hi .ar h2{font-size:27px}
.ar .rule{width:48mm;margin:5mm auto 8mm}
.grid4{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.qd{background:rgba(255,255,255,.55);border:1px solid rgba(201,162,75,.7);border-radius:14px;padding:8mm 8mm 8mm}
.qd .hd{display:flex;align-items:center;gap:12px;margin-bottom:4mm}
.qd .ib{width:15mm;height:15mm;border-radius:50%;background:var(--ink);display:flex;align-items:center;justify-content:center;flex:none;box-shadow:0 0 0 3px var(--ivory),0 0 0 4px var(--gold)}
.qd h4{font-size:28px;font-weight:600;line-height:1}
.hi .qd h4{font-size:22px;line-height:1.3}
.qd .sub{font-size:13.5px;font-style:italic;color:var(--golddk);margin-top:3px;font-family:'Cormorant Garamond','Noto Serif Devanagari',serif;font-weight:600}
.hi .qd .sub{font-style:normal;font-size:12px}
.qd ul{font-size:14px;line-height:2.1;color:var(--text)}
.qd.body{background:rgba(255,255,255,.75);border-color:var(--gold);box-shadow:0 10px 30px rgba(138,106,31,.12)}
.note{margin-top:7mm;display:flex;gap:12px;align-items:center;background:var(--ink);color:#e6e7f3;border-radius:12px;padding:5mm 7mm;font-size:13px;line-height:1.65;border-left:4px solid var(--saffron)}
.note b{color:var(--goldlt);font-weight:500}
.note svg{flex:none}
.ar .cta{position:absolute;left:24mm;right:24mm;bottom:17mm;text-align:center;font-size:19px;font-style:italic;line-height:1.45;color:var(--ink)}
.hi .ar .cta{font-style:normal;font-size:16px}
.ar .cta .mk{width:9mm;display:block;margin:0 auto 3mm}
/* 5 journey + inspiration */
.jr{padding:17mm 15mm 0}
.jr h2{font-size:36px;font-weight:600;text-align:center;margin-top:3mm}
.hi .jr h2{font-size:29px}
.jr .rule{width:48mm;margin:5mm auto 9mm}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:4mm;position:relative}
.steps:before{content:"";position:absolute;top:25px;left:12%;right:12%;height:1px;background:linear-gradient(90deg,transparent,var(--gold) 15%,var(--gold) 85%,transparent)}
.st{text-align:center;position:relative}
.st .n{width:50px;height:50px;border-radius:50%;background:var(--ink);border:1.5px solid var(--gold);color:var(--goldlt);font-family:'Cormorant Garamond',serif;font-size:24px;font-weight:600;display:flex;align-items:center;justify-content:center;margin:0 auto 9px;box-shadow:0 0 18px rgba(201,162,75,.25)}
.st h5{font-size:18px;color:var(--goldlt);margin-bottom:5px;font-weight:600;line-height:1.2}
.hi .st h5{font-size:15.5px;line-height:1.4}
.st p{font-size:12.2px;line-height:1.55;color:#dfe0f0}
.insp{position:absolute;left:15mm;right:15mm;top:104mm;bottom:15mm;display:flex;flex-direction:column;justify-content:space-evenly;border:1px solid rgba(201,162,75,.55);border-radius:18px;background:linear-gradient(180deg,rgba(227,139,58,.07),rgba(255,255,255,.02));padding:8mm 11mm;overflow:hidden}
.insp .mand{width:200mm;left:50%;margin-left:-100mm;top:60mm;opacity:.07}
.insp .top{display:grid;grid-template-columns:64mm 1fr;gap:8mm;align-items:center}
.insp .em{width:64mm;height:64mm}
.insp h3{font-size:36px;font-weight:600;color:var(--ivory);margin:3mm 0 4mm;line-height:1.1}
.hi .insp h3{font-size:27px;line-height:1.4}
.insp p{font-size:13.6px;line-height:1.75;color:#dfe0f0}
.hi .insp p{font-size:12.4px;line-height:1.85}
.verse{text-align:center}
.verse .v{font-size:33px;line-height:1.55;color:var(--goldlt)}
.verse .tr{font-size:19px;font-style:italic;color:var(--ivory);margin-top:4mm;opacity:.92}
.verse .src{font-size:10px;color:var(--gold);margin-top:3mm}
.verse .rule{width:30mm;margin:5mm auto}
.sankat{text-align:center;font-size:13px;color:var(--mist)}
/* 6 credentials + contact */
.cr{padding:16mm 18mm 0}
.cr h2{font-size:31px;font-weight:600;margin-top:3mm}
.hi .cr h2{font-size:26px}
.cr .rule{width:40mm;margin:4mm 0 6mm}
.crow{display:grid;grid-template-columns:58mm 1fr;gap:8mm;align-items:start}
.seal{position:relative;overflow:hidden;width:58mm;padding:7mm 4.5mm 6mm;text-align:center;color:var(--ink);background:#fbf7ea;border:1.6px solid var(--gold);border-radius:3px;box-shadow:inset 0 0 0 1.6mm #fbf7ea,inset 0 0 0 1.9mm var(--gold),0 10px 26px rgba(14,18,51,.22)}
.seal .wm{position:absolute;width:62mm;left:50%;top:50%;transform:translate(-50%,-50%);opacity:.07}
.seal .mk{width:13mm;position:relative}
.seal .sk{position:relative;margin-top:2.5mm;font-size:7.4px;color:var(--golddk);font-weight:600}
.seal .sn{position:relative;margin-top:1.5mm;font-size:21px;font-weight:600;line-height:1.1}
.seal .rule{width:16mm;margin:3mm auto 3.4mm}
.seal .st{position:relative;font-size:12.4px;font-weight:600;line-height:1.3}
.seal .sh{position:relative;margin-top:2mm;font-size:8.6px;color:var(--text)}
.seal .sb{position:relative;margin-top:4mm;padding-top:3mm;border-top:1px solid rgba(201,162,75,.55);font-size:7.6px;color:var(--golddk);font-weight:600}
.seal .sm{position:relative;margin-top:1.4mm;font-size:8.2px;color:#6a6f95}
.hi .seal .st{font-size:11.6px;line-height:1.5}.hi .seal .sk,.hi .seal .sb{font-size:9px}.hi .seal .sh,.hi .seal .sm{font-size:9.4px}
.crow p{font-size:12.2px;line-height:1.7;color:var(--text)}
.hi .crow p{line-height:1.8}
.crow ul{margin-top:4mm;font-size:12.2px;line-height:1.95;color:var(--ink)}
.crow .cap{font-size:9.5px;color:#6a6f95;margin-top:3mm;letter-spacing:.04em}
.faq{display:grid;grid-template-columns:1fr 1fr;gap:5mm 8mm;margin-top:4mm}
.faq h5{font-size:17px;font-weight:600;color:var(--ink);line-height:1.25}
.hi .faq h5{font-size:13.5px;line-height:1.5}
.faq p{font-size:11.8px;line-height:1.55;color:var(--text);margin-top:2px}
.faqh{font-size:10.5px;color:var(--golddk);margin-top:7mm}
.ct{position:absolute;left:0;right:0;bottom:0;height:100mm;padding:11mm 18mm 0;overflow:hidden;border-top:2px solid var(--gold)}
.ct .mand{width:170mm;right:-60mm;top:-50mm;opacity:.11}
.ct .row{display:grid;grid-template-columns:1fr 36mm;gap:10mm;align-items:center}
.ct h2{font-size:34px;font-weight:600;line-height:1.1}
.hi .ct h2{font-size:27px;line-height:1.4}
.ct .sub{font-size:13px;color:var(--goldlt);margin-top:3mm}
.ct .wa-pill{margin-top:6mm;padding:9px 26px 9px 16px}
.ct .wa-pill .num{font-size:25px}
.ct .loc{margin-top:5mm;font-size:11px;color:var(--ivory)}
.ct .em{margin-top:2mm;font-size:12px;color:var(--goldlt);letter-spacing:.04em}
.ct .qr{width:36mm;height:36mm;padding:3mm}
.ct .scan{font-size:9px;text-align:center;color:var(--mist);margin-top:2mm;line-height:1.35}
.disc{position:absolute;left:18mm;right:18mm;bottom:8mm;font-size:9.3px;line-height:1.5;color:var(--mist);border-top:1px solid rgba(201,162,75,.45);padding-top:3mm;text-align:center}

/* Hindi optical size boost */
.hi .kicker{font-size:13px}
.hi .ab p{font-size:14.6px}
.hi .meet p{font-size:13.6px;line-height:1.8}
.hi .meet ul{font-size:13.4px}
.hi .sc p{font-size:13.6px}
.hi .sc h4{font-size:19px}
.hi .fmts p{font-size:13.4px}
.hi .qd ul{font-size:15px}
.hi .qd .sub{font-size:13.4px}
.hi .note{font-size:14px}
.hi .st p{font-size:13.2px;line-height:1.7}
.hi .st h5{font-size:17px}
.hi .insp p{font-size:14.8px}
.hi .crow p,.hi .crow ul{font-size:13.4px}
.hi .faq p{font-size:12.8px}
.hi .faq h5{font-size:14.6px}
.hi .pil p{font-size:13px}
.hi .ct .sub{font-size:15px}
.hi .ct .loc{font-size:13px}
.hi .disc{font-size:10.4px}
.hi .cv .foot{font-size:14px}
.hi .faqh{font-size:13px}
.hi .ct .scan{font-size:10.5px}
.hi .crow .cap{font-size:11px}
.hi .ar .cta{font-size:18px}
.hi .sankat{font-size:15px}
.hi .verse .src{font-size:13px}
"""


def seal(c):
    """Typeset credential panel used instead of the scanned certificate."""
    return (f'<div class="seal"><img class="wm" src="{MANDALA_DK}" alt=""><img class="mk" src="{MARK_INK}" alt="">'
            f'<div class="sk caps">{c["seal_k"]}</div><div class="sn serif">{c["name_title"]}</div><div class="rule"></div>'
            f'<div class="st serif">{c["seal_t"]}</div><div class="sh">{c["seal_h"]}</div>'
            f'<div class="sb caps">{c["seal_by"]}</div><div class="sm">{c["seal_meta"]}</div></div>')

def brochure(c):
    L = c["lang"]
    serv = "".join(f'<div class="sc{" new" if k == "child" else ""}"><div class="ic">{ICONS[k]}</div><div><h4 class="serif">{t}</h4><p>{d}</p></div></div>' for k, t, d in c["serv"])
    quads = "".join(
        f'<div class="qd {k}"><div class="hd"><div class="ib">{icon_c(k, "#E6CB8A", 34, 2.2)}</div><div><h4 class="serif">{t}</h4><div class="sub">{s}</div></div></div>'
        f'<ul class="chk">{"".join(f"<li>{i}</li>" for i in items)}</ul></div>' for k, t, s, items in c["areas"])
    steps = "".join(f'<div class="st"><div class="n">{i+1}</div><h5 class="serif">{t}</h5><p>{d}</p></div>' for i, (t, d) in enumerate(c["steps"]))
    fmts = "".join(f'<div><h5 class="serif">{a}</h5><p>{b}</p></div>' for a, b in c["formats"])
    faq = "".join(f'<div><h5 class="serif">{q}</h5><p>{a}</p></div>' for q, a in c["faq"])
    pil = "".join(f'<div><h5 class="serif">{a}</h5><p>{b}</p></div>' for a, b in c["pil"])
    tr = f'<div class="tr serif">{c["verse_tr"]}</div>' if c["verse_tr"] else ""
    body = f"""
<section class="pg dark cv"><div class="stars"></div><img class="mand" src="{MANDALA}" alt="">
  <div class="devo tiro rel">{c['devotion']}</div>
  <img class="mk rel" src="{MARK}" alt="">
  <div class="arch rel"><img src="{P_FORMAL}" alt=""></div>
  <h1 class="serif rel">{c['name']}</h1><div class="rule rel"></div>
  <div class="ttl caps rel">{c['title_2l']}</div>
  <div class="tag serif it rel">{c['tagline']} <span>{c['tagline2']}</span></div>
  <div class="cred caps rel">{c['cred_short']}</div>
  <div class="foot caps"><span>{c['loc']}</span><span class="ph">{wa_icon(20)}{PHONE_DISPLAY}</span></div>
</section>

<section class="pg light ab">
  <div class="col"><div class="kicker caps">{c['about_k']}</div><h2 class="serif">{c['about_h']}</h2><div class="rule l"></div>
  <p>{c['about_p1']}</p><p>{c['about_p2']}</p><p>{c['about_p3']}</p></div>
  <div class="ph"><img src="{P_WARM}" alt=""></div><div class="phc serif">{c['name_title']}</div>
  <div class="meet"><img class="mand" src="{MANDALA}" alt="">
    <div class="rel"><h3 class="serif">{c['meet']}</h3><p>{c['meet_p']}</p></div>
    <ul class="chk rel">{"".join(f"<li>{i}</li>" for i in c['cred_list'])}</ul></div>
  <div class="btm"><img class="mk" src="{MARK_INK.replace('mark-ink', 'mark')}" alt=""><div class="q serif">{c['quote']}</div><div class="pil">{pil}</div></div>
</section>

<section class="pg dark sv"><div class="stars"></div><img class="mand" src="{MANDALA}" alt="">
  <div class="kicker c caps rel">{c['serv_k']}</div><h2 class="serif rel">{c['serv_h']}</h2><div class="rule rel"></div>
  <div class="grid6 rel">{serv}</div>
  <div class="fmts rel">{fmts}</div>
  <div class="q serif">{c['values']}</div>
</section>

<section class="pg light ar">
  <div class="kicker c caps">{c['areas_k']}</div><h2 class="serif">{c['areas_h']}</h2><div class="rule"></div>
  <div class="grid4">{quads}</div>
  <div class="note">{icon_c('body', '#E6CB8A', 34, 2)}<div>{c['body_note']}</div></div>
  <div class="cta serif"><img class="mk" src="{MARK}" alt="">{c['areas_cta']}</div>
</section>

<section class="pg dark jr"><div class="stars"></div>
  <div class="kicker c caps rel">{c['journey_k']}</div><h2 class="serif rel">{c['journey_h']}</h2><div class="rule rel"></div>
  <div class="steps">{steps}</div>
  <div class="insp"><img class="mand" src="{MANDALA}" alt="">
    <div class="top rel"><div class="em">{ram_heart()}</div>
      <div><div class="kicker caps">{c['inspo_k']}</div><h3 class="serif">{c['inspo_h']}</h3><p>{c['inspo_p']}</p></div></div>
    <div class="verse rel"><div class="rule"></div><div class="v tiro">{c['verse']}</div>{tr}<div class="src caps">{c['verse_src']}</div></div>
    <div class="sankat rel">{c['sankat']}</div>
  </div>
</section>

<section class="pg light cr">
  <div class="kicker caps">{c['cred_k']}</div><h2 class="serif">{c['cred_h']}</h2><div class="rule l"></div>
  <div class="crow">{seal(c)}<div><p>{c['cred_p']}</p><ul class="chk">{"".join(f"<li>{i}</li>" for i in c['cred_list'])}</ul><div class="cap">{c['cert_cap']}</div></div></div>
  <div class="faqh caps">{c['faq_h']}</div>
  <div class="faq">{faq}</div>
  <div class="ct dark"><div class="stars"></div><img class="mand" src="{MANDALA}" alt="">
    <div class="row rel"><div>
      <div class="kicker caps">{c['cta_k']}</div><h2 class="serif" style="margin-top:3mm">{c['cta_h']}</h2>
      <div class="sub">{c['cta_p']}</div>
      <a class="wa-pill" href="{wa_url(L)}">{wa_icon(30)}<span class="num">{PHONE_DISPLAY}</span></a>
      <div class="loc caps">{c['loc']}</div><div class="em">{EMAIL}</div></div>
      <div><div class="qr">{qr_svg(L)}</div><div class="scan">{c['scan']}</div></div></div>
    <div class="disc">{c['disc']}</div>
  </div>
</section>"""
    return page(f"Dhiraj Sarda - Brochure ({L.upper()})", L, BRO_CSS, body)


if __name__ == "__main__":
    for lg, c in T.items():
        write(f"brochure-{lg}.html", brochure(c))
    print("built brochure")
    import pieces
    pieces.build_all()
