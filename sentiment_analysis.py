# 3. Sentiment Analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text: str) -> str:
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    compound_score = scores['compound']

    # Classify sentiment
    if compound_score > 0.2:
        return "Positive"
    elif compound_score < -0.2:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    text = "The product launch was a huge success, and customers loved it!"
    sentiment = analyze_sentiment(text)
    print("Sentiment (VADER):", sentiment)
