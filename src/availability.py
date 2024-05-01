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
        """Cleans the price and service fees columns.
        NaN values in price are dropped, in service fee are assumed to be 0.
        The price and service fee columns are converted from Strings to integers.
        Has to be called before the first method which calculates min or max prices is called."""
        self.df.dropna(subset=['availability 365'], inplace=True)
        self.df.loc[self.df["availability 365"] > 365, "availability 365"] = 365
        self.df.loc[self.df["availability 365"] < 0, "availability 365"] = 0
        return self.df

    def room_availability_in_exact_days(self, days: int) -> pd.DataFrame:
        listings = self.df[self.df['availability 365'] == days]
        quotient = self.df.shape[0] / listings.shape[0]
        return round(100 / quotient)

    def room_availability_more_than(self, days: int) -> pd.DataFrame:
        listings = self.df[self.df['availability 365'] >= days]
        quotient = self.df.shape[0] / listings.shape[0]
        return round(100 / quotient)

    def room_availability_less_than(self, days: int):
        listings = self.df[self.df['availability 365'] <= days]
        quotient = self.df.shape[0] / listings.shape[0]
        return round(100 / quotient)

    def room_type_with_max_availability(self):
        listings_grouped_by_type = self.df.groupby("room type")["availability 365"].sum()
        idx = listings_grouped_by_type.idxmax()
        return idx, int(listings_grouped_by_type[idx])

    def room_type_with_min_availability(self):
        listings_grouped_by_type = self.df.groupby("room type")["availability 365"].sum()
        idx = listings_grouped_by_type.idxmin()
        return idx, int(listings_grouped_by_type[idx])

    def mean_availability_per_room_type(self):
        listings = self.df.groupby("room type")["availability 365"].mean()
        return listings

    def percentage_no_availability_per_type(self):
        listings = self.df[self.df["availability 365"] == 0]
        listings_grouped_by_type = listings.groupby("room type")["availability 365"].count()
        total_count = self.df.groupby("room type")["availability 365"].count()
        quotients = total_count / listings_grouped_by_type
        df = pd.DataFrame(quotients)
        df = df.rename(columns={"availability 365": "Percentage (%)"})
        result = 100 / df
        return result

    def percentage_availability_per_type(self, days: int):
        listings = self.df[self.df["availability 365"] >= days]
        listings_grouped_by_type = listings.groupby("room type")["availability 365"].count()
        total_count = self.df.groupby("room type")["availability 365"].count()
        quotient = total_count / listings_grouped_by_type
        result = 100 / quotient
        return result

    def mean_room_availability_with_price_less_than(self, price: float):
        mean = self.df.loc[self.df["price"] <= price, "price"].mean()
        return mean

    def room_availability_with_price_between_and_more_than(self, lower_bound: float, upper_bound: float, days: int):
        listings = self.df[["price", "availability 365"]]
        prices = listings["price"].str.replace(",", "").str[1:].astype(float)
        listings["price"] = prices
        listings = listings[(listings["price"] <= upper_bound) & (listings["price"] >= lower_bound)]
        listings_with_availability = listings[listings["availability 365"] >= days]
        quotient = listings.shape[0] / listings_with_availability.shape[0]
        return round(100 / quotient)

    def availability_per_neighbour_group_more_than(self, days: int):
        self.df.loc[self.df["neighbourhood group"] == "manhatan", "neighbourhood group"] = "Manhattan"
        self.df.loc[self.df["neighbourhood group"] == "brookln", "neighbourhood group"] = "Brooklyn"
        listings = self.df.groupby("neighbourhood group")["availability 365"].count()
        listings_with_availability = self.df[self.df["availability 365"] >= days]
        listings_availability_grouped_by_neighbourhood_group = \
            listings_with_availability.groupby("neighbourhood group")[
                "availability 365"].count()
        quotients = listings / listings_availability_grouped_by_neighbourhood_group
        df = pd.DataFrame(quotients)
        df = df.rename(columns={"availability 365": "Percentage (%)"})
        return round(100 / df)
