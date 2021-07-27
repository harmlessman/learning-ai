import pandas as pd
import seaborn as sns

df = pd.read_csv("./titanic/newbie.csv")
feature=["who","Country", "Years on Internet"]
# 독립변수 제거
df = df.drop(df[feature], axis=1)
# 종속변수
dfy=df["Newbie"].copy()
# 평균값으로 nan값 채움
df["Age"].fillna(df["Age"].mean(), inplace=True)
# 최빈값으로 nan값 채움
df["Household Income"].fillna(df["Household Income"].mode()[0], inplace=True)
df["Sexual Preference"].fillna(df["Sexual Preference"].mode()[0], inplace=True)
df["Marital Status"].fillna(df["Marital Status"].mode()[0], inplace=True)
# 독립변수를 더미변수로 변경
col=df.columns
col.drop("Newbie")
dummie=pd.DataFrame(col)
d=pd.get_dummies(dummie)
print(d)