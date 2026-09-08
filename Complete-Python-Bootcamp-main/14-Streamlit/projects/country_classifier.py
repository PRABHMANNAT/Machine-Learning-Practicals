"""A tiny country guesser that mirrors the Iris classifier structure."""  # This describes the purpose of the file.

import pandas as pd  # Pandas creates the table of country coordinates.
import streamlit as st  # Streamlit supplies the page, sliders, map, and result boxes.
from sklearn.neighbors import KNeighborsClassifier  # KNN chooses the nearest known capital coordinate.

st.set_page_config(page_title="Country Guesser", page_icon="🌍")  # This chooses the browser-tab label and emoji.


@st.cache_data  # This keeps the same little dataset ready between widget reruns.
def load_countries():  # This function makes our deliberately small learning table.
    return pd.DataFrame(  # A DataFrame stores rows and named columns like a spreadsheet.
        {  # This dictionary supplies each column of the table.
            "country": ["India", "Japan", "Australia", "Egypt", "Kenya", "France", "United Kingdom", "Brazil", "Canada", "Mexico"],  # These are the country labels the model knows.
            "capital": ["New Delhi", "Tokyo", "Canberra", "Cairo", "Nairobi", "Paris", "London", "Brasilia", "Ottawa", "Mexico City"],  # Capital names make the coordinates meaningful.
            "lat": [28.61, 35.68, -35.28, 30.04, -1.29, 48.86, 51.51, -15.79, 45.42, 19.43],  # Latitude measures north and south position.
            "lon": [77.21, 139.65, 149.13, 31.24, 36.82, 2.35, -0.13, -47.88, -75.70, -99.13],  # Longitude measures east and west position.
        }  # This closes the column dictionary.
    )  # This closes DataFrame creation.


@st.cache_resource  # This caches the fitted model instead of fitting it after every slider move.
def train_model(data):  # This function learns coordinate-to-country examples.
    model = KNeighborsClassifier(n_neighbors=1)  # One neighbour means “pick the closest capital in the table.”
    model.fit(data[["lat", "lon"]], data["country"])  # The two coordinate columns are clues and country is the answer.
    return model  # The trained model is returned to the page.


countries = load_countries()  # This gets the coordinate table.
model = train_model(countries)  # This trains or retrieves the cached nearest-neighbour model.

st.title("🌍 Country Coordinate Classifier")  # This large heading names the lesson.
st.write("Pick a latitude and longitude. The model guesses the country whose listed capital is closest.")  # This explains exactly what “classification” means here.
st.caption("This is a geography practice toy, not a border lookup service.")  # This states the model's important limitation.

latitude = st.slider("Latitude", min_value=-60.0, max_value=70.0, value=28.6, step=0.1, help="Positive is north; negative is south.")  # This lets the visitor move north or south.
longitude = st.slider("Longitude", min_value=-180.0, max_value=180.0, value=77.2, step=0.1, help="Positive is east; negative is west.")  # This lets the visitor move east or west.
chosen_point = pd.DataFrame({"lat": [latitude], "lon": [longitude]})  # A one-row table is the shape scikit-learn expects.
prediction = model.predict(chosen_point)[0]  # This asks for the nearest learned country label.
capital = countries.loc[countries["country"] == prediction, "capital"].iloc[0]  # This looks up the matching capital name.

st.success(f"Closest example country: **{prediction}**")  # This highlights the guessed country.
st.metric("Nearest listed capital", capital)  # This metric card shows why that country was selected.
st.map(pd.concat([countries[["lat", "lon"]], chosen_point], ignore_index=True), zoom=1)  # This draws the known capitals plus the selected point on a map.

with st.expander("See the examples the model knows"):  # This keeps the training data available without crowding the page.
    st.dataframe(countries, hide_index=True, width="stretch")  # This shows all labels and coordinates in an interactive table.
    st.write("Try New Delhi: latitude `28.6`, longitude `77.2`.")  # This gives the learner a quick experiment.
