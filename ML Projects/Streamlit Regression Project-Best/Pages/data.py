import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_california_housing

@st.cache_data  # cache the data so it doesn't reload on every interaction
def load_data():
    housing = fetch_california_housing(as_frame=True)
    df = housing.frame  # includes features + target column "MedHouseVal"
    return df

df = load_data()

st.title("Data Explorer")


st.subheader("Dataset Preview")
st.dataframe(df.head(100), use_container_width=True)


st.subheader("Summary Statistics")
st.dataframe(df.describe(), use_container_width=True)


st.subheader("Target Distribution — Median House Value")
st.bar_chart(df["MedHouseVal"].value_counts(bins=50).sort_index())