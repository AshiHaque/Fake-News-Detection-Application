from flask import Flask, request , jsonify
from DecisionTreeTrained import DecisionTreeScore
from LogisticRegressionTrained import LogisticRegressionScore
from RandomForestTrained import RandomForestScore
from scrape import article_scraping
from newspaper import Article
import nltk

app = Flask(__name__)

stringUrl = ""


# Get Article URL API Routes

@app.route('/getArticleUrl', methods=['POST'])
def get_string():
    global stringUrl
    data = request.get_json()
    string = data['string']
    stringUrl = string
    print(stringUrl)

    article_scraping(stringUrl)
    return 'String received: ' + stringUrl


# Get Article Info API Routes

@app.route('/articleInfo', methods=['GET'])
def article_info():
    url = stringUrl
    nltk.download('punkt')

    article = Article(url)

    # Download
    article.download()

    # Basic Tasks
    article.parse()

    # Gets the author or authors of the article
    author_list = []
    for author in article.authors:
        author_list.append(author)

    date = article.publish_date

    # Gets the top image of the article
    top_image = article.top_image

    # Get the Title
    title = article.title

    # Process Article for NLP
    article.nlp()

    # Gets the article summary
    summary = article.summary

    # Create a dictionary with the article information
    article_dict = {'title': title, 'summary': summary, 'authors': author_list, 'date': date, 'top_image': top_image}

    # Return the dictionary as a JSON object
    return jsonify(article_dict)


# Score API Routes

@app.route("/score1")
def score1():
    
    if stringUrl == "":
        return "No string received"
    else:
        return {"Score": [DecisionTreeScore]}

@app.route("/score2")
def score2():
    
    if stringUrl == "":
        return "No string received"
    else:
        return {"Score": [LogisticRegressionScore]}

@app.route("/score3")
def score3():
    
    if stringUrl == "":
        return "No string received"
    else:
        return {"Score": [RandomForestScore]}

if __name__ == "__main__":
    app.run(debug=True)