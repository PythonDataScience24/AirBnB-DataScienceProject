import pandas as pd
import streamlit as st
import neighbourhood_selector
import neighbourhood_visualizer
from airbnb_summary import AirBnBSummary

# To start the program please make sure you have streamlit installed
# Then in your command line enter the following command:
# streamlit run src/home.py
# See also README.md

st.title('Home')
selector = neighbourhood_selector.NeighbourhoodSelector(
    'data/Airbnb_Open_Data.csv')
neighbourhood: str = st.selectbox('Neighbourhood', selector.get_neighbourhoods())
room_type: str = st.selectbox('Room Type', selector.get_room_types())
selector.set_selection(neighbourhood, room_type)

if selector.selection_df is not None:
    df: pd.DataFrame = selector.selection_df
    visualizer: neighbourhood_visualizer.NeighbourhoodVisualizer = neighbourhood_visualizer.NeighbourhoodVisualizer(df)
    visualizer.visualize_numbers_of_listings()
    visualizer.visualize_filtered_dataframe()
    st.subheader("See below multiple information about the neighbourhood " + neighbourhood + " and room type "
                 + room_type)
    visualizer.visualize_max_price()
    visualizer.visualize_min_price()
    st.subheader("Mean Price of the neighbourhood " + str(neighbourhood) + " and room type " + str(room_type))
    visualizer.visualize_mean_price()
else:
    st.write("No data available for this selection.")

