"""
Generates animated GIF files for each Paratag LED pattern.
Requires: pip install Pillow
"""

from PIL import Image, ImageDraw
import os

SIZE = 20          # canvas size in pixels
RADIUS = 8         # circle radius
CENTER = SIZE // 2
COLOR_BLUE = (68, 136, 255)
COLOR_OFF = (255, 255, 255)  # white background to represent LED off
BG = (255, 255, 255)        # white background

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "images", "led")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def make_frame(color):
    """Create a single RGB frame with a circle of the given color on white."""
    img = Image.new("RGB", (SIZE, SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    x0, y0 = CENTER - RADIUS, CENTER - RADIUS
    x1, y1 = CENTER + RADIUS, CENTER + RADIUS
    draw.ellipse([x0, y0, x1, y1], fill=color)
    return img


ON = make_frame(COLOR_BLUE)
OFF = make_frame(COLOR_OFF)


def save_gif(filename, pattern):
    """
    pattern: list of (is_on, duration_ms) tuples
    """
    frames = []
    durations = []
    for is_on, ms in pattern:
        frames.append(ON if is_on else OFF)
        durations.append(ms)

    path = os.path.join(OUTPUT_DIR, filename)
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        loop=0,
        duration=durations,
        optimize=False,
    )
    print(f"Saved: {path}")


# ── LED patterns ────────────────────────────────────────────────────────────

# One short blink (turned off): 100ms on, padded with 2900ms off
save_gif("led_off.gif", [
    (True,  100),
    (False, 2900),
])

# AAD blink (turned on): 800ms on, 100ms off, 1000ms on, padded with 3100ms off
save_gif("led_on.gif", [
    (True,  800),
    (False, 100),
    (True,  1000),
    (False, 3100),
])

# Heartbeat (GPS aligning): 100ms on, 100ms off, 100ms on, 700ms off
save_gif("led_heartbeat.gif", [
    (True,  100),
    (False, 100),
    (True,  100),
    (False, 700),
])

# Occasional blink (transmitting): 4900ms off, 100ms on
save_gif("led_transmit.gif", [
    (False, 4900),
    (True,  100),
])

# Pairing: 500ms on, 500ms off
save_gif("led_pairing.gif", [
    (True,  500),
    (False, 500),
])

print("\nAll GIFs generated in:", OUTPUT_DIR)
