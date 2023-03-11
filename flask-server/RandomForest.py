import pandas as pd
import random
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.metrics import recall_score 
from sklearn.metrics import classification_report


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


RFC = RandomForestClassifier(random_state=0)
RFC.fit(x_train, y_train)


joblib.dump(vectorizer,'count_vectorizerRFC.joblib')

joblib.dump(RFC,'random_forest_model.joblib')


#prediction = RFC.predict(x_test)


#RFC.score(x_test, y_test)


#print(classification_report(y_test, prediction))

#1. Precision: Percentage of correct positive predictions relative to total positive predictions.

#2. Recall: Percentage of correct positive predictions relative to total actual positives.

#3. F1 Score: A weighted harmonic mean of precision and recall. The closer to 1, the better the model.

#RandomForestScore= recall_score(y_test, prediction)

#print(RandomForestScore)




