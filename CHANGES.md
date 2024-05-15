# Structure and Code Improvements
## Abstraction
### Example 1 Create a data_preprocessor class

The class abstracts away the details of data preprocessing by providing methods like 
- 'drop_columns'
- 'standardize_datatypes_columns'
- 'clean_invalid_values'
- 'clean_missing_values'
- 'preprocess'

#### Example rating.py Class 
The task of cleaning the DataFrame has been moved to the data_preprocessor.py class. Consequently, data cleaning is performed at the same abstraction level as the class. The data cleaning in the rating.py class is now limited to class-specific cleanings.<br>
Before Abstraction:<br>
rating.py
```python
  def clean_data(self) -> pd.DataFrame:
      self.df.loc[self.df["neighbourhood_group"] == "manhatan", "neighbourhood_group"] = "Manhattan"
      self.df.loc[self.df["neighbourhood_group"] == "brookln", "neighbourhood_group"] = "Brooklyn"
      self.df.dropna(subset=['review_rate_number'], inplace=True)
      return self.df
```
After Abstraction: <br>
rating.py 
```python
  def clean_data(self) -> pd.DataFrame:
      """ Drops NAN values for review rate number 
      Returns:
      pd.DataFrame: cleaned dataframe
      """
      self.df.dropna(subset=['review_rate_number'], inplace=True)
      return self.df
```
data_preprocessor.py <br>
```python
  def clean_invalid_values(self):
      """Clean invalid values from a DataFrame"""
      self.df.loc[self.df["availability_365"] > 365, "availability 365"] = 365
      self.df.loc[self.df["availability_365"] < 0, "availability 365"] = 0
      self.df.loc[self.df["neighbourhood_group"] == "manhatan", "neighbourhood_group"] = "Manhattan"
      self.df.loc[self.df["neighbourhood_group"] == "brookln", "neighbourhood_group"] = "Brooklyn"
```

These methods hide the complexities of data cleaning and transformation behind a simple interface, allowing users to preprocess data without worrying about the implementation details.

## Decomposition
In generally we tried to follow up the single responsibility principle to enforce the decomposition as much as possible. 
That means we tried to identify all responsibilities and delegate them to single classes. So we decomposed parts of the whole software 
into smaller parts, which all have one single responsibility. That increases the cohesion and 
decrease coupling between software moduls.

### Example 1 Create a neighbourhood_selector
The class decomposes the preprocessing task into smaller, manageable parts represented by individual methods. Each method is responsible for performing a specific preprocessing step, such as dropping columns, cleaning invalid values etc. This decomposition enhances code readability, modularity and maintainability by breaking down a complex task into smaller, more understandable components. 

#### Example rating.py Class 
The task of selecting the group has been delegated to the neighbourhood_selector.py class. This achieves a clear division of tasks: rating.py is responsible solely for evaluating the DataFrame's ratings, while neighbourhood_selector.py is tasked with filtering the DataFrame according to the selected group and then passing it to the evaluation classes. <br>

Before Decomposition: <br>
rating.py 
```python
    def get_average_rating_per_nhood(self) -> pd.DataFrame:
        grouped = self.df.groupby('neighbourhood_group')
        average_ratings = grouped['review_rate_number'].mean()
        return average_ratings
```
After Decomposition: <br>
rating.py
```python
    def average_rating(self):
        """
        Returns:
            float: average rating
        """
        return round(self.df['review_rate_number'].mean(), 3)
```

### Example 2 neighbourhood visualizer
The neighbourhood visualizer capsules the responsibility of visualizing
information about the selected neighbourhood. 
The neighbourhood visualizer has only knowledge about 
the data which he has to visualize. Also does the neighbourhood visualizer not modify any data, he only visualizes the data.
The visualizer decomposes the visualizing part into smaller manageable parts represented by individual methods. 
With the Neighbourhood visualizer we achieve as well a clear separation of processing visualizations, which do not
contain complex logic parts and complex data calculations which need a lot of logical computations.

## Project Structure

The project was initially divided into various classes responsible for analyzing costs, availability, and ratings. The main class started Streamlit and displayed the UI. <br>

Old Project Structure: 
```bash
.
└── src
    ├── airbnb_summary.py
    ├── availability.py
    ├── main.py
    ├── price.py
    └── rating.py
```
Changes: <b>

 - Addition of pages: <br>
   Users should have the ability to make desired selections for the view in home.py. <br> The Overview page displays general information about all AirBnBs.
 - New Classes: <br>
        - data_preprocessor: Outsourcing the task of performing general data cleaning on the DataFrame. <br>
        - neighbourhood_selector: Outsourcing the task of selecting a specific neighborhood. <br>
        - neighbourhood_vizualizor: Outsourcing the task of visualizing information based on the selection of a neighborhood,               room type in home.py. <br>
        
Refactored Project Structure:
```bash
.
└── src
    └── pages
        └── overview.py  
    ├── airbnb_summary.py
    ├── availability.py
    ├── data_preprocessor.py
    ├── home.py
    ├── neighbourhood_selector.py
    ├── neighbourhood_vizualizer.py
    ├── price.py
    └── rating.py
```



