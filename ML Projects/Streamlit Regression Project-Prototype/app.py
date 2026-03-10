import streamlit as st
import pandas as pd
import joblib

# -----------------------------

# -----------------------------
model = joblib.load("California homes gb.pkl")

# -----------------------------
# App Title
# -----------------------------
st.title("California Housing Price Prediction ")

st.write("Enter the housing features below to predict the median house value.")

# -----------------------------
# User Input Form
# -----------------------------
with st.form("user_input"):

    MedInc = st.number_input("Median Income", min_value=0.0, value=None, placeholder="Enter value")
    HouseAge = st.number_input("House Age", min_value=0.0, value=None)
    AveRooms = st.number_input("Average Rooms", min_value=0.0, value=None)
    AveBedrms = st.number_input("Average Bedrooms", min_value=0.0, value=None)
    Population = st.number_input("Population", min_value=0.0, value=None)
    AveOccup = st.number_input("Average Occupancy", min_value=0.0, value=None)
    Latitude = st.number_input("Latitude", value=None)
    Longitude = st.number_input("Longitude", value=None)

    submit = st.form_submit_button("Predict")

# -----------------------------
# Prediction Logic
# -----------------------------
if submit:

    values = [MedInc, HouseAge, AveRooms, AveBedrms,
              Population, AveOccup, Latitude, Longitude]

    if None in values:
        st.error("Please enter all values before predicting.")
    else:
        input_data = pd.DataFrame([values], columns=[
            "MedInc", "HouseAge", "AveRooms", "AveBedrms",
            "Population", "AveOccup", "Latitude", "Longitude"
        ])

        prediction = model.predict(input_data)

        st.subheader("Prediction Result")
        st.success(f"Predicted Median House Value: ${prediction[0]*100000:,.2f}")