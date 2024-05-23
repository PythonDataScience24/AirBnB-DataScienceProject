"""
The rating plotter is responsible for plotting
information about Airbnb ratings
"""
import matplotlib.pyplot as plt
import streamlit as st
from rating import RatingSummary


class RatingPlotter:
    
    def __init__(self, rating_summary: RatingSummary):
        self.rating_summary: RatingSummary = rating_summary


            
    def plot_hist_rating(self):
        """
        Creates a histogram plot visualizing the distribution of 
        AirBnB rating
        """
        fig,ax = plt.subplots()
        bins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
        ax.hist(self.rating_summary.df['review_rate_number'], bins=bins,
                        rwidth=0.5)
        plt.xticks([1, 2, 3, 4, 5])
        plt.title('Rating Distribution')
        plt.xlabel('Rating')
        plt.ylabel('Number of AirBnBs')
        st.pyplot(fig)
        
    def plot_pie_average(self): 
        """
        Creates a pie plot visualizing ratings above and under 
        the average rating
        """
        fig, ax = plt.subplots(figsize=(3,3))
        data = []
        over_avrg = self.rating_summary.percentage_rating_over_average()
        under_avrg = self.rating_summary.percentage_rating_under_average()
        data.append(over_avrg)
        data.append(under_avrg)
        labels = ["Rating over Average", 'Rating under Average']
        ax.set_title("Accomodations Rated Below or Above Average")
        ax.pie(data, labels= labels, autopct = '%1.1f%%')
        ax.legend(labels, loc="best", bbox_to_anchor=(1, 0, 0.5, 1))
        st.pyplot(fig)