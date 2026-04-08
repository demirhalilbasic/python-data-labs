import pandas as pd

df = pd.read_csv("src/account_profiles.csv")

prevaranti = df[df["fraud_count"] > 0]
print(f"Računa s prevarama: {len(prevaranti)} od {len(df)}")

prevaranti = df[df["is_fraudster"] == 1]
neprevaranti = df[df["is_fraudster"] == 0]
print(f"Risk score prevaranta:   {prevaranti['risk_score'].mean():.1f}")
print(f"Risk score neprevaranta: {neprevaranti['risk_score'].mean():.1f}")

prev_bez_2fa = prevaranti[prevaranti["has_2fa"] == 0]
procenat = len(prev_bez_2fa) / len(prevaranti) * 100
print(f"Prevaranti bez 2FA: {procenat:.1f}%")