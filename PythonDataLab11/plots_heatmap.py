import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

sns.set_theme(style="whitegrid")
df = sns.load_dataset("penguins")

corr_df = df[["flipper_length_mm", "body_mass_g"]].dropna()
r, p = stats.pearsonr(corr_df["flipper_length_mm"], corr_df["body_mass_g"])
print(f"r = {r:.3f}, p = {p:.4f}")

fig, ax = plt.subplots(figsize=(7, 5))
sns.regplot(data=df, x="flipper_length_mm", y="body_mass_g", ax=ax, scatter=False, color="gray")
sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species", ax=ax)
plt.tight_layout()
plt.show()

corr = df.corr(numeric_only=True)
plt.figure(figsize=(7, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.tight_layout()
plt.show()

sns.pairplot(df, hue="species", diag_kind="kde")
plt.show()