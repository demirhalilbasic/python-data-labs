import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("src/imdb_top_1000.csv")

df["Gross_clean"] = df["Gross"].str.replace(",", "").astype(float)
df_gross = df.dropna(subset=["Gross_clean"])

plt.scatter(df_gross["IMDB_Rating"], df_gross["Gross_clean"], alpha=0.4, s=15, color="steelblue")
plt.title("IMDB Rating vs Zarada")
plt.xlabel("IMDB Rating")
plt.ylabel("Gross ($)")
plt.tight_layout()
plt.show()