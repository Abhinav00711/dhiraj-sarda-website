"""Generates the website (G:/DhirajSarda/Website) from content.py: index.html (English baked in for SEO),
assets/js/i18n.js (EN + HI strings), optimised images, favicons. CSS/JS behaviour live in Website/assets/ (hand-written).
Run: python site.py"""
import json, pathlib, shutil, html as H
from PIL import Image
from content import T, PHONE_DISPLAY, PHONE_LINK, EMAIL
from assets import mark, mandala, ram_heart, ICON_BODIES, icon, WA, wa_url, qr_svg

ROOT = pathlib.Path(__file__).parent
SITE = ROOT.parent / "Website"
IMG = SITE / "assets" / "img"
IMG.mkdir(parents=True, exist_ok=True)

# ---------- website-only strings ----------
W = {
 "en": dict(
  nav_about="About", nav_ther="Therapies", nav_heal="Healing", nav_breathe="Breathe", nav_journey="Journey", nav_insp="Inspiration", nav_contact="Contact",
  book="Book a session", cta2="Breathe with me", scroll="Scroll", sound="Calm sound",
  br_k="A moment for you", br_h="Breathe with me",
  br_p="Before anything else, let your body settle. Follow the lotus &mdash; breathe in as it opens, hold gently, and breathe out slowly as it closes.",
  br_in="Breathe in", br_hold="Hold", br_out="Breathe out", br_start="Begin", br_stop="Pause", br_count="breaths", br_tip="Tip: turn on the calm sound for a soft tanpura drone.",
  wheel_hint="Tap a circle to explore",
  f_name="Your name", f_concern="What would you like support with?", f_mode="Session", f_online="Online (video call)", f_person="In person, Delhi",
  f_time="Preferred day / time", f_msg="Anything you&rsquo;d like to share (optional)", f_send="Send on WhatsApp", f_other="Something else",
  f_priv="Your message opens in WhatsApp &mdash; nothing is stored on this website.", f_or="Or message directly",
  wa_hello="Namaste Dhiraj ji", wa_name="Name", wa_concern="Support with", wa_mode="Session", wa_time="Preferred time", wa_note="Note",
  rights="All rights reserved.", top="Back to top", lang_btn="हिं",
  meta_title="Dhiraj Sarda — Past Life Regression Therapist & Hypnotherapist, Delhi & Online",
  meta_desc="Certified Past Life Regression Therapist & Transpersonal Hypnotherapist in Delhi and online. Inner child healing, age & womb regression, and gentle support for stress, depression, migraine, pain and habits.",
 ),
 "hi": dict(
  nav_about="परिचय", nav_ther="थेरेपी", nav_heal="उपचार", nav_breathe="श्वास", nav_journey="यात्रा", nav_insp="प्रेरणा", nav_contact="संपर्क",
  book="सत्र बुक करें", cta2="मेरे साथ साँस लें", scroll="नीचे देखें", sound="शांत ध्वनि",
  br_k="आपके लिए एक पल", br_h="मेरे साथ साँस लें",
  br_p="सबसे पहले, शरीर को शांत होने दें। कमल के साथ चलें &mdash; खिलते समय साँस लें, थोड़ा रुकें, और बंद होते समय धीरे-धीरे साँस छोड़ें।",
  br_in="साँस लें", br_hold="रुकें", br_out="साँस छोड़ें", br_start="शुरू करें", br_stop="विराम", br_count="साँसें", br_tip="सुझाव: तानपूरे की कोमल ध्वनि के लिए ‘शांत ध्वनि’ चालू करें।",
  wheel_hint="देखने के लिए किसी वृत्त पर टैप करें",
  f_name="आपका नाम", f_concern="आप किस विषय में सहयोग चाहते हैं?", f_mode="सत्र", f_online="ऑनलाइन (वीडियो कॉल)", f_person="आमने-सामने, दिल्ली",
  f_time="पसंदीदा दिन / समय", f_msg="कुछ और बताना चाहें (वैकल्पिक)", f_send="WhatsApp पर भेजें", f_other="कुछ और",
  f_priv="आपका संदेश WhatsApp में खुलेगा &mdash; इस वेबसाइट पर कुछ भी सेव नहीं होता।", f_or="या सीधे संदेश भेजें",
  wa_hello="नमस्ते धीरज जी", wa_name="नाम", wa_concern="सहयोग चाहिए", wa_mode="सत्र", wa_time="पसंदीदा समय", wa_note="टिप्पणी",
  rights="सर्वाधिकार सुरक्षित।", top="ऊपर जाएँ", lang_btn="EN",
  meta_title="धीरज सारड़ा — पास्ट लाइफ रिग्रेशन थेरेपिस्ट एवं हिप्नोथेरेपिस्ट, दिल्ली व ऑनलाइन",
  meta_desc="दिल्ली व ऑनलाइन प्रमाणित पास्ट लाइफ रिग्रेशन थेरेपिस्ट एवं ट्रांसपर्सनल हिप्नोथेरेपिस्ट।",
 ),
}

