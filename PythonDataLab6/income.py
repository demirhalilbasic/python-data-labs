import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

print(df["Gross"].isnull().sum())

df["Gross_clean"] = df["Gross"].str.replace(",", "").astype(float)

idx = df["Gross_clean"].idxmax()
print(df.loc[idx, ["Series_Title", "Gross_clean"]])