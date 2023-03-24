# Import required libraries
import pandas as pd  # For data manipulation and analysis
import re  # For regular expressions
import string  # For string operations

# Read in the fake and true news datasets as separate dataframes
df_fake = pd.read_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set\Fake.csv")
df_true = pd.read_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set\True.csv")

# Print the first five rows of both dataframes
df_fake.head()
df_true.head()

# Add a new column to the fake dataframe called "Status" with the value "Fake"
df_fake["Status"]="Fake"
# Add a new column to the true dataframe called "Status" with the value "True"
df_true["Status"]="True"

# Print the first five rows of both dataframes with the new columns included
df_fake.head()
df_true.head()

# Concatenate the two dataframes into a single dataframe called "df_all"
frames=[df_true,df_fake]
df_all=pd.concat(frames)

# Print the first five rows of the combined dataframe
df_all.head()

# Save the dataframe to a CSV file called "All.csv" in the specified directory
df_all.to_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set\All.csv", encoding="UTF-8", index=False)

# Define a function to preprocess text data
def wordopt(text):
    text = text.lower()  # Convert text to lowercase
    text = re.sub('\[.*?\]', '', text)  # Remove text within square brackets
    text = re.sub("\\W"," ",text)  # Replace non-word characters with space
    text = re.sub('https?://\S+|www\.\S+', '', text)  # Remove URLs
    text = re.sub('<.*?>+', '', text)  # Remove HTML tags
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)  # Remove punctuation
    text = re.sub('\n', '', text)  # Remove newline characters
    text = re.sub('\w*\d\w*', '', text)  # Remove words containing digits
    return text

# Apply the preprocessing function to the "text" column of the combined dataframe
df_all["text"] = df_all["text"].apply(wordopt)

# Create a new dataframe called "df" with only the "text" and "Status" columns from the combined dataframe
df=df_all[["text","Status"]].copy()

# Replace the values in the "Status" column with integers (1 for "True" and 0 for "Fake")
df["Status"]= df["Status"].replace({"True" : 1, "Fake" : 0})

# Rename the "Status" column to "status"
df=df.rename(columns={"Status":"status"})

# Save the cleaned dataframe to a CSV file called "Clean.csv" in the specified directory
df.to_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set\Clean.csv", encoding="UTF-8", index=False)
