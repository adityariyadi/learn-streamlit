import streamlit as st
import pandas as pd

def run_eda_app():
    st.subheader("Exploratory Data Analysis")
    df = pd.read_csv("data/diabetes_data_upload.csv")
    st.dataframe(df)
