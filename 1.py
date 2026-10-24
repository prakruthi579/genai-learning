
import nltk
from nltk.stem import PorterStemmer,RegexpStemmer,SnowballStemmer
from nltk.tokenize import word_tokenize,sent_tokenize
text="Hello everyone, welcome to the world of streamlit. Streamlit is a great tool for building interactive web applications using Python."
sentences=nltk.sent_tokenize(text)
words=nltk.word_tokenize(text)
print("Sentences:",sentences)
print("Words:",words)
stemming=PorterStemmer()
stemmed_words=[stemming.stem(word) for word in words]
print("Stemmed Words:",stemmed_words)
exp=RegexpStemmer("ing$|s$|e$|ly$|tion$")
exp_words=[exp.stem(word) for word in words]
print("Exp Stemming:",exp_words)
snowball=SnowballStemmer("english")
snowball_words=[snowball.stem(word) for word in words]
print("Snowball Stemming:",snowball_words)
