# import pytest
from app.analyzer import compute_sentiment, compute_filler_ratio, sentiment_polarity

def test_compute_sentiment_positive():
    text = "I absolutely loved the presentation!"
    result = compute_sentiment(text)
    assert isinstance(result, dict)
    assert "label" in result and "score" in result
    assert result["label"] in {"POSITIVE", "NEGATIVE", "NEUTRAL"}
    assert 0.0 <= result["score"] <= 1.0
    assert result["label"] == "POSITIVE"  

def test_filler_ratio_typical():
    text = "Um, I was like totally going to do that, you know?"
    ratio = compute_filler_ratio(text)
    assert 0.0 < ratio <= 1.0

def test_filler_ratio_no_fillers():
    text = "This is a normal sentence with no filler words."
    ratio = compute_filler_ratio(text)
    assert ratio == 0.0

def test_sentiment_polarity_mapping():
    assert sentiment_polarity("POSITIVE") == 1
    assert sentiment_polarity("NEUTRAL") == 0
    assert sentiment_polarity("NEGATIVE") == -1
    assert sentiment_polarity("UNKNOWN") == 0