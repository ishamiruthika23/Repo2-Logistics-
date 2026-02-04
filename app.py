import streamlit as st
import numpy as np
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, "logistic_model.pkl"), "rb"))
scaler = pickle.load(open(os.path.join(BASE_DIR, "scaler.pkl"), "rb"))

st.set_page_config(page_title="Heart Disease Prediction")
st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient details to predict heart disease risk")

male = st.selectbox("Gender", ["Female", "Male"])
age = st.number_input("Age", min_value=1, max_value=120, value=30)

currentSmoker = st.selectbox("Current Smoker", ["No", "Yes"])
cigsPerDay = st.number_input("Cigarettes per Day", min_value=0, max_value=100, value=0)

BPMeds = st.selectbox("On BP Medication", ["No", "Yes"])
prevalentStroke = st.selectbox("History of Stroke", ["No", "Yes"])
prevalentHyp = st.selectbox("Hypertension", ["No", "Yes"])
diabetes = st.selectbox("Diabetes", ["No", "Yes"])

totChol = st.number_input("Total Cholesterol", value=200)
sysBP = st.number_input("Systolic BP", value=120)
diaBP = st.number_input("Diastolic BP", value=80)
BMI = st.number_input("BMI", value=25.0)
heartRate = st.number_input("Heart Rate", value=70)
glucose = st.number_input("Glucose Level", value=80)

input_data = [
    1 if male == "Male" else 0,
    age,
    1 if currentSmoker == "Yes" else 0,
    cigsPerDay,
    1 if BPMeds == "Yes" else 0,
    1 if prevalentStroke == "Yes" else 0,
    1 if prevalentHyp == "Yes" else 0,
    1 if diabetes == "Yes" else 0,
    totChol,
    sysBP,
    diaBP,
    BMI,
    heartRate,
    glucose
]

if st.button("Predict"):
    input_array = np.array(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")