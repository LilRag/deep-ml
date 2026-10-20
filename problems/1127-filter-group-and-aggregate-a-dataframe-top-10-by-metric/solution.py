import pandas as pd

def solution(df):
    # region , product, status, amount 
    # keep only rows whose status is complete 
    # group remaining rows by region and compute total amount for each region 
    # sort by descening order of totals , max 10 

    df_filter = df[df["status"] == "completed"]
    totals = df_filter.groupby("region", as_index = False)["amount"].sum()


    result = (
        totals.sort_values("amount", ascending = False).head(10).reset_index(drop= True)
    )

    return result