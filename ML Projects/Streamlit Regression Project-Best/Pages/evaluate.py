import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from logic.utils import load_all_models, evaluate_all_models


st.title("📈 Model Evaluation")

results = evaluate_all_models()
df_results = pd.DataFrame(results)
df_results = df_results.sort_values(["MAE", "RMSE"], ascending=[True, True]).reset_index(drop=True)
best_model_name = df_results.iloc[0]["Model"]


st.subheader("🏆 Leaderboard")
st.caption(f"Best model: **{best_model_name}** — ranked by lowest MAE, RMSE as tiebreaker")

def highlight_best(row):
    return ["background-color: #d4edda" if row["Model"] == best_model_name else "" for _ in row]

st.dataframe(
    df_results.style.apply(highlight_best, axis=1),
    use_container_width=True
)


st.subheader("🔍 Residual & Prediction Plots")
selected_model_name = st.selectbox("Select a model to inspect", df_results["Model"])
model = load_all_models()[selected_model_name]


housing  = fetch_california_housing(as_frame=True)
X        = housing.frame.drop(columns="MedHouseVal")
y        = housing.frame["MedHouseVal"]
preds    = model.predict(X)
residuals = y - preds


col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    ax.scatter(y, preds, alpha=0.3, s=5)
    ax.plot([y.min(), y.max()], [y.min(), y.max()], "r--")
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title("Actual vs Predicted")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    ax.scatter(preds, residuals, alpha=0.3, s=5)
    ax.axhline(0, color="r", linestyle="--")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Residuals")
    ax.set_title("Residual Plot")
    st.pyplot(fig)


st.subheader("🔎 Feature Importance")

if hasattr(model, "feature_importances_"):
    importance_df = pd.DataFrame({
        "Feature":    X.columns,
        "Importance": model.feature_importances_
    }).sort_values("Importance", ascending=False)
    st.bar_chart(importance_df.set_index("Feature"))
else:
    st.info(f"{selected_model_name} doesn't support feature importance — expected for Linear Regression.")