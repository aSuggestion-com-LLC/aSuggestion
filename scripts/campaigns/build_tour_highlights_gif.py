#!/usr/bin/env python3
"""Builds assets/images/campaigns/tour-highlights.gif from the About Us Tour showcase
screenshots. Run from anywhere -- paths are resolved relative to this script's own
location, not the working directory.

    python3 scripts/campaigns/build_tour_highlights_gif.py

Requires Pillow (`pip install Pillow`). Uses local Outfit/Karla TTFs in
scripts/campaigns/fonts/ so this reproduces byte-identically without network access.

To change frame duration, screens, or caption copy, edit the constants below and rerun --
no other setup needed.
"""
from PIL import Image, ImageDraw, ImageFont
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
SRC_DIR = os.path.join(REPO_ROOT, "assets", "images", "showcase")
FONT_DIR = os.path.join(SCRIPT_DIR, "fonts")
OUT_PATH = os.path.join(REPO_ROOT, "assets", "images", "campaigns", "tour-highlights.gif")

# (label, filename) -- matches the About Us Tour's own tourTabs order/labels in about.html
FRAMES = [
    ("Social Rooms", "showcase-social-rooms.png"),
    ("Activities", "showcase-activities.png"),
    ("Excursions", "showcase-excursions.png"),
    ("Check-In Chats", "showcase-checkin-chat.png"),
    ("Person Centered Goals", "showcase-admin-goals.png"),
    ("Data Export", "showcase-admin-export.png"),
]

# Brand palette (tailwind.config.js)
NAVY = (1, 56, 74)
BLUE = (0, 153, 204)
ORANGE = (239, 129, 16)
WHITE = (255, 255, 255)
LETTERBOX = (255, 255, 255)

CANVAS_W = 640
SHOT_H = 380
CAPTION_H = 84
CANVAS_H = SHOT_H + CAPTION_H

FRAME_DELAY_MS = 3000  # 3 seconds per frame -- Greg's confirmed final pacing (2026-08-22)
FONT_SIZE = 30

title_font = ImageFont.truetype(os.path.join(FONT_DIR, "Outfit-Bold.ttf"), FONT_SIZE)
title_font.set_variation_by_axes([700])


def fit_contain(img, target_w, target_h):
    """Scale img to fit entirely within target_w x target_h, preserving aspect ratio."""
    src_w, src_h = img.size
    scale = min(target_w / src_w, target_h / src_h)
    new_w, new_h = round(src_w * scale), round(src_h * scale)
    return img.resize((new_w, new_h), Image.LANCZOS)


def build_frame(label, filename):
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), LETTERBOX)
    shot = Image.open(os.path.join(SRC_DIR, filename)).convert("RGB")
    fitted = fit_contain(shot, CANVAS_W, SHOT_H)
    ox = (CANVAS_W - fitted.width) // 2
    oy = (SHOT_H - fitted.height) // 2
    canvas.paste(fitted, (ox, oy))

    draw = ImageDraw.Draw(canvas)
    draw.rectangle([0, SHOT_H, CANVAS_W, CANVAS_H], fill=NAVY)
    draw.rectangle([0, SHOT_H, CANVAS_W, SHOT_H + 3], fill=BLUE)

    dot_r = 6
    bbox = draw.textbbox((0, 0), label, font=title_font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    gap = 14
    group_w = dot_r * 2 + gap + text_w
    start_x = (CANVAS_W - group_w) // 2
    cy = SHOT_H + 3 + (CAPTION_H - 3) // 2

    dot_cx = start_x + dot_r
    draw.ellipse([dot_cx - dot_r, cy - dot_r, dot_cx + dot_r, cy + dot_r], fill=ORANGE)

    text_x = start_x + dot_r * 2 + gap
    text_y = cy - text_h // 2 - bbox[1]
    draw.text((text_x, text_y), label, font=title_font, fill=WHITE)

    return canvas


def main():
    frames = [build_frame(label, filename) for label, filename in FRAMES]
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    frames[0].save(
        OUT_PATH,
        save_all=True,
        append_images=frames[1:],
        duration=FRAME_DELAY_MS,
        loop=0,
        optimize=True,
    )
    size_kb = os.path.getsize(OUT_PATH) / 1024
    print(f"Saved {OUT_PATH} ({size_kb:.1f} KB, {CANVAS_W}x{CANVAS_H}, "
          f"{len(frames)} frames @ {FRAME_DELAY_MS}ms)")


if __name__ == "__main__":
    main()
