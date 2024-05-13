import pandas as pd


# 2. Min - Max Value of listings price per night
# extract the min and max price per night (is it per night?).
# How many NaN values (if any) do we have? What do we do with those?
# what do we do w/service fee? display MIN / night (show separate service fee).
# Show MIN price for 1 night service fee included (but just display MIN night and in (service_fee))
# same for max
# what about min-nights?


class PriceSummary:
    def __init__(self, csv_path: str = None, df: pd.DataFrame = None):
        assert csv_path is not None or df is not None, "Either csv_path or df must be provided"
        if df is not None:
            self.df = df
        else:
            self.df = pd.read_csv(csv_path)

    def clean_data(self) -> pd.DataFrame:
        """Cleans the price and service fees columns.
        NaN values in price are dropped, in service fee are assumed to be 0.
        The price and service fee columns are converted from Strings to integers.
        Has to be called before the first method which calculates min or max prices is called."""
        self.df.dropna(subset=['price'], inplace=True)
        return self.df

    def get_number_of_nan_prices(self) -> int:
        """Returns the number of NaN values in the price column.
        Has to be called before clean_data() to get the correct number of NaN values."""
        return self.df['price'].isna().sum()

    def get_number_of_nan_service_fees(self) -> int:
        """Returns the number of NaN values in the service fee column.
        Has to be called before clean_data() to get the correct number of NaN values."""
        return self.df['service_fee'].isna().sum()

    def get_total_number_of_listings(self) -> int:
        return self.df.shape[0]

    def get_min_price_per_night(self) -> tuple[str, int, int]:
        min_price = self.df['price'].min()
        min_prices = self.df[self.df['price'] == min_price]
        min_price_index = min_prices['service_fee'].idxmin()
        return self._get_price_and_service_fees_of_row(min_price_index)

    def get_max_price_per_night(self) -> tuple[str, int, int]:
        max_price = self.df['price'].max()
        max_prices = self.df.loc[self.df['price'] == max_price, ['name', 'price', 'service_fee']]
        max_price_index = max_prices['service_fee'].idxmax()
        return self._get_price_and_service_fees_of_row(max_price_index)

    def _get_price_and_service_fees_of_row(self, row_index) -> tuple[str, int, int]:
        price = self.df.at[row_index, 'price']
        service_fee = self.df.at[row_index, 'service_fee']
        name = self.df.at[row_index, 'name']
        return name, price, service_fee

    def get_min_costs_for_one_night(self) -> tuple[str, int, int]:
        if 'costs' not in self.df.columns:
            self.df['costs'] = self.df['price'] + self.df['service_fee']
        min_costs_index = self.df['costs'].idxmin()
        return self._get_price_and_service_fees_of_row(min_costs_index)

    def get_max_costs_for_one_night(self) -> tuple[str, int, int]:
        if 'costs' not in self.df.columns:
            self.df['costs'] = self.df['price'] + self.df['service_fee']
        max_costs_index = self.df['costs'].idxmax()
        return self._get_price_and_service_fees_of_row(max_costs_index)

    def get_median_price_for_one_night(self) -> int:
        return self.df['price'].median()

    def get_mean_price_per_night(self) -> float:
        return self.df['price'].mean()

    def _get_name(self, idx):
        return self.df.at[idx, 'name']

    def get_summary_table(self):
        min_price_per_night = self.get_min_price_per_night()
        max_price_per_night = self.get_max_price_per_night()
        min_costs_for_one_night = self.get_min_costs_for_one_night()
        max_costs_for_one_night = self.get_max_costs_for_one_night()
        table = pd.DataFrame({
            "name": ["Min price per night", "Max price per night", "Min costs for one night",
                     "Max costs for one night"],
            "Amount": [f"${min_price_per_night[1]}", f"${max_price_per_night[2]}",
                       f"${min_costs_for_one_night[1] + min_costs_for_one_night[2]}",
                       f"${max_costs_for_one_night[1] + max_costs_for_one_night[2]}"],
            "Additional Information": [f"additional ${min_price_per_night[1]} of service fee",
                                       f"additional ${max_price_per_night[1]} of service fee",
                                       f"${min_costs_for_one_night[1]} price per night + ${min_costs_for_one_night[2]} service fee",
                                       f"${max_costs_for_one_night[1]} price per night + ${max_costs_for_one_night[2]} service fee"]})
        table.style.hide(axis="index")
        table.set_index("name", inplace=True)
        return table