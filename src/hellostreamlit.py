import streamlit as st
import pandas as pd

#we're testing whether we can display data

st.title("Figure out if we want to use streamlit")

st.map()
df = pd.read_csv('data/Airbnb_Open_Data.csv')
df_10 = df.head(10)
st.table(data=df_10)

