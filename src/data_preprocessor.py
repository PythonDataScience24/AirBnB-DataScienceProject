import pandas as pd
import numpy as np


class DataPreprocessor:
    """Convert column names and their respective data types"""
    column_names = ['id',
                    'name',
                    'host_id',
                    'host_identity_verified',
                    'host_name',
                    'neighbourhood_group',
                    'neighbourhood',
                    'lat',
                    'long',
                    'country',
                    'country_code',
                    'instant_bookable',
                    'cancellation_policy',
                    'room_type',
                    'construction_year',
                    'price',
                    'service_fee',
                    'minimum_nights',
                    'number_of_reviews',
                    'last_review',
                    'reviews_per_month',
                    'review_rate_number',
                    'calculated_host_listings_count',
                    'availability_365',
                    'house_rules',
                    'license']

    data_types = {'id': np.int64,
                  'name': str,
                  'host_id': np.int64,
                  'host_identity_verified': str,
                  'host_name': str,
                  'neighbourhood_group': str,
                  'neighbourhood': str,
                  'lat': np.float64,
                  'long': np.float64,
                  'country': str,
                  'country_code': str,
                  'instant_bookable': str,
                  'cancellation_policy': str,
                  'room_type': str,
                  'construction_year': np.float64,
                  'price': object,
                  'service_fee': object,
                  'minimum_nights': np.float64,
                  'number_of_reviews': np.float64,
                  'last_review': object,
                  'reviews_per_month': np.float64,
                  'review_rate_number': np.float64,
                  'calculated_host_listings_count': np.float64,
                  'availability_365': np.float64,
                  'house rules': str,
                  'license': str}

    def __init__(self, csv_path: str = None):
        """Load CSV file with specified column names and data types"""
        self.df = pd.read_csv(csv_path, names=self.column_names, dtype=self.data_types, header=0)

    def drop_columns(self):
        """Delete columns that are not being used or have mostly null values"""
        # Drop the 'country' column since it's all United States
        self.df.drop(columns=['country'], inplace=True)
        # Drop the 'country_code' column since it's all US
        self.df.drop(columns=['country_code'], inplace=True)
        # Drop the 'license' column since there's only one license all other values are null
        self.df.drop(columns=['license'], inplace=True)

    def standardize_datatypes_columns(self):
        """Change string data types to float, int or to_datetime"""
        self.df["price"] = self.df["price"].str.replace(",", "").str[1:].astype(float)
        self.df["service_fee"] = self.df["service_fee"].astype(str).str.replace('$', "").astype(np.float64)
        self.df['service_fee'] = self.df['service_fee'].fillna(0.0)
        self.df['last_review'] = pd.to_datetime(self.df['last_review'])  # instead of NaN there's NaT value

    def clean_invalid_values(self):
        """Clean invalid values from a DataFrame"""
        # clean invalid data from 'availability' column
        self.df.loc[self.df["availability_365"] > 365, "availability_365"] = 365
        self.df.loc[self.df["availability_365"] < 0, "availability_365"] = 0
        self.df.loc[self.df["neighbourhood_group"] == "manhatan", "neighbourhood_group"] = "Manhattan"
        self.df.loc[self.df["neighbourhood_group"] == "brookln", "neighbourhood_group"] = "Brooklyn"

    def clean_missing_values(self):
        """Clean null values from the data set"""
        # clean NaN data from 'id' column
        self.df.dropna(subset=['id'], inplace=True)
        # clean NaN data from 'name' column since we consider a listing with no description as not valuable for our
        # target user group
        self.df.dropna(subset=['name'], inplace=True)

    def preprocess(self):
        """Apply all preprocessing steps"""
        self.standardize_datatypes_columns()
        self.clean_invalid_values()
        self.drop_columns()
        self.clean_missing_values()

    def write_csv(self, path: str):
        """Write out the data set as a CSV file
        :param path: path to the output file"""
        self.df.to_csv(path, index=False)

