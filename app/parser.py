import os

def parse_transcript(file_path: str) -> list[dict]:
    """
    Reads and parses a transcript file.
    Returns a list of dictionaries with 'speaker' and 'utterance'.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Transcript file not found at: {file_path}")
    
    parsed_turns = []

    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue  # skip blank lines

            if ":" not in line:
                raise ValueError(f"Malformed line (missing ':'): {line}")
            
            speaker, utterance = line.split(":", 1)
            parsed_turns.append({
                "turn": i + 1,
                "speaker": speaker.strip(),
                "utterance": utterance.strip()
            })

    return parsed_turns

def get_speakers(transcript: list[dict]) -> list[str]:
    """
    Extracts unique speakers from the transcript.
    Returns a sorted list of speaker names.
    """
    if not transcript:
        raise ValueError("Transcript is empty or not provided.")
    speakers_set = set(turn['speaker'] for turn in transcript)
    return set(sorted(speakers_set))


if __name__ == "__main__":
    # Example usage
    file_path = "data/transcript.txt"
    try:
        parsed_data = parse_transcript(file_path)
        print(f"Parsed {len(parsed_data)} turns from the transcript.")
        print("Sample output:")
        print(parsed_data[:5])  # Print first 5 entries for brevity
        # for entry in parsed_data:
        #     print(f"Turn {entry['turn']}: {entry['speaker']} says '{entry['utterance']}'")

        speakers = get_speakers(parsed_data)
        print(f"Speakers: {speakers}")
    except Exception as e:
        print(f"Error: {e}")
