import pandas as pd 

def split_dates(X, column, max_year=2068, delete_original=True):
    """ 
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
  
    """
    # Create datetime column and extract features
    X['date_dt'] = pd.to_datetime(column, infer_datetime_format=True)
    X['year'] = X['date_dt'].dt.year.apply(lambda x: x if x < max_year 
                                           else x - 100)
    X['month'] = X['date_dt'].dt.month
    X['day'] = X['date_dt'].dt.day

    # Drop the created column and the original if specified
    if delete_original==True:
        X = X.drop(columns=column.name)
       
    X = X.drop(columns='date_dt')
    return X