# import required libraries
import streamlit as st
from app.parser import parse_transcript
from app.metrics import compute_summary_stats, prepare_per_turn_dataframe
from ui.styles.card_styles import section_header_style
from ui.sections.landing_summary import render_landing_summary
from ui.sections.annotated_transcript import render_annotated_transcript
from ui.sections.per_turn_metrics import render_per_turn_metrics
from ui.sections.overall_metrics import render_overall_metrics

# Set page config
st.set_page_config(page_title="Dialogue Insights Dashboard", layout="wide")

def main():
    st.sidebar.title("📤 Upload Transcript")
    uploaded_file = st.sidebar.file_uploader("Upload transcript.txt", type=["txt"])

    st.title("📝 Dialogue Insights Dashboard")

    if not uploaded_file:
        st.markdown("""
        ## ⏳ Awaiting Transcript Upload
        Please upload a `.txt` file to analyze.
        """)
        st.stop()

    # Read and parse the transcript
    transcript_str = uploaded_file.read().decode("utf-8")

    parsed_data = parse_transcript(transcript_str)
    per_turn_df = prepare_per_turn_dataframe(parsed_data)
    summary_stats = compute_summary_stats(parsed_data)

    # Render the dashboard components
    render_landing_summary(summary_stats)
    render_annotated_transcript(per_turn_df)

    # Section Header
    st.markdown(f"""<div style='{section_header_style}'>📊 Metrics Overview</div>""", unsafe_allow_html=True)

    # Per-Turn Metrics Expander
    with st.expander("🔍 Per-Turn Metrics", expanded=False):
        render_per_turn_metrics(per_turn_df)

    # Overall Metrics
    with st.expander("📊 Overall Metrics", expanded=False):
        render_overall_metrics(per_turn_df, summary_stats)


if __name__ == "__main__":
    main()
