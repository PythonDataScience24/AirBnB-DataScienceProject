import pandas as pd
import streamlit as st

import neigbourhood_selector
import neighbourhood_visualizer

# To start the program please make sure you have streamlit installed
# Then in your command line enter the following command:
# streamlit run src/home.py
# See also README.md

st.title('Home')
selector: neigbourhood_selector.NeighbourhoodSelector = neigbourhood_selector.NeighbourhoodSelector(
    'data/Airbnb_Open_Data.csv')
neighbourhood: str = st.selectbox('Neighbourhood', selector.get_neighbourhoods())
room_type: str = st.selectbox('Room Type', selector.get_room_types())
selector.set_selection(neighbourhood, room_type)

if selector.selection_df is not None:
    df: pd.DataFrame = selector.selection_df
    visualizer: neighbourhood_visualizer.NeighbourhoodVisualizer = neighbourhood_visualizer.NeighbourhoodVisualizer(df)

else:
    st.write("No data available for this selection.")

