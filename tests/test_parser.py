import pytest
from app.parser import parse_transcript, get_speakers

# ---- Positive Test Case ----

def test_parse_transcript_valid():
    result = parse_transcript("data/transcript.txt")
    assert isinstance(result, list)
    assert len(result) >= 12
    assert all("speaker" in turn and "utterance" in turn for turn in result)

def test_parse_transcript_speakers(tmp_path):
    good_file = tmp_path / "good_transcript.txt"
    good_file.write_text("""
Speaker A: Hello
Speaker B: Hi
Speaker A: How are you?
    """)
    result = parse_transcript(str(good_file))
    speakers = get_speakers(result) #set(turn['speaker'] for turn in result)
    assert speakers == {"Speaker A", "Speaker B"}

# ---- Negative Test Cases ----

def test_parse_transcript_missing_file():
    with pytest.raises(FileNotFoundError):
        parse_transcript("data/nonexistent.txt")