import pandas as pd 

class RatingSummary:
    
    def __init__(self, csv_path: str = None, df: pd.DataFrame = None):
        assert csv_path is not None or df is not None, "Either csv_path or df must be provided"
        if df is not None:
            self.df = df
        else:
            self.df = pd.read_csv(csv_path)
            self.clean_data()


    def clean_data(self)-> pd.DataFrame:
        self.df.dropna(subset = ['review rate number'], inplace = True)
        self.df.loc[self.df["neighbourhood group"] == "manhatan", "neighbourhood group"] = "Manhattan"
        self.df.loc[self.df["neighbourhood group"] == "brookln", "neighbourhood group"] = "Brooklyn"
        return self.df 

    def get_average_rating_per_nhood(self)->pd.DataFrame:
        grouped = self.df.groupby('neighbourhood group')
        average_ratings = grouped['review rate number'].mean()
        return average_ratings         

    def get_min_rating_per_nhood(self) -> pd.DataFrame:
        grouped = self.df.groupby('neighbourhood group')
        min_rating = grouped['review rate number'].min()
        return min_rating

    def get_max_rating_per_nhood(self) -> pd.DataFrame:
        grouped = self.df.groupby('neighbourhood group')
        max_rating = grouped['review rate number'].max()
        return max_rating
