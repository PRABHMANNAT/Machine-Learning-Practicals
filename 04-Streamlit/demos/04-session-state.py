"""Focused demo: values that survive reruns for one browser session."""

import streamlit as st


st.set_page_config(page_title="Session state", page_icon="🎒")
st.title("Session State Counter and Tasks")

if "count" not in st.session_state:
    st.session_state.count = 0
if "tasks" not in st.session_state:
    st.session_state.tasks = []

decrease, increase, reset = st.columns(3)
if decrease.button("−1"):
    st.session_state.count -= 1
if increase.button("+1"):
    st.session_state.count += 1
if reset.button("Reset"):
    st.session_state.count = 0
st.metric("Count", st.session_state.count)

with st.form("task_form", clear_on_submit=True):
    task = st.text_input("New task")
    submitted = st.form_submit_button("Add task")
if submitted and task.strip():
    # Reassigning a fresh list makes the state change explicit.
    st.session_state.tasks = [*st.session_state.tasks, task.strip()]

for index, task_name in enumerate(st.session_state.tasks, start=1):
    st.write(f"{index}. {task_name}")

if st.button("Clear tasks"):
    st.session_state.tasks = []
    st.rerun()

st.caption("Session state is not a permanent database and should not hold secrets.")

