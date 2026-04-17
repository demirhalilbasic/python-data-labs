import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")
df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
df["Decenija"] = (df["Released_Year"] // 10) * 10

prosjek = df.groupby("Decenija")["IMDB_Rating"].mean()

plt.figure(figsize=(10, 5))
plt.plot(prosjek.index, prosjek.values, "o-", color="navy",
         linewidth=2, markersize=8, label="Prosječna ocjena")
plt.title("Prosječna IMDB ocjena po deceniji")
plt.xlabel("Decenija")
plt.ylabel("Prosječna ocjena")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()