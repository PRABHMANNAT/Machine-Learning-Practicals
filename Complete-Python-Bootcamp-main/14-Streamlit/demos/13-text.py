"""A friendly tour of Streamlit text-display components."""  # This docstring tells learners what the file demonstrates.

import streamlit as st  # Streamlit turns our strings into styled web-page text.

st.set_page_config(page_title="Text Demo", page_icon="✍️")  # This configures the browser tab before other page elements.
st.title("✍️ Text components")  # A title is the largest standard heading.
st.header("A header starts a big section")  # A header breaks the page into major ideas.
st.subheader("A subheader starts a smaller section")  # A subheader creates a level below a header.
st.write("`st.write` is the helpful all-rounder: it understands plain text, Markdown, numbers, and many Python objects.")  # Write automatically chooses a useful display.

learner_name = st.text_input("Your name", value="Asha", max_chars=20, help="`value` is the starting text and `max_chars` limits its length.")  # This text widget collects one short line.
st.markdown(f"Hello **{learner_name or 'learner'}**! Markdown makes text **bold**, *italic*, or `code-like`.")  # Markdown adds lightweight formatting to a string.
st.caption("A caption is quiet helper text for sources, hints, or limitations.")  # A caption uses smaller, softer styling.
st.code("for number in range(3):\n    print(number)", language="python", line_numbers=True)  # This code block adds Python colours and line numbers.

with st.expander("See LaTeX and a divider"):  # An expander hides optional text until clicked.
    st.latex(r"a^2 + b^2 = c^2")  # LaTeX renders a mathematical formula clearly.
    st.divider()  # A divider draws a horizontal line between ideas.
    st.info("Use the most specific text component when its visual meaning helps the reader.")  # An info box highlights a useful lesson.
