# Streamlit Quick Revision Cheat Sheet

## Run

```text
streamlit run app.py
streamlit run multipage_app/Home.py
```

## Page and text

```python
st.set_page_config(page_title="App", layout="wide")
st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.write(value)
st.markdown("**Markdown**")
st.caption("Small note")
st.code("print('hi')", language="python")
st.image("assets/picture.png")
```

## Inputs

```python
clicked = st.button("Run")
name = st.text_input("Name", key="name")
age = st.number_input("Age", 0, 120)
choice = st.selectbox("Choice", options)
many = st.multiselect("Many", options)
value = st.slider("Value", 0, 100, 50)
enabled = st.checkbox("Enabled")
uploaded = st.file_uploader("CSV", type="csv")
```

## Form

```python
with st.form("form_key"):
    name = st.text_input("Name")
    submitted = st.form_submit_button("Save")
if submitted:
    st.success(name)
```

## Layout

```python
with st.sidebar: ...
left, right = st.columns(2)
tab1, tab2 = st.tabs(["One", "Two"])
with st.container(): ...
with st.expander("Details"): ...
placeholder = st.empty()
```

## State and caching

```python
if "count" not in st.session_state:
    st.session_state.count = 0

@st.cache_data(ttl=300)
def load_data(path): ...

@st.cache_resource
def load_model(): ...
```

## Data, metrics, charts

```python
st.dataframe(frame, width="stretch")
edited = st.data_editor(frame)
st.metric("Revenue", "$120K", delta="8%")
st.line_chart(frame)
st.bar_chart(frame)
st.scatter_chart(frame, x="x", y="y", color="group")
st.altair_chart(chart, width="stretch")
```

## Status

```python
st.success("Done")
st.info("Note")
st.warning("Careful")
st.error("Failed")
st.progress(0.5)
with st.spinner("Working..."): ...
st.toast("Saved")
```

## Download

```python
st.download_button(
    "Download CSV",
    frame.to_csv(index=False),
    file_name="result.csv",
    mime="text/csv",
)
```

## Golden rules

- The script reruns top-to-bottom after widget changes.
- Give repeated widgets unique stable keys.
- Use forms to batch input, session state for per-session memory, and the correct cache decorator.
- Validate uploads and model inputs; show empty/error/loading states.
- Base file paths on `Path(__file__)`.
- Do not store secrets in source or per-user data in global variables.
- Cache with limits/TTL where inputs can grow or data changes.
- Test the actual app, then deploy with pinned dependencies and monitoring.
