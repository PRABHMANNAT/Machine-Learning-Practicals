"""About page: plain explanatory content."""

import streamlit as st


st.title("About This Multipage Demo")
st.markdown(
    """
    - `Home.py` is the entry point.
    - Files in `pages/` become navigable pages.
    - Shared data loading can move to an importable utility module as the app grows.
    """
)
