"""Tri-fold, visiting card, flyer, story, posts, DPs, highlights, covers, intake form, letterhead, brand sheet."""
from build import (page, write, wa_icon, FONTS, P_FORMAL, P_WARM, BG_POSTER, HANUMAN, MARK, MARK_INK, MANDALA, MANDALA_DK)
from content import T, PHONE_DISPLAY, EMAIL
from assets import ICONS, icon_c, icon, ram_heart, wa_url, qr_svg, mark

# =====================================================================
# TRI-FOLD  A4 landscape, 2 sides x 3 panels (99mm)
# =====================================================================
TRI_CSS = """
@page{size:297mm 210mm;margin:0}
.side{width:297mm;height:210mm;display:grid;grid-template-columns:repeat(3,99mm);break-after:page;position:relative;overflow:hidden}
.side:last-child{break-after:auto}
.pn{position:relative;overflow:hidden;padding:13mm 10mm}
.pn .mand{opacity:.1}
.pn h2{font-size:28px;font-weight:600;line-height:1.15;margin:2.5mm 0 0}
.hi .pn h2{font-size:21px;line-height:1.45}
.pn .rule{width:28mm;margin:4mm 0 5mm}
.pn p{font-size:11.6px;line-height:1.68}
.hi .pn p{font-size:12.2px;line-height:1.8}
.light p{color:var(--text)}
.dark p{color:#dfe0f0}
/* cover */
.cov{display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:9mm}
.cov .devo{font-size:11px;color:var(--goldlt);opacity:.9}
.cov .mk{width:11mm;margin-top:3mm}
.cov .arch{width:68mm;height:90mm;margin-top:7mm}
.cov h1{font-size:32px;font-weight:600;letter-spacing:.13em;margin-top:8mm;line-height:1.1}
.hi .cov h1{font-size:32px;letter-spacing:0}
.cov .rule{width:40mm;margin:4mm auto}
.cov .ttl{font-size:8.8px;color:var(--goldlt);line-height:1.9}
.hi .cov .ttl{font-size:10.5px;line-height:1.6}
.cov .tag{font-size:19px;margin-top:6mm;font-style:italic}
.hi .cov .tag{font-style:normal;font-size:15px}
.cov .tag span{color:var(--goldlt)}
.cov .loc{position:absolute;bottom:8mm;left:0;right:0;font-size:8.5px;color:var(--mist)}
.hi .cov .loc{font-size:10.5px}
/* back / contact */
.bk{text-align:center;display:flex;flex-direction:column;align-items:center}
.bk .mk{width:15mm;margin-top:8mm}
.bk h2{text-align:center}
.bk .rule{margin:4mm auto 4mm}
.bk .qr{width:40mm;height:40mm;padding:3mm;margin-top:8mm}
.bk .scan{font-size:8px;color:var(--mist);margin-top:2mm}
.hi .bk .scan{font-size:9.5px}
.bk .wa-pill{margin-top:8mm;padding:7px 18px 7px 12px}
.bk .wa-pill .num{font-size:18px}
.bk .loc{font-size:8.5px;margin-top:4mm;color:var(--ivory)}
.bk .eml{font-size:9.5px;margin-top:1.6mm;color:var(--goldlt);letter-spacing:.03em}
.hi .bk .loc{font-size:10.5px}
.bk .disc{position:absolute;left:9mm;right:9mm;bottom:8mm;font-size:7.4px;line-height:1.5;color:var(--mist);border-top:1px solid rgba(201,162,75,.45);padding-top:2.5mm}
.hi .bk .disc{font-size:8.2px}
/* inspiration flap */
.fl{text-align:center}
.fl .em{width:60mm;height:60mm;margin:5mm auto 2mm}
.fl h2{text-align:center}
.fl .rule{margin:4mm auto}
.fl .v{font-size:23px;line-height:1.55;color:var(--goldlt);margin-top:7mm}
.fl .tr{font-size:14px;font-style:italic;margin-top:3mm;color:var(--ivory);font-family:'Cormorant Garamond',serif}
.fl .src{font-size:7.5px;color:var(--gold);margin-top:2.5mm}
.hi .fl .src{font-size:9.5px}
.fl .sk{font-size:10px;color:var(--mist);margin-top:8mm}
.hi .fl .sk{font-size:10.5px}
/* inside */
.in1 .ph{width:34mm;height:43mm;border-radius:999px 999px 6px 6px;overflow:hidden;border:2px solid var(--gold);box-shadow:0 0 0 4px var(--ivory),0 0 0 5px var(--gold);float:right;margin:0 0 3mm 4mm}
.in1 .ph img{width:100%;height:100%;object-fit:cover;object-position:50% 20%}
.in1 p+p{margin-top:2mm}
.in1 .meet{clear:both;margin-top:7mm;background:var(--ink);color:var(--ivory);border-radius:10px;padding:5mm 5mm;border:1px solid var(--gold)}
.in1 .meet h3{font-size:17px;color:var(--goldlt);font-weight:600}
.in1 .meet ul{font-size:10.6px;line-height:1.9;margin-top:2mm}
.hi .in1 .meet ul{font-size:10.4px}
.in1 .pil{display:flex;justify-content:space-between;margin-top:9mm;text-align:center}
.in1 .pil div{flex:1;border-top:1px solid var(--gold);padding-top:2mm;margin:0 1.5mm}
.in1 .pil h5{font-size:17px;font-weight:600}
.in1 .pil p{font-size:9.4px;line-height:1.3}
.sv2 .svi{display:flex;gap:10px;margin-bottom:6.2mm;align-items:flex-start}
.sv2 .svi svg{flex:none;width:30px;height:30px}
.sv2 h4{font-size:17px;color:var(--goldlt);font-weight:600;line-height:1.15}
.hi .sv2 h4{font-size:14.5px;line-height:1.4}
.sv2 .svi p{font-size:10.6px;line-height:1.55;margin-top:2px}
.hi .sv2 .svi p{font-size:11.2px;line-height:1.65}
.sv2 .svi.new h4:after{content:"";display:inline-block;width:6px;height:6px;background:var(--saffron);border-radius:50%;margin-left:6px;vertical-align:middle}
.ar2 .q{margin-bottom:6mm}
.ar2 .q .hd{display:flex;align-items:center;gap:7px}
.ar2 .q .hd .ib{width:28px;height:28px;border-radius:50%;background:var(--ink);display:flex;align-items:center;justify-content:center}
.ar2 .q h4{font-size:19px;font-weight:600}
.hi .ar2 .q h4{font-size:13.5px}
.ar2 .q .sub{font-size:12px;color:var(--golddk);font-style:italic;font-family:'Cormorant Garamond',serif;font-weight:600;margin-left:3px}
.hi .ar2 .q .sub{font-family:inherit;font-style:normal;font-size:9.5px}
.ar2 .q .ls{font-size:10.8px;line-height:1.65;color:var(--text);margin-top:1.5mm;padding-left:35px}
.hi .ar2 .q .ls{font-size:11.4px}
.ar2 .note{margin-top:6mm;background:var(--ink);color:#e6e7f3;border-radius:8px;padding:3mm 4mm;font-size:10px;line-height:1.6;border-left:3px solid var(--saffron)}
.hi .ar2 .note{font-size:10.6px}
.ar2 .note b{color:var(--goldlt);font-weight:500}
.kicker{font-size:8.5px}.hi .kicker{font-size:10.5px}
.fold{position:absolute;top:0;bottom:0;width:0;border-left:1px dashed rgba(201,162,75,.0)}
"""


