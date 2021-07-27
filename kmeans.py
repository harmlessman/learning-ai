from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
# 키와 몸무게 데이터 읽어 들이기 --- (※1)
tbl = pd.read_csv("./titanic/bmi.csv")
df = tbl.iloc[:100, :-1]
sns.lmplot('height', 'weight', data=df, fit_reg=False, scatter_kws={"s": 150})
data_points = df.values
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, init='random').fit(data_points)

kmeans.cluster_centers_
kmeans.labels_
df['cluster_id'] = kmeans.labels_
a=sns.lmplot('height', 'weight', data=df, fit_reg=False,
           scatter_kws={"s": 150},
           hue="cluster_id")
