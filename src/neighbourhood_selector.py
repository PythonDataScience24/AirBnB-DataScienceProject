"""
Implements from task #15 select neighbourhood and room type to get summary data:
user can choose neighbourhood and room type
"""

import numpy as np
import pandas as pd


def get_group(group_by: pd.api.typing.DataFrameGroupBy, group_key, df: pd.DataFrame) \
        -> pd.DataFrame | None:
    """
    Returns the group from a DataFrameGroupBy object, if the group exists, else None.

    Helper function to get the group from a GroupBy object, since DataFrameGroupBy.get_group() is
    deprecated and cannot handle if the group does not exist.

    :param group_by: The DataFrameGroupBy object
    :type group_by: pd.api.typing.DataFrameGroupBy
    :param group_key: The key of the group to get
    :param df: The original DataFrame on which the group_by object was created
    :type df: pd.DataFrame
    :return: The group, if it exists, else None
    :rtype: pd.DataFrame | None
    """
    indexes = group_by.indices.get(group_key)
    group_df: pd.DataFrame | None = None
    if indexes is not None:
        group_df = df.iloc[indexes]
    return group_df


class NeighbourhoodSelector:
    """
    Provides the ability to select a neighbourhood and room type from a dataset and get the rows of
    the dataframe fitting to the selection.
    """
    def __init__(self, csv_path: str = None, df: pd.DataFrame = None):
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

    def set_selection(self, neighbourhood: str, room_type: str, price: float) -> pd.DataFrame | None:
        """
        Set the selection_df to the selection of the neighbourhood and room type, if it exists,
        else None.
        :param neighbourhood: The neighbourhood to select
        :type neighbourhood: str
        :param room_type: The room type to select
        :type room_type: str
        :return: The selection, if it exists, else None
        :rtype: pd.DataFrame | None
        """
        group_by: pd.api.typing.DataFrameGroupBy = self.full_df.groupby(
            ['neighbourhood', 'room_type'])
        self.selection_df = get_group(group_by=group_by, group_key=(neighbourhood, room_type),
                                      df=self.full_df)
        if price is not None:
            self.selection_df = self.selection_df[self.selection_df['price'] <= price]
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
