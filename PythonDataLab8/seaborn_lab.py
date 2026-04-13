import seaborn as sns
import pandas as pd

def main() -> None:
	tips = sns.load_dataset("tips")

	print("Prvih 5 redova:")
	print(tips.head())

	print("\nZbir i prosjek total_bill i tip po danu:")
	summary = tips.groupby("day")[["total_bill", "tip"]].agg(["sum", "mean"])
	print(summary)

	print("\nPronalazenje najboljeg izvodjaca:")
	summary2 = tips.groupby('day')['total_bill'].sum().idxmax()
	print(summary2)

	print("\nPivot table:")
	summary3 = pd.pivot_table(tips, index="day", columns="time", values=["total_bill", "tip", "size"], aggfunc="mean")
	print(summary3)

if __name__ == "__main__":
	main()
