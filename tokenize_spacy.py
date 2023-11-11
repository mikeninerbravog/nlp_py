import spacy

nlp = spacy.load('en_core_web_sm')

file = nlp(u'Python is one of the easy programming languages to learn.')

print([w.text for w in file])

"""
Tokenization
The initial action carried by any NLP application on a text is parsing that text into tokens. 
The text can exist in the form of words, numbers, or punctuation marks. 
Tokenization is the first operation because all the other operations require existing tokens in place. 
Implement spaCy tokenization as described in the steps below.

"""