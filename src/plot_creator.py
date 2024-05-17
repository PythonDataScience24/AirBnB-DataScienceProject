"""
The plot visualizer is responsible for
creating and providing visualizations of
different kinds of plots.
The plot visualizer uses to create the plots matplotlib and seaborn
The plot visualizer provides functions for creating different diagram types
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class PlotCreator:

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def histogram(self):
        pass

    def histogram_room_type_distribution(self):
        fig, ax = plt.subplots(figsize=(10, 5))
        plt.ylim(top=5500, bottom=0)
        plt.title("Room type distribution for the selected neighbourhood")
        plt.yticks(np.arange(0, 5500, 250))
        room_typed_accumulated = self.df.groupby("room type")["room type"].count()
        room_types = room_typed_accumulated.index.values
        counts = room_typed_accumulated.values
        ax.bar(room_types, counts, align="center", color="green")
        for i in range(len(room_types)):
            ax.text(i, counts[i] / 10, counts[i], ha="center", va="center")


