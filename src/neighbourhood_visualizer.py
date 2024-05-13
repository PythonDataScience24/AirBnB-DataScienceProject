import pandas as pd
from availability import AvailabilitySummary
from price import PriceSummary
import streamlit as st
from airbnb_summary import AirBnBSummary
from rating import RatingSummary

"""
The neighbourhood visualizer visualizes 
information about selected the neighbourhood and room type
"""


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
        """ Returns a visualization of the filtered dataframe """
        st.dataframe(self.df)

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
        st.write(str(result) + " % of all rooms in this neighbourhood with the "
                               "selected room type still have more than 180 days " +
                 " availability in future and " + str(result1) + "% of all rooms in this neighbourhood with the "
                                                                 "selected room type have less than 90 days "
                                                                 "availability in future")

    def visualize_max_price(self):
        """
        visualizes the max price per
        night for the selected neighbourhood
        """
        (name, max_price, service_fee) = self.price_summary.get_max_price_per_night()
        st.subheader("Max Price per Night")
        st.write("The accommodation " + str(name) + " has the max price " + str(max_price) + "dollar per night and a "
                                                                                             "service fee of " + str(
            service_fee)
                 + " dollars")

    def visualize_min_price(self):
        """
        visualizes the min price per
        night for the selected neighbourhood
        """
        (name, min_price, service_fee) = self.price_summary.get_min_price_per_night()
        st.subheader("Min Price per Night")
        st.write("The accommodation " + str(name) + " has the min price " + str(min_price) + "dollar per night and "
                                                                                             "service fee: " + str(
            service_fee) + " dollars per")

    def visualize_mean_price(self):
        """
        visualizes the mean price
        of the selected neighbourhood
        """
        mean_price = self.price_summary.get_mean_price_per_night()
        st.write("mean price per night: " + str(round(mean_price)))

    def visualize_availability_when_price_is_between(self, lower_bound: float, upper_bound: float, days):
        """
        visualizes information about how much percentage of listings
        in the selected neighbourhood with price (per night) between
        lower and upper bound still have days of availability in future
        Keyword arguments:
            lower_bound -- lower bound of the price
            upper_bound -- upper bound of the price
            days -- days of availability
        """
        result = self.availability_summary.room_availability_when_price_id_between(lower_bound, upper_bound, days)
        print(result)
        st.write(result + "%")

    def visualize_mean_availability_when_price_is_between(self, lower_bound: float, upper_bound: float):
        """
               visualizes mean availability of all listings
               in the selected neighbourhood with price (per night) between
               lower and upper bound
               Keyword arguments:
                   lower_bound -- lower bound of the price
                   upper_bound -- upper bound of the price
               """

        pass

    def visualize_mean_rating(self):
        """
        visualizes the mean rating
        of the selected neighbourhood
        """
        mean = self.rating_summary.get_average_rating_per_nhood()
        st.subheader("See below the average rating of this neighbourhood")
        st.write(mean)

    def visualize_median_cost(self):
        """
        visualizes the median costs (price per night) of all
        rooms in the selected neighbourhood
        """
        st.subheader("Median price per night")
        median = self.price_summary.get_median_price_for_one_night()
        st.write("The median price per night is: " + str(median))

    def visualize_numbers_of_listings(self):
        """
        visualizes the number many listings in the selected neighbourhood exist
        """
        total_number_of_listings = self.price_summary.get_total_number_of_listings()
        st.write(f"Total number of listings in the selected neighbourhood:", total_number_of_listings)
