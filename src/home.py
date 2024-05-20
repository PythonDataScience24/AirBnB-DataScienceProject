"""
home page of the application
the home.py file is the entry point of the programm
"""
import pandas as pd
import streamlit as st
from neighbourhood_selector import NeighbourhoodSelector
from neighbourhood_visualizer import NeighbourhoodVisualizer

# To start the program please make sure you have streamlit installed
# Then in your command line enter the following command:
# streamlit run src/home.py
# See also README.md


st.title('Home')
selector = NeighbourhoodSelector(
    'data/Airbnb_Open_processed_Data.csv')
st.subheader('Please select a neighbourhood and a room type to display room information')
neighbourhood: str = st.selectbox('Neighbourhood*', selector.get_neighbourhoods(), index=None)
room_type: str = st.selectbox('Room Type*', selector.get_room_types(), index=None)

prices = [60, 100, 200, 300, 500, 750, 1000, 1500, 2000]
price: float = st.selectbox('Price', prices,
                            placeholder="Only rooms which have a price equals or less than "
                                        "the selected price will be displayed", index=None)
selector.set_selection(neighbourhood, room_type, price)

if selector.selection_df is not None:
    df: pd.DataFrame = selector.selection_df
    visualizer: NeighbourhoodVisualizer = NeighbourhoodVisualizer(df)
    visualizer.visualize_numbers_of_listings()
    visualizer.visualize_filtered_dataframe()
    st.subheader("See below multiple information about the neighbourhood " + neighbourhood +
                 " and room type " + room_type)
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
