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

### 🖼️ UI Components
#### 🏠 Landing Summary (Always Visible)

#### 📤 Sidebar
- **Upload Transcript**: Upload a `.txt` file containing the dialogue transcript.

#### 🏠 Landing Summary
Displays upon successful upload:
- 📄 **Total Turns**: Number of dialogue entries parsed.
- 👥 **Speakers Detected**: List of distinct speakers.
- 💬 **Average Filler Ratio**: Mean usage of filler words.
- 📊 **Average Sentiment Polarity**: Overall emotional tone (-1 to +1).

- 🎯 **Sentiment Distribution**: Donut chart showing label proportions.
- 🔠 **Top 5 Filler Words**: Bar chart or table view of the most used fillers.





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
### 5. Run the Application
```bash
streamlit run app.py
```