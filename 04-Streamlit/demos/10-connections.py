"""Offline connection demo using Python's built-in SQLite database."""  # This describes the local, no-password data source.

import sqlite3  # SQLite is a tiny database included with Python.

import pandas as pd  # Pandas turns database rows into a friendly table.
import streamlit as st  # Streamlit provides caching, widgets, metrics, and tables.

st.set_page_config(page_title="Connections Demo", page_icon="🔌")  # This sets the page's browser-tab details.
st.title("🔌 Connections")  # This adds the visible lesson title.


@st.cache_resource  # A database connection is a resource that should be reused across reruns.
def get_connection():  # This function creates the local practice database.
    connection = sqlite3.connect(":memory:", check_same_thread=False)  # ':memory:' keeps the database temporary and leaves no file behind.
    connection.execute("CREATE TABLE snacks (name TEXT, kind TEXT, price REAL)")  # This SQL statement makes a table with three columns.
    connection.executemany("INSERT INTO snacks VALUES (?, ?, ?)", [("Apple", "Fruit", 0.8), ("Banana", "Fruit", 0.5), ("Carrot", "Vegetable", 0.6), ("Cookie", "Treat", 1.2)])  # Question marks safely receive each tuple's values.
    connection.commit()  # Commit tells the database to keep the inserted rows for this session.
    return connection  # The ready connection goes back to the page.


database = get_connection()  # This creates the connection once or retrieves its cached copy.
kind = st.selectbox("Choose a food kind", options=["All", "Fruit", "Vegetable", "Treat"])  # This widget becomes our simple query filter.
query = "SELECT name, kind, price FROM snacks"  # This base query asks for all three display columns.
parameters = ()  # An empty tuple means there are no safe placeholder values yet.
if kind != "All":  # This branch adds a filter only when the visitor chooses one kind.
    query += " WHERE kind = ?"  # The question mark is a safe SQL parameter placeholder.
    parameters = (kind,)  # A one-item tuple supplies the value for that placeholder.

results = pd.read_sql_query(query, database, params=parameters)  # Pandas runs the query and returns a DataFrame.
st.dataframe(results, hide_index=True, width="stretch")  # This interactive grid shows the matching database records.
st.metric("Rows returned", len(results))  # This metric counts the records produced by the query.
st.code(query, language="sql")  # This code box reveals the SQL being taught.

with st.expander("What about st.connection?"):  # This hides the production-oriented note until requested.
    st.write("`st.connection()` reads connection settings from Streamlit secrets and can connect to SQL services and APIs.")  # This links the tiny lesson to the official abstraction.
    st.code("conn = st.connection('pets_db', type='sql')\ndf = conn.query('SELECT * FROM pets', ttl=600)", language="python")  # This shows connection name, type, query, and cache lifetime parameters.
    st.caption("`ttl=600` means a query result may be reused for 600 seconds.")  # This translates the time-to-live parameter.
