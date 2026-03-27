import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

drame = df[df["Genre"].str.contains("Drama")]
akcije = df[df["Genre"].str.contains("Action")]

print(f"Broj drama: {len(drame)}")
print(f"Broj komedija: {len(akcije)}")

print(f"Prosječna ocjena drama: {drame['IMDB_Rating'].mean():.2f}")
print(f"Prosječna ocjena akcija: {akcije['IMDB_Rating'].mean():.2f}")