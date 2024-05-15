# Structure and Code Improvements
## Abstraction
### 1. Create a data_preprocessor class

The class abstracts away the details of data preprocessing by providing methods like 
- 'drop_columns'
- 'standardize_datatypes_columns'
- 'clean_invalid_values'
- 'clean_missing_values'
- 'preprocess'

#### Example rating.py Class 
The task of cleaning the DataFrame has been moved to the process_dataframe.py class. Consequently, data cleaning is performed at the same abstraction level as the class. The data cleaning in the rating.py class is now limited to class-specific cleanings.
Before Abstraction:
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

### 2. Create a neighbourhood_visualizer
The class decomposes the preprocessing task into smaller, manageable parts represented by individual methods. Each method is responsible for performing a specific preprocessing step, such as dropping columns, cleaning invalid values etc. This decomposition enhances code readability, modularity and maintainability by breaking down a complex task into smaller, more understandable components. 

#### Example rating.py Class 
The task of selecting the group has been delegated to the neighbourhood_selector.py class. This achieves a clear division of tasks: rating.py is responsible solely for evaluating the DataFrame's ratings, while neighbourhood_selector.py is tasked with filtering the DataFrame according to the selected group and then passing it to the evaluation classes.

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



