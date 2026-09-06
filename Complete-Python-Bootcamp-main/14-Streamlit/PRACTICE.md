# Streamlit Practice Path

## Beginner

1. Add a header, caption, code block, and image to `app.py`.
2. Add a radio button and color picker to `widgets.py`.
3. Put controls in the sidebar and results in the main page.
4. Create three metrics in columns.
5. Add tabs for table, chart, and explanation.
6. Build a form that validates name, email, and age.

## Intermediate

7. Create a counter with reset using session state.
8. Add callback functions to two widgets without causing a key conflict.
9. Cache a CSV loader with TTL and a maximum number of entries.
10. Upload a CSV, select columns, filter rows, and download the result.
11. Add empty-data and malformed-file error states.
12. Create a line, bar, and scatter chart from one tidy DataFrame.
13. Add progress and status elements to a simulated multi-step job.
14. Make an editable task table with `st.data_editor` and session state.

## Practical

15. Add filters and honest KPI definitions to the sales dashboard.
16. Add missing-value summaries and datatype controls to the CSV explorer.
17. Save form submissions to SQLite rather than a global list.
18. Add cross-validation metrics and model limitations to the Iris app.
19. Turn one mini-project into a multipage app with shared utility functions.
20. Add a theme, pinned dependencies, safe secrets, tests, and a deployment README.

## Review questions

- Why does Streamlit rerun, and which variables survive?
- When should you use `cache_data` versus `cache_resource`?
- Why can code in an unselected tab still execute?
- Why should uploaded filenames not become trusted local paths?
- Why is a model probability not guaranteed correctness?
- What belongs in session state, a cache, a database, or a URL parameter?
