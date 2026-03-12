import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("ufo_sightings.csv", low_memory=False)

shape_counts = df["shape"].value_counts().head(10)

shape_counts.plot(kind="bar")

plt.title("Most Common UFO Shapes")
plt.xlabel("Shape")
plt.ylabel("Number of Sightings")
plt.show()