# ---------- flatten copy into keyed strings ----------
def flat(lang):
    c, w = T[lang], W[lang]
    d = {}
    for k in ("name", "name_title", "title", "title_2l", "title_short", "cred_short", "loc", "loc_short", "tagline", "tagline2",
              "about_k", "about_h", "about_p1", "about_p2", "about_p3", "meet", "meet_p", "serv_k", "serv_h", "areas_k", "areas_h",
              "body_note", "areas_cta", "journey_k", "journey_h", "inspo_k", "inspo_h", "inspo_p", "verse_tr", "verse_src", "sankat",
              "quote", "cred_k", "cred_h", "cred_p", "cert_cap", "seal_k", "seal_t", "seal_h", "seal_by", "seal_meta", "faq_h", "cta_k", "cta_h", "cta_p", "wa_cta", "scan", "disc", "values"):
        d[k] = c[k]
    for i, (a, b) in enumerate(c["pil"]): d[f"pil{i}t"], d[f"pil{i}d"] = a, b
    for i, (k, t, desc) in enumerate(c["serv"]): d[f"sv{i}t"], d[f"sv{i}d"] = t, desc
    for i, (k, t, s, items) in enumerate(c["areas"]):
        d[f"ar{i}t"], d[f"ar{i}s"] = t, s
        d[f"ar{i}l"] = "".join(f"<li>{x}</li>" for x in items)
    for i, (t, desc) in enumerate(c["steps"]): d[f"st{i}t"], d[f"st{i}d"] = t, desc
    for i, (t, desc) in enumerate(c["formats"]): d[f"fm{i}t"], d[f"fm{i}d"] = t, desc
    for i, x in enumerate(c["cred_list"]): d[f"cl{i}"] = x
    for i, (q, a) in enumerate(c["faq"]): d[f"fq{i}q"], d[f"fq{i}a"] = q, a
    d.update(w)
    # concern options for the booking form
    d["opts"] = [x for _, _, _, items in c["areas"] for x in items] + [w["f_other"]]
    d["marquee"] = [x for _, _, _, items in c["areas"] for x in items[:3]] + [s[1] for s in c["serv"]]
    return d

EN, HI = flat("en"), flat("hi")


