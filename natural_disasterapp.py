import streamlit as st
import pandas as pd
from joblib import load

# Load model
model = load("preparedness_model.joblib")

st.title("Disaster Preparedness Predictor")

# Collect user input
age = st.selectbox("Are you 60 or older?", ["No", "Yes"])
socio = st.selectbox("Socioeconomically Disadvantaged?", ["No", "Yes"])
home = st.selectbox("Homeownership?", ["Renter", "Homeowner"])
edu = st.selectbox("Education Level", ["<HS", "HS", "Some College", "BA", "Grad"])
race = st.selectbox("Race", ["White", "Black", "Latino", "Asian", "Other"])
lang = st.selectbox("Primary Language", ["English", "Other"])

# Convert input to model-ready format
input_df = pd.DataFrame([{
    'socioeconomically_disadvantaged': 1 if socio == "Yes" else 0,
    'homeownership': 1 if home == "Homeowner" else 0,
    'education': ["<HS", "HS", "Some College", "BA", "Grad"].index(edu),
    'race_selfid': ["White", "Black", "Latino", "Asian", "Other"].index(race),
    'englishlang': 0 if lang == "Other" else 1,
    'sixtyplus': 1 if age == "Yes" else 0
}])

# Prediction
if st.button("Predict"):
    pred = model.predict(input_df)[0]
    st.success("Prepared" if pred == 1 else "Unprepared")
