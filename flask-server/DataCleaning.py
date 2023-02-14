import pandas as pd
import re
import string


df_fake = pd.read_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set\Fake.csv") 
df_true = pd.read_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set\True.csv")


df_fake.head()


df_true.head()


df_fake["Status"]="Fake"
df_fake.head()


df_true["Status"]="True"
df_true.head()


frames=[df_true,df_fake]

df_all=pd.concat(frames)
df_all.head()


df_all.to_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set\All.csv", encoding="UTF-8", index=False)



def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text


df_all["text"] = df_all["text"].apply(wordopt)
df_all.head()


df=df_all[["text","Status"]].copy()
df.head()


df["Status"]= df["Status"].replace({"True" : 1})
df["Status"]= df["Status"].replace({"Fake" : 0})
df.head()



df=df.rename(columns={"Status":"status"})
df.head()


df.to_csv("D:/Python Projects/Fake-News-Detection-Application\DataSets\Data Set\Clean.csv", encoding="UTF-8", index=False)





