import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("src/recruitment_data.csv")
print("Shape:", df.shape)
df.head()

df.info()
df.describe()
df.isnull().sum()

gender_map  = {0: "M", 1: "Ž"}
edu_map     = {1: "Bach-1", 2: "Bach-2", 3: "Master", 4: "Phd"}
strat_map   = {1: "Strategija 1", 2: "Strategija 2", 3: "Strategija 3"}
hire_map    = {0: "Odbijen", 1: "Zaposlen"}

view = df.copy()
view["GenderLabel"] = view["Gender"].map(gender_map)
view["HireLabel"] = view["HiringDecision"].map(hire_map)
view["StratLabel"] = view["RecruitmentStrategy"].map(strat_map)

df.groupby("HiringDecision")["Age"].mean()
df.groupby("Gender")["HiringDecision"].mean()

sns.boxplot(data=view, x="HireLabel", y="ExperienceYears")
plt.title("Godine iskustva: zaposleni vs odbijeni")
plt.show()

df.groupby("EducationLevel")["HiringDecision"].mean()

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)

sns.scatterplot(data=view, x="InterviewScore", y="SkillScore",
                hue="HireLabel", alpha=0.6)
plt.title("InterviewScore vs SkillScore: zaposleni vs odbijeni")
plt.show()

sns.boxplot(data=view, x="StratLabel", y="InterviewScore",
            hue="HireLabel")
plt.title("InterviewScore po strategiji i odluci o zapošljavanju")
plt.show()

sns.histplot(df["Age"], kde=True, bins=15)
plt.title("Raspodjela godina kandidata")
plt.show()

sns.histplot(df["DistanceFromCompany"], kde=True, bins=20)
plt.title("Raspodjela udaljenosti od kompanije")
plt.show()

sns.histplot(data=view, x="PersonalityScore",
             hue="StratLabel", element="step", kde=True)
plt.title("Raspodjela PersonalityScore po strategiji regrutacije")
plt.show()

edu_share = df["EducationLevel"].value_counts(normalize=True) * 100
edu_share.plot(kind="pie", autopct="%1.1f%%")
plt.title("Raspodjela znanja")
plt.show()

start_hire = df.groupby("RecruitmentStrategy")["HiringDecision"] \
    .value_counts(normalize=True).unstack() * 100
start_hire.plot(kind="bar", stacked=True)
plt.title("Udio zapošljavanja po strategiji regrutacije")
plt.ylabel("Postotak")
plt.show()

X = df.drop(columns=["HiringDecision"])
y = df["HiringDecision"]

rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X, y)

importances = pd.Series(rf.feature_importances_, index=X.columns) \
    .sort_values()
importances.plot(kind="barh")
plt.title("Vrijednosti vrijednosti atributa")
plt.xlabel("Vrijednost atributa")
plt.show()