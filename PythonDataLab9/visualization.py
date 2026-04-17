import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

df = pd.read_csv("src/imdb_top_1000.csv")

# --- 5a) Koji žanrovi zarađuju najviše? ---

df["Gross_clean"] = df["Gross"].str.replace(",", "").astype(float)
df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

zarada_po_zanru = (df.groupby("PrviZanr")["Gross_clean"]
                     .mean()
                     .dropna()
                     .sort_values(ascending=True)
                     .tail(10))

plt.figure(figsize=(10, 6))
plt.barh(zarada_po_zanru.index, zarada_po_zanru.values / 1e6,
         color="goldenrod", edgecolor="white")
plt.title("Prosječna zarada po žanru (IMDB Top 1000)", fontsize=14)
plt.xlabel("Prosječna zarada (milioni $)")
plt.tight_layout()
plt.show()


# --- 5b) Koliko filmova po deceniji? ---

df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
df["Decenija"] = (df["Released_Year"] // 10) * 10
po_deceniji = df.groupby("Decenija").size()

plt.figure(figsize=(10, 5))
bars = plt.bar(po_deceniji.index.astype(int), po_deceniji.values,
               width=8, color="steelblue", edgecolor="white")

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
             str(int(bar.get_height())), ha="center", fontsize=9)

plt.title("Broj filmova u IMDB Top 1000 po deceniji", fontsize=14)
plt.xlabel("Decenija")
plt.ylabel("Broj filmova")
plt.tight_layout()
plt.show()


# --- 5c) Koji reditelj ima najbolji prosječni rating? (min 3 filma) ---

dir_counts = df["Director"].value_counts()
dirs_3plus = dir_counts[dir_counts >= 3].index

df_filtered = df[df["Director"].isin(dirs_3plus)]
best_dirs = (df_filtered.groupby("Director")["IMDB_Rating"]
                        .mean()
                        .sort_values(ascending=True)
                        .tail(10))

plt.figure(figsize=(10, 6))
plt.barh(best_dirs.index, best_dirs.values, color="darkgreen",
         edgecolor="white")
plt.title("Top 10 reditelja po prosječnom ratingu (min. 3 filma)")
plt.xlabel("Prosječni IMDB Rating")
plt.xlim(left=7.5)
plt.tight_layout()
plt.show()


# --- 5d) python.jpg kroz razne colormap-e ---

img = np.asarray(Image.open("src/python.jpg"))
gray = img.mean(axis=2)

cmaps = ["gray", "viridis", "hot", "cool", "nipy_spectral", "terrain"]

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

for ax, cmap_name in zip(axes.ravel(), cmaps):
    ax.imshow(gray, cmap=cmap_name)
    ax.set_title(f'cmap="{cmap_name}"', fontsize=12)
    ax.axis("off")

plt.suptitle("python.jpg — 6 različitih colormap-a", fontsize=16, y=0.98)
plt.tight_layout()
plt.show()