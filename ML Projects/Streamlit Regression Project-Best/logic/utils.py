from pathlib import Path
import joblib
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import cross_validate
from xgboost import XGBRegressor
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATHS = {
    "Linear Regression": os.path.join(BASE_DIR, "models", "California_homesLR.pkl"),
    "Random Forest":     os.path.join(BASE_DIR, "models", "California_homesRF.pkl"),
    "Gradient Boosting": os.path.join(BASE_DIR, "models", "California_homesGB.pkl"),
    "XGBoost":           os.path.join(BASE_DIR, "models", "California_homesXGB.pkl"),
}

MODEL_CLASSES = {
    "Linear Regression": LinearRegression(),
    "Random Forest":     RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
    "XGBoost":           XGBRegressor(n_estimators=100, random_state=42, verbosity=0)
}

FEATURE_NAMES = [
    "MedInc", "HouseAge", "AveRooms", "AveBedrms",
    "Population", "AveOccup", "Latitude", "Longitude"
]


@st.cache_data
def load_data():
    housing = fetch_california_housing(as_frame=True)
    return housing.frame

# ── Models ────────────────────────────────────────────────────
@st.cache_resource
def load_all_models():
    return {name: joblib.load(path) for name, path in MODEL_PATHS.items()}


@st.cache_data
def evaluate_all_models():
    df = load_data()
    X  = df.drop(columns="MedHouseVal")
    y  = df["MedHouseVal"]
    models = load_all_models()

    results = []
    for name, model in models.items():
        preds = model.predict(X)
        results.append({
            "Model": name,
            "RMSE":  round(np.sqrt(mean_squared_error(y, preds)), 4),
            "MAE":   round(mean_absolute_error(y, preds), 4),
            "R²":    round(r2_score(y, preds), 4)
        })
    return results


def train_and_save(name, model, X, y):
    cv_results = cross_validate(
        model, X, y, cv=5,
        scoring=["neg_root_mean_squared_error", "neg_mean_absolute_error", "r2"],
        return_train_score=False
    )

    model.fit(X, y)

    save_path = MODEL_PATHS[name]
    save_path.parent.mkdir(exist_ok=True)
    joblib.dump(model, save_path)

    return {
        "Model": name,
        "RMSE":  round(-cv_results["test_neg_root_mean_squared_error"].mean(), 4),
        "MAE":   round(-cv_results["test_neg_mean_absolute_error"].mean(), 4),
        "R²":    round(cv_results["test_r2"].mean(), 4)
    }