import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required NLTK resources (only needed once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Input (same as PRE1.py)
input = "my name faraz alam. i was born in 2005."
print("INPUT:\n", input)

# Tokenization
word_tokens = word_tokenize(input)

# POS Tagging
pos_tags = pos_tag(word_tokens)
print("\nPOS TAGS:\n", pos_tags)

# Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in word_tokens]
print("\nSTEMMED WORDS:\n", stemmed)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in word_tokens]
print("\nLEMMATIZED WORDS:\n", lemmatized)