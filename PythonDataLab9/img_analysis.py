import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open("src/python.jpg"))
print(f"Shape: {img.shape}, Dtype: {img.dtype}")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Gore lijevo: originalna slika
axes[0, 0].imshow(img)
axes[0, 0].set_title("Original")
axes[0, 0].axis("off")

# Gore desno: zeleni kanal
axes[0, 1].imshow(img[:, :, 1], cmap="Greens")
axes[0, 1].set_title("Zeleni kanal")
axes[0, 1].axis("off")

# Dolje lijevo: grayscale
gray = img.mean(axis=2)
axes[1, 0].imshow(gray, cmap="gray")
axes[1, 0].set_title("Grayscale")
axes[1, 0].axis("off")

# Dolje desno: RGB histogram
for i, boja in enumerate(["red", "green", "blue"]):
    axes[1, 1].hist(img[:, :, i].ravel(), bins=range(1,256),
                     color=boja, alpha=0.5, label=boja.upper())
axes[1, 1].set_title("RGB Histogram")
axes[1, 1].set_xlabel("Vrijednost piksela (0-255)")
axes[1, 1].set_ylabel("Broj piksela")
axes[1, 1].legend()

plt.tight_layout()
plt.show()