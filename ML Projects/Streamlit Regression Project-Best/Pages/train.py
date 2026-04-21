import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from logic.utils import load_data, BASE_DIR

st.title("Train Models")

MODEL_REGISTRY = {
    "Linear Regression": LinearRegression(),
    "Random Forest":     RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
    "XGBoost":           XGBRegressor(n_estimators=100, random_state=42, verbosity=0),
}

SAVE_PATHS = {
    "Linear Regression": os.path.join(BASE_DIR, "models", "California_homesLR.pkl"),
    "Random Forest": os.path.join(BASE_DIR, "models", "California_homesRF.pkl"),
    "Gradient Boosting": os.path.join(BASE_DIR, "models", "California_homesGB.pkl"),
    "XGBoost":  os.path.join(BASE_DIR, "models", "California_homesXGB.pkl"),
}

st.subheader("Select Models to Train")
selected_models = []
cols = st.columns(4)
for i, name in enumerate(MODEL_REGISTRY.keys()):
    with cols[i]:
        if st.checkbox(name, value=True):
            selected_models.append(name)

cv_folds = st.slider("Cross-validation folds", min_value=2, max_value=5, value=5)

if st.button("Train Selected Models", disabled=len(selected_models) == 0):
    df = load_data()
    X  = df.drop(columns="MedHouseVal")
    y  = df["MedHouseVal"]
    results = []

    for name in selected_models:
        model = MODEL_REGISTRY[name]

        with st.spinner(f"Training {name}..."):
            model.fit(X, y)

            cv_scores = cross_val_score(model, X, y, cv=cv_folds, scoring="neg_mean_absolute_error")
            cv_mae    = round(-cv_scores.mean(), 4)
            cv_std    = round(cv_scores.std(), 4)

            preds = model.predict(X)
            mae   = round(mean_absolute_error(y, preds), 4)
            rmse  = round(np.sqrt(mean_squared_error(y, preds)), 4)