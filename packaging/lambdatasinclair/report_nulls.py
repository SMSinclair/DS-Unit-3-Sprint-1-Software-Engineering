import pandas as pd 

def report_nulls(df):
    print('Number of (non-zero) null values')
    print('-'*41)
    for col in df.columns.values:
        if df[col].isnull().sum() > 0:
             print('{:<30} {:>10}'.format(col, df[col].isnull().sum()))