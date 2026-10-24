"""Removes the Gemini sparkle watermark (bottom-right) from the generated images.
Masters -> art/master/*.png ; web copies -> art/*.jpg. Originals kept in art/original/.
Run all:  python remove_sparkle.py      One:  python remove_sparkle.py P5"""
import sys
import numpy as np
from PIL import Image, ImageFilter

ART = __import__("pathlib").Path(__file__).parent / "art"
JOBS = {  # file -> (output name, method, donor dx,dy)
    "P1": ("portrait-formal", "patch", (-170, 0)),
    "P2": ("portrait-warm",   "patch", (-60, -140)),
    "P3": ("bg-poster",       "patch", (-190, 0)),
    "P4": ("bg-brochure",     "diffuse", None),
    "P5": ("hanuman-dhyan",   "plain", None),   # sparkle sits on flat indigo: fill + matched grain
}

TEX = {"P1": 0.35, "P2": 1.0}

def star_mask(shape, cx, cy, r, p=0.8):
    h, w = shape
    yy, xx = np.mgrid[0:h, 0:w]
    return ((np.abs(xx - cx) / r) ** p + (np.abs(yy - cy) / r) ** p) <= 1.0

def feather(mask, rad):
    im = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(rad))
    return np.asarray(im, dtype=np.float32) / 255.0

def blur_norm(img, w, rad):
    """Gaussian blur of img ignoring pixels where w==0 (normalised convolution)."""
    out = np.zeros_like(img)
    wb = np.asarray(Image.fromarray((w * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(rad)), dtype=np.float32) / 255.0
    for c in range(3):
        ch = Image.fromarray((img[..., c] * w).clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(rad))
        out[..., c] = np.asarray(ch, dtype=np.float32) / np.maximum(wb, 1e-3) / 255.0 * 255.0 * 1.0
    return out

def diffuse(img, mask, iters=4000):
    out = img.copy()
    ys, xs = np.where(mask)
    y0, y1, x0, x1 = ys.min() - 4, ys.max() + 5, xs.min() - 4, xs.max() + 5
    sub = out[y0:y1, x0:x1].copy(); m = mask[y0:y1, x0:x1]
    sub[m] = sub[~m].mean(axis=0)
    for _ in range(iters):
        nb = (np.roll(sub, 1, 0) + np.roll(sub, -1, 0) + np.roll(sub, 1, 1) + np.roll(sub, -1, 1)) / 4
        sub[m] = nb[m]
    out[y0:y1, x0:x1] = sub
    return out

for key, (name, method, donor) in JOBS.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    im = Image.open(ART / "original" / f"{key}.png").convert("RGB")
    a = np.asarray(im, dtype=np.float32)
    h, w, _ = a.shape
    cx, cy = w - 112, h - 112
    mask = star_mask((h, w), cx, cy, 68, p=0.9)
    fm = feather(mask.astype(np.float32), 3)
    ring = (star_mask((h, w), cx, cy, 100, p=0.9) & ~mask).astype(np.float32)
    if method == "patch":
        dx, dy = donor
        don = np.roll(np.roll(a, -dy, 0), -dx, 1)  # donor[y,x] = a[y+dy, x+dx]
        donimg = Image.fromarray(don.clip(0, 255).astype(np.uint8))
        low = np.asarray(donimg.filter(ImageFilter.GaussianBlur(6)), dtype=np.float32)
        # smooth lighting from the surroundings + weave/grain texture from the donor
        fill = diffuse(a, mask) + (don - low) * TEX.get(key, 1.0)
    elif method == "plain":
        mask = star_mask((h, w), cx, cy, 62, p=0.9)
        fm = feather(mask.astype(np.float32), 2)
        don = np.roll(a, 220, 1)  # real background grain from 220 px to the left
        low = np.asarray(Image.fromarray(don.clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6)), dtype=np.float32)
        fill = diffuse(a, mask) + (don - low)
    else:
        gold0 = (a[..., 0] - a[..., 2]) > 70
        ys0, xs0 = np.where(mask)
        box = np.zeros_like(mask); box[ys0.min() - 14:ys0.max() + 15, xs0.min() - 14:xs0.max() + 15] = True
        fill = diffuse(a, mask | (gold0 & box))
        # add paper grain matched to the ring
        sd = a[ring > 0].std(axis=0).mean() * 0.35
        rng = np.random.default_rng(7)
        g = rng.normal(0, sd, (h, w, 1)).astype(np.float32)
        gimg = Image.fromarray(((g[..., 0] * 8) + 128).clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.7))
        fill = fill + ((np.asarray(gimg, dtype=np.float32) - 128) / 8)[..., None]
        # restore the gold border lines that cross the mask by copying along the line direction
        gold = (a[..., 0] - a[..., 2]) > 70
        by0, by1, bx0, bx1 = cy - 68, cy + 68, cx - 68, cx + 68
        cols = np.where(gold[by0 - 150:by0 - 80, bx0:bx1 + 40].mean(0) > 0.5)[0] + bx0   # vertical line columns
        rows = np.where(gold[by0:by1 + 40, bx0 - 150:bx0 - 80].mean(1) > 0.5)[0] + by0    # horizontal line rows
        print("  lines cols", cols.tolist(), "rows", rows.tolist())
        for x in cols:
            for dy in (-130,):
                fill[by0:by1, x - 1:x + 2] = a[by0 + dy:by1 + dy, x - 1:x + 2]
        for y in rows:
            fill[y - 1:y + 2, bx0:bx1] = a[y - 1:y + 2, bx0 - 130:bx1 - 130]
    out = a * (1 - fm[..., None]) + fill * fm[..., None]
    res = Image.fromarray(out.clip(0, 255).astype(np.uint8))
    (ART / "master").mkdir(exist_ok=True)
    res.save(ART / "master" / f"{name}.png")
    web = res if key in ("P3", "P4") else res
    web.save(ART / f"{name}.jpg", quality=92, optimize=True, subsampling=0)
    print(name, res.size, "ok")
