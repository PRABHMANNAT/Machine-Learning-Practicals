"""Chart page: visualize the same sample data."""

from pathlib import Path

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parents[2]
data = pd.read_csv(ROOT / "sampledata.csv", index_col=0)
st.title("Charts Page")
st.bar_chart(data.set_index("Name")["Age"])
st.caption("Age values from sampledata.csv; this tiny dataset is for UI learning only.")

