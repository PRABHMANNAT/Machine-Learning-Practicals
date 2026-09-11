"""Data page: load and display the shared repository CSV."""

from pathlib import Path

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parents[2]


@st.cache_data
def load_data():
    return pd.read_csv(ROOT / "sampledata.csv", index_col=0)


st.title("Data Page")
data = load_data()
st.dataframe(data, width="stretch")
st.write("Shape:", data.shape)
