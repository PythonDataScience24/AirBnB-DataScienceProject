import pandas as pd
from src.availability import AvailabilitySummary


class NeighbourhoodVisualizer:

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.availabilitySummary = self.get_availability_summary_of_selection()

    def get_availability_summary_of_selection(self) -> AvailabilitySummary:
        """ Returns a AvailabilitySummary of the selected neighbourhood and room type."""
        availability_summary: AvailabilitySummary = AvailabilitySummary(
            df=self.df.copy())
        availability_summary.clean_data()
        return availability_summary

    def visualize_neighbourhood_availability(self, days: int):
        """
        visualizes how many percentage of the listings
            in the selected neighbourhood have still
            more than days of availability in future
        Keyword arguments:
            days -- days of availability
        """
        pass

    def visualize_price_data(self):
        pass

    def visualize_max_price(self):
        pass

    def visualize_min_price(self):
        pass

    def visualize_mean_price(self):
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

    def visualize_mean_rating(self):
        pass
