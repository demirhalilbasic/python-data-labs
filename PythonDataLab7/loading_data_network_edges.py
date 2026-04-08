import pandas as pd

edges = pd.read_csv("src/network_edges.csv")

print(edges.shape)
print(edges.head())
print(edges.isnull().sum())