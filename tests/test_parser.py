import pytest
from app.parser import parse_transcript

# ---- Positive Test Case ----

def test_parse_transcript_valid():
    result = parse_transcript("data/transcript.txt")
    assert isinstance(result, list)
    assert len(result) >= 12
    assert all("speaker" in turn and "utterance" in turn for turn in result)

# ---- Negative Test Cases ----

def test_parse_transcript_missing_file():
    with pytest.raises(FileNotFoundError):
        parse_transcript("data/nonexistent.txt")