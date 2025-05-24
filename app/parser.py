import os

def parse_transcript(transcript_str: str) -> list[dict]:
    """
    Parses transcript text string into a structured list of dialogue turns.
    Each turn is expected to start with 'Speaker X:'
    """
    lines = transcript_str.strip().split('\n')
    parsed_turns = []

    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue

        if ':' not in line:
            raise ValueError(f"Malformed line at index {i + 1}: {line}")

        speaker, utterance = line.split(':', 1)
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
