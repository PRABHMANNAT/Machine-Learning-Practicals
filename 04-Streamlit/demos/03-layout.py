"""Focused demo: sidebar, columns, tabs, containers, and expanders."""

import streamlit as st


st.set_page_config(page_title="Layout", page_icon="🧱", layout="wide")
st.title("Layout Building Blocks")

with st.sidebar:
    st.header("Filters")
    period = st.selectbox("Period", ["Week", "Month", "Year"])
    show_details = st.toggle("Show details", value=True)

one, two, three = st.columns(3)
one.metric("Visitors", "1,240", "+8%")
two.metric("Orders", "86", "+4")
three.metric("Returns", "3", "-1", delta_color="inverse")

overview, data, help_tab = st.tabs(["Overview", "Data", "Help"])
with overview:
    st.write("Selected period:", period)
    with st.container(border=True):
        st.write("Containers keep related elements together.")
with data:
    st.table({"Day": ["Mon", "Tue"], "Orders": [10, 14]})
with help_tab:
    with st.expander("Why use layout tools?", expanded=True):
        st.write("They create hierarchy without custom frontend code.")

if show_details:
    st.caption("Details are visible because the sidebar toggle is on.")

