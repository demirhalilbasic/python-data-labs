import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")
df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

top5_zanrovi = df["PrviZanr"].value_counts().head(5).index
df_top5 = df[df["PrviZanr"].isin(top5_zanrovi)]

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df_top5, x="PrviZanr", y="IMDB_Rating",
            ax=ax, palette="Set2", order=top5_zanrovi)
sns.stripplot(data=df_top5, x="PrviZanr", y="IMDB_Rating",
              ax=ax, color="black", alpha=0.4, size=4,
              order=top5_zanrovi)
plt.title("IMDB ocjene po žanru — boxplot + strip")
plt.tight_layout()
plt.show()