def trifold(c):
    L = c["lang"]
    serv = "".join(f'<div class="svi{" new" if k == "child" else ""}">{icon_c(k, "#E6CB8A", 30, 2)}<div><h4 class="serif">{t}</h4><p>{d}</p></div></div>' for k, t, d in c["serv"])
    areas = "".join(f'<div class="q"><div class="hd"><div class="ib">{icon_c(k, "#E6CB8A", 17, 2.4)}</div><h4 class="serif">{t}</h4><span class="sub">{s}</span></div>'
                    f'<div class="ls">{" · ".join(items)}</div></div>' for k, t, s, items in c["areas"])
    tr = f'<div class="tr">{c["verse_tr"]}</div>' if c["verse_tr"] else ""
    body = f"""
<section class="side">
  <div class="pn dark fl"><div class="stars"></div><img class="mand" src="{MANDALA}" style="width:150mm;left:-25mm;top:80mm" alt="">
    <div class="kicker c caps rel">{c['inspo_k']}</div><div class="em rel">{ram_heart()}</div>
    <h2 class="serif rel">{c['inspo_h']}</h2><div class="rule rel"></div><p class="rel">{c['inspo_p']}</p>
    <div class="v tiro rel">{c['verse']}</div>{tr}<div class="src caps rel">{c['verse_src']}</div><div class="sk rel">{c['sankat']}</div></div>
  <div class="pn dark bk"><div class="stars"></div>
    <img class="mk rel" src="{MARK}" alt=""><div class="kicker c caps rel" style="margin-top:5mm">{c['cta_k']}</div>
    <h2 class="serif rel">{c['cta_h']}</h2><div class="rule rel"></div><p class="rel" style="text-align:center">{c['cta_p']}</p>
    <div class="qr rel">{qr_svg(L)}</div><div class="scan rel">{c['scan']}</div>
    <a class="wa-pill rel" href="{wa_url(L)}">{wa_icon(20)}<span class="num">{PHONE_DISPLAY}</span></a>
    <div class="loc caps rel">{c['loc']}</div><div class="eml rel">{EMAIL}</div>
    <div class="disc">{c['disc']}</div></div>
  <div class="pn dark cov"><div class="stars"></div><img class="mand" src="{MANDALA}" style="width:140mm;left:-20mm;top:10mm" alt="">
    <div class="devo tiro rel">{c['devotion']}</div><img class="mk rel" src="{MARK}" alt="">
    <div class="arch rel"><img src="{P_FORMAL}" alt=""></div>
    <h1 class="serif rel">{c['name']}</h1><div class="rule rel"></div><div class="ttl caps rel">{c['title_2l']}</div>
    <div class="tag serif rel">{c['tagline']} <span>{c['tagline2']}</span></div>
    <div class="loc caps">{c['cred_short']}</div></div>
</section>
<section class="side">
  <div class="pn light in1"><div class="kicker caps">{c['about_k']}</div><h2 class="serif">{c['about_h']}</h2><div class="rule l"></div>
    <div class="ph"><img src="{P_WARM}" alt=""></div><p>{c['about_p1']}</p><p>{c['about_p2']}</p><p>{c['about_p3']}</p>
    <div class="meet"><h3 class="serif">{c['meet']}</h3><ul class="chk">{"".join(f"<li>{i}</li>" for i in c['cred_list'])}</ul></div>
    <div class="pil">{"".join(f'<div><h5 class="serif">{a}</h5><p>{b}</p></div>' for a, b in c['pil'])}</div></div>
  <div class="pn dark sv2"><div class="stars"></div><img class="mand" src="{MANDALA}" style="width:160mm;left:-30mm;bottom:-90mm" alt="">
    <div class="kicker caps rel">{c['serv_k']}</div><h2 class="serif rel">{c['serv_h']}</h2><div class="rule l rel"></div><div class="rel">{serv}</div></div>
  <div class="pn light ar2"><div class="kicker caps">{c['areas_k']}</div><h2 class="serif">{c['areas_h']}</h2><div class="rule l"></div>
    {areas}<div class="note">{c['body_note']}</div></div>
</section>"""
    return page(f"Dhiraj Sarda - Trifold ({L.upper()})", L, TRI_CSS, body)


# =====================================================================
# VISITING CARD  89 x 51 mm trim + 3 mm bleed = 95 x 57 mm
# =====================================================================
CARD_CSS = """
@page{size:95mm 57mm;margin:0}
html{background:#0E1233}
.cd{width:95mm;height:57.15mm;position:relative;overflow:hidden;break-after:page}
.cd:last-child{break-after:auto}
.safe{position:absolute;left:8mm;right:8mm;top:8mm;bottom:8mm}
.fr .mand{width:120mm;left:50%;top:50%;margin:-60mm 0 0 -60mm;opacity:.13}
.fr .safe{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.fr .devo{font-size:7px;color:var(--goldlt);opacity:.85}
.fr .mk{width:11mm;margin-top:1.6mm}
.fr h1{font-size:19px;font-weight:600;letter-spacing:.16em;margin-top:2.6mm;line-height:1}
.hi .fr h1{font-size:21px;letter-spacing:0;line-height:1.3;margin-top:1.6mm}
.fr .rule{width:26mm;margin:2.4mm auto 2.2mm}
.fr .rule:after{width:5px;height:5px;top:-2px}
.fr .ttl{font-size:6.3px;color:var(--goldlt);line-height:1.85;letter-spacing:.2em}
.hi .fr .ttl{font-size:8px;line-height:1.6}
.frame{position:absolute;inset:5.2mm;border:.6px solid rgba(201,162,75,.6);border-radius:2px;pointer-events:none}
.bkc{color:var(--ink)}
.bkc .safe{display:grid;grid-template-columns:1fr 20mm;gap:4mm}
.bkc h2{font-size:15px;font-weight:600;letter-spacing:.08em;line-height:1.05}
.hi .bkc h2{font-size:16px;letter-spacing:0;line-height:1.3}
.bkc .t{font-size:6.6px;color:var(--golddk);line-height:1.5;margin-top:1mm;font-weight:500}
.hi .bkc .t{font-size:7.6px}
.bkc .rule{width:14mm;margin:2mm 0 2mm}
.bkc .rule:after{width:4px;height:4px;top:-1.5px;left:0;transform:rotate(45deg)}
.bkc ul{font-size:6.8px;line-height:1.6;color:var(--text)}
.hi .bkc ul{font-size:7.6px;line-height:1.55}
.bkc .chk li{padding-left:8px}.bkc .chk li:before{width:3.2px;height:3.2px;top:.6em;left:0}
.bkc .ph{position:absolute;left:0;bottom:6.6mm;display:flex;align-items:center;gap:4px;font-family:'Jost',sans-serif;font-weight:600;font-size:11.5px;letter-spacing:.02em}
.bkc .eml{position:absolute;left:0;bottom:3.3mm;font-size:7.2px;color:var(--ink);letter-spacing:.02em;font-weight:500}
.bkc .loc{position:absolute;left:0;bottom:0;font-size:5.6px;color:var(--golddk);letter-spacing:.14em}
.hi .bkc .loc{font-size:6.8px;letter-spacing:0;bottom:-.4mm}
.bkc .qr{width:20mm;height:20mm;padding:1.4mm;border-radius:4px;border-width:.8px;background:#fff}
.bkc .scan{font-size:4.8px;color:var(--golddk);text-align:center;margin-top:1mm;line-height:1.3}
.hi .bkc .scan{font-size:5.6px}
.bkc .mk{width:7mm;display:block;margin:2.4mm auto 0;opacity:.95}
.bkc .band{position:absolute;left:0;right:0;bottom:0;height:4.6mm;background:var(--ink)}
.bkc .band:before{content:"";position:absolute;left:0;right:0;top:0;height:.6px;background:var(--gold)}
"""


def card(c):
    L = c["lang"]
    body = f"""
<section class="cd dark fr"><div class="stars"></div><img class="mand" src="{MANDALA}" alt=""><div class="frame"></div>
  <div class="safe"><div class="devo tiro">{c['devotion']}</div><img class="mk" src="{MARK}" alt="">
  <h1 class="serif">{c['name']}</h1><div class="rule"></div><div class="ttl caps">{c['title_2l']}</div></div></section>
<section class="cd light bkc"><div class="band"></div>
  <div class="safe"><div style="position:relative">
    <h2 class="serif">{c['name']}</h2><div class="t">{c['title']}</div><div class="rule"></div>
    <ul class="chk">{"".join(f"<li>{s}</li>" for s in c['card_services'])}</ul>
    <div class="ph">{wa_icon(12)}{PHONE_DISPLAY}</div><div class="eml">{EMAIL}</div><div class="loc caps">{c['loc_short']} &nbsp;·&nbsp; {c['cred_short'].split('·')[0].strip()}</div></div>
    <div><div class="qr">{qr_svg(L)}</div><div class="scan">{c['scan']}</div><img class="mk" src="{MARK_INK}" alt=""></div></div></section>"""
    return page(f"Dhiraj Sarda - Card ({L.upper()})", L, CARD_CSS, body)


