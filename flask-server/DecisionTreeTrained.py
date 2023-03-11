import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer

# Load the cleaned article data from the CSV file
df = pd.read_csv('D:\\Python Projects\\Fake-News-Detection-Application\\articles\\articleClean.csv')

# Load the trained count vectorizer and logistic regression model from disk
vectorizer = joblib.load('count_vectorizerDT.joblib')
DT = joblib.load('decision_tree_model.joblib')

# Transform the text data using the new vectorizer
X = vectorizer.transform(df['text'])

# Make predictions on the document-term matrix
y_pred = DT.predict(X)

# Loop over the predictions and print whether each one is positive or negative
for prediction in y_pred:
    if prediction == 1:
        DecisionTreeScore="Positive prediction"
        print(DecisionTreeScore)
       
    else:
        DecisionTreeScore="Negative prediction"
        print(DecisionTreeScore)
        