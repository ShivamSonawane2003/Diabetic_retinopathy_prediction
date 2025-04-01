#!/usr/bin/env python
# coding: utf-8
import streamlit as st
import pickle
import numpy as np

# Load the trained SVM model
with open("svm_best_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load the scaler
with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# Streamlit UI
st.title("Diabetic Retinopathy Prediction")
st.write("Enter patient details to predict diabetic retinopathy risk.")

# User Inputs
age = st.number_input("Age", min_value=1.0, max_value=120.0, value=40.0, format="%.2f")
systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=50.0, max_value=250.0, value=120.0, format="%.2f")
diastolic_bp = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=30.0, max_value=150.0, value=80.0, format="%.2f")
cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=50.0, max_value=400.0, value=180.0, format="%.2f")

input_data = np.array([[age, systolic_bp, diastolic_bp, cholesterol]])


# Predict button
if st.button("Predict"):

    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display result
    if prediction == 1:
        st.error("The patient may have Diabetic Retinopathy.")
    else:
        st.success("The patient may not have Diabetic Retinopathy.")