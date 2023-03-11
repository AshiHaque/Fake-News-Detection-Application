import csv
import re
import string

def wordopt(text):
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

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