def card_mockup():
    css = """body{width:1600px;height:1100px;overflow:hidden;background:radial-gradient(ellipse at 40% 30%,#2b3380 0%,#141a52 45%,#0a0d28 100%)}
.c{position:absolute;width:712px;height:408px;overflow:hidden;border-radius:6px;box-shadow:0 40px 80px rgba(0,0,0,.55),0 8px 18px rgba(0,0,0,.35)}
.c img{position:absolute;width:760px;height:456px;left:-24px;top:-24px}
.a{left:150px;top:150px;transform:rotate(-7deg)}
.b{left:760px;top:520px;transform:rotate(5deg)}
.cap{position:absolute;left:150px;bottom:70px;color:#E6CB8A;font:500 15px Jost;letter-spacing:.3em;text-transform:uppercase;opacity:.8}
.mand{width:900px;right:-250px;top:-300px;opacity:.07}"""
    o = "../out/3-Visiting-Card"
    body = f"""<div class="stars"></div><img class="mand" src="{MANDALA}" alt="">
<div class="c a"><img src="{o}/Dhiraj-Sarda-Card-EN-print-p1.png"></div>
<div class="c b"><img src="{o}/Dhiraj-Sarda-Card-EN-print-p2.png"></div>
<div class="cap">Visiting card &nbsp;·&nbsp; 89 × 51 mm</div>"""
    return page("Card mockup", "en", css, body)


# =====================================================================
# INFO FLYER  1240 x 1754 (A4 @150dpi) - the WhatsApp-forward one-pager
# =====================================================================
FLY_CSS = """
body{width:1240px;height:1754px;position:relative;overflow:hidden;background:var(--ink)}
.top{position:absolute;left:0;right:0;top:0;height:800px;overflow:hidden}
.top .mand{width:1100px;left:-300px;top:-160px;opacity:.12}
.devo{position:absolute;left:0;right:0;top:40px;text-align:center;font-size:22px;color:var(--goldlt);opacity:.9}
.top .arch{position:absolute;left:90px;top:120px;width:440px;height:560px}
.who{position:absolute;left:600px;right:60px;top:120px}
.who .mk{width:84px}
.who h1{font-size:60px;font-weight:600;letter-spacing:.09em;line-height:1.02;margin-top:22px;white-space:nowrap}
.hi .who h1{font-size:82px;letter-spacing:0;line-height:1.25}
.who .rule{width:200px;margin:28px 0 24px}
.who .ttl{font-size:19px;color:var(--goldlt);line-height:1.8}
.hi .who .ttl{font-size:26px;line-height:1.55}
.who .tag{font-size:36px;font-style:italic;margin-top:24px;line-height:1.25}
.hi .who .tag{font-style:normal;font-size:33px}
.who .tag span{color:var(--goldlt)}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:30px}
.chips span{border:1.5px solid rgba(201,162,75,.8);border-radius:999px;padding:8px 18px;font-size:16px;background:rgba(201,162,75,.08)}
.hi .chips span{font-size:19px}
.mid{position:absolute;left:0;right:0;top:760px;height:720px;padding:46px 70px 0;border-top:3px solid var(--gold);border-radius:44px 44px 0 0}
.sh{display:flex;align-items:center;gap:18px;font-size:16px;color:var(--golddk);font-weight:600;margin-bottom:20px}
.hi .sh{font-size:21px}
.sh:after{content:"";flex:1;height:1px;background:rgba(201,162,75,.6)}
.sv{display:grid;grid-template-columns:repeat(3,1fr);gap:14px 18px;margin-bottom:34px}
.sv>div{display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.6);border:1px solid rgba(201,162,75,.6);border-radius:14px;padding:13px 16px}
.sv>div.new{border:1.5px solid var(--saffron);background:rgba(255,255,255,.85)}
.sv .ib{width:54px;height:54px;border-radius:50%;background:var(--ink);display:flex;align-items:center;justify-content:center;flex:none}
.sv h4{font-size:23px;font-weight:600;color:var(--ink);line-height:1.1}
.hi .sv h4{font-size:21px;line-height:1.35}
.ar{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.ar .q{background:rgba(255,255,255,.55);border-top:3px solid var(--gold);border-radius:4px 4px 14px 14px;padding:16px 18px 14px}
.ar .q.body{border-top-color:var(--saffron);background:rgba(255,255,255,.8)}
.ar h4{font-size:28px;font-weight:600;color:var(--ink);display:flex;align-items:center;gap:10px}
.hi .ar h4{font-size:25px}
.ar ul{font-size:17.5px;line-height:1.75;color:var(--text);margin-top:8px}
.hi .ar ul{font-size:18.5px;line-height:1.7}
.ar .chk li{padding-left:16px}.ar .chk li:before{width:6px;height:6px}
.nt{font-size:15px;color:var(--text);margin-top:16px;text-align:center;font-style:italic}
.hi .nt{font-style:normal;font-size:17px}
.bot{position:absolute;left:0;right:0;top:1480px;bottom:0;padding:0 70px}
.bot .mand{width:900px;right:-350px;top:-200px;opacity:.08}
.ins{display:flex;align-items:center;gap:22px;padding-top:22px;width:560px}
.ins .em{width:120px;height:120px;flex:none}
.ins h3{font-size:32px;font-weight:600;color:var(--ivory)}
.hi .ins h3{font-size:30px}
.ins .v{font-size:25px;color:var(--goldlt);line-height:1.4;margin-top:4px}
.ins .src{font-size:13px;color:var(--gold);margin-top:2px}
.hi .ins .src{font-size:16px}
.ct{position:absolute;right:70px;top:20px;display:flex;align-items:center;gap:20px}
.ct .wa-pill{padding:12px 28px 12px 18px}
.ct .wa-pill .num{font-size:34px}
.ct .qr{width:130px;height:130px;padding:9px}
.ct .loc{font-size:15px;text-align:center;margin-top:10px;color:var(--ivory)}
.ct .eml{font-size:17px;text-align:center;margin-top:6px;color:var(--goldlt);letter-spacing:.03em}
.hi .ct .loc{font-size:18px}
.disc{position:absolute;left:70px;right:70px;bottom:22px;font-size:13px;line-height:1.5;color:var(--mist);text-align:center;border-top:1px solid rgba(201,162,75,.4);padding-top:12px}
.hi .disc{font-size:14.5px}
"""


