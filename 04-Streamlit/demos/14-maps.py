"""Simple map components using a few Indian city coordinates."""  # This names the topic and the data used.

import pandas as pd  # Pandas stores city names and coordinates in a table.
import streamlit as st  # Streamlit displays controls, metrics, data, and maps.

st.set_page_config(page_title="Maps Demo", page_icon="🗺️")  # This selects the browser-tab title and icon.
st.title("🗺️ Maps")  # This shows the page heading.

cities = pd.DataFrame(  # This creates a tiny location dataset.
    {  # Each dictionary key becomes a column name.
        "city": ["New Delhi", "Mumbai", "Bengaluru", "Kolkata", "Chennai"],  # These labels identify the points.
        "lat": [28.6139, 19.0760, 12.9716, 22.5726, 13.0827],  # Latitude says how far north or south each city is.
        "lon": [77.2090, 72.8777, 77.5946, 88.3639, 80.2707],  # Longitude says how far east or west each city is.
        "students": [120, 95, 140, 80, 110],  # This extra value will control point size.
    }  # This closes the data dictionary.
)  # This closes DataFrame creation.

selected_city = st.selectbox("Focus on a city", options=cities["city"], help="A selectbox allows exactly one choice.")  # This widget chooses the highlighted city.
selected_row = cities[cities["city"] == selected_city]  # This filter keeps only the matching table row.
st.metric("Students in the sample", int(selected_row["students"].iloc[0]))  # This card displays one value from the selected row.
st.map(cities, latitude="lat", longitude="lon", size="students", color="#ff4b4b", zoom=3)  # These parameters name coordinate columns, point size, colour, and zoom.
st.dataframe(cities, hide_index=True, width="stretch")  # The table lets learners inspect the exact numbers behind the map.
st.caption("Map data needs latitude and longitude columns. Latitude is north/south; longitude is east/west.")  # This repeats the key coordinate idea.
