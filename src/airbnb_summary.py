import pandas as pd 

class AirBnBSummary: 
    
    def __init__(self, csv_path: str = None, df: pd.DataFrame = None):
        assert csv_path is not None or df is not None, "Either csv_path or df must be provided"
        if df is not None:
            self.df = df
        else:
            self.df = pd.read_csv(csv_path)
            self.clean_data()
    
    def clean_data(self)-> pd.DataFrame: 
        self.df.drop_duplicates(subset=['id'], inplace=True)
        self.df.dropna(subset = ['id'], inplace= True)
        self.df.loc[self.df["neighbourhood group"] == "manhatan", "neighbourhood group"] = "Manhattan"
        self.df.loc[self.df["neighbourhood group"] == "brookln", "neighbourhood group"] = "Brooklyn"
        return self.df
    
    def get_total_airbnbs(self) -> int:
        return self.df.shape[0]
    
    def get_airbnbs_per_nhood(self) -> pd.DataFrame:
        airbnbs_per_group = self.df.groupby('neighbourhood group').size()
        return airbnbs_per_group