def flyer(c):
    L = c["lang"]
    sv = "".join(f'<div class="{"new" if k == "child" else ""}"><div class="ib">{icon_c(k, "#E6CB8A", 34, 2.2)}</div><h4 class="serif">{t}</h4></div>' for k, t, d in c["serv"])
    ar = "".join(f'<div class="q {k}"><h4 class="serif">{icon_c(k, "#8a6a1f", 34, 2.2)}{t}</h4><ul class="chk">{"".join(f"<li>{i}</li>" for i in items)}</ul></div>' for k, t, s, items in c["areas"])
    chips = "".join(f"<span>{x}</span>" for x in [c["cred_list"][1], c["cred_list"][0], c["loc_short"]])
    body = f"""
<div class="top dark"><div class="stars"></div><img class="mand" src="{MANDALA}" alt="">
  <div class="devo tiro">{c['devotion']}</div>
  <div class="arch"><img src="{P_FORMAL}" alt=""></div>
  <div class="who"><img class="mk" src="{MARK}" alt=""><h1 class="serif">{c['name']}</h1><div class="rule l"></div>
    <div class="ttl caps">{c['title_2l']}</div><div class="tag serif">{c['tagline']}<br><span>{c['tagline2']}</span></div>
    <div class="chips">{chips}</div></div></div>
<div class="mid light">
  <div class="sh caps">{c['serv_h']}</div><div class="sv">{sv}</div>
  <div class="sh caps">{c['areas_h']}</div><div class="ar">{ar}</div>
  <div class="nt serif">{c['disc_short']}</div></div>
<div class="bot dark"><div class="stars"></div><img class="mand" src="{MANDALA}" alt="">
  <div class="ins rel"><div class="em">{ram_heart()}</div><div><h3 class="serif">{c['inspo_h']}</h3><div class="v tiro">{c['verse']}</div><div class="src caps">{c['verse_src']}</div></div></div>
  <div class="ct"><div style="text-align:center"><a class="wa-pill" href="{wa_url(L)}">{wa_icon(40)}<span class="num">{PHONE_DISPLAY}</span></a><div class="loc caps">{c['wa_cta']} &nbsp;·&nbsp; {c['loc_short']}</div><div class="eml">{EMAIL}</div></div><div class="qr">{qr_svg(L)}</div></div>
  <div class="disc">{c['disc']}</div></div>"""
    return page(f"Flyer {L}", L, FLY_CSS, body)


# =====================================================================
# STORY POSTER 1080 x 1920
# =====================================================================
STORY_CSS = """
body{width:1080px;height:1920px;position:relative;overflow:hidden}
.art{position:absolute;left:0;right:0;bottom:150px;height:1180px;background:url('BGP') center bottom/auto 100% no-repeat;-webkit-mask-image:radial-gradient(ellipse 42% 50% at 50% 66%,#000 35%,transparent 100%);opacity:.6}
.wrap{position:relative;display:flex;flex-direction:column;align-items:center;padding-top:70px}
.devo{font-size:26px;color:var(--goldlt);opacity:.9}
.mk{width:88px;margin-top:18px}
.ribbon{margin-top:30px;padding:12px 44px;border:2px solid var(--gold);border-radius:999px;font-size:25px;color:var(--goldlt);background:rgba(201,162,75,.12)}
.hi .ribbon{font-size:31px}
.arch{width:560px;height:650px;margin-top:40px}
h1{font-size:100px;font-weight:600;letter-spacing:.1em;line-height:1.05;margin-top:48px;text-align:center;text-shadow:0 2px 24px rgba(14,18,51,.9)}
.hi h1{font-size:108px;letter-spacing:0;line-height:1.25;margin-top:34px}
.rule{width:420px;margin-top:24px}
.ttl{margin-top:24px;font-size:22px;color:var(--goldlt);text-align:center;line-height:1.75;text-shadow:0 2px 18px rgba(14,18,51,.95)}
.hi .ttl{font-size:32px;line-height:1.5}
.chips{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:44px;width:900px}
.chips span{text-align:center;border:1.5px solid var(--gold);border-radius:999px;padding:13px 10px;font-size:25px;background:rgba(14,18,51,.65);backdrop-filter:blur(4px)}
.hi .chips span{font-size:28px}
.bar{position:absolute;left:0;right:0;bottom:0;height:200px;background:var(--ivory);border-top:4px solid var(--gold);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;color:var(--ink)}
.bar .row{display:flex;align-items:center;gap:18px}
.bar .num{font-size:70px;font-weight:600;letter-spacing:.03em;font-family:'Jost',sans-serif}
.bar .sub{font-size:24px;color:var(--golddk)}
.hi .bar .sub{font-size:30px}
""".replace("BGP", BG_POSTER)


def story(c):
    chips = "".join(f"<span>{x}</span>" for x in c["poster_chips"])
    body = f"""<div class="art"></div><div class="stars"></div>
<div class="wrap"><div class="devo tiro">{c['devotion']}</div><img class="mk" src="{MARK}" alt="">
<div class="ribbon caps">{c['poster_top']}</div><div class="arch"><img src="{P_FORMAL}" alt=""></div>
<h1 class="serif">{c['name']}</h1><div class="rule"></div><div class="ttl caps">{c['title_2l']}</div>
<div class="chips">{chips}</div></div>
<div class="bar"><div class="row">{wa_icon(66)}<span class="num">{PHONE_DISPLAY}</span></div><div class="sub caps">{c['poster_sub']}</div></div>"""
    return page(f"Story {c['lang']}", c["lang"], STORY_CSS, body, "dark")


# =====================================================================
# INSTAGRAM / WHATSAPP POSTS 1080 x 1350
# =====================================================================
POST_CSS = """
body{width:1080px;height:1350px;position:relative;overflow:hidden}
.wrap{position:absolute;left:90px;right:90px;top:90px;bottom:200px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.kicker{font-size:19px}.hi .kicker{font-size:24px}
h2{font-size:70px;font-weight:600;line-height:1.08;margin-top:22px}
.hi h2{font-size:58px;line-height:1.4}
.rule{width:180px;margin:34px auto}
p.b{font-size:28px;line-height:1.55;max-width:820px}
.hi p.b{font-size:28px;line-height:1.7}
.dark p.b{color:#dfe0f0}.light p.b{color:var(--text)}
.foot{position:absolute;left:0;right:0;bottom:0;height:150px;display:flex;align-items:center;justify-content:space-between;padding:0 80px;border-top:2px solid var(--gold)}
.dark .foot{background:rgba(14,18,51,.75)}
.light .foot{background:var(--ink);color:var(--ivory)}
.foot .id{display:flex;align-items:center;gap:18px}
.foot .id img{width:64px}
.foot .id b{font-family:'Cormorant Garamond','Noto Serif Devanagari',serif;font-size:30px;font-weight:600;letter-spacing:.12em;display:block}
.hi .foot .id b{letter-spacing:0;font-size:32px}
.foot .id span{font-size:14px;color:var(--goldlt);letter-spacing:.2em}
.hi .foot .id span{font-size:17px;letter-spacing:0}
.foot .ph{display:flex;align-items:center;gap:12px;font-family:'Jost',sans-serif;font-weight:600;font-size:34px}
.mand{opacity:.1}
.arch{width:420px;height:500px;margin-bottom:46px}
.em{width:330px;height:330px;margin-bottom:10px}
.han{width:540px;height:540px;margin:-50px 0 -14px;mix-blend-mode:lighten;-webkit-mask:radial-gradient(circle,#000 50%,transparent 70%);mask:radial-gradient(circle,#000 50%,transparent 70%)}
.ic{width:250px;height:250px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:radial-gradient(circle,rgba(201,162,75,.18),transparent 70%);border:1.5px solid rgba(201,162,75,.6);margin-bottom:46px;box-shadow:0 0 0 14px rgba(201,162,75,.08)}
.items{display:grid;grid-template-columns:1fr 1fr;gap:16px 22px;margin-top:34px;width:880px;text-align:left}
.items div{display:flex;align-items:center;gap:14px;border:1.5px solid rgba(201,162,75,.6);border-radius:16px;padding:18px 20px;font-size:25px;background:rgba(255,255,255,.04)}
.hi .items div{font-size:25px}
.items div svg{flex:none}
.nt{margin-top:30px;font-size:21px;color:var(--goldlt);border-left:4px solid var(--saffron);padding:8px 16px;text-align:left}
.hi .nt{font-size:23px}
.v{font-size:44px;color:var(--goldlt);line-height:1.45;margin-top:30px}
"""


