# Basic DataFrame helper functions.

### Start with a DataFrame:

```
import pandas as pd
import numpy as np


df = pd.DataFrame({'people': ['Bob', 'John', 'Jane'],
                   'age': [40, 23, np.nan],
                   'eye_color': ['brown', np.nan, 'blue'], 
                   'birthday': ['07/08/1979', '01/06/96', '05/01/1998']})
```

## Generate a clean report of null values

### Use like this:

```
from report_nulls import report_nulls

report_nulls(df)
```

```
Number of (non-zero) null values
-----------------------------------------
age                                     1
eye_color                               1

```

## Separate dates into year, month and day columns.

``` 
Helper function to split dates into multiple columns in a pandas DataFrame. 
  
Takes a column of dates and creates new columns for year, month and day. 
Deletes input column unless you specify delete_original=False
  
Parameters: 
    X (DataFrame): DataFrame with column to be split
    column (Series): the column to be split
    max_year: four digit year, maximum year in column. To be used 
              when resolving two digit year ambiguity. Default = 2068.
    delete_original: drops column from X when True. Default = True.
  
Returns: 
    DataFrame: a DataFrame with the new columns added
```

### Use like this:

```
from split_dates import split_dates

df = split_dates(df, df.birthday)
```
```

   people   age    eye_color    year    month   day
0   Bob     40.0    brown       1979      7      8
1   John    23.0    NaN         1996      1      6
2   Jane    NaN     blue        1998      5      1

```