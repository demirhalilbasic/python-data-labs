import pandas as pd
from matplotlib import pyplot as plt

# Load dataset
df = pd.read_csv("../PythonDataLab2/src/ufo_sightings.csv", low_memory=False)

# Clean coordinates
df["latitude"]  = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
df = df.dropna(subset=["latitude", "longitude"])

# Optional: reduce dataset for faster plotting
df = df.sample(15000)
plt.figure(figsize=(12, 6))
plt.hexbin(
    df["longitude"],
    df["latitude"],
    gridsize=70,
    cmap="inferno",
    mincnt=1
)

plt.colorbar(label="Sightings density")
plt.title("UFO Sightings Density Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()