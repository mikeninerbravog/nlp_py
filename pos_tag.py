import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('averaged_perceptron_tagger')

sentence = "The dog is barking at the visitor."

tokens = word_tokenize(sentence)

pos_tags = pos_tag(tokens)

for token, pos_tag in pos_tags:
    print(f"{token}: {pos_tag}")

"""
Part-of-Speech Tagging in NLTK
Part-of-speech (POS) tagging is the process of assigning grammatical labels to each word in a sentence. 
The NLTK (Natural Language Toolkit) library provides various methods and resources for performing POS tagging. 
It offers pre-trained taggers for different languages and allows for training custom taggers on annotated corpora. 
In this section, perform POS tagging in NLTK as described above.
"""