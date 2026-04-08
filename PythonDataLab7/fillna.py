import pandas as pd

edges = pd.read_csv("src/network_edges.csv")

edges_filled = edges.fillna({"ring_id": "NEPOZNAT"})

print(edges_filled["ring_id"].value_counts().head(5))