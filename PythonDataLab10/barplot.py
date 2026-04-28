import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

top5_zanrovi = df["PrviZanr"].value_counts().head(5).index
df_top5 = df[df["PrviZanr"].isin(top5_zanrovi)]

plt.figure(figsize=(10, 5))
sns.barplot(data=df_top5, x="PrviZanr", y="IMDB_Rating",
            palette="viridis", errorbar=("ci", 95))
plt.title("Prosječna ocjena po žanru (s intervalom povjerenja)")
plt.ylabel("Prosječna IMDB ocjena")
plt.show()