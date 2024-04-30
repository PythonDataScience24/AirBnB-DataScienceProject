import pandas as pd
import numpy as np
import streamlit as st
import price
import airbnb_summary as airsum


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

def display_listingAirbnb_summary():
    st.header("Overview of available AirBnBs")
    data = pd.read_csv('data/Airbnb_Open_Data.csv')
    data = airsum.clean_data(data)
    #airbnb_summary.clean_data()
    # st.text(f"There are {airbnb_summary.get_total_AirBnB()} AirBnbs in NYC")


def calculate_color(value, max_value):
    # Normalize the value to be between 0 and 1
    normalized_value = (value/max_value)
    # Calculate the color gradient from red to green
    r = 255
    g = 255
    b = 0
    print("#"+hex(r)+hex(g)+hex(b))
    #return "#"+hex(r)+hex(g)+hex(b)
    return "ff0000"


st.title("AirBnBs in NYC")
display_listingAirbnb_summary()
display_price_summary()

st.header('Map')
df = pd.read_csv('data/Airbnb_Open_Data.csv')
df_10 = df.head(10).drop(columns=['house_rules'])
df_map = df.dropna(subset=['lat', 'long'])
price_summary = price.PriceSummary('data/Airbnb_Open_Data.csv')
price_summary.clean_data()
max_price = price_summary.get_max_price_per_night()[0]
df_map['price'] = df_map['price'].fillna('-1')
df_map['price'] = df['price'].str.replace('$','').str.replace(',','')
print(df_map['price'])
#df_map['price'] = df_map['price'].astype(float)
#df_map['Color'] = np.where(df_map['price'] == -1, "#ffffff40", calculate_color(df_map['price'], max_price))
st.map(data=df_map, latitude='lat', longitude='long', size=1)
# st.table(data=df_10)

# calculate_color(int(df['price'].str.replace('$','').str.replace(',','')), max_price)

