## IMPORTING 

import pandas as pd
from pandas import json_normalize

import requests 
import json
import os
import numpy as np

# Visualization 
import plotly.express as px

#dontenv
from dotenv import load_dotenv 





## Function 1: Importing and Transforming S&P 500 csv





def import_and_transform_sp500():
    # Importing csv
    sp500_df = pd.read_csv("HistoricalData_S&P500.csv")

    #creating new date format
    sp500_df["date"] = sp500_df["Date"].str[6:] + "-"  + sp500_df["Date"].str[:2] + "-" + sp500_df["Date"].str[3:5]

    # dropping unwanted columns
    sp500_df = sp500_df.drop(["Volume","Date"],axis=1)

    # changing column names
    sp500_df = sp500_df.rename(columns={"Close/Last":"sp500_price",
                                        "Open":"sp500_open",
                                        "High":"sp500_high",
                                        "Low":"sp500_low"})

    # Creating column with the name
    sp500_df["company"] = sp500_df["company"] = "sp500"

    #To date type
    sp500_df['date'] = pd.to_datetime(sp500_df['date'])

    # Sorting values
    sp500_df.sort_values(by="date", inplace=True)

    #Moving date column to the begginig
    first_column = sp500_df.pop("date")
    sp500_df.insert(0,'date',first_column)

    # Creating Moving Average columns

    sp500_df["sp500_MA50"] = sp500_df["sp500_price"].rolling(50).mean()
    sp500_df["sp500_MA30"] = sp500_df["sp500_price"].rolling(30).mean()
    sp500_df["sp500_MA100"] = sp500_df["sp500_price"].rolling(100).mean()
    
    return sp500_df



## Function 2: Get stock and Transform data




def get_stock(TICKER):
    
    load_dotenv()

    api_key = os.getenv('api_key') 

    url = (f"https://financialmodelingprep.com/api/v3/historical-price-full/{TICKER}?apikey={api_key}")

    #Perform the request

    data = requests.get(url)
    symbol = data.json()

    #json_normalize: https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
    dataframe_1 = json_normalize(symbol)

    # Creating the df
    list_1 = list(dataframe_1["historical"])
    data = list_1[0]
    df = pd.DataFrame(data)
    
    df["changePercent"] = df["changePercent"] / 100


    # Renaming columns
    df = df.rename(columns={"close":f"{TICKER}_price",
                                    "open":f"{TICKER}_open",
                                    "changePercent":f"{TICKER}_change_percentage",
                                    "high":f"{TICKER}_high",
                                    "low":f"{TICKER}_low",
                                    "vwap":f"{TICKER}_vwap",
                                    "unadjustedVolume": f"{TICKER}_volume"},)
    
    # Changing date data-type
    df['date'] = pd.to_datetime(df['date'])
    
    
    # Adding column with the company name
    df["company"] = df["company"] = f"{TICKER}"
    
    # filtering date
    df = df[df["date"] > "2013-02-04"]
    df.sort_values(by="date", inplace=True)
    
    # dropping unwanted columns 
    df = df.drop(["label","changeOverTime","change","adjClose"],axis=1)
    
    # Moving average
    
    df[f"{TICKER}_MA50"] = df[f"{TICKER}_price"].rolling(50).mean()
    df[f"{TICKER}_MA30"] = df[f"{TICKER}_price"].rolling(30).mean()
    df[f"{TICKER}_MA100"] = df[f"{TICKER}_price"].rolling(100).mean()
    
    
    # Moving company name to the first position
    first_column = df.pop("company")
    df.insert(0,'company',first_column)
    
    return df





## Function 3: Visualize Individual Stock Price Evolution




def stock_price_evolution(TICKER,start_date,end_date):
    
    # Getting the data
    
    df = get_stock(TICKER)
    
    # Filtering by date

    graph = df[df["date"].isin(pd.date_range(start_date, end_date))]

    # Selecting columns
    graph = graph[["date",f"{TICKER}_price",f"{TICKER}_MA30",f"{TICKER}_MA50",f"{TICKER}_MA100"]]
    graph.set_index("date",inplace=True)

    # Plotting

    fig = px.line(graph,width=1000, height=500)
    #fig.title=(f"S&P500 vs {TICKER} Return Evolution for each $",size=30)
    fig.update_layout(
    title={
        'text': f"{TICKER} Stock Price Chart",
        'y':0.9,
        'x':0.4,
        'xanchor': 'right',
        'yanchor': 'top'})
                  
    fig.show()   





