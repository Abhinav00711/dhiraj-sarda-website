# Dhiraj Sarda — brand kit

Past Life Regression Therapist & Transpersonal Hypnotherapist · Delhi & Online · +91 93501 55044 · dhirajsarda79@gmail.com

Everything is in English **and** Hindi. All copy comes from one file (`Build/content.py`), so print, social and website always say the same thing.

## What's where

| Folder | What | Use |
|---|---|---|
| `Build/out/0-Brand/` | Brand guidelines (PNG + PDF) | Logo, colours, fonts, icons, photo rules, **"Words we use"** |
| `Build/out/1-Brochure/` | 6-page A4 brochure (PDF) + each page as PNG | Send the PDF, or share page images on WhatsApp |
| `Build/out/2-Trifold-Leaflet/` | A4 tri-fold leaflet, 2 sides (PDF) | Printed handout, folds into 3 panels |
| `Build/out/3-Visiting-Card/` | Print PDFs (front + back) EN & HI, 600-dpi previews, mockup | Send the `-print.pdf` to the printer |
| `Build/out/4-Social/` | One-page flyer, story poster, 4 posts (1080×1350), Facebook / LinkedIn / YouTube covers | WhatsApp forwards, status, Instagram, Facebook |
| `Build/out/5-Profile-Pictures/` | DPs (formal portrait, warm photo, logo) + 6 Instagram highlight covers | WhatsApp / Instagram / Facebook profile |
| `Build/out/6-Practice-Docs/` | Bilingual client intake & consent form, letterhead | Print and use with every new client |
| `Website/` | Complete website (open `index.html` in a browser) | See "Put the website online" below |
| `Dhiraj-Sarda-Website.zip` | The same website, zipped | Drag-and-drop upload |

## Printing

- **Visiting card:** 89 × 51 mm (3.5 × 2 in) trim, **3 mm bleed included** (PDF page is 95 × 57 mm). 350 gsm matt or velvet laminate. Optional upgrade: gold foil on the front mark and name. One side per page: page 1 = front, page 2 = back.
- **Brochure:** A4, 6 pages, 170 gsm matt art paper. As a printed booklet, add 2 pages or print as loose sheets.
- **Tri-fold:** A4 landscape, double-sided, 2 roll folds. Page 1 = outside, page 2 = inside.
- **Intake form / letterhead:** plain A4, any office printer (white background, saves ink).

## Put the website online (free)

The site is live on GitHub Pages: **https://abhinav00711.github.io/dhiraj-sarda-website/**

1. Every push to `main` that changes `Website/` redeploys it automatically (`.github/workflows/pages.yml`). Only the `Website/` folder is published.
2. Optional: buy a domain such as `dhirajsarda.in` (~₹600–900/yr) and connect it in the repo → *Settings → Pages → Custom domain*.
3. Once the domain is live, put it in `Build/content.py` → `WEBSITE = "dhirajsarda.in"` and rebuild.

This repo is public. `Certificate.png`, `References/`, `OwnImages/` and the old `_previous/` drafts are kept out by `.gitignore`: keep them on this computer only.

The booking form needs no server: it opens WhatsApp with the message pre-filled. Nothing is stored. Visitors can add `?lang=hi` to the link to open the Hindi version directly.

## Health claims — keep it safe

The brand mentions migraine, pain, depression and sugar, because those are real concerns of the people who come. It always frames them as **support alongside the doctor's care**:

- Diabetes is on the Schedule of India's **Drugs & Magic Remedies (Objectionable Advertisements) Act, 1954**. In 2024 the Supreme Court enforced the Act against cure claims. **Never** write "sugar cure", "sugar healing" or "diabetes treatment". Use "Sugar (diabetes): stress & cravings support".
- No "guaranteed", "100%", "permanent relief", "stop your medicines", or "Dr." title.
- Every piece that names a health condition carries the "please continue your medicines" line.

## Other brand rules (confirmed with Dhiraj, Oct 2026)

- **No trainer's name.** The trainer is not named anywhere. Training is credited to the International Past Life Academy (IPLA) and the IPHM (UK) accreditation.
- **The scanned certificate is not published**, because it carries the trainer's name, seal and website. Brochure and website show a typeset credential panel instead (diploma, IPHM UK, 115 hours, Reg. 202610_28) and say the original is available on request. Do not edit the certificate itself.
- **No address.** Location is only "Delhi & Online"; in-person sessions read "In Delhi, by appointment".
- **Name in Hindi:** धीरज सारड़ा.
- **Hanuman illustration** (`Build/art/hanuman-dhyan.jpg`, watermark removed by `remove_sparkle.py P5`): used on the website's Inspiration section, the "Remember your strength" post and the brand sheet. Never place lines, text or rays across the figure.

## Editing & rebuilding

Needs Python 3 (with Pillow, PyMuPDF, segno) and Google Chrome.

```
cd Build
python build.py      # writes all print/social HTML into Build/html/
python render.py     # renders PDFs/PNGs into Build/out/   (or: python render.py card brochure)
python site.py       # regenerates Website/index.html + images
```

- Text: `Build/content.py` (EN + HI side by side). Website-only text (menu, form, breathing guide) is at the top of `Build/site.py`.
- Icons, mark, mandala, Ram-heart emblem, QR: `Build/assets.py`
- Layouts: `Build/build.py` (brochure) and `Build/pieces.py` (everything else)
- Website look & motion: `Website/assets/css/style.css`, `Website/assets/js/main.js`
