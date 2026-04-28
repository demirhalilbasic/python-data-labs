import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

num_cols = ["IMDB_Rating", "Meta_score", "No_of_Votes", "Runtime"]
df["Runtime"] = df["Runtime"].str.replace(" min", "").astype(float)

korelacija = df[num_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(korelacija, annot=True, cmap="coolwarm",
            center=0, fmt=".2f", linewidths=1)
plt.title("Korelacijska matrica — IMDB dataset")
plt.tight_layout()
plt.show()