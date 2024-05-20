"""
Implements from task #15 select neighbourhood and room type to get summary data:
user can choose neighbourhood and room type
"""

import numpy as np
import pandas as pd


class NeighbourhoodSelector:
    """
    Provides the ability to select a neighbourhood and room type from a dataset and get the rows of
    the dataframe fitting to the selection.
    """

    def __init__(self, csv_path: str | None = None, df: pd.DataFrame = None):
        """
        :keyword csv_path: Path to the CSV file containing the data
        :type csv_path: str | None
        :keyword df: DataFrame containing the data
        :type df: pd.DataFrame | None
        :raises AssertionError: If neither csv_path nor df is provided
        """
        assert csv_path is not None or df is not None, "Either csv_path or df must be provided"
        if df is not None:
            self.full_df: pd.DataFrame = df
        else:
            self.full_df: pd.DataFrame = pd.read_csv(csv_path)
        self.selection_df: pd.DataFrame | None = None

    def set_selection(self, neighbourhood_group: str | None = None,
                      neighbourhood: str | None = None, room_type: str | None = None,
                      price: float | None = None) -> pd.DataFrame | None:
        """
        Set the selection_df to the selection of the neighbourhood_group, neighbourhood
        and room type, and upper bound on price.
        If the selection does not match any rows, selection_df is set to None.
        :param neighbourhood_group: The neighbourhood group to select
        :param neighbourhood: The neighbourhood to select
        :param room_type: The room type to select
        :param price: The maximum price to select
        :return: selection_df, the DataFrame containing the selected rows,
        or None if no rows match the selection
        :rtype: pd.DataFrame | None
        """
        selection_df: pd.DataFrame = self.full_df
        if neighbourhood_group is not None:
            neighbourhood_group_mask = selection_df['neighbourhood_group'] == neighbourhood_group
            selection_df = selection_df[neighbourhood_group_mask]
        if neighbourhood is not None:
            neighbourhood_mask = selection_df['neighbourhood'] == neighbourhood
            selection_df = selection_df[neighbourhood_mask]
        if room_type is not None:
            room_type_mask = selection_df['room_type'] == room_type
            selection_df = selection_df[room_type_mask]
        if price is not None:
            selection_df = selection_df[selection_df['price'] <= price]
        if selection_df.empty:
            selection_df = None
        self.selection_df = selection_df
        return self.selection_df

    def get_neighbourhoods(self) -> np.ndarray:
        """
        :return: List of all neighbourhood names in the dataset.
        :rtype: np.ndarray
        """
        return self.full_df['neighbourhood'].unique()

    def get_neighbourhood_groups(self) -> np.ndarray:
        """
        :return: List of all neighbourhood group names in the dataset.
        :rtype: np.ndarray
        """
        return self.full_df['neighbourhood_group'].unique()

    def get_room_types(self) -> np.ndarray:
        """
        Returns a list of all room types in the dataset.
        :return: List of all room type names  in the dataset.
        :rtype: np.ndarray
        """
        return self.full_df['room_type'].unique()
