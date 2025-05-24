import streamlit as st
import plotly.express as px
import pandas as pd
from wordcloud import WordCloud
from ui.styles.card_styles import metric_card_style
from matplotlib import pyplot as plt

def render_overall_metrics(per_turn_df: pd.DataFrame, summary_stats: dict):
    # st.markdown(f"""<div style='{metric_card_style}'>
    #         <div style='font-size:1.5rem;font-weight:bold'>👤 Speaker-wise Summary Table</div>""", unsafe_allow_html=True)
    
    st.markdown(f"""<div style='{metric_card_style}'>
    <div style='font-size:1.5rem;font-weight:bold'>👤 Speaker-wise Summary Table</div>
    <hr style='border: 1px solid #ccc; margin: 0.5rem 0;' />
    """, unsafe_allow_html=True)

    # st.markdown(f"""<div style='{section_header_style}'>🔍 Per-Turn Metrics Summary</div>""", unsafe_allow_html=True)


    speaker_summary = per_turn_df.groupby('speaker')[['filler_ratio', 'polarity_score']].mean().reset_index()
    speaker_summary.columns = ['Speaker', 'Avg Filler Ratio', 'Avg Sentiment Polarity']
    st.dataframe(speaker_summary.set_index('Speaker'))

    col31, col32, col33 = st.columns(3)
    with col31:
        st.markdown(f"""<div style='{metric_card_style}'>
                <div style='font-size:1.5rem;font-weight:bold'>🎯 Sentiment Distribution</div>"""
                ,unsafe_allow_html=True)
        sentiment_dist = summary_stats['sentiment_distribution']
        sentiment_df = pd.DataFrame({"Sentiment": list(sentiment_dist.keys()), "Count": list(sentiment_dist.values())})
        fig_sentiment = px.pie(sentiment_df, names="Sentiment", values="Count", hole=0.4)
        st.plotly_chart(fig_sentiment, use_container_width=True, key="sentiment_main")
        st.markdown("</div>", unsafe_allow_html=True)

    with col32:
        st.markdown(f"""<div style='{metric_card_style}'>
                <div style='font-size:1.5rem;font-weight:bold'>☁️ Word Cloud of All Utterances</div>"""
                ,unsafe_allow_html=True)
        all_text = " ".join(per_turn_df['utterance'].tolist())
        wordcloud = WordCloud(width=800, height=750, background_color='white').generate(all_text)
        fig_wc, ax_wc = plt.subplots()
        ax_wc.imshow(wordcloud, interpolation='bilinear')
        ax_wc.axis("off")
        st.pyplot(fig_wc)

    with col33:
        st.markdown(f"""<div style='{metric_card_style}'>
                <div style='font-size:1.5rem;font-weight:bold'>🔠 Top 5 Filler Words</div>"""
                ,unsafe_allow_html=True)
        top_fillers = summary_stats['top_fillers']
        filler_df = pd.DataFrame(top_fillers, columns=["Filler Word", "Count"])
        chart_type = st.radio("", ["Bar Chart", "Table"], horizontal=True, key="filler_view")

        if chart_type == "Bar Chart":
            fig_filler = px.bar(filler_df, x="Filler Word", y="Count", color="Filler Word")
            st.plotly_chart(fig_filler, use_container_width=True)
        else:
            st.dataframe(filler_df.set_index("Filler Word"))

        st.markdown("</div>", unsafe_allow_html=True)