"""Beginner demo: common widgets and a safe CSV upload/download flow."""

from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(page_title="Widget Playground", page_icon="🎛️")
st.title("Streamlit Widget Playground")
st.write("A widget is a control the visitor can touch. Changing it reruns the script.")

basic_tab, data_tab = st.tabs(["Inputs", "CSV data"])

with basic_tab:
    name = st.text_input("Enter your name", placeholder="Asha")
    age = st.slider("Select your age", min_value=0, max_value=100, value=25)
    options = ["Python", "Java", "C++", "JavaScript"]
    choice = st.selectbox("Choose your favorite language", options)
    learning = st.checkbox("I am learning Streamlit")

    if st.button("Show my answers", type="primary"):
        if name.strip():
            st.success(f"Hello, {name.strip()}! You selected {choice}.")
        else:
            st.warning("Please enter your name first.")
    st.write(f"Your age is {age}.")
    if learning:
        st.info("Wonderful—small experiments are the fastest way to learn.")

with data_tab:
    # Preserve the original John/Jane/Jake/Jill DataFrame example.
    example_data = pd.DataFrame(
        {
            "Name": ["John", "Jane", "Jake", "Jill"],
            "Age": [28, 24, 35, 40],
            "City": ["New York", "Los Angeles", "Chicago", "Houston"],
        }
    )
    st.dataframe(example_data, width="stretch", hide_index=True)

    # The original script wrote sampledata.csv on every rerun. A download
    # button teaches CSV export without silently overwriting a repository file.
    st.download_button(
        "Download example CSV",
        data=example_data.to_csv(index=False).encode("utf-8"),
        file_name="people.csv",
        mime="text/csv",
    )

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        try:
            uploaded_dataframe = pd.read_csv(uploaded_file)
        except (UnicodeDecodeError, pd.errors.ParserError) as error:
            st.error(f"Could not read that CSV: {error}")
        else:
            st.success(f"Loaded {len(uploaded_dataframe):,} rows.")
            st.dataframe(uploaded_dataframe.head(100), width="stretch")

st.caption(f"Repository sample: {Path(__file__).with_name('sampledata.csv').name}")
