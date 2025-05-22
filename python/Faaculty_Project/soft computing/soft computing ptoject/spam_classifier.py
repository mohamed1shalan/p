import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, f1_score, confusion_matrix
import pickle
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
path_gui = os.path.join(current_dir, "gui.py")

data = pd.read_csv(os.path.join(current_dir, "spam.csv"), encoding='latin1')

data = data.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'])
data = data.rename(columns={'v1': 'Target', 'v2': 'Text'})
data = data.drop_duplicates()
data['Target'] = data['Target'].replace({'ham': 1, 'spam': 0})

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

def Process(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = re.split(r'\s+', text)
    clean_tokens = [word for word in tokens if word not in stop and word.strip() != '']
    return ' '.join(clean_tokens)

data['Text_after_cleaning'] = data['Text'].apply(Process)

cv = CountVectorizer()
x = cv.fit_transform(data['Text_after_cleaning']).toarray() # type: ignore
y = data['Target'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=40)

model = MLPClassifier(hidden_layer_sizes=(100,50,25), activation='relu', solver='adam', max_iter=300)
model.fit(x_train, y_train)
pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, pred))
print("Precision:", precision_score(y_test, pred))
print("F1 Score:", f1_score(y_test, pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
pickle.dump(cv, open('Victorize.pkl', 'wb'))
pickle.dump(model, open('Model.pkl', 'wb'))


with open("test_data.pkl", "wb") as f:
    pickle.dump((x_test, y_test), f)
