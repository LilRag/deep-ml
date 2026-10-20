import pandas as pd

def solution(df):
    # name , date , value 
    # trim whitespace ffrom name, only first letter capital 
    # convert date to yyyymmdd format
    # keep only unique rows 
    # fill missing values with mean 

    df['name'] = df['name'].str.strip().str.title()
    df['date'] = pd.to_datetime(df['date'].astype(str).str.strip()).dt.strftime('%Y-%m-%d')
    df = df.drop_duplicates(keep='first').reset_index(drop=True)
    df['value'] = df['value'].fillna(df['value'].mean())
    
    return df

