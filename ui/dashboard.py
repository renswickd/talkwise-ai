import streamlit as st
import pandas as pd
import plotly.express as px
from app.parser import parse_transcript
from app.metrics import compute_summary_stats, prepare_per_turn_dataframe
from ui.components import metric_card_style
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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

    col11, col12, col13, col14 = st.columns(4)

    with col11:
        st.markdown(f"""<div style='{metric_card_style}'>
        <div>👥 Speakers Detected</div>
        <ul style='text-align:left;'>
        {''.join([f'<li>{spk}</li>' for spk in summary_stats['speakers']])}
        </ul>
        </div>""", unsafe_allow_html=True)

    with col12:
        st.markdown(f"""<div style='{metric_card_style}'>
        <div>📄 Total Turns</div>
        <div style='font-size:2rem;font-weight:bold'>{summary_stats['num_turns']}</div>
        </div>""", unsafe_allow_html=True)

    with col13:
        st.markdown(f"""<div style='{metric_card_style}'>
        <div>💬 Avg Filler Ratio</div>
        <div style='font-size:2rem;font-weight:bold'>{round(summary_stats['avg_filler_ratio'],2)*100}%</div>
        </div>""", unsafe_allow_html=True)

    with col14:
        st.markdown(f"""<div style='{metric_card_style}'>
        <div>📊 Avg Sentiment Polarity</div>
        <div style='font-size:2rem;font-weight:bold'>{summary_stats['avg_sentiment_polarity']}</div>
        </div>""", unsafe_allow_html=True)

    st.divider()

    # st.markdown("### 📋 Annotated Transcript")
    st.markdown(f"""<div style='{metric_card_style}'>
                <div style='font-size:2rem;font-weight:bold'>📋 Annotated Transcript</div>""", unsafe_allow_html=True)
    st.dataframe(per_turn_df)

    st.divider()

    # Per-Turn Metrics Expander
    with st.expander("🔍 Per-Turn Metrics", expanded=False):

        col21, col22, col23 = st.columns(3)
        with col21:
            st.markdown(f"""<div style='{metric_card_style}'>
                        <div style='font-size:2rem;font-weight:bold'>📈 Sentiment Polarity Trend</div>""", unsafe_allow_html=True)
            st.line_chart(per_turn_df['polarity_score'], use_container_width=True, x_label="Turn Number", y_label="Sentiment Polarity")
            st.markdown("</div>", unsafe_allow_html=True)

        with col22:
            st.markdown(f"""<div style='{metric_card_style}'>
                        <div style='font-size:2rem;font-weight:bold'>📉 Filler Ratio per Turn</div>""", unsafe_allow_html=True)
            st.bar_chart(per_turn_df['filler_ratio'], use_container_width=True, x_label="Turn Number", y_label="Filler Ratio")
            st.markdown("</div>", unsafe_allow_html=True)
            
        
        with col23:
            st.markdown(f"""<div style='{metric_card_style}'>
                         <div style='font-size:2rem;font-weight:bold'>🔁 Sentiment Overlaid by Turn</div>""", unsafe_allow_html=True)
            fig = px.line(per_turn_df, x=per_turn_df.index + 1, y='polarity_score', color='speaker', 
                          labels={'x': 'Turn Number', 'polarity_score': 'Sentiment Polarity'})
            fig.update_layout(xaxis_title='Turn Number', yaxis_title='Sentiment Polarity')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)


    # Overall Metrics
    with st.expander("📊 Overall Metrics", expanded=False):

        # st.markdown("#### 👤 Speaker-wise Summary Table")
        st.markdown(f"""<div style='{metric_card_style}'>
                <div style='font-size:2rem;font-weight:bold'>👤 Speaker-wise Summary Table</div>""", unsafe_allow_html=True)
        speaker_summary = per_turn_df.groupby('speaker')[['filler_ratio', 'polarity_score']].mean().reset_index()
        speaker_summary.columns = ['Speaker', 'Avg Filler Ratio', 'Avg Sentiment Polarity']
        st.dataframe(speaker_summary.set_index('Speaker'))

        col31, col32, col33 = st.columns(3)
        with col31:
            st.markdown(f"""<div style='{metric_card_style}'>
                    <div style='font-size:2rem;font-weight:bold'>🎯 Sentiment Distribution</div>"""
                    ,unsafe_allow_html=True)
            sentiment_dist = summary_stats['sentiment_distribution']
            sentiment_df = pd.DataFrame({"Sentiment": list(sentiment_dist.keys()), "Count": list(sentiment_dist.values())})
            fig_sentiment = px.pie(sentiment_df, names="Sentiment", values="Count", hole=0.4)
            st.plotly_chart(fig_sentiment, use_container_width=True, key="sentiment_main")
            st.markdown("</div>", unsafe_allow_html=True)

        with col32:
            st.markdown(f"""<div style='{metric_card_style}'>
                    <div style='font-size:2rem;font-weight:bold'>☁️ Word Cloud of All Utterances</div>"""
                    ,unsafe_allow_html=True)
            all_text = " ".join(per_turn_df['utterance'].tolist())
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
            fig_wc, ax_wc = plt.subplots()
            ax_wc.imshow(wordcloud, interpolation='bilinear')
            ax_wc.axis("off")
            st.pyplot(fig_wc)

        with col33:
            st.markdown(f"""<div style='{metric_card_style}'>
                    <div style='font-size:2rem;font-weight:bold'>🔠 Top 5 Filler Words</div>"""
                    ,unsafe_allow_html=True)
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
