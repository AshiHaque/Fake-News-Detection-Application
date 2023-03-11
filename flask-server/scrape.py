import csv
import re
import string
import nltk
from newspaper import Article

def wordopt(text):
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

def article_scraping(url):
    # Download punkt tokenizer if not already downloaded
    nltk.download('punkt')

    news_url = url
    article = Article(news_url)

    # Download and parse the article
    article.download()
    article.parse()

    # Get the title and text of the article
    title = article.title
    text = article.text

    # Write the article title and text to a CSV file
    with open('./articles/article.csv', 'w', encoding='utf8', newline='') as a:
        thewriter = csv.writer(a)
        header = ['title', 'text']
        thewriter.writerow(header)
        thewriter.writerow([title, text])

    # Clean the article text and write to a new CSV file
    with open('./articles/articleClean.csv', 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['title', 'text'])

        with open('./articles/article.csv', 'r', newline='', encoding='utf-8') as input_file:
            reader = csv.reader(input_file)
            next(reader) # skip header row
            for row in reader:
                title, text = row
                text = wordopt(text)
                writer.writerow([title, text])