def post(c, kind):
    L, P = c["lang"], c["posts"][kind]
    light = kind == "child"
    foot = (f'<div class="foot"><div class="id"><img src="{MARK}" alt=""><div><b>{c["name"]}</b><span class="caps">{c["title_short"]}</span></div></div>'
            f'<div class="ph">{wa_icon(44)}{PHONE_DISPLAY}</div></div>')
    if kind == "intro":
        inner = f'<div class="arch"><img src="{P_WARM}" alt="" style="object-position:50% 18%"></div><div class="kicker c caps">{P["k"]}</div><h2 class="serif">{P["h"]}</h2><div class="rule"></div><p class="b">{P["p"]}</p>'
    elif kind == "child":
        inner = f'<div class="ic">{icon_c("child", "#8a6a1f", 150, 1.6)}</div><div class="kicker c caps">{P["k"]}</div><h2 class="serif" style="color:var(--ink)">{P["h"]}</h2><div class="rule"></div><p class="b">{P["p"]}</p>'
    elif kind == "body":
        its = "".join(f'<div>{icon_c(k, "#E6CB8A", 40, 2)}<span>{t}</span></div>' for k, t in zip(("mind", "body", "heart", "med"), P["items"]))
        inner = f'<div class="kicker c caps">{P["k"]}</div><h2 class="serif">{P["h"]}</h2><div class="rule"></div><p class="b">{P["p"]}</p><div class="items">{its}</div><div class="nt">{P["note"]}</div>'
    else:
        inner = f'<img class="han" src="{HANUMAN}" alt=""><div class="kicker c caps">{P["k"]}</div><h2 class="serif">{P["h"]}</h2><div class="rule"></div><p class="b">{P["p"]}</p><div class="v tiro">{c["verse"]}</div>'
    mand = f'<img class="mand" src="{MANDALA_DK if light else MANDALA}" style="width:1300px;left:-110px;top:-80px" alt="">'
    body = f'{"" if light else "<div class=stars></div>"}{mand}<div class="wrap">{inner}</div>{foot}'
    return page(f"Post {kind} {L}", L, POST_CSS, body, "light" if light else "dark")


# =====================================================================
# PROFILE PICTURES 1080 x 1080 + highlight covers
# =====================================================================
DP_CSS = """
body{width:1080px;height:1080px;position:relative;overflow:hidden}
.mand{width:1240px;left:-80px;top:-160px;opacity:.12}
.ring{position:absolute;left:50%;top:70px;width:620px;height:620px;margin-left:-310px;border-radius:50%;overflow:hidden;border:5px solid var(--gold);box-shadow:0 0 0 14px #0E1233,0 0 0 16px var(--gold),0 0 90px rgba(201,162,75,.35)}
.ring img{width:100%;height:100%;object-fit:cover;object-position:50% 14%}
.name{position:absolute;left:0;right:0;top:752px;text-align:center;font-size:66px;font-weight:600;letter-spacing:.12em;line-height:1}
.hi .name{font-size:76px;letter-spacing:0;top:740px;line-height:1.2}
.sub{position:absolute;left:0;right:0;top:850px;text-align:center;font-size:23px;color:var(--goldlt)}
.hi .sub{font-size:32px;top:858px}
.mk{position:absolute;left:50%;top:922px;width:66px;margin-left:-33px}
/* full-bleed variant for WhatsApp circle crop */
.full{position:absolute;inset:0}
.full img{width:100%;height:100%;object-fit:cover;object-position:50% 22%}
.full:after{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 46%,transparent 58%,rgba(14,18,51,.35) 72%,rgba(14,18,51,.85) 100%)}
.halo{position:absolute;inset:26px;border-radius:50%;border:3px solid var(--gold);box-shadow:0 0 0 10px rgba(201,162,75,.18)}
/* logo */
.lg{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.lg img.m{width:420px}
.lg .n{font-size:74px;font-weight:600;letter-spacing:.12em;margin-top:34px;line-height:1.1}
.hi .lg .n{font-size:86px;letter-spacing:0;line-height:1.3}
.lg .rule{width:380px;margin-top:22px}
.lg .s{margin-top:22px;font-size:23px;color:var(--goldlt);text-align:center}
.hi .lg .s{font-size:32px}
"""


def dp(c, kind):
    L = c["lang"]
    if kind == "portrait":
        b = f'<div class="stars"></div><img class="mand" src="{MANDALA}" alt=""><div class="ring"><img src="{P_FORMAL}" alt=""></div><div class="name serif">{c["name"]}</div><div class="sub caps">{c["title_short"]}</div><img class="mk" src="{MARK}" alt="">'
    elif kind == "warm":
        b = f'<div class="full"><img src="{P_WARM}" alt=""></div><div class="halo"></div>'
    else:
        b = f'<div class="stars"></div><img class="mand" src="{MANDALA}" alt=""><div class="lg"><img class="m rel" src="{MARK}" alt=""><div class="n serif rel">{c["name"]}</div><div class="rule rel"></div><div class="s caps rel">{c["title_short"]}</div></div>'
    return page(f"DP {kind} {L}", L, DP_CSS, b, "dark")


CAL = '<rect x="7" y="10" width="34" height="31" rx="4"/><path d="M7 19h34M16 6v8M32 6v8"/><path d="M17 29l5 5 9-10"/>'


def highlight(kind):
    inner = {
        "sessions": icon_c("hypno", "#E6CB8A", 360, 1.4),
        "inner-child": icon_c("child", "#E6CB8A", 360, 1.4),
        "healing": icon_c("heart", "#E6CB8A", 360, 1.4),
        "about": f'<img src="{MARK}" style="width:420px" alt="">',
        "inspiration": f'<div style="width:470px;height:470px">{ram_heart()}</div>',
        "book": icon(CAL, "#E6CB8A", 340, 1.5),
    }[kind]
    css = """body{width:1080px;height:1080px;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}
.c{position:relative;width:700px;height:700px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:3px solid rgba(201,162,75,.8);box-shadow:0 0 0 18px rgba(201,162,75,.08),0 0 120px rgba(201,162,75,.18) inset}
.mand{width:1300px;left:-110px;top:-110px;opacity:.1}"""
    return page(f"Highlight {kind}", "en", css, f'<div class="stars"></div><img class="mand" src="{MANDALA}" alt=""><div class="c">{inner}</div>', "dark")


# =====================================================================
# COVERS - Facebook 1640x624, LinkedIn 1584x396, YouTube 2560x1440
# =====================================================================
def cover(kind):
    c = T["en"]
    W, H = {"facebook": (1640, 624), "linkedin": (1584, 396), "youtube": (2560, 1440)}[kind]
    # text block position: LinkedIn photo sits bottom-left -> right side; YouTube safe zone centre 1546x423
    if kind == "youtube":
        block = "left:507px;right:507px;top:508px;height:423px;justify-content:center;align-items:center;text-align:center"
        ns, ts, gs = 92, 22, 36
    elif kind == "linkedin":
        block = "left:560px;right:70px;top:0;bottom:0;justify-content:center;align-items:flex-end;text-align:right"
        ns, ts, gs = 58, 14, 25
    else:
        block = "left:560px;right:80px;top:0;bottom:0;justify-content:center;align-items:flex-end;text-align:right"
        ns, ts, gs = 76, 17, 32
    css = f"""body{{width:{W}px;height:{H}px;position:relative;overflow:hidden}}
.mand{{width:{int(H*1.9)}px;left:{-int(H*0.35)}px;top:50%;margin-top:{-int(H*0.95)}px;opacity:.16}}
.glow{{position:absolute;left:{-int(H*0.2)}px;top:0;bottom:0;width:{int(H*1.6)}px;background:radial-gradient(circle at 45% 50%,rgba(227,139,58,.18),transparent 60%)}}
.b{{position:absolute;display:flex;flex-direction:column;{block}}}
.b .mk{{width:{int(ns*1.1)}px}}
.b h1{{font-size:{ns}px;font-weight:600;letter-spacing:.12em;line-height:1;margin-top:{int(ns*.3)}px}}
.b .ttl{{font-size:{ts}px;color:var(--goldlt);margin-top:{int(ns*.35)}px;line-height:1.7}}
.b .tag{{font-size:{gs}px;font-style:italic;margin-top:{int(ns*.25)}px}}
.b .tag span{{color:var(--goldlt)}}"""
    body = f"""<div class="stars"></div><div class="glow"></div><img class="mand" src="{MANDALA}" alt="">
<div class="b"><img class="mk" src="{MARK}" alt=""><h1 class="serif">{c['name']}</h1><div class="ttl caps">{c['title']}</div>
<div class="tag serif">{c['tagline']} <span>{c['tagline2']}</span></div></div>"""
    return page(f"Cover {kind}", "en", css, body, "dark")


