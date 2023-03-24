# import necessary modules
import csv
import re
import string

# function to clean text
def wordopt(text):
    text = re.sub('\[.*?\]', '', text) # remove text within square brackets
    text = re.sub("\\W"," ",text) # replace non-alphanumeric characters with whitespace
    text = re.sub('https?://\S+|www\.\S+', '', text) # remove URLs
    text = re.sub('<.*?>+', '', text) # remove HTML tags
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # remove punctuation
    text = re.sub('\n', '', text) # remove newlines
    text = re.sub('\w*\d\w*', '', text) # remove words containing digits
    return text

# open output file for writing cleaned data
with open('./articles/articleClean.csv', 'w', newline='', encoding='utf-8') as output_file:
    # create csv writer object
    writer = csv.writer(output_file)
    # write header row
    writer.writerow(['title', 'text'])

    # open input file for reading
    with open('./articles/article.csv', 'r', newline='', encoding='utf-8') as input_file:
        # create csv reader object
        reader = csv.reader(input_file)
        next(reader) # skip header row
        # iterate over rows in input file
        for row in reader:
            # extract title and text from current row
            title, text = row
            # clean text using wordopt function
            text = wordopt(text)
            # write cleaned title and text to output file
            writer.writerow([title, text])