import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

top_dirs = df["Director"].value_counts().head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_dirs.index, top_dirs.values, color="coral")
plt.title("Top 10 reditelja u IMDB Top 1000")
plt.xlabel("Broj filmova")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()