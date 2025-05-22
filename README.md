# 💬 Dialogue Insights

A self-contained NLP-powered web app that analyzes conversation transcripts for sentiment and filler-word usage. Built using Hugging Face Transformers, spaCy, and Streamlit.

---

## 🚀 Features

- 📊 Sentiment analysis per dialogue turn (Positive, Negative, Neutral)
- 🗣️ Filler word ratio (e.g., "um", "like", "uhh")
- 📈 Interactive web dashboard using Streamlit
- 📄 Custom transcript support (12–16 line dialogues)
- ⚠️ Defensive error handling for invalid or missing input
- 🔍 Sentiment analysis using CardiffNLP RoBERTa (3-class)
- 🗣️ Filler word analysis using spaCy (customizable filler list in config)

---

## 📊 Metrics & Visualizations in the Dashboard
The application analyzes the conversation transcript and presents the following metrics and visual insights in the Streamlit dashboard:

#### 🏠 Landing Summary (Always Visible)
- **Number of Turns**: Total number of dialogue lines parsed from the transcript.
- **Speakers Detected**: Unique participants (e.g., Speaker A, Speaker B).
- **Sentiment Distribution**: Count of turns classified as Positive, Neutral, or Negative.
- **Average Filler Ratio**: Average proportion of filler words (e.g., “um”, “like”) used per turn.
- **Most Frequent Filler Words**: Top 5 most commonly used filler words across all turns.
- **Average Sentiment Polarity**: Normalized sentiment score from -1 (Negative) to +1 (Positive), indicating the overall emotional tone.

#### 🔽 Per-Turn Metrics (Expandable Tab)
- **Transcript Table**: Shows each turn with speaker, utterance, sentiment label, and filler word ratio.
- **Sentiment Line Plot**: Visualizes sentiment polarity progression across the conversation.
- **Filler Ratio Bar Chart**: Highlights how frequently filler words appear per turn.
- **Sentiment Heatmap**: Displays a heatmap of sentiment confidence per turn (optional advanced view).

#### 🔽 Overall Metrics (Expandable Tab)
- **Sentiment Distribution Pie Chart**: Visual breakdown of total sentiment classes.
- **Average Filler Ratio Gauge**: Interactive gauge showing overall filler usage.
- **Speaker-wise Comparison Charts**: Visual comparison of sentiment and filler usage across speakers.
- **Word Cloud**: Emphasizes most common (non-filler, non-stopword) words used in the transcript.
- **Summary Table**: Aggregated stats (e.g., avg. polarity, filler ratio) for each speaker.

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/talkwise-ai.git
cd talkwise-ai
```
### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
### 3. Install the dependencies
```bash
pip install -r requirements.txt
```
### 4. Run Unit Tests (Optional)
```bash
pytest tests/
```