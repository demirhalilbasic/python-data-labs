import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# ── 1. Učitavanje fotografije ──────────────────────────────────────────────────
img_original = Image.open("src/uuap_POKVARENA.png")
arr_original = np.array(img_original)

print(f"Originalna veličina : {img_original.size}  ({img_original.mode})")
print(f"  R kanal – srednja vrijednost: {arr_original[:,:,0].mean():.1f}")
print(f"  G kanal – srednja vrijednost: {arr_original[:,:,1].mean():.1f}")
print(f"  B kanal – srednja vrijednost: {arr_original[:,:,2].mean():.1f}")

# ── 2. Popravka fotografije ────────────────────────────────────────────────────
# Problem 1 – fotografija je okrenuta naopako  →  rotiraj 180°
arr_rotirana = arr_original[::-1, ::-1, :]

# Problem 2 – R i B kanali su zamijenjeni (BGR umjesto RGB)  →  zamijeni ih
arr_popravljena = arr_rotirana.copy()
arr_popravljena[:, :, 0] = arr_rotirana[:, :, 2]   # novi R  = stari B
arr_popravljena[:, :, 2] = arr_rotirana[:, :, 0]   # novi B  = stari R

img_popravljena = Image.fromarray(arr_popravljena)

# ── 3. Statistika kanala (DataFrame + Seaborn grafikon) ───────────────────────
kanali = ["R", "G", "B"]
df = pd.DataFrame({
    "Kanal"       : kanali * 2,
    "Srednja vr." : [
        arr_original[:,:,0].mean(),
        arr_original[:,:,1].mean(),
        arr_original[:,:,2].mean(),
        arr_popravljena[:,:,0].mean(),
        arr_popravljena[:,:,1].mean(),
        arr_popravljena[:,:,2].mean(),
    ],
    "Fotografija" : ["Pokvarena"] * 3 + ["Popravljena"] * 3,
})

# ── 4. Vizualizacija ──────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("Popravka fotografije – Burano, Venecija", fontsize=16, fontweight="bold")

# 4a – originalna (pokvarena) fotografija
axes[0].imshow(arr_original)
axes[0].set_title("Pokvarena fotografija\n(okrenuta + zamijenjeni kanali)", fontsize=12)
axes[0].axis("off")

# 4b – popravljena fotografija
axes[1].imshow(arr_popravljena)
axes[1].set_title("Popravljena fotografija", fontsize=12)
axes[1].axis("off")

# 4c – Seaborn usporedni grafikon RGB kanala
sns.barplot(
    ax=axes[2],
    data=df,
    x="Kanal",
    y="Srednja vr.",
    hue="Fotografija",
    palette={"Pokvarena": "#e07070", "Popravljena": "#70b070"},
)
axes[2].set_title("Usporedba RGB kanala\n(prije i poslije popravke)", fontsize=12)
axes[2].set_ylabel("Srednja vrijednost piksela (0–255)")
axes[2].set_ylim(0, 255)
axes[2].legend(title="Fotografija")

plt.tight_layout()

# ── 5. Spremanje rezultata ────────────────────────────────────────────────────
img_popravljena.save("src/uuap_POPRAVLJENA.png")
print("\nPopravljena fotografija spremljena → src/uuap_POPRAVLJENA.png")

plt.savefig("src/usporedba.png", dpi=150, bbox_inches="tight")
print("Usporedni grafikon spremljen    → src/usporedba.png")

plt.show()