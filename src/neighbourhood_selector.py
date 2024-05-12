import pandas as pd
import numpy as np
import price
import availability
import rating
import airbnb_summary


def get_group(group_by: pd.api.typing.DataFrameGroupBy, group_key, df: pd.DataFrame) \
        -> pd.DataFrame | None:
    """
    Returns the group from a DataFrameGroupBy object, if the group exists, else None.

    group_by: The DataFrameGroupBy object
    group_key: The key of the group to get
    df: The original DataFrame on which the group_by object was created

    Helper function to get the group from a GroupBy object, since DataFrameGroupBy.get_group() is deprecated and
    cannot handle if the group does not exist.
    """
    indexes = group_by.indices.get(group_key)
    group_df: pd.DataFrame | None = None
    if indexes is not None:
        group_df = df.iloc[indexes]
    return group_df


class NeighbourhoodSelector:
    def __init__(self, csv_path: str = None, df: pd.DataFrame = None):
        assert csv_path is not None or df is not None, "Either csv_path or df must be provided"
        if df is not None:
            self.full_df: pd.DataFrame = df
        else:
            self.full_df: pd.DataFrame = pd.read_csv(csv_path)
        self.selection_df: pd.DataFrame | None = None

    def set_selection(self, neighbourhood: str, room_type: str) -> pd.DataFrame | None:
        """ Set the selection_df to the selection of the neighbourhood and room type, if it exists, else None.
        Returns the selection_df."""
        # TODO: change column names after data cleaning
        group_by: pd.api.typing.DataFrameGroupBy = self.full_df.groupby(['neighbourhood', 'room type'])
        self.selection_df = get_group(group_by=group_by, group_key=(neighbourhood, room_type), df=self.full_df)
        return self.selection_df

    def get_neighbourhoods(self) -> np.ndarray:
        """ Returns a list of all neighbourhoods in the dataset."""
        return self.full_df['neighbourhood'].unique()

    def get_neighbourhood_groups(self) -> np.ndarray:
        """ Returns a list of all neighbourhood groups in the dataset."""
        return self.full_df['neighbourhood group'].unique()

    def get_room_types(self) -> list:
        """ Returns a list of all room types in the dataset."""
        return self.full_df['room type'].unique().tolist()


