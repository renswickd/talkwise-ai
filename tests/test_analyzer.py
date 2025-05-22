import pytest
from app.analyzer import compute_sentiment

def test_compute_sentiment_positive():
    text = "I absolutely loved the presentation!"
    result = compute_sentiment(text)
    assert isinstance(result, dict)
    assert "label" in result and "score" in result
    assert result["label"] in {"POSITIVE", "NEGATIVE", "NEUTRAL"}
    assert 0.0 <= result["score"] <= 1.0
    assert result["label"] == "POSITIVE"  