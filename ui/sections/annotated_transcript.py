import streamlit as st
from ui.styles.card_styles import metric_card_style

def render_annotated_transcript(df):
    # st.markdown(f"""<div style='{metric_card_style}'>
    #             <div style='font-size:2rem;font-weight:bold'>📋 Annotated Transcript</div>""", unsafe_allow_html=True)
    st.markdown(f"""<div style='{metric_card_style}'>
    <div style='font-size:1.5rem;font-weight:bold'>📋 Annotated Transcript</div>
    <hr style='border: 1px solid #ccc; margin: 0.5rem 0;' />
    """, unsafe_allow_html=True)
    st.dataframe(df)
    # st.divider()
