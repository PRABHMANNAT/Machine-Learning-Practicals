"""Focused demo: immediate widgets versus batched form submission."""

from datetime import date

import streamlit as st


st.set_page_config(page_title="Widgets and forms", page_icon="🧩")
st.title("Widgets and Forms")

# Outside a form, changing most widgets triggers an immediate rerun.
mode = st.radio("Learning mode", ["Read", "Practice", "Build"], horizontal=True)
topics = st.multiselect("Topics", ["Widgets", "State", "Caching", "Charts"])
st.write("Current choices:", mode, topics)

# A form waits until its submit button is pressed.
with st.form("profile_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120, value=18)
    start_date = st.date_input("Start date", value=date.today())
    notes = st.text_area("Learning goal", max_chars=300)
    submitted = st.form_submit_button("Save profile", type="primary")

if submitted:
    if not name.strip():
        st.error("Name is required.")
    else:
        st.success(f"Saved {name.strip()}, age {age}, starting {start_date}.")
        st.write(notes or "No goal supplied.")

