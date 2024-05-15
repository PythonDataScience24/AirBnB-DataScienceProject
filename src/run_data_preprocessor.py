"""
This script is used to preprocess the data and save it to a new csv file.
This should be run every time the data in Airbnb_Open_Data.csv is updated.
"""
from data_preprocessor import DataPreprocessor

if __name__ == '__main__':
    data_preprocessor = DataPreprocessor('../data/Airbnb_Open_Data.csv')
    data_preprocessor.preprocess()
    data_preprocessor.write_csv("..data/Airbnb_Open_processed_Data.csv")
