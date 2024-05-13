# Message 1: 
 src/main.py:99:0: R1711: Useless return at end of function or method (useless-return)
#### previous code: 
```bash
 def display_mean_availability_per_room_type():
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_Data.csv')
    st.subheader("Mean availability per room type")
    data = availability_summary.mean_availability_per_room_type()
    st.table(data=data)
    return
```
### adapted code

```bash 
def display_availability_percentage_per_neighbour_group():
    availability_summary = availability.AvailabilitySummary('data/Airbnb_Open_Data.csv')
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
