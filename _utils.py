import random
from pathlib import Path

from _generators import generate_analogous_palette, generate_complementary_palette, generate_triadic_palette, \
    generate_monochromatic_palette


def get_model_name() -> str:
    """
    Get the model Name

    :return:
    """
    return "model_generator.pth"


def get_model_path() -> str:
    """
    Get Model path

    :return:
    """
    path = Path("models")
    path.mkdir(parents=True, exist_ok=True)
    name = get_model_name()
    return path / name


def generate_real_palettes(num_palettes):
    palettes = []
    for i in range(num_palettes):
        # Randomly choose a color scheme generator
        generator = random.choice([
            generate_analogous_palette,
            generate_complementary_palette,
            generate_triadic_palette,
            generate_monochromatic_palette
        ])

        palette = generator()
        palettes.append(palette)
    return palettes