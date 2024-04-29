import pandas as pd


# 2. Min - Max Value of listings price per night
# extract the min and max price per night (is it per night?).
# How many NaN values (if any) do we have? What do we do with those?
# what do we do w/service fee? display MIN / night (show separate service fee).
# Show MIN price for 1 night service fee included (but just display MIN night and in (service_fee))
# same for max
# what about min-nights?

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the price and service fees columns.
    NaN values in price are dropped, in service fee are assumed to be 0.
    The price and service fee columns are converted from Strings to integers."""
    df.dropna(subset=['price'], inplace=True)
    df['price'] = df['price'].str.replace('$', '').str.replace(',', '').astype(int)
    df['service fee'] = df['service fee'].fillna('0')
    df['service fee'] = df['service fee'].str.replace('$', '').str.replace(',', '').astype(int)
    return df


class PriceSummary:
    def __init__(self, csv_path: str = None, df: pd.DataFrame = None):
        assert csv_path is not None or df is not None, "Either csv_path or df must be provided"
        if df is not None:
            self.df = df
        else:
            self.df = pd.read_csv(csv_path)
            self.df = clean_data(self.df)

    def get_min_price_per_night(self):
        min_price = self.df['price'].min()
        min_prices = self.df[self.df['price'] == min_price]
        min_price_index = min_prices['service fee'].idxmin()
        return self.get_price_and_service_fees_of_row(min_price_index)

    def get_max_price_per_night(self):
        max_price = self.df['price'].max()
        max_prices = self.df[self.df['price'] == max_price]
        max_price_index = max_prices['service fee'].idxmax()
        return self.get_price_and_service_fees_of_row(max_price_index)

    def get_price_and_service_fees_of_row(self, row_index):
        price = self.df.at[row_index, 'price']
        service_fee = self.df.at[row_index, 'service fee']
        return price, service_fee

    def get_min_costs_for_one_night(self):
        if 'costs' not in self.df.columns:
            self.df['costs'] = self.df['price'] + self.df['service fee']
        min_costs_index = self.df['costs'].idxmin()
        return self.get_price_and_service_fees_of_row(min_costs_index)

    def get_max_costs_for_one_night(self):
        if 'costs' not in self.df.columns:
            self.df['costs'] = self.df['price'] + self.df['service fee']
        max_costs_index = self.df['costs'].idxmax()
        return self.get_price_and_service_fees_of_row(max_costs_index)


if __name__ == '__main__':
    price_summary = PriceSummary('../data/Airbnb_Open_Data.csv')
    print(price_summary.get_min_price_per_night())
    print(price_summary.get_max_price_per_night())
    print(price_summary.get_min_costs_for_one_night())
    print(price_summary.get_max_costs_for_one_night())
