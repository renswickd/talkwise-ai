import streamlit as st
import plotly.express as px
import pandas as pd
from ui.styles.card_styles import metric_card_style

def render_per_turn_metrics(per_turn_df: pd.DataFrame):
    col21, col22, col23 = st.columns(3)
    with col21:
        st.markdown(f"""<div style='{metric_card_style}'>
                    <div style='font-size:1.5rem;font-weight:bold'>📈 Sentiment Polarity Trend</div>""", unsafe_allow_html=True)
        st.line_chart(per_turn_df['polarity_score'], use_container_width=True, x_label="Turn Number", y_label="Sentiment Polarity")
        st.markdown("</div>", unsafe_allow_html=True)

    with col22:
        st.markdown(f"""<div style='{metric_card_style}'>
                    <div style='font-size:1.5rem;font-weight:bold'>📉 Filler Ratio per Turn</div>""", unsafe_allow_html=True)
        st.bar_chart(per_turn_df['filler_ratio'], use_container_width=True, x_label="Turn Number", y_label="Filler Ratio")
        st.markdown("</div>", unsafe_allow_html=True)
        
    
    with col23:
        st.markdown(f"""<div style='{metric_card_style}'>
                        <div style='font-size:1.5rem;font-weight:bold'>🔁 Sentiment Overlaid by Turn</div>""", unsafe_allow_html=True)
        fig = px.line(per_turn_df, x=per_turn_df.index + 1, y='polarity_score', color='speaker', 
                        labels={'x': 'Turn Number', 'polarity_score': 'Sentiment Polarity'})
        fig.update_layout(xaxis_title='Turn Number', yaxis_title='Sentiment Polarity')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)