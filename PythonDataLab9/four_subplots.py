import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Gore lijevo: histogram IMDB_Rating
axes[0, 0].hist(df["IMDB_Rating"], bins=20, color="steelblue",
                edgecolor="white")
axes[0, 0].set_title("Distribucija IMDB ocjena")
axes[0, 0].set_xlabel("IMDB Rating")
axes[0, 0].set_ylabel("Broj filmova")

# Gore desno: histogram Meta_score
axes[0, 1].hist(df["Meta_score"].dropna(), bins=20, color="coral",
                edgecolor="white")
axes[0, 1].set_title("Distribucija Metascore")
axes[0, 1].set_xlabel("Metascore")
axes[0, 1].set_ylabel("Broj filmova")

# Dolje lijevo: scatter Rating vs Votes
axes[1, 0].scatter(df["IMDB_Rating"], df["No_of_Votes"],
                    alpha=0.3, s=10, color="teal")
axes[1, 0].set_title("Rating vs Glasovi")
axes[1, 0].set_xlabel("IMDB Rating")
axes[1, 0].set_ylabel("Broj glasova")

# Dolje desno: bar chart top 5 reditelja
top5 = df["Director"].value_counts().head(5)
axes[1, 1].barh(top5.index, top5.values, color="green")
axes[1, 1].set_title("Top 5 reditelja")
axes[1, 1].set_xlabel("Broj filmova")
axes[1, 1].invert_yaxis()

plt.tight_layout()
plt.show()