# =====================================================================
# CLIENT INTAKE & CONSENT FORM (bilingual, print-friendly white)
# =====================================================================
FORM_CSS = """
@page{size:210mm 297mm;margin:0}
body{color:var(--ink);background:#fff}
.pg{width:210mm;height:297mm;position:relative;overflow:hidden;padding:11mm 16mm 16mm;break-after:page}
.pg:last-child{break-after:auto}
.hd{display:flex;align-items:center;gap:12px;border-bottom:1.5px solid var(--gold);padding-bottom:4mm}
.hd img{width:13mm}
.hd b{font-family:'Cormorant Garamond',serif;font-size:22px;letter-spacing:.14em;display:block;line-height:1}
.hd span{font-size:8.5px;color:var(--golddk);letter-spacing:.18em}
.hd .r{margin-left:auto;text-align:right;font-size:9.5px;color:#555;line-height:1.5}
h1{font-family:'Cormorant Garamond',serif;font-size:26px;font-weight:600;margin-top:4mm;line-height:1.1}
h1 small{display:block;font-family:'Noto Sans Devanagari',sans-serif;font-size:15px;font-weight:500;color:var(--golddk);margin-top:1mm}
.intro{font-size:10px;color:#444;margin-top:2mm;line-height:1.5}
h3{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--golddk);margin:5mm 0 2.5mm;display:flex;gap:10px;align-items:center}
h3 span{letter-spacing:0;text-transform:none;font-family:'Noto Sans Devanagari';font-size:11.5px;color:var(--golddk)}
h3:after{content:"";flex:1;height:1px;background:rgba(201,162,75,.6)}
.f{display:grid;gap:3mm 6mm}
.f2{grid-template-columns:1fr 1fr}.f3{grid-template-columns:2fr 1fr 1fr}
.fld{font-size:9.6px;color:#333}
.fld i{font-style:normal;color:#8a6a1f;font-family:'Noto Sans Devanagari';font-size:9.2px}
.fld .ln{border-bottom:1px solid #9aa0c0;height:5.6mm}
.box{border:1px solid #9aa0c0;border-radius:4px;height:18mm;margin-top:1.5mm}
.qs{font-size:9.6px;line-height:1.5}
.qs .q{display:grid;grid-template-columns:1fr 26mm;gap:4mm;padding:.75mm 0;border-bottom:1px dotted #c8cbe0}
.qs .q i{font-style:normal;color:#8a6a1f;font-family:'Noto Sans Devanagari';font-size:9.2px;display:block}
.yn{display:flex;gap:4mm;align-items:center;justify-content:flex-end;font-size:9.4px}
.yn span:before{content:"";display:inline-block;width:3.2mm;height:3.2mm;border:1px solid #6a6f95;border-radius:1px;margin-right:1.5mm;vertical-align:-.6mm}
.cons{font-size:9.6px;line-height:1.55}
.cons li{display:grid;grid-template-columns:5mm 1fr;padding:1.4mm 0;border-bottom:1px dotted #e0e2ee;list-style:none}
.cons li:before{content:"";width:3.2mm;height:3.2mm;border:1px solid #6a6f95;border-radius:1px;margin-top:.6mm}
.cons i{font-style:normal;color:#5a5f85;font-family:'Noto Sans Devanagari';font-size:9.2px;display:block}
.sig{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:6mm;margin-top:6mm}
.ft{position:absolute;left:16mm;right:16mm;bottom:8mm;border-top:1px solid rgba(201,162,75,.6);padding-top:2.5mm;font-size:8.4px;color:#666;display:flex;justify-content:space-between}
.conf{font-size:9px;color:#555;background:#faf6ea;border-left:3px solid var(--gold);padding:2.5mm 4mm;margin-top:4mm;line-height:1.5}
"""


