import pandas as pd
import re
import string


df_all = pd.read_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set3\data.csv")
df_all.head()


df = df_all[["Body", "Label"]].copy()


df.head()


df=df.rename(columns={"Body":"text"})
df.head()


df=df.rename(columns={"Label":"status"})
df.head()


df.to_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set3\All.csv", encoding="UTF-8", index=False)


df1=pd.read_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set3\AllSmall.csv")


def wordopt(text):
   
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text


df1["text"] = df1["text"].apply(wordopt)
df1.head()





