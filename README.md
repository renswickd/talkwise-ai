# 💬 Dialogue Insights

This is a self-contained NLP-powered web app that analyzes conversation transcripts for sentiment and filler-word usage. Built using Hugging Face Transformers, spaCy, and Streamlit. The app extracts per-turn and overall conversation insights such as sentiment, filler word usage, and speaker statistics, and presents them in an engaging dashboard.

---

## 🚀 Features

1. 📊 Sentiment analysis per dialogue turn (Positive, Negative, Neutral)
2. 🗣️ Filler word ratio (e.g., "um", "like", "uhh")
3. 📈 Interactive web dashboard using Streamlit
4. 📄 Custom transcript support (12–16 line dialogues)
5. ⚠️ Defensive error handling for invalid or missing input
6. 🔍 Sentiment analysis using CardiffNLP RoBERTa (3-class)
7. 🗣️ Filler word analysis using spaCy (customizable filler list in config)

---

## 📊 Metrics & Visualizations in the Dashboard
The application analyzes the conversation transcript and presents the following metrics in the Streamlit dashboard:

### 🖥️ UI Components

#### 📤 Sidebar
- Upload `.txt` file containing the transcript.

#### 🏠 Landing Summary
- 👥 **Speakers Detected**
- 📄 **Total Turns**
- 💬 **Average Filler Ratio**
- 📊 **Average Sentiment Polarity**

#### 📋 Annotated Transcript
- Full parsed dialogue with computed metrics per turn.

##### 🔽 Per-Turn Metrics (Expandable)
- Sentiment Trend (line chart)
- Filler Ratio (bar chart)
- Colored Sentiment Line (speaker overlay)

#### 🔽 Overall Metrics (Expandable)
- Speaker Summary Table
- Sentiment Distribution (Pie)
- Word Cloud
- Top 5 Filler Words (Bar/Table toggle)

## Folder Structure
.
├── app/                         # Core NLP logic
│   ├── analyzer.py              # Sentiment & filler ratio computations
│   ├── metrics.py               # Summary & per-turn metric calculations
│   └── parser.py                # Parses raw transcript string
│
├── config/                      # YAML config files
│   └── pipeline_config.yaml     # Filler word list, top filler count, etc.
│
├── data/                        # Transcript input/output storage
│   └── temp_transcript.txt      # Temporary file for uploaded transcript
│
├── tests/                       # Unit tests
│   ├── test_parser.py
│   ├── test_analyzer.py
│   └── test_metrics.py
│
├── ui/                          # Streamlit dashboard
│   ├── dashboard.py             # Main Streamlit entry logic
│   ├── components.py            # Shared styles (card CSS)
│   └── sections/                # Modular UI views
│       ├── landing_summary.py
│       ├── annotated_transcript.py
│       ├── per_turn_metrics.py
│       └── overall_metrics.py
│
├── utils/                       # Helper functions
│   └── common_functions.py      # YAML loader and shared utilities
│
├── app.py                       # 🔁 ENTRY POINT for Streamlit app
├── requirements.txt             # Python dependencies
├── setup.py                     # Project metadata (optional packaging)
└── README.md                    # You are here




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