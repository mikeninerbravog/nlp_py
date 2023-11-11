"""
The code demonstrates how to perform lemmatization using the spaCy library in Python.
Lemmatization involves reducing words to their base or dictionary form.
"""

#  This line imports the spaCy library, enabling you to use its functionalities for natural language processing.
import spacy

#  This line loads the English language model `en_core_web_sm` provided by spaCy.
#  This model contains pre-trained word vectors and supports various NLP tasks.
nlp = spacy.load("en_core_web_sm")

# These are two sample phrases that you'll be analyzing and lemmatizing using the spaCy model.
phrase1 = "John Doe coded for 5 hours without taking a break"
phrase2 = "Taking takes take took adjustable ability meeting better"

# These lines use the spaCy model to process the text in `phrase1` and `phrase2`, creating spaCy `Doc` objects
# (`doc1` and `doc2`) that contain information about the words, their parts of speech, lemmatized forms, etc.
doc1 = nlp(phrase1)
doc2 = nlp(phrase2)

# These loops iterate through each token in `doc1` and `doc2` respectively.
# For each token, it prints the original text and its corresponding lemma (base form).
for token in doc1:
    print(token.text, " | ", token.lemma_)

for token in doc2:
    print(token.text, " | ", token.lemma_)

"""
Lemmatization
A lemma serves as the fundamental form of a token. 
It represents how the token would appear if included in a dictionary. 
Lemmatization is the procedure of converting word forms to their respective lemmas. 
Perform lemmatization using spaCy as described in the following steps.
"""
