""" Gives short overview about existing AirBnBs in NYC
    might be extended in next iteration
"""
import pandas as pd

class AirBnBSummary:

    def __init__(self, csv_path: str = None, df: pd.DataFrame = None):
        """ Initializes the class with data from a CSV file or an existing DataFrame 
        Data is either read from the specified CSV file and cleaned, 
        or DataFrame is provided
        Args:
            csv_path (str, optional): Path to the CSV file to be read and cleaned. Defaults to None
            df (pd.DataFrame, optional): Existing DataFrame to be used directly. Defaults to None
        Raises:
            AssertionError: If neither csv_path nor df is provided.
        """
        assert csv_path is not None or df is not None, "Either csv_path or df must be provided"
        if df is not None:
            self.df = df
        else:
            self.df = pd.read_csv(csv_path)
            self.clean_data()

    def clean_data(self) -> pd.DataFrame:
        """ Drops duplicated id's and NAN values
        Returns:
            pd.DataFrame: cleaned dataframe
        """
        self.df.drop_duplicates(subset=['id'], inplace=True)
        self.df.dropna(subset=['id'], inplace=True)
        return self.df

    def get_total_airbnbs(self) -> int:
        """
        Returns:
            int: total num of AirBnBs
        """
        return self.df.shape[0]

    def get_airbnbs_per_nhood(self) -> pd.DataFrame:
        """ gets total num of AirBnBs in each neighbourhood group
        Returns:
            pd.DataFrame: grouped by neighbourhood group
        """
        airbnbs_per_group = self.df.groupby('neighbourhood_group').size()
        return airbnbs_per_group
