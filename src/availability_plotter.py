import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class AvailabilityPlotter:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def bar_plot_mean_availability_by_room_type(self):
        """
            creates a bar plot visualizing the mean
            availability for each room type
        """
        pass

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
        with availability less than the average availability
        and more than the average availability'
        """
        pass
