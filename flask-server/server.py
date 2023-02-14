from flask import Flask
from DecisionTree import DecisionTreeScore
from LogisticRegression import LogisticRegressionScore
from RandomForest import RandomForestScore



app= Flask (__name__)

# Score API Route


@app.route("/score")

def score():

    return {"Score":["Decision Tree Score:",DecisionTreeScore,"LogisticRegression Score:",LogisticRegressionScore,"Random Forest Score:",RandomForestScore]}

if __name__ == "__main__":
     app.run(debug=True)