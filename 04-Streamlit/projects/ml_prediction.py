"""Mini-project 5: ML prediction with validation and probabilities."""

import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


st.set_page_config(page_title="ML Prediction", page_icon="🤖")


@st.cache_data
def iris_data():
    bunch = load_iris(as_frame=True)
    return bunch.frame, list(bunch.feature_names), list(bunch.target_names)


@st.cache_resource
def fitted_model(frame, features):
    model = LogisticRegression(max_iter=500, random_state=42)
    model.fit(frame[features], frame["target"])
    return model


frame, features, names = iris_data()
model = fitted_model(frame, features)
st.title("Iris ML Prediction")

with st.form("prediction"):
    values = {
        feature: st.number_input(
            feature.title(),
            min_value=float(frame[feature].min()),
            max_value=float(frame[feature].max()),
            value=float(frame[feature].median()),
            step=0.1,
        )
        for feature in features
    }
    submitted = st.form_submit_button("Predict", type="primary")

if submitted:
    one_row = pd.DataFrame([values], columns=features)
    predicted_index = int(model.predict(one_row)[0])
    probabilities = model.predict_proba(one_row)[0]
    st.metric("Prediction", names[predicted_index].title())
    st.bar_chart(pd.DataFrame({"species": names, "probability": probabilities}).set_index("species"))
    st.warning("Educational model only. Validate data and model quality before real decisions.")

