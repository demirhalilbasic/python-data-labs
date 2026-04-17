import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = np.asarray(Image.open("src/python.jpg"))

red_channel = img[:, :, 0]
print(f"Red channel shape: {red_channel.shape}")

# Default colormap (viridis)
plt.imshow(red_channel)
plt.colorbar()
plt.title("Crveni kanal — viridis colormap")
plt.show()

# Hot colormap
plt.imshow(red_channel, cmap="hot")
plt.colorbar()
plt.title("Crveni kanal — hot colormap")
plt.show()