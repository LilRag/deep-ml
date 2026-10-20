import pandas as pd

def solution(df1, df2, df3):
    result1 = pd.merge(df1,df2, on='emp_id', how ='inner')
    result2 = pd.merge(result1, df3, on ='emp_id', how='left')
    return result2 