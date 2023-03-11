import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer

# Load the cleaned article data from the CSV file
df = pd.read_csv('D:\\Python Projects\\Fake-News-Detection-Application\\articles\\articleClean.csv')

# Load the trained count vectorizer and logistic regression model from disk
vectorizer = joblib.load('count_vectorizerLR.joblib')
lr = joblib.load('logistic_regression_model.joblib')

# Transform the text data using the new vectorizer
X = vectorizer.transform(df['text'])

# Make predictions on the document-term matrix
y_pred = lr.predict(X)

# Loop over the predictions and print whether each one is positive or negative
for prediction in y_pred:
    if prediction == 1:
        LogisticRegressionScore ="Positive prediction"
        print(LogisticRegressionScore)

    else:
        
        LogisticRegressionScore ="Negative prediction"
        print(LogisticRegressionScore)