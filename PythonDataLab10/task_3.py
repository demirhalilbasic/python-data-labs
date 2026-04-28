import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
df["Decenija"] = (df["Released_Year"] // 10) * 10

top5_zanrovi = df["PrviZanr"].value_counts().head(5).index
df_top5 = df[df["PrviZanr"].isin(top5_zanrovi)]

pivot = pd.pivot_table(df_top5, values="IMDB_Rating",
                       index="Decenija", columns="PrviZanr",
                       aggfunc="mean")
pivot = pivot.loc[pivot.index >= 1950]

plt.figure(figsize=(10, 8))
sns.heatmap(pivot, annot=True, cmap="YlOrRd", fmt=".1f",
            linewidths=0.5)
plt.title("Prosječna IMDB ocjena — Decenija vs Žanr")
plt.tight_layout()
plt.show()