"""
The Availability plotter is responsible for plotting
information about the room availability
"""
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from matplotlib import gridspec

from availability import AvailabilitySummary


class AvailabilityPlotter:

    def __init__(self, availability_summary: AvailabilitySummary):
        self.availability_summary = availability_summary

    def plot_room_availability(self, room_type_selected):
        st.subheader("Availability")
        pie = self.plot_pie_charts()
        pie.tight_layout()
        st.pyplot(pie)
        self.plot_scatter_and_hist()
        if not room_type_selected:
            self.bar_plot_mean_availability_by_room_type()
            special_chart = self.pie_chart_room_availability_covered_by_room_type()
            st.pyplot(special_chart)

    def plot_scatter_and_hist(self):
        """
        plots the scatter and histograms
        in the home page
        """
        fig = plt.figure()
        gs = fig.add_gridspec(3, 1)
        ax1 = fig.add_subplot(gs[0, :])
        ax2 = fig.add_subplot(gs[1, :])
        ax3 = fig.add_subplot(gs[2, :])
        self.scatter_rating_and_room_availability(ax3)
        self.hist_room_availability(ax1)
        self.scatter_chart_price_and_room_availability(ax2)
        fig.tight_layout()
        st.pyplot(fig)

    def plot_pie_charts(self):
        """
        plots the piecharts
        """
        fig = plt.figure(figsize=(10, 6))
        gs = gridspec.GridSpec(2, 2, figure=fig, wspace=0.5, hspace=0.5)
        ax1 = fig.add_subplot(gs[0, 0])
        ax2 = fig.add_subplot(gs[0, 1])
        self.pie_chart_room_availability(180, ax1)
        self.pie_chart_room_availability(90, ax2)
        ax1 = fig.add_subplot(gs[1, 0])
        ax2 = fig.add_subplot(gs[1, 1])
        self.pie_chart_one_year_room_availability(ax1)
        self.pie_chart_no_room_availability(ax2)
        return fig

    def bar_plot_mean_availability_by_room_type(self):
        """
            creates a bar plot visualizing the mean
            availability for each room type
            will be rendered only if room type is not selected

        """
        df: pd.DataFrame = self.availability_summary.mean_availability_per_room_type()
        fig, ax = plt.subplots(figsize=(5, 5))
        plt.title("Mean Availability by room type")
        room_types = df.index.values
        means = df.values
        rects = ax.bar(room_types, means, width=0.5, align='center')
        ax.bar_label(container=rects, padding=3)
        st.pyplot(fig)

    def pie_chart_no_room_availability(self, ax: plt.Axes):
        """
                creates a pie chart visualizing the percentage of
                Airbnb's which have no more room availability
        """
        data = []
        rooms_df = self.availability_summary.room_availability_in_exact_days(0)
        percentage = round(100 * rooms_df.shape[0] / self.availability_summary.get_df().shape[0], 3)
        percentage_over_zero = 100 - percentage
        data.append(percentage_over_zero)
        data.append(percentage)
        labels = ["still available", "no availability any more"]
        ax.set_title("No room availability")
        ax.pie(data, labels=labels, autopct='%1.1f%%')
        ax.legend(labels, loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))
        pass

    def pie_chart_room_availability(self, days: int, ax: plt.Axes):
        """
        creates a pie chart visualizing the percentage of
        Airbnb's with availability more than days in future
        Keyword arguments:
            days -- number of days of availability
        """
        data = []
        ax.set_title("Rooms with more than \n "
                     + str(days) + " days of availability in future")
        percentage_over_days = self.availability_summary.room_availability_more_than(days)
        percentage_under_days = 100 - percentage_over_days
        data.append(percentage_over_days)
        data.append(percentage_under_days)
        labels = ["more than " + str(days) + " days", "less than " + str(days) + " days"]
        ax.pie(data, autopct='%1.1f%%')
        ax.legend(labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    def pie_chart_one_year_room_availability(self, ax: plt.Axes):
        """
                creates a pie chart visualizing the percentage of
                Airbnb's which still have 365 days
                of availability anymore
        """
        data = []
        rooms_df = self.availability_summary.room_availability_in_exact_days(365)
        percentage = round(100 * rooms_df.shape[0] / self.availability_summary.get_df().shape[0], 3)
        percentage_under_365 = 100 - percentage
        data.append(percentage)
        data.append(percentage_under_365)
        labels = [" 365 days of availability", "less than 365 days of availability"]
        ax.set_title("Rooms with 365 days of availability")
        ax.pie(data, labels=labels, autopct='%1.1f%%')
        ax.legend(labels, loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))

    def pie_chart_room_availability_covered_by_room_type(self):
        """
        creates a pie chart visualizing
        the percentage of total availability covered
        by each room type
        I.e. 100% availability is 1000 days, then room
        type Home/Apartment covers for example 35% of the total availability.
        Notice: This plot will be rendered only if room type is not selected
        """
        fig = plt.figure()
        total_availability = self.availability_summary.total_room_availability()
        rooms = self.availability_summary.df.groupby("room_type")["availability_365"].sum()
        data = 100 * rooms / total_availability
        labels = rooms.index
        plt.title("Coverage of total availability by each room type")
        plt.pie(data.values, labels=labels, autopct='%1.1f%%', )
        plt.legend(labels, loc="lower left", title="room availability covering percentage by each room type",
                   bbox_to_anchor=(1, 0, 0.5, 1))
        return fig

    def scatter_chart_price_and_room_availability(self, ax: plt.Axes):
        """
        creates a scatter plot visualizing relation
        between price and room availability
        """
        ax.set_title("Price vs Room Availability")
        ax.set(xlabel='price in $', ylabel='availability \n in days')
        ax.scatter(self.availability_summary.df['price'], self.availability_summary.df['availability_365'])
        pass

    def hist_room_availability(self, ax: plt.Axes):
        """creates a plot visualizing the distribution of
        the room availability"""
        ax.set(ylabel='number of accommodations', xlabel='availabilits in days', title='Room Availability distribution')
        ax.hist(self.availability_summary.df["availability_365"])

    def scatter_rating_and_room_availability(self, ax: plt.Axes):
        """
                creates a scatter plot visualizing relation
                between rating and room
                availability
        """
        ax.set_title("Room Availability vs rating")
        ax.set(xlabel='rating', ylabel='availability \n in days')
        ax.scatter(self.availability_summary.df['review_rate_number'], self.availability_summary.df['availability_365'])
        pass


