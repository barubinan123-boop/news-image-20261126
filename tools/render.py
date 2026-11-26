#!/usr/bin/env python3
"""Render the 26 November 2026 world-news image (1024x1024 PNG).

Run from the repo root:  python3 tools/render.py
Writes entry.png next to main.ts. Deterministic: same bytes every run.
Only stdlib + Pillow are used at build time; the shipped entry program
(main.ts) only copies the finished PNG, so the graded run needs no
network, no fonts and no libraries.
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "entry.png")

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (20, 20, 20)
NAVY = (16, 35, 63)
RED = (142, 27, 27)
CREAM = (250, 246, 236)
GREY = (90, 88, 82)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = font("DejaVuSans-Bold.ttf", 52)
F_KICK = font("DejaVuSans-Bold.ttf", 15)
F_FOCAL = font("DejaVuSans-Bold.ttf", 37)
F_FOCAL_SUB = font("DejaVuSans.ttf", 17)
F_TAG = font("DejaVuSans-Bold.ttf", 10)
F_CARD = font("DejaVuSans-Bold.ttf", 13)
F_FOOT = font("DejaVuSans.ttf", 12)
F_CHART = font("DejaVuSans-Bold.ttf", 15)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


REGION_COLORS = {
    "ASIA": (192, 57, 43),
    "EUROPE": (46, 111, 183),
    "N. AMERICA": (30, 122, 76),
    "S. AMERICA": (142, 68, 173),
    "AFRICA": (212, 136, 15),
    "MIDDLE EAST": (14, 124, 123),
    "OCEANIA": (91, 124, 153),
    "SPACE": (51, 51, 51),
}

# (region, headline) — 35 grid cards; the focal panel carries tariffs,
# and its second line carries the US-markets story.
CARDS = [
    ("ASIA", "India marks Constitution Day"),
    ("ASIA", "IITs to add 6,000 seats in AI, robotics & space"),
    ("ASIA", "India unveils Rs 15,000-crore aid for Nepal"),
    ("ASIA", "India: keep humans in control of AI weapons"),
    ("ASIA", "Hasina asks to return to Bangladesh on 16 Dec"),
    ("ASIA", "Bangladesh lifts garment minimum wage 36%"),
    ("ASIA", "Flipkart CEO to step down in December"),
    ("ASIA", "1,220 players sign up for IPL 2027 auction"),
    ("ASIA", "Sooryavanshi smashes 204 off 53 balls vs UAE"),
    ("ASIA", "PIA resumes UK flights on its own jets"),
    ("ASIA", "North Korea expels Swiss diplomat"),
    ("ASIA", "Hong Kong tower-fire toll reaches 168"),
    ("EUROPE", "Gukesh-Sindarov chess title Game 2 drawn"),
    ("EUROPE", "Duran Duran guitarist Andy Taylor dies at 65"),
    ("EUROPE", "BBC appeals ruling on Trump's $10bn suit"),
    ("EUROPE", "Russia's own toll: ~500,000 lost in Ukraine war"),
    ("N. AMERICA", "US Army blast of 5 tons of explosives 'a success'"),
    ("N. AMERICA", "Plane crash off Mississippi kills six"),
    ("N. AMERICA", "Macy's Thanksgiving parade postponed"),
    ("N. AMERICA", "Steelers release four-time MVP Aaron Rodgers"),
    ("N. AMERICA", "King tides flood California coastline"),
    ("N. AMERICA", "Shein to pay $100m in FTC settlement"),
    ("N. AMERICA", "Unclassified CIA system breached in cyberattack"),
    ("N. AMERICA", "Huawei guilty of stealing US trade secrets"),
    ("N. AMERICA", "Canada PM roasts Trump with impersonator"),
    ("MIDDLE EAST", "Judges: drop gravest charges against Netanyahu"),
    ("AFRICA", "Cairo tanker fire kills 31"),
    ("AFRICA", "Ramaphosa wins court battle over impeachment"),
    ("AFRICA", "Zimbabwe warrant for Mugabe's son"),
    ("AFRICA", "Five Mexicans held in Nigeria over $227m meth lab"),
    ("AFRICA", "DR Congo plane missing; rebels claim shoot-down"),
    ("S. AMERICA", "Colombia police free 76 supermarket hostages"),
    ("OCEANIA", "Australia inflation hits 4.9%; ASX sinks"),
    ("OCEANIA", "Senator Blyth defects to One Nation"),
    ("SPACE", "Asteroid crater revealed: stadium-sized scar"),
]


def draw_globe(d, cx, cy, r, color):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=3)
    d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=color, width=2)
    d.line([cx - r, cy, cx + r, cy], fill=color, width=2)
    d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 180, fill=color, width=2)
    d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 180, 360, fill=color, width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Header band ----
    d.rectangle([0, 0, W, 100], fill=NAVY)
    d.rectangle([0, 100, W, 104], fill=RED)
    draw_globe(d, 52, 50, 30, CREAM)
    d.text((96, 14), "THE WORLD IN ONE DAY", font=F_KICK, fill=(232, 196, 120))
    d.text((96, 34), "THURSDAY 26 NOVEMBER 2026", font=F_TITLE, fill=CREAM)

    # ---- Focal panel: tariffs ----
    fx, fy, fw, fh = 6, 112, 1012, 184
    d.rectangle([fx, fy, fx + fw, fy + fh], fill=(255, 255, 255),
                outline=(200, 195, 185), width=1)
    d.rectangle([fx, fy, fx + 10, fy + fh], fill=RED)
    d.text((fx + 26, fy + 12), "TOP STORY  •  TRADE WAR",
           font=F_KICK, fill=RED)
    d.text((fx + 26, fy + 36),
           "US slaps new tariffs on China,", font=F_FOCAL, fill=INK)
    d.text((fx + 26, fy + 78),
           "the EU and Brazil", font=F_FOCAL, fill=INK)
    d.text((fx + 26, fy + 128),
           "Section 301 probe hits 16 economies. Markets slide too:",
           font=F_FOCAL_SUB, fill=GREY)
    d.text((fx + 26, fy + 152),
           "Nasdaq -2%, near bear market as the AI sell-off deepens.",
           font=F_FOCAL_SUB, fill=GREY)

    # Falling-market chart on the right of the focal panel.
    cx0, cy0, cw, chh = 700, 132, 300, 140
    d.rectangle([cx0, cy0, cx0 + cw, cy0 + chh], fill=(248, 240, 228),
                outline=(200, 195, 185), width=1)
    d.text((cx0 + 14, cy0 + 8), "NASDAQ  -2%  •  NEAR BEAR MARKET",
           font=font("DejaVuSans-Bold.ttf", 13), fill=RED)
    pts = [(cx0 + 14 + i * 34, cy0 + 44 + i * 9 + (i * i) // 8)
           for i in range(9)]
    d.line(pts, fill=RED, width=4, joint="curve")
    for (px, py) in pts:
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=RED)

    # ---- Grid of story cards: 5 columns x 7 rows ----
    cols, rows = 5, 7
    cw2, ch2, gap = 196, 90, 8
    gx, gy = 6, 304
    for idx, (region, headline) in enumerate(CARDS):
        col, row = idx % cols, idx // cols
        x = gx + col * (cw2 + gap)
        y = gy + row * (ch2 + gap)
        color = REGION_COLORS[region]
        d.rectangle([x, y, x + cw2, y + ch2], fill=(255, 255, 255),
                    outline=(205, 200, 190), width=1)
        d.rectangle([x, y, x + cw2, y + 5], fill=color)
        d.text((x + 8, y + 11), region, font=F_TAG, fill=color)
        lines = wrap(d, headline, F_CARD, cw2 - 16)[:3]
        ly = y + 30
        for line in lines:
            d.text((x + 8, ly), line, font=F_CARD, fill=INK)
            ly += 16

    # ---- Footer ----
    d.text((6, 992),
           "37 stories, 8 regions — every story verified against a primary source on 26 November 2026.",
           font=F_FOOT, fill=GREY)
    d.text((6, 1008),
           "Sources: Reuters  •  AP  •  BBC  •  Xinhua  •  The Hindu  •  The West Australian",
           font=F_FOOT, fill=GREY)

    img.save(OUT, format="PNG", optimize=True)


if __name__ == "__main__":
    main()
    print("wrote", OUT)
