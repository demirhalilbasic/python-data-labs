import pandas as pd
from matplotlib import pyplot as plt

# Load dataset
df = pd.read_csv("../PythonDataLab2/src/ufo_sightings.csv", low_memory=False)

# Convert datetime column
df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")

# Extract hour
df["hour"] = df["datetime"].dt.hour

# Count sightings per hour
hour_counts = df["hour"].value_counts().sort_index()
hour_counts.plot(kind="bar")

# Plot
hour_counts.plot()
plt.title("UFO Sightings by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Sightings")
plt.grid(True)

plt.show()