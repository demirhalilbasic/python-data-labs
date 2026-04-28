import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")
df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

df["Runtime_num"] = pd.to_numeric(
    df["Runtime"].str.replace(" min", "", regex=False), errors="coerce"
)
df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
df["Decenija"] = (df["Released_Year"] // 10) * 10

top5_zanrovi = df["PrviZanr"].value_counts().head(5).index
df_top5 = df[df["PrviZanr"].isin(top5_zanrovi)]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.histplot(data=df, x="IMDB_Rating", bins=20, kde=True,
             ax=axes[0, 0], color="steelblue")
axes[0, 0].set_title("Distribucija IMDB ocjena")

sns.boxplot(data=df_top5, x="PrviZanr", y="Runtime_num",
            ax=axes[0, 1], palette="Set2")
axes[0, 1].set_title("Runtime po žanru")

sns.scatterplot(data=df_top5, x="IMDB_Rating", y="No_of_Votes",
                hue="PrviZanr", alpha=0.5, ax=axes[1, 0])
axes[1, 0].set_title("Rating vs Glasovi")

prosjek = df.groupby("Decenija")["IMDB_Rating"].mean().reset_index()
prosjek = prosjek[prosjek["Decenija"] >= 1960]
sns.barplot(data=prosjek, x="Decenija", y="IMDB_Rating",
            ax=axes[1, 1], color="coral")
axes[1, 1].set_title("Prosjek po deceniji")
axes[1, 1].tick_params(axis="x", rotation=45)

plt.suptitle("IMDB Top 1000 — Seaborn Dashboard", fontsize=16)
plt.tight_layout()
plt.show()