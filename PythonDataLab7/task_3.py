import pandas as pd

fp = pd.read_csv("src/fraud_patterns.csv")
df = pd.read_csv("src/account_profiles.csv")

fp["fraud_pattern"] = fp["fraud_pattern"].replace({
    "card_not_present": "CNP prevara",
    "account_takeover": "Preuzimanje računa",
    "card_present_stolen": "Ukradena kartica",
    "friendly_fraud": "Lažna reklamacija",
    "atm_fraud": "ATM prevara",
    "money_laundering": "Pranje novca",
    "identity_theft": "Krađa identiteta"
})
print(fp[["fraud_pattern", "fraud_share_pct"]])

df.loc[df["risk_score"] > 50, "rizik_kategorija"] = "Visok"
df.loc[(df["risk_score"] > 25) & (df["risk_score"] <= 50), "rizik_kategorija"] = "Srednji"
df.loc[df["risk_score"] <= 25, "rizik_kategorija"] = "Nizak"

print(df["rizik_kategorija"].value_counts())