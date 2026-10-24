"""Renders Build/html/*.html to PDF/PNG with headless Chrome into Build/out/<group>/.
Usage:  python render.py              (everything)
        python render.py brochure card (only those groups)"""
import subprocess, pathlib, sys
import pymupdf

ROOT = pathlib.Path(__file__).parent
HTML, OUT = ROOT / "html", ROOT / "out"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
COMMON = ["--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files", "--virtual-time-budget=15000"]
LANGS = ("en", "hi")


def _out(group, name):
    d = OUT / group
    d.mkdir(parents=True, exist_ok=True)
    return d / name


def png(src, group, name, w, h, scale=1):
    dst = _out(group, name)
    subprocess.run([CHROME, *COMMON, f"--window-size={w},{h}", f"--force-device-scale-factor={scale}",
                    f"--screenshot={dst}", (HTML / src).resolve().as_uri()], check=True, capture_output=True)
    print("png", dst.relative_to(OUT))


def pdf(src, group, name, previews=0, preview_dpi=110):
    dst = _out(group, name)
    subprocess.run([CHROME, *COMMON, "--no-pdf-header-footer", f"--print-to-pdf={dst}", (HTML / src).resolve().as_uri()],
                   check=True, capture_output=True)
    print("pdf", dst.relative_to(OUT))
    if previews:
        doc = pymupdf.open(dst)
        for i, p in enumerate(doc):
            pv = dst.with_name(f"{dst.stem}-p{i+1}.png")
            p.get_pixmap(dpi=preview_dpi).save(pv)
        print("   +", len(doc), "page previews")


JOBS = {
    "brochure": lambda: [pdf(f"brochure-{l}.html", "1-Brochure", f"Dhiraj-Sarda-Brochure-{l.upper()}.pdf", previews=1, preview_dpi=130) for l in LANGS],
    "trifold": lambda: [pdf(f"trifold-{l}.html", "2-Trifold-Leaflet", f"Dhiraj-Sarda-Trifold-{l.upper()}.pdf", previews=1, preview_dpi=100) for l in LANGS],
    "card": lambda: [pdf(f"card-{l}.html", "3-Visiting-Card", f"Dhiraj-Sarda-Card-{l.upper()}-print.pdf", previews=1, preview_dpi=600) for l in LANGS],
    "mockup": lambda: png("card-mockup.html", "3-Visiting-Card", "Dhiraj-Sarda-Card-Mockup.png", 1600, 1100),
    "flyer": lambda: [png(f"flyer-{l}.html", "4-Social", f"Flyer-{l.upper()}.png", 1240, 1754) for l in LANGS],
    "story": lambda: [png(f"story-{l}.html", "4-Social", f"Story-Poster-{l.upper()}.png", 1080, 1920) for l in LANGS],
    "posts": lambda: [png(f"post-{p}-{l}.html", "4-Social", f"Post-{i}-{p}-{l.upper()}.png", 1080, 1350)
                      for l in LANGS for i, p in enumerate(("intro", "child", "body", "remember"), 1)],
    "dp": lambda: [png(f"dp-{k}-{l}.html", "5-Profile-Pictures", f"DP-{k.title()}-{l.upper()}.png", 1080, 1080)
                   for l in LANGS for k in ("portrait", "logo")] + [png("dp-warm-en.html", "5-Profile-Pictures", "DP-Warm.png", 1080, 1080)],
    "highlights": lambda: [png(f"hl-{k}.html", "5-Profile-Pictures/Instagram-Highlights", f"Highlight-{k}.png", 1080, 1080)
                           for k in ("sessions", "inner-child", "healing", "about", "inspiration", "book")],
    "covers": lambda: [png("cover-facebook.html", "4-Social", "Cover-Facebook.png", 1640, 624),
                       png("cover-linkedin.html", "4-Social", "Cover-LinkedIn.png", 1584, 396),
                       png("cover-youtube.html", "4-Social", "Cover-YouTube.png", 2560, 1440)],
    "docs": lambda: [pdf("intake-form.html", "6-Practice-Docs", "Client-Intake-and-Consent-Form.pdf", previews=1, preview_dpi=90),
                     pdf("letterhead.html", "6-Practice-Docs", "Letterhead.pdf", previews=1, preview_dpi=90)],
    "brand": lambda: [png("brand-sheet.html", "0-Brand", "Brand-Guidelines.png", 1600, 3140),
                      pdf("brand-sheet.html", "0-Brand", "Brand-Guidelines.pdf")],
}

if __name__ == "__main__":
    which = sys.argv[1:] or list(JOBS)
    for k in which:
        try:
            JOBS[k]()
        except subprocess.CalledProcessError as e:
            print("FAILED", k, e)
        except FileNotFoundError as e:
            print("missing", k, e)
