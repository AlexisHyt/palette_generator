"""
Use this file to use the trained model
"""

import os
import torch

from _visualizers import visualize_palettes
from _models import PaletteGenerator
from _utils import get_model_path

# Model Path
MODEL_SAVE_PATH = get_model_path()

# Hyperparameters
noise_dim = 100
palette_number = 5

if __name__ == '__main__':
    if os.path.isfile(MODEL_SAVE_PATH):  # If the model already exists, then load it's dict
        loaded_generator = PaletteGenerator(noise_dim=100, output_dim=15)
        loaded_generator.load_state_dict(torch.load(get_model_path()))
        loaded_generator.eval()  # Set to evaluation mode

        z = torch.randn(palette_number, noise_dim)  # Generate n palettes
        with torch.no_grad():
            generated_palettes = loaded_generator(z).cpu().numpy()
            visualize_palettes(generated_palettes, palette_number)

    else:
        print('You need to have a model first (run: `python main.py`)')
