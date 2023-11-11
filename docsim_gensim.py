from gensim import corpora, similarities
from gensim.utils import simple_preprocess

documents = [
    "World War II, spanning from 1939 to 1945, involved global powers in a conflict that reshaped the political and social landscape.",
    "The war's devastating impact included widespread destruction, loss of millions of lives, and the emergence of new technologies for warfare.",
    "Key events such as the invasion of Normandy and the bombing of Hiroshima and Nagasaki remain pivotal moments in the war's history.",
    "Alliances between major powers, including the Axis and the Allies, shaped the direction and outcome of the conflict.",
    "The war's aftermath led to the establishment of international organizations like the United Nations, aiming to prevent such catastrophic conflicts in the future.",

]

tok_docs = [simple_preprocess(doc) for doc in documents]

dictionary = corpora.Dictionary(tok_docs)

corpus = [dictionary.doc2bow(doc) for doc in tok_docs]

id = similarities.MatrixSimilarity(corpus)

query = [
    "World War II, a global conflict spanning from 1939 to 1945, had far-reaching implications, involving major powers and fundamentally altering the political and social fabric of nations worldwide. The scale of this war reshaped the very essence of societal structures and international relations.",
    "The war's impact was nothing short of devastating, leaving behind a trail of widespread destruction, claiming millions of lives and catalyzing the development of innovative technologies designed for the battlefield. The emergence of these technologies drastically altered the nature of warfare and its potential consequences.",
    "Monumental events such as the invasion of Normandy and the catastrophic bombings of Hiroshima and Nagasaki stand as pivotal, defining moments in the narrative of World War II. These instances not only altered the course of the war but continue to shape our historical understanding of it.",
    "Donald Duck is so nervous. Duff Duck the same.",
    "In the aftermath of the war, the world faced a crucial turning point. The establishment of international organizations, such as the United Nations, became an imperative step towards global cooperation, aiming to prevent the recurrence of such catastrophic conflicts and to foster international peace and stability.",
]

query_bow = dictionary.doc2bow(simple_preprocess(' '.join(query)))

familiar_docs = id[query_bow]

print(familiar_docs)

"""
Document Similarity and Indexing
Gensim offers document similarity and build document indexes for efficient retrieval. 
Create an application that computes document similarity using Gensim as described in the steps above.

The above script tokenizes a list of documents, creates a bag-of-words corpus, and initializes a similarity index. 
It also defines query documents, tokenizes them, and retrieves similar documents based on the query. 
By applying tokenization, bag-of-words representation, and the similarity index, the application finds 
similar documents to a given query.
"""
