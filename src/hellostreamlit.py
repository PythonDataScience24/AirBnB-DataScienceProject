import pandas as pd
import streamlit as st
import price


def display_price_summary():
    st.header('Prices')
    price_summary = price.PriceSummary('data/Airbnb_Open_Data.csv')
    st.text("Min price per night: " + str(price_summary.get_min_price_per_night()))
    st.text("Max price per night: " + str(price_summary.get_max_price_per_night()))
    st.text("Min costs for one night: " + str(price_summary.get_min_costs_for_one_night()))
    st.text("Max costs for one night: " + str(price_summary.get_max_costs_for_one_night()))


st.title("Figure out if we want to use streamlit")
display_price_summary()

st.header('Map')
df = pd.read_csv('data/Airbnb_Open_Data.csv')
df_10 = df.head(10).drop(columns=['house_rules'])
df_map = df.dropna(subset=['lat', 'long'])
df_map['Color'] = '#ffdd0040'
st.map(data=df_map, latitude='lat', longitude='long', size=1, color='Color')
# st.table(data=df_10)
