from app.metrics import compute_summary_stats, prepare_per_turn_dataframe

sample_data = [
    {"speaker": "A", "utterance": "Um, I think we should go.", "sentiment": "NEUTRAL", "confidence": 0.85, "filler_ratio": 0.2},
    {"speaker": "B", "utterance": "Yeah, like totally agree!", "sentiment": "POSITIVE", "confidence": 0.95, "filler_ratio": 0.3},
    {"speaker": "A", "utterance": "You know, it's a good idea.", "sentiment": "POSITIVE", "confidence": 0.88, "filler_ratio": 0.25}
]

def test_summary_stats_output():
    stats = compute_summary_stats(sample_data)
    assert stats["num_turns"] == 3
    assert set(stats["speakers"]) == {"A", "B"}
    assert "POSITIVE" in stats["sentiment_distribution"]
    assert isinstance(stats["avg_filler_ratio"], float)
    assert isinstance(stats["avg_sentiment_polarity"], float)
    assert len(stats["top_fillers"]) <= 5

def test_prepare_per_turn_df():
    df = prepare_per_turn_dataframe(sample_data)
    assert df.shape[0] == 3
    assert all(col in df.columns for col in ["speaker", "utterance", "sentiment", "filler_ratio"])
