import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Lijevi graf: histogram
axes[0].hist(df["IMDB_Rating"], bins=20, color="steelblue")
axes[0].set_title("Distribucija ocjena")
axes[0].set_xlabel("IMDB Rating")

# Desni graf: scatter
axes[1].scatter(df["IMDB_Rating"], df["No_of_Votes"],
                alpha=0.3, s=10, color="coral")
axes[1].set_title("Rating vs Glasovi")
axes[1].set_xlabel("IMDB Rating")
axes[1].set_ylabel("Broj glasova")

plt.tight_layout()
plt.show()