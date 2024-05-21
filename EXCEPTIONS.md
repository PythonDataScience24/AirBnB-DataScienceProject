# Exception handling

### Chosen place for try-except block
For the implementation of the try-except block,  home.py -> Home.try_init_neighbourhood_selector() was chosen.
The rationale is, this is the place where one try-except block may have the biggest impact.
It tries to construct the NeighbourhoodSelector, which is a crucial part of the dashboard, since
it allows the user to select a neighbourhood and see the data for that neighbourhood and provides the 
data frame fort the shown stats and plots. If the NeighbourhoodSelector cannot be constructed, nothing on the
home page can be shown, the user would only see a cryptic error message.

The part that most likely can fail is the loading of the data frame in the constructor of the neighbourhood selector.
The try catch block was not implemented in the constructor of the neighbourhood selector,
since the constructor can not interact with streamlit directly and therefore cannot show an error message to the user.

### Exception handling strategy
The strategy is to catch all exceptions that can occur during the construction of the neighbourhood selector.
Since without data, the dashboard is useless and cant show anything, there is no simple way to recover from this error.
Instead, a user-friendly error message is shown to the user, that explains that the data could not be loaded and what next steps might be to fix the issue.

### Handled exceptions
- FileNotFoundError: If the data file is not found, the user is informed to run the data preprocessor script first.
- ValueError: If the data file is empty or somehow corrupted, the user is informed to run the data preprocessor script again.
- MemoryError: If the data file is too large to be loaded into memory, the user is informed to close other programs to free up memory.
- Exception: If any other exception occurs, the user is informed that an unknown error occurred and to contact the developers.