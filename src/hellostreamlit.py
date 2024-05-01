import pandas as pd
import streamlit as st
import price
import availability


def display_availability_percentage_per_neighbour_group():
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_Data.csv')
    st.header("Percentage of Listings with Availability more than 180 days in future per neighbour group")
    data = availability_summary.availability_per_neighbour_group_more_than(180)
    st.table(data=data)
    return


def display_mean_availability_per_room_type():
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_Data.csv')
    st.header("Mean availability per room type")
    data = availability_summary.mean_availability_per_room_type()
    st.table(data=data)
    return


def display_room_availabilities_with_more_than(values):
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_Data.csv')
    for value in values:
        data = availability_summary.room_availability_in_more_than_days(value)
        st.text(str(data) + "% of all listings still have " + str(value) + " or more days availability in future")


def display_listings_with_one_year_availabilities():
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_Data.csv')
    data = availability_summary.room_availability_in_exact_days(365)
    st.text(str(data) + "% of all listings still have 365 days availability")


def display_room_availability_with_less_than(days):
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_Data.csv')
    data = availability_summary.room_availability_less_than(days)
    st.text(str(data) + "% of all listings  have less than " + str(days) + " days availability in future")


def display_room_types_with_zero_availability():
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_Data.csv')
    data = availability_summary.percentage_no_availability_per_type()
    st.header("Percentage of Listings with no availability per room type")
    st.table(data=data)
    return


if __name__ == '__main__':
    # display_price_summary()
    display_availability_percentage_per_neighbour_group()
    display_mean_availability_per_room_type()
    display_room_types_with_zero_availability()
    st.header("Some more Informations about availability in the next 365 days")
    display_room_availabilities_with_more_than([180, 90])
    display_room_availability_with_less_than(30)
    display_listings_with_one_year_availabilities()
