import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
messages=pd.read_csv('bow_tfidf_practice.csv',
                    sep=',')
print(messages.head())

nltk.download('stopwords')
wl=WordNetLemmatizer()
corpus=[]
for i in range(0,len(messages)):
    review=re.sub('[^a-zA-Z]',' ',messages['text'][i])
    review=review.lower()
    review=review.split()
    review=[wl.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)
cv=CountVectorizer(max_features=100)
X=cv.fit_transform(corpus).toarray()
print(X)
print(cv.vocabulary_)
