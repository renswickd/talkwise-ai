from collections import Counter
import numpy as np
import pandas as pd
import spacy
from utils.common_functions import read_yaml
from app.parser import parse_transcript
from app.analyzer import compute_sentiment, compute_filler_ratio

nlp = spacy.load("en_core_web_sm")
CONFIG = read_yaml()
FILLER_WORDS = set(CONFIG["FILLER_WORDS"])

def prepare_per_turn_dataframe(transcript: list[dict]) -> pd.DataFrame:
    """
    Prepares a DataFrame with per-turn analysis.
    """
    df = pd.DataFrame(transcript)
    df['sentiment'] = df['utterance'].apply(lambda x: compute_sentiment(x)['label'])
    df['filler_ratio'] = df['utterance'].apply(compute_filler_ratio)
    return df

def compute_summary_stats(transcript_data: list[dict]) -> dict:
    df  = prepare_per_turn_dataframe(transcript_data)
    # print("hello\n\n")
    print(df.head(5))
    
    # Speaker stats
    speakers = df['speaker'].unique().tolist()
    num_turns = len(df)  

    # Sentiment counts
    sentiment_counts = df['sentiment'].value_counts().to_dict()
    
    # Average filler ratio
    avg_filler_ratio = round(df['filler_ratio'].mean(), 3)
    
    # Avg sentiment polarity
    df['polarity_score'] = df['sentiment'].map(lambda x: {"POSITIVE": 1, "NEUTRAL": 0, "NEGATIVE": -1}.get(x, 0))
    avg_polarity = round(df['polarity_score'].mean(), 3)
    
    # Frequent filler words
    filler_counter = Counter()
    for text in df['utterance']:
        doc = nlp(text)
        for token in doc:
            if token.text.lower() in FILLER_WORDS:
                filler_counter[token.text.lower()] += 1
    top_fillers = filler_counter.most_common(5)

    return {
        "speakers": speakers,
        "num_turns": num_turns,
        "sentiment_distribution": sentiment_counts,
        "avg_filler_ratio": avg_filler_ratio,
        "avg_sentiment_polarity": avg_polarity,
        "top_fillers": top_fillers,
    }


if __name__ == "__main__":
    # Example usage
    file_path = "data/transcript.txt"
    try:
        parsed_data = parse_transcript(file_path)
        print(f"Parsed {len(parsed_data)} turns from the transcript.")
        print("Sample output:")
        print(parsed_data[:5])  # Print first 5 entries

        prepare_parsed_data = prepare_per_turn_dataframe(parsed_data)
        summary_stats = compute_summary_stats(parsed_data)
        print("\n\nSummary Statistics:")
        print(summary_stats)

    except Exception as e:
        print(f"Error in: {e}")
