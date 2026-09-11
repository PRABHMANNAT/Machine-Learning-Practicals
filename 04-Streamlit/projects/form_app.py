"""Mini-project 3: validated feedback form stored in session state."""

import re

import pandas as pd
import streamlit as st


st.set_page_config(page_title="Feedback Form", page_icon="📝")
st.title("Feedback Form App")

if "submissions" not in st.session_state:
    st.session_state.submissions = []

with st.form("feedback", clear_on_submit=True):
    name = st.text_input("Name")
    email = st.text_input("Email")
    rating = st.slider("Rating", 1, 5, 3)
    message = st.text_area("Feedback", max_chars=500)
    consent = st.checkbox("I agree to submit this feedback")
    submitted = st.form_submit_button("Submit", type="primary")

if submitted:
    errors = []
    if not name.strip():
        errors.append("Name is required.")
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()):
        errors.append("Enter a simple valid email address.")
    if not message.strip():
        errors.append("Feedback is required.")
    if not consent:
        errors.append("Consent is required.")

    if errors:
        for error in errors:
            st.error(error)
    else:
        # Session state is only for this learning demo; use a database when
        # submissions must survive restarts or be shared across users.
        st.session_state.submissions.append(
            {"name": name.strip(), "email": email.strip(), "rating": rating, "feedback": message.strip()}
        )
        st.success("Thank you—your feedback was recorded for this session.")

if st.session_state.submissions:
    st.subheader("Session submissions")
    st.dataframe(pd.DataFrame(st.session_state.submissions), hide_index=True, width="stretch")
