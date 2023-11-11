from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["talking", "ate", "play", "played", "playing", "home"]
word_stem = [stemmer.stem(word) for word in words]

for word, stemmed_word in zip(words, word_stem):
    print(f"{word} -:: {stemmed_word}")

"""
Stemming in NLTK
Stemming is an NLP process that reduces words to their base form, known as a stem. 
The purpose of stemming is to normalize words by removing suffixes and prefixes. 
This allows treating variations of a word as the same word. 
NLTK provides various stemmers for different languages and Porter stemmer is one of the most used variants. 
In this section, perform stemming using the Porter stemmer in NLTK as described above.
"""