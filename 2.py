import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
text="Hello everyone, welcome to the world of streamlit. Streamlit is a great tool for building interactive web applications using Python."
words=nltk.word_tokenize(text)
print(words)
nltk.download('stopwords')

lemmatizer=WordNetLemmatizer()
stemming_words=[lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
print("Lemmatized Words:",stemming_words)
print(' '.join(stemming_words))
nltk.download('averaged_perceptron_tagger_eng')
tag_elements=(nltk.pos_tag(stemming_words))
r=(nltk.pos_tag(("taj mahal is a beautiful monument").split()))
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
print(nltk.ne_chunk(nltk.pos_tag(("mahatma gandhi got us independence on august 15, 1947").split())))