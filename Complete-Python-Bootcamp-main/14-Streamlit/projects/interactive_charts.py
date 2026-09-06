"""Mini-project 4: interactive Altair charts with filters and tooltips."""

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(page_title="Interactive Charts", page_icon="📈", layout="wide")
st.title("Interactive Charts App")

rng = np.random.default_rng(7)
data = pd.DataFrame(
    {
        "day": pd.date_range("2025-01-01", periods=120),
        "category": np.tile(["A", "B", "C"], 40),
        "value": rng.normal(100, 18, 120).round(1),
        "size": rng.integers(20, 100, 120),
    }
)

categories = st.multiselect("Categories", ["A", "B", "C"], default=["A", "B", "C"])
filtered = data[data.category.isin(categories)]
if filtered.empty:
    st.warning("Select at least one category.")
    st.stop()

line = (
    alt.Chart(filtered)
    .mark_line(point=True)
    .encode(
        x=alt.X("day:T", title="Date"),
        y=alt.Y("value:Q", title="Value (units)"),
        color="category:N",
        tooltip=["day:T", "category:N", "value:Q"],
    )
    .properties(height=380)
    .interactive()
)
st.altair_chart(line, width="stretch")

scatter = (
    alt.Chart(filtered)
    .mark_circle(opacity=0.7)
    .encode(x="size:Q", y="value:Q", color="category:N", tooltip=list(filtered.columns))
    .properties(height=320)
)
st.altair_chart(scatter, width="stretch")
