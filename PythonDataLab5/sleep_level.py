import pandas as pd

df = pd.read_csv("src/Sleep_health_and_lifestyle_dataset.csv", low_memory=False)

# Najmanje spava
print("\nNajmanje spava:")
print(df.loc[df["Sleep Duration"].idxmin()])

# Najvise spava
print("\nNajvise spava:")
print(df.loc[df["Sleep Duration"].idxmax()])

# Najvisi heart rate
print("\nNajvisi heart rate:")
print(df.loc[df["Heart Rate"].idxmax()])

# Najnizi daily steps
print("\nNajnizi daily steps:")
print(df.loc[df["Daily Steps"].idxmin()])
