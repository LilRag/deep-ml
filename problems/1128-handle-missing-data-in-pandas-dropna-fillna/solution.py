import pandas as pd

def solution(df):
    # drop colummn whose fraction of missing values greater than 0.5
    # drop any row if fraction of missing values greater than 0.5

    # fill the remaining missing values, 
    # numeric -> mean 
    # non numeric -> mode 

    # drop columns with > 50% missing values (axis = 0 is default)
    df_cleaned = df.loc[:, df.isna().mean() <= 0.50]
    # drop rows with > 50% missing values across remaining columns 
    df_cleaned_1 = df_cleaned.loc[df_cleaned.isna().mean(axis = 1) <= 0.50, :].copy()

    
    num_cols = df_cleaned_1.select_dtypes(include ='number').columns
    cat_cols = df_cleaned_1.select_dtypes(exclude ='number').columns


    if len(num_cols) >0:
        df_cleaned_1[num_cols] = df_cleaned_1[num_cols].fillna(df_cleaned_1[num_cols].mean())

    if len(cat_cols) >0:
        df_cleaned_1[cat_cols] = df_cleaned_1[cat_cols].fillna(df_cleaned_1[cat_cols].mode().iloc[0])

    
    return df_cleaned_1