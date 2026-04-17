import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open("src/python.jpg"))

red_channel = img[:, :, 0]
print(f"Red channel shape: {red_channel.shape}")

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].imshow(red_channel, cmap="gray")
axes[0].set_title("Puni raspon (0-255)")

axes[1].imshow(red_channel, cmap="gray", clim=(50, 200))
axes[1].set_title("clim=(50, 200)")

axes[2].imshow(red_channel, cmap="gray", clim=(100, 180))
axes[2].set_title("clim=(100, 180)")

for ax in axes:
    ax.axis("off")
plt.tight_layout()
plt.show()