def t(k, tag="span", cls="", attrs=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-k="{k}"{attrs}>{EN[k]}</{tag}>'


def ic(k, size=44, sw=1.8, color="currentColor"):
    return icon(ICON_BODIES[k], color, size, sw).replace("<svg ", '<svg aria-hidden="true" ')


# ---------- images ----------
def img(src, name, w, q=82):
    im = Image.open(src).convert("RGB")
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    im.save(IMG / f"{name}.webp", "WEBP", quality=q, method=6)
    return im.size

sz_formal = img(ROOT / "art" / "portrait-formal.jpg", "portrait-formal", 900)
sz_warm = img(ROOT / "art" / "portrait-warm.jpg", "portrait-warm", 800)
img(ROOT / "art" / "bg-poster.jpg", "lotus-glow", 1100, 78)
img(ROOT / "art" / "hanuman-dhyan.jpg", "hanuman-dhyan", 900, 80)
for old in ("certificate", "certificate-thumb"):  # certificate shows the trainer's name: not published
    (IMG / f"{old}.webp").unlink(missing_ok=True)
(IMG / "mark.svg").write_text(mark(), encoding="utf-8")
(IMG / "mandala.svg").write_text(mandala(sw=1.2), encoding="utf-8")
# favicons
fav = mark().replace('stroke-width="2.2"', 'stroke-width="5"').replace('stroke-width="2.4"', 'stroke-width="6"').replace('stroke-width="2.6"', 'stroke-width="6"')
fav = fav.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"><rect width="200" height="200" rx="44" fill="#0E1233"/><g transform="translate(14 14) scale(.86)"', 1).replace("</svg>", "</g></svg>")
(IMG / "favicon.svg").write_text(fav, encoding="utf-8")
og = ROOT / "out" / "4-Social" / "Cover-Facebook.png"
if og.exists():
    Image.open(og).convert("RGB").resize((1200, 457)).crop((0, 0, 1200, 457)).save(IMG / "og-wide.jpg", quality=86)
dp = ROOT / "out" / "5-Profile-Pictures" / "DP-Logo-EN.png"
if dp.exists():
    im = Image.open(dp).convert("RGB")
    im.resize((180, 180), Image.LANCZOS).save(IMG / "apple-touch-icon.png")
    im.resize((512, 512), Image.LANCZOS).save(IMG / "icon-512.png")
fl = ROOT / "out" / "4-Social" / "Flyer-EN.png"
og_src = ROOT / "html" / "og.html"

# ---------- page ----------
c = T["en"]
serv_cards = "".join(
    f'<article class="card tilt{" feat" if k == "child" else ""}" data-r style="--d:{i*70}ms"><div class="card-ic">{ic(k, 46, 1.7)}</div>'
    f'{t(f"sv{i}t", "h3", "serif")}{t(f"sv{i}d", "p")}<span class="card-glow"></span></article>' for i, (k, _, _) in enumerate(c["serv"]))
wheel_nodes = "".join(
    f'<button class="node n{i}{" on" if i == 0 else ""}" data-i="{i}" aria-label="{a[1]}"><span class="node-ic">{ic(a[0], 34, 1.9)}</span>{t(f"ar{i}t", "span", "serif")}</button>'
    for i, a in enumerate(c["areas"]))
wheel_panels = "".join(
    f'<div class="wp{" on" if i == 0 else ""}" data-i="{i}"><div class="wp-h">{ic(a[0], 40, 1.8)}<div>{t(f"ar{i}t", "h3", "serif")}{t(f"ar{i}s", "p", "sub serif")}</div></div>'
    f'<ul class="chk" data-k="ar{i}l">{EN[f"ar{i}l"]}</ul></div>' for i, a in enumerate(c["areas"]))
steps = "".join(f'<li class="step" data-r style="--d:{i*140}ms"><span class="step-n serif">{i+1}</span>{t(f"st{i}t", "h3", "serif")}{t(f"st{i}d", "p")}</li>' for i in range(4))
fmts = "".join(f'<div data-r style="--d:{i*90}ms">{t(f"fm{i}t", "h4", "serif")}{t(f"fm{i}d", "p")}</div>' for i in range(3))
pils = "".join(f'<div data-r style="--d:{i*90}ms">{t(f"pil{i}t", "h4", "serif")}{t(f"pil{i}d", "p")}</div>' for i in range(3))
creds = "".join(f'<li>{t(f"cl{i}")}</li>' for i in range(4))
faqs = "".join(f'<details class="fq" data-r style="--d:{i*70}ms"><summary>{t(f"fq{i}q", "span", "serif")}<i></i></summary>{t(f"fq{i}a", "p")}</details>' for i in range(4))
marq = "".join(f'<span>{x}</span><b>✦</b>' for x in EN["marquee"])
opts = "".join(f'<option>{x}</option>' for x in EN["opts"])
petals = "".join(f'<path class="pt" style="--a:{a}deg" d="M100 100 C 84 80, 86 46, 100 24 C 114 46, 116 80, 100 100 Z"/>' for a in range(0, 360, 45))
petals2 = "".join(f'<path class="pt2" style="--a:{a}deg" d="M100 100 C 88 84, 90 58, 100 42 C 110 58, 112 84, 100 100 Z"/>' for a in range(22, 360, 45))

jsonld = {
    "@context": "https://schema.org", "@type": "ProfessionalService", "name": "Dhiraj Sarda — Past Life Regression & Hypnotherapy",
    "description": W["en"]["meta_desc"], "telephone": PHONE_DISPLAY, "email": EMAIL, "areaServed": ["Delhi", "Online"],
    "founder": {"@type": "Person", "name": "Dhiraj Sarda", "jobTitle": "Past Life Regression Therapist & Transpersonal Hypnotherapist",
                "hasCredential": "Past Life Regression, Transpersonal Hypnotherapy, Age & Womb Regression Diploma (IPHM UK accredited)"},
    "knowsAbout": ["Past Life Regression", "Hypnotherapy", "Inner Child Healing", "Age Regression", "Womb Regression", "Guided Meditation"],
}

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{H.escape(W['en']['meta_title'])}</title>
<meta name="description" content="{H.escape(W['en']['meta_desc'])}">
<meta name="theme-color" content="#0E1233">
<meta property="og:type" content="website">
<meta property="og:title" content="{H.escape(W['en']['meta_title'])}">
<meta property="og:description" content="{H.escape(W['en']['meta_desc'])}">
<meta property="og:image" content="assets/img/og-wide.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Jost:wght@300;400;500;600&family=Noto+Serif+Devanagari:wght@500;600;700&family=Noto+Sans+Devanagari:wght@400;500;600&family=Tiro+Devanagari+Hindi&display=swap" rel="stylesheet">
<link rel="preload" as="image" href="assets/img/portrait-formal.webp">
<link rel="stylesheet" href="assets/css/style.css">
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
</head>
<body>
<div class="loader" aria-hidden="true"><div class="ld-mark">{mark()}</div></div>
<a class="skip" href="#about">Skip to content</a>

<header class="nav" id="nav">
  <a class="brand" href="#top" aria-label="Dhiraj Sarda — home"><img src="assets/img/mark.svg" alt="" width="40" height="40"><span><b data-k="name">{EN['name']}</b><small data-k="title_short">{EN['title_short']}</small></span></a>
  <nav class="links" aria-label="Main">
    <a href="#about" data-k="nav_about">{EN['nav_about']}</a><a href="#therapies" data-k="nav_ther">{EN['nav_ther']}</a><a href="#healing" data-k="nav_heal">{EN['nav_heal']}</a>
    <a href="#breathe" data-k="nav_breathe">{EN['nav_breathe']}</a><a href="#journey" data-k="nav_journey">{EN['nav_journey']}</a><a href="#inspiration" data-k="nav_insp">{EN['nav_insp']}</a><a href="#contact" data-k="nav_contact">{EN['nav_contact']}</a>
  </nav>
  <div class="tools">
    <button class="snd" id="snd" aria-pressed="false" title="Calm sound"><span class="bars"><i></i><i></i><i></i><i></i></span><span data-k="sound">{EN['sound']}</span></button>
    <button class="lang" id="lang" aria-label="Switch language" data-k="lang_btn">{EN['lang_btn']}</button>
    <a class="btn sm gold" href="#contact" data-k="book">{EN['book']}</a>
    <button class="burger" id="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
  </div>
</header>

<main id="top">
<section class="hero dark" id="hero">
  <canvas class="sky" aria-hidden="true"></canvas>
  <div class="aurora" aria-hidden="true"><i></i><i></i><i></i></div>
  <div class="hero-in">
    <div class="hero-text">
      <p class="devo tiro" data-intro>॥ श्री हनुमते नमः ॥</p>
      <p class="kicker" data-intro style="--d:.15s" data-k="cred_short">{EN['cred_short']}</p>
      <h1 class="serif split" data-k="name">{EN['name']}</h1>
      <div class="rule" data-intro style="--d:1s"></div>
      <p class="caps title" data-intro style="--d:1.1s" data-k="title_2l">{EN['title_2l']}</p>
      <p class="tagline serif" data-intro style="--d:1.25s"><span data-k="tagline">{EN['tagline']}</span> <em data-k="tagline2">{EN['tagline2']}</em></p>
      <div class="hero-cta" data-intro style="--d:1.4s">
        <a class="btn gold" href="{wa_url('en')}" target="_blank" rel="noopener" data-wa>{WA.replace('width="30" height="30"','width="22" height="22"')}<span data-k="book">{EN['book']}</span></a>
        <a class="btn ghost" href="#breathe"><span class="pulse-dot"></span><span data-k="cta2">{EN['cta2']}</span></a>
      </div>
      <p class="loc caps" data-intro style="--d:1.55s" data-k="loc">{EN['loc']}</p>
    </div>
    <div class="hero-art" data-intro style="--d:.3s">
      <img class="mandala spin" src="assets/img/mandala.svg" alt="" aria-hidden="true">
      <div class="halo" aria-hidden="true"></div>
      <div class="arch par" data-depth="10"><img src="assets/img/portrait-formal.webp" alt="Dhiraj Sarda, Past Life Regression Therapist" width="{sz_formal[0]}" height="{sz_formal[1]}" fetchpriority="high"></div>
      <div class="orbit" aria-hidden="true"><i></i><i></i><i></i></div>
    </div>
  </div>
  <a class="scroll" href="#about" aria-label="Scroll"><span data-k="scroll">{EN['scroll']}</span><i></i></a>
</section>

<div class="marquee" aria-hidden="true"><div class="mq-track" id="mq">{marq}{marq}</div></div>

<section class="about light" id="about">
  <div class="wrap two">
    <div>
      <p class="kicker" data-r data-k="about_k">{EN['about_k']}</p>
      <h2 class="serif" data-r data-k="about_h">{EN['about_h']}</h2>
      <div class="rule l" data-r></div>
      <p data-r data-k="about_p1">{EN['about_p1']}</p>
      <p data-r data-k="about_p2">{EN['about_p2']}</p>
      <p data-r class="strong" data-k="about_p3">{EN['about_p3']}</p>
    </div>
    <figure class="about-ph" data-r>
      <div class="arch light-arch par" data-depth="6"><img src="assets/img/portrait-warm.webp" alt="Dhiraj Sarda smiling" loading="lazy" width="{sz_warm[0]}" height="{sz_warm[1]}"></div>
      <figcaption class="serif" data-k="name_title">{EN['name_title']}</figcaption>
    </figure>
  </div>
  <div class="wrap">
    <div class="meet dark" data-r>
      <img class="mandala" src="assets/img/mandala.svg" alt="" aria-hidden="true">
      <div>{t("meet", "h3", "serif")}{t("meet_p", "p")}</div>
      <ul class="chk">{creds}</ul>
    </div>
    <blockquote class="quote serif" data-r><img src="assets/img/mark.svg" alt="" width="46" height="46">{t("quote")}</blockquote>
    <div class="pils">{pils}</div>
  </div>
</section>

<section class="therapies dark" id="therapies">
  <img class="mandala bgm" src="assets/img/mandala.svg" alt="" aria-hidden="true">
  <div class="wrap">
    <div class="head c">{t("serv_k", "p", "kicker c")}{t("serv_h", "h2", "serif")}<div class="rule"></div></div>
    <div class="cards">{serv_cards}</div>
    <div class="fmts">{fmts}</div>
  </div>
</section>

<section class="healing light" id="healing">
  <div class="wrap">
    <div class="head c">{t("areas_k", "p", "kicker c")}{t("areas_h", "h2", "serif")}<div class="rule"></div>{t("wheel_hint", "p", "hint")}</div>
    <div class="wheel-wrap">
      <div class="wheel" data-r>
        <div class="w-ring r1"></div><div class="w-ring r2"></div>
        <img class="w-mand" src="assets/img/mandala.svg" alt="" aria-hidden="true">
        <div class="w-core"><img src="assets/img/mark.svg" alt="" width="70" height="70"></div>
        {wheel_nodes}
      </div>
      <div class="w-panels" data-r>{wheel_panels}</div>
    </div>
    <div class="note" data-r>{ic("body", 38, 1.8)}{t("body_note", "p")}</div>
    <p class="areas-cta serif" data-r><span data-k="areas_cta">{EN['areas_cta']}</span></p>
  </div>
</section>

<section class="breathe dark" id="breathe">
  <canvas class="sky" aria-hidden="true"></canvas>
  <div class="wrap two">
    <div class="br-text">
      {t("br_k", "p", "kicker")}{t("br_h", "h2", "serif")}<div class="rule l"></div>{t("br_p", "p")}
      <div class="br-ctl"><button class="btn gold" id="brBtn"><span data-k="br_start">{EN['br_start']}</span></button>
      <span class="br-count"><b id="brN">0</b> <span data-k="br_count">{EN['br_count']}</span></span></div>
      {t("br_tip", "p", "tip")}
    </div>
    <div class="lotus-wrap">
      <div class="br-glow"></div>
      <svg class="lotus" id="lotus" viewBox="0 0 200 200" aria-hidden="true">{petals2}{petals}<circle cx="100" cy="100" r="9" class="seed"/></svg>
      <div class="br-label serif" id="brLabel" aria-live="polite">&nbsp;</div>
      <svg class="br-ring" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="48"/><circle id="brProg" cx="50" cy="50" r="48" pathLength="1"/></svg>
    </div>
  </div>
</section>

<section class="journey light" id="journey">
  <div class="wrap">
    <div class="head c">{t("journey_k", "p", "kicker c")}{t("journey_h", "h2", "serif")}<div class="rule"></div></div>
    <ol class="steps" id="steps"><span class="line" aria-hidden="true"><i></i></span>{steps}</ol>
  </div>
</section>

<section class="inspo dark" id="inspiration">
  <canvas class="sky" aria-hidden="true" data-embers="saffron"></canvas>
  <div class="wrap two">
    <div class="em-wrap" data-r><img class="han" src="assets/img/hanuman-dhyan.webp" alt="Hanuman ji seated in meditation on a lotus" loading="lazy" width="900" height="900"></div>
    <div>
      {t("inspo_k", "p", "kicker")}{t("inspo_h", "h2", "serif")}<div class="rule l"></div>{t("inspo_p", "p", "lead")}
      <div class="verse"><p class="v tiro" id="verse">{T['en']['verse']}</p>{t("verse_tr", "p", "tr serif")}{t("verse_src", "p", "src caps")}</div>
      {t("sankat", "p", "sankat")}
    </div>
  </div>
</section>

<section class="creds light" id="credentials">
  <div class="wrap two">
    <div class="seal" data-r><img class="wm" src="assets/img/mandala.svg" alt="" aria-hidden="true"><img class="mk" src="assets/img/mark.svg" alt="" width="72" height="72">
      {t("seal_k", "p", "sk caps")}{t("name_title", "p", "sn serif")}<div class="rule"></div>
      {t("seal_t", "p", "st serif")}{t("seal_h", "p", "sh")}{t("seal_by", "p", "sb caps")}{t("seal_meta", "p", "sm")}</div>
    <div>
      {t("cred_k", "p", "kicker")}{t("cred_h", "h2", "serif")}<div class="rule l"></div>{t("cred_p", "p")}
      <ul class="chk big">{creds}</ul>{t("cert_cap", "p", "cap")}
      <div class="faq">{t("faq_h", "p", "kicker")}{faqs}</div>
    </div>
  </div>
</section>

<section class="contact dark" id="contact">
  <img class="mandala bgm r" src="assets/img/mandala.svg" alt="" aria-hidden="true">
  <div class="wrap two">
    <div>
      {t("cta_k", "p", "kicker")}{t("cta_h", "h2", "serif")}<div class="rule l"></div>{t("cta_p", "p", "lead")}
      <form class="form" id="form" novalidate>
        <label><span data-k="f_name">{EN['f_name']}</span><input name="name" autocomplete="name" required></label>
        <label><span data-k="f_concern">{EN['f_concern']}</span><select name="concern" id="concern">{opts}</select></label>
        <fieldset><legend data-k="f_mode">{EN['f_mode']}</legend>
          <label class="rad"><input type="radio" name="mode" value="online" checked><span data-k="f_online">{EN['f_online']}</span></label>
          <label class="rad"><input type="radio" name="mode" value="person"><span data-k="f_person">{EN['f_person']}</span></label></fieldset>
        <label><span data-k="f_time">{EN['f_time']}</span><input name="time"></label>
        <label class="full"><span data-k="f_msg">{EN['f_msg']}</span><textarea name="msg" rows="3"></textarea></label>
        <button class="btn gold full" type="submit">{WA.replace('width="30" height="30"','width="22" height="22"')}<span data-k="f_send">{EN['f_send']}</span></button>
        <p class="priv full" data-k="f_priv">{EN['f_priv']}</p>
      </form>
    </div>
    <aside class="direct" data-r>
      <div class="qr">{qr_svg('en')}</div>
      {t("scan", "p", "scan")}
      <p class="or" data-k="f_or">{EN['f_or']}</p>
      <a class="wa-big" href="{wa_url('en')}" target="_blank" rel="noopener" data-wa>{WA.replace('width="30" height="30"','width="28" height="28"')}<span>{PHONE_DISPLAY}</span></a>
      <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
      <p class="loc caps" data-k="loc">{EN['loc']}</p>
    </aside>
  </div>
</section>
</main>

<footer class="foot dark">
  <div class="wrap">
    <img src="assets/img/mark.svg" alt="" width="64" height="64">
    <p class="f-name serif" data-k="name">{EN['name']}</p>
    <p class="caps f-t" data-k="title">{EN['title']}</p>
    <p class="devo tiro">॥ श्री हनुमते नमः ॥</p>
    <p class="disc" data-k="disc">{EN['disc']}</p>
    <p class="copy">© 2026 Dhiraj Sarda. <span data-k="rights">{EN['rights']}</span> · <a href="#top" data-k="top">{EN['top']}</a></p>
  </div>
</footer>

<a class="fab" href="{wa_url('en')}" target="_blank" rel="noopener" aria-label="WhatsApp" data-wa>{WA.replace('width="30" height="30"','width="30" height="30"').replace('fill="#25D366"','fill="#fff"')}</a>

<script>window.I18N={json.dumps({"en": EN, "hi": HI}, ensure_ascii=False)};window.WA_NUM="{PHONE_LINK}";window.VERSE={json.dumps(T['en']['verse'], ensure_ascii=False)};</script>
<script src="assets/js/main.js" defer></script>
</body>
</html>"""
(SITE / "index.html").write_text(page, encoding="utf-8")
print("site built ->", SITE / "index.html")
