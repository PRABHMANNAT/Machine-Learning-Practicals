"""Display, style, select, and edit a tiny DataFrame."""  # This introduces the table lesson.

import pandas as pd  # Pandas creates and styles spreadsheet-like data.
import streamlit as st  # Streamlit supplies static, interactive, and editable table components.

st.set_page_config(page_title="DataFrames Demo", page_icon="🧾")  # This sets the browser tab's title and icon.
st.title("🧾 DataFrames")  # This creates the page's large heading.

scores = pd.DataFrame(  # This begins a tiny class-score table.
    {  # Each key below becomes a column.
        "student": ["Asha", "Ben", "Chen", "Diya"],  # This text column stores names.
        "score": [82, 74, 93, 88],  # This number column stores scores out of 100.
        "passed": [True, True, True, True],  # This Boolean column creates checkboxes in the editor.
    }  # This closes the dictionary.
)  # This closes DataFrame creation.

display_tab, edit_tab, static_tab = st.tabs(["Interactive", "Editable", "Static"])  # These tabs compare three ways to show the same data.
with display_tab:  # This block contains the interactive dataframe.
    styled_scores = scores.style.highlight_max(subset=["score"], color="#b7f7c5")  # Styling paints the largest score green.
    st.dataframe(styled_scores, hide_index=True, width="stretch", column_config={"score": st.column_config.ProgressColumn("Score", min_value=0, max_value=100)})  # Column config turns score numbers into progress bars.
with edit_tab:  # This block contains the editable grid.
    edited_scores = st.data_editor(scores, hide_index=True, width="stretch", num_rows="dynamic", key="score_editor")  # `dynamic` lets the visitor add or remove rows.
    st.metric("Current rows", len(edited_scores))  # This metric reacts to edits because the app reruns.
    st.download_button("Download edited CSV", data=edited_scores.to_csv(index=False), file_name="edited_scores.csv", mime="text/csv")  # This component turns the changed table into a downloadable file.
with static_tab:  # This block contains the simplest non-interactive table.
    st.table(scores)  # A static table is best when sorting and scrolling are unnecessary.

st.caption("Use `st.dataframe` to explore, `st.data_editor` to change, and `st.table` for a fixed snapshot.")  # This summarizes when each component fits.
