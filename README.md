# 💬 Dialogue Insights

This is a self-contained NLP-powered web app that analyzes conversation transcripts for sentiment and filler-word usage. Built using Hugging Face Transformers, spaCy, and Streamlit. The app extracts per-turn and overall conversation insights such as sentiment, filler word usage, and speaker statistics, and presents them in an engaging dashboard.

## 💼 Why This App Is Useful
### 📌 Business Use Case
In any communication-heavy domain—like customer support, team meetings, interviews, or sales conversations—understanding how people speak can be as important as what they say.

This app provides structured insights into:

    - Emotional tone of a dialogue

    - Clarity and fluency (via filler usage)

    - Speaker-specific tendencies

### 🎯 Who Benefits from This?
- Customer Support Teams	- Monitor call quality, emotional tone, overuse of fillers
- Sales Teams	- Analyze winning vs. losing call patterns
- UX Researchers / Analysts	- Study conversation clarity during usability tests
- Interviewers / Hiring Panels	- Track candidate fluency, confidence, or tone
- Educators / Public Speakers	- Get feedback on speaking style

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
```
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
│   └── transcript.txt           # Sample input transcript file
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
├── app.py                       # ENTRY POINT for Streamlit app
├── requirements.txt             # Python dependencies
├── setup.py                     # Project metadata
└── README.md                    
```

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

## Future Enhancements
1. **Transcript Summarizer**: Automatically converts the full conversation into a short summary using HuggingFace `summarization` pipeline (e.g., `facebook/bart-large-cnn`).
2. **Dynamic Top-N Controls** - User-selectable value to control "Top N" fillers and common words.
3. **Downloadable Reports** - Export full summary as PDF or CSV.
4. **Stopword Filtering Toggle** - Let user choose to ignore or include common stopwords.
5. **UI Enhancements** - Streamlit theming with .streamlit/config.toml.
6. **Voice Transcription Pipeline** - Auto-transcribe audio using Whisper Plug into this dashboard. (Advanced)
