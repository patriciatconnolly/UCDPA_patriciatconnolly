# main file for assignment
print("above displays location of file 'main.py' saved")
print(" ")
# Importing Python Packages to use

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import datetime as datetime
import method

# Requesting an API "CBM03 - Detailed Daily Card Payments" from www.cso.ie
# request=requests.get('https://ws.cso.ie/public/api.jsonrpc?data=%7B%22jsonrpc%22:%222.0%22,%22method%22:%22PxStat.Data.Cube_API.ReadDataset%22,%22params%22:%7B%22class%22:%22query%22,%22id%22:%5B%5D,%22dimension%22:%7B%7D,%22extension%22:%7B%22pivot%22:null,%22codes%22:false,%22language%22:%7B%22code%22:%22en%22%7D,%22format%22:%7B%22type%22:%22CSV%22,%22version%22:%221.0%22%7D,%22matrix%22:%22CBM03%22%7D,%22version%22:%222.0%22%7D%7D')

# request=requests.get('https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CBM03/CSV/1.0/en')

# print(request.status_code)

# if request.status_code==200:
#   print("Success")
# else:
# print("Error")

data = pd.read_csv("https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/CBM03/CSV/1.0/en")
print("*****  log position 1 get api file   *****")
print("")
print("head of dataframe 'data':")
print(data.head())
print("")
print("describe: dataframe 'data':")
print(data.describe())
print("")
print("column names of dataframe 'data':")
print(list(data.columns))
print("test1")

print(data.count())
print(len(data.index))
data_count = len(data.index)
print("test2")

if data_count > 300:
    print("\n Count of rows in dataframe > 300")
else:
    print("\n Count of rows in dataframe =< 300")

print(type(data['Daily']))
print("")
from datetime import datetime

format_str = "%Y %B %d"
# data["Month"]=data[datetime.strptime(data['Daily'], format_str)]

#data['Month'] = data.apply(pd.to_datetime(data['Daily'], format=format_str), axis=1)
# new_df = data[['Statistic',pd.to_datetime(data['Daily'], format=format_str),'Daily and Seven Day Rolling Totals','UNIT','VALUE']].copy()
new_df = data[['Statistic', 'Daily', 'Daily and Seven Day Rolling Totals', 'UNIT', 'VALUE']].copy()

print("*****  log position 2 create new_df   *****  ")

pd.options.display.max_colwidth = 100
print("head of dataframe 'new_df':")
print(new_df.head())
print("")
print("column names of dataframe 'new_df':")
print(list(new_df.columns))
print("")
print("return of first five rows of column 'Daily and Seven Day Rolling Totals' in dataframe df_new:")
print(new_df['Daily and Seven Day Rolling Totals'].head())
print("")
print("describe df_new:")
print(new_df.describe())
print("")
print("shape of df_new:")
print("shape of new_df")
print(new_df.shape)
print("")
print("display how many fields have not available:")
print(new_df.isna().sum())
print(" ")
print("replace nan with 0")
print("log position 3 before replace nan with 0")

new_df2 = new_df.fillna({'VALUE': 0})
print("")
print("head of dataframe 'new_df2':")
print(new_df2.head())
print("")
print("check to ensure all fields have a value:")
print(new_df2.isna().sum())
print("log position 4 after replace nan with 0")

print(list(new_df2.columns))

new_df3 = new_df2[new_df2["Daily and Seven Day Rolling Totals"] == "Daily total"]
print(new_df3)

new_df3.set_index('Daily', inplace=True)
print("**********")
print(list(new_df3.columns))
print(new_df3.head())

debit_card_trans_atm = new_df3[new_df3["Statistic"] == "Debit Card Transactions - ATM Withdrawals"]
debit_card_trans_pos = new_df3[new_df3["Statistic"] == "Debit Card Transactions - Point of Sale"]

debit_card_trans = pd.concat([debit_card_trans_atm, debit_card_trans_pos])

# use of indexing
totals = ["Total value for Debit Card Transactions - ATM Withdrawals", "Total value for Debit Card Transactions - Point of Sale","Total value for Debit Card Transactions"]

print(totals[0],":", debit_card_trans_atm["VALUE"].sum())
print(totals[1],":", debit_card_trans_pos["VALUE"].sum())
print(totals[2],":", debit_card_trans["VALUE"].sum())

print("******index")

print(debit_card_trans_atm.shape)
print(debit_card_trans_pos.shape)
print(debit_card_trans.shape)
print(debit_card_trans.describe())

debit_card_vols_atm = new_df3[new_df3["Statistic"] == "Debit Card Volumes - ATM Withdrawals"]

debit_card_vols_pos = new_df3[new_df3["Statistic"] == "Debit Card Volumes - Point of Sale"]

