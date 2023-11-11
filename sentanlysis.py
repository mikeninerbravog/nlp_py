import spacy
from nltk.sentiment import SentimentIntensityAnalyzer

nlp = spacy.load("en_core_web_sm")

sia = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    doc = nlp(text)
    sentiment_scores = sia.polarity_scores(text)
    combined_score = sentiment_scores["compound"]

    if combined_score >= 0.05:
        return "positive feedback"

    elif combined_score <= -0.05:
        return "negative feedback"

    else:
        return "neutral feedback"


review = "Disgusting one"

"""

Try also these two sentences to see difference in the output:

I love this movie. It's stunning.

I hated the movie.

"""

sentiment = analyze_sentiment(review)

print("Your review is a", sentiment)

"""
Perform Sentiment Analysis Using NLTK and spaCy
To perform sentiment analysis, combine NLTK and spaCy to leverage the strengths of both libraries as described below.

"""