import pandas as pd

edges = pd.read_csv("src/network_edges.csv")

print(edges.duplicated().sum())

print(edges.duplicated(subset=["shared_type"]).sum())

unique_a = edges.drop_duplicates(subset=["account_a"])
print(f"Svi redovi: {len(edges)}, Jedinstveni account_a: {len(unique_a)}")