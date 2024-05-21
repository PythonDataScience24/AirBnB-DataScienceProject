import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from src.availability import AvailabilitySummary


class AvailabilityPlotter:

    def __init__(self, df: pd.DataFrame, availability_summary: AvailabilitySummary):
        self.df = df
        self.availability_summary = availability_summary

    def bar_plot_mean_availability_by_room_type(self):
        """
            creates a bar plot visualizing the mean
            availability for each room type
        """
        df: pd.DataFrame = self.availability_summary.mean_availability_per_room_type()
        fig, ax = plt.subplots(figsize=(7, 10))
        plt.title("Mean Availability by room type")
        rects = ax.bar(df)
        ax.bar_label(container=rects, padding=3)

    def pie_chart_room_availability(self, days: int):
        """
        creates a pie chart visualizing the percentage of
        Airbnb's with availability more than days in future
        Keyword arguments:
            days -- number of days of availability
        """
        pass

    def pie_chart_room_availability_under_and_over_average(self):
        """
        creates a pie chart visualizing the percentages of Airbnb's
        with availability less than the average availability value
        and more than the average availability value
        """
        pass

    def pie_chart_room_availability_per_room_type(self):
        """
        creates a pie chart visualizing
        the percentage of availability covered
        by each room type
        Example 100% availability is 1000 days, then room
        type Home/Apartment covers for example 35%
        """
        pass

    def bar_chart_number_of_availability_per_room_type(self):
        """
        creates a bar chart visualizing the days of availability
        """
        pass

    def line_chart_mean_room_availability_and_price(self):
        """
        creates a line chart visualizing the mean course
        of availability by increasing price per night
        """
        fig, ax = plt.subplots(figsize=(7, 10))
        price_range = range(50, 1500, 50)
        mean_availabilities = []
        for price in price_range:
            mean = self.availability_summary.mean_room_availability_with_price_equals_than(price)
            mean_availabilities.append(mean)
        np_mean_array = np.array(mean_availabilities)
        ax.plot(price_range, np_mean_array, label="mean availability")
        ax.set_title("Mean availability by price")
        ax.set(ylabel="Availability", xlabel="Price per night")
        ax.grid()
        ax.legend(labels="mean availability")
        ax.set_xlim(0)
        ax.legend(title='mean availability')
        return fig, ax

