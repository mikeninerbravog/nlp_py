from gensim.models import Word2Vec

sentences = [

    "World War II, spanning from 1939 to 1945, involved global powers in a conflict that reshaped the political and social landscape.",
    "The war's devastating impact included widespread destruction, loss of millions of lives, and the emergence of new technologies for warfare.",
    "Key events such as the invasion of Normandy and the bombing of Hiroshima and Nagasaki remain pivotal moments in the war's history.",
    "Alliances between major powers, including the Axis and the Allies, shaped the direction and outcome of the conflict.",
    "The war's aftermath led to the establishment of international organizations like the United Nations, aiming to prevent such catastrophic conflicts in the future.",

]

model = Word2Vec(sentences, window=10, min_count=1)

vector = model.wv['War']

"""
Word Embeddings with Word2Vec
Word2Vec is an algorithm used for learning word embeddings from large text datasets. 
Gensim includes an implementation of Word2Vec that allows you to train your own word embeddings or 
load pre-trained models. Implement Word2Vec with Gensim as described below.

The above code trains a Word2Vec model using Gensim on a list of preprocessed sentences. 
It sets the parameters for vector size, window size, and minimum word frequency. 
After training the model, it allows you to access word vectors using the trained model's wv attribute. 
The code retrieves the word vector for the word AI. The application's goal is to create word embeddings 
that capture the semantic relationships and contextual meaning of words within the given sentences.
"""
