import pandas as pd
import matplotlib.pyplot as plt

fp = pd.read_csv("src/fraud_patterns.csv")
fp_sorted = fp.sort_values("fraud_share_pct", ascending=True)

plt.barh(fp_sorted["fraud_pattern"], fp_sorted["fraud_share_pct"],
         color="crimson")
plt.title("Udio svake vrste prevare (%)")
plt.xlabel("Procenat (%)")
plt.tight_layout()
plt.show()