import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

df["Runtime_min"] = df["Runtime"].str.replace(" min", "").astype(int)

print(df["Runtime_min"].head())

print(f"Prosječno trajanje: {df['Runtime_min'].mean():.1f} minuta")
print(f"Najkraći film: {df['Runtime_min'].min()} minuta")
print(f"Najduži film: {df['Runtime_min'].max()} minuta")