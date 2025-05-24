import streamlit as st
from ui.styles.card_styles import metric_card_style

def render_landing_summary(stats: dict):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""<div style='{metric_card_style}'>
        <div>👥 Speakers Detected</div>
        <ul style='text-align:left;'>{''.join([f'<li>{spk}</li>' for spk in stats['speakers']])}</ul>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""<div style='{metric_card_style}'>
        <div>📄 Total Turns</div>
        <div style='font-size:2rem;font-weight:bold'>{stats['num_turns']}</div>
        </div>""", unsafe_allow_html=True)

    with col3:
        st.markdown(f"""<div style='{metric_card_style}'>
        <div>💬 Avg Filler Ratio</div>
        <div style='font-size:2rem;font-weight:bold'>{round(stats['avg_filler_ratio'], 2) * 100}%</div>
        </div>""", unsafe_allow_html=True)

    with col4:
        st.markdown(f"""<div style='{metric_card_style}'>
        <div>📊 Avg Sentiment Polarity</div>
        <div style='font-size:2rem;font-weight:bold'>{stats['avg_sentiment_polarity']}</div>
        </div>""", unsafe_allow_html=True)

    st.divider()
