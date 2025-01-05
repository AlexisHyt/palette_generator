from pathlib import Path
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

from _datasets import ColorPaletteDataset
from _models import PaletteGenerator, PaletteDiscriminator
from _utils import generate_real_palettes
from _visualizers import visualize_loss

# Paths
SAVE_MODEL_AFTER_TRAINING = True
MODEL_PATH = Path("models")
MODEL_PATH.mkdir(parents=True, exist_ok=True)
MODEL_NAME = "model_generator.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME

# Hyperparameters
noise_dim = 100
palette_dim = 15
batch_size = 64
epochs = 800
lr = 0.0002

# Generate n different palettes using different color schemes
num_palettes = 50000
palettes = generate_real_palettes(num_palettes)

# Create the dataset
dataset = ColorPaletteDataset(palettes)
dataloader = DataLoader(
    dataset,
    batch_size=batch_size,
    shuffle=True,
    num_workers=0
)

# Instantiate models
generator = PaletteGenerator(noise_dim=noise_dim, output_dim=palette_dim)
discriminator = PaletteDiscriminator(input_dim=palette_dim)

# Optimizers
optimizer_g = optim.Adam(generator.parameters(), lr=lr)
optimizer_d = optim.Adam(discriminator.parameters(), lr=lr)

# Loss
criterion = nn.BCELoss()
g_losses = []
d_losses = []

# Training Loop
for epoch in range(epochs):
    for real_palettes in dataloader:
        real_palettes = real_palettes.to(torch.float32)
        batch_size = real_palettes.size(0)

        # Train Discriminator
        optimizer_d.zero_grad()

        # Real labels: 1, Fake labels: 0
        real_labels = torch.ones(batch_size, 1)
        fake_labels = torch.zeros(batch_size, 1)

        # Discriminator loss on real palettes
        real_output = discriminator(real_palettes)
        real_loss = criterion(real_output, real_labels)

        # Generate fake palettes
        z = torch.randn(batch_size, noise_dim)
        fake_palettes = generator(z)

        # Discriminator loss on fake palettes
        fake_output = discriminator(fake_palettes.detach())
        fake_loss = criterion(fake_output, fake_labels)

        # Total Discriminator loss
        d_loss = real_loss + fake_loss
        d_losses.append(d_loss.item())
        d_loss.backward()
        optimizer_d.step()

        # Train Generator
        optimizer_g.zero_grad()

        # Generator tries to make the discriminator believe fake palettes are real
        fake_output = discriminator(fake_palettes)
        g_loss = criterion(fake_output, real_labels)
        g_losses.append(g_loss.item())

        g_loss.backward()
        optimizer_g.step()

    print(f"Epoch [{epoch + 1}/{epochs}], D Loss: {d_loss.item():.4f}, G Loss: {g_loss.item():.4f}")

# Save Model
if SAVE_MODEL_AFTER_TRAINING:
    torch.save(obj=generator.state_dict(), f=MODEL_SAVE_PATH)
    print(f"Model {MODEL_NAME} has been saved in {MODEL_SAVE_PATH}")

# Visualize losses
visualize_loss(g_losses, "g_losses")
visualize_loss(d_losses, "d_losses")