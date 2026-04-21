import streamlit as st
import pandas as pd
import numpy as np
from logic.utils import load_all_models, FEATURE_NAMES

st.title("Predict House Prices")


models = load_all_models()


st.subheader("Select Model")
default = st.session_state.get("best_model", "XGBoost") 
selected_model_name = st.selectbox("Model", list(models.keys()), index=list(models.keys()).index(default))
model = models[selected_model_name]


st.subheader("Enter House Features")

col1, col2 = st.columns(2)
with col1:
        MedInc     = st.number_input("Median Income (MedInc)",         min_value=0.0, value=3.0,   step=0.1)
        HouseAge   = st.number_input("House Age (HouseAge)",           min_value=0.0, value=20.0,  step=1.0)
        AveRooms   = st.number_input("Average Rooms (AveRooms)",       min_value=0.0, value=5.0,   step=0.1)
        AveBedrms  = st.number_input("Average Bedrooms (AveBedrms)",   min_value=0.0, value=1.0,   step=0.1)
with col2:
        Population = st.number_input("Population",                     min_value=0.0, value=1000.0,step=10.0)
        AveOccup   = st.number_input("Average Occupants (AveOccup)",   min_value=0.0, value=3.0,   step=0.1)
        Latitude   = st.number_input("Latitude",                       min_value=32.0, max_value=42.0, value=36.0, step=0.1)
        Longitude  = st.number_input("Longitude",                      min_value=-125.0, max_value=-114.0, value=-119.0, step=0.1)
if st.button("Predict"):
        input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms,
                                 Population, AveOccup, Latitude, Longitude]])
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Median House Value: **${round(float(prediction) * 100_000, 2):,}**")
        st.caption("The model outputs in hundreds of thousands of USD — multiplied by 100,000 for display.")