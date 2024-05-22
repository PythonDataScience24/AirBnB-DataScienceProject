"""
This script is used to preprocess the data and save it to a new csv file.
This should be run every time the data in Airbnb_Open_Data.csv is updated.
"""
import os

from data_preprocessor import DataPreprocessor


def get_abs_project_path() -> str:
    """Gets the absolute path of the project directory. Works only if this script is in the src
    directory.
    :return: The absolute path of the project directory"""
    abs_script_path = os.path.abspath(__file__)
    src_path = os.path.dirname(abs_script_path)
    return os.path.dirname(src_path)


if __name__ == '__main__':
    project_path = get_abs_project_path()
    source_file = os.path.join(project_path, 'data/Airbnb_Open_Data.csv')
    data_preprocessor = DataPreprocessor(source_file)
    data_preprocessor.preprocess()
    processed_file = os.path.join(project_path, 'data/Airbnb_Open_processed_Data.csv')
    data_preprocessor.write_csv(processed_file)
