import pandas as pd

edges = pd.read_csv("src/network_edges.csv")
print(edges.isnull().sum())

edges_clean = edges.dropna(subset=["ring_id"])
print(edges_clean.shape)

print(edges_clean["shared_type"].value_counts())

print(edges_clean["ring_id"].value_counts().head(5))