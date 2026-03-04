import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load LightGBM Model
# -----------------------------
model = joblib.load("California_homes.pkl")

# -----------------------------
# App Title
# -----------------------------
st.title("California Housing Price Prediction (Gradient Boosting)")

st.write("Enter the housing features below to predict the median house value.")

# -----------------------------
# User Input Form
# -----------------------------
with st.form("user_input"):

    MedInc = st.number_input("Median Income", min_value=0.0)
    HouseAge = st.number_input("House Age", min_value=0.0)
    AveRooms = st.number_input("Average Rooms", min_value=0.0)
    AveBedrms = st.number_input("Average Bedrooms", min_value=0.0)
    Population = st.number_input("Population", min_value=0.0)
    AveOccup = st.number_input("Average Occupancy", min_value=0.0)
    Latitude = st.number_input("Latitude")
    Longitude = st.number_input("Longitude")

    submit = st.form_submit_button("Predict")

# -----------------------------
# Prediction Logic
# -----------------------------
if submit:

    input_data = pd.DataFrame([[MedInc, HouseAge, AveRooms, AveBedrms,
                                Population, AveOccup, Latitude, Longitude]],
                              columns=[
                                  "MedInc", "HouseAge", "AveRooms", "AveBedrms",
                                  "Population", "AveOccup", "Latitude", "Longitude"
                              ])

    prediction = model.predict(input_data)

    st.subheader("Prediction Result")
    st.success(f"Predicted Median House Value: ${prediction[0] * 100000:,.2f}")