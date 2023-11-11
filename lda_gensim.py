import gensim
from gensim import corpora
from gensim.models import LdaModel

sentences = [

    "World War II, spanning from 1939 to 1945, involved global powers in a conflict that reshaped the political and social landscape.",
    "The war's devastating impact included widespread destruction, loss of millions of lives, and the emergence of new technologies for warfare.",
    "Key events such as the invasion of Normandy and the bombing of Hiroshima and Nagasaki remain pivotal moments in the war's history.",
    "Alliances between major powers, including the Axis and the Allies, shaped the direction and outcome of the conflict.",
    "The war's aftermath led to the establishment of international organizations like the United Nations, aiming to prevent such catastrophic conflicts in the future.",

]

documents_list = [doc.split() for doc in sentences]
dictionary = corpora.Dictionary(documents_list)
corpus = [dictionary.doc2bow(doc) for doc in documents_list]
lda_model = LdaModel(corpus, num_topics=10, id2word=dictionary)

index = 0

topic = lda_model.print_topics(num_topics=50, num_words=50)[index]
words = topic[1].split(' + ')
topic_words = [word.split('*')[1].strip().strip('"') for word in words]
document = ' '.join(topic_words)

print("Topic:", document)

"""
Introduction to Gensim
Gensim is a Python library used for topic modeling, document similarity analysis, and other 
Natural Language Processing (NLP) tasks. It offers efficient algorithms and data structures to process large 
textual corpora and extract meaningful information from them. In this section apply Gensim in your application as 
described if the following steps.

Topic modeling with Latent Dirichlet Allocation (LDA)
LDA is a common technique for extracting topics from a collection of documents. 
Gensim offers an efficient implementation of LDA. In this section, perform topic modeling with 
LDA using Gensim as described above

The above code performs topic modeling using the LDA algorithm from the Gensim library. 
It takes a list of sentences, splits them into individual words, creates a dictionary of unique words, 
and converts the sentences into a bag-of-words representation. The LDA model is then trained on the corpus, 
and printing of specific extracted topic based on the given index. The code allows for topic modeling analysis on the given documents.
"""
