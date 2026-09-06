"""Practical ML demo: Iris classification with cached data and model.

Run:
    streamlit run classification.py

This model is a teaching example, not a real-world decision system.
"""

import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


st.set_page_config(page_title="Iris Predictor", page_icon="🌸")


@st.cache_data
def load_data():
    """Cache serializable data so reruns do not rebuild it unnecessarily."""
    iris = load_iris(as_frame=True)
    dataframe = iris.frame.rename(columns={"target": "species"})
    return dataframe, list(iris.target_names), list(iris.feature_names)


@st.cache_resource
def train_model(dataframe, feature_names):
    """Cache the model resource separately from cached data."""
    model = RandomForestClassifier(n_estimators=150, random_state=42)
    model.fit(dataframe[feature_names], dataframe["species"])
    return model


dataframe, target_names, feature_names = load_data()
model = train_model(dataframe, feature_names)

st.title("Iris Flower Prediction")
st.write("Move the sliders, then ask the trained model for a prediction.")

with st.sidebar:
    st.header("Input features")
    chosen_values = {}
    for feature in feature_names:
        chosen_values[feature] = st.slider(
            feature.title(),
            min_value=float(dataframe[feature].min()),
            max_value=float(dataframe[feature].max()),
            value=float(dataframe[feature].median()),
            step=0.1,
        )

input_data = pd.DataFrame([chosen_values], columns=feature_names)
prediction = int(model.predict(input_data)[0])
probabilities = model.predict_proba(input_data)[0]
predicted_species = target_names[prediction]

st.subheader("Your input")
st.dataframe(input_data, hide_index=True, width="stretch")
st.metric("Predicted species", predicted_species.title())

probability_data = pd.DataFrame(
    {"species": [name.title() for name in target_names], "probability": probabilities}
).set_index("species")
st.bar_chart(probability_data)
st.caption("A high model probability is confidence from this model—not a guarantee of truth.")
