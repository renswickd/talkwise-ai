import numpy as np
import spacy
from utils.common_functions import read_yaml
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
# from config.pipeline_config import MODEL_NAME, PIPELINE_NAME, LABELS

# Load configuration
CONFIG = read_yaml()
MODEL_NAME = CONFIG['MODEL_NAME']
PIPELINE_NAME = CONFIG['PIPELINE_NAME']
LABELS = CONFIG['LABELS']
LABEL_SCORE_MAP = CONFIG['LABEL_SCORE_MAP']

nlp = spacy.load("en_core_web_sm")
FILLER_WORDS = set(CONFIG["FILLER_WORDS"])

# Tokenizer & model setup
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
sentiment_pipeline = pipeline(PIPELINE_NAME, model=model, tokenizer=tokenizer)


def compute_sentiment(text: str) -> dict:
    """
    Returns sentiment label and confidence score for given text.
    """
    result = sentiment_pipeline(text)[0]
    label = LABELS.get(result['label'], result['label'])
    score = round(result['score'], 3)
    return {"label": label, "score": score}


def compute_filler_ratio(text: str) -> float:
    """
    Calculates the ratio of filler words to total valid tokens.
    """
    doc = nlp(text)
    total_tokens = [token for token in doc if token.is_alpha]
    if not total_tokens:
        return 0

    filler_count = sum(1 for token in total_tokens if token.text.lower() in FILLER_WORDS)
    ratio = round(filler_count / len(total_tokens), 3)
    return ratio

def sentiment_polarity(label: str) -> int:
    """
    Converts sentiment label to polarity score.
    """
    return LABEL_SCORE_MAP.get(label, 0)

if __name__ == "__main__":
    # Example usage
    text = "I love programming!"
    result = compute_sentiment(text)
    print(f"Sentiment: {result['label']}, Score: {result['score']}")

    # text = "I'm not feeling with how things turned out!"
    # result = compute_sentiment(text)
    # # print(f"Sentiment: {result['label']}, Score: {result['score']}")
    # print(result)

    text = "Um, I was like totally going to do that, you know?"
    ratio = compute_filler_ratio(text)
    print(f"Filler Ratio: {ratio}")

    text = "This is a normal sentence with no filler words."
    polarity = sentiment_polarity(result['label'])
    print(f"Sentiment Polarity: {polarity}")