import streamlit as st
import numpy as np
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(
    BASE_DIR,
    "models",
    "random_forest_model.pkl"
)

model = joblib.load(model_path)

st.title("📈 Stock Price Prediction")

st.write("Predict the next day's closing stock price")

open_price = st.number_input("Open Price")
high_price = st.number_input("High Price")
low_price = st.number_input("Low Price")
volume = st.number_input("Volume")

input_data = np.array([
    [open_price, high_price, low_price, volume]
])

if st.button("Predict Closing Price"):
    
    prediction = model.predict(input_data)

    st.success(
        f"Predicted Next Close Price: ${prediction[0]:.2f}"
    )