"""Developer helpers for inspecting code, objects, and configuration."""  # This introduces tools meant for people building the app.

import streamlit as st  # Streamlit includes several small debugging and teaching helpers.

st.set_page_config(page_title="Developer Tools", page_icon="🛠️")  # This configures the browser tab.
st.title("🛠️ Developer tools")  # This creates the lesson heading.

with st.echo():  # Echo both runs the indented code and prints that code on the page.
    numbers = [1, 2, 3, 4]  # This sample list gives the echo block something understandable to run.
    doubled = [number * 2 for number in numbers]  # This creates a new list by doubling each old value.
    st.write("Doubled numbers:", doubled)  # This shows the result beneath the echoed source code.

debug_object = {"page": "developer-tools", "reruns": "top to bottom", "debug_mode": True}  # A dictionary is a common object developers need to inspect.
st.subheader("Inspect structured data")  # This heading introduces the JSON inspector.
st.json(debug_object, expanded=True)  # JSON gives dictionaries a clear tree-like display.

show_help = st.checkbox("Show help for st.metric")  # The checkbox prevents a large help panel from crowding the default view.
if show_help:  # This branch runs only when the learner asks for API help.
    st.help(st.metric)  # Help displays the function's signature, parameter descriptions, and documentation.

st.subheader("Read a configuration value")  # This heading introduces runtime configuration inspection.
st.code("st.get_option('theme.base')", language="python")  # This code block shows exactly which call is being demonstrated.
st.write("Current theme base:", st.get_option("theme.base") or "Streamlit default")  # Get option reads one setting; the fallback explains a missing explicit value.
st.caption("Use `st.echo`, `st.json`, `st.help`, and `st.get_option` while learning or debugging.")  # This summarizes the four developer helpers.
