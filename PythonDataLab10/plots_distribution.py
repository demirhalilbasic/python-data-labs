import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("src/imdb_top_1000.csv")

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

sns.histplot(data=df, x="IMDB_Rating", bins=20, ax=axes[0],
             color="steelblue")
axes[0].set_title("Histogram")

sns.kdeplot(data=df, x="IMDB_Rating", ax=axes[1],
            color="coral", fill=True)
axes[1].set_title("KDE plot")

sns.histplot(data=df, x="IMDB_Rating", bins=20, ax=axes[2],
             kde=True, color="teal")
axes[2].set_title("Histogram + KDE")

plt.tight_layout()
plt.show()