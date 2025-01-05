import torch.nn as nn


class PaletteGenerator(nn.Module):
    def __init__(self, noise_dim=100, output_dim=15):
        super(PaletteGenerator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(noise_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 256),
            nn.ReLU(),
            nn.Linear(256, output_dim),
            nn.Sigmoid()  # Output values in [0, 1]
        )

    def forward(self, z):
        return self.model(z)


class PaletteDiscriminator(nn.Module):
    def __init__(self, input_dim=15):
        super(PaletteDiscriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 128),
            nn.LeakyReLU(0.2),
            nn.Linear(128, 1),
            nn.Sigmoid()  # Output: probability of being real
        )

    def forward(self, x):
        return self.model(x)