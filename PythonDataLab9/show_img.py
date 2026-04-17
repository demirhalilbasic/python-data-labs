import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open("src/python.jpg"))

print(f"type:  {type(img)}")
print(f"shape: {img.shape}")
print(f"dtype: {img.dtype}")

plt.imshow(img)
plt.title("Python — doslovno!")
plt.axis("off")
plt.show()