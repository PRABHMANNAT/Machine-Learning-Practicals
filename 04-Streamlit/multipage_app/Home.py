"""Home page for the automatic pages-directory multipage demo."""

from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
st.set_page_config(page_title="Multipage Learning App", page_icon="🗂️")
st.title("Multipage Streamlit App")
st.write("Use the page navigation to open the data, chart, and about pages.")
st.image(str(ROOT / "assets" / "streamlit_learning.svg"))
st.info("Files inside `pages/` become pages automatically in this simple structure.")

