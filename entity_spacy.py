import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp(u'Germany invades Poland in 1939. United KingDom and France declares War.')

for token in doc:

    if token.ent_type != 0:
        print(token.text, token.ent_type_)

"""
Named Entity Recognition
A named entity refers to a specific object you identify by its proper name. 
They encompass individuals, organizations, locations, and other relevant entities. 
Recognizing named entities holds significance in the field of Natural Language Processing (NLP) 
as they unveil the specific place or organization of the user. In this section, 
build an application to detect named entities within the provided sample discourse as described above.
"""