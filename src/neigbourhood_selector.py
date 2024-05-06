import pandas as pd
import numpy as np
import price
import availability
import rating
import airbnb_summary


def get_group(group_by: pd.api.typing.DataFrameGroupBy, group_key, df: pd.DataFrame) -> pd.DataFrame | None:
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

    def get_price_summary_of_selection(self) -> price.PriceSummary:
        """ Returns a PriceSummary of the selected neighbourhood and room type."""
        price_summary: price.PriceSummary = price.PriceSummary(df=self.selection_df.copy())
        price_summary.clean_data()
        return price_summary

    def get_availability_summary_of_selection(self) -> availability.AvailabilitySummary:
        """ Returns a AvailabilitySummary of the selected neighbourhood and room type."""
        availability_summary: availability.AvailabilitySummary = availability.AvailabilitySummary(
            df=self.selection_df.copy())
        availability_summary.clean_data()
        return availability_summary

    def get_rating_summary_of_selection(self) -> rating.RatingSummary:
        """ Returns a RatingSummary of the selected neighbourhood and room type."""
        rating_summary: rating.RatingSummary = rating.RatingSummary(df=self.selection_df.copy())
        rating_summary.clean_data()
        return rating_summary

    def get_overall_summary_of_selection(self) -> airbnb_summary.AirBnBSummary:
        """ Returns a AirBnBSummary of the selected neighbourhood and room type."""
        overall_summary: airbnb_summary.AirBnBSummary = airbnb_summary.AirBnBSummary(df=self.selection_df.copy())
        overall_summary.clean_data()
        return overall_summary


def print_summary(selector: NeighbourhoodSelector):
    overall_summary: airbnb_summary.AirBnBSummary = selector.get_overall_summary_of_selection()
    print(f'Total Airbnbs: {overall_summary.get_total_airbnbs()}')
    print()
    price_summary: price.PriceSummary = selector.get_price_summary_of_selection()
    print(f'Price range: {price_summary.get_min_price_per_night()} - {price_summary.get_max_price_per_night()}')
    print(f'Average price: {price_summary.get_average_price_per_night()}')
    print()
    availability_summary: availability.AvailabilitySummary = selector.get_availability_summary_of_selection()
    print(f'Availability more than 180 days: {availability_summary.room_availability_more_than(180)}%')
    print()
    rating_summary: rating.RatingSummary = selector.get_rating_summary_of_selection()
    print(f'Average rating: {rating_summary.get_average_rating_per_nhood()}')


if __name__ == '__main__':
    n = NeighbourhoodSelector('../data/Airbnb_Open_Data.csv')
    print(n.get_neighbourhoods())
    print(n.get_room_types())
    n.set_selection('Kensington', 'Shared room')
    if n.selection_df is not None:
        print_summary(n)
    else:
        print('Selection has no fitting accommodation, please try another combination.')
