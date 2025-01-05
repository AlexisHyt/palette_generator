import colorsys
import random

def generate_analogous_palette():
    """Generate 5 analogous colors starting from a random hue"""
    base_hue = random.random()  # Random starting hue
    saturation = random.uniform(0.5, 0.9)  # Moderate to high saturation
    value = random.uniform(0.7, 1.0)  # Medium to high brightness

    colors = []
    for i in range(5):
        # Shift hue by small increments (0.05 = 18 degrees)
        hue = (base_hue + (i - 2) * 0.05) % 1.0
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        colors.extend(rgb)

    return colors

def generate_complementary_palette():
    """Generate 5 colors based on complementary color scheme"""
    base_hue = random.random()
    complement_hue = (base_hue + 0.5) % 1.0

    colors = []
    # Base color and variants
    for i in range(3):
        sat = random.uniform(0.5, 0.9)
        val = random.uniform(0.7, 1.0)
        rgb = colorsys.hsv_to_rgb(base_hue, sat, val)
        colors.extend(rgb)

    # Complementary color and variant
    for i in range(2):
        sat = random.uniform(0.5, 0.9)
        val = random.uniform(0.7, 1.0)
        rgb = colorsys.hsv_to_rgb(complement_hue, sat, val)
        colors.extend(rgb)

    return colors

def generate_triadic_palette():
    """Generate 5 colors based on triadic color scheme"""
    base_hue = random.random()
    hue2 = (base_hue + 0.33) % 1.0
    hue3 = (base_hue + 0.66) % 1.0

    colors = []
    # Two colors from first hue
    for i in range(2):
        sat = random.uniform(0.5, 0.9)
        val = random.uniform(0.7, 1.0)
        rgb = colorsys.hsv_to_rgb(base_hue, sat, val)
        colors.extend(rgb)

    # Two colors from second hue
    for i in range(2):
        sat = random.uniform(0.5, 0.9)
        val = random.uniform(0.7, 1.0)
        rgb = colorsys.hsv_to_rgb(hue2, sat, val)
        colors.extend(rgb)

    # One color from third hue
    sat = random.uniform(0.5, 0.9)
    val = random.uniform(0.7, 1.0)
    rgb = colorsys.hsv_to_rgb(hue3, sat, val)
    colors.extend(rgb)

    return colors

def generate_monochromatic_palette():
    """Generate 5 colors in monochromatic scheme"""
    hue = random.random()
    colors = []

    for i in range(5):
        sat = random.uniform(0.3, 0.9)
        val = 0.4 + (i * 0.15)  # Gradually increasing brightness
        rgb = colorsys.hsv_to_rgb(hue, sat, val)
        colors.extend(rgb)

    return colors