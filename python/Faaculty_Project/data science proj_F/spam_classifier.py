import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import nltk
import re
import string



# stopwords

stop = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", 
    "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", 
    "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", 
    "their", "theirs", "themselves", "what", "which", "who", "whom", "this", 
    "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", 
    "being", "have", "has", "had", "having", "do", "does", "did", "doing", 
    "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
    "while", "of", "at", "by", "for", "with", "about", "against", "between", 
    "into", "through", "during", "before", "after", "above", "below", "to", 
    "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", 
    "further", "then", "once", "here", "there", "when", "where", "why", 
    "how", "all", "any", "both", "each", "few", "more", "most", "other", 
    "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", 
    "too", "very", "can", "will", "just", "don", "should", "now"
])



# تحميل الموارد الأساسية

import warnings 
warnings.filterwarnings('ignore')

data=pd.read_csv(r'spam.CSV',encoding='latin1')


####################################################################################################################
##############     EXPLORE DATA


data.head()
data.tail()
data.sample(10)
print (data.shape)
#data.info()


data.duplicated().sum()
data.isna().sum()

#########################################################

###########     CLEANING DATA      ##################


data=data.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'])

data=data.rename(columns={'v1':'Target','v2':'Text'})
data=data.drop_duplicates(keep='first')
data.duplicated().sum()
data.isnull().sum()

data['Target'].replace({'ham':1,'spam':0},inplace=True)

############################################################
################   DATA ANALYSIS  ##########################


data.Target.value_counts().plot.pie(autopct='%.1f%%')

plt.show()

data['Num_Char']=data['Text'].apply(len)


data['Word_Num'] = data['Text'].apply(lambda x: len(str(x).split()))
data['Sent_num'] = data['Text'].apply(lambda x: str(x).count('.') + str(x).count('!') + str(x).count('?'))




sns.histplot(data[data['Target']==0]['Num_Char'],binwidth=100,kde=True,label='spam')
plt.legend()
plt.title('Count Of Char By Spam Massages')
plt.show()

df=data[['Target','Num_Char','Word_Num','Sent_num']]
cor=df.corr()
sns.heatmap(cor,annot=True,linewidth=1)
plt.show()


#############################################################
#################           DATA PROCESSING     #############





def Process(text):

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = re.split(r'\s+', text)
    clean_tokens = [word for word in tokens if word not in stop and word.strip() != '']
    return ' '.join(clean_tokens)

data['New_Text']=data['Text'].apply(Process)


##############################################################
#################        DATA MODELING          ####################

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer

cv=CountVectorizer()
tf=TfidfVectorizer()

x=cv.fit_transform(data['New_Text']).toarray()

y=data.Target.values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=40)

from sklearn.naive_bayes import GaussianNB , MultinomialNB , BernoulliNB
from sklearn.metrics import accuracy_score , precision_score , f1_score , confusion_matrix

gnb=GaussianNB()
mnb=MultinomialNB()
bnb=BernoulliNB()

model_names=['GaussianNB','MultinomialNB','BernoulliNB']
score=[]
preci=[]
f1=[]

def model(mo):
    mo.fit(x_train,y_train)
    pred=mo.predict(x_test)
    score.append(accuracy_score(pred,y_test))
    preci.append(precision_score(pred,y_test))
    f1.append(precision_score(pred,y_test))
    print(confusion_matrix(pred,y_test))


model(gnb)
model(mnb)
model(bnb)


ndf=pd.DataFrame({'Models_name':model_names,'Accuracy':score,'Precision':preci,'f1':f1})
print(ndf)


ndf.plot(x='Models_name',y=['Accuracy','Precision'],kind='bar')
plt.show()


import pickle
pickle.dump(cv,open('Victorize.pkl','wb'))
pickle.dump(mnb,open('Model.pkl','wb'))
