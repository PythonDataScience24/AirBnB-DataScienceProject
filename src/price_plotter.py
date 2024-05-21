"""handles the plotting of price and service fee data."""

import matplotlib.pyplot as plt
import streamlit as st

from price import PriceSummary


class PricePlotter:
    """ Class for plotting price and service fee data, given a PriceSummary object."""

    def __init__(self, price_summary: PriceSummary):
        self.price_summary: PriceSummary = price_summary

    def plot_price_and_service_fee(self):
        """
        Creates a scatter plot visualizing the relationship between price and service fee
        and two histograms visualizing the distribution of prices and service fees.
        Displays the plots in streamlit.
        """
        st.subheader("Price and Service Fee")
        fig = plt.figure()
        gs = fig.add_gridspec(2, 2)
        ax1 = fig.add_subplot(gs[0, :])
        ax2 = fig.add_subplot(gs[1, 0])
        ax3 = fig.add_subplot(gs[1, 1])
        self.subplot_price_and_service_fee(ax1)
        self.subplot_price_distribution(ax2)
        self.subplot_service_fee_distribution(ax3)
        fig.tight_layout()
        st.pyplot(fig)

    def subplot_price_and_service_fee(self, ax: plt.Axes):
        """
        Creates a scatter plot visualizing the relationship between price and service fee.
        :return: The sublot containing the plot
        :rtype: plt.Axes
        """
        ax.scatter(self.price_summary.df['price'], self.price_summary.df['service_fee'], alpha=0.5,
                   s=10)
        ax.grid(True)
        ax.set_xlabel('Price in $')
        ax.set_ylabel('Service Fee in $')
        ax.set_title('Price and Service Fee')
        return ax

    def subplot_price_distribution(self, ax: plt.Axes):
        """
        Creates a histogram visualizing the distribution of prices.
        :return: The subplot containing the plot
        :rtype: plt.Axes
        """
        ax.hist(self.price_summary.df['price'], bins=50)
        ax.title.set_text('Price distribution')
        ax.set_xlabel('Price in $')
        ax.set_ylabel('Number of accommodations')
        return ax

    def subplot_service_fee_distribution(self, ax: plt.Axes):
        """
        Creates a histogram visualizing the distribution of service fees.
        :return: The subplot containing the plot
        :rtype: plt.Axes
        """
        ax.hist(self.price_summary.df['service_fee'], bins=50)
        ax.title.set_text('Service fee distribution')
        ax.set_xlabel('Service fee in $')
        ax.set_ylabel('Number of accommodations')
        return ax
