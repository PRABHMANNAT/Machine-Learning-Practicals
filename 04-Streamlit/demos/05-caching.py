"""Focused demo: cache_data for values and cache_resource for shared objects."""

from pathlib import Path
import time

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
st.set_page_config(page_title="Caching", page_icon="⚡")
st.title("Caching Without Mystery")


@st.cache_data(ttl=300, max_entries=10)
def load_people(path: str) -> pd.DataFrame:
    time.sleep(0.25)  # Makes the first load visibly slower for teaching.
    return pd.read_csv(path, index_col=0)


@st.cache_resource
def shared_labeler():
    # Models/database clients are typical resources. Shared mutable resources
    # must be thread-safe because sessions can use them concurrently.
    return {"name": "tiny reusable resource"}


people = load_people(str(ROOT / "sampledata.csv"))
st.dataframe(people, width="stretch")
st.write(shared_labeler())
st.info("Change an input argument or function code to create a new cache entry.")
if st.button("Clear this app's caches"):
    load_people.clear()
    shared_labeler.clear()
    st.success("Caches cleared.")