debit_card_vols = pd.concat([debit_card_vols_atm, debit_card_vols_pos])
print(debit_card_vols_atm.shape)
print(debit_card_vols_pos.shape)
print(debit_card_vols.shape)
print("*****  debit cards   *****")

credit_card_trans_per = new_df3[new_df3["Statistic"] == "Credit Card Transactions - Personal Cards"]

credit_card_trans_bus = new_df3[new_df3["Statistic"] == "Credit Card Transactions - Business Cards"]

credit_card_trans = pd.concat([credit_card_trans_per, credit_card_trans_bus])

print(credit_card_trans_per.shape)
print(credit_card_trans_bus.shape)
print(credit_card_trans.shape)
print(credit_card_trans.describe())

credit_card_vols_per = new_df3[new_df3["Statistic"] == "Credit Card Volumes - Personal Cards"]

credit_card_vols_bus = new_df3[new_df3["Statistic"] == "Credit Card Volumes - Business Cards"]

credit_card_vols = pd.concat([credit_card_vols_per, credit_card_vols_bus])
print(credit_card_vols_per.shape)
print(credit_card_vols_bus.shape)
print(credit_card_vols.shape)
print("*****  credit cards   *****")

# daily_card_payments= new_df2.sort_values("Daily and Seven Day Rolling =Totals", ascending=[True])
# print(daily_card_payments.head())

# mask_rolling_totals = daily_card_payments.'Daily and Seven Day Rolling Totals' == 'Daily total'
# daily_total = daily_card_payments.loc[mask_rolling_totals]
# daily_total.describe(include='object')


print("\n")

print("Detailed Daily Card Payments file imported")

# import Retail Sales Index in csv file from CSO website call 'retail_sales' dataframe
# hardcoded filename without path
retail_sales = pd.read_csv("retail_sales_index_cso.csv")
print("*****  log position 5 read retail sales csv file   *****")

# Look at retail_sales

print(retail_sales.head())
print("")
print("column names of dataframe 'retail_sales':")
print(list(retail_sales.columns))
print("")
print("mapping for retail_sales")
print("")
# hardcoded filename without path
mapping = pd.read_csv("mapping.csv")
print(mapping.info())
print("*****  log position 6 read csv mapping   *****")

#iterrow example to print mapping reference table
for index, row in mapping.iterrows():
    print(row['C02583V03135'], row['NACE higher Group'])

#print(mapping)
print("")
new_retail_sales = retail_sales.merge(mapping, on=['C02583V03135'])
new_retail_sales.sort_values("TLIST(M1)", ascending=[True])
print("")
print("*****  log position 7 sorting     *****")

print(new_retail_sales.isna().sum())
print(new_retail_sales.head())
print(list(new_retail_sales.columns))
print(retail_sales.describe())

# create new df extract of retail_sales with date greater than 2019
retail_sales_20_21 = new_retail_sales[new_retail_sales['TLIST(M1)'] > 201912]
# retail_sales_20_21_grouped= retail_sales_20_21.sort_values("NACE higher Group")
print("")
print("*****  log position 8 filter retail sales file > 2019     *****")
retail_sales_20_21.drop(columns=['Month', 'NACE Group', 'UNIT'],
                        axis=1,
                        inplace=True)
print("")
print("log position 9 drop columns from df")
print(retail_sales_20_21.head())
print(list(retail_sales_20_21.columns))
print(retail_sales_20_21.describe())
print(retail_sales_20_21.shape)
print("position 10")

# List
year_value = ["FY 2020 totals value", "YTD 2021 totals value"]
print(year_value)
year2020 = retail_sales_20_21[retail_sales_20_21['TLIST(M1)'] < 202101]["VALUE"].agg('sum')
year2021 = retail_sales_20_21[retail_sales_20_21['TLIST(M1)'] > 201912]["VALUE"].agg('sum')
print("abc")

# tidy up
print(year_value[0])
print(year2020)

print(year_value[1])
print(year2021)
print("abc")
# if year2020>300:
#    print("\n Count of rows in dataframe > 300")
# else:
#    print("\n Count of rows in dataframe =< 300")


retail_sales_20_21_grouped = retail_sales_20_21.groupby(["TLIST(M1)", "NACE higher Group"])["VALUE"].agg('sum')
print(retail_sales_20_21_grouped)

print("position 11 group df with date and higher NACE code")
retail_sales_20_21_grouped.agg('sum').plot(kind='bar', y='VALUE')
# retail_sales_20_21.groupby(["TLIST(M1),"NACE higher Group"])["VALUE"].agg('sum').plot(kind='bar', y='VALUE')
# plt.show()
