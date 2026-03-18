import pandas as pd

df = pd.read_csv("src/Sleep_health_and_lifestyle_dataset.csv", low_memory=False)

filtered_rows = []
for _, row in df.iterrows():
    if row["Gender"] == "Female" and row["Age"] > 30 and row["Stress Level"] > 7:
        filtered_rows.append(row)

filtered = pd.DataFrame(filtered_rows)

print(filtered[["Gender", "Age", "Stress Level", "Occupation"]])
