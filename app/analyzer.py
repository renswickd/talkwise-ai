import torch
import numpy as np
from utils.common_functions import read_yaml
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# from config.pipeline_config import MODEL_NAME, PIPELINE_NAME, LABELS
# Load configuration
config = read_yaml("config/pipeline_config.yaml")
MODEL_NAME = config['MODEL_NAME']
PIPELINE_NAME = config['PIPELINE_NAME']
LABELS = config['LABELS']


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

if __name__ == "__main__":
    # Example usage
    text = "I love programming!"
    result = compute_sentiment(text)
    print(f"Sentiment: {result['label']}, Score: {result['score']}")

    # text = "I'm not feeling with how things turned out!"
    # result = compute_sentiment(text)
    # # print(f"Sentiment: {result['label']}, Score: {result['score']}")
    # print(result)