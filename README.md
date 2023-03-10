# **S&P 500 RETURNS VS MOST RELEVANT STOCKS OF TOP SECTORS**



![This is an image](images/stonks.png)




The goal of this project is study which is the best way to invest your money in the US stock market. It is putting you money into a index like the S&P 500? Or the best way to go is investing on a leader company of one the best sectors of the US economy? We will find out based on the historical performace of the index & companies by:

- Create a function to import historical data of the stocks from an API.
- Import historical price data from the S&P 500 from a csv dowloaded in Kaggle.
- Create chart to explore the price evolution of the main companies in each sector.
- Explore if it exist similar patterns between the price evolution of the companies of the same sector.
- Finally, we are going to explore the difference of returns between the top stocks vs the S&P 500 index. What would have been the return for each dollar I would have invested?


We have used the following as our main sources of data: 

- **API**: https://site.financialmodelingprep.com/developer/docs/historical-stock-data-free-api/#Historical-Daily-Prices-with-change-and-volume
- **Kaggle S&P 500 Stocks**: https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks?select=sp500_index.csv 



## **1. Importing and Transforming Data from csv and API**

### **1.1 S&P 500 csv from Kaggle**

In this first step we have created a function to import the kaggle's csv and apply some transformations to it: 

- Modify the date column structure so we can match it with the API information.
- Renaming columns.
- Change datatypes.
- Calculate moving avergages of 30,50 and 100 days.


### **1.2 Stock price data from API (financialmodelingprep.com)**

With the API function we have created a way to easily get the historical price evolution from any company within the US stock market.
This function also calculates the moving averages for 30, 50 and 100 days ,as we did for the S&P index. We also perform similar modificantions to the df.

## **2 Data Exploration**

### **2.1 Exploration of the price evolution of companies in the same sector**

In this first part, we are going to have a quick look on the performance of the main companies for each of the main sectors. We have selected both companies and sectors based on the market cap.

After some research, we have found the top 3 companies of the top 3 sectors:

- **Technology**:
    - Apple (AAPL)
    - Microsoft (MSFT)
    - Alphabet (GOOG)


- **Heath Care**:
    - Johnson & Johnson (JNJ)
    - Elli Lilly (LLY)
    - Merk & Co (MRK)


- **Finance**: 
    - JPM (JPM)
    - Bank of America (BAC)
    - Visa (V)


#### **2.1.1 Technology**

Let's start with Technology stocks from jan 2018 to dec 2022 (Notice that we have normalized the price, so we can have a better look at the trends of the sector price performance)

As we can see in the graph, all the prices of the stocks have behaved similarly during this period.

![This is an image](images/Tech_3.png)

#### **2.1.2 Health Care**

As we can see in the Health Care stocks, they have behaved different but they have ended at the same point.

![This is an image](images/Healthcare_3.png)

#### **2.1.3 Finance**

In the Finance chart, we can see that they have been hit big with coronavirus, but thay have ended up with a little increase of the price. Looks like the Visa stock managed better the coronavirus period. Probably because it sells different product than JPM and Bank of America.

![This is an image](images/Finance_3.png)

### **2.2 Visualize Top Individual Stock Price Evolution for each sector**

For this part of the project, we are going to have a more personalized look of the top selected stocks for each sector:

- **JNJ**
- **AAPL**
- **V**

As you can see, we have added moving averages of the price for 30,50 and 100 trading days

#### **2.2.1 Johnson & Johnson chart**

![This is an image](images/jnj_chart.png)


#### **2.2.2 Apple price evolution chart**

![This is an image](images/apple_chart.png)


#### **2.2.3 Visa price evolution chart**

![This is an image](images/Visa_chart.png)


'''


## 3. **Stock comparison vs S&P500**

Finally, we are going to check the main goal of this project. Explore the return of the stock in the last years vs the one of an index 

**Note that:**
1. For this comparison, we have calculated the cumulative return from the dates selected. This represents the return per dollar!
2. We are not taking into account the dividents, we are just looking at the price of the stock and index. 

### **3.1 Johnson & Johnson**

In this first comparison, we can see that from 2018 to 2023, **the index has outperformed the Johnson & Johnson health care stock**

![This is an image](images/sp_jnj.png)


### **3.2 Apple**

As you can see in the graph, Apple has (by far!) outperformed the S&P 500 index. 

    - Apple has x3 each dollar invested, while the index has returned a 45% 

![This is an image](images/sp_apple.png)


### **3.3 Visa**

As we can see, visa has outperformed the index from the very beginning

![This is an image](images/sp_visa.png)


## **4. Conclusions**

Can we conclude that is is always better to invest in stocks than one of the best indexes like the S&P 500? 

We can't really say this, since we were looking at some of the best companies in the world. What if we take to companies that haven't perfomed that good over time? Let's look at two examples:

1. Let's take a look into Celanese "CE". This company is a global chemical and speciality materials company, but is what more improtant for us is that it is a "average" or "normal" company. As shown in the graph, we can see that if you invested on this company 5 years ago, you will have nearly non return, while with the S&P 500 you would have get a 40% return in the same period.

![This is an image](images/sp_ce.png)
 

2. META aka Facebook: This company has been one of the biggest ones in tech on the last decade, but as you can see in meta's graph, the performance has been poor.

![This is an image](images/sp_meta.png)

### **Final takeaways**
After this exploration, we can say that maybe the best (and safest) aproach is combine both so you can diversify your risks and returns, which helps to reduce the impact of market volatility on your portfolio. By allocating some of your investments in the S&P 500 index, you can benefit from the broad market exposure and potentially achieve a good return. On the other hand, investing in high-quality stocks provides an opportunity for higher returns but also carries a higher level of risk. By diversifying your investments between the two, you can balance the risk and return and improve the overall performance of your portfolio.


![This is an image](images/wolf.jpg)