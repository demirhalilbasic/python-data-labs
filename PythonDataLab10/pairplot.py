import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

df["PrviZanr"] = df["Genre"].str.split(",").str[0].str.strip()

num_cols = ["IMDB_Rating", "Meta_score", "No_of_Votes", "Runtime"]
df["Runtime"] = pd.to_numeric(
    df["Runtime"].str.replace(" min", "", regex=False), errors="coerce"
)

korelacija = df[num_cols].corr()
plot_df = df[num_cols + ["PrviZanr"]].dropna()

sns.pairplot(
    plot_df,
    hue="PrviZanr",
    palette="Set2",
    plot_kws={"alpha": 0.5, "s": 20},
)
plt.suptitle("Pairplot - IMDB Top 1000", y=1.02)
plt.show()