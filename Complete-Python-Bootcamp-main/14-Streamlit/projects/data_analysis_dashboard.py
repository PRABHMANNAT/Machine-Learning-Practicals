"""Mini-project 6: analysis dashboard built from the repository CSV."""

from pathlib import Path

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
st.set_page_config(page_title="People Analysis", page_icon="🧭", layout="wide")


@st.cache_data
def load_people():
    data = pd.read_csv(ROOT / "sampledata.csv", index_col=0)
    data["Age Group"] = pd.cut(data["Age"], bins=[0, 25, 35, 200], labels=["25 or under", "26–35", "36+"])
    return data


people = load_people()
st.title("Sample Data Analysis Dashboard")
st.caption("Source: sampledata.csv in this learning folder.")

cities = st.sidebar.multiselect("Cities", sorted(people.City.unique()), default=sorted(people.City.unique()))
minimum_age, maximum_age = st.sidebar.slider(
    "Age range",
    int(people.Age.min()),
    int(people.Age.max()),
    (int(people.Age.min()), int(people.Age.max())),
)
filtered = people[people.City.isin(cities) & people.Age.between(minimum_age, maximum_age)]

if filtered.empty:
    st.warning("No people match the selected filters.")
    st.stop()

one, two, three = st.columns(3)
one.metric("People", len(filtered))
two.metric("Average age", f"{filtered.Age.mean():.1f}")
three.metric("Cities", filtered.City.nunique())

st.bar_chart(filtered.groupby("Age Group", observed=False).size().rename("People"))
st.dataframe(filtered, width="stretch")
st.download_button("Download filtered data", filtered.to_csv(index=False), "people_filtered.csv", "text/csv")
