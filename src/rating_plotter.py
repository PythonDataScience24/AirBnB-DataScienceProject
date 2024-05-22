import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from rating import RatingSummary
   
class RatingPlotter:
    def __init__(self, rating_summary: RatingSummary):
        self.rating_summary: RatingSummary = rating_summary


        

    def plot_rating(self):
        bins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
        plot = plt.hist(self.rating_summary.df['review rate number'], bins = bins, 
                rwidth = 0.5)
        plt.xticks([1, 2, 3, 4, 5]) 
        plt.title('Rating Distribution of')
        plt.xlabel('Rating')
        plt.ylabel('Number of AirBnBs')
        st.pyplot(plot)