## Function 4: Compare S&P500 returns vs Stock 





def sp500_vs_stock_returns(TICKER,start_date,end_date):
    # STOCK INFO UPLOAD 

    stock_df = get_stock(TICKER)

    # Sorting and selecting dates
    stock_df.sort_values(by="date", inplace=True)
    stock_df = stock_df[stock_df["date"].isin(pd.date_range(start_date, end_date))]

     ## Returns with shift (https://www.geeksforgeeks.org/python-pandas-dataframe-shift/) + Cumulative returns
    stock_df[f"{TICKER}_returns"] = (stock_df[f"{TICKER}_price"]/stock_df[f"{TICKER}_price"].shift(1)) - 1
    stock_df[f"{TICKER}_cumulative_returns"] = (1 + stock_df[f"{TICKER}_returns"]).cumprod()

    # S&P500 INFO UPLOAD
    
    sp500_df = import_and_transform_sp500()
    
    # Sorting and selecting dates
    sp500_df.sort_values(by="date", inplace=True)
    sp500_df = sp500_df[sp500_df["date"].isin(pd.date_range(start_date, end_date))]
    
    ## Setting Returns & Cumulative returns
    sp500_df["sp500_returns"] = (sp500_df["sp500_price"]/sp500_df["sp500_price"].shift(1)) - 1
    sp500_df["sp500_cumulative_returns"] = (1 + sp500_df["sp500_returns"]).cumprod()
    
    # CREATING FINAL DF
    
    stock = stock_df[["date",f"{TICKER}_cumulative_returns"]]
    sp500 = sp500_df[["date","sp500_cumulative_returns"]]
    
    # Merging 
    
    merged_df = stock.merge(sp500,on="date",how="left")
    merged_df.set_index("date",inplace=True)

    
    # Plotting
    
    fig = px.line(merged_df,width=1200, height=800)
    #fig.title=(f"S&P500 vs {TICKER} Return Evolution for each $",size=30)
    fig.update_layout(
    title={
        'text': f"S&P500 vs {TICKER} Return Evolution for each $",
        'y':0.9,
        'x':0.4,
        'xanchor': 'right',
        'yanchor': 'top'})
                  
    fig.show()




## Function 5: Comparing Price Evolution of Three Stocks (Normalized)




def compare_three_stocks(TICKER_1,TICKER_2,TICKER_3,start_date,end_date):

    # Getting data from API

    df_1 = get_stock(TICKER_1)
    df_2 = get_stock(TICKER_2)
    df_3 = get_stock(TICKER_3)


    # Setting the table

    merge_df_1 = df_1[["date",f"{TICKER_1}_price"]]
    merge_df_2 = df_2[["date",f"{TICKER_2}_price"]]
    merge_df_3 = df_3[["date",f"{TICKER_3}_price"]]

    new_df_1 = merge_df_1.merge(merge_df_2,on="date",how="left")
    df = new_df_1.merge(merge_df_3,on="date",how="left")

    # Filtering by date

    #df = df[df["date"] > "2015-12-31"]

    df = df[df["date"].isin(pd.date_range(start_date, end_date))]


    df.set_index("date",inplace=True)

    # Normalization

    for column in df.columns:
        df[column] = df[column]  / df[column].abs().max()

    fig = px.line(df,width=1000, height=500)
    #fig.title=(f"S&P500 vs {TICKER} Return Evolution for each $",size=30)
    fig.update_layout(
    title={
        'text': f"{TICKER_1} & {TICKER_2} & {TICKER_3} Price Chart (Normalized)",
        'y':0.9,
        'x':0.4,
        'xanchor': 'right',
        'yanchor': 'top'})

    return fig.show()