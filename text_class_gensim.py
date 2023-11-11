from gensim import corpora
from gensim.models import TfidfModel
from gensim.models import LsiModel
from gensim.models import LdaModel
from gensim import similarities
from gensim.parsing.preprocessing import preprocess_string, remove_stopwords

documents = [

    "AI is the power of the future.",
    "NLP being its AI sub field its great equipping yourself with it",
    "Allows for AI communication and interaction between human and computer.",
    "Having a vast AI field of application?"

]

labels = ["AI", "NLP"]
p_docs = [preprocess_string(doc) for doc in documents]
dictionary = corpora.Dictionary(p_docs)
corpus = [dictionary.doc2bow(doc) for doc in p_docs]
tfidf = TfidfModel(corpus)
c_tfidf = tfidf[corpus]
lsi = LsiModel(c_tfidf, id2word=dictionary, num_topics=10)
id = similarities.MatrixSimilarity(lsi[corpus])

new_phrase = "NLP changes all things."

preprocessed_new_phrase = preprocess_string(new_phrase)
new_doc_bow = dictionary.doc2bow(preprocessed_new_phrase)
new_doc_lsi = lsi[new_doc_bow]
sims = id[new_doc_lsi]
most_familiar_doc_index = sims.argmax()
most_sim_label = labels[most_familiar_doc_index]

print("Predicted label:", most_sim_label)

"""
Text Classification
Using Gensim, you can train models to classify documents into predefined categories with machine learning algorithms 
such as Support Vector Machines (SVM) or Naive Bayes. In this section, perform text classification with Gensim as described above.

The above application pre-processes a set of documents, creates a dictionary and corpus, 
and applies TF-IDF and Latent Semantic Indexing (LSI) techniques. 
To measure the similarity between documents, create a similarity index using the LSI-transformed corpus. 
Then, pre-process and convert a new document into an LSI representation. 
Compute similarity scores between the new document and existing documents using the similarity index. 
Based on the highest similarity score, identify the most similar document and assign its label to the new document.

"""
