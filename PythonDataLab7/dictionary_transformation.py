import pandas as pd

df = pd.read_csv("src/account_profiles.csv")

tip_prevod = {
    "personal": "Lični",
    "business": "Poslovni",
    "premium":  "Premium"
}

df["tip_racuna"] = df["account_type"].map(tip_prevod)
print(df[["account_id", "account_type", "tip_racuna"]].head())