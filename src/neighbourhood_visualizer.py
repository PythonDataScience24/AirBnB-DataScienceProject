"""
    This clas has the following functions and responsibility:
    visualizes information about the selected neighbourhood
"""
import pandas as pd
import streamlit as st

from airbnb_summary import AirBnBSummary
from availability import AvailabilitySummary
from price import PriceSummary
from rating import RatingSummary


class NeighbourhoodVisualizer:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.availability_summary = self.get_availability_summary_of_selection()
        self.price_summary = self.get_price_summary_of_selection()
        self.airbnb_summary = self.get_overall_summary_of_selection()
        self.rating_summary = self.get_rating_summary_of_selection()

    def get_availability_summary_of_selection(self) -> AvailabilitySummary:
        """ Returns a AvailabilitySummary of the selected neighbourhood and room type."""
        availability_summary: AvailabilitySummary = AvailabilitySummary(
            df=self.df.copy())
        availability_summary.clean_data()
        return availability_summary

    def get_price_summary_of_selection(self) -> PriceSummary:
        """ Returns a PriceSummary of the selected neighbourhood and room type."""
        price_summary: PriceSummary = PriceSummary(df=self.df.copy())
        price_summary.clean_data()
        return price_summary

    def get_overall_summary_of_selection(self) -> AirBnBSummary:
        """ Returns a AirBnBSummary of the selected neighbourhood and room type."""
        overall_summary: AirBnBSummary = AirBnBSummary(df=self.df.copy())
        overall_summary.clean_data()
        return overall_summary

    def get_rating_summary_of_selection(self) -> RatingSummary:
        """ Returns a RatingSummary of the selected neighbourhood and room type."""
        rating_summary: RatingSummary = RatingSummary(df=self.df.copy())
        rating_summary.clean_data()
        return rating_summary

    def visualize_filtered_dataframe(self):
        """ Returns a visualization of the dataframe filtered
        by the neighbourhood and room type"""
        st.dataframe(self.df)

    def visualize_min_max_price_summary(self):
        """
        Creates a table which visualizes the
        accommodations with the max and min price
        """
        (name_max, max_price, service_fee_max) = self.price_summary.get_max_price_per_night()
        (name_min, min_price, service_fee_min) = self.price_summary.get_min_price_per_night()
        st.subheader("Min and Max Price per Night")
        df = pd.DataFrame({'Price in $': [max_price, min_price],
                           'service_fee': [service_fee_max, service_fee_min],
                           'Accommodation': [name_max, name_min]},
                          index=["Max Price", "Min Price"])
        st.table(df)

    def visualize_neighbourhood_availability(self):
        """
        visualizes how many percentage of the listings
            in the selected neighbourhood have still
            more than days of availability in future
        Keyword arguments:
            days -- days of availability
        """
        st.subheader("Availability")
        result = self.availability_summary.room_availability_more_than(days=180)
        result1 = self.availability_summary.room_availability_less_than(90)
        result2 = self.availability_summary.room_availability_less_than(0)
        st.write(str(result) + " % of all rooms in this neighbourhood with the "
                               "selected room type still have more than 180 days " +
                 " availability in future and " + str(result1) +
                 "% of all rooms in this neighbourhood with the "
                 "selected room type have less than 90 days "
                 "availability in future")
        st.write(str(result2) + " % of all rooms have no availability anymore")

    def visualize_rooms_with_one_year_availability(self):
        """
            visualizes a dataframe with rooms which still have 365 days of availability
            in future
        """
        df = self.availability_summary.room_availability_in_exact_days(365).reset_index()
        if df.shape[0] == 0:
            return
        st.subheader("The following rooms can still be rented for one year")
        st.dataframe(df)

    def visualize_mean_median_price_summary(self):
        """visualizes a table with median price per night and average price per night"""
        avg_price = self.price_summary.get_mean_price_per_night()
        median = self.price_summary.get_median_price_for_one_night()
        df = pd.DataFrame({'price in $': [avg_price, median]},
                          index=["average price", "median Price"])
        st.subheader("Median and average price per night")
        st.table(df)
    
    def visualize_mean_availability(self):
        """
        visualizes mean availability in days
        """
        mean_availability = self.availability_summary.mean_availability()
        st.write("Average availability in days: " + str(round(mean_availability)))
        
    def visualize_rating(self):
        """
        visualizes the rating
        of the selected neighbourhood 
        """
        st.subheader("Guest Ratings for AirBnB Accomodations")
        st.write("Important to note: Our rating data does not consider " + 
                 "things like how recent a review is and if the reviewer bought the review." +
                 "It also does not analyse reviews to verify trustworthiness.")
        st.write("Guests gave accommodations a rating of 1 (worst rating) " + 
                 "to 5 (best rating). In this plot you can see how many accommodations " +
                 "got ratings 1, 2, 3, 4, 5.")       

    def visualize_mean_rating(self):
        """
        visualizes the average rating
        of the selected neighbourhood
        """
        mean = self.rating_summary.average_rating()
        st.markdown('#### Average rating')
        st.write("The average rating is: ", mean)
        st.write("See how guests rated accomodations " + 
                 "compared to the average rating.")

    def visualize_numbers_of_listings(self):
        """
        visualizes the number many listings in the selected neighbourhood exist
        """
        total_number_of_listings = self.price_summary.get_total_number_of_listings()
        st.write("Total number of listings in the selected neighbourhood: ")
        st.write(total_number_of_listings)
