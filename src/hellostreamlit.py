import pandas as pd
import streamlit as st

# we're testing whether we can display data

st.title("Figure out if we want to use streamlit")

df = pd.read_csv('data/Airbnb_Open_Data.csv')
df_10 = df.head(10).drop(columns=['house_rules'])
df_map = df.dropna(subset=['lat', 'long'])

st.map(data=df_map, latitude='lat', longitude='long', size=1)
st.table(data=df_10)
