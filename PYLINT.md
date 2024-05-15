# Message 1: 
 src/main.py:99:0: R1711: Useless return at end of function or method (useless-return)
#### previous code: 
```bash
 def display_mean_availability_per_room_type():
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_processed_Data.csv.csv')
    st.subheader("Mean availability per room type")
    data = availability_summary.mean_availability_per_room_type()
    st.table(data=data)
    return
```
### adapted code

```bash 
def display_availability_percentage_per_neighbour_group():
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_processed_Data.csv')
    st.subheader("Percentage of Listings with Availability more than 180 days in future per neighbour group")
    data = availability_summary.availability_per_neighbour_group_more_than(180)
    st.table(data=data)
````
#### fixed issue 
removed return statement

# Message 2
src/neighbourhood_selector.py:9:0: C0301: Line too long (108/100) (line-too-long)
### previous code
```bash
def get_group(group_by: pd.api.typing.DataFrameGroupBy, group_key, df: pd.DataFrame) -> pd.DataFrame | None:
```
### adapted code
```bash
def get_group(group_by: pd.api.typing.DataFrameGroupBy, group_key, df: pd.DataFrame) \
        -> pd.DataFrame | None:
```
#### fixed issue
shortened line with method definition

# Message 3
src/neighbourhood_selector.py:3:0: W0611: Unused import price (unused-import)
#### Previous code: 
```bash
 import price #unused
```
#### fixed issue 
removed unused import statement

# Message 4
src/home.py:1:0: C0114: Missing module docstring (missing-module-docstring)
#### Previous code: 
```bash
from airbnb_summary import AirBnBSummary #unused
```
#### fixed issue 
removed unused import statement

# Message 5
src/price.py:83:8: W0107: Unnecessary pass statement (unnecessary-pass)
#### Previous code: 
```bash
    def _get_name(self, idx):
        return self.df.at[idx, 'NAME']
        pass
```
### adapted code
```bash
 def _get_name(self, idx):
        return self.df.at[idx, 'NAME']
```
#### fixed issue 
removed unnecessary pass statement

# Message 6
src/neighbourhood_visualizer.py:1:0: C0103: Module name "src/neighbourhood_visualizer" doesn't conform to snake_case naming style (invalid-name)
#### previous code
```bash
self.availabilitySummary = self.get_availability_summary_of_selection()
```
#### adapted code
```bash
self.availability_summary = self.get_availability_summary_of_selection()
```
#### fixed issue
changed name style self.availabilitySummary -> self.availability_summary (snake_case naming style)

# Message 7
src/neighbourhood_visualizer.py:4:0: C0411: third party import "streamlit" should be placed before first party imports "availability.AvailabilitySummary", "price.PriceSummary"  (wrong-import-order)

#### previous code
```bash
import pandas as pd
from availability import AvailabilitySummary
from price import PriceSummary
import streamlit as st
```
#### adapted code
```bash
import pandas as pd
import streamlit as st
from availability import AvailabilitySummary
from price import PriceSummary
```
#### fixed issue
placed third party import under first party imports

# Message 8
src/home.py:30:0: C0301: Line too long (119/100) (line-too-long)
### previous code
```bash
    st.subheader("Mean Price of the neighbourhood " + str(neighbourhood) + " and room type " + str(room_type))
```
### adapted code
```bash
 st.subheader("Mean Price of the neighbourhood " + str(neighbourhood)
                 + " and room type " + str(room_type))
```
### fixed issue
shortened code line


#### Message 9
src/home.py:1:0: C0114: Missing module docstring (missing-module-docstring)
### previous code
```bash
import pandas as pd
```
### adapted code
```bash
"""
home page of the application
the home.py file is the entry point of the programm
"""
import pandas as pd
```
### fixed issue added module doc string

# Message 10
src/neighbourhood_visualizer.py:131:17: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)

### previous code
```bash
    def visualize_numbers_of_listings(self):
        """
        visualizes the number many listings in the selected neighbourhood exist
        """
        total_number_of_listings = self.price_summary.get_total_number_of_listings()
        st.write(f"Total number of listings in the selected neighbourhood:", total_number_of_listings)
```
### adapted code
```bash
    def visualize_numbers_of_listings(self):
        """
        visualizes the number many listings in the selected neighbourhood exist
        """
        total_number_of_listings = self.price_summary.get_total_number_of_listings()
        st.write("Total number of listings in the selected neighbourhood: " + str(total_number_of_listings))
```
### fixed issue
removed f-string which had no interpolated variable

# Message 11
src/neighbourhood_visualizer.py:56:30: W0612: Unused variable 'service_fee' (unused-variable)
### previous code
```bash
    def visualize_min_max_price_summary(self):
        """
        Creates a table which visualizes the
        accommodations with the max and min price
        """
        (name_max, max_price, service_fee) = self.price_summary.get_max_price_per_night()
        (name_min, min_price, service_fee) = self.price_summary.get_min_price_per_night()
        st.subheader("Min and Max Price per Night")
        df = pd.DataFrame({'Price': [max_price, min_price], 'Accommodation': [name_max, name_min]},
                          index=["Max Price", "Min Price"])
        st.table(df)
```
### adapted code
```bash
    def visualize_min_max_price_summary(self):
        """
        Creates a table which visualizes the
        accommodations with the max and min price
        """
        (name_max, max_price, service_fee_max) = self.price_summary.get_max_price_per_night()
        (name_min, min_price, service_fee_min) = self.price_summary.get_min_price_per_night()
        st.subheader("Min and Max Price per Night")
        df = pd.DataFrame({'Price': [max_price, min_price], 'service_fee':[service_fee_max, service_fee_min] 'Accommodation': [name_max, name_min, service_fee]},
                          index=["Max Price", "Min Price"])
        st.table(df)
```
### fixed issue
displayed the variable service_fee in the dataframe
