from sklearn.datasets import fetch_20newsgroups
newsdata = fetch_20newsgroups(subset='train')

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB # 다항분포 나이브 베이즈 모델
from sklearn.metrics import accuracy_score #정확도 계산
cv = CountVectorizer()
X_train_dtm = cv.fit_transform(newsdata.data)
print(X_train_dtm.shape)

model = MultinomialNB()
model.fit(X_train_dtm, newsdata.target)

newsdata_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_dtm = cv.transform(newsdata_test.data)

predicted = model.predict(X_test_dtm) #테스트 데이터에 대한 예측
print("정확도:", accuracy_score(newsdata_test.target, predicted))
