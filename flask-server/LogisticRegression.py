import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.metrics import recall_score, classification_report
from sklearn.feature_extraction import text
from sklearn.model_selection import train_test_split

# load the dataset
df = pd.read_csv("D:/Python Projects/Fake-News-Detection-Application/DataSets/Data Set/Clean.csv")

# split the dataset into training and testing sets
# set random_state to some arbitrary number to get the same split each time
# set test_size to the percentage of data you want to allocate to the test set
train, test = train_test_split(df, test_size=0.2, random_state=42)

# convert text to vectors using count vectorizer
stop_words = text.ENGLISH_STOP_WORDS.union(['a', 'an', 'and', 'the', 'in', 'is', 'it', 'of', 'that', 'to', 'was', 'with'])
vectorizer = CountVectorizer(token_pattern=r'\b\w+\b', stop_words=stop_words)
train_matrix = vectorizer.fit_transform(train['text'])
test_matrix = vectorizer.transform(test['text'])

# prepare the input and output variables for the logistic regression model
x_train = train_matrix
x_test = test_matrix
y_train = train['status']
y_test = test['status']

# train a logistic regression model with a fixed maximum number of iterations to avoid convergence warnings
lr = LogisticRegression(max_iter=500)
lr.fit(x_train, y_train)

# save the count vectorizer and logistic regression model for later use
joblib.dump(vectorizer, 'count_vectorizerLR.joblib')
joblib.dump(lr, 'logistic_regression_model.joblib')

# make predictions on the test set
#prediction=lr.predict(x_test)


#new = np.asarray(y_test)
#confusion_matrix(prediction,y_test)


#print(classification_report(prediction,y_test))

#1. Precision: Percentage of correct positive predictions relative to total positive predictions.

#2. Recall: Percentage of correct positive predictions relative to total actual positives.

#3. F1 Score: A weighted harmonic mean of precision and recall. The closer to 1, the better the model.

# evaluate the performance of the model using recall score and classification report
#LogisticRegressionScore= recall_score(y_test, prediction)
# print("Logistic Regression Recall Score: ", LogisticRegressionScore)
# print(classification_report(y_test, prediction))





