# Data, CSV Files, Tables, and Charts

## Pandas and tables

```python
data = pd.read_csv("sampledata.csv", index_col=0)
st.dataframe(data, width="stretch")
st.table(data.head())
```

- `st.dataframe` is interactive and scrollable.
- `st.table` is static and best for small tables.
- `st.data_editor` lets users edit cells; validate the returned DataFrame.
- Preview or paginate large datasets instead of rendering millions of rows.

## Upload safety

`file_uploader` provides an in-memory uploaded object. Check extension **and**
actual parse result, limit upload size, catch encoding/parser errors, and avoid
trusting filenames as safe filesystem paths.

```python
uploaded = st.file_uploader("CSV", type="csv")
if uploaded:
    try:
        frame = pd.read_csv(uploaded)
    except (UnicodeDecodeError, pd.errors.ParserError) as error:
        st.error(str(error))
```

## Charts

Quick charts accept tidy Pandas data:

```python
st.line_chart(frame, x="date", y="sales")
st.bar_chart(summary, x="category", y="total")
st.scatter_chart(frame, x="age", y="score", color="group")
```

Use Altair for richer encodings and tooltips. Always label units, handle missing
values, explain filters, and do not imply causation from a simple correlation.

## Dashboard flow

1. Load and validate data.
2. Put filters in sidebar/form.
3. Derive filtered data.
4. Show a few honest metrics.
5. Add charts and a bounded table.
6. Explain empty states and assumptions.
7. Offer a download of the filtered result when useful.
