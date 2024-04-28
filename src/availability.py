import pandas as pd

data = pd.read_csv("../data/Airbnb_Open_Data.csv")
data.loc[data["availability 365"] > 365, "availability 365"] = 365
data.loc[data["availability 365"] < 0, "availability 365"] = 0


def room_availability_in_exact_days(days: int, data: pd.DataFrame) -> pd.DataFrame:
    listings = data[data['availability 365'] == days]
    quotient = data.shape[0] / listings.shape[0]
    return round(100 / quotient)


def room_availability_less_than(days: int):
    listings = data[data['availability 365'] <= days]
    quotient = data.shape[0] / listings.shape[0]
    return round(100 / quotient)


def room_type_max_availability_per_type() -> pd.DataFrame:
    listings = data.groupby("room type")["availability 365"].max()
    return listings


def room_type_min_availability_per_type() -> pd.DataFrame:
    listings = data.groupby("room type")["availability 365"].min()
    return listings


def room_type_avg_availability_per_type():
    listings = data.groupby("room type")["availability 365"].mean()
    return listings


def percentage_no_availability_per_type():
    listings = data[data["availability 365"] == 0]
    listings_grouped_by_type = listings.groupby("room type")["availability 365"].count()
    total_count = data.groupby("room type")["availability 365"].count()
    quotient = total_count / listings_grouped_by_type
    result = 100 / quotient
    return result


def percentage_availability_per_type(days: int):
    listings = data[data["availability 365"] >= days]
    listings_grouped_by_type = listings.groupby("room type")["availability 365"].count()
    total_count = data.groupby("room type")["availability 365"].count()
    quotient = total_count / listings_grouped_by_type
    result = 100 / quotient
    return result


def room_availability_with_price_less_than(price: float):
    mean = data.loc[data["price"] <= price, "price"].mean()
    return mean


def no_room_availability_with_price_less_than(price: float):
    listings = data[["price", "availability 365"]]
    prices = listings["price"].str.replace(",", ".").str[1:].astype(float)
    listings["price"] = prices
    listings = listings[listings["price"] <= price]
    listings_no_availability = listings[listings["availability 365"] == 0]
    quotient = listings.shape[0] / listings_no_availability.shape[0]
    return 100 / quotient
