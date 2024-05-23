"""
home page of the application
the home.py file is the entry point of the programm
"""
import traceback

import pandas as pd
import streamlit as st

from neighbourhood_selector import NeighbourhoodSelector
from neighbourhood_visualizer import NeighbourhoodVisualizer
from price_plotter import PricePlotter
from availability_plotter import AvailabilityPlotter
from neighbourhhod_summary_plotter import NeighbourhoodSummaryPlotter
from rating_plotter import RatingPlotter


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

        df_path: str = 'data/Airbnb_Open_processed_Data.csv'
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
                NeighbourhoodSummaryPlotter(visualizer.df).plot_neighbourhood_room_type_summary(
                    room_type_selected=self.room_type is not None)
                visualizer.visualize_rating()
                RatingPlotter(visualizer.rating_summary).plot_hist_rating()
                visualizer.visualize_mean_rating()
                RatingPlotter(visualizer.rating_summary).plot_pie_average()
                PricePlotter(visualizer.price_summary).plot_price_and_service_fee()
                visualizer.visualize_min_max_price_summary()
                visualizer.visualize_mean_median_price_summary()
                visualizer.visualize_neighbourhood_availability()
                visualizer.visualize_mean_availability()
                visualizer.visualize_rooms_with_one_year_availability()
                AvailabilityPlotter(visualizer.availability_summary).plot_room_availability(
                    room_type_selected=self.room_type is not None)
        else:
            st.write("")
            st.write("There are currently no listings available for your selection. Please adjust "
                     "your selection.")

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
                                  placeholder="Only rooms priced at or below the selected amount "
                                              "will be shown.",
                                  index=None)
        selector.set_selection(neighbourhood_group=self.neighbourhood_group,
                               neighbourhood=self.neighbourhood,
                               room_type=self.room_type,
                               price=self.price)

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
            Error: Airbnb data table not found.

            File `{df_path}` missing.
            
            Steps to resolve:
            1. Run ```python src/data_preprocessor.py```
            2. Verify `{df_path}` exists and is not moved or deleted.
            
            See
            [README.md](https://github.com/PythonDataScience24/AirBnB-DataScienceProject/blob/main/README.md#how-can-you-get-involved) 
            for more details.
            
            If the issue persists, contact the developers or report on GitHub.
            """)
            return None
        except ValueError:
            st.error(f"""
            Error: Unable to read the Airbnb data table.

            File `{df_path}` could not be read.
            
            Steps to resolve:
            1. Run ```python src/data_preprocessor.py```
            2. Verify `{df_path}` exists and is not moved or deleted.
            
            See
            [README.md](https://github.com/PythonDataScience24/AirBnB-DataScienceProject/blob/main/README.md#how-can-you-get-involved) 
            for more details.
            
            If the issue persists, contact the developers or report on GitHub.
            """)
            return None
        except MemoryError:
            st.error(f"""
            Error: Unable to load AirBnB data due to memory issues.

            Not enough free memory to load "{df_path}".
            
            Steps to resolve:
            1. Free up memory by closing other applications.
            2. Use a device with more memory.
            3. Try a smaller dataset by editing "data/Airbnb_Open_Data.csv" (save a copy first).
            
            To run "data_preprocessor.py", use:
            python src/data_preprocessor.py
            
            See
            [README.md](https://github.com/PythonDataScience24/AirBnB-DataScienceProject/blob/main/README.md#how-can-you-get-involved) 
            for more details.
            
            If the issue persists, contact the developers or report on GitHub.
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
