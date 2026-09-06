"""Focused demo: CSV upload, validation, filtering, and download."""

import pandas as pd
import streamlit as st


st.set_page_config(page_title="CSV upload", page_icon="📄", layout="wide")
st.title("Safe CSV Preview")
uploaded = st.file_uploader("Upload a CSV up to the configured size limit", type="csv")

if uploaded is None:
    st.info("Choose a CSV file to begin.")
    st.stop()

try:
    frame = pd.read_csv(uploaded)
except (UnicodeDecodeError, pd.errors.EmptyDataError, pd.errors.ParserError) as error:
    st.error(f"Could not parse the CSV: {error}")
    st.stop()

if frame.empty:
    st.warning("The CSV has columns but no rows.")
    st.stop()

st.metric("Rows", len(frame))
selected_columns = st.multiselect("Columns to keep", list(frame.columns), default=list(frame.columns))
if not selected_columns:
    st.warning("Select at least one column.")
    st.stop()

result = frame[selected_columns]
st.dataframe(result.head(500), width="stretch")
st.download_button(
    "Download selected data",
    result.to_csv(index=False),
    file_name="selected.csv",
    mime="text/csv",
)
