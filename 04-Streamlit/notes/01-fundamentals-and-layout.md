# Streamlit Fundamentals and Layout

## Explain it like I am 5

A Streamlit script is a stack of building blocks. `st.title()` places a big text
block, `st.button()` places a button, and `st.dataframe()` places a table. When a
widget changes, Streamlit reruns the Python script from the top and redraws the
page for that browser session.

## Basic structure

```python
import streamlit as st

st.set_page_config(page_title="My app", layout="wide")
st.title("My first app")
st.write("Hello!")
```

Call `set_page_config` before other Streamlit page commands.

## Text and media

| Element | Best use |
|---|---|
| `st.title`, `st.header`, `st.subheader` | hierarchy |
| `st.write` | convenient mixed values |
| `st.markdown` | formatted explanatory text |
| `st.caption` | small supporting note |
| `st.code` | source code |
| `st.latex` | equations |
| `st.image` | image path, URL, array, or file |

Do not render untrusted HTML with unsafe options. Prefer normal Markdown and
Streamlit components that escape/handle content safely.

## Layout tools

```python
with st.sidebar:
    year = st.selectbox("Year", [2024, 2025])

left, right = st.columns(2)
with left:
    st.metric("Sales", 120)
with right:
    st.metric("Customers", 40)

overview, details = st.tabs(["Overview", "Details"])
with st.expander("How it works"):
    st.write("Extra explanation")
```

- Sidebar: persistent controls/navigation.
- Columns: side-by-side content; avoid overly deep nesting.
- Tabs: switch visible sections. Code in all tabs may still run during reruns.
- Containers/placeholders: reserve or update a region.
- Expander: hide optional detail.

## Rerun mental model

Widgets return current values. Ordinary local variables are recreated on every
rerun. Use session state for per-session memory and caching for reusable computed
results. Keep side effects behind buttons/forms and make writes idempotent.

