import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import plotly.express as px
from app.parser import parse_transcript
from app.metrics import compute_summary_stats, prepare_per_turn_dataframe
from ui.components import metric_card_style
# Set page config
st.set_page_config(page_title="Dialogue Insights Dashboard", layout="wide")

def main():
    st.sidebar.title("📤 Upload Transcript")
    uploaded_file = st.sidebar.file_uploader("Upload transcript.txt", type=["txt"])

    st.title("🧠 Dialogue Insights Dashboard")

    if not uploaded_file:
        st.markdown("""
        ## ⏳ Awaiting Transcript Upload
        Please upload a `.txt` file from the sidebar to begin analysis.
        """)
        st.stop()

    # Read and parse the transcript
    transcript_str = uploaded_file.read().decode("utf-8")
    with open("data/temp/temp_transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript_str)

    parsed_data = parse_transcript("data/temp/temp_transcript.txt")
    per_turn_df = prepare_per_turn_dataframe(parsed_data)
    summary_stats = compute_summary_stats(parsed_data)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""<div style='{metric_card_style}'>
        <div>👥 Speakers Detected</div>
        <ul style='text-align:left;'>
        {''.join([f'<li>{spk}</li>' for spk in summary_stats['speakers']])}
        </ul>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""<div style='{metric_card_style}'>
        <div>📄 Total Turns</div>
        <div style='font-size:2rem;font-weight:bold'>{summary_stats['num_turns']}</div>
        </div>""", unsafe_allow_html=True)

    with col3:
        st.markdown(f"""<div style='{metric_card_style}'>
        <div>💬 Avg Filler Ratio</div>
        <div style='font-size:2rem;font-weight:bold'>{round(summary_stats['avg_filler_ratio'],2)*100}%</div>
        </div>""", unsafe_allow_html=True)

    with col4:
        st.markdown(f"""<div style='{metric_card_style}'>
        <div>📊 Avg Sentiment Polarity</div>
        <div style='font-size:2rem;font-weight:bold'>{summary_stats['avg_sentiment_polarity']}</div>
        </div>""", unsafe_allow_html=True)

    st.divider()

    col5, col6 = st.columns(2)

    with col5:
        st.markdown(f"""<div style='{metric_card_style}'>
                    <div style='font-size:2rem;font-weight:bold'>🎯 Sentiment Distribution</div>"""
                    ,unsafe_allow_html=True)
        sentiment_dist = summary_stats['sentiment_distribution']
        sentiment_df = pd.DataFrame({"Sentiment": list(sentiment_dist.keys()), "Count": list(sentiment_dist.values())})
        fig_sentiment = px.pie(sentiment_df, names="Sentiment", values="Count", hole=0.4)
        st.plotly_chart(fig_sentiment, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col6:
        # st.markdown(f"<div style='{metric_card_style}'>", unsafe_allow_html=True)
        st.markdown(f"""<div style='{metric_card_style}'>
                    <div style='font-size:2rem;font-weight:bold'>🔠 Top 5 Filler Words</div>"""
                    ,unsafe_allow_html=True)
        # st.markdown("### 🔠 Top 5 Filler Words")
        top_fillers = summary_stats['top_fillers']
        filler_df = pd.DataFrame(top_fillers, columns=["Filler Word", "Count"])
        chart_type = st.radio("View As:", ["Bar Chart", "Table"], horizontal=True, key="filler_view")

        if chart_type == "Bar Chart":
            fig_filler = px.bar(filler_df, x="Filler Word", y="Count", color="Filler Word")
            st.plotly_chart(fig_filler, use_container_width=True)
        else:
            st.dataframe(filler_df.set_index("Filler Word"))

        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
