import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

sns.set_theme(style="whitegrid")
df = sns.load_dataset("penguins")

print(df.describe().round(2))

cols = ["body_mass_g", "bill_length_mm", "bill_depth_mm", "flipper_length_mm"]

summary = df.groupby("species")[cols].agg(["mean", "median", "std"]).round(2)
print(summary)

cv = df.groupby("species")["body_mass_g"].agg(lambda x: (x.std() / x.mean()) * 100).round(2)
print("KV (%):", cv)