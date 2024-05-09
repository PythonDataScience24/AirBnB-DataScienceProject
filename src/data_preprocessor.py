import pandas as pd
import numpy as np

class DataPreprocessor:
    def __init__(self, csv_path: str = None, df: pd.DataFrame = None):
        assert csv_path is not None or df is not None, "Either csv_path or df must be provided"
        if df is not None:
            self.df = df
        else:
            self.df = pd.read_csv(csv_path)


    def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
        """
        Overwrites the existing column names with snake_case names
        df:
        """
        #rename NAME to name
        self.df.rename(columns={'NAME' : 'name',
                                'host id' : 'host_id',
                                'host name' : 'host_name',
                                'neighbourhood group' : 'neighbourhood_group',
                                'country code' : 'country_code',
                                'room type' : 'room_type',
                                'Construction year' : 'construction_year',
                                'service fee' : 'service_fee',
                                'minimum nights' : 'minimum_nights',
                                'number of reviews' : 'number_of_reviews',
                                'last review' : 'last_review',
                                'reviews per month' : 'reviews_per_month',
                                'review rate number' : 'review_rate_number',
                                'calculated host listings count' : 'calculated_host_listings_count',
                                'availablity 365' : 'availability_365',
                                }, inplace=True)
        return df

    def clean_invalid_values(self, pd.DataFrame) -> pd.DataFrame:
        """
        Cleans invalid values from a DataFrame
        df:
        """
        # clean invalid data from availability column
        self.df.loc[self.df["availability 365"] > 365, "availability 365"] = 365
        self.df.loc[self.df["availability 365"] < 0, "availability 365"] = 0

        # clean invalid data from abc column


        # clean invalid data from xzy column


    return df


    def clean_missing_values(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        Cleans missing values from a DataFrame
        df:
        """
        self.df.dropna(subset=['availability 365'], inplace=True)
