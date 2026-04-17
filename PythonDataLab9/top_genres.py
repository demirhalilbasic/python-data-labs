import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")
df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

top_zanrovi = df["PrviZanr"].value_counts().head(10)

plt.figure(figsize=(10, 6))
bars = plt.barh(top_zanrovi.index, top_zanrovi.values, color="teal")
plt.title("Top 10 žanrova u IMDB Top 1000")
plt.xlabel("Broj filmova")
plt.gca().invert_yaxis()

# Bonus: brojevi na stupcima
for bar in bars:
    plt.text(bar.get_width() + 2, bar.get_y() + bar.get_height() / 2,
             str(int(bar.get_width())), va="center", fontsize=10)

plt.tight_layout()
plt.show()