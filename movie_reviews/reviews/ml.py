from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("RedBeam/sentiment_model")

sentiment_model = AutoModelForSequenceClassification.from_pretrained("RedBeam/sentiment_model")

stars_model = AutoModelForSequenceClassification.from_pretrained("RedBeam/stars_model")


def get_review_status(text):
    encoding = tokenizer(text, return_tensors="pt")
    sentiment_logits = sentiment_model(**encoding).logits

    stars_logits = stars_model(**encoding).logits

    sentiment = "Positive" if torch.argmax(sentiment_logits).item() == 1 else "Negative"
    stars_count = torch.argmax(stars_logits).item() + 1

    print(f"predicted sentiment: {sentiment}")
    print(f"predicted stars: {stars_count}")

    return {'sentiment': sentiment, 'stars_count': stars_count}
