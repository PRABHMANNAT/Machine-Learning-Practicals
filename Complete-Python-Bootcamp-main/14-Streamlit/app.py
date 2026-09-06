"""Beginner demo: text, a DataFrame, metrics, and charts.

Run from this folder:
    streamlit run app.py

Explain it like I am 5: Streamlit reads this script from top to bottom and
turns each `st.*` call into a piece of a web page. When a widget changes, the
script reruns, so keep computations deterministic or cache expensive work.
"""

import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(page_title="Hello Streamlit", page_icon="👋", layout="wide")

st.title("Hello Streamlit")
st.write("This is simple text rendered by `st.write()`.")
st.caption("Start here, then explore widgets.py and the demos/ folder.")

# Preserve the original two-column DataFrame example.
dataframe = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    }
)

left, right = st.columns([2, 1])
with left:
    st.subheader("A small DataFrame")
    st.dataframe(dataframe, width="stretch", hide_index=True)
with right:
    st.subheader("Quick metrics")
    st.metric("Rows", len(dataframe))
    st.metric("Second-column total", int(dataframe["second column"].sum()))

st.subheader("A deterministic line chart")
# A seeded generator keeps the chart stable across reruns.
rng = np.random.default_rng(seed=42)
chart_data = pd.DataFrame(rng.normal(size=(20, 3)), columns=["a", "b", "c"])
st.line_chart(chart_data)

with st.expander("What did this app teach?"):
    st.markdown(
        """
        - `st.title`, `st.write`, and `st.caption` display text.
        - `st.columns` creates side-by-side areas.
        - `st.dataframe` displays interactive tabular data.
        - `st.metric` highlights one important number.
        - `st.line_chart` makes a quick chart from a DataFrame.
        """
    )
