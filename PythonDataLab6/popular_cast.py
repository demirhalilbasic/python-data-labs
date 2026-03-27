import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

all_stars = pd.concat([df["Star1"], df["Star2"], df["Star3"], df["Star4"]])

print(all_stars.value_counts().head(10))