from pathlib import Path
import csv

import openpyxl
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"
excel_path = SRC_DIR / "Test.xlsx"
csv_path = SRC_DIR / "Test_2.csv"

excel = openpyxl.load_workbook(excel_path)
sheet = excel.active

with csv_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    for row in sheet.rows:
        writer.writerow([cell.value for cell in row])

df = pd.read_csv(str(csv_path))

print(df)