import torch
from torch.utils.data import Dataset

class ColorPaletteDataset(Dataset):
    """Dataset class for color palettes"""

    def __init__(self, palettes):
        # Convert the list of palettes to a torch tensor
        self.palettes = torch.tensor(palettes, dtype=torch.float32)

    def __len__(self):
        return len(self.palettes)

    def __getitem__(self, idx):
        return self.palettes[idx]