import pandas as pd
import matplotlib.pyplot as plt


class NeighbourhoodSummaryPlotter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def bar_diagram_room_type_distribution(self):
        fig, ax = plt.subplots(figsize=(7, 10))
        plt.ylim(top=5500, bottom=0)
        plt.title("Room type distribution for the selected neighbourhood")
        plt.yticks(np.arange(0, 30000, 1500))
        room_typed_accumulated = self.df.groupby("room type")["room type"].count()
        room_types = room_typed_accumulated.index.values
        counts = room_typed_accumulated.values
        rects = ax.bar(room_types, counts)
        ax.bar_label(container=rects, padding=3)
