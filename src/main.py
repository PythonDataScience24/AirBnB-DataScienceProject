import pandas as pd
import numpy as np
import streamlit as st
import price


def display_price_summary():
    st.header('Prices')
    price_summary = price.PriceSummary('data/Airbnb_Open_Data.csv')
    number_of_nan_prices = price_summary.get_number_of_nan_prices()
    total_number_of_listings = price_summary.get_total_number_of_listings()
    non_nan_prices = total_number_of_listings - number_of_nan_prices
    price_summary.clean_data()
    st.text(f"Prices for {non_nan_prices} out of {total_number_of_listings} listings are available.")
    st.text(f"Min price per night: {price_summary.get_min_price_per_night()}\n" +
            f"Max price per night: {price_summary.get_max_price_per_night()}")
    st.text(f"Min costs for one night: {price_summary.get_min_costs_for_one_night()}\n" +
            f"Max costs for one night: {price_summary.get_max_costs_for_one_night()}")


def display_map():
    st.header('Map')
    df = pd.read_csv('data/Airbnb_Open_Data.csv')
    df_map = df.dropna(subset=['lat', 'long'])
    st.map(data=df_map, latitude='lat', longitude='long', size=1)


st.title("Figure out if we want to use streamlit")
display_price_summary()
display_map()
