import pandas as pd

df = pd.read_csv("src/Sleep_health_and_lifestyle_dataset.csv", low_memory=False)

print(df.head())
print(df.info())
print(df.describe())

print(df["Sleep Duration"])
print(df[["Gender", "Age", "Sleep Duration"]])