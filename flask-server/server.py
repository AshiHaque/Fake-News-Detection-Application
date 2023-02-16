from flask import Flask
from DecisionTree import DecisionTreeScore
from LogisticRegression import LogisticRegressionScore
from RandomForest import RandomForestScore

app = Flask(__name__)

# Score API Routes

@app.route("/score1")
def score1():
    return {"Score": ["Decision Tree Score:", DecisionTreeScore]}

@app.route("/score2")
def score2():
    return {"Score": ["LogisticRegression Score:", LogisticRegressionScore]}

@app.route("/score3")
def score3():
    return {"Score": ["Random Forest Score:", RandomForestScore]}

if __name__ == "__main__":
    app.run(debug=True)