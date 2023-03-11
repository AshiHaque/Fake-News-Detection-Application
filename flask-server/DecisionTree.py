import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import joblib
from sklearn.metrics import classification_report
from sklearn.metrics import recall_score 
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import text
from sklearn.model_selection import train_test_split

# load the data from the CSV file into a Pandas DataFrame
df=pd.read_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set\Clean.csv")
df.head()

# create a CountVectorizer object to convert the text data into a matrix of word frequencies
stop_words = text.ENGLISH_STOP_WORDS.union(['a', 'an', 'and', 'the', 'in', 'is', 'it', 'of', 'that', 'to', 'was', 'with'])
vectorizer = CountVectorizer(token_pattern=r'\b\w+\b', stop_words=stop_words)
text_matrix = vectorizer.fit_transform(df['text'])
status = df['status']

# split the data into training and testing sets using the train_test_split function
# the test size is set to 0.2, which means 20% of the data is used for testing and 80% is used for training
# the random_state parameter is set to 42 so that the split is the same each time the code is run
x_train, x_test, y_train, y_test = train_test_split(text_matrix, status, test_size=0.2, random_state=42)

# create a decision tree classifier object and train it on the training data
DT = DecisionTreeClassifier()
DT.fit(x_train, y_train)

# save the CountVectorizer and the trained decision tree model to disk using joblib.dump
joblib.dump(vectorizer,'count_vectorizerDT.joblib')
joblib.dump(DT,'decision_tree_model.joblib')

# use the trained model to predict the target variable for the test data
#prediction=DT.predict(x_test)


#DT.score(x_test, y_test)

# calculate the recall score for the model on the test data
#DecisionTreeScore = recall_score(y_test, prediction)

# print a classification report for the model on the test data
# the classification report shows precision, recall, f1-score, and support for each class
#print(classification_report(y_test, prediction))

#1. Precision: Percentage of correct positive predictions relative to total positive predictions.

#2. Recall: Percentage of correct positive predictions relative to total actual positives.

#3. F1 Score: A weighted harmonic mean of precision and recall. The closer to 1, the better the model.

# print the recall score for the model on the test data
#print("DecisionTreeScore:", DecisionTreeScore)

