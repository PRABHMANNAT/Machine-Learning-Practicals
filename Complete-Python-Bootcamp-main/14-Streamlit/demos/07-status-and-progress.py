"""Focused demo: status messages, progress bars, placeholders, and spinner."""

import time

import streamlit as st


st.set_page_config(page_title="Status elements", page_icon="⏳")
st.title("Progress and Status")

if st.button("Run tiny job", type="primary"):
    progress = st.progress(0, text="Starting")
    message = st.empty()
    with st.spinner("Working..."):
        for step in range(1, 6):
            time.sleep(0.05)
            progress.progress(step / 5, text=f"Step {step} of 5")
            message.info(f"Finished step {step}")
    progress.empty()
    message.success("All steps completed.")
    st.toast("Job finished")
else:
    st.warning("Press the button to start the demonstration.")
