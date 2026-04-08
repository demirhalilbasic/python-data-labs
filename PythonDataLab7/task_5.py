import pandas as pd

fp = pd.read_csv("src/fraud_patterns.csv")
df = pd.read_csv("src/account_profiles.csv")

bez_2fa = df[df["has_2fa"] == 0]
sa_2fa  = df[df["has_2fa"] == 1]
print(f"Bez 2FA: {bez_2fa['fraud_rate'].mean():.4f}")
print(f"Sa 2FA:  {sa_2fa['fraud_rate'].mean():.4f}")

print(df.groupby("account_type")["is_fraudster"].mean())

print(fp.sort_values("avg_amount", ascending=False)[["fraud_pattern", "avg_amount"]])