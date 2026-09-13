
import streamlit as st
import joblib
import pandas as pd

# Load trained Decision Tree model
model = joblib.load("diabetes_model.pkl")

# Page title
st.set_page_config(
    page_title="Diabetes Prediction AI",
    page_icon="🩺"
)

st.title("🩺 Diabetes Prediction using AI")
st.write("Enter the patient's information to predict diabetes.")

st.subheader("Patient Information")

# Input fields
pregnancies = st.number_input(
    "Pregnancies",
    min_value=0,
    max_value=20,
    value=1
)

glucose = st.number_input(
    "Glucose",
    min_value=0,
    max_value=300,
    value=120
)

blood_pressure = st.number_input(
    "Blood Pressure",
    min_value=0,
    max_value=200,
    value=70
)

skin_thickness = st.number_input(
    "Skin Thickness",
    min_value=0,
    max_value=100,
    value=20
)

insulin = st.number_input(
    "Insulin",
    min_value=0,
    max_value=900,
    value=80
)

bmi = st.number_input(
    "BMI",
    min_value=0.0,
    max_value=70.0,
    value=25.0
)

diabetes_pedigree = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    max_value=3.0,
    value=0.5
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=30
)

# Prediction button
if st.button("🔍 Predict Diabetes"):

    input_data = pd.DataFrame([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]], columns=[
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age"
    ])

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ The model predicts a higher likelihood of diabetes.")
    else:
        st.success("✅ The model predicts a lower likelihood of diabetes.")

st.info(
    "This application is for educational purposes and is not a medical diagnosis."
)
