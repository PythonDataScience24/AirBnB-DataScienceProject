""" Displays all general information about all AirBnBs such as 
    existing AirBnBs, price, availability and rating
"""
from typing import List

import pandas as pd
import streamlit as st
import airbnb_summary
import price
import availability
import rating


# imports need to be this way because of streamlit

def display_map():
    """ Displays a Map from NYC with all AirBnBs """
    st.header('Map')
    st.write('The following map shows the location of the AirBnBs in New York City.')
    df = pd.read_csv('data/Airbnb_Open_Data.csv')
    df_map = df.dropna(subset=['lat', 'long'])
    st.map(data=df_map, latitude='lat', longitude='long', size=1)


def display_airbnb_summary():
    """ diplays a table with an overview for AirBnBs for each neighbourhood group"""
    st.subheader('Available AirBnBs in NYC')
    airbnb_summ = airbnb_summary.AirBnBSummary('data/Airbnb_Open_processed_Data.csv')
    number = airbnb_summ.get_total_airbnbs()
    st.text(f"In NYC you can choose between {number} different AirBnbs")
    st.text("The following table shows you the number of available AirBnbs per neighbourhood")
    data = airbnb_summ.get_airbnbs_per_nhood()
    st.table(data=data)


def display_price_summary():
    """ displays a table with general information about the price """
    st.subheader('Prices')
    price_summary = price.PriceSummary('data/Airbnb_Open_processed_Data.csv')
    number_of_nan_prices = price_summary.get_number_of_nan_prices()
    total_number_of_listings = price_summary.get_total_number_of_listings()
    non_nan_prices = total_number_of_listings - number_of_nan_prices
    price_summary.clean_data()
    st.write(f"{total_number_of_listings} listings are available in New York City. "
             f" {non_nan_prices} provide pricing information. "
             "In the following pricing summary, "
             + "only listings with pricing information are considered.")
    st.write("Accommodations are available in the following price range:")
    st.table(price_summary.get_summary_table())


def display_availability_percentage_per_neighbour_group():
    """ displays table with percentage of listings of AirBnB
        with availability > 180 days per nhood group 
    """
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_processed_Data.csv')
    st.subheader("Percentage of Listings with Availability more than 180 days "
                 + "in future per neighbour group")
    data = availability_summary.availability_per_neighbour_group_more_than(180)
    st.table(data=data)


def display_mean_availability_per_room_type():
    """ displays table with mean availability per room type"""
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_processed_Data.csv')
    st.subheader("Mean availability per room type")
    data = availability_summary.mean_availability_per_room_type()
    st.table(data=data)


def display_room_availabilities_with_more_than(values: List):
    """ displays table with percentage of AirBnBs with more than values days
    Args:
        values (int): min value of available days
    """
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_processed_Data.csv')
    for value in values:
        data = availability_summary.room_availability_more_than(value)
        st.text(str(data) + "% of all listings still have " + str(value)
                + " or more days availability in future")


def display_room_with_one_year_availabilities():
    """ diplays percentage of AirBnBs that can be rented for one year """
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_processed_Data.csv')
    data = availability_summary.room_availability_in_exact_days(365)
    st.write(str(data.shape[0]) + " rooms can still be rented for one year")


def display_room_availability_with_less_than(days):
    """ displays table with percentage of AirBnB that are less than days available

    Args:
        days (int): max days for availability
    """
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_processed_Data.csv')
    data = availability_summary.room_availability_less_than(days)
    st.text(str(data) + "% of all listings  have less than " + str(days)
            + " days availability in future")


def display_room_types_with_zero_availability():
    """ displays table with percentage of AirBnBs with no days availability"""
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_processed_Data.csv')
    data = availability_summary.percentage_no_availability_per_type()
    st.subheader("Percentage of Listings with no availability per room type")
    st.table(data=data)


def display_room_with_max_availability():
    """ displays information about maximal availability """
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_processed_Data.csv')
    (type, max_value) = availability_summary.room_type_with_max_availability()
    st.subheader("Room Type with max availability")
    st.write("Book now a room with type " + str(type) + ", this type still has "
             + str(max_value) + " days of availability")


def display_room_with_min_availability():
    """ displays information about minimal availability """
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_processed_Data.csv')
    (type, min_value) = availability_summary.room_type_with_min_availability()
    st.subheader("Room Type with min availability")
    st.write("Don't miss it and book now a room with type " + str(type) + ", this type only has "
             + str(min_value) + " days left of availability")


def display_rating_summary():
    """ displays and greate table with information about average, min and max rating
        gives information about percentage of AirBnBs over and under average rating,
        under max rating and over min rating 
    """
    rating_summary = rating.RatingSummary('data/Airbnb_Open_processed_Data.csv')
    rating_summary.clean_data()
    st.subheader("The Average Rating for all AirBnbs")
    avr = rating_summary.average_rating()
    higher = rating_summary.percentage_rating_over_average()
    lower = rating_summary.percentage_rating_under_average()
    values = [str(avr), str(higher) + " %", str(lower) + " %"]
    index = ['Average Rating', 'Percentage of Higher Ratings',
             'Percentage of Lower Rating'
             ]
    average = pd.DataFrame({'Values': values}, index=index)
    st.table(average)
    st.subheader("General Information about Minimal and Maximal Rating")
    min_rating = rating_summary.min_rating()
    over_min = rating_summary.percentage_over_min_rating()
    max_rating = rating_summary.max_rating()
    under_max = rating_summary.percentage_under_max_rating()
    values = [str(min_rating), str(over_min) + " %", str(max_rating), str(under_max) + " %"]
    index = ['Lowest Rating', 'Percentage of Higher Rating',
             'Highest Rating', 'Percentage of Lower Rating'
             ]
    rating_df = pd.DataFrame({
        'Values': values},
        index=index)
    st.table(rating_df)


def display_room_availability_with_price_between_and_more_than():
    """ gives short summary about prices and availability """
    st.subheader('Check prices and availability in one shot')
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_processed_Data.csv')
    data = availability_summary.room_availability_when_price_is_between(60, 200, 180)
    if data < 50:
        st.write("Don't loose more time there are only " + str(data) + "% "
                 + "rooms left with more than 180 days availability "
                 + "which cost between 60 and 200 Dollar")
    else:
        st.write(str(data) + "%" + "of all rooms which cost between 50 Dollar "
                 + "and 100 Dollar still have more than 180 days availability left")


if __name__ == '__main__':
    st.set_page_config(page_title="AirBNB in New York City")
    st.title("AirBNB in New York City")
    display_map()
    st.header("AirBnB Summary")
    display_airbnb_summary()
    st.header("Price Summary")
    display_price_summary()
    st.header("Availability Summary")
    display_availability_percentage_per_neighbour_group()
    display_mean_availability_per_room_type()
    display_room_types_with_zero_availability()
    st.header("Some more information about room availability in the next 365 days")
    display_room_availabilities_with_more_than([180, 90])
    display_room_availability_with_less_than(30)
    display_room_with_one_year_availabilities()
    display_room_with_max_availability()
    display_room_with_min_availability()
    display_room_availability_with_price_between_and_more_than()
    st.header("Rating Summary")
    display_rating_summary()
