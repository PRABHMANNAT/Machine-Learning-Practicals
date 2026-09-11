# Beginner Streamlit Learning Folder

Streamlit turns ordinary Python scripts into interactive data apps. Start with
`streamlit.ipynb`, then run the examples from this folder:

```text
python -m pip install -r requirements.txt
streamlit run app.py
```

## Learning path

1. `app.py` — text, DataFrames, metrics, and a chart.
2. `widgets.py` — inputs, buttons, file upload, and download.
3. `classification.py` — cached ML prediction app.
4. `projects/dinosaur_classifier.py` — nearest-neighbour dinosaur matching.
5. `projects/country_classifier.py` — coordinate-to-country matching.
6. `demos/` — one focused concept per file, with line-by-line comments.
7. `multipage_app/` — automatic pages-directory navigation.
8. `notes/` — detailed concept guides.
9. `PRACTICE.md` — exercises from beginner to practical.
10. `STREAMLIT-CHEAT-SHEET.md` — fast revision.

## New focused demonstrations

The numbered files `demos/08-charts.py` through
`demos/22-llm-chat-component.py` cover charts, authentication, connections,
images and video, audio, text, maps, DataFrames, graphs, molecules and genes,
code editors, page navigation, developer tools, integrations, and a local
LLM-shaped chat interface. Every file demonstrates multiple visible components
and explains important parameters directly beside the code.

The chat lesson uses the third-party `st-chat-message` package requested in the
exercise. It is an offline rule-based simulation, so no API key or paid LLM is
needed. The built-in `st.chat_message` remains available as a fallback.

Run any focused example like this:

```text
streamlit run demos/08-charts.py
streamlit run projects/dinosaur_classifier.py
```

Authentication is special: the runnable page uses a clearly marked pretend
login, while `.streamlit/secrets.toml.example` demonstrates where real OIDC
settings belong. Never put real secret values in a committed file.

Streamlit reruns the script top-to-bottom when a visitor changes a widget.
Understanding reruns, session state, caching, and input validation is the key to
building predictable apps.
