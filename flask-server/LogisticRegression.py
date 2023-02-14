import pandas as pd
import random
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score 
from sklearn.metrics import classification_report,confusion_matrix


df=pd.read_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set\Clean.csv")
df.head()


index = df.index
df['random_number'] = [random.uniform(0, 1) for k in df.index]

train = df[df['random_number'] <= 0.8]
test = df[df['random_number'] > 0.8]

df.head()


vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')

train_matrix = vectorizer.fit_transform(train['text'])
test_matrix = vectorizer.transform(test['text'])


x_train = train_matrix
x_test = test_matrix
y_train = train['status']
y_test = test['status']


lr= LogisticRegression(max_iter=500)
lr.fit(x_train,y_train)


prediction=lr.predict(x_test)


new = np.asarray(y_test)
confusion_matrix(prediction,y_test)


#print(classification_report(prediction,y_test))

#1. Precision: Percentage of correct positive predictions relative to total positive predictions.

#2. Recall: Percentage of correct positive predictions relative to total actual positives.

#3. F1 Score: A weighted harmonic mean of precision and recall. The closer to 1, the better the model.

LogisticRegressionScore= recall_score(y_test, prediction)

print(LogisticRegressionScore)





