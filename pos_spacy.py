import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp(u'I have finished coding. Now I am taking a nature walk.')

for token in doc:
    print(token.text, token.pos_, token.dep_)

"""
Part-of-Speech Tagging
A tag offers information about the part-of-speech (such as noun or verb) of a specific word within a given sentence. 
It's important to note that a word can have multiple parts of speech depending on its context. In spaCy, 
part-of-speech tags offer detailed information about a token.

For instance, in verbs, they state various features like tense (past, present, or future), 
aspect (progressive or perfect), person (1st, 2nd, or 3rd), and number (singular or plural). 
Extracting these verb part-of-speech tags is useful in determining a user's intent when tokenization 
and lemmatization alone are insufficient. Apply tagging as described in the steps below.
"""