import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('./titanic/mushroom.csv', na_values=['?'])

dataset.isnull().sum()

dataset = dataset.drop("stalk-root", axis=1)

x = dataset.drop('class', axis=1) # 독립변수. 학습 데이터
y = dataset['class'] # 종속변수. Label 데이터

#one hot incoding 작업
from sklearn.preprocessing import LabelEncoder
Encoder_y = LabelEncoder()
y = Encoder_y.fit_transform(y)

x = pd.get_dummies(x, columns=x.columns)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(max_depth=15, min_samples_leaf=3, n_estimators=10,
                               min_samples_split=22, random_state=0, n_jobs=-1)
model.fit(X_train, y_train)



from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, classification_report

pred = model.predict(X_test)
score = accuracy_score(y_test, pred)
print(score)
