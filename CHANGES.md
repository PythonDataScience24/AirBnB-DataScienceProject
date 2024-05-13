# Structure and Code Improvements
## 1. Create a data_preprocessor class
### _Abstraction_
The class abstracts away the details of data preprocessing by providing methods like 
- 'drop_columns'
- 'standardize_datatypes_columns'
- 'clean_invalid_values'
- 'clean_missing_values'
- 'preprocess' 

These methods hide the complexities of data cleaning and transformation behind a simple interface, allowing users to preprocess data without worrying about the implementation details.
### _Decomposition_
The class decomposes the preprocessing task into smaller, manageable parts represented by individual methods. Each method is responsible for performing a specific preprocessing step, such as dropping columns, cleaning invalid values etc. This decomposition enhances code readability, modularity and maintainability by breaking down a complex task into smaller, more understandable components. 

## 2. (?e.g.?) Use the neighbourhood_visualizer

