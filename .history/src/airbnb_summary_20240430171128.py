import pandas as pd 



# clean dataFrame 
def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    data.drop_duplicates(subset=['id'])
    data.dropna(subset= ['id'])
    return data
        

# get amount of unique AirBnBs in NYC 
def get_total_AirBnB(data: pd.DataFrame) -> pd.DataFrame:
    return data.shape[0]
    
# get amount of AirBnBs in each neighbourhood group 
def get_AirBnB_by_nhood(data: pd.DataFrame):
    grouped = data.groupby("neighbourhood group")
    str = ""
    for name, g in grouped:
        str += "You'll find" + str(grouped.size()) + "AirBnBs in the neighbourhood" + g.groups.keys() + "\n"
    return str
    
    
