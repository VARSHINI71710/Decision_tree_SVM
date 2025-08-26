import streamlit as st
import pickle
import numpy as np

svc, scaler, le = pickle.load(open('trained_model.sav', 'rb'))

st.title("🌸 Iris Flower Classification App")
st.write("Enter the measurements below to predict the type of Iris flower:")

sepal_length = st.number_input("Sepal Length (cm):", min_value=4.3, max_value=7.9, value=5.1)
sepal_width = st.number_input("Sepal Width (cm):", min_value=2.0, max_value=4.4, value=3.5)
petal_length = st.number_input("Petal Length (cm):", min_value=1.0, max_value=6.9, value=1.4)
petal_width = st.number_input("Petal Width (cm):", min_value=0.1, max_value=2.5, value=0.2)

features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
features_scaled = scaler.transform(features)

if st.button("Predict Flower"):
    prediction_numeric = svc.predict(features_scaled)
    predicted_flower = le.inverse_transform(prediction_numeric)[0]  # Convert numeric label back to species
    st.success(f"🌼 The predicted Iris flower is: **{predicted_flower}**")

# Optional: show sample prediction
if st.button("Try Sample Input [5.5, 3.0, 4.2, 1.3]"):
    sample = np.array([[5.5, 3.0, 4.2, 1.3]])
    sample_scaled = scaler.transform(sample)
    sample_prediction = svc.predict(sample_scaled)
    sample_flower = le.inverse_transform(sample_prediction)[0]
    st.info(f"Sample Prediction: **{sample_flower}**")
