import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open("src/python.jpg"))

red_channel = img[:, :, 0]
print(f"Red channel shape: {red_channel.shape}")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].imshow(img)
axes[0].set_title("Originalna slika")
axes[0].axis("off")

axes[1].hist(red_channel.ravel(), bins=range(1, 256),
             color="red", alpha=0.7)
axes[1].set_title("Histogram crvenog kanala")
axes[1].set_xlabel("Vrijednost piksela (0-255)")
axes[1].set_ylabel("Broj piksela")

plt.tight_layout()
plt.show()