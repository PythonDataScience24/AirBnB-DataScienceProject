"""
    The class AvailabilitySummary has the task to calculate every kind of information
    about the availability of the Airbnb Accommodations
"""

import pandas as pd


class AvailabilitySummary:

    def __init__(self, csv_path: str = None, df: pd.DataFrame = None):
        assert csv_path is not None or df is not None, "Either csv_path or df must be provided"
        if df is not None:
            self.df = df
        else:
            self.df = pd.read_csv(csv_path)
            self.clean_data()

    def clean_data(self) -> pd.DataFrame:
        """removes the rows where column availability is null"""
        self.df.dropna(subset=['availability_365'], inplace=True)
        return self.df

    def room_availability_in_exact_days(self, days: int):
        """
        returns the rooms which still have exact days
        of availability in future
        Keyword arguments:
            days -- number of days of availability
        """
        listings = self.df.loc[self.df['availability_365'] == days, "name"]
        return listings

    def room_availability_more_than(self, days: int):
        """
        returns the rooms which still have more or equals
            days of availability in future
            Keyword arguments:
            days -- number of days of availability
        """
        listings = self.df[self.df['availability_365'] >= days]
        if listings.shape[0] == 0:
            return 0
        quotient = self.df.shape[0] / listings.shape[0]
        return round(100 / quotient)

    def room_availability_less_than(self, days: int):
        """
        filters the rooms which have less or equals
        days of availability in future
        Keyword arguments:
        days -- number of days of availability
        """
        listings = self.df[self.df['availability_365'] <= days]
        if listings.shape[0] == 0:
            return 0
        quotient = self.df.shape[0] / listings.shape[0]
        return round(100 / quotient)

    def room_type_with_max_availability(self):
        """
        groups the dataframe by room types
        and sums the days of availability,
        finally returns the room type with the
        maximum amount of days in availability
        """
        listings_grouped_by_type = self.df.groupby("room_type")["availability_365"].sum()
        idx = listings_grouped_by_type.idxmax()
        return idx, int(listings_grouped_by_type[idx])

    def room_type_with_min_availability(self):
        """
            groups the dataframe by room types
            and sums the days of availability,
            finally returns the room type with the
            minimum amount of days in availability
        """
        listings_grouped_by_type = self.df.groupby("room_type")["availability_365"].sum()
        idx = listings_grouped_by_type.idxmin()
        return idx, int(listings_grouped_by_type[idx])

    def mean_availability(self):
        """
            float: calculates the mean availability
        """
        mean = self.df["availability_365"].mean()
        return mean

    def mean_availability_per_room_type(self)-> pd.DataFrame:
        """
        Returns:
            float: calculates the mean availability per room type
        """
        listings = self.df.groupby("room_type")["availability_365"].mean()
        return listings

    def percentage_no_availability_per_type(self):
        """
            Returns:
                float: percentage of AirBnB's per room type with no availability anymore
        """
        listings = self.df[self.df["availability_365"] == 0]
        listings_grouped_by_type = listings.groupby("room_type")["availability_365"].count()
        total_count = self.df.groupby("room_type")["availability_365"].count()
        quotients = total_count / listings_grouped_by_type
        df = pd.DataFrame(quotients)
        df = df.rename(columns={"availability_365": "Percentage (%)"})
        result = 100 / df
        return result

    def percentage_availability_per_type(self, days: int):
        """
            Returns:
                    float: calculates for every room type
                    the percentage of AirBnB's which have more than
                    availability than the specified days
            Keyword arguments:
                    days -- the number of days of availability
        """
        listings = self.df[self.df["availability_365"] >= days]
        listings_grouped_by_type = listings.groupby("room_type")["availability_365"].count()
        total_count = self.df.groupby("room_type")["availability_365"].count()
        quotient = total_count / listings_grouped_by_type
        result = 100 / quotient
        return result

    def mean_room_availability_with_price_equals_than(self, price: float):
        """
            Returns:
                    float: mean price for all accommodations with a smaller price than a certain price
            Keyword arguments:
                    price -- the upper bound of the price
        """
        mean = self.df.loc[self.df["price"] == price, "price"].mean()
        return mean

    def room_availability_when_price_is_between(self, lower_bound: float, upper_bound: float, days: int):
        """
        Returns:
                float: percentage of rooms which have prices between lower_bound and upper_bound and more
                or equals days of availability in future
        Keyword arguments:
                price -- the upper bound of the price
                lower_bound -- the lower bound of the price
                upper_bound -- the upper bound of the price
        """
        listings = self.df[["price", "availability_365"]]
        listings = listings[(listings["price"] <= upper_bound) & (listings["price"] >= lower_bound)]
        print(listings.shape, upper_bound, lower_bound)
        listings_with_availability = listings[listings["availability_365"] >= days]
        quotient = listings.shape[0] / listings_with_availability.shape[0]
        return round(100 / quotient)

    def availability_per_neighbour_group_more_than(self, days: int):
        """
            Returns:
                    float: percentage of rooms which have prices between lower_bound and upper_bound and more
                    or equals days of availability in future for every room type
            Keyword arguments:
                    days -- the number of days of availability
        """
        listings = self.df.groupby("neighbourhood_group")["availability_365"].count()
        listings_with_availability = self.df[self.df["availability 365"] >= days]
        listings_availability_grouped_by_neighbourhood_group = \
            listings_with_availability.groupby("neighbourhood_group")[
                "availability_365"].count()
        quotients = listings / listings_availability_grouped_by_neighbourhood_group
        df = pd.DataFrame(quotients)
        df = df.rename(columns={"availability 365": "Percentage (%)"})
        return round(100 / df)

    def total_room_availability(self):
        return self.df["availability_365"].sum()

    def get_df(self):
        """
        returns the whole dataframe
        """
        return self.df
