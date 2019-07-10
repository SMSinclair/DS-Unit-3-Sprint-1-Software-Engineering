# Basic DataFrame helper functions.

Start with a DataFrame.

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
from placeholder import something

report_nulls(df)
```

```
Number of (non-zero) null values
-----------------------------------------
age                                     1
eye_color                               1

```

## Separate dates into year, month and day columns.

### Use like this:

```
from placeholder import something

df = split_dates(df, df.birthday)
```
```

   people	age	   eye_color	year	month	day
0	Bob	    40.0	brown	    1979	  7	     8
1	John	23.0	NaN	        1996	  1	     6
2	Jane	NaN	    blue	    1998	  5	     1

```