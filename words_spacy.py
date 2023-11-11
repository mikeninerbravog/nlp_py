import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp("I love coding")

for token in doc:
    print(token.text, token.vector)

"""
Word Vectors
In spaCy, word vectors represent words as dense numerical vectors. 
These vectors capture the semantic meaning of words based on their contextual usage. 
spaCy provides pre-trained word vectors for different languages, including English. 
In this section, use the vector attribute of a token object to access word vectors in spaCy as described above.

"""