"""A tiny, beginner-friendly dinosaur classification app."""  # This sentence tells Python and learners what this file teaches.

import pandas as pd  # Pandas puts our dinosaur facts into a table.
import streamlit as st  # Streamlit turns normal Python into a web app.
from sklearn.neighbors import KNeighborsClassifier  # KNN finds the most similar known dinosaur.
from sklearn.pipeline import make_pipeline  # A pipeline joins data preparation and prediction.
from sklearn.preprocessing import StandardScaler  # Scaling gives large and small measurements a fair vote.

st.set_page_config(page_title="Dinosaur Classifier", page_icon="🦖")  # This sets the browser-tab name and icon.


@st.cache_data  # This remembers the small table so reruns do not rebuild it.
def load_dinosaurs():  # This function creates and returns our teaching dataset.
    return pd.DataFrame(  # A DataFrame is a spreadsheet-like table in Python.
        {  # This dictionary stores one table column under each heading.
            "dinosaur": ["Velociraptor", "Triceratops", "Stegosaurus", "Tyrannosaurus", "Brachiosaurus", "Ankylosaurus"],  # These are the answers the model may choose.
            "length_m": [2.0, 9.0, 9.0, 12.3, 22.0, 8.0],  # This column stores approximate body length in metres.
            "weight_kg": [15.0, 9000.0, 5000.0, 8000.0, 35000.0, 6000.0],  # This column stores approximate weight in kilograms.
            "walked_on_legs": [2, 4, 4, 2, 4, 4],  # This feature says whether two or four legs were normally used.
        }  # This closes the dictionary.
    )  # This closes DataFrame creation.


@st.cache_resource  # This remembers the fitted model, which is a reusable resource.
def train_model(data):  # This function learns from the dinosaur table it receives.
    features = ["length_m", "weight_kg", "walked_on_legs"]  # These are the clues given to the model.
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=1))  # Scaling runs first, then KNN picks the nearest example.
    model.fit(data[features], data["dinosaur"])  # Fit means “learn the link between clues and names.”
    return model, features  # The app needs both the trained model and the feature order.


dinosaurs = load_dinosaurs()  # This calls our data function and saves its returned table.
classifier, feature_names = train_model(dinosaurs)  # This trains the classifier once and saves it.

st.title("🦖 Dinosaur Classifier")  # A title tells the visitor what the page does.
st.write("Choose body measurements and the model finds the most similar dinosaur in its tiny table.")  # This explains the app in plain language.
st.caption("Teaching toy only: real palaeontology uses fossils and much richer evidence.")  # This warns that the model is intentionally simple.

length = st.slider("Body length (metres)", min_value=1.0, max_value=25.0, value=9.0, step=0.5, help="Move this to describe nose-to-tail length.")  # This collects a decimal length from the visitor.
weight = st.slider("Body weight (kilograms)", min_value=10, max_value=40000, value=5000, step=10, help="Large dinosaurs can weigh many thousands of kilograms.")  # This collects a whole-number weight.
legs = st.radio("Usually walked on", options=[2, 4], horizontal=True, format_func=lambda value: f"{value} legs")  # This lets the visitor choose two legs or four.

new_dinosaur = pd.DataFrame([[length, weight, legs]], columns=feature_names)  # The model expects one table row in the same column order used for training.
prediction = classifier.predict(new_dinosaur)[0]  # Predict asks KNN for the closest known dinosaur name.
match = dinosaurs.loc[dinosaurs["dinosaur"] == prediction].iloc[0]  # This finds the full row for the predicted dinosaur.

st.success(f"Closest match: **{prediction}**")  # A success box makes the main answer easy to spot.
left_column, right_column = st.columns(2)  # Columns place two small result cards beside each other.
left_column.metric("Known length", f"{match['length_m']:.1f} m")  # This compares the selected length with the stored example.
right_column.metric("Known weight", f"{match['weight_kg']:,.0f} kg")  # This compares the selected weight with the stored example.

with st.expander("See the tiny training table"):  # An expander hides details until the learner asks to see them.
    st.dataframe(dinosaurs, hide_index=True, width="stretch")  # This renders the complete dataset as an interactive table.
    st.write("`n_neighbors=1` means: choose the single nearest training example.")  # This translates the important model parameter into simple words.
