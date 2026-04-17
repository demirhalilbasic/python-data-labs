import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

plt.figure(figsize=(10, 6))
plt.scatter(df["IMDB_Rating"], df["Meta_score"],
            alpha=0.5, s=20, color="teal")
plt.title("IMDB Rating vs Metascore")
plt.xlabel("IMDB Rating")
plt.ylabel("Metascore")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()