import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("../PythonDataLab2/src/ufo_sightings.csv", low_memory=False)

# Clean coordinates
df["latitude"]  = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")
df = df.dropna(subset=["latitude", "longitude"])
fig = go.Figure()

fig.add_trace(go.Scattergeo(
    lon=df["longitude"],
    lat=df["latitude"],
    text=df["city"],
    marker=dict(
        size=3,
        opacity=0.7,
    )
))

fig.update_layout(
    title="Global UFO Sightings",
    geo=dict(
        projection_type="orthographic",
        showland=True,
        landcolor="rgb(217, 217, 217)",
        showocean=True,
        oceancolor="rgb(205, 229, 255)",
    )
)

fig.show()