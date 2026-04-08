import pandas as pd

df = pd.read_csv("src/account_profiles.csv")

print(df.shape)
print(df.columns)
print(df.head())
print(df.info())