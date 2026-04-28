import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

top5_zanrovi = df["PrviZanr"].value_counts().head(5).index
df_top5 = df[df["PrviZanr"].isin(top5_zanrovi)]

plt.figure(figsize=(10, 5))
sns.histplot(data=df_top5, x="IMDB_Rating", hue="PrviZanr",
             bins=15, alpha=0.5)
plt.title("Distribucija ocjena po žanru")
plt.show()

plt.figure(figsize=(10, 5))
sns.kdeplot(data=df_top5, x="IMDB_Rating", hue="PrviZanr",
            fill=True, alpha=0.4)
plt.title("KDE po žanru")
plt.show()