def intake():
    def fld(en, hi, cls=""):
        return f'<div class="fld {cls}">{en} <i>/ {hi}</i><div class="ln"></div></div>'

    def q(en, hi):
        return f'<div class="q"><div>{en}<i>{hi}</i></div><div class="yn"><span>Yes</span><span>No</span></div></div>'

    hd = (f'<div class="hd"><img src="{MARK_INK}" alt=""><div><b>DHIRAJ SARDA</b><span>PAST LIFE REGRESSION THERAPIST · HYPNOTHERAPIST</span></div>'
          f'<div class="r">{PHONE_DISPLAY}<br>{EMAIL}<br>Delhi · Online</div></div>')
    ft = '<div class="ft"><span>Confidential client record · गोपनीय</span><span>Page PAGE / 2</span></div>'
    med = [("Are you currently under a doctor's care for any condition?", "क्या आप किसी रोग के लिए वर्तमान में डॉक्टर के उपचार में हैं?"),
           ("Are you taking any regular medicines?", "क्या आप नियमित रूप से कोई दवा ले रहे हैं?"),
           ("Have you ever been diagnosed with epilepsy or seizures?", "क्या आपको कभी मिर्गी या दौरे की समस्या बताई गई है?"),
           ("Have you ever been diagnosed with psychosis, schizophrenia or bipolar disorder?", "क्या आपको कभी साइकोसिस, स्किज़ोफ्रेनिया या बाइपोलर डिसऑर्डर बताया गया है?"),
           ("Do you have a heart condition, or very high/low blood pressure?", "क्या आपको हृदय रोग या बहुत अधिक/कम रक्तचाप है?"),
           ("Do you have diabetes (sugar)? If yes, it is managed by: ________", "क्या आपको डायबिटीज़ (शुगर) है? यदि हाँ, उपचार किसके द्वारा: ________"),
           ("Are you pregnant?", "क्या आप गर्भवती हैं?"),
           ("Are you currently receiving counselling or psychiatric care?", "क्या आप वर्तमान में काउंसलिंग या मनोचिकित्सा उपचार ले रहे हैं?"),
           ("Have you had thoughts of harming yourself recently?", "क्या हाल में आपके मन में स्वयं को नुकसान पहुँचाने के विचार आए हैं?"),
           ("Have you consumed alcohol or any intoxicant in the last 24 hours?", "क्या पिछले 24 घंटों में आपने शराब या कोई नशीला पदार्थ लिया है?")]
    cons = [("I understand that Past Life Regression and Hypnotherapy are complementary practices and not a substitute for medical or psychiatric treatment.", "मैं समझता/समझती हूँ कि ये पूरक पद्धतियाँ हैं, चिकित्सा या मनोचिकित्सा उपचार का विकल्प नहीं।"),
            ("I will continue any treatment and medicines prescribed by my doctor, and will not stop them because of these sessions.", "मैं डॉक्टर द्वारा दी गई दवाइयाँ और उपचार जारी रखूँगा/रखूँगी, और इन सत्रों के कारण उन्हें बंद नहीं करूँगा/करूँगी।"),
            ("I understand that no specific result or cure is promised or guaranteed, and experiences differ from person to person.", "मैं समझता/समझती हूँ कि किसी विशेष परिणाम या इलाज का वादा या गारंटी नहीं है, और अनुभव व्यक्ति-व्यक्ति में अलग होते हैं।"),
            ("I understand that imagery from regression may be experienced as memory, symbol or imagination, and its meaning is mine to interpret.", "मैं समझता/समझती हूँ कि रिग्रेशन के दृश्य स्मृति, प्रतीक या कल्पना हो सकते हैं, और उनका अर्थ मैं स्वयं समझूँगा/समझूँगी।"),
            ("I remain aware and in control, and may stop the session at any time.", "मैं जागरूक और नियंत्रण में रहूँगा/रहूँगी, और कभी भी सत्र रोक सकता/सकती हूँ।"),
            ("I have answered the health questions honestly and will inform the therapist of any changes.", "मैंने स्वास्थ्य संबंधी प्रश्नों के उत्तर ईमानदारी से दिए हैं और किसी भी बदलाव की सूचना दूँगा/दूँगी।"),
            ("I consent to online sessions being held privately; sessions are not recorded without my written permission.", "मैं ऑनलाइन सत्रों के लिए सहमत हूँ; मेरी लिखित अनुमति के बिना सत्र रिकॉर्ड नहीं किए जाएँगे।")]
    body = f"""
<section class="pg">{hd}
<h1>Client Intake &amp; Consent Form<small>क्लाइंट विवरण एवं सहमति पत्र</small></h1>
<div class="intro">Please complete this form before your first session. Everything you share is kept strictly confidential. &nbsp;<span style="font-family:'Noto Sans Devanagari'">कृपया पहले सत्र से पहले यह फ़ॉर्म भरें। आपकी हर जानकारी पूर्णतः गोपनीय रखी जाएगी।</span></div>
<h3>Your details <span>आपका विवरण</span></h3>
<div class="f f3">{fld("Full name", "पूरा नाम")}{fld("Date of birth", "जन्म तिथि")}{fld("Gender", "लिंग")}</div>
<div class="f f2" style="margin-top:3mm">{fld("Phone / WhatsApp", "फ़ोन / WhatsApp")}{fld("Email", "ईमेल")}</div>
<div class="f f2" style="margin-top:3mm">{fld("City", "शहर")}{fld("Occupation", "व्यवसाय")}</div>
<div class="f f2" style="margin-top:3mm">{fld("Emergency contact (name &amp; phone)", "आपातकालीन संपर्क")}{fld("Session mode: Online / In person", "सत्र: ऑनलाइन / आमने-सामने")}</div>
<h3>What brings you here <span>आप क्यों आए हैं</span></h3>
<div class="fld">What would you like support with? <i>/ आप किस विषय में सहयोग चाहते हैं?</i><div class="box"></div></div>
<div class="fld" style="margin-top:3mm">How long has this been affecting you, and what have you tried so far? <i>/ यह कब से है, और अब तक क्या प्रयास किए?</i><div class="box" style="height:14mm"></div></div>
<h3>Health check <span>स्वास्थ्य जानकारी</span></h3>
<div class="qs">{"".join(q(a, b) for a, b in med)}</div>
{ft.replace("PAGE", "1")}</section>

<section class="pg">{hd}
<div class="fld" style="margin-top:5mm">What would a good outcome look like for you? <i>/ आपके लिए अच्छा परिणाम क्या होगा?</i><div class="box" style="height:16mm"></div></div>
<div class="fld" style="margin-top:4mm">If you answered “Yes” to any health question, please give details (condition, doctor, medicines): <i>/ यदि किसी प्रश्न का उत्तर “हाँ” है, तो विवरण दें:</i><div class="box" style="height:18mm"></div></div>
<div class="conf"><b>Please note:</b> If you are under psychiatric care, or have epilepsy, psychosis or a serious heart condition, sessions may need your doctor’s approval first. This is for your safety. &nbsp;<span style="font-family:'Noto Sans Devanagari'">यदि आप मनोचिकित्सा उपचार में हैं, या आपको मिर्गी, साइकोसिस या गंभीर हृदय रोग है, तो पहले डॉक्टर की अनुमति आवश्यक हो सकती है। यह आपकी सुरक्षा के लिए है।</span></div>
<h3>Consent <span>सहमति</span></h3>
<ul class="cons">{"".join(f"<li><div>{a}<i>{b}</i></div></li>" for a, b in cons)}</ul>
<h3>Confidentiality <span>गोपनीयता</span></h3>
<div class="intro" style="font-size:9.6px">Everything shared in sessions is kept confidential. The only exception is if there is a serious risk of harm to you or someone else, when appropriate help may need to be contacted. <span style="font-family:'Noto Sans Devanagari'">सत्र में साझा की गई हर बात गोपनीय रहती है। केवल तब अपवाद होगा जब आपको या किसी अन्य को गंभीर हानि का खतरा हो।</span></div>
<div class="sig">{fld("Client signature", "हस्ताक्षर")}{fld("Name", "नाम")}{fld("Date", "दिनांक")}</div>
<div class="sig" style="margin-top:6mm">{fld("Therapist: Dhiraj Sarda", "थेरेपिस्ट")}{fld("Signature", "हस्ताक्षर")}{fld("Date", "दिनांक")}</div>
<h3 style="margin-top:6mm">For therapist use <span>केवल थेरेपिस्ट हेतु</span></h3>
<div class="f f3">{fld("Session no.", "सत्र क्र.")}{fld("Technique used", "तकनीक")}{fld("Follow-up", "अगला सत्र")}</div>
<div class="fld" style="margin-top:3mm">Notes <i>/ टिप्पणी</i><div class="box" style="height:13mm"></div></div>
{ft.replace("PAGE", "2")}</section>"""
    return page("Client Intake & Consent Form", "en", FORM_CSS, body)


def letterhead():
    css = """@page{size:210mm 297mm;margin:0}
body{background:#fff;color:var(--ink)}
.pg{width:210mm;height:297mm;position:relative;overflow:hidden}
.hd{height:34mm;padding:0 18mm;display:flex;align-items:center;gap:14px;border-bottom:1.5px solid var(--gold)}
.hd img{width:17mm}
.hd b{font-family:'Cormorant Garamond',serif;font-size:27px;letter-spacing:.15em;display:block;line-height:1}
.hd span{font-size:8.6px;color:var(--golddk);letter-spacing:.2em}
.hd .devo{margin-left:auto;font-size:12px;color:var(--golddk)}
.wm{position:absolute;width:150mm;left:30mm;top:85mm;opacity:.06}
.ft{position:absolute;left:0;right:0;bottom:0;height:20mm;background:var(--ink);color:var(--ivory);display:flex;align-items:center;justify-content:center;gap:10mm;font-size:10px;letter-spacing:.12em;border-top:2px solid var(--gold)}
.ft span{display:flex;align-items:center;gap:6px}"""
    c = T["en"]
    body = f"""<section class="pg"><div class="hd"><img src="{MARK_INK}" alt=""><div><b>DHIRAJ SARDA</b><span>{c['title'].upper()}</span></div><div class="devo tiro">{c['devotion']}</div></div>
<img class="wm" src="{MANDALA_DK}" alt="">
<div class="ft caps"><span>{wa_icon(16)} {PHONE_DISPLAY}</span><span style="text-transform:none;letter-spacing:.06em">{EMAIL}</span><span>{c['loc']}</span></div></section>"""
    return page("Letterhead", "en", css, body)


