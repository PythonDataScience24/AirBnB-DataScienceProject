import pandas as pd
from availability import AvailabilitySummary
from price import PriceSummary
import streamlit as st
from airbnb_summary import AirBnBSummary
from rating import RatingSummary


class NeighbourhoodVisualizer:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.availabilitySummary = self.get_availability_summary_of_selection()
        self.priceSummary = self.get_price_summary_of_selection()
        self.airbnbSummary = self.get_overall_summary_of_selection()
        self.ratingSummary = self.get_rating_summary_of_selection()

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

    def visualize_neighbourhood_availability(self, days: int):
        """
        visualizes how many percentage of the listings
            in the selected neighbourhood have still
            more than days of availability in future
        Keyword arguments:
            days -- days of availability
        """
        pass

    def visualize_max_price(self):
        """
        visualizes the max price per
        night for the selected neighbourhood
        """
        (name, max_price, service_fee) = self.priceSummary.get_max_price_per_night()
        st.subheader("Max Price per Night")
        st.write("The accommodation " + str(name) + " has the max price " + str(max_price) + " dollar per night")

    def visualize_min_price(self):
        """
        visualizes the min price per
        night for the selected neighbourhood
        """
        (name, min_price, service_fee) = self.priceSummary.get_min_price_per_night()
        st.subheader("Min Price per Night")
        st.write("The accommodation " + str(name) + " has the min price " + str(min_price) + " dollar per night")

    def visualize_mean_price(self):
        """
        visualizes the mean price
        of the selected neighbourhood
        """
        mean_price = self.priceSummary.get_mean_price_per_night()
        st.write("mean price per night: " + str(round(mean_price)))

    def visualize_max_costs(self):
        """
        visualizes the max costs, that means
        the max costs per night plus the service fee
        """
        pass

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
        pass

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
        pass

    def visualize_median_cost(self):
        """
        visualizes the median costs of all
        rooms in the selected neighbourhood
        """
        pass

    def visualize_numbers_of_listings(self):
        """
        visualizes the number many listings in the selected neighbourhood exist
        """
        total_number_of_listings = self.airbnbSummary.get_total_airbnbs()
        st.write(f"Total number of listings in the selected neighbourhood:", total_number_of_listings)
