import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


class NeighbourhoodSummaryPlotter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_neighbourhood_room_type_summary(self, room_type_selected: bool):
        if not room_type_selected:
            fig1 = self.bar_chart_room_type_()
            fig2 = self.pie_chart_room_type()
            st.pyplot(fig1)
            st.pyplot(fig2)

    def bar_chart_room_type_(self):
        """
        creates a plt visualizing
        the total numbers of accommodations
        by each room type
        will only be rendered if room type is not selected
        """
        fig, ax = plt.subplots(figsize=(5, 5))
        plt.title("Total numbers of accommodations of each room type")
        room_typed_count = self.df.groupby("room_type")["room_type"].count()
        room_types = room_typed_count.index.values
        counts = room_typed_count.values
        rects = ax.bar(room_types, counts)
        ax.bar_label(container=rects, padding=3)
        return fig

    def pie_chart_room_type(self):
        """
        creates a plot visualizing the percentage
        of each room type occurring in selected the neighbourhood
        Notice: This plot will only be rendered if the room type is not selected
        """
        fig, ax = plt.subplots(figsize=(5,5))
        room_types_count = self.df.groupby("room_type")["room_type"].count()
        data = room_types_count * 100 / self.df.shape[0]
        labels = room_types_count.index.values
        ax.set_title("Occurrence of each room type")
        ax.pie(data, autopct='%1.1f%%', labels=labels)
        ax.legend(labels, loc='lower left', bbox_to_anchor=(1, 0, 0.5, 1))
        return fig