# =====================================================================
# BRAND GUIDELINES SHEET  1600 wide
# =====================================================================
def brand_sheet():
    e, h = T["en"], T["hi"]
    css = """body{width:1600px;background:var(--ivory) ;color:var(--ink);font-family:'Jost',sans-serif}
@page{size:1600px 3140px;margin:0}
.w{padding:70px 80px 60px;height:3140px;position:relative;overflow:hidden}
h1{font-family:'Cormorant Garamond',serif;font-size:56px;font-weight:600}
.lead{font-size:18px;color:#4a4f75;margin-top:6px;max-width:1100px;line-height:1.6}
h2{font-family:'Cormorant Garamond',serif;font-size:34px;font-weight:600;margin:46px 0 18px;display:flex;align-items:center;gap:20px}
h2:after{content:"";flex:1;height:1px;background:var(--gold)}
.g{display:grid;gap:20px}
.t{border-radius:16px;overflow:hidden;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:30px}
.t.d{background:radial-gradient(ellipse at 50% 20%,#283080,#151b55 45%,#0E1233 85%);color:var(--ivory)}
.t.l{background:#fff;border:1px solid #e6dcc0}
.t .n{font-family:'Cormorant Garamond',serif;font-size:44px;font-weight:600;letter-spacing:.14em;margin-top:16px;line-height:1.1}
.t .n.hi{font-family:'Noto Serif Devanagari',serif;letter-spacing:0;font-size:46px;line-height:1.4}
.t .s{font-size:13px;letter-spacing:.24em;color:var(--goldlt);margin-top:12px;text-transform:uppercase}
.t.l .s{color:var(--golddk)}
.t .s.hi{letter-spacing:0;text-transform:none;font-size:18px}
.sw{height:150px;border-radius:14px;padding:16px;display:flex;flex-direction:column;justify-content:flex-end;font-size:14px;line-height:1.4}
.ty{background:#fff;border:1px solid #e6dcc0;border-radius:14px;padding:24px}
.ty small{font-size:11px;letter-spacing:.24em;color:var(--golddk);text-transform:uppercase}
.ty div{margin-top:10px}
.ic{background:var(--ink);border-radius:14px;padding:22px 10px;text-align:center;color:var(--goldlt);font-size:13px}
.ic svg{display:block;margin:0 auto 10px}
.say{background:#fff;border:1px solid #e6dcc0;border-radius:14px;padding:26px 30px;font-size:16px;line-height:1.85}
.say h4{font-family:'Cormorant Garamond',serif;font-size:26px;margin-bottom:8px}
.say.ok{border-top:5px solid #3c8c5a}.say.no{border-top:5px solid #b4483c}
.say s{color:#b4483c}
.note{font-size:15px;color:#4a4f75;line-height:1.7;margin-top:14px}
.ph{border-radius:14px;overflow:hidden;height:330px;position:relative}
.ph img{width:100%;height:100%;object-fit:cover;object-position:50% 20%}
.ph span{position:absolute;left:12px;bottom:12px;background:rgba(14,18,51,.8);color:#fff;font-size:13px;padding:6px 12px;border-radius:999px}"""
    sw = [("#0E1233", "Midnight Indigo", "#0E1233", "#fff"), ("#1A1F4D", "Deep Indigo", "#1A1F4D", "#fff"), ("#C9A24B", "Antique Gold", "#C9A24B", "#0E1233"),
          ("#E6CB8A", "Soft Gold", "#E6CB8A", "#0E1233"), ("#F6EFDD", "Ivory", "#F6EFDD", "#0E1233"), ("#B9BDDA", "Mist", "#B9BDDA", "#0E1233"),
          ("#E38B3A", "Sindoor Saffron · accent only", "#E38B3A", "#fff")]
    sws = "".join(f'<div class="sw" style="background:{b};color:{fg};{"border:1px solid #e6dcc0;" if b == "#F6EFDD" else ""}"><b>{n}</b>{x}</div>' for b, n, x, fg in sw)
    ics = "".join(f'<div class="ic">{icon_c(k, "#E6CB8A", 56, 1.8)}{k}</div>' for k in ("plr", "hypno", "child", "age", "womb", "med", "mind", "body", "heart", "soul"))
    body = f"""<div class="w">
<h1>Dhiraj Sarda — Brand Guidelines</h1>
<div class="lead">Midnight indigo for depth and calm, antique gold for the sacred, ivory for warmth — with a single touch of sindoor saffron that quietly honours Hanuman ji. Calm, premium and trustworthy: never loud, never “miracle”.</div>
<h2>Logo lock-ups</h2>
<div class="g" style="grid-template-columns:1fr 1fr">
<div class="t d" style="height:360px"><img src="{MARK}" style="width:150px"><div class="n">{e['name']}</div><div class="s">{e['title']}</div></div>
<div class="t l" style="height:360px"><img src="{MARK_INK}" style="width:150px"><div class="n">{e['name']}</div><div class="s">{e['title']}</div></div>
<div class="t d" style="height:300px"><img src="{MARK}" style="width:120px"><div class="n hi">{h['name']}</div><div class="s hi">{h['title']}</div></div>
<div class="t d" style="height:300px;flex-direction:row;gap:30px"><img src="{MARK}" style="width:150px"><div style="text-align:left"><div class="n" style="margin:0">{e['name']}</div><div class="s">{e['title_short']}</div></div></div>
</div>
<div class="note">The mark is a lotus whose centre turns into a spiral: the journey inward. The saffron <b>bindu</b> above it is the brand’s quiet devotion. Keep clear space of half the mark’s width around it. Never stretch, recolour or add effects.</div>
<h2>Emblems &amp; pattern</h2>
<div class="g" style="grid-template-columns:1fr 1fr 1fr">
<div class="t d" style="height:330px"><div style="width:240px;height:240px">{ram_heart()}</div><div class="s">Ram in the heart · inspiration</div></div>
<div class="t d" style="height:330px"><img src="{MANDALA}" style="width:260px;opacity:.8"><div class="s">Mandala · backgrounds at 6–16%</div></div>
<div class="t d" style="height:330px"><div class="tiro" style="font-size:40px;color:var(--goldlt)">{e['devotion']}</div><div class="s" style="margin-top:24px">Devotion line · top of covers</div></div>
</div>
<h2>Palette</h2><div class="g" style="grid-template-columns:repeat(7,1fr)">{sws}</div>
<h2>Typography</h2>
<div class="g" style="grid-template-columns:repeat(4,1fr)">
<div class="ty"><small>Display</small><div class="serif" style="font-size:44px">Cormorant Garamond</div></div>
<div class="ty"><small>Body</small><div style="font-size:30px">Jost — clean and calm</div></div>
<div class="ty"><small>Hindi</small><div style="font-family:'Noto Serif Devanagari';font-size:32px">नोटो सेरिफ़ देवनागरी</div></div>
<div class="ty"><small>Verse / devotional</small><div class="tiro" style="font-size:32px">तिरो देवनागरी</div></div>
</div>
<h2>Icons</h2><div class="g" style="grid-template-columns:repeat(10,1fr)">{ics}</div>
<h2>Photography</h2>
<div class="g" style="grid-template-columns:1fr 1fr 1fr 1fr">
<div class="ph"><img src="{P_FORMAL}"><span>Formal — covers, DP, posters</span></div>
<div class="ph"><img src="{P_WARM}"><span>Warm — about, intro posts</span></div>
<div class="ph" style="background:#0E1233"><img src="{HANUMAN}"><span>Dhyan Hanuman — inspiration posts</span></div>
<div class="say" style="font-size:15px;line-height:1.7"><h4>Photo rules</h4>Natural skin, real face — no heavy beautify filters. Indigo or ivory backgrounds. Eyes sharp, calm expression. Always inside an arch or circle frame with the gold double line.</div>
</div>
<h2>Words we use</h2>
<div class="g" style="grid-template-columns:1fr 1fr">
<div class="say ok"><h4>Say</h4>“Support for migraine &amp; chronic pain”<br>“Sugar (diabetes): stress &amp; cravings support”<br>“Depression &amp; low mood support”<br>“May help”, “can support”, “alongside your doctor’s care”<br>“Certified Therapist · IPHM (UK) accredited training”<br>“Inner child healing”, “release”, “remember your strength”</div>
<div class="say no"><h4>Avoid</h4><s>“Cure diabetes / sugar healing”</s> — diabetes is on the Drugs &amp; Magic Remedies Act schedule<br><s>“Guaranteed”, “100% result”, “permanent relief”</s><br><s>“Stop your medicines”</s> or anything implying it<br><s>“Dr.”</s> — not a medical title for this practice<br><s>Before/after health claims or testimonials as proof</s><br>Every piece that names a health condition carries the “alongside your doctor” line.</div>
</div>
</div>"""
    return page("Brand Guidelines", "en", css, body)


def build_all():
    for lg, c in T.items():
        write(f"trifold-{lg}.html", trifold(c))
        write(f"card-{lg}.html", card(c))
        write(f"flyer-{lg}.html", flyer(c))
        write(f"story-{lg}.html", story(c))
        for k in ("intro", "child", "body", "remember"):
            write(f"post-{k}-{lg}.html", post(c, k))
        for k in ("portrait", "warm", "logo"):
            write(f"dp-{k}-{lg}.html", dp(c, k))
    write("card-mockup.html", card_mockup())
    for k in ("sessions", "inner-child", "healing", "about", "inspiration", "book"):
        write(f"hl-{k}.html", highlight(k))
    for k in ("facebook", "linkedin", "youtube"):
        write(f"cover-{k}.html", cover(k))
    write("intake-form.html", intake())
    write("letterhead.html", letterhead())
    write("brand-sheet.html", brand_sheet())
    print("built pieces")
