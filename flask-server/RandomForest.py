import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.metrics import recall_score, classification_report
from sklearn.feature_extraction import text
from sklearn.model_selection import train_test_split

# load the dataset
df = pd.read_csv("D:/Python Projects/Fake-News-Detection-Application/DataSets/Data Set/Clean.csv")

# perform train-test split with a fixed random seed of 42
train, test = train_test_split(df, test_size=0.2, random_state=42)

# convert text to vectors using count vectorizer
stop_words = text.ENGLISH_STOP_WORDS.union(['a', 'an', 'and', 'the', 'in', 'is', 'it', 'of', 'that', 'to', 'was', 'with'])
vectorizer = CountVectorizer(token_pattern=r'\b\w+\b', stop_words=stop_words)
train_matrix = vectorizer.fit_transform(train['text'])
test_matrix = vectorizer.transform(test['text'])

# prepare the input and output variables for the random forest classifier
x_train = train_matrix
x_test = test_matrix
y_train = train['status']
y_test = test['status']

# train a random forest classifier with a fixed random seed of 42
RFC = RandomForestClassifier(random_state=42)
RFC.fit(x_train, y_train)

# save the count vectorizer and random forest classifier models for later use
joblib.dump(vectorizer, 'count_vectorizerRFC.joblib')
joblib.dump(RFC, 'random_forest_model.joblib')


# make predictions on the test set
#prediction = RFC.predict(x_test)


#RFC.score(x_test, y_test)


#print(classification_report(y_test, prediction))

#1. Precision: Percentage of correct positive predictions relative to total positive predictions.

#2. Recall: Percentage of correct positive predictions relative to total actual positives.

#3. F1 Score: A weighted harmonic mean of precision and recall. The closer to 1, the better the model.

# evaluate the performance of the model using recall score and classification report
#RandomForestScore= recall_score(y_test, prediction)
#print("Random Forest Recall Score: ", RandomForestScore)
#print(classification_report(y_test, prediction))




