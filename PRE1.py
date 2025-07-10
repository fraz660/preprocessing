input = "my name faraz alam. i was born in 2005."
print("INPUT:", input)

# Lowercasing
lowercase = input.lower()
print("LOWERCASE = ", lowercase)

import re

lowercase_re = re.sub(r'1999', '2025', lowercase)  # Not found in new input
print("REGULAR EXP1 = ", lowercase_re)

lowercase_re = re.sub(r'[a-m]', '*', lowercase)
print("REGULAR EXP2 = ", lowercase_re)

lowercase_re = re.sub(r'\d', '-', lowercase)
print("REGULAR EXP3 = ", lowercase_re)

# Tokenization
import nltk
from nltk import word_tokenize, sent_tokenize

word_tokens = word_tokenize(input)
print("WORD TOKENS = ", word_tokens)
print("WORD TOKEN COUNT = ", len(word_tokens))

sent_tokens = sent_tokenize(input)
print("SENT TOKENS = ", sent_tokens)
print("SENTENCE COUNT = ", len(sent_tokens))

# Stopwords Removal
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

tokens_stopwords = []
for token in word_tokens:
    if token.lower() not in stop_words:
        tokens_stopwords.append(token)
print("WITHOUT STOPWORDS = ", ' '.join(tokens_stopwords))