import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

sns.set_theme(style="whitegrid")
df = sns.load_dataset("penguins")

adelie = df[df["species"] == "Adelie"]["flipper_length_mm"]
chinstrap = df[df["species"] == "Chinstrap"]["flipper_length_mm"]

t, p = stats.ttest_ind(adelie, chinstrap)
print(f"t = {t:.3f}, p = {p:.4f}")

zajednicki = np.sqrt((adelie.std()**2 + chinstrap.std()++2) / 2)
d = (adelie.mean() - chinstrap.mean()) / zajednicki
print(f"Choenov d = {d:.3f}")

sns.barplot(data=df, x="species", y="flipper_length_mm", capsize=0.1)
plt.title("Srednja duljina peraje po vrsti (95% CI)")
plt.show()