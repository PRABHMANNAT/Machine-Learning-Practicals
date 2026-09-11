"""Mini-project 2: upload, inspect, filter, summarize, and export a CSV."""

import pandas as pd
import streamlit as st


st.set_page_config(page_title="CSV Explorer", page_icon="🔎", layout="wide")
st.title("CSV Explorer")

uploaded = st.file_uploader("Upload a CSV", type="csv")
if uploaded is None:
    st.info("Upload a CSV. The file is processed in memory for this session.")
    st.stop()

try:
    data = pd.read_csv(uploaded)
except (UnicodeDecodeError, pd.errors.EmptyDataError, pd.errors.ParserError) as error:
    st.error(f"Could not read the file: {error}")
    st.stop()

rows, columns = data.shape
c1, c2, c3 = st.columns(3)
c1.metric("Rows", f"{rows:,}")
c2.metric("Columns", columns)
c3.metric("Missing cells", f"{int(data.isna().sum().sum()):,}")

preview_tab, summary_tab, filter_tab = st.tabs(["Preview", "Summary", "Filter"])
with preview_tab:
    st.dataframe(data.head(500), width="stretch")
with summary_tab:
    st.dataframe(data.describe(include="all").transpose().fillna(""), width="stretch")
    st.dataframe(data.dtypes.astype(str).rename("dtype"), width="stretch")
with filter_tab:
    selected = st.multiselect("Columns", list(data.columns), default=list(data.columns))
    search = st.text_input("Contains text anywhere (optional)").strip()
    filtered = data[selected] if selected else data.iloc[:, 0:0]
    if search and selected:
        mask = filtered.astype(str).apply(lambda column: column.str.contains(search, case=False, na=False)).any(axis=1)
        filtered = filtered[mask]
    st.write(f"{len(filtered):,} matching rows")
    st.dataframe(filtered.head(500), width="stretch")
    st.download_button("Download filtered CSV", filtered.to_csv(index=False), "filtered.csv", "text/csv")
