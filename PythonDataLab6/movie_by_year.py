import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")
df["Decade"] = (df["Released_Year"] // 10) * 10

print(df["Decade"].value_counts().sort_index())

print(df.groupby("Decade")["IMDB_Rating"].mean())