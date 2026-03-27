import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

df["Director"].value_counts().head(10)
print(df["Director"].value_counts())

nolan = df[df["Director"] == "Christopher Nolan"]
print(nolan["IMDB_Rating"].mean())

spilberg = df[df["Director"] == "Steven Spielberg"]
print(spilberg["IMDB_Rating"].mean())