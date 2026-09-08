"""A tiny code-editor playground built from standard Streamlit components."""  # This describes a safe editor that does not execute visitor code.

import streamlit as st  # Streamlit supplies the editor-like box, preview, selector, and download button.

st.set_page_config(page_title="Code Editor Demo", page_icon="💻")  # This sets the tab title and icon.
st.title("💻 Code editors")  # This displays the lesson heading.
st.warning("This demo displays code but never executes typed code.")  # This important boundary keeps the example safe.

language = st.selectbox("Syntax language", options=["python", "javascript", "sql"], help="The language parameter changes colours, not what Python executes.")  # This lets the learner choose syntax highlighting.
starter_code = {  # This dictionary stores one friendly example for each language.
    "python": "name = 'Asha'\nprint(f'Hello {name}')",  # This is the default Python example.
    "javascript": "const name = 'Asha';\nconsole.log(`Hello ${name}`);",  # This is the JavaScript example.
    "sql": "SELECT name\nFROM learners\nWHERE active = 1;",  # This is the SQL example.
}  # This closes the examples dictionary.
code_text = st.text_area("Edit the code", value=starter_code[language], height=180, key=f"editor_{language}", help="`height` controls the editor box in pixels.")  # A multiline text area works as a beginner code editor.

st.subheader("Highlighted preview")  # This heading separates editing from display.
st.code(code_text, language=language, line_numbers=True, wrap_lines=True)  # These parameters add syntax colours, line numbers, and long-line wrapping.
st.download_button("Download code", data=code_text, file_name=f"example.{ {'python': 'py', 'javascript': 'js', 'sql': 'sql'}[language] }", mime="text/plain")  # This turns the current editor contents into a text file.
st.metric("Characters", len(code_text))  # This metric updates whenever the learner edits the text.
