import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/Sleep_health_and_lifestyle_dataset.csv", low_memory=False)

# Prosjecan stress level po kategoriji sleep disorder
disorder_stress = (
	df.groupby("Sleep Disorder", dropna=False)["Stress Level"]
	.mean()
	.sort_values(ascending=False)
)

labels = ["No Disorder" if pd.isna(x) else str(x) for x in disorder_stress.index]
values = disorder_stress.values

highest_label = labels[0]
highest_value = values[0]
lowest_label = labels[-1]
lowest_value = values[-1]

print("Zanimljiv info:")
print(
	f"Najveci prosjecni stress level imaju osobe sa '{highest_label}' (avg {highest_value:.2f})."
)
print(
	f"Najmanji prosjecni stress level imaju osobe sa '{lowest_label}' (avg {lowest_value:.2f})."
)

plt.figure(figsize=(8, 4))
plt.bar(labels, values, color=["#d62728", "#ff7f0e", "#2ca02c"][: len(labels)])
plt.title("Average Stress Level by Sleep Disorder")
plt.xlabel("Sleep Disorder")
plt.ylabel("Average Stress Level")
plt.tight_layout()
plt.show()
