import pandas as pd

read_file = pd.read_excel("src/Test.xlsx")

read_file.to_csv("src/Test.csv", index=False, header=True)

df = pd.DataFrame(pd.read_csv("src/Test.csv"))

print(df)