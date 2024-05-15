"""
    Calculates and summarize rating statistics for Airbnb listings.

    This class provides methods to calculate the average rating, minimum and maximum ratings,
    percentages of listings that are above or below the average, minimum, and maximum ratings.
    It allows initialization with a CSV file from which data is loaded and cleaned,
    or directly with given pandas DataFrame.
"""
import pandas as pd


class RatingSummary:

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
        """ Drops NAN values for review rate number 
        Returns:
            pd.DataFrame: cleaned dataframe
        """
        self.df.dropna(subset=['review_rate_number'], inplace=True)
        return self.df

    def average_rating(self):
        """
        Returns:
            float: average rating
        """
        return round(self.df['review_rate_number'].mean(), 3)

    def percentage_rating_over_average(self):
        """ 
        Returns:
            float: percentage of AirBnB with better rating then average
        """
        over_average = self.df[self.df['review_rate_number'] > self.average_rating()].shape[0]
        return self.calculate_percentage(over_average)

    def percentage_rating_under_average(self):
        """ 
        Returns:
            float: percentage of AirBnB with worse rating then average
        """
        under_average = self.df[self.df['review_rate_number'] < self.average_rating()].shape[0]
        return self.calculate_percentage(under_average)

    def min_rating(self):
        """ 
        Returns:
            int: min rating of all AirBnBs
        """
        return self.df['review_rate_number'].min()

    def max_rating(self):
        """ 
        Returns:
            int: max rating of all AirBnBs
        """
        return self.df['review_rate_number'].max()

    def percentage_over_min_rating(self):
        """ 
        Returns:
            float: percentage of AirBnB with higher rating then min rating
        """
        over_min = self.df[self.df['review_rate_number'] > self.min_rating()].shape[0]
        return self.calculate_percentage(over_min)

    def percentage_under_max_rating(self):
        """ 
        Returns:
            float: percentage of AirBnB with worse rating then max rating
        """
        under_max = self.df[self.df['review_rate_number'] < self.max_rating()].shape[0]
        return self.calculate_percentage(under_max)

    def calculate_percentage(self, value):
        """ Calculate the percentage of a specific subset of Airbnb listings
        relative to the total number of listings.
        Args:
            value (int): The count of Airbnb listings meeting a specific condition.
        Returns:
            float: percentage of listings that meet the condition, 
            rounded to three decimal places.
        """
        total = self.df.shape[0]
        return round(100 * value / total, 3)
