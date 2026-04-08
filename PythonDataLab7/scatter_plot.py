import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("src/account_profiles.csv")

sample = df.sample(5000, random_state=42)

plt.scatter(sample["risk_score"], sample["fraud_rate"],
            alpha=0.3, s=10, color="steelblue")
plt.title("Risk Score vs Fraud Rate")
plt.xlabel("Risk Score")
plt.ylabel("Fraud Rate")
plt.tight_layout()
plt.show()

df_bs = df.rename(columns={
    "account_type":  "tip_racuna",
    "risk_score":    "ocjena_rizika",
    "fraud_count":   "broj_prevara",
    "is_fraudster":  "je_prevarant"
})
print(df_bs.columns)