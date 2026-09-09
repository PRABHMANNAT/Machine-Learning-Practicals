# Widgets, Forms, Session State, and Caching

## Widgets

Common inputs include `button`, `checkbox`, `toggle`, `radio`, `selectbox`,
`multiselect`, `slider`, `number_input`, `text_input`, `text_area`, `date_input`,
`time_input`, `color_picker`, and `file_uploader`.

Give widgets stable, unique keys when labels repeat or state must be addressed:

```python
name = st.text_input("Name", key="profile_name")
```

## Forms

Outside a form, most widget changes rerun immediately. A form batches values and
submits them together.

```python
with st.form("profile"):
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120)
    submitted = st.form_submit_button("Save")

if submitted:
    st.success(f"Saved {name}")
```

Validate on the server/script side even if a widget limits values.

## Session state

`st.session_state` is one visitor session's labeled backpack. It survives reruns
but not necessarily a server restart or expired session.

```python
if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("Add"):
    st.session_state.count += 1
st.write(st.session_state.count)
```

Avoid placing secrets or enormous data in session state. Initialize keys before
reading them. Widget keys automatically appear in session state.

## Caching

| Decorator | Use |
|---|---|
| `@st.cache_data` | serializable data/results; callers receive safe copies |
| `@st.cache_resource` | shared resource/model/client; may be mutable |

```python
@st.cache_data(ttl=300, max_entries=20)
def load_csv(path):
    return pd.read_csv(path)

@st.cache_resource
def load_model():
    return train_model()
```

Function code and arguments help form cache keys. Cache functions should be
predictable. Add TTL/entry bounds for changing or unbounded inputs. Shared cached
resources may need thread safety. Use clear-cache controls during development.

