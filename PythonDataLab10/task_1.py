import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")
df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

top10 = df["PrviZanr"].value_counts().head(10).index
df_top10 = df[df["PrviZanr"].isin(top10)]

plt.figure(figsize=(10, 6))
sns.countplot(data=df_top10, y="PrviZanr",
              order=top10, palette="viridis")
plt.title("Top 10 žanrova — IMDB Top 1000")
plt.xlabel("Broj filmova")
plt.tight_layout()
plt.show()