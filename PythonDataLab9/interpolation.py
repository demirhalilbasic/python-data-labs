import matplotlib.pyplot as plt
from PIL import Image

small = Image.open("src/python.jpg")
small.thumbnail((16, 16))

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].imshow(small, interpolation="nearest")
axes[0].set_title("Nearest (pikselizirano)")

axes[1].imshow(small, interpolation="bilinear")
axes[1].set_title("Bilinear (glatkije)")

axes[2].imshow(small, interpolation="bicubic")
axes[2].set_title("Bicubic (najglatkije)")

for ax in axes:
    ax.axis("off")
plt.tight_layout()
plt.show()