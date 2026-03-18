import pandas as pd

df = pd.read_csv("src/Sleep_health_and_lifestyle_dataset.csv", low_memory=False)

high_stress = df[df["Stress Level"] > 7]
print(high_stress["Sleep Duration"].mean())

low_stress = df[df["Stress Level"] <= 3]
print(low_stress["Sleep Duration"].mean())