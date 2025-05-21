# 💬 Dialogue Insights

A self-contained NLP-powered web app that analyzes conversation transcripts for sentiment and filler-word usage. Built using Hugging Face Transformers, spaCy, and Streamlit.

---

## 🚀 Features

- 📊 Sentiment analysis per dialogue turn (Positive, Negative, Neutral)
- 🗣️ Filler word ratio (e.g., "um", "like", "you know")
- 📈 Interactive web dashboard using Streamlit
- 📄 Custom transcript support (12–16 line dialogues)

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/dialogue-insights.git
cd dialogue-insights
```
### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
### 3. Install the dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
