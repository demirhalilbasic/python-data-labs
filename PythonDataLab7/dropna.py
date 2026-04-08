import pandas as pd

edges = pd.read_csv("src/network_edges.csv")

edges_clean = edges.dropna()
print(edges_clean.shape)

edges_rings = edges.dropna(subset=["ring_id"])
print(edges_rings.shape)

# Analysis after dropna
print(edges_rings["ring_id"].nunique())

print(edges_rings["ring_id"].value_counts().head(5))

print(edges_rings["shared_type"].value_counts())