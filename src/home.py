"""
home page of the application
the home.py file is the entry point of the programm
"""
import traceback
import pandas as pd
import streamlit as st

from neighbourhood_selector import NeighbourhoodSelector
from neighbourhood_visualizer import NeighbourhoodVisualizer


# To start the program please make sure you have streamlit installed
# Then in your command line enter the following command:
# streamlit run src/home.py
# See also README.md

class Home:
    """
    This class is the entry point of the application.
    It provides the user with a homepage where they can select a neighbourhood,
    a room type and a price to display information about the selected neighbourhood and room type
    and price.
    """

    def __init__(self):
        """Declares the attributes of the class and initializes them with None."""
        self.neighbourhood_group: str | None = None
        self.neighbourhood: str | None = None
        self.room_type: str | None = None
        self.price: float | None = None

    def show_homepage(self):
        """Shows the homepage of the application."""
        st.title('Home')

        df_path: str = 'data/Airbnb_Open_processeed_Data.csv'
        selector: NeighbourhoodSelector | None = self.try_init_neighbourhood_selector(df_path)
        if selector is None:
            return

        st.subheader(
            'Please select a neighbourhood and a room type to display room information')
        self.show_select_boxes(selector)
        if selector.selection_df is not None:
            df: pd.DataFrame = selector.selection_df
            visualizer: NeighbourhoodVisualizer = NeighbourhoodVisualizer(df)
            visualizer.visualize_numbers_of_listings()
            visualizer.visualize_filtered_dataframe()
            if df.size != selector.full_df.size:
                st.subheader(self.build_subheader())
                visualizer.visualize_mean_rating()
                visualizer.visualize_percentage_rating_over_average()
                visualizer.visualize_percentage_rating_under_average()
                visualizer.visualize_min_max_price_summary()
                visualizer.visualize_mean_median_price_summary()
                visualizer.visualize_neighbourhood_availability()
                visualizer.visualize_mean_availability()
                visualizer.visualize_rooms_with_one_year_availability()
        else:
            st.write("No data available for this selection.")

    def show_select_boxes(self, selector: NeighbourhoodSelector):
        """
        Shows the select boxes for the neighbourhood, room type and price.
        The select_box for the neighbourhood only shown when a neighbourhood group is selected
        and has only the neighbourhoods of the selected neighbourhood group.
        :param selector: The NeighbourhoodSelector
        """
        self.neighbourhood_group = st.selectbox('Neighbourhood Group',
                                                selector.get_neighbourhood_groups(),
                                                index=None)
        self.neighbourhood = None
        if self.neighbourhood_group is not None:
            self.neighbourhood = st.selectbox('Neighbourhood',
                                              selector.get_neighbourhoods(
                                                  self.neighbourhood_group),
                                              index=None)
        self.room_type = st.selectbox('Room Type', selector.get_room_types(), index=None)
        prices = [60, 100, 200, 300, 500, 750, 1000, 1500, 2000]
        self.price = st.selectbox('Price', prices,
                                  placeholder="Only rooms which have a price equals or less "
                                              "than the selected price will be displayed",
                                  index=None)
        selector.set_selection(neighbourhood_group=self.neighbourhood_group,
                               neighbourhood=self.neighbourhood,
                               room_type=self.room_type, price=self.price)

    def build_subheader(self) -> str:
        """
        Create the subheader for the visualizations based on the selected neighbourhood
        and room type
        :return: The subheader
        :rtype: str
        """
        title = "See below multiple information about"
        if self.neighbourhood is not None:
            title += " the neighbourhood " + self.neighbourhood
        if self.neighbourhood is not None and self.room_type is not None:
            title += " and"
        if self.room_type is not None:
            title += " the room type " + self.room_type
        if self.neighbourhood is None and self.room_type is None:
            title += " all neighbourhoods and room types"
        return title

    @staticmethod
    def try_init_neighbourhood_selector(df_path: str) -> NeighbourhoodSelector | None:
        """
        Try to initialize a NeighbourhoodSelector with the given path to the data.
        if an error occurs loading the data from the path, a user-friendly error message is
        displayed in the Streamlit app.
        :param df_path: The path to the data
        :type df_path: str
        :return: The NeighbourhoodSelector or None if an error occurred
        :rtype: NeighbourhoodSelector | None
        """
        try:
            selector = NeighbourhoodSelector(csv_path=df_path)
        except FileNotFoundError:
            st.error(f"""
            Error: Table with the AirBnB data could not be found.

            File ```{df_path}``` containing the AirBnB data not found.
            
            Next Steps:
            Make sure ```data_preprocessor.py``` has been executed before running this script and
            the resulting file ```{df_path}``` has not been moved or deleted.
            
            To run ```data_preprocessor.py```, execute the following command in the command line:

            ```python src/data_preprocessor.py```

            For more information see README.md -> 'How to get started'

            If this does not solve the problem, please contact the developers
            or create an issue in the GitHub repository of this project.
            More information can be found in the README.md file.
            """)
            return None
        except ValueError:
            st.error(f"""
            Error: Table with the AirBnB data could not be read correctly.

            Unable to read file ```{df_path}``` containing the AirBnB.
            
            Next Steps:
            Execute ```data_preprocessor.py``` again and make sure the file ```{df_path}```
            is not corrupted or manually altered. If you wish to edit the data,
            do so in the original file ```data/Airbnb_Open_Data.csv``` and
            then run ```data_preprocessor.py``` again.
            
            To run ```data_preprocessor.py```, execute the following command in the command line:

            ```python src/data_preprocessor.py```

            For more information see README.md -> 'How to get started'

            If this does not solve the problem, please contact the developers
            or create an issue in the GitHub repository of this project.
            More information can be found in the README.md file.
            """)
            return None
        except MemoryError:
            st.error(f"""
            Error: Table with the AirBnB data can not be loaded because of memory issues.

            Not enough free memory on the device to load the file ```{df_path}``` containing
            the AirBnB data.
            
            Next Steps:
            Try to free up memory on the device by closing other applications or processes.
            If this doesn't solve the problem, try to run the application on a device with
            more memory or try use a smaller dataset by editing the file 
            ```data/Airbnb_Open_Data.csv```.
            Make sure to  save a copy of the original file before editing it.
            
            To run ```data_preprocessor.py```, execute the following command in the command line:

            ```python src/data_preprocessor.py```

            For more information see README.md -> 'How to get started'

            If this does not solve the problem, please contact the developers
            or create an issue in the GitHub repository of this project.
            More information can be found in the README.md file.
            """)
            return None
        except Exception:  # pylint: disable=broad-except
            # intentionally catching all exceptions, to show more user-friendly error message to
            # the user inside the Streamlit app
            stacktrace = f"""```{traceback.format_exc()}```"""
            st.error(f"An unexpected error occurred:\n\n{stacktrace}\n\n"
                     f"Please contact the developers or create an issue in the GitHub repository "
                     f"of this project. More information can be found in the README.md file."
                     )
            return None
        return selector


if __name__ == '__main__':
    home = Home()
    